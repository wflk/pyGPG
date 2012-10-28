#!/usr/bin/python
# -*- coding: utf-8 -*-
#################################################################################
# pyGPG Config
#################################################################################
# File:       config.py
#
#             Python configuration and options class for
#             an Interface access to gnupg
#
# Copyright:
#             (c) 2012 Brian Dolbec
#             Distributed under the terms of the GNU General Public License v2
#
# Author(s):
#             Brian Dolbec <dolsen@gentoo.org>
#
'''Handles pyGPG's config's.'''



class GPGConfig(object):
    '''holds all options and configuration data
    for running the GnuPG class'''

    def __init__(self):
        self._defaults = {
            'gpg_command': '/usr/bin/gpg',
            'decrypt': '--decrypt',
            'verify': '--verify',
            'sign': '--sign',
            'clearsign': '--clearsign',
            'detach-sign': '--detach-sign',
            'dump-otions': '--dump-options',
            'no-tty': '--no-tty',
            'version': '--version',
        }
        self._options = ['--no-tty',
        ]


    def get_options(self):
        '''Returns the list of default options to be applied to
        all gpg runs except the GnuPG.custom_run()
        '''
        return self._options.copy()


    def get_defaults(self):
        '''Returns a dictionary of the default settings
        '''
        return self._defaults.copy()


    def set_options(self, options):
        '''Sets the options to the value passed in
        @param options: list
        '''
        self._options = options.copy()


    def sign_modes(self, gpg_options=None):
        '''Returns the list of supported signing types
        @param gpg_options: list of gpg options such as those returned by
            GnuPG.dump_options(). If passed in, it will do a set intersection
            of the supported signing modes and gpg_options
        @rtype list: of supported signing options
            '''
        supported = ["clearsign", "sign", "detach-sign"]
        if gpg_options:
            return list(set(supported).intersection(set(gpg_options)))
        return supported


