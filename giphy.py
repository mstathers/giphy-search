#!/usr/bin/env python
# 
# Uses the giphy api (https://github.com/Giphy/GiphyAPI) to search for an
# appropriate gif, given arguments.
# 
# Usage:
#  ./giphy.py <search terms>
#
# Example:
#  ./giphy.py funny cats
#

import click
import requests
import json

giphy="http://api.giphy.com/v1/gifs/search?"
api_key="api_key=dc6zaTOxFJmzC"
flags="limit=1"


@click.command()
@click.argument('searchterms', nargs=-1, required=1)
@click.option('--debug', 'debug', is_flag=1, help='Enable debugging.')

def main(searchterms, debug):
    searchterms = cat_and_encode(searchterms)

    if debug:
        print "Search Terms: " + searchterms 

    apiout = api_call(searchterms, debug)
    # pesky newlines
    apiout = apiout.replace("\n", "")
    api_json = json.loads(apiout)
    
    if debug:
        print json.dumps(api_json,
            indent=4,
            separators=(',', ': '))

    print api_json['data'][0]['images']['original']['url']


def cat_and_encode(instr):
    encoded = str()
    for term in instr:
        if encoded == "":
            encoded = term
        else:
            encoded += "+" + term
    return encoded

def api_call(searchterms, debug):
    # http://api.giphy.com/v1/gifs/search?api_key=dc6zaTOxFJmzC&limit=1&q=funny+cat
    url = "{}{}&{}&q={}".format(giphy, api_key, flags, searchterms)
    if debug:
        print "DEBUG URL: " + url + "&fmt=html"
    rout = requests.get(url)
    return rout.text


if __name__ == "__main__":
        main()
