#!/usr/bin/env python3
import os

basedir = os.path.dirname(os.path.realpath(__file__))

dirs = sorted(list(filter(os.path.isdir, os.listdir(basedir))))

files = [f'{basedir}/{d}/{f}' for d in dirs for f in sorted(os.listdir(d)) if f.endswith('.md')]


if __name__ == '__main__':
    with open('all_questions.md', 'w') as f:
        for inp in files:
            with open(inp) as fi:
                f.write(fi.read())
                f.write('\n\n')
