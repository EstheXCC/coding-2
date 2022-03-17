from urllib import request
from bs4 import BeautifulSoup
from gensim import corpora
from gensim import models
from gensim import similarities

base_url = 'https://newsroom.wcs.org/News-Releases.aspx'

def get_models(data):
    print('model building')
    stop_list = set('for a of the and to in with'.split(' '))
    texts = [[word for word in (d['title'] + d['body']).lower().split() if word not in stop_list] for d in data]
    dictionary = corpora.Dictionary(texts)
    bow_corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(bow_corpus)
    index = similarities.SparseMatrixSimilarity(tfidf[bow_corpus],
                                                     num_features=len(dictionary.token2id))
    return dictionary, index, tfidf

def get_data(html):
    print('getting data')
    data = []
    soup = BeautifulSoup(html, features="html.parser")
    divs = soup.find_all('div', attrs={'class': 'articleEntry Normal'})
    as_ = soup.find_all('a', attrs={'class':'text-default text-xxl'})
    for i in range (len(divs)):
        p = divs[i].find('p')
        data.append({
            'title': as_[i].string,
            'body': str(divs[i].div.p.string if p is not None else divs[i].div.string),
            'url': as_[i]['href']
        })
    print('get data')
    return data

def search_word(keywords, dictionary,index,tfidf):
    print('serching', keywords)
    words = keywords.lower().split()
    bow = dictionary.doc2bow(words)
    sims = index[tfidf[bow]]
    results = list(enumerate(sims))
    return results

# get url html
def get_url_content(url):
    print('getting html')
    html = request.urlopen(url).read()
    print('get html', url)
    return html

if __name__ == '__main__':
    html = get_url_content(base_url)
    data = get_data(html)
    dictionary, index, tfidf = get_models(data)
    while True:
        key_word = input('input for interesting keywords (0 exit):')
        if key_word == '0':
            break
        results = search_word(key_word, dictionary, index, tfidf)
        print(key_word, 'found:')
        info_count = 0
        for info in results:
            if info[1] != 0:
                info_count = info_count + 1
                print('correlation={}, title={}, url={}, content={}'.format(
                    info[1], data[info[0]]['title'], data[info[0]]['url'], data[info[0]]['body']
                ))
        if info_count == 0:
            print('no found keywords')
