#!/bin/bash
#script that curls
curl -sIX OPTIONS $1 | grep -i "Allow" | cut -d' ' -f2-
