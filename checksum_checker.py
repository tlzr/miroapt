#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import aptrep

def main(args):
  first_repository = aptrep.Repository()
  second_repository = aptrep.Repository()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Verify packages chechsums in 2 repositories.')
    parser.add_argument('-f', '--force-cache-update', action='store_true',
                        help='Force cache update')
    parser.add_argument('-i', '--info', action='version',
                        version='Version: 0.1')
    parser.add_argument('-p', '--profile', metavar=('PROFILE'), type=str,
                        help="Set profile")
    parser.add_argument('-r', '--remove-cache', action='store_true',
                        help='Remove specified cache')
    args = parser.parse_args()

    main(args)
