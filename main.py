#!/bin/python

import argparse
from BooleanLogic import BooleanLogic

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str)
    parser.add_argument("letter", type=str)
    parser.add_argument("start", nargs='?', default=-1, type=int)
    parser.add_argument("end", nargs='?', default=-1, type=int)
    parser.add_argument("-t", "--text", action='store_true')
    parser.add_argument("-m", "--minimized", action='store_true')
    parser.add_argument("-u", "--unminimized", action='store_true')
    parser.add_argument("-p", "--print", action='store_true')
    parser.add_argument("-a", "--append", action='store_true')
    parser.add_argument("-l", "--lines", default=1, type=int)
    args = parser.parse_args()


    with open(args.file, 'r') as f:
        fileText = f.readlines()
        data = fileText
    if args.start > 0:
        data = data[args.start-1:]
        if args.end > 0:
            data = data[:args.end - args.start]
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

    if not args.print and not args.append:
        print(out)
    if args.print:
        print(out)
    if args.append:
        fileText[args.end - 1] += '\n' + out
        with open(args.file, 'w') as f:
            f.writelines(fileText)
