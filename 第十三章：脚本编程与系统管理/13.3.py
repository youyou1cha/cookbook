#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  logging

def main():
    #
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('Host %s unknown',hostname)
    logging.error('Count find ')