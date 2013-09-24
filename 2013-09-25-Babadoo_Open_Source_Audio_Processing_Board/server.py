#! /usr/bin/env python3

import os
import bottle
import os.path

@bottle.route("/<filename:path>")
def pages(filename):
    root = "output"
    if os.path.splitext(filename)[-1] == '':
        filename = os.path.join(filename, "index.html")
    return bottle.static_file(filename, root=root)

@bottle.route("/")
def index():
    return bottle.static_file("index.html", root="output")

if __name__ == "__main__":
    bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

app = bottle.default_app()
