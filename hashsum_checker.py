#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import aptrep
import sys

def main(args):
    print args

    if args.remove_cache:
        answer = raw_input('Do you really want to delete directories:\n%s\n%s\nPress "y" to continue.\n' % (args.cache_1, args.cache_2)) or 'n'
        if answer == 'y':
            cache = aptrep.Repository()
            cache.remove_cache(args.cache_1)
            cache.remove_cache(args.cache_2)

    first_repository = aptrep.Repository()
    second_repository = aptrep.Repository()

    repo_1 = first_repository.prepare_cache(cache_dir=args.cache_1, sources_lists=args.sources_1, keys=args.keys_1, force_cache_update=args.update_cache)
    repo_2 = second_repository.prepare_cache(cache_dir=args.cache_2, sources_lists=args.sources_2, keys=args.keys_2, force_cache_update=args.update_cache)

    for package in repo_1.keys():
        if package in repo_2:
            if repo_1[package].versions[0].version == repo_2[package].versions[0].version:
                if repo_1[package].versions[0].md5 != repo_2[package].versions[0].md5:
                    print('%s: %s <=> %s Hash sum is not identical: %s <=> %s' % (package, repo_1[package].versions[0].version, repo_2[package].versions[0].version, repo_1[package].versions[0].md5, repo_2[package].versions[0].md5))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Verify packages hash sums in 2 repositories')
    parser.add_argument('-i', '--info', action='version', version='0.1')
    first = parser.add_argument_group('first-repository', '1st repository')
    first.add_argument('--cache-1', type=str, help='Cache location', default='cache/first')
    first.add_argument('--sources-1', type=str, help='Sources lists location')
    first.add_argument('--keys-1', type=str, help='Keys location')
    second = parser.add_argument_group('second-repository', '2nd repository')
    second.add_argument('--cache-2', type=str, help='Cache location', default='cache/second')
    second.add_argument('--sources-2', type=str, help='Sources lists location')
    second.add_argument('--keys-2', type=str, help='Keys location')
    second.add_argument('-u', '--update-cache', action='store_true', help='Force cache update')
    second.add_argument('-r', '--remove-cache', action='store_true', help='Remove cache folders for both repositories')
    args = parser.parse_args()

    main(args)
