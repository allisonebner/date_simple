#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:45:34 2018

@author: allisone
"""

import datetime

def get_date_object(date=None):
    if date == None:
        x = datetime.date.today()
    else:
        if not isinstance(date, str):
            raise ValueError('must be a string')
        x = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    return x

def get_date_string(date_object=None, format='YYYY-mm-dd'):
    format = format.lower()
    for item in [['dd', '%d'], ['mm', '%m'], ['yyyy', '%Y'], ['yyy', '%y'], ['yy', '%Y'], ['mon', '%b']]:
        format = format.replace(item[0], item[1])
    if date_object == None:
        date = datetime.date.today()
    else:
        if not isinstance(date_object, datetime.date):
            raise TypeError('must be in date format')
        date = date_object
    return date.strftime(format)


if __name__ == "__main__":
    x = get_date_object()
    print(type(get_date_object('2018-09-09')))
    # print(get_date_string(get_date_object('01/01/2018'), format= "mm-dd-yyyy"))
    print(get_date_string())


        
