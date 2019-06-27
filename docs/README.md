# BetterX Documentation

## Table of Contents

1. [Commands](#commands)
	+ [lsx](#lsx)
	+ [rme](#rme)
	+ [tshift](#tshift)
2. [Contributing](#contributing)
3. [Future Plans](#future-plans)
4. [Reasons for BetterX](#reasons-for-betterx)

### Commands

_BetterX_ currently has three commands but more can be expected as time and needs go on.

#### [lsx](commands/lsx.md)

[examples](commands/lsx.md#examples)

It's a tool for viewing the contents of a directory after some interval of time - by default, 1 second - for a fixed number of iterations - by default 10. It can be useful for keeping an eye on a media folder on a server that manages user uploads constantly. If a user does not want to specify the number of times to iterate of a directory, he / she can just pass the `-i` argument for __infinity mode__. That just means that the command will run forever until manually halted by a `KeyboardInterrupt` (pressing <kbd>Ctrl+C</kbd>). Proper checks for data inputs have been implemented. `lsx` is a unique command since it doesn't have a dependency on some `betterx/_lsx.py` function. To know how the code works or how it's structured, read the [contributing](#contributing) guide.

#### [rme](commands/rme.md)

[examples](commands/rme.md#examples)

`rme` stands for "remove except" and it is meant to be used as the opposite of the `rm` command in Unix-like systems. That is pretty much self explanatory - while `rm` deletes all the files (or directories if the `-r` flag is used) passed as arguments. For example, consider you have a directory with 3 files in it - `a.txt`, `b.txt`, and `c.txt`. Now you only want to save `b.txt` and delete the rest of the contents of the directory. You'd have to do this with the traditional `rm` command - 

```sh
$ rm a.txt c.txt
```

But with `rme`, all you need to do is pass the file that needs to be saved - 
```sh
$ rme b.txt
```

Both will result in the deletion of files other than `b.txt`

I've also always hated the `-r` flag you have to use to delete a directory which is why I didn't include a flag for directories specifically. That is one of the reasons why this command is extremely dangerous to use if not handled properly. There is a supress flag that is turned off by default - it's used to raise a `FileNotFoundError` if a file you mention in the arguments is not found in the directory you pass.

#### [tshift](commands/tshift.md)

[examples](commands/tshift.md#examples)

Programmers often come across the war between spaces and tabs. I'm mostly neutral in this battle but I do like to go by the popular style guides of languages. Or if I don't have the time or if the guide's too complex for me, I just let a formatter take care of my code for me. But that happens rarely. I write my own code and I write it so that after ten years, I'd like to read it. Now Python is, by far, my favourite programming language. And sometimes my editors use my Python defaults for other programming languages like Javascript or C++. And I'm sure you've come across this problem as well. 

Thus I found myself using Sublime Text's `convert indentation to (spaces|tabs)` feature a lot. And once I get familiar with an editor, I don't bother incorporating the same shortcuts in others. So I fixed it by writing a script to convert the indentation of a source code file from tabs to spaces. The vice-versa for it is much more complex as it'd take the parsing of the type of language and I found myself converting spaces to tabs much less than the other way around. And thus `tshift` was born. All it takes is a file and its magic will convert all the tabs in the file to `n` spaces which you can also provide as an argument.

### Reasons for BetterX

BetterX is a command line utility toolkit that aims to distribute programs that most shells don't already have. For example, the motivation for one of the first programs was to make a script that would remove every file in a directory except for the ones that were passed as arguments - kind of like a reverse `rm` command. In fact, the first version of a 'remove except' script was hacked together almost two months ago at [rme.py](https://gist.github.com/mentix02/8baff0b2e7e59b9b0a5d8860d363dde8).

Some more followed with one for listing the contents of a directory every `t` number of seconds `n` times - [list.py](https://gist.github.com/mentix02/b49d051a2d181a689abc72e548bce314). But they were slap-job at best and wren't really meant to be used by anyone other than me. But I like to change my Linux distros every so often and I found myself `wget`-ing these raw files into my `/usr/bin/`. Then I'd forget I needed to use a `sudo` and it was very hassling. Finally, I decided to write some good code for once and made this local project. But what I didn't realize was that when one's working with commands that deal with mass deletion of files, it's usually a good idea to backup code every step of the way. And like the moron I am, a badly configured `rme` test ended up deleting all my code.

So I went at it again but this time, I was crystal clear what I had to do - impose some static checks using mypy early on and always use sandboxes while testing all these utilities. And so I did. And I also went one step ahead and added a testing suite. And something that I've observed from my other projects is that a testing suite usually takes **much** longer to code than the actual project itself. Edge cases and just clean code, I suppose but still. But writing those cases is just so painful. Better use them if you're going to be [contributing](#contributing).

### Contributing

Read the contributing guide [here](CONTRIBUTING.md).
