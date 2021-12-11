import re
import argparse
from colorama import Back, init

init()

parser = argparse.ArgumentParser()
parser.add_argument('--regex', help='Set Regex to Use.')
parser.add_argument('--string', help='String to Analize.')
args = parser.parse_args()

string = args.string
pattern = re.compile(r'' + args.regex)
result = pattern.findall(args.string)

if len(result) == 0:
    print('\nError: Didn\'t Found any Matches.\n')
    exit(1)

else:
    for match in result:
        string = string.replace(match, f'{Back.GREEN}{match}{Back.RESET}')

print(f'\n{string}\n')
