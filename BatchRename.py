"""
    Batch renames all the files present inside the given directory.

    Inputs can supplied as runtime arguments, or will be requested by the script
    at runtime under interactivate mode.
"""

import string
from enum import Enum, auto
from io import TextIOWrapper
from os import listdir, rename
from os.path import abspath, basename, isdir, isfile, join
from pathlib import PurePosixPath
from re import Match, match
from sys import argv
from time import sleep
from typing import Dict, List


class Mode:
    """
        An enum to indicate the mode to be used while generating randomized
        strings.

        Values
        -------
        safe: Indiactes the safe randomization mode. Lesser chances of collisions.
        Neglibibly more resource-expensive. \n
        fast: Indicates the fast randomization mode. A bit higher chances of
        collisions - in exchange of being more resource efficient. \n
    """

    # Using string values to ensure that the input term for these variables
    # can be simply changed from in here to reflect the changes across the
    # entire script.
    safe = 'safe'
    fast = 'fast'


class SelectionMode:
    """
        Enum used to indicate the scope within which files are to be selected and renamed.

        Values
        -------
        direct: Only those files that are present directly in the given directory are to
        be renamed. Files that present in any sub-directories inside the root directory
        will be ignored. \n
        recursive: Indicates all the files that are present anywhere inside the root
        directory are to be included. \n
    """

    direct = 'direct'
    recursive = 'recursive'


class Extension(Enum):
    """
        Enum to indicate the process that is to be used while *estimating*
        file extensions.

        Remarks
        --------
        Under the `hard` mode, any text present after the last period
        (full-stop) will be assumed to be the file-extension. Any text present
        in the file name except this part will be renamed.

        Under `soft` mode, anything present in the file name after the first
        period will be treated as the file extension.

        In case of a file named 'test.file.here.txt', `hard` mode will pick up
        '.txt' as the file extension, whereas, `soft` mode will identify
        '.file.here.txt' as the file extension.

        As a downside, hard mode will identify '.gz' as the file extension for
        files having '.tar.gz' as the extension - meaning that the file will be
        randomly renamed to say `1sFlmd.gz`, this could have negative
        consequences in some scenario(s).

        Values
        -------
        soft: Anything in the file title placed after the first period [full-stop]
        will be treated as the file extension. This is useful in cases where files
        have custom extensions or if the file is supposed to have multiple extensions
        (such as `.tar.gz`). \n
        hard: Only the text present after the last period in the file name will
        be treated as the file extension.  \n
    """

    soft = auto()
    hard = auto()


# A dictionary taht will contain the original full paths of the files as the keys
# and the new names (including the rest of the path) as values - will be used to
# list down the original names and the new file paths as a text file.
name_pairs = {}

# String containing the name of the file that will contain a list of all the
# original names and the new names they were mapped to.
original_names_file_title: str = 'Original Names.txt'

# String containing the value that is supposed to be used as equal-to
# sign in the text file.
#
# Note: It is recommended that the equality symbol have at least one
# '/' (forward-slash) symbol to avoid mixing it with the file names
# this is being used since most OS do not allow file/directories to have
# a forward slash in their name.
equality: str = '--//-->'


def randomize(*, string_length: int, mode: Mode, charset: str) -> str:
    """
        Generates random strings and returns them.

        Parameters
        -----------
        string_length: The length of random string that is to be generated. \n
        mode: Defines the mode that should be used for generating random strings. \n
        include_digits: Optional. Boolean defining whether numbers should be included in
        the random strings that are generated. \n

        Returns
        --------
        A string of random characters having length equal to the value of `string_length`.
    """

    if mode == Mode.safe:
        import secrets

        # Generating a random string of `string_length` characters and returning the same.
        return ''.join(secrets.choice(charset) for i in range(string_length))
    elif mode == Mode.fast:
        import random

        # Generating a random string of `string_length` characters and returning the same.
        return ''.join(random.choices(charset, k=string_length))


def generate_names(root: str, name_length: int, charset: str, extension_criteria: Extension,
                   *, randomization_mode: Mode, dump_file: TextIOWrapper, recurse: bool = True):
    """
        The main method that internally fetches random strings can applies them as file name

        Parameters
        -----------
        root: Path of the root directory inside which files are to be renamed. \n
        name_length: Integer indicating the length of random strings which are to be used
        as file names. \n
        charset: String containing the character set that is to be used to generate random strings. \n
        extension_criteria: The criteria that is to be used to pick extensions from file names. \n
        randomization_mode: Randomization mode to be used to generate random strings. \n
        dump_file: IO wrapper pointing to the open dumps file where the mappings between old and new
        names will be placed. \n
        recurse: Optional. Boolean indicating if this method is to be recursively run for every directory
        found inside the root or not. Default: True. \n
    """

    global equality

    # A dictionary to contain mappings between the original file titles, and the new file titles.
    #
    name_pairs = {}

    # Iterating through all items present in the given directory
    for item in sorted(listdir(root)):

        # If the current item is a directory, and recursion is allowed calling
        # this method on the directory recursively.
        if isdir(join(root, item)):
            if recurse is True:
                # The new results will be appended to the same file.
                generate_names(
                    root=join(root, item),
                    name_length=name_length,
                    charset=charset,
                    extension_criteria=extension_criteria,
                    dump_file=dump_file,
                    randomization_mode=randomization_mode,
                    recurse=recurse
                )

            # Skipping the rest of the loop to avoid renaming the directory.
            continue

        # Getting the extension from the filename.
        ext: str = ''
        if extension_criteria == Extension.hard:
            ext = item.rpartition('.')[-1]
        else:
            ext = ''.join(PurePosixPath(item).suffixes).strip('.')

        # Generating a random title of the specified length and attaching file
        # extension to the title.
        new_title = '{0}.{1}'.format(
            randomize(
                string_length=name_length,
                mode=randomization_mode,
                charset=charset
            ),
            ext
        )

        # Converting item name to be the full path to the item.
        item = join(root, item)

        # Forming full path for the file using the randomized title.
        new_title = join(root, new_title)

        try:
            # Renaming the file, and appending the entry to the text file.
            rename(item, new_title)
            dump_file.write(f'{item} \t{equality}\t {new_title} \n')
        except Exception as e:
            print(f'''
                Error: Ran into an exception.

                Type: {type(e)}
                Error: {str(e.args)}
            ''')

    return name_pairs


