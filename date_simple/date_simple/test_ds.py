#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 21:45:34 2018

@author: allisone
"""

import ds
import datetime
import pytest

dateobj1 = ds.get_date_object()  
testdate = datetime.date.today()
dateobj2 = ds.get_date_object(date='2018-02-26')  

datestr = ds.get_date_string()
newstr = ds.get_date_string(date_object=dateobj2)

datestr2 = ds.get_date_string(date_object=dateobj2, format='MM/DD/YYYY')
datestr3 = ds.get_date_string(date_object=dateobj2, format='DD-Mon-YY')  # 26-Feb-18


def test_today():
    assert dateobj1 == testdate

def test_randdate():
    assert dateobj2 == datetime.datetime.strptime('2018-02-26', '%Y-%m-%d').date()

def testtoday2():
    assert datestr == datetime.date.today().strftime('%Y-%m-%d')

def test_randdate2():
    assert newstr == dateobj2.strftime(format='%Y-%m-%d')

def test_extra1():
    assert datestr2 == '02/26/2018'
    
def test_extra2():
    assert datestr3 == '26-Feb-2018'
    
def test_val1():
    with pytest.raises(ValueError):
        ds.get_date_object(date='bad date')
        
def test_type2():
    with pytest.raises(TypeError):
        ds.get_date_string(date_object='not_a_date_object')

def test_type1():
    with pytest.raises(ValueError):
        ds.get_date_object(date=5)
        
