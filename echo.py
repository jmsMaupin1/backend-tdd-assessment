#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "jmsMaupinRC"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description='Perform transformation on input text.')

    parser.add_argument('-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument('-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument('-t', '--title', help='convert text to titlecase ', action='store_true')
    parser.add_argument('text', help='text to be manipulated')

    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    text = parsed_args.text

    if parsed_args.upper:
        text = text.upper()
    if parsed_args.lower:
        text = text.lower()
    if parsed_args.title:
        text = text.title()

    return text


if __name__ == '__main__':
    main(sys.argv[1:])
