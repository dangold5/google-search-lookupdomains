# Lookup Domain Names Python script

Simple script to lookup a list of domain names from search terms using the Google Search API. 

## Setup
`
python -m venv .venv
source ./.venv/bin/activate
pip install -r ./requirements.txt
`

Update file:
`input/startupsearchterms.csv`

Inputs:
CSV file of Name, Search term
Google search language to use

Requirements:
Google Customer Search API Key
Doppler secrets account

pip install doppler-env
