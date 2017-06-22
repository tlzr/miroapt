#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apt
import os
import re
import shutil

class Repository:
    def __init__(self):
        self.somevariable = []

    def prepare_cache(self, distr, path_to_cache_dir='cache', update_cache=True):
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
            else:
                print('Cache is not going to be updated.')
                update_cache=False

        cache = apt.cache.Cache(rootdir=cache_dir)
        path_to_sources_list = os.path.join(cache_dir, 'etc/apt/sources.list')
        try:
            shutil.copyfile(source_list_file, path_to_sources_list)
        except:
            print('Unexpacted error:', sys.exc_info()[0])
            raise

        if update_cache:
            cache.update(fetch_progress=True,sources_list=path_to_sources_list)
        cache.open()

        return cache

