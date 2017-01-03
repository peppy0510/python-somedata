# encoding: utf-8

'''
author: Taehong Kim


'''

import os


class somedata():

    def __inti__(self):
        self.choice = random.choice

        path = os.path.dirname(os.path,abspath(__file__))
        path = os.path.abspath(os.path.join(path, 'source'))

       for language in ('en', 'ko'):
       	with open(os.path.join(path, language, 'word.txt'), 'rb') as file:
       		