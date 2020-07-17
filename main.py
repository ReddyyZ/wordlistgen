from include.wordlists import Wordlist
from progress.bar import ChargingBar
import sys,argparse

def arguments():
    parser = argparse.ArgumentParser(description="Simple Wordlist Generator. By: ReddyyZ")
    parser.add_argument('-l','--length',default=4,type=int,help="Max length of passwords")
    parser.add_argument('-f','--file',default='wordlist.txt',type=str,help="Output file name")
    args = parser.parse_args()
    return (args.file,args.length)

if __name__ == "__main__":
    FILENAME,LENGTH = arguments()

    print(
f"""
-----------------------------------------------------------------------------------------
                                Simple Wordlist Generator
                                    Coded by: Reddyyz
                        https://github.com/ReddyyZ/wordlistgen
-----------------------------------------------------------------------------------------

LENGTH: {LENGTH}
FILENAME: {FILENAME}
"""
    )

    bar = ChargingBar('Creating wordlist...',max=LENGTH)
    cb = lambda : bar.next()
    wordlist = Wordlist(FILENAME,length=LENGTH,cb=cb)
    try:
        wordlist.generate()
    except KeyboardInterrupt:
        bar.finish()
        sys.exit('Exiting...')
    bar.finish()