#!/bin/bash

result=`python newrelic_decision.py`
if [ "$result" == "enable" ]; then
    NEW_RELIC_CONFIG_FILE=/etc/newrelic.ini ; export NEW_RELIC_CONFIG_FILE ;  
    newrelic-admin run-program uwsgi --http :8000 --wsgi-file mysite/wsgi.py
else
    #command to run without newrelic

fi
