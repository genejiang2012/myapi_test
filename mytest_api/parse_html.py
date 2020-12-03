#!/usr/bin/env python3
"""
File: parse_html.py
Author: Gene Jiang
Email: genejiang2012@outlook.com
Github: https://github.com/genejiang2012
Description: 
"""

from bs4 import BeautifulSoup

my_file = '../mytest_api/report.html'
f = open(my_file, 'r')
soup = BeautifulSoup(f.read(), 'html.parser')
print(soup.title)

