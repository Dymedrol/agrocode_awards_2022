# -*- coding: utf-8 -*-

from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string
from easy_thumbnails.exceptions import InvalidImageFormatError


def send_rich_mail(subject, email_to, email_from, template, data):
    if isinstance(email_to, str):
        email_to = [email_to]

    html = render_to_string(template, data)
    msg = EmailMessage(subject, html, email_from, email_to)
    msg.content_subtype = "html"
    msg.extra_headers = {
        'X-MC-Track': 'opens,clicks_all',
        'X-MC-Autotext': 'true',
    }
    msg.send()
    return msg

def get_picture_url(picture, thumb_alias):
    try:
        if picture:
            return picture[thumb_alias].url
    except IOError:
        pass
    except InvalidImageFormatError:
        pass
    except UnicodeEncodeError:
        pass
    return None
