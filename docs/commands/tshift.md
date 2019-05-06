# tshift

## help
```
usage: tshift [-h] [-o OUTPUT] [-n NUMBER] [-v] file

replaces all tab characters in a file with spaces

positional arguments:
  file           file to read for tab characters

optional arguments:
  -h, --help     show this help message and exit
  -o OUTPUT      write tab replaced file into a different file
  -n NUMBER      number of spaces to convert tab to
  -v, --version  show program's version number and exit
```

## examples

### 1

Source code in file `hello.py` - 
```python
def main():
	print("hello")

if __name__ == '__main__':
	main()
```

Run `tshift` to convert all tabs to 2 spaces - 
```sh
$ cat hello.py
def main():
	print("hello")

if __name__ == '__main__':
	main()
$ tshift hello.py -n 2
$ cat hello.py
def main():
  print("hello")

if __name__ == '__main__':
  main()
```

### 2

Source code in file `drink.c` - 
```c
#include <stdio.h>

int main(void) {
	int age;
	printf("enter age : ");
	scanf("%d" &age);

	if (age > 18) {
		printf("you can drink\n");
	} else {
		pritnf("you can't drink\n");
	}

	return 0;
}
```

Run tshift with `-o` flag and output filename as `modified_space_drink.c` - 

```sh
$ ls
world.c
$ tshift world.c -o modified_space_drink.c
$ ls
modified_space_drink.c  world.c
```
