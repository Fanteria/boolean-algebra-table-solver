#!/bin/python

import argparse
from BooleanLogic import BooleanLogic

fileHelp   = "A path to the input file."
letterHelp = "The last letter of input variables for the truth table."
startHelp  = "Nuber of the first line of the truth table. Default is the first line of the file."
endHelp    = "The last line of the truth table. Default is the last line of the file."
tHelp = "If enabled, creates text style output. If disabled, the output will be in LaTeX. The default value is disabled."
mHelp = "This flag minimizes the logic functions on the output. Can be combined with -u to output both. The default value is enabled."
uHelp = "Create unminimized output. Can be combined with -m to output both. The default is disabled."
pHelp = "Print the output to the terminal. Can be combined with -i to create both outputs. The default is enabled."
iHelp = "Insert the result table after the last line specified in the 4th argument. Can be combined with -p to create both outputs. The default is disabled."
lHelp = "Defines the number of lines between the line with variable names and the first line of the truth table. If used, a value must be specified. The default value is 1."

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help = fileHelp)
    parser.add_argument("letter", type=str, help = letterHelp)
    parser.add_argument("start", nargs='?', default=-1, type=int, help=startHelp)
    parser.add_argument("end", nargs='?', default=-1, type=int, help = endHelp)
    parser.add_argument("-t", "--text", action='store_true', help = tHelp)
    parser.add_argument("-m", "--minimized", action='store_true', help = mHelp)
    parser.add_argument("-u", "--unminimized", action='store_true', help = uHelp)
    parser.add_argument("-p", "--print", action='store_true', help = pHelp)
    parser.add_argument("-i", "--insert", action='store_true', help = iHelp)
    parser.add_argument("-l", "--lines", default=1, type=int, help = lHelp)
    args = parser.parse_args()


    with open(args.file, 'r') as f:
        fileText = f.readlines()
        data = fileText
    if args.start > 0:
        data = data[args.start-1:]
        if args.end > 0:
            data = data[:args.end - args.start + 1]
    table = ''.join([str(e) for e in data])

    b = BooleanLogic(table, args.letter, args.lines)
    if args.text:
        BooleanLogic.texOutput = False
        
    out = ""
    if not args.minimized and not args.unminimized:
        out = b.getAll()
    if args.minimized:
        out += b.getAll(True)
    if args.unminimized:
        out += b.getAll(False)

    if not args.print and not args.insert:
        print(out)
    if args.print:
        print(out)
    if args.insert:
        if (args.end < 0 or len(fileText) >= args.end):
            fileText.append('\n' + out)
        else:
            fileText[args.end] += '\n' + out
        with open(args.file, 'w') as f:
            f.writelines(fileText)
