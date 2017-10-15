# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from djangocms_bootstrap4.contrib.bootstrap4_picture.models import Bootstrap4Picture
from djangocms_bootstrap4.contrib.bootstrap4_link.models import Bootstrap4Link

from .models import (
    Bootstrap4CardImage,
    Bootstrap4CardInner,
    Bootstrap4CardContent,
)


LOREM_TEXT = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed '
              'do eiusmod tempor incididunt ut labore et dolore magna aliqua.')


def create_picture(obj, order=0):
    return Bootstrap4Picture(
        parent=obj,
        placeholder=obj.placeholder,
        language=obj.language,
        position=order,
        plugin_type='Bootstrap4PicturePlugin',
        external_picture='https://dummyimage.com/600x250/777777/dcdcdc',
    )

def create_link(obj, order=0):
    return Bootstrap4Link(
        parent=obj,
        placeholder=obj.placeholder,
        language=obj.language,
        position=order,
        plugin_type='Bootstrap4LinkPlugin',
        name='Go somewhere',
        external_link='https://www.google.com',
        link_type='btn',
        link_context='primary'
    )

def create_card_image(obj, content_type, order=0):
    return Bootstrap4CardImage(
        parent=obj,
        placeholder=obj.placeholder,
        language=obj.language,
        position=order,
        plugin_type='Bootstrap4CardImagePlugin',
        content_type=content_type,
    )

def create_card_inner(obj, inner_type, order=0):
    return Bootstrap4CardInner(
        parent=obj,
        placeholder=obj.placeholder,
        language=obj.language,
        position=order,
        plugin_type='Bootstrap4CardInnerPlugin',
        inner_type=inner_type,
    )

def create_card_content(obj, content_type, order=0, content='', tag_type='div'):
    return Bootstrap4CardContent(
        parent=obj,
        placeholder=obj.placeholder,
        language=obj.language,
        position=order,
        plugin_type='Bootstrap4CardContentPlugin',
        content_type=content_type,
        card_content=content,
        tag_type=tag_type,
    )


# create card type preset
def create_card_blueprint(obj):
    card_image = create_card_image(obj, 'card-img-top')
    obj.add_child(instance=card_image)

    image = create_picture(card_image)
    card_image.add_child(instance=image)

    card_body = create_card_inner(obj, 'card-body', order=1)
    obj.add_child(instance=card_body)

    card_body_text = create_card_content(card_body, 'card-text', content=LOREM_TEXT)
    card_body.add_child(instance=card_body_text)

def create_panel_blueprint(obj):
    card_header = create_card_inner(obj, 'card-header')
    obj.add_child(instance=card_header)

    card_header_text = create_card_content(card_header, 'card-text', content='Card header')
    card_header.add_child(instance=card_header_text)

    card_body = create_card_inner(obj, 'card-body', order=1)
    obj.add_child(instance=card_body)

    card_body_title = create_card_content(card_body, 'card-title', content='Card title', tag_type='h4')
    card_body.add_child(instance=card_body_title)

    card_body_text = create_card_content(card_body, 'card-text', content=LOREM_TEXT)
    card_body.add_child(instance=card_body_text)

    card_footer = create_card_inner(obj, 'card-footer', order=2)
    obj.add_child(instance=card_footer)

    card_footer_title = create_card_content(card_footer, 'card-text', content='Card footer')
    card_footer.add_child(instance=card_footer_title)

def create_teaser_blueprint(obj):
    card_body = create_card_inner(obj, 'card-body')
    obj.add_child(instance=card_body)

    card_body_title = create_card_content(card_body, 'card-title', content='Card title', tag_type='h4')
    card_body.add_child(instance=card_body_title)

    card_body_text = create_card_content(card_body, 'card-text', content=LOREM_TEXT, tag_type='p', order=1)
    card_body.add_child(instance=card_body_text)

    card_body_button = create_link(card_body, order=2)
    card_body.add_child(instance=card_body_button)
