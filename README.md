# Lookup Domain Names Python script

Simple script to lookup a list of domain names from search terms using the Google Search API. 

## Run Script
### Setup Python 
```
python -m venv .venv
source ./.venv/bin/activate
pip install -r ./requirements.txt
```
### Set Environment variables
```
export GOOGLE_SEARCH_KEY_DLOOKUP=
export GOOGLE_CSE_ID_DLOOKUP=
```
### Setup Search
Search terms are in file:
`input/startupsearchterms.csv`

### Run Script
```python
python ./lookupDomains.py
```
### Get Output
See output subfolder

## Notes on Google Search API set up
To set up the necessary environment variables for Google Custom Search in your project, here are the links that guide you through the process for obtaining the required identifiers and keys:

- **GOOGLE_CSE_ID**:
  - **Google Custom Search Engine Setup**: Visit the [Google Custom Search Engine](https://cse.google.com/cse/) page to create or configure your search engine and obtain the CSE ID.

- **GOOGLE_SEARCH_KEY** (commonly referred to as `GOOGLE_API_KEY`):
  - **Google API Key Setup**: For creating and managing API keys, head over to the [Google Cloud Console](https://console.cloud.google.com/). Navigate to "APIs & Services" > "Credentials" to generate a new API key and restrict it for use with the Custom Search API.

These links will direct you to the respective Google services where you can configure and retrieve your CSE ID and API key, which are essential for enabling search functionality in your application.

### Rate Limits
In the context of Google Custom Search, rate limits determine how many search queries you can execute per day or per second. The standard quota allows for 100 search queries per day for free, with a small cost incurred for additional queries beyond this limit. Additionally, the rate limit can impose a cap on the number of queries per second (QPS), which is particularly important for applications expecting high-frequency access.

For users needing higher limits, Google offers the option to increase these quotas through their billing settings in the Google Cloud Console. Managing these limits effectively requires a good understanding of your application's demand and potential peak usage times. To adjust or review your specific rate limits and the associated costs for exceeding them, you should consult the "Quotas" section of the Custom Search API in your [Google Cloud Console](https://console.cloud.google.com/). This section provides detailed information on your current usage, limits, and options for quota increases.
