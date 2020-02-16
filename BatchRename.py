"""
    Batch renames all the files present inside the given directory.

    All the inputs required are taken at the runtime.
"""

import os
from enum import Enum, auto
from os.path import basename, isdir, isfile, join
from pathlib import PurePosixPath
from typing import Dict, List


class Mode:
    """
        An enum to indicate the mode to be used while generating randomized
        strings.

        Values
        -------

        safe : Lesser chances of collisions. But is more resource-expensive\n
        fast : Relatively more chances of collisions, but will be faster and
        consume lesser resources
    """

    # Using string values to ensure that the input term for these variables
    # can be simply changed from in here to reflect the changes across the
    # entire script.
    safe = 'safe'
    fast = 'fast'


class SelectionMode(Enum):
    """
        An enum that will be used to indicate the files that are to be selectively 
        read and renamed.

        Values
        -------
        direct: Indicates that only those files that are present directly in the given 
            directory are to be selected. Files that present in any sub-directories of
            the given directory will be ignored\n
        recursive: Indicates that all the files that are present anywhere inside the given
            directory are to be included. Files present in any sub-directory inside the 
            given directory will also be included\n
    """

    direct = auto()
    recursive = auto()


class PickExtension(Enum):
    """
        An enum used to indicate the process that is to be used while choosing 
        the file extensions.

        Remarks
        --------
        The `hard` mode should be used if the file titles have multiple (periods) full
        -stops and they do not signify the file extension. The `soft` mode should be used
        if everything after the first period (full-stop) in the file title should be 
        treated as the file title.

        In a file named 'test.file.here.txt', `hard` mode will pick up '.txt' as the
        file extension, whereas, `soft` mode will identify '.file.here.txt' as the 
        file extension.

        In another scenario, hard mode will identify '.gz' as the file extension 
        for files having '.tar.gz' as the extension.

        Some precaution is recommended while selecting the mode.

        Values
        -------
        soft: Anything from the file name that is placed after the first period
            [full-stop] will be selected as the file extension. This is useful in
            cases where files have custom extensions or if the file is supposed to 
            have multiple extensions (such as `.tar.gz` files and more)\n
        hard: Anything that is placed after the last period in the file name will
            be selected as the file extension. This means that in case of files 
            having extensions such as `.tar.gz`, only `.gz` will be selected as the 
            file extension and the rest will be removed.
    """

    soft = auto()
    hard = auto()


# This dictionary will contain the original full paths of the files as the keys
# and the new names (including the rest of the path) as values.
name_pairs = {}

# The default length of the random string that is generated.
fixed_length: int = 15

# The default mode that is to be used to generate random strings.
randomize_mode: Mode = Mode.fast

# The default strategy that is to be used while selecting the files
# that are to be renamed.
selection_mode: SelectionMode = SelectionMode.recursive

# Boolean indicating if digits are to be included while generating random names.
use_digits: bool = False

# String containing the name of the file that will contain a list of all the
# original names and the new names they were mapped to.
original_names_file_title: str = 'Original Names.txt'

# String containing the value that is supposed to be used as equal-to
# sign in the text file.
#
# Note: It is recommended that the equality symbol have at least one
# '/' (forward-slash) symbol to avoid mixing it with the file names.
equality: str = '--//-->'


def randomize(*, string_length: int, mode: Mode, include_digits: bool = use_digits) -> str:
    """
        Generates random names and returns them in the form of a string.

        The default length will be `fixed_length` characters and can be changed by
        supplying the optional parameter with the desired length.

        Parameters
        -----------
        string_length :
            The length required for the resulting string. Defaults to the value 
            of `fixed_length` characters.\n
        mode:
            Defines the mode that should be used for generating random strings.
            Defaults to the value of `default_mode` variable.\n
        include_digits:
            Optional. Boolean defining whether numbers should be included in
            the random strings that are generated. Defaults to `use_digits`\n

        Returns
        --------
        A string of random characters having length equal to the value of `string_length`.
    """

    # This module will be used to chose the characters that are a part of the randomly
    # generated string. Can also be used to include digits if required.
    import string

    # This string will be used to decide the characters that can be included in the random
    # string. Adding the upper case and lower case characters by default.
    random_restrictions: str = string.ascii_letters
    if include_digits is True:
        # Adding numbers to this string if required.
        random_restrictions += string.digits

    if mode == Mode.safe:
        import secrets

        # Generating a random string of `string_length` characters and returning the same.
        return ''.join(secrets.choice(random_restrictions) for i in range(string_length))
    elif mode == Mode.fast:
        import random

        # Generating a random string of `string_length` characters and returning the same.
        return ''.join(random.choices(random_restrictions, k=string_length))


