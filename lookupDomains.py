from googleapiclient.discovery import build
import os
import re
import tldextract # to extract domain names
import csv
import time

# API Keyes
# Google
api_key = os.environ.get("GOOGLE_SEARCH_KEY_DLOOKUP")
cse_id =  os.environ.get("GOOGLE_CSE_ID_DLOOKUP") # Google Programmable Search Engine ID

# Use Amazon S3 instead of CSV instead of the local filesystem
defaultinput="startupsearchlist.csv"
inputfolder="input"
outputfolder="output"
defaultlanguage="lang_en"
defaultcountry="countryAU"

def google_search(search_term, api_key, cse_id, country, language, **kwargs):
    print(f"Searching for \'{search_term}\' ...")
    service = build("customsearch", "v1", developerKey=api_key)
    # No restriction
    res = service.cse().list(q=search_term, cx=cse_id, cr=country, lr=language, **kwargs).execute() # Brazil 
    # Restricts to country
    #res = service.cse().siterestrict().list(q=search_term, cx=cse_id, cr=country, lr=language, **kwargs).execute() # Brazil
    ds = {"search_term": search_term} # empty dictionary to store search_term, domain, snippet, url, title
    try:
        results = res["items"]
        if not results: # check if no items in the result to avoid indexing error
            ds = {"search_term": search_term, "domain": "", "snippet": "", "url": "", "title": ""}
        else:
            r = results[0] # grab first item from result
            link = r["link"]
            ds["url"] = link
            ds["title"] = r["title"]
            # Extract domain & suffix
            extracted_domain = tldextract.extract(link)
            ds["domain"] = "{}.{}".format(extracted_domain.domain, extracted_domain.suffix)
            ds["snippet"] = r["snippet"]
    except KeyError as ke:
        ds = {"search_term": search_term, "domain": "no result", "snippet": "no result", "url": "no result", "title": "no result"}
    return ds


# 1. Read CSV of startup names and search terms to use (max 100)

# Use Amazon S3 instead of CSV instead of the local filesystem

defaultinput="startupsearchlist.csv"
inputfolder="input"
outputfolder="output"
defaultlanguage="lang_en"
defaultcountry="countryAU"

fileinput = defaultinput
language = defaultlanguage
country = defaultcountry
#fileinput = str(input(f"Which CSV file do you want to open (defaults to \'{defaultinput}\') from {inputfolder} folder? ") or defaultinput)
#language = str(input(f"Which language do you want to use (defaults to \'{defaultlanguage}\')? ") or defaultlanguage)
#country = str(input(f"Which country do you want to use (defaults to \'{defaultcountry}\')? ") or defaultcountry)

# 2. Prompt user for output
# Set default filename to input filename but add -output in filename before csv
defaultoutput = re.sub(r'\.csv$', '-output.csv', fileinput)
fileoutput = defaultoutput
#fileoutput = str(input(f"Which CSV file do you want to write (defaults to \'{defaultoutput}\') in {outputfolder}? ") or defaultoutput)

# read input CSV file containing search terms
input_file_path = inputfolder + "/"+ fileinput
with open(input_file_path, "r") as input_file:
    reader = csv.reader(input_file)
    next(reader) # skip header row
    terms = [row[0] + " " + row[1] for row in reader]

# create output CSV file and write header row
output_file_path = outputfolder + "/" + fileoutput

with open(output_file_path, "w", newline="") as output_file:
    writer = csv.DictWriter(output_file, fieldnames=["search_term","domain", "snippet", "url", "title"])
    writer.writeheader()

    # iterate through search terms and write results to output file
    for term in terms:
        result_dict = google_search(term, api_key, cse_id, country, language)
        time.sleep(0.1)
        # dummy result_dict
        # result_dict = {"search_term": term, "domain": "dummy", "snippet": "dummy", "url": "dummy", "title": "dummy"}
        # print(f"{term}")
        l = writer.writerow(result_dict)

