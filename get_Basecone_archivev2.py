import os
import requests
import json
import time
import re
import random

# Login op secure.basecone.com en haal de volgende Cookies uit je browser:
cookies = {
    'SelectedTenant': 'VALUE',
    'LoggedInUserId': 'VALUE',
    'CurrentCulture': 'nl-NL',
    'SelectedCompanyId': 'VALUE',
    'WebPortalSessionId': 'VALUE',
    '.ASPXAUTH': 'VALUE',
    'intercom-session-jc1nhv3o': 'VALUE',
    '.AspNet.Cookies': 'VALUE',
    'SessionExpiryTime': 'VALUE',
}

headers = {
    'authority': 'secure.basecone.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://secure.basecone.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://secure.basecone.com/archive/index',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,nl;q=0.7',
}

def get_grid_data():
    data = {
        '_search': 'false',
        'nd': '1628755527660',
        'page': '1',
        'rows': '500',
        'sidx': 'DateModified',
        'sord': 'desc',
        'Company': cookies['SelectedCompanyId'],
        'FileName': '',
        'DateModifiedFrom': '',
        'DateModifiedUntil': '',
        'BookingNumber': '',
        'InvoiceDateFrom': '',
        'InvoiceDateUntil': '',
        'InvoiceNumber': '',
        'PurchaseOrderNumber': '',
        'TotalAmountFromString': '',
        'TotalAmountUntilString': '',
        'Description': ''
    }

    response = requests.post('https://secure.basecone.com/archive/GridData', headers=headers, cookies=cookies, data=data)
    json_response = json.loads(response.content)
    return(json_response)


def download_invoice(grid_data):
    for row in grid_data["rows"]:

        params = (
            ('ids', row["DocumentId"]),
        )

        filename = "pdf/{} - {} - {}.pdf".format(row["BookingNumber"],row["InvoiceDate"], row["DocumentNameForDisplay"])
        if not os.path.exists(filename):
            response = requests.get('https://secure.basecone.com/Archive/Download', headers=headers, params=params, cookies=cookies)
            file = open(filename, 'wb')
            file.write(response.content)
            file.close()

            print("Downloading: {}, {}".format(row["DocumentId"],filename))
            time.sleep(random.randint(0,3))
        else:
            print("Skipping:    {}, {}".format(row["DocumentId"],filename))

grid_data = get_grid_data()
download_invoice(grid_data)


