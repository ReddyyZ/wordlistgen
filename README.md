<h1 align="center">Simple Wordlist Generator</h1>

> Example file: [wordlist.txt](wordlist.txt)

## What is this
Generates all possible passwords of the defined length.

## Want to use in your code?
You can use the **wordlists.py** in the **include** dir in your code. This contains a class Wordlist.

Example:
```python
from wordlists import Wordlist

length = int(input('Length of passwords: '))
filename = str(input('Filename: '))

wordlist = Wordlist(filename,length)
print('Generating...')
wordlist.generate()
```

## How to use
```python main.py -l 4 -f wordlist.txt```

The -l option sets the length of the passwords
The -f option sets the output filename

To see the help options, type: 
```python main.py -h```

## License
This project is under [MIT License](LICENSE)

<h2 align="center">&lt;/&gt; by ReddyyZ</h2>