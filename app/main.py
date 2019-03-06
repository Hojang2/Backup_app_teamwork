#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description="Backup client application",
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-g' '--graphics', dest='graphics', action='store_true')
parser.add_argument('--no-graphics', dest='graphics', action='store_false')
parser.set_defaults(graphics=False)
args = parser.parse_args()


def main():
    if args.graphics:
        pass
        # Starts graphics session.
    else:
        pass
        # Runs only CLI


if __name__ == "__main__":
    main()
