#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apt
import logging
import os
import re
import shutil

class Repository:

    def prepare_cache(self, distr, path_to_cache_dir='cache', force_cache_update=False, preserve_cache=True, key_path=None):
        if not distr:
            raise 'Please provide distribution name'
        for root, dirs, files in os.walk('sources.list.d'):
            if distr+'.list' not in files:
                print('The list {0} is not in {1} directory.').format(distr+'.list', root)
                raise
            source_list_file = os.path.join(root, distr+'.list')

        cache_dir = os.path.join(path_to_cache_dir)
        if os.path.exists(cache_dir):
            if not preserve_cache:
                try:
                    logging.warning('Cache dir: {0} — is going to be deleted.').format(cache_dir)
                    shutils.rmtree(cache_dir)
                except:
                    print('Unexpacted error:', sys.exc_info()[0])
                    raise
            else:
                logging.warning('Cache is not going to be updated.')
                update_cache=False
        else:
            cache = apt.cache.Cache(rootdir=cache_dir)

        if key_path:
            path_to_trusted.gpg.d = os.path.join(cache_dir, 'etc/apt/trusted.gpg.d')
            try:
                if not os.path.exists(path_to_trusted.gpg.d):
                    os.mkdir(path_to_trusted.gpg.d)
                #shutil.copyfile(key, path_to_trusted.gpg.d)
            except:
                print('Unexpacted error:', sys.exc_info()[0])
                raise
        else:
           logging.notice('The key has not been provided.')

        if force_cache_update:
            path_to_sources_list = os.path.join(cache_dir, 'etc/apt/sources.list')
            cache.update(fetch_progress=True,sources_list=source_list_file)

        cache.open()

        return cache

    def remove_cache(cache_dir):
        if os.path.exists(cache_dir):
            try:
                logging.warning('Cache dir: {0} — is going to be deleted.').format(cache_dir)
                shutils.rmtree(cache_dir)
            except:
                print('Unexpacted error:', sys.exc_info()[0])
                raise

