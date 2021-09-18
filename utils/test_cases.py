# -*- coding: utf8 -*- we should add test cases here because we can miss some cases while writing automation code or
# some manuel testers (test analystes) can handle this more efficiently we can obtain test cases from test management
#  tools, I used this for my previous project:
# http://www.inflectra.com/SpiraTest/Integrations/Unit-Test-Frameworks.aspx We can also record the result of test
# cases to test management tool

# for maintainability, we can seperate web test cases by page name but I just listed every case in same array


def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Case 01', 'In the home page click user icon enter credentials and login'],
    ['Case 02', 'Navigate to speaker page, Grab all brands, go to brands and grab products'],
    ['Case 03', 'Navigate to career page, expand all accordions and check email domains'],
    ]