def list_files(root: str) -> List[str]:
    """
        Fetches a list of all the files that are present in the directory at the given path.

        The list will contain strings with each string being the full path of a file located
        in the directory. Any directories present will be ignored.

        Remarks
        --------
        This function will list the files that are located directly inside the root directory.

        In simpler terms, this is a non-recursive method and won't list the files that are
        present in a sub-directory inside the parent directory.

        Parameters
        -----------
        path: 
            A string containing the full path for the directory.

        Exceptions
        -----------
        os.Error: Raised in case of invalid path or inaccessible path provided\n
        os.FileNotFoundError: Thrown if the file does not exist or if the root points to 
            a file instead of a directory\n

        Returns
        --------
        A list of strings with each string containing the full path of a file present in the directory.
    """

    if isfile(root):
        raise FileNotFoundError(
            'The path points to a file instead of a directory')

    return [join(root, file) for file in os.listdir(root) if isfile(join(root, file))]


def list_directories(root: str) -> List[str]:
    """
        Returns a list of all the directories present inside the given directory.

        Fetches a list of all the items present in the given directory, removes all
        the files from this path and returns the remaining directories in a list.

        Remarks
        --------
        This function will return a list of strings containing the full paths of the
        directories present directly inside the given directory. Any of the
        sub-directories that are present in a child directory of the main directory shall
        not be a part of the results.

        tl;dr --> This method is not-recursive and simply provides a list of directories present
                directly inside the parent directory.

        Parameters
        -----------
        root: 
            String containing the full path of a directory.

        Exceptions
        -----------
        os.Error: Thrown if the path is invalid or if the application is unable to access
                the given location\n
        os.FileNotFoundError: Thrown if the path supplied points to a file instead of a
                directory or if the path itself is incorrect\n

        Returns
        ---------
        A list of strings with each string containing the full path of a directory present
        inside the given directory.
    """

    if isfile(root):
        raise FileNotFoundError(
            'The path points to a file instead of a directory.')

    return [join(root, file) for file in os.listdir(root) if (isdir(join(root, file)))]


