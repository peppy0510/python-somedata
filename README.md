
## Installation

```bash
pip install git+http://muteklab.com:9000/root/python-somedata.git
```

```bash
pip uninstall somedata
```

## Example

```python
from somedata import somedata
some = somedata()
```

```python
some.bool(0.5)
>>> True
```

```python
some.word()
>>> 'python'
some.word(language='KO')
>>> '파이썬'
```

```python
some.text(1, 5)
>>> 'python is a language'
some.text(1, 5, language='KO')
>>> '파이썬은 언어다'
```

```python
some.name()
>>> 'Tommy Jake'
some.name(language='KO')
>>> '홍길동'
```

```python
some.loginid()
>>> 'someloginid'
```

```python
some.email()
>>> 'someemail@google.com'
```

```python
some.phone()
>>> '739-5645-4212'
```

```python
some.country()
>>> ('BE', 'Belgium')
some.country_code()
>>> 'BE'
some.country_name()
>>> 'Belgium'
```

```python
some.serial(16)
>>> 'xhRsZVAr0ww43fXy'
some.hexdigit(16)
>>> 'fed3a2a64206ac75'
```

```python
some.date('1980-01-01', '2010-12-31')
>>> '1990-01-14 15:43:59+0000'
some.dates('1980-01-01', '2010-12-31', [60, 80])
>>> ('2010-12-03 02:09:20+0000', '2011-02-21 02:09:20+0000')
```

```python
some.image()
>>> 'base64 encoded image data'
some.image(b64encode=False)
>>> 'image file object'
```

```python
some.avatar()
>>> 'base64 encoded avatar data'
some.avatar(b64encode=False)
>>> 'avatar file object'
```

```python
some.audio()
>>> 'base64 encoded audio data'
some.audio(b64encode=False)
>>> 'audio file object'
```

```python
some.video()
>>> 'base64 encoded video data'
some.video(b64encode=False)
>>> 'video file object'
```

## Repository

```bash
git clone http://muteklab.com:9000/root/python-somedata.git
```

## Reference

[chris1610/barnum-proj](https://github.com/chris1610/barnum-proj/)

[English and European dictionaries *.txt downloads](http://www.gwicks.net/dictionaries.htm)
