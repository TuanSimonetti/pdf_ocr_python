#!/bin/sh

streamlit run Home.py --server.port=8502 --server.address=0.0.0.0 & uvicorn api_app:app --host 0.0.0.0 --port 8000
