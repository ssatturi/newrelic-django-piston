#!/usr/bin/env bash
uwsgi --http :8000 --wsgi-file mysite/wsgi.py
#uwsgi --http :8000 --wsgi-file mysite/wsgi.py --enable-threads

