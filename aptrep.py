#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apt
import os
import re
import shutil

class Repository:
    def __init__(self):
        self.somevariable = []

    def prepare_cache(self, distr, path_to_cache_dir='cache'):
        if not distr:
            raise 'Please provide distribution name'
        for root, dirs, files in os.walk('sources.list.d'):
            if distr+'.list' not in files:
                print('The list {0} is not in {1} directory.').format(distr+'.list', root)
                raise
            source_list_file = os.path.join(root, distr+'.list')

        cache_dir = os.path.join(path_to_cache_dir)
        if os.path.exists(cache_dir):
            question = raw_input('Directory is already there. Do you want to \
                                  remove it ?\n')
            if re.match('(y|yes)', question, re.IGNORECASE):
                try:
                    shutils.rmtree(cache_dir)
                except:
                    print('Unexpacted error:', sys.exc_info()[0])
                    raise

        cache = apt.cache.Cache(rootdir=cache_dir)
        path_to_sources_list = os.path.join(cache_dir, 'etc/apt/sources.list')
        try:
            shutil.copyfile(source_list_file, path_to_sources_list)
        except:
            print('Unexpacted error:', sys.exc_info()[0])
            raise

        cache.update(fetch_progress=True,sources_list=path_to_sources_list)
        cache.open()

        return cache

    def prepare_apt(self, distr, update_cache=False, cache_path='cache'):
        try:
            current_dir = os.getcwd()
        except:
            current_dir = './'

        path_to_cache = os.path.join(current_dir, cache_path, distr)

        if update_cache:
            cache = self.prepare_cache(path_to_cache, distr)
        else:
            cache = apt.cache.Cache(rootdir=path_to_cache)
            if len(cache) == 0:
                cache = self.prepare_cache(path_to_cache, distr)

                if len(cache) == 0:
                    print('Cache is still empty after update. Check sources list. Aborting.')
                    sys.exit(2)

        return cache


