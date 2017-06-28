#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import aptrep


def main(args):
    if args.remove_cache:
        answer = raw_input('Do you really want to delete cache directory:\n%s\n%s\nPress "y" to continue.\n' % (args.cache)) or 'n'
        if answer == 'y':
            cache = aptrep.Repository()
            cache.remove_cache(args.cache)

    repository = aptrep.Repository()
    repo = repository.prepare_cache(cache_dir=args.cache, sources_lists=args.sources, keys=args.keys, force_cache_update=args.update_cache)

    for package in repo.keys():
        #TBD: add more information for several versions
        print('Package name: %s, Version: %s' % (package, repo[package].versions[0].version))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get package information')
    parser.add_argument('-i', '--info', action='version', version='0.1')
    parser.add_argument('--cache', type=str, help='Cache location', default='cache/first')
    parser.add_argument('--sources', type=str, help='Sources lists location')
    parser.add_argument('--keys', type=str, help='Keys location')
    parser.add_argument('-u', '--update-cache', action='store_true', help='Force cache update')
    parser.add_argument('-r', '--remove-cache', action='store_true', help='Remove cache folders for both repositories')
    args = parser.parse_args()

    main(args)
