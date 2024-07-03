# Lookup Domain Names Python script

Simple script to lookup a list of domain names from search terms using the Google Search API. 

## Setup Python 
```
python -m venv .venv
source ./.venv/bin/activate
pip install -r ./requirements.txt
```
## Set Environment variables
```
export GOOGLE_SEARCH_KEY_DLOOKUP=
export GOOGLE_CSE_ID_DLOOKUP=
```

## Setup Search
Search terms are in file:
`input/startupsearchterms.csv`

## Run Script
```python
python ./lookupDomains.py
```

## Output
See output subfolder

