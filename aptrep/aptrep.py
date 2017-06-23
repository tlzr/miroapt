#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apt
import logging
import os
import re
import shutil
import urllib


class Repository:
    def prepare_cache(self, cache_dir='cache', sources_lists='/etc/apt/sources.list', keys='/etc/apt/trusted.gpg', force_cache_update=False):
#        path_to_sources_list = os.path.join(cache_dir, 'etc/apt/sources.list.d')

        if not os.path.exists(cache_dir):
            apt.cache.Cache(rootdir=cache_dir)
            force_cache_update=True

        path_to_apt = os.path.join(cache_dir, 'etc/apt')
        if sources_lists:
            path_to_sources_list = os.path.join(cache_dir, 'etc/apt/sources.list')
            try:
                if isinstance(sources_lists, list):
                    for sources_list in sources_lists:
                        if not os.path.exists(path_to_sources_list):
                            os.makedirs(path_to_sources_list)
                        shutil.copy2(sources_list, path_to_sources_list)
                else:
                        shutil.copy2(sources_lists, path_to_sources_list)
            except:
                        print('Unexpacted error:', os.sys.exc_info()[0])
                        raise

        if keys:
            path_to_trusted_gpg_d = os.path.join(cache_dir, 'etc/apt/trusted.gpg.d')
            try:
                if not os.path.exists(path_to_trusted_gpg_d):
                    os.makedirs(path_to_trusted_gpg_d)
                if isinstance(keys, list):
                    for key in keys:
                        if key.startswith('http'):
                            if self.download(key, path_to_trusted_gpg_d):
                        else:
                            shutil.copy2(key, path_to_trusted_gpg_d)
                else:
                    shutil.copy2(keys, path_to_trusted_gpg_d)
            except:
                print('Unexpacted error:', os.sys.exc_info()[0])
                raise
        else:
           logging.warning('The key has not been provided.')

        cache = apt.cache.Cache(rootdir=cache_dir)
        if force_cache_update:
            cache.update()

        cache.open(None)

        return cache

    def remove_cache(self, cache_dir):
        if os.path.exists(cache_dir):
            try:
                print('Cache dir: {0} — is going to be deleted.').format(cache_dir)
                shutil.rmtree(cache_dir)
            except:
                print('Unexpacted error:', os.sys.exc_info()[0])
                raise

    def download(self, url, save_to_path):
            save_to_path = os.path.join(save_to_path, filename)
            url = sanitize_link(url)
            if url:
                filename = get_file_from_link(url)
            if filename:
                try:
                    urllib.urlretrieve(url, filename=filename)
                except:
                    print('Unexpacted error:', os.sys.exc_info()[0])
                    raise
                return True
            return False

    def get_file_from_link(self, url)
        if url:
            url.split('/')
            filename = url.splot('/')[-1]
        if filename:
            return filename
        return None

    def sanitize_link(self, url):
        url = url.strip()
        if url:
            return url
        return None

