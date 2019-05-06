# rme

## help

```
usage: rme [-h] [-d DIRECTORY] [-s] [-v] files [files ...]

remove every file except for the ones mentioned

positional arguments:
  files          files to save or not remove

optional arguments:
  -h, --help     show this help message and exit
  -d DIRECTORY   directory to remove files from
  -s             supress errors for files not found
  -v, --version  show program's version number and exit
```

## examples

### 1

Consider 3 files - `a.txt`, `b.txt`, and `c.txt`. Suppose you only want to retain `b.txt` but are too lazy to write a script or pattern match with some regex. You use `rme` - 

```sh
$ ls
a.txt  b.txt  c.txt
$ rme b.txt
$ ls
b.txt
```

All files except b.txt are saved.

### 2

Consider the same situation as [example 1](#1) but say you're in a different directory. You COULD specify the full path but that would lead you to deleting files in the current directory. This is why you have to be **very** careful while using `rme`. So to specify the directory you need to use with files, you use the `-d` flag. In this example, consider the files `a.txt`, `b.txt`, and `c.txt` in a directory called `alphabets/`. You're in the parent directory of alphabets - 

```sh
$ ls
alphabets
$ ls alphabets
a.txt  b.txt  c.txt
$ rme b.txt -d alphabets
$ ls alphabets
b.txt
```

The only drawback for this solution of managing location is the loss of autocompletion on the terminal and somewhat un-intuitiveness while removing-except files by only using the name and not the full path.