if __name__ == '__main__':
    # Initialze all values to empty string for now. These variables will later be resorted
    # to their defaults.
    root: str = ''
    name_length: int = 10
    character_set: str = 'alphanumeric'
    randomization: Mode = ''
    operation_mode: str = 'auto'
    selection_mode: SelectionMode = ''
    extension_selection: Extension = ''

    # The regex patterns being used to extract information from incoming arguments.
    # If a value is to be extracted, it will be extracted from the FIRST group
    # found by `re.match`.
    #
    # As a programming choice, designing ALL patterns such that they optionally allow
    # double quotes.
    #
    # Accepting ANY value as the choice in the patterns. If this value is incorrect, the
    # script will enter interactive mode and fetch correct input.
    pattern_root = r'^--root="?(.+)"?$'
    pattern_randomization = r'^--randomization="?(safe|fast)"?$'
    pattern_selection_strategy = r'^--(recursive|direct)$'
    pattern_file_length = r'^--title-length=(\d+)$'
    pattern_character_set = r'^--charset=(lowercase|uppercase|numeric|alphanumeric|alphabet)$'
    pattern_extensions = r'^--extensions="?(hard|soft)"?$'

    # Checking for parameters passed while running the script.
    for arg in argv[1:]:
        # Iterating through every argument after the first - the first argument being the
        # name of the python script, and is being skipped.
        #
        # Allowing a match only if the parameter hasn't been filled already -- each parameter
        # can be filled at most once.
        if match(pattern_root, arg):
            root = match(pattern_root, arg).groups()[0]
        elif match(pattern_randomization, arg):
            randomization = match(pattern_randomization, arg).groups()[0]

            randomization = Mode.safe if randomization == 'safe' else Mode.fast
        elif match(pattern_selection_strategy, arg):
            selection_mode = match(pattern_selection_strategy, arg).groups()[0]

            selection_mode = SelectionMode.recursive if selection_mode == 'recursive' else SelectionMode.direct
        elif match(pattern_file_length, arg):
            name_length = int(match(pattern_file_length, arg).groups()[0])

            if name_length <= 7:
                print('Error: New titles need to have a length of 8 characters or more')
                exit(10)
        elif match(pattern_character_set, arg):
            # Mapping char-set later, this value has to be printed, after which it will be mapped
            # to the correct input type.
            character_set = match(pattern_character_set, arg).groups()[0]
        elif extension_selection == '' and match(pattern_extensions, arg):
            extension_selection = match(pattern_extensions, arg).groups()[0]

            extension_selection = Extension.hard if extension_selection == 'hard' else Extension.soft
        else:
            # If the parameter can't be matched to the existing patterns, flagging it.
            print(f'Error: Unwanted parameter `{arg}`')
            exit(10)

        if operation_mode == '':
            # If even a single parameter has been supplied, making the script switch to manual mode.
            # Doing this only if the operation mode hasn't been set already (to avoid over-writing
            # a value of `auto` mode).
            operation_mode = 'manual'

    if operation_mode != 'manual':
        # If the operation mode is not manual, by default it shall be auto.
        operation_mode = 'auto'

    # The regex pattern ensures all parameters will be non-null (and belong in the expected)
    # range when required. Can directly validate them.

    if root != '' and not isdir(root):
        # If the root is incorrect, flagging it up. Validating the root over here since this
        # will resort to manual input if the root is incorrect.
        print(f'Error: Path Incorrect \nThe path supplied does not point to a directory:\
            \n\t{root}')
    elif root == '':
        # If the root does not have a value (yet), asking the user for one.
        while True:
            print(f'Full path to the root directory \n\nroot>', end=' ')
            root = str(input())

            if isdir(root):
                # Breaking out of the loop if the path is correct.
                break

            print(f'Error: Invalid path detected')

    # Converting relative path to absolute path.
    root = abspath(root)

    print(f'''
        Configurations

        Root: `{root}`
        Selection Mode: `{selection_mode}`
        Randomization Mode: `{randomization}`
        Title Length: `{name_length}`
        CharSet: `{character_set}`
        Extension Selection: `{extension_selection}`\n
    ''')

    for i in range(5, -1, -1):
        print(f'Initializing the script in {i} seconds\r', end='')
        sleep(1)

    print('\n')

    # Mapping the character set as needed.
    if character_set == 'alphabet':
        character_set = string.ascii_letters
    elif character_set == 'lowecase':
        character_set = string.ascii_lowercase
    elif character_set == 'uppercase':
        character_set = string.ascii_uppercase
    elif character_set == 'numeric':
        character_set = string.digits
    elif character_set == 'alphanumeric':
        character_set = string.ascii_letters + string.digits

    with open(original_names_file_title, 'w') as dumps:
        # Finally, renaming the files as needed.
        generate_names(
            root=root,
            name_length=name_length,
            charset=character_set,
            extension_criteria=extension_selection,
            randomization_mode=randomization,
            dump_file=dumps,
            recurse=True if selection_mode == SelectionMode.recursive else False
        )
