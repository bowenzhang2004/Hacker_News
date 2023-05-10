import requests
from bs4 import BeautifulSoup
import pprint as pp

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.subtext')


def sort_stories_by_votes(hnllist):
    return sorted(hnllist, key=lambda k: k['points'], reverse=True)


def create_custom_hn(links, votes):
    hnl = []

    for idx, item in enumerate(links):
        score = votes[idx].select('.score')
        if len(score) == 0:
            continue

        cp = int(score[0].getText().replace(' points', ''))
        if cp > 99:
            title = item.getText()
            href = item.a['href']
            hnl.append({'title': title, 'link': href, 'points': cp})
    return sort_stories_by_votes(hnl)


pp.pprint(create_custom_hn(links, votes))
