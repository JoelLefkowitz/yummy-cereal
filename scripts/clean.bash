#!/bin/bash
for directory in build dist templ8.egg-info; do
  target=$(pwd)/$directory
  read -p "Would you like to delete $target? `echo $'\n> '`"
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Trying to delete $target"
    if [ -d "$target" ]; then
      rm -rf $target
      echo "Deleted $target"
    else
      echo "Cannot find $target"
    fi
  else
    echo "Skipping $target"
  fi
done