import csv
import json
import os
import sys
import traceback
from datetime import datetime
from itertools import cycle
from random import uniform
from time import sleep
from urllib.parse import quote_plus

#checking and setting up the environment 
try:
    import httpx
    import pandas as pd
    import undetected_chromedriver as uc
    from loguru import logger
    from pydash import get as _
    from selectolax.parser import HTMLParser
except:
    print('Installing dependencies...')
    try:
        os.system(
            'pip install -U selectolax loguru psutil pydash pandas xlsxwriter')
    except:
        os.system(
            'pip3 install -U selectolax loguru psutil pydash pandas xlsxwriter'
        )
    import httpx
    import pandas as pd
    import undetected_chromedriver as uc
    from loguru import logger
    from pydash import get as _
    from selectolax.parser import HTMLParser

maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

#sign into crunchbase with the API associated with your account      
API_KEY = '5997205bf36a0f923c14066e7ae6408a'

#helper function converting file to a list
def file2list(filename):
    if os.path.isfile(filename):
        with open(filename, encoding='utf-8') as f:
            return [x.strip() for x in f.read().splitlines() if x.strip()]
    return []

#access the proxy server indicated in "proxy.txt" and return proxy server URLs
def load_proxy(fn='./proxy.txt'):
    proxies = set()
    if os.path.exists(fn):
        with open(fn, 'r') as f:
            for line in f:
                px = line.strip().split(':')
                proxies.add(f'http://{px[2]}:{px[3]}@{px[0]}:{px[1]}')
    #if the file with proxy server information does not exist 
    if not proxies:
        raise Exception('No proxy found')
    return proxies

#create an infinite iterator that cycles through the set of proxy URLs returned by the previous function
proxies = cycle(load_proxy(os.path.join(os.getcwd(), 'proxy.txt')))

#helper function introducing random delays between requests 
def rand_sleep(from_min, to_max):
    sleep(uniform(from_min, to_max))

#helper function making HTTP GET requests to a given URL while adding proxy servers
def fetch(url, method='GET', headers=None, retry=3, proxy=None):
    for rt in range(retry):
        session = httpx.Client(timeout=30,
                               follow_redirects=True,
                               proxies={'all://': proxy} if proxy else None)
        if True:
            try:
                if method == 'GET':
                    r = session.get(url, headers=headers)
                elif method == 'POST':
                    r = session.post(url, headers=headers)
                else:
                    raise Exception(f'Invalid method: {method}')
                if r.status_code == 200:
                    return r
            except Exception as e:
                logger.error(f'Error: {e}')
                traceback.print_exc()

#helper function getting search response from Crunchbase API and converts the response's JSON into python objects
def search(term):
    response = fetch(
        f'https://api.crunchbase.com/api/v4/autocompletes?query={quote_plus(term)}&collection_ids=organizations&limit=25&user_key={API_KEY}'
    )

    js = response.json()
    with open('search.json', 'w') as f:
        json.dump(js, f, indent=4)
    first_result = None
    for entity in _(js, 'entities') or []:
        v = (_(entity, 'identifier.value')
             or '').lower().replace("'", '').replace('’', '')
        if v == term.lower().replace("'", '').replace('’', ''):
            return _(entity, 'identifier.permalink')
        if not first_result:
            first_result = _(entity, 'identifier.permalink')
    return first_result


@logger.catch

