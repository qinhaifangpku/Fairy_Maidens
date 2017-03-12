# -*- coding: utf-8

LANG = 'english'
#wordlist = open('labMTwords-%s.csv' % LANG,'r').read().split('\n')
#scores = open('labMTscores-%s.csv' % LANG,'r').read().split('\n')
import happy as h
s1 = '''
int internet computer shit fuck love
'''

s2 = '''
happy shunny lovely
'''
print h.hi(s1,4,4)

#print h.hi(s2,3,7)
