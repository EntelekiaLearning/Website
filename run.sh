#!/bin/bash

echo '--------------------';
echo '--- Starting App ---';
echo '--------------------';
echo '';
./src/static/build.sh && ./src/build.sh "$@"