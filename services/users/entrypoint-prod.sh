#!/bin/sh

echo 'waiting on postgres'
while ! nc -z users-db 5432; do
  sleep 1
done

echo 'postgres started'

gunicorn -b 0.0.0.0:5000 manage:app