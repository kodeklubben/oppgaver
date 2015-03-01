#!/bin/bash
cd ${0%/*}
git pull 
./deploy.sh
