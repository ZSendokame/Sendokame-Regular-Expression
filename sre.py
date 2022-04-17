import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--regex', help='Set Regex to Use.')
parser.add_argument('--string', help='String to Analize.')
parser.add_argument('--file', help='File to Analize.')
args = parser.parse_args()

# Error
if not args.file == None and not os.path.exists(args.file):
    print('Error: Cannot found file.')
    exit(1)

# Main
string = args.string or open(args.file).read()
result = re.findall(args.regex, string)

if len(result) == 0:
    print('\nDidn\'t Found any Matches.\n')
    exit(1)

else:
    for match in result:
        print(match)
