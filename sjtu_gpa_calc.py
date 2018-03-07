'''
=============================================================================

The MIT License (MIT)

Copyright (c) 2014 Windy Darian
Copyright (c) 2018 Alex Qiu

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
Modified on Mar 7, 2018

A GPA calculator for Shanghai Jiao Tong University.
just call "python [script_name] test.txt" (Replace test.txt with your own file)
The only module.

@author: Windy Darian
@author: Alex Qiu
'''

import sys

gp_letter = {
    'A+':   4.3,
    'A':    4.0,
    'A-':   3.7,
    'B+':   3.3,
    'B':    3.0,
    'B-':   2.7,
    'C+':   2.3,
    'C':    2.0,
    'C-':   1.7,
    'D':    1.0,
    'F':    0.0,
    'P':    3.3,
    'N':    0.0,
}


def score_to_gp(score):
    '''
    convert a score text (integer or A/B/C/F/P/N) to grade point
    A+ 95-100 4.3
    A  90-94  4.0
    A- 85-89  3.7
    B+ 80-84  3.3
    B  75-79  3.0
    B- 70-74  2.7
    C+ 67-69  2.3
    C  65-66  2.0
    C- 62-64  1.7
    D  60-61  1.0
    F  0-60   0.0
    P         3.3
    N         0.0
    '''
    if score in gp_letter:
        return gp_letter[score]
    else:
        score = int(score)
        if score >= 95:
            return 4.3
        elif score >= 90:
            return 4.0
        elif score >= 85:
            return 3.7
        elif score >= 80:
            return 3.3
        elif score >= 75:
            return 3.0
        elif score >= 70:
            return 2.7
        elif score >= 67:
            return 2.3
        elif score >= 65:
            return 2.0
        elif score >= 62:
            return 1.7
        elif score >= 60:
            return 1.0
        else:
            return 0.0

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
        # text parsing
        line = line.strip()
        if line == '' or line[0] == '#':
            continue
        line = line.split(maxsplit=2)
        credit = line[0]
        score = line[1]
        if len(line) > 2:
            name = line[2]
        else:
            name = ''

        # print and score recording
        cgp = score_to_gp(score)
        ccre = float(credit)
        print('%s\t%s\t%s\t%s' % (ccre, score, cgp, name))
        total_credit += ccre
        total_gp += cgp * ccre

    f.close()
    gpa = (total_gp / total_credit) if total_credit > 0 else 0
    print('GPA: ' + str(gpa))
    return gpa

if __name__ == '__main__':
    calc_gpa(sys.argv[1] if len(sys.argv) > 1 else input("Score file name: "))
    
    
    
    
    
