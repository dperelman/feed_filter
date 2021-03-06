#!/usr/bin/env python3

from sys import stdin, stdout, argv
from xml.etree.ElementTree import ElementTree
import xml


tree = ElementTree()
xml.etree.ElementTree.register_namespace("","http://www.w3.org/2005/Atom")
tree.parse(stdin)

if argv[1] == '--whitelist':
    whitelist=True
    keywordID = argv[2:]
else:
    whitelist=False
    keywordID = argv[1:]
root = tree.getroot()

for node in tree.findall('{http://www.w3.org/2005/Atom}entry'):
    ch = node.find('{http://www.w3.org/2005/Atom}title')
    if ch is not None:
        node_matched = False
        for keyword in keywordID:
            if ch.text.find(keyword) != -1:
                node_matched = True
                break
        if node_matched ^ whitelist:
            root.remove(node)
tree.write(stdout, encoding='unicode')
