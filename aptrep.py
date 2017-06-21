#!/usr/bin/env python
# -*- coding: utf-8 -*-

import apt
import os

class repository:
    def __init__(self):
        self.somevariable = []

    def prepare_cache(self, path_to_cache, version):
        cache = apt.cache.Cache(rootdir=path_to_cache)
        path_to_sources_list = os.path.join(path_to_cache, 'etc/apt/sources.list')
        if os.path.exists(path_to_sources_list) and os.stat(path_to_sources_list).st_size == 0:
            if version == 'debian':
                sources = """
#------------------------------------------------------------------------------#
#                            Debian REPOS                                      #
#------------------------------------------------------------------------------#
"""

            with open(path_to_sources_list, 'w') as file:
                file.write(sources)
                file.close()

        cache.clear()
        cache.update()
        cache.open()

        return cache

    def prepare_apt(self, version, update_cache=False, cache_path='cache'):
        try:
            current_dir = os.getcwd()
        except:
            current_dir = './'

        path_to_cache = os.path.join(current_dir, cache_path, version)

        if update_cache:
            cache = self.prepare_cache(path_to_cache, version)
        else:
            cache = apt.cache.Cache(rootdir=path_to_cache)
            if len(cache) == 0:
                cache = self.prepare_cache(path_to_cache, version)

                if len(cache) == 0:
                    print('Cache is still empty after update. Check sources list. Aborting.')
                    sys.exit(2)

        return cache


