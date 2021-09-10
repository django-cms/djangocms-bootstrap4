#!/usr/bin/env python
HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'easy_thumbnails',
        'filer',
        'mptt',
        'djangocms_text_ckeditor',
        'djangocms_link',
        'djangocms_picture',
        'djangocms_bootstrap5',
        'djangocms_bootstrap5.contrib.bootstrap5_alerts',
        'djangocms_bootstrap5.contrib.bootstrap5_badge',
        'djangocms_bootstrap5.contrib.bootstrap5_card',
        'djangocms_bootstrap5.contrib.bootstrap5_carousel',
        'djangocms_bootstrap5.contrib.bootstrap5_collapse',
        'djangocms_bootstrap5.contrib.bootstrap5_content',
        'djangocms_bootstrap5.contrib.bootstrap5_grid',
        'djangocms_bootstrap5.contrib.bootstrap5_jumbotron',
        'djangocms_bootstrap5.contrib.bootstrap5_link',
        'djangocms_bootstrap5.contrib.bootstrap5_listgroup',
        'djangocms_bootstrap5.contrib.bootstrap5_media',
        'djangocms_bootstrap5.contrib.bootstrap5_picture',
        'djangocms_bootstrap5.contrib.bootstrap5_tabs',
        'djangocms_bootstrap5.contrib.bootstrap5_utilities',
    ],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    # required otherwise subject_location would throw an error in the template
    'THUMBNAIL_PROCESSORS': (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    ),
    'LANGUAGE_CODE': 'en',
    'ALLOWED_HOSTS': ['localhost'],
    'DJANGOCMS_PICTURE_RESPONSIVE_IMAGES': False,
    'DJANGOCMS_PICTURE_RESPONSIVE_IMAGES_VIEWPORT_BREAKPOINTS': [576, 768, 992],
}


def run():
    from app_helper import runner
    runner.cms('djangocms_bootstrap5')


if __name__ == '__main__':
    run()
