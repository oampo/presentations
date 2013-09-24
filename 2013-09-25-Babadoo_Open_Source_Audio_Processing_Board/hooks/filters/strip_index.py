import os.path

def strip_index(url):
    head, tail = os.path.split(url)
    if tail == "index.html":
        return head
    return url
