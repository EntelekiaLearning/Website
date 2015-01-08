#!/bin/bash

#@Note: run as admin
#@Deps: Python, Python Pip, NodeJS, NPM

echo '--------------------------------------';
echo '--- Installing Server Dependencies ---';
echo '--------------------------------------';
pip install Flask

echo '--------------------------------------';
echo '--- Installing Client Dependencies ---';
echo '--------------------------------------';
npm install -g grunt-cli grunt local-web-server
npm --prefix ./client install
