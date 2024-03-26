#!/usr/bin/python3
from jinja2 import Template
import sys
import os

if os.path.isdir(sys.argv[1]):
    print("already exists: "+sys.argv[1])
    pass
else:
    print("create: "+sys.argv[1])
    os.makedirs(sys.argv[1])
    pass
os.chdir(sys.argv[1])


tmp = 'Hello {{ string }}!'
template = Template(tmp)
body = template.render(string='World')
print(body)

