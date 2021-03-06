# encoding: utf-8


'''
author: Taehong Kim
email: peppy0510@hotmail.com
'''


import base64
import datetime
import io
import json
import os
import random
import re
import string


class somedata():

    def __init__(self):
        self.choice = random.choice

        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.path.join(path, 'source'))

        for language in ('en', 'ko'):
            with open(os.path.join(path, language, 'word.txt'), 'rb') as file:
                values = file.read().decode('utf-8').split('\n')
                values = [v.strip() for v in values if len(v) > 0]
                setattr(self, '_data_word_' + language, values)
            with open(os.path.join(path, language, 'name.txt'), 'rb') as file:
                values = file.read().decode('utf-8').split('\n')
                values = [v.strip() for v in values if len(v) > 0]
                setattr(self, '_data_name_' + language, values)

        with open(os.path.join(path, 'emailhost.txt'), 'rb') as file:
            values = file.read().decode('utf-8').split('\n')
            values = [v.strip() for v in values if len(v) > 0]
            self._data_emailhost = values

        with open(os.path.join(path, 'country.json'), 'rb') as file:
            values = json.loads(file.read().decode('utf-8'))
            self._data_country = values

        for name in ('avatar', 'image', 'audio', 'video'):
            self.set_media_path(name)

    def bool(self, true_percentage=None):
        '''
        True, False 값을 확률에 기반하여 랜덤으로 반환.
        '''
        if true_percentage is None or true_percentage == 0.5:
            return self.choice([True, False])
        bools = [True] * int(true_percentage * 100) \
            + [False] * int((1 - true_percentage) * 100)
        return self.choice(bools)

    def num(self, gte, lt=None, step=1):
        '''
        범위에 해당하는 숫자를 랜덤으로 반환.
        '''
        if gte == lt:
            return gte
        if lt is None:
            lt, gte = (gte, 0)
        return self.choice(range(gte, lt, step))

    def text(self, gte, lt=None, step=1, language='EN'):
        '''
        텍스트를 랜덤으로 반환.
        특수문자가 없으며 띄어쓰기만 존재.
        '''
        num = self.num(gte, lt, step)
        sources = getattr(self, '_data_word_' + language.lower())
        return ' '.join([self.choice(sources) for _ in range(num)])

    def word(self, language='EN'):
        '''
        단어를 랜덤으로 반환.
        '''
        values = getattr(self, '_data_word_' + language.lower())
        return self.choice(values).strip()

    def serial(self, num):
        '''
        숫자와 알파벳 대소문자의 조합으로 이루어진 랜덤 스트링을 반환.
        '''
        chars = string.digits + string.ascii_letters
        return ''.join([self.choice(chars) for i in range(num)])

    def hexdigit(self, num):
        '''
        16진수를 랜덤으로 생성하여 반환.
        '''
        return ''.join([self.choice(string.hexdigits[:16]) for i in range(num)])

    def name(self, language='EN'):
        '''
        이름을 랜덤으로 생성하여 반환.
        '''
        if language.upper() == 'KO':
            return self.choice(self._data_name_ko).strip()
        name = []
        for _ in range(0, self.num(self.choice([1, 2]), self.choice([3, 4]))):
            name += [self.choice(self._data_name_en).strip().capitalize()]
        return ' '.join(name)

    def loginid(self, gte=5, lt=16):
        '''
        로그인아이디를 랜덤으로 생성하여 반환.
        '''
        uid = ''
        for _ in range(lt + 1):
            sources = self.choice([self._data_name_en, self._data_word_en])
            uid += self.choice(sources).lower().strip()
        suffix = ''
        if self.bool():
            suffix = str(self.num(0, 10000))
        uid = uid[:self.num(gte, lt - 3)] + suffix
        return uid[:lt + 1]

    def email(self, prefix=None):
        '''
        이메일을 랜덤으로 생성하여 반환.
        '''
        if prefix is None:
            prefix = self.loginid()
        return '@'.join([prefix, self.choice(self._data_emailhost)])

    def phone(self):
        '''
        전화번호를 랜덤으로 반환.
        '''
        value = '%03d-%04d-%04d' % (self.num(1000),
                                    self.num(10000), self.num(10000))
        return value

    def country(self):
        '''
        국가코드와 국가명을 랜덤으로 반환.
        '''
        value = self.choice([v for v in self._data_country])
        return value['Code'], value['Name']

    def country_code(self):
        '''
        국가코드를 랜덤으로 반환.
        '''
        return self.choice([v['Code'] for v in self._data_country])

    def country_name(self):
        '''
        국가명을 랜덤으로 반환.
        '''
        return self.choice([v['Name'] for v in self._data_country])

    def ip_address(self, ip_base=None):
        '''
        아이피주소를 랜덤으로 반환.
        '''
        ip_base_parts = (ip_base or '').split('.')
        ip_base_parts = [v for v in ip_base_parts if v]
        value = '{}.{}.{}.{}'.format(
            *ip_base_parts,
            *[self.choice(range(1, 255)) for _ in range(4 - len(ip_base_parts))])
        return value

    def date(self, start, end):
        '''
        두 날짜 사이의 날짜시간을 랜덤으로 반환.
        ex) some.date('1979-05-10', '2016-05-10')
        '2010-10-14 13:40:04+0000'
        '''
        def random_datetime(start, end):
            delta = end - start
            int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
            random_second = random.randrange(int_delta)
            return start + datetime.timedelta(seconds=random_second)

        if len(start.split(' ')) == 2:
            d1 = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        else:
            d1 = datetime.datetime.strptime(start, '%Y-%m-%d')

        if len(end.split(' ')) == 2:
            d2 = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        else:
            d2 = datetime.datetime.strptime(end, '%Y-%m-%d')

        return random_datetime(d1, d2).strftime('%Y-%m-%d %H:%M:%S+0000')

    def dates(self, start, end, days):
        '''
        두 날짜 사이의 두 날짜시간을 랜덤으로 반환.
        두 날짜 사이의 기간을 얻는데 사용할 수 있음.
        공지기간 등을 생성하는데 사용.
        ex) some.date('1979-05-10', '2016-05-10')
        ('2010-10-14 13:40:04+0000', '2011-01-02 13:40:04+0000')
        '''
        started = datetime.datetime.strptime(
            self.date(start, end), '%Y-%m-%d %H:%M:%S+0000')
        finished = started + datetime.timedelta(days=self.choice(days))
        started = started.strftime('%Y-%m-%d %H:%M:%S+0000')
        finished = finished.strftime('%Y-%m-%d %H:%M:%S+0000')
        return started, finished

    def set_media_path(self, name):
        path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.abspath(os.path.join(path, 'media', name))
        paths = [os.path.join(path, v) for v in os.listdir(path)]
        setattr(self, '_%s_path' % (name), paths)

    def get_media(self, paths, b64encode=True):
        path = os.path.abspath(self.choice(paths))
        if b64encode:
            with open(path, 'rb') as file:
                return base64.b64encode(file.read()).decode('utf-8')
        else:
            return path

    def image(self, b64encode=True):
        return self.get_media(self._image_path, b64encode=b64encode)

    def avatar(self, b64encode=True):
        return self.get_media(self._avatar_path, b64encode=b64encode)

    def audio(self, b64encode=True):
        return self.get_media(self._audio_path, b64encode=b64encode)

    def video(self, b64encode=True):
        return self.get_media(self._video_path, b64encode=b64encode)


