# Title-Randomizer

A simple utility script that batch randomizes the names of all the files present inside a directory.
<br>

## Table of Contents:
 - [What does this script do?](https://github.com/demon-rem/Title-Randomizer#what-does-this-script-do)
 - [How do I use this script?](https://github.com/demon-rem/Title-Randomizer#how-do-i-use-this-script)
     - [Quick usage guide](https://github.com/demon-rem/Title-Randomizer#quick-usage-guide)
     - [In-Depth usage guide](https://github.com/demon-rem/Title-Randomizer#in-depth-usage-guide)
- [What are the input parameters the script requires?](https://github.com/demon-rem/Title-Randomizer#input-parameters)
    - [Root Directory](https://github.com/demon-rem/Title-Randomizer#root-directory)
    - [Operation Mode](https://github.com/demon-rem/Title-Randomizer#operation-mode)
        - [Auto Mode v/s Manual Mode](https://github.com/demon-rem/Title-Randomizer#auto-mode-vs-manual-mode)
    - [Randomization Scheme](https://github.com/demon-rem/Title-Randomizer#randomization-scheme)
        - [Safe Mode v/s Fast Mode](https://github.com/demon-rem/Title-Randomizer#safe-mode-vs-fast-mode)
    - [Selection Mode](https://github.com/demon-rem/Title-Randomizer#selection-mode)
        - [Recursive Mode v/s Direct Mode](https://github.com/demon-rem/Title-Randomizer#recursive-mode-vs-direct-mode)
    - [File title length](https://github.com/demon-rem/Title-Randomizer#file-title-length)
    - [Include numbers in file titles](https://github.com/demon-rem/Title-Randomizer#include-numbers)
    - [Extension recognition criteria](https://github.com/demon-rem/Title-Randomizer#extenstion-recongition)
        - [Hard Mode v/s Soft Mode](https://github.com/demon-rem/Title-Randomizer#hard-mode-vs-soft-mode)
-    [I messed up, how do I undo the damage?](https://github.com/demon-rem/Title-Randomizer#how-to-undo-the-damage)
 - [What is the purpose of making this script?](https://github.com/demon-rem/Title-Randomizer#why-make-this-script)
 - [Meme(s)](https://github.com/demon-rem/Title-Randomizer#i-want-memes-gib-memes) :p

## What does this script do?
This is a simple utility script that will **batch rename** all the files in the given directory with completely random titles.

***Modes***:
- With `auto mode`, you give minimal inputs, sit back and watch the script do the work.
- With `manual mode`, you have complete control over what the script does, the length of random titles, and much more.

## How do I use this script?

- Download this script (the Python file, rest is fluff)
- Run the file `BatchRename.py`
- Enter the required input when you're asked to

If you're unsure about the input to give, check out [this section](https://github.com/demon-rem/Title-Randomizer#input-parameters)

## Quick Usage Guide
This section teaches you how to use the script in `Auto mode` and should be enough to give you a basic understanding on how to use this script within the shortest amount of time possible

**Note**: If you go with `auto mode`, the script uses the default values for inputs. If you don't like these values, you can always go with the manual mode, or directly change these values in the script.

Here are the steps to follow:
- Copy the *full-path* of the **directory** containing the files whose titles are to be randomized. Paste this path when asked for the root directory.
- Next, when asked to select modes, enter `auto` as the input. This selects `auto mode`, and the script uses default values for the inputs. [Check out the [In-Depth Usage Guide](https://github.com/demon-rem/Title-Randomizer#in-depth-usage-guide) for using **manual mode**]
- When asked for the criteria to select file extensions, the average user can choose `hard mode`. If you're unsure about this, check out the section for [*extension selection criteria*](https://github.com/demon-rem/Title-Randomizer#extenstion-recongition) which explains this in detail.

## In-Depth Usage Guide
This section explains how to use the script in manual mode.

If you require a detailed explanation about the input parameters (including the default fall-back values), each of these input parameters has its own [section](https://github.com/demon-rem/Title-Randomizer#input-parameters) which shall provide you with a detailed explanation for that parameter.

Here are the steps to follow:
- Copy the full path of the directory containing the directory whose items are to be randomized. This path will be the value for the `root path`.

- Select `manual` when asked for mode to use **manual mode**. [Check out the [Brief Usage Guide](https://github.com/demon-rem/Title-Randomizer#quick-usage-guide) for using **auto mode**]

- When asked for **randomization scheme**, selecting `fast` will be good enough for most people. As the name implies `safe` randomization scheme is very safe (meaning negligible chances of repeated random names), however, it is a tad bit slower. Generally, this should be chosen if you have more than 10K files whose names are to be randomized.

- When asked for  *file selection mode*, go with `direct` only if the files present in the `root directory` should be assigned random titles. This means that a file present in a sub-directory inside the `root directory` will not be affected under this mode. Use `recursive` mode to include **any** file present **anywhere** in the `root directory`

- When asked for **length of file titles**, make sure to use a value large enough to avoid any collisions. Generally, 10 characters are good enough if you have less than 1,000 file titles to randomize. For every 1,000 files above that, add one character. 

- When asked to include numbers in random titles, enter `yes` if you want the new names to include random numbers too, `no` otherwise.

- When asked for the criteria to select file extensions, the average user can choose `hard mode`. If you're unsure about this, check out the section for *extension selection criteria* which explains this in detail.


## Input Parameters

This section contains an in-depth explanation for the input parameters that the script requires, along with the default values that will be used in case of *no input*/*auto mode*.

### *Root Directory*
Expects *full path* of the directory containing the files whose titles are to be randomized. Does not accept the path for anything other than a directory. 

- **Can be skipped**: No
- **Default Value**: None
- **Expected Value**: Full path for a directory

If the path you enter for this input is incorrect or does not belong to a directory, the script will throw an error and ask you to re-enter a valid path.

To get the full path of any directory in Windows, right-click the directory and select `Properties`. Navigate to `General` tab in the pop-up window that opens, copy the path corresponding to the entry `Location`. 

To verify the path (in any operating system), paste the path in File Explorer and hit enter. This should take you to the directory that you selected.
<br>
<br>

### Operation Mode
This mode determines if the script should use the default values (which is `auto-mode`) or if the script should ask you to enter a value for all inputs required (`manual mode`).

- **Can be skipped**: No
- **Default Value**: None
- **Expected Value**: `auto` or `manual`

Under `auto mode`, the script uses default values for all the input fields. In `manual mode`, if no input is supplied for any value, again, the script uses the default value for that particular input.
<br>

#### Auto Mode v/s Manual Mode

The auto mode is made to ease the entire process for the majority of users who want to skip the process of reading the entire documentation and would simply like to play it safe :p

Personally, I recommend using the `Manual Mode` if you want to fine-tune the outcome to match your expectations.
<br>
<br>

### Randomization Scheme
This mode determines the process to use while generating random names for the file titles.

- **Can be skipped**: Yes
- **Default Value**: Fast Mode
- **Expected Value**: `safe` or `fast`
<br>

#### Safe Mode v/s Fast Mode
As the names suggest, fast mode is typically faster than safe mode, the tradeoff being that there is a slightly higher percentage of name collisions or similar-looking names.

`Fast` mode uses the *random* module in Python, which is time-based. Meaning that the file names could end up looking similar to each other in some rare instances. On the other hand, `safe` mode uses the *secrets* module which results in a very high degree of randomization while consuming a bit more resources and being less efficient than *random* module.

If you require a high degree of randomization, go with `safe` mode, however for most of the users, simply choosing `fast` mode will be more efficient in terms of time and CPU Processing power.

**Note**: For the most part, the difference between using `safe` mode and `fast` mode will be negligible except for the latter being a few milliseconds faster than the former. No need to stress upon this decision :p
<br>
<br>

### Selection Mode
This input determines the files that will be selected from the `root directory`. 

- **Can be skipped**: Yes
- **Default Value**: Recursive Mode
- **Expected Value**: `recursive` or `direct`
<br>

#### Recursive Mode v/s Direct Mode
Recursive mode selects all the files that are present anywhere inside the `root directory`. A file that is present in a sub-directory under `root directory` will also be selected in recursive mode.

Direct mode will simply select files that are present **directly inside** `root directory`

```bash
|── <root directory>
│   ├── Folder A
│   │   ├── Folder New
│   │   │    ├── test-file.mp4
│   │   ├── test-file.mp4
│   │   ├── test-file.html
│   ├── Folder B
│   │   ├── qt-bindings.py
│   │   ├── hello.mp3
│   └── file.mkv
│   └── song.flac
│   └── presentation.pptx
│   └── writeup.docx
│   └── Code.cpp
```

For example, in the directory structure displayed above, the `root directory` contains several files, `Folder A` and `Folder B` and `Folder New` are directories present somewhere inside the root directory.

If you choose to rename the contents of `root directory` using `direct` mode, the titles of 5 files will be randomized. The remaining files are present inside some sub-directory and are not present **directly** inside root directory. Thus, direct mode will skip these files.

`Recursive` mode will randomize the titles of all ten files that are present inside the `root directory`. This mode will **recursively** visit each directory and rename the titles of all the files that are present anywhere inside the root directory.
<br>
<br>

### File Title Length
As is painfully obvious, this input will decide the length of the random file titles that are generated. All files will have final titles having length of exactly these many characters.

- **Can be skipped**: Yes
- **Default Value**: 15
- **Expected Value**: A number greater than 10

**Note**: It is recommended that you use a file title length of at least 10 characters. Add a new character for every 1,000 files whose titles you want to randomize.
<br>
<br>

### Include Numbers
This parameter determines if numbers are to be included in the randomly generated titles that are applied to the files.

- **Can be skipped**: Yes
- **Default Value**: No (numbers are excluded from random titles)
- **Expected Value**: `yes` or `true` or `no` or `false`

Although the script does not mention it anywhere, using `true` or `false` as an input for this parameter is also valid, true equates to `yes`, and false equates to `no`.
<br>
<br>

### Extenstion Recongition

This is one of the most important input parameters that the script will ask you for. And also is one that has the most potential to mess up something if you choose the wrong parameter.

- **Can be skipped**: No
- **Default Value**: None
- **Expected Value**: `hard` or `soft`

While renaming files, the script has to recognize the file name and the file extension. 

The name is replaced by a random string, and the extension is then added back to this random string. This ensures that while the file title is randomized, the extension isn't and thus the file can be used normally.

This file extension is used by the operating system to differentiate between different types of files. This also decides the software that will be used to open the file, a file with an extension of `.mp3` will be opened by audio players for example.

Changing the file extension from `.mp3` to `.docx` does not harm the file in any manner. However, if you try to open the file, Word (or anything similar) won't be able to open the file. This is exactly what will happen if you choose the wrong input for this parameter.
<br>

#### Hard Mode v/s Soft Mode
As a general rule, you should use `soft mode` if you are ever unsure. This mode ensures that the file extension is never changed. 

Anything placed after the first full-stop (period) in the file name will be recognized as the file extension under this mode. This means that if you have a file named;
```
Test.File.In.Here.Do.Not.Touch.mp4
```

Soft mode will recognize `.File.In.Here.Do.Not.Touch.mp4` as the file extension instead of `.mp4`, and thus, the final file name will be;
```
<random-string>.File.In.Here.Do.Not.Touch.mp4
```
<br>

On the other hand, `hard mode` will **assume** that only the contents after the last full-stop (period) are the file extension. Using the previous example, hard mode will identify the file extension as `.mp4` -- which in this case is the correct extension, and thus under `hard mode`, the final file name will be 
```
<random-string>.mp4
```

However, for files such as 
```
Compressed-Album.tar.gz
```

Hard mode will recognize the file extension as `.gz` and thus rename the file to be 
```
<random-string>.gz
``` 
While many people will agree that the actual file extension is `.gz`, the file becomes unusable after being renamed until its extension is changed back to `.tar.gz`, and thus using `hard mode` in this scenario is a bad decision.


## How to Undo The Damage
I expect myself to be the one who messes up (anytime in the future), and thus have added something to help a bit :p

Before changing the titles of the files, the script will write down the original file names and the new file names to a text-file named `Original Names.txt`, this file will be saved in the root directory.

Once all these titles are listed out, only then will the script move on to the part of actually renaming the files.

An example of an entry in this text file will be:
```
D:\Movies\Test.mp4 --//--> D:\Movies\aDmAkSsds.mp4
```

And yes, the `--//-->` is an equal-to symbol  (⊙_⊙;)

#### What do I do with this text file?
Once you locate this text file, this file contains the full path with the original file title on the left and the new file title (with full path) in the right. 

Simply rename the file in the right to be the file on the left. You can make a custom script to scrape the text file and rename the files for you, or manually make these changes, or wait for me to mess up and make another script to do the scraping and renaming part :p
<br>

#### Why use this ugly symbol instead of normal equal-to sign?
The main reason for using the ugly symbol (`--//-->`) over the normal equal-to (`=`) symbol, is because there is always a possibility that some file could be ending with '=' or have an equal-to symbol in the middle of the file path.

In such a scenario, making a script to scrape the text file and rename the files to their original names will be a lot more challenging, and any problems over there could permanently alter the files. So, using this ugly looking symbol to avoid any headaches in the future. Linux, Windows and most other Operating Systems do not allow forward-slash '`/`'  symbol in file or directory names. And so, the probability of valid file paths containing '`--//-->`' is next to impossible.

## Why make this script?
Uh, I have a lot of wallpapers with me (I've got a collection of wallpapers). 

One of the problems that I faced was the grouping of similar wallpapers. For example, all the Lord of the Rings wallpapers were present close to each other (even though I got them from multiple sources).

And I didn't want to rely on the shuffle mode in Windows, as sometimes I see a wallpaper and by the time I can recognize the movie/series that the wallpaper is from it changes.

With shuffle mode on, it becomes impossible to locate the wallpaper (it could be anyone of the thousand-plus wallpapers). 

Having shuffle mode off makes locating the previous wallpaper possible as it will be just before (or close to) the current wallpaper. Thus, the in-built shuffle mode can't be the solution.

And so, I decided to make a custom script to randomize the titles, to give a shuffle effect while still making it possible to locate previous wallpapers.

( ´･･)ﾉ(._.`)

## I want memes, gib memes

Alright, here you go

![Meme](https://github.com/demon-rem/res/blob/master/memes/5pkdJtI35VToSlCEsPRG2l3q2p.jpg?raw=true)