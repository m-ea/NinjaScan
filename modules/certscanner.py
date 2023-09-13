import config
import requests
from bs4 import BeautifulSoup
from datetime import datetime

now = datetime.now()

def isNotExpired(expiration_date):
    if expiration_date > now:
        return True
    return False

def NotOnSubdomainList(subdomain, valid_subdomains):
    if subdomain not in valid_subdomains:
        return True
    return False

def FormatList(valid_subdomains):

    final_subdomains_list = [] # Holds final list of subdomains
    
    for sublist in valid_subdomains:
        # Breaks up lists of domains longer than 1
        if len(sublist) > 1:
            i = 0
            for j in sublist:
                # Ignores line breaks that make up odd number list indexes
                if sublist.index(sublist[i]) % 2 == 0:
                    final_subdomains_list.append(sublist[i])
                i = i + 1
        elif len(sublist) == 1:
            # Lists of 1 simply have their strings added to the list
            final_subdomains_list.append(sublist[0])
    
    return final_subdomains_list

def CertScanner():
    endpoint = 'https://crt.sh/?q=' + config.domain
    request = requests.get(endpoint)

    valid_subdomains = []

    # Parse HTML and get all table rows
    soup = BeautifulSoup(request.text, features="html.parser")
    trimmed_soup = soup.find_all('tr')

    # Skip the first few table rows and start iterating
    for table_row in trimmed_soup[3:]:
        # Establishes certificate expiration date
        date_string = str(table_row.contents[7].contents[0])
        expiration_date = datetime.strptime(date_string.strip(), '%Y-%m-%d')
        # Extract list of subdomains under the certificate being iterated
        subdomain = table_row.contents[11].contents
        # Subdomains with unexpired certs are added to a list
        if isNotExpired(expiration_date) and NotOnSubdomainList(subdomain, valid_subdomains):
            valid_subdomains.append(table_row.contents[11].contents)

    for x in FormatList(valid_subdomains):
        print(x, end="\n")

if "__name__" == "__main__":
    CertScanner()