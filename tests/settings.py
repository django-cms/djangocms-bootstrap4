#!/usr/bin/env python
# -*- coding: utf-8 -*-

HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'easy_thumbnails',
        'filer',
        'mptt',
        'djangocms_text_ckeditor',
        'djangocms_link',
        'djangocms_picture',
        'djangocms_bootstrap4',
        'djangocms_bootstrap4.contrib.bootstrap4_grid',
        'djangocms_bootstrap4.contrib.bootstrap4_link',
        'djangocms_bootstrap4.contrib.bootstrap4_picture',
    ],
    'ALLOWED_HOSTS': ['localhost'],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'LANGUAGE_CODE': 'en',
}

def run():
    from djangocms_helper import runner
    runner.cms('djangocms_bootstrap4')

if __name__ == '__main__':
    run()
