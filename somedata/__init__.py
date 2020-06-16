# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com
'''


try:
    from .somedata import somedata
except Exception:
    from somedata import somedata  # noqa
