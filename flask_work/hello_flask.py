'''
Created on 2 Sep 2019

@author: peter
'''

from flask import Flask
from search_for_chars import search_for_chars
import sys

app = Flask(__name__)

@app.route('/')
def homepage() ->str:
    return 'Search for letters in a phrase'

@app.route('/search')
def do_search() ->str:
    return str(search_for_chars('life, the universe, then everything', 'aeiou'))

@app.route('/version')
def version() ->str:
    return sys.version

if __name__ == '__main__':
    app.run(debug=True)


        