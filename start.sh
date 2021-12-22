#!/bin/sh
# use this command with source start.sh

python -m venv myflask
source myflask/bin/activate
export DB_USER=admin
export DB_HOST=ktshmz-free-tier-rds.cstur58da9sb.us-west-2.rds.amazonaws.com
export DB_NAME=flasktest
export DB_PASSWORD=SECRET
