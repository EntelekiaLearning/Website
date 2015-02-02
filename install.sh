#!/bin/bash

#@Note: run as admin
#@Deps: Python, Python Pip, NodeJS, NPM

echo '--------------------------------------';
echo '--- Installing Server Dependencies ---';
echo '--------------------------------------';
pip install pyjade==3.0.0
pip install Flask==0.10.1
echo '--------------------------------------';
echo '--- Installing Client Dependencies ---';
echo '--------------------------------------';
npm install -g grunt-cli grunt
npm --prefix ./src/static install
