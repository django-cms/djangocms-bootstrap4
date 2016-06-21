# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from .conf import settings


def get_additional_styles():
    """
    Get additional styles choices from settings
    """
    choices = []
    raw = getattr(
        settings,
        'ALDRYN_BOOTSTRAP3_CAROUSEL_STYLES',
        getattr(settings, 'GALLERY_STYLES', False)
    )
    if raw:
        if isinstance(raw, str):
            raw = raw.split(',')
        for choice in raw:
            clean = choice.strip()
            choices.append((clean.lower(), clean.title()))
    return choices
