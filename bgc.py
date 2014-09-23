'''
=============================================================================

The MIT License (MIT)

Copyright (c) 2014 Windy Darian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

=============================================================================

Created on Sep 22, 2014

A GPA calculator for Beihang University.
just call "python bgc.py test.txt" (Replace test.txt with your own file)
The only module.

@author: Windy Darian
'''

import sys

gp_letter = {
             'A': 4.0,
             'B': 3.0,
             'C': 2.0,
             'D': 0.0,
             'F': 0.0,
             'P': 3.3,
             'N': 0.0,
             }


def score_to_gp(score):
    '''
    convert a score text (integer or A/B/C/F/P/N) to grade point
    A:85-100 Excellent (4)
    B:70-84  Good      (3)
    C:60-69  Average   (2)
    F: 0-59  Fail      (0)
    P:60-100 Pass      (3.3)
    N: 0-59  No Pass   (0)
    '''
    if score in gp_letter:
        return gp_letter[score]
    else:
        score = float(score)
        if 85 <= score:
            return 4.0
        elif 70 <= score < 85:
            return 3.0
        elif 60 <= score < 70:
            return 2.0
        else:
            return 0

def calc_gpa(file_name, encoding = 'utf-8'):
    '''
    calculate the gpa, input from a file
    '''
    total_gp = 0.0
    total_credit = 0.0
    try:
        f = open(file_name, encoding = encoding)
    except:
        f = open(file_name)
    for line in f:
        cl = line.strip().split(maxsplit = 2)   #credit score name
        if not cl or not cl[0]: continue
        cgp = score_to_gp(cl[1])
        ccre = float(cl[0])
        print('%s\t%s\t%s\t%s' % (ccre,cl[1],cgp,cl[2]))
        total_credit +=  ccre
        total_gp += cgp * ccre
    f.close()
    gpa = (total_gp / total_credit) if total_credit > 0 else 0
    print('GPA: ' + str(gpa))
    return gpa

if __name__ == '__main__':
    calc_gpa(sys.argv[1] if len(sys.argv) > 1 else input(prompt = "Score file name: "))
    
    
    
    
    