def trim_words(self, source, destination=None):
    if destination is None:
        base, ext = os.path.splitext(source)
        destination = base + '.some' + ext

    with open(source, 'r', encoding='utf-8') as file:
        data = file.read()
    data = data.lower()

    subchars = string.whitespace
    # subchars = string.whitespace + string.punctuation
    subchars = subchars.replace('.', '')
    subchars = '[' + subchars + ']'
    data = [v.strip() for v in re.sub(subchars, ' ', data).split(' ')]

    data = sorted(set([v for v in data if len(v) > 0]))
    with open(destination, 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def __test__():
    import sys
    from io import TextIOWrapper
    sys.stdout = TextIOWrapper(sys.stdout.buffer,
                               encoding='utf-8', errors='replace')
    # trim_words(os.path.join('source', 'ko', 'word.txt'))
    pad = 60
    some = somedata()

    print('some.bool(0.5)'.ljust(pad),
          [some.bool(0.5) for i in range(5)])

    print('some.word()'.ljust(pad), some.word())

    print('some.word(language="KO")'.ljust(pad),
          some.word(language='KO'))

    print('some.text(1, 5)'.ljust(pad),
          some.text(1, 5))

    print('some.text(1, 5, language="KO")'.ljust(pad),
          some.text(1, 5, language='KO'))

    print('some.name()'.ljust(pad), some.name())

    print('some.name(language="KO")'.ljust(pad),
          some.name(language='KO'))

    print('some.loginid()'.ljust(pad), some.loginid())

    print('some.email()'.ljust(pad), some.email())

    print('some.phone()'.ljust(pad), some.phone())

    print('some.country()'.ljust(pad), some.country())

    print('some.country_code()'.ljust(pad), some.country_code())

    print('some.country_name()'.ljust(pad), some.country_name())

    print('some.ip_address()'.ljust(pad), some.ip_address())

    print('some.ip_address(192)'.ljust(pad), some.ip_address('192'))

    print('some.ip_address(192.168)'.ljust(pad), some.ip_address('192.168'))

    print('some.ip_address(192.168.0)'.ljust(pad), some.ip_address('192.168.0'))

    print('some.serial(16)'.ljust(pad), some.serial(16))

    print('some.hexdigit(16)'.ljust(pad), some.hexdigit(16))

    print('some.date("1980-01-01", "2010-12-31")'.ljust(pad),
          some.date('1980-01-01', '2010-12-31'))

    print('some.dates("1980-01-01", "2010-12-31", [60, 80])'.ljust(pad),
          some.dates('1980-01-01', '2010-12-31', [60, 80]))


if __name__ == '__main__':
    __test__()
