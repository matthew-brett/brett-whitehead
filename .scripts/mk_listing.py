#!/usr/bin/env python
""" Re-create Markdown directory listing
"""

import os
import os.path as op

from argparse import ArgumentParser, RawDescriptionHelpFormatter

OK_LEXTS = ['.jpg', '.jpeg', '.png', '.pdf']

def mk_listing(pth):
    out_fname = op.join(pth, 'index.md')
    to_list = []
    for fname in sorted(os.listdir(pth)):
        root, ext = op.splitext(fname)
        if ext.lower() not in OK_LEXTS:
            continue
        to_list.append(fname)
    with open(out_fname, 'wt') as fobj:
        fobj.write(f"""\
---
title: Directory listing of {pth}
---

""")
        for fname in to_list:
            bn = op.basename(fname)
            root, ext = op.splitext(bn)
            fobj.write(f'*   [{root}]({bn})\n')


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('dir',
                        help='Directory to create md listing for.')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    mk_listing(args.dir)


if __name__ == '__main__':
    main()