def generate_names(root: str, extension_criteria: PickExtension, *,
                   selection_mode: SelectionMode = selection_mode) -> Dict[str, str]:
    """
        Prepares the final list of random names that are to be applied to the files.

        This method will also be responsible for populating the `name_pairs` 
        dictionary with data.

        The key in the dictionary will be a string containing the full path of the file 
        with the original name of the file, while the value will be a string containing 
        the full path of the file with the new (random) name that is to be applied.

        Also, this method does not renames the files or modify them in any manner, it simply
        fetches the random names that are to be applied to the files and adds this data to the 
        dictionary.

        Remarks
        --------		
        The extensions of the files will remain unchanged. Only the titles shall be changed.

        Parameters
        -----------
        root: 
            A string containing the path of the directory in which the files are to be renamed\n
        rename: 
            Optional. An enum object of the class `SelectFile` indicating the type of 
            strategy that is to be used while selecting the files that are to be renamed.

        Exceptions
        -----------
        os.Error: The parent exception that will be thrown if any exceptions are raised while dealing
            with the files\n
        os.FileNotFoundError: Thrown if the value of `root` is invalid or if the path points to a file
            instead of a directory\n

        Returns
        --------
        Returns the dictionary `name_pairs`. Since the dictionary is also global, it can always be 
        directly accessed if required.
    """

    if isfile(root):
        raise FileNotFoundError(
            'The path supplied belongs to a file instead of directory.')

    # Iterating through every file that is present in the given directory
    for orig_title in list_files(root=root):
        # A boolean that will be used to indicate if the name of any file is already
        # present in the dictionary or not.
        is_set: bool = False

        new_title: str = None

        for title in name_pairs.keys():
            if basename(orig_title).lower() == basename(title).lower():
                # If the file name is the same as the original name of some other file
                # in the parent directory, the using the same name new name for this file.
                new_title = join(root, basename(name_pairs[title]))
                is_set = True

        if not is_set or new_title == None:
            # Getting the extension of the file.
            ext: str = ''
            if extension_criteria == PickExtension.hard:
                ext = orig_title.rpartition('.')[-1]
            else:
                ext = ''.join(PurePosixPath(orig_title).suffixes)

            # Generating a random title of the specified length and attaching file
            # extension to the title.
            new_title = '{0}.{1}'.format(
                randomize(
                    string_length=fixed_length,
                    mode=randomize_mode,
                    include_digits=use_digits
                ),
                ext
            )

            # Forming full path for the file using the randomized title.
            new_title = f'{os.path.join(os.path.split(orig_title)[0], new_title)}'

        # Adding the full path with original title as key to the dictionary and
        # the full path of the file with new title as the value.
        name_pairs[orig_title] = new_title

    # If the file selection mode is set as recursive, running the method for every sub-directory.
    if selection_mode == SelectionMode.recursive:
        for directory in list_directories(root):
            generate_names(
                root=directory,
                extension_criteria=extension_criteria,
                selection_mode=selection_mode
            )

    return name_pairs


