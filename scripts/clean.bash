#!/bin/bash
for directory in build dist templ8.egg-info; do
  target=$(pwd)/$element
  if [ -d "$target" ]; then
    echo Removing $target
    rm -rf $target
  else
    echo $target not found
  fi
done
