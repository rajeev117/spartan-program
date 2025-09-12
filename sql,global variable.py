#import urllib.request
import webbrowser

#a=urllib.request.urlopen('http://www.google.com/')

import urllib.request
import urllib.parse
request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
#print(request_url.read())

from urllib.parse import *
parse_url=('https://www.geeksforgeeks.org / python-langtons-ant/')
print(parse_url)
print("\n")
unparse_url = unparse_url(parse_url)
print(unparse_url)

# HTTP Error

import urllib.request
import urllib.parse

# trying to read the URL
try:
	x = urllib.request.urlopen('https://www.google.com / search?q = test')
	print(x.read())

# Catching the exception generated
except Exception as e :
	print(str(e))

# importing robot parser class
import urllib.robotparser as rb

bot = rb.RobotFileParser()

# checks where the website's robot.txt file reside
x = bot.set_url('https://www.geeksforgeeks.org / robot.txt')
print(x)

# reads the files
y = bot.read()
print(y)

# we can crawl the main site
z = bot.can_fetch('*', 'https://www.geeksforgeeks.org/')
print(z)

# but can not crawl the disallowed url
w = bot.can_fetch('*', 'https://www.geeksforgeeks.org / wp-admin/')
print(w)

def sum(a,b):
    print(a+b)
#main
x=2
y=3
print(x,y)
sum(x,y)
a = 1

# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)


# Variable 'a' is redefined as a local
def g():
	print('Inside g() : ')

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print ('Inside h() ' ,a)

# Global scope
print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()
print ('global : ',a)
