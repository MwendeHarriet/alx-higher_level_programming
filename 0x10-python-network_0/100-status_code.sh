#!/bin/bash
#script that curls
curl -s -o dev/null/ -w "%{http_code}" $1