if __name__ == '__main__':
    # Helpful message before starting the actual script :p
    print('Go through the ReadMe file for the project to get an idea on how to use this script')

    root: str = ''
    while True:
        # Infinite loop. Will break out of it only when a valid path is entered as input.
        root = input('Enter the full path for the root directory: ').strip()

        if not isdir(root):
            # If the path is invalid, printing an error message. The loop will simply
            # ask for the root path until a valid path is selected as the root
            print(
                f'Entered path `{root}` is invalid or is not a directory.',
                'Enter a valid path ://\n',
                sep='\n'
            )
        else:
            # If the path is valid, breaking out of the loop.
            break

    # This will be the criteria that will be used to extract the extensions from the file paths.
    # Using none as the default value as this won't have a default value and will be manually
    # taken as an input from the user.
    criteria: PickExtension = None

    operation_mode: str = ''
    while True:
        # Taking input mode from the user. In 'auto' mode, the default values all vairables
        # will be used, however, in 'manual' mode, the user will select values for each variable.
        operation_mode = input('Select a mode (auto/manual): ').strip().lower()

        if operation_mode not in ['auto', 'manual']:
            print('The mode selected is incorrect. Try again. \n')
        else:
            # Breaking out of the loop if the input is as expected.
            break

    if operation_mode == 'manual':
        # Asking the user to set values for all defaults. Falling back to the default
        # value if the user input is unexpected.

        print(
            '\n\nUsing the manual mode. \nYou will be asked to add a value for all default variables.',
            'If you are unsure about the required value, hitting enter will make the program',
            'use the original default value.',
            '\n\nIf you are unsure, feel free to go through the ReadMe section to get an idea about what',
            'these values do to avoid messing up xD'
        )

        value = input('Select a randomization scheme ' +
                      f'({Mode.safe}/{Mode.fast}): ').strip().lower()
        if value not in [Mode.safe, Mode.fast]:
            print(
                f'Invalid input. Using `{randomize_mode}` as the default mode.')
        else:
            # If the value is either `Mode.safe` or `Mode.fast`, then no need to
            # check which one of them it is. Can directly store it, the value
            # for the variables is a string by itself and thus does not matter.
            randomize_mode = value

        value = input('Select a file selection mode (recursive/direct): ').strip().lower()
        if value not in ['recursive', 'direct']:
            print(f'Invalid input. Using `{selection_mode}` as default.')
        elif value == 'recursive':
            selection_mode = SelectionMode.recursive
        elif value == 'direct':
            selection_mode = SelectionMode.direct

        try:
            # Getting the length required for the file names.
            value = int(input('Required length for the random ' +
                              'file names: ').strip())
            if value < 10:
                # If the value is zero or a negative number, explicitly throwing
                # an error to end up in the catch section :p
                raise ValueError()
            else:
                fixed_length = value
        except ValueError:
            print(f'Unexpected response. Using `{fixed_length}` as the default',
                  'length for file names.')

        # Asking whether to include numbers in the randomized names or not.
        value = input('Use numbers in random file names (yes/no): ').strip().lower()
        if value not in ['yes', 'no', 'true', 'false']:
            value = 'yes' if use_digits else 'no'
            print(f'Unexpected response. Using `{value}` as default')
        elif value in ['yes', 'true']:
            use_digits = True
        elif value in ['no', 'false']:
            use_digits = False

    # Regardless of auto mode or manual mode, asking the user to select the extension selection
    # criteria.
    while True:
        # Breaking out of this loop only if a valid criteria is selected.
        value = input('Select a criteria to recognize extensions from file ' +
                      'names (hard/soft): ').strip().lower()
        if value not in ['hard', 'soft']:
            print('Unexpected input. Please choose one of the two types\n',
                  'This response cannot be skipped or defaulted.', sep='\n')
        elif value == 'hard':
            criteria = PickExtension.hard
        elif value == 'soft':
            criteria = PickExtension.soft

        if criteria is not None and isinstance(criteria, PickExtension):
            # Breaking out of the infinite loop only if criteria has a value
            # and is an instance of `PickExtension` class (read enum).
            break

    # Checking if the root directory still exists -- if the user is slow,
    # then there is always an edge case that the root directory might have been
    # removed or moved while the user was (slowly) giving input to the script.
    if not isdir(root):
        print('Could not locate the root directory. The directory could have been',
              'moved or deleted. Quitting the application. Hit enter to confirm.')

        # Taking input to make sure that the message is actually read -- and I don't
        # get people telling me that the script crashes suddenly...
        input()

        # Exiting with a negative value to indicate an error.
        exit(-10)

    # Generating random names for the files. If the user went with manual mode,
    # then the global values were overwritten with the user selected parameters.
    # No need to supply any optional paratemers as they default to the global values
    # which would have been modified under manual mode, or were supposed to remain
    # un-modified under the auto mode.
    generate_names(root=root, extension_criteria=criteria)

    # Once the dictionary is prepared, saving it as a text file.
    try:
        # Getting the full path for creating the text file. And creating the file in
        # write mode with truncate.
        new_file = os.path.join(root, original_names_file_title)
        text_file = open(new_file, 'w')

        # Once the file is opened, simply writing the original file names along with the
        # new files names (separated by the equality symbol). With one value on each line.
        for orig_name in name_pairs.keys():
            text_file.write(
                f'{orig_name} \t{equality}\t {name_pairs[orig_name]}\n')

        # Once done, simply flushing and closing the file
        text_file.flush()
        text_file.close()
    except OSError:
        # This error will be raised if the script does not have the rights to edit/create
        # files in the root directory. And if the script cannot edit files in the root
        # directory, then it won't be able to rename the files. Quitting the script.
        print(f'The script does not have edit/create rights in the directory `{root}`\n',
              'Rerun the script as an admin (or as sudo) if the problem persists.')
        exit(-12)

    # An integer to keep a track of the number of files that are renamed.
    count = 0

    # Once the new names for the files are saved, renaming files as the last step.
    for orig_name in name_pairs.keys():
        os.rename(orig_name, name_pairs[orig_name])
        count += 1

    print(f'\n\nRenamed {count} files in the given directory successfully')
    print('Execution completed successfully.')
    input('Hit enter to close the application!')
