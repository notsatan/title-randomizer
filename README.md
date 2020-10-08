

<p align="center">
<img src="https://img.shields.io/github/license/demon-rem/title-randomizer?style=for-the-badge"/>

<img src="https://img.shields.io/github/repo-size/demon-rem/title-randomizer?style=for-the-badge"/>
</p>

<br/>
<p align="center">
  <a href="https://github.com/demon-rem/title-randomizer/">
    <img src="./images/image-main.jpg" alt="Logo" width="320" height="320">
  </a>

  <h3 align="center">title-randomizer</h3>

  <p align="center">
    A simple utility script that batch randomizes the names of all the files present inside a directory.
    <br><br>
    <a href="https://github.com/demon-rem/title-randomizer/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/demon-rem/title-randomizer/issues">Bug Report</a>
    ·
    <a href="https://github.com/demon-rem/title-randomizer/issues">Request Feature</a>
    ·
    <a href="https://github.com/demon-rem/title-randomizer/fork">Fork Repo</a>
    ·
  </p>
</p>

---
<br>

## Table of Contents
- [What does this script do?](#what-does-this-script-do)
- [Quick Usage Guide](#quick-usage-guide)
- [Input Parameters](#input-parameters)
  - [*Root Directory*](#root-directory)
  - [Randomization Scheme](#randomization-scheme)
    - [Safe Mode v/s Fast Mode](#safe-mode-vs-fast-mode)
  - [Selection Mode](#selection-mode)
    - [Recursive Mode v/s Direct Mode](#recursive-mode-vs-direct-mode)
  - [File Title Length](#file-title-length)
  - [Character Set](#character-set)
  - [Extenstion Recongition](#extenstion-recongition)
    - [Hard Mode v/s Soft Mode](#hard-mode-vs-soft-mode)
- [How to Undo The Damage](#how-to-undo-the-damage)
    - [What do I do with this text file?](#what-do-i-do-with-this-text-file)
    - [Why use this ugly symbol instead of normal equal-to sign?](#why-use-this-ugly-symbol-instead-of-normal-equal-to-sign)
- [Examples](#examples)
    - [Using Default Parameters](#using-default-parameters)
    - [Custom Length](#custom-length)
    - [Using Safe Mode](#using-safe-mode)
    - [Custom Length with Soft Extensions](#custom-length-with-soft-extensions)
    - [Numeric Titles](#numeric-titles)
    - [Using Direct Mode](#using-direct-mode)
    - [Direct Mode with Custom Length and Lower Case Titles](#direct-mode-with-custom-length-and-lower-case-titles)
    - [Using Double Quotation Marks](#using-double-quotation-marks)
- [Random Meme](#random-meme)



## What does this script do?

This is a simple utility script that will **batch rename** all files in the given directory with completely random titles.

***Modes***:

Originally, for ease-of-use, the functioning of this script was divided into `auto` and `manual` mode.

However, in a later commit, I decided to get rid of this system, and replace it with a system whereby parameters can be selectively overwritten, and the rest of them will fall-back to their default value(s).

All parameters are to be passed to the script in the form of [command line arguments](https://en.wikipedia.org/wiki/Command-line_interface#Arguments). Parameters that are not used will resort to their default values.

## Quick Usage Guide

This section explains how to use the script in auto mode, which is enough to to understand how to use this script in the shortest amount of time.

* Clone this repository.
* Run the python script 
    > `python BatchRename.py`

**Note**: Any parameter that is not passed to this script will resort to a set [default value](#input-parameters).

## Input Parameters

This section explains various input parameters that can be passed to the script, along with their default values.

Do note that these input parameters are to be provided in the form of command-line arguments (take a look at the [examples](#examples) section to get an idea of how to use these parameters).

Note: Values for **all** parameters can be *optionally* passed between double quotation marks. [Example](#using-double-quotation-marks)

### *Root Directory*

* **Argument:** `--root="path/to/directory/"`
* **Can be skipped:** No
* **Default Value:** *None*
* **Expected Value(s):** Full path to a directory

Expects path to the root directory containing the files. 

If the path you enter for this input is incorrect or does not point to a directory, the script will throw an error and ask you to re-enter a valid path.
<br>
<br>

### Randomization Scheme

* **Argument:** `--randomization=<value>`
* **Can be skipped:** Yes
* **Default Value:** `fast`
* **Expected Value(s):** `safe` or `fast`
<br>

This mode determines the process to use while generating random names for the file titles.

#### Safe Mode v/s Fast Mode

As the names suggest, fast mode is (*negligibly*) faster than safe mode, the tradeoff being that there is a slightly higher chance of name collisions.

The main difference between the two being; `fast` mode uses the *random* module, which is time-based, i.e. random strings generated one after the other have slightly higher chances of collisions. On the other hand, `safe` mode uses the *secrets* module which results in a higher degree of randomization while consuming *negligibly* more resources than *random* module.

If you require a high degree of randomization, go with `safe` mode - for most users, `fast` mode will be good enough.
<br>
<br>

### Selection Mode

* **Argument:** `--recursive` ***OR*** `--direct`
* **Can be skipped:** Yes
* **Default Value:** Recursive Mode
* **Expected Value:** `recursive` or `direct`
<br>

This is used to control the files that will be affected by this script to some extent. 

#### Recursive Mode v/s Direct Mode

Recursive mode selects all the files that are present anywhere inside the root directory . A file that is present in a sub-directory under `root directory` will also be selected in recursive mode.

Direct mode will simply select files that are present **directly inside** `root directory`

``` bash
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

For example, in the directory structure displayed above, the root directory contains several files, `Folder A` and `Folder B` are directories present **directly** inside the root directory.

If you choose to rename the contents of `root directory` using `direct` mode, the titles of 5 files will be randomized. The remaining files are present inside a sub-directory and are not present **directly** inside root directory. 

`Recursive` mode will affect all ten files that are present inside the `root directory` . This mode will **recursively** visit each sub-directory. 


tl;dr
* Direct mode will skip ***any*** file that is not present directly inside the root directory.
* Recursive mode affects file(s) present anywhere inside the root directory.
<br>
<br>

### File Title Length

* **Argument:** `--title-length=<integer>`
* **Can be skipped:** Yes
* **Default Value:** 10
* **Expected Value(s):** Any integer above 7

This parameter dictates the length of the random file titles. All files will have randomized titles having length of exactly these many characters.


**Note**: It is recommended that you use a file title length of at least 10 characters.
<br>
<br>

### Character Set

* **Argument:** `--charset=<value>`
* **Can be skipped:** Yes
* **Default Value:** `alphanumeric`
* **Allowed Value(s):** `alphanumeric` ***OR*** `numeric` ***OR*** `lowercase` ***OR*** `uppercase` ***OR*** `alphabet`

This parameter decides which characters are to be included in the set of random characters to be used. In the backend, the script will form a set of all characters that are to be used, and then randomly select a character from this set to form random titles.

The character sets available are;

* `alphanumeric` - Alphabets and Numbers
* `alphabet` - Alphabets
* `numeric` - Numbers
* `lowercase` - Lower case alphabets
* `uppercase` - Upper case alphabets

Only one value can be set for this parameter at a time.

### Extenstion Recongition

* **Argument:** `--extensions=<value>`
* **Can be skipped:** Yes
* **Default Value:** `soft`
* **Allowed Value(s):** `hard` or `soft`

While renaming files, the script has to recognize the file name and the file extension. 

The name is replaced by a random string, and the extension is then added back to this random string. This ensures that while the file title is randomized, the extension isn't - allowing file to be used normally.

Changing the file extension from `.mp3` to `.docx` does not harm the file in any manner. However, if you try to open the file, Word (or anything similar) won't be able to open the file. This is exactly what will happen if you choose the wrong input for this parameter.
<br>

#### Hard Mode v/s Soft Mode

As a general rule, use the `soft` mode if you are unsure. This mode ensures that the file extension is never changed.

Under `soft` mode, anything placed after the first period in the file name will be treated as a part of the file extension. For example, if you have a file;

``` 
Test.File.Here.mp4
```

Soft mode will recognize `.File.Here.mp4` as the file extension instead of `.mp4` , and thus, the final file name will be; 

``` 
<random-string>.File.Here.mp4
```
<br>

On the other hand, `hard` mode will **assume** that only the contents after the last period are the extension. Using the previous example, hard mode will identify the file extension as `.mp4` -- which in this case is the correct extension. Under `hard mode` , the final file name will be;

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

While the actual file extension is indeed `.gz` , the file becomes unusable after being renamed until its extension is changed back to `.tar.gz`.

Keeping the above in mind, you are free to use either one of these modes depending on the files that you intend to rename.

## How to Undo The Damage

I expect myself to be the one who messes up (anytime in the future), and thus have added something to help a bit.

Before changing the titles of the files, the script will write down the original file names and the new file names to a text-file named `Original Names.txt` , this file will saved in the working directory.

> Use `pwd` in Linux/Unix, and `cd` in Windows to get the path to the working directory.

An example of an entry in this text file will be:

``` 
D:\Movies\Test.mp4 --//--> D:\Movies\aDmAkSsds.mp4
```

And yes, the `--//-->` is an equal-to symbol!

#### What do I do with this text file?

Once you locate this text file, this file contains the full path with the original file title on the left and the new file title (with full path) in the right.

Simply rename the file in the right to be the file on the left. You can make a custom script to scrape the text file and rename the files for you, or manually make these changes to get the original file title back.
<br>

#### Why use this ugly symbol instead of normal equal-to sign?

The main reason for using the ugly symbol ( `--//-->` ) over the normal equal-to ( `=` ) symbol, is because there is always a possibility that some file could be ending with '=' or have an equal-to symbol in the middle of the file path.

In such a scenario, a script to scrape the text file and rename the files to their original names will have a tough time, and any problems over here could permanently alter the files. Using this ugly looking symbol avoid all these problems since most operating systems do not allow forward-slash '`/`'  symbol in file or directory names. And so, the probability of valid file paths containing ' `--//-->` ' is nearly none.


## Examples

#### Using Default Parameters

All parameters will resort to their [default values](#input-parameters).
> `python BatchRename.py --root="/home/demon-rem/Wallpapers"`

#### Custom Length

Random titles generated will have a length of 15 characters.
> `python BatchRename.py --title-length=14 --root="/home/demon-rem/Wallpapers"`

#### Using Safe Mode

Random titles will be generated using the `secrets` modules, and have a higher degree of randomness.
> `python BatchRename.py --root="/home/demon-rem/Wallpapers" --randomization=safe`

#### Custom Length with Soft Extensions

The script will attempt to identify file extensions using the [soft mode](#hard-mode-vs-soft-mode), with a fixed length of 12 characters.
> `python BatchRename.py --root="/home/demon-rem/Wallpapers" --extensions=soft --title-length=12`

#### Numeric Titles

The random titles generated will consist of just numbers.
> `python BatchRename.py --root="/home/demon-rem/Wallpapers" --charset=numeric`

#### Using Direct Mode

Only the files present directly inside the root directory will be affected (and renamed).

> `python BatchRename.py --root="/home/demon-rem/Wallpapers" --direct`

#### Direct Mode with Custom Length and Lower Case Titles

Files present **directly inside** the root directory will be renamed with random titles of custom length consisting of lower-case alphabets.
> `python BatchRename --root="/home/demon-rem/Wallpapers" --title-length=15 --charset=lowercase --direct` 

#### Using Double Quotation Marks

An example to display that values for **all** parameters can be wrapped in double-quotation marks and still work normally.
> `python BatchRename --root="/home/demon-rem/Wallpapers" --title-length="15" --charset="lowercase" --direct`

## Random Meme

![Meme](https://github.com/demon-rem/res/blob/master/memes/5pkdJtI35VToSlCEsPRG2l3q2p.jpg?raw=true)
