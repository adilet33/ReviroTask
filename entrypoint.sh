#!/bin/bash

# Run Alembic migration
alembic upgrade head

# Start uvloop
uvicorn main:app --host 0.0.0.0 --port 8000