#searching for a single company on Crunchbase API and extracts specific information, including number of acquisitions, exits, investments, total funding amount, number of lead investors, number of investors, country, and industry
def scrape_company(company, writer, f):
    logger.info(f'Searching {company}...')
    #obtion json information of the company
    slug = search(company)
    print(company, slug)
    if not slug:
        return

    for ii in range(2):
        if True:
            if True:
                try:
                    headers = {
                        'authority': 'www.crunchbase.com',
                        'accept': 'application/json, text/plain, */*',
                        'cookie':
                        'authcookie=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIwODgyOWE4NC00OTBkLTQzMWQtOTdhNS00YWRiMmFjMGNjNjYiLCJpc3MiOiJ1c2Vyc2VydmljZV9kYTc0NTFkOF82NTkiLCJzdWIiOiJlNDMxNmY1Zi1kMjI5LTQ1YjAtODQzYy1iNDc0YWIxZWYwMmQiLCJleHAiOjE2Nzg3NTg2NzMsImlhdCI6MTY3ODc1ODM3MywicHJpdmF0ZSI6IlhBbVRTc2V5enVsWjVuRE5BTnlJOTRuUjNoQ01tN0wvczVwaGdQekpFZDRxR29xZ1FXaE0vZ252LzJJNmJPbTI5dHQ2STZjZGRVNnRQTlVoMzl0TUJVQ1VRY3QycEhyUXg3eUQydEV4YS9aWnJoLzFpS2dXQ2JjVk1GeWlDQWpiZldNcUx0RU1qTnFBME9Na3pjNHpHOGxIc3JPeXJsN2JMYnBrOEliVWxzQUZwMzI2V2w5NERBRWJLamZhTXlOSEVuditOQ2JmTUw5cDV1TWNzenZ5S3dNNnZCcXE1RE5hUng3TnJRQmsvL25SNXpuREtNNkJyRFJSY2NWRTNlbjkvUVJhMDlkMmJkekp1Qy9WVk8ycmtYOEU1OUVOc0N3elczV3UxdklSWlkrN2JIL1EvZXVCN1hVWGptMFd2cU85RHI1UGFvQnRib3hpSWxlb3NMcjRHL2ZaMlJGdklueDRSR0xWMWFwVUpIS2JmYUt4SlowSm9wWWUrZXJlUHR1NE9TRkw1N1d5WGEyWTNPSUFuUld4cnlVYnUxcGVmUW90d3F6akFrTmFlT3lrdmEvTlUyR2taTWtpZHZFRjhpS04iLCJwdWJsaWMiOnsic2Vzc2lvbl9oYXNoIjoiMTc3MDA2NjI5OSJ9fQ.HATfNrBCF4UpqkI_C6JEPc5p0NUpP_9TfanvPQjPL5gR7BF7UDImkl6OxoNoi7TXLJZLuagkLfAiImUhsuth8Q',
                        'pragma': 'no-cache',
                        'referer':
                        f'https://www.crunchbase.com/organization/{slug}',
                        'user-agent':
                        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
                        'x-cb-client-app-instance-id':
                        '9e1b5ea8-3f2d-477e-a023-a9a649232282',
                        'x-requested-with': 'XMLHttpRequest',
                    }
                    #adding proxy to company's url
                    url = f'https://www.crunchbase.com/v4/data/entities/organizations/{slug}?field_ids=%5B%22identifier%22,%22layout_id%22,%22facet_ids%22,%22title%22,%22short_description%22,%22is_locked%22%5D&layout_mode=view_v2'
                    proxy = next(proxies)
                    r = fetch(url, headers=headers, proxy=proxy)
                    js = r.json()
                    with open('test.json', 'w', encoding='utf-8') as f2:
                        json.dump(js, f2, indent=2, ensure_ascii=False)
                    country = None
                    for ct in _(
                            js,
                            'cards.company_about_fields2.location_identifiers'
                    ) or []:
                        if _(ct, 'location_type') == 'country':
                            country = _(ct, 'value')
                            break
                    if not country:
                        for ct in _(
                                js,
                                'cards.investor_about_fields2.location_identifiers'
                        ) or []:
                            if _(ct, 'location_type') == 'country':
                                country = _(ct, 'value')
                                break
                    #indicating and extracting desired features in json file
                    data = {
                        'Company':
                        company,
                        'URL':
                        f'https://www.crunchbase.com/organization/{slug}',
                        'Acquisitions':
                        _(
                            js,
                            'cards.company_overview_highlights.num_acquisitions'
                        ) or _(
                            js,
                            'cards.investor_overview_highlights.num_acquisitions'
                        ) or
                        _(js, 'cards.investments_highlights.num_acquisitions')
                        or _(js,
                             'cards.acquisitions_headline.num_acquisitions'),
                        'Exits':
                        _(js, 'cards.company_overview_highlights.num_exits')
                        or _(js, 'cards.exits_summary.num_exits')
                        or _(js, 'cards.exits_headline.num_exits')
                        or _(js, 'cards.overview_investor_fields.num_exits') or
                        _(js, 'cards.company_financials_highlights.num_exits'),
                        'Investments':
                        _(js,
                          'cards.company_overview_highlights.num_investments')
                        or _(js, 'cards.investments_summary.num_investments')
                        or _(js, 'cards.investments_headline.num_investments')
                        or _(
                            js,
                            'cards.company_financials_highlights.num_investments'
                        ),
                        'Total Funding Amount':
                        _(
                            js,
                            'cards.company_overview_highlights.funding_total.value_usd'
                        ) or _(
                            js,
                            'cards.investor_financials_highlights.funding_total.value_usd'
                        ) or _(
                            js,
                            'cards.funding_rounds_summary.funding_total.value_usd'
                        ) or _(
                            js,
                            'cards.investor_overview_highlights.funding_total.value_usd'
                        ),
                        'Number of Lead Investors':
                        _(
                            js,
                            'cards.company_financials_highlights.num_lead_investors'
                        )
                        or _(js, 'cards.investors_headline.num_lead_investors')
                        or _(
                            js,
                            'cards.investor_financials_highlights.num_lead_investors'
                        ),
                        'Number of Investors':
                        _(js,
                          'cards.company_financials_highlights.num_investors')
                        or _(js, 'cards.investors_summary.num_investors') or _(
                            js,
                            'cards.investor_overview_highlights.num_investors')
                        or _(js, 'cards.investors_headline.num_investors'),
                        'Country':
                        country,
                        'Industry':
                        ', '.join(
                            _(x, 'value') for x in
                            _(js, 'cards.overview_fields_extended.categories')
                            or [] if _(x, 'value')),
                    }
                    writer.writerow(data)
                    f.flush()
                    scraped.add(company)
                    break
                except KeyboardInterrupt:
                    raise KeyboardInterrupt('Stop by user')
                except OSError:
                    pass
                except:
                    logger.exception('There was an error. Retrying...')


