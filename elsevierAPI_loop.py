'''
Script to run ScienceDirect API to get article information

'''

import json
from urllib2 import urlopen
import sqlite3

SEARCH_URL = 'http://api.elsevier.com/content/search/scidir?'
API_KEY = '9e92e087c4f6a85b7d2250ef59f490de'

conn = sqlite3.connect('SJreader.db')

#date_list = [20160808, 20160809, 20160810, 20160811, 20160812, 20160813, 20160814, 20160815]
date_list = [20160801, 20160802, 20160803, 20160804, 20160805, 20160806, 20160807]

for date in date_list:
    nstart = 0
    url = 'https://api.elsevier.com/content/search/scidir?query=pub-date+IS+%i&content=journals' \
      '&view=complete&count=1&apiKey=%s' %(date, API_KEY)
    x = json.load(urlopen(url))
    num_results = int(x['search-results']['opensearch:totalResults'])
    print(num_results)

    while (nstart < num_results) and (nstart < 5800):
        url = 'https://api.elsevier.com/content/search/scidir?query=pub-date+IS+%i&content=journals' \
              '&view=complete&count=200&start=%i&apiKey=%s' %(date, nstart, API_KEY)
        print('Sending request %i' %nstart)
        x = json.load(urlopen(url))
        print('Received')

        entries = x['search-results']['entry']

        info = []

        for entry in entries:
            authors = []
            try:
                title = entry['dc:title']
                doi = entry['dc:identifier']
                keywords = entry['authkeywords'].split('|')
                abstract = entry['dc:description']
                article_url = entry['link'][1]['@href']
                author_list = entry['authors']['author']
                open_access = entry['openaccessArticle']
                journal = entry['prism:publicationName']
                pub_date = entry['prism:coverDate'][0]['$']
            except:
                print('')
            for author in author_list:
                try:
                    surname = author['surname']
                    given = author['given-name']
                    authors.append('%s, %s' %(surname, given))
                except:
                    print('')
            key1 = ''
            key2 = ''
            key3 = ''
            key4 = ''
            author1 = ''
            author2 = ''
            author3 = ''
            author4 = ''
            author5 = ''
            author6 = ''
            try:
                key1 = keywords[0]
                key2 = keywords[1]
                key3 = keywords[2]
                key4 = keywords[3]
                author1 = authors[0]
                author2 = authors[1]
                author3 = authors[2]
                author4 = authors[3]
                author5 = authors[4]
                author6 = authors[5]
            except:
                print('')


            info_tuple = (title, abstract, journal, author1, author2, author3,
                          author4, author5, author6, doi, article_url, key1, key2,
                          key3, key4, pub_date, open_access)
            info.append(info_tuple)

        conn.executemany('''INSERT INTO recent_articles(title, abstract, journal, author1, author2, author3,
        author4, author5, author6, doi, url, keyword1, keyword2, keyword3, keyword4, pubdate, OA)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); ''', info)
        print('Added articles %i to %i' %(nstart, nstart+200))
        conn.commit()
        nstart+=200


conn.close()