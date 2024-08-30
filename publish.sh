#!/bin/bash
#
# Publish site to pages branch.
#

pelican content -o output -s publishconf.py
ghp-import -m "Generate Pelican site" --no-jekyll -b pages output
git push origin pages