csv_headers = [
    "Company", 'URL', "Acquisitions", "Exits", "Investments",
    "Total Funding Amount", "Number of Lead Investors", "Number of Investors",
    "Country", "Industry"
]
scraped = set()

#calls all functions above and save them into a ".xlsx" file
def main():
    output = os.path.join(os.getcwd(), 'crunchbase.csv')
    mode = "a" if os.path.exists(output) else "w"
    if mode == "a":
        with open(output, encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)
            for line in reader:
                if any(line):
                    scraped.add((line[0]))
    logger.info(f'Scraping {len(scraped)} events')

    with open(output, mode, newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_headers)
        if mode == "w":
            writer.writeheader()
            f.flush()
        for ii in range(3):
            for company in file2list(os.path.join(os.getcwd(),
                                                  'startups.txt')):
                if company not in scraped:
                    scrape_company(company, writer, f)

    df = pd.read_csv(output, dtype=str)
    print(f'Before dedup: {len(df)}')
    df.drop_duplicates(inplace=True)
    print(f'After dedup: {len(df)}')
    writer = pd.ExcelWriter(output.replace(".csv", ".xlsx"),
                            engine='xlsxwriter',
                            options={'strings_to_urls': False})
    df.to_excel(writer, index=False)
    writer.close()


if __name__ == '__main__':
    import argparse
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    today = datetime.today().strftime('%Y-%m-%d')
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default=f'crunchbase.csv')
    parser.add_argument('--headless', action='store_true')
    parser.add_argument('-t', '--threads', type=int, default=4)
    args = parser.parse_args()
    headless_mode = args.headless
    output = args.output
    main()
