from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def add(x, y):
    print('lol')
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def hi():
    print('hi pidr')
    return 1
