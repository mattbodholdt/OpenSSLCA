#!/usr/bin/env python

import base64, urllib, sys
file=sys.argv[1]
with open(file, "rb") as req:
    str = base64.b64encode(req.read())

print urllib.quote_plus(str)
