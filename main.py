#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'esemi'

import timeit


def test_imghdr(filename):
    import imghdr

    try:
        fd = open(filename, 'rb').read()
        return (imghdr.what(None, fd) == 'jpeg')
    except:
        return False


def test_pil(filename):
    from PIL import Image
    from cStringIO import StringIO

    try:
        file_data = StringIO(open(filename, 'rb').read())
        im = Image.open(file_data)
        im.verify()
        return (im.format == 'JPEG')
    except:
        return False

if __name__ == '__main__':

    assert test_imghdr('test.jpg') == True
    assert test_imghdr('unvalid.jpg') == False
    assert test_imghdr('notfound.jpg') == False

    assert test_pil('test.jpg') == True
    assert test_pil('unvalid.jpg') == False
    assert test_pil('notfound.jpg') == False

    print "test_imghdr %.2f" % timeit.timeit("test_imghdr('test.jpg')", setup="from __main__ import test_imghdr")
    print "test_pil %.2f" %  timeit.timeit("test_pil('test.jpg')", setup="from __main__ import test_pil")