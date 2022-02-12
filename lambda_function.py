import json
import feedparser
from bs4 import BeautifulSoup
import lxml

def lambda_handler(event, context):
    a = feedparser.parse("https://reddit.com/r/java.rss")
    summary_list = json.dumps([{'title': a.entries[0].title, 'summary': a.entries[0].summary, 'link': a.entries[0].link},
    {'title': a.entries[1].title, 'summary': a.entries[1].summary, 'link': a.entries[1].link},
    {'title': a.entries[2].title, 'summary': a.entries[2].summary, 'link': a.entries[2].link},
    {'title': a.entries[3].title, 'summary': a.entries[3].summary, 'link': a.entries[3].link},
    {'title': a.entries[4].title, 'summary': a.entries[4].summary, 'link': a.entries[4].link}, 
    {'title': a.entries[5].title, 'summary': a.entries[5].summary, 'link': a.entries[5].link},
    {'title': a.entries[6].title, 'summary': a.entries[6].summary, 'link': a.entries[6].link},
    {'title': a.entries[7].title, 'summary': a.entries[7].summary, 'link': a.entries[7].link},
    {'title': a.entries[8].title, 'summary': a.entries[8].summary, 'link': a.entries[8].link},
    {'title': a.entries[9].title, 'summary': a.entries[9].summary, 'link': a.entries[9].link},
    {'title': a.entries[10].title, 'summary': a.entries[10].summary, 'link': a.entries[10].link},
    {'title': a.entries[11].title, 'summary': a.entries[11].summary, 'link': a.entries[11].link},
    {'title': a.entries[12].title, 'summary': a.entries[12].summary, 'link': a.entries[12].link},
    {'title': a.entries[13].title, 'summary': a.entries[13].summary, 'link': a.entries[13].link},
    {'title': a.entries[14].title, 'summary': a.entries[14].summary, 'link': a.entries[14].link},
    {'title': a.entries[15].title, 'summary': a.entries[15].summary, 'link': a.entries[15].link},
    {'title': a.entries[16].title, 'summary': a.entries[16].summary, 'link': a.entries[16].link},
    {'title': a.entries[17].title, 'summary': a.entries[17].summary, 'link': a.entries[17].link},
    {'title': a.entries[18].title, 'summary': a.entries[18].summary, 'link': a.entries[18].link},
    {'title': a.entries[19].title, 'summary': a.entries[19].summary, 'link': a.entries[19].link},
    {'title': a.entries[20].title, 'summary': a.entries[20].summary, 'link': a.entries[20].link},
    {'title': a.entries[21].title, 'summary': a.entries[21].summary, 'link': a.entries[21].link},
    {'title': a.entries[22].title, 'summary': a.entries[22].summary, 'link': a.entries[22].link},
    {'title': a.entries[23].title, 'summary': a.entries[23].summary, 'link': a.entries[23].link},
    {'title': a.entries[24].title, 'summary': a.entries[24].summary, 'link': a.entries[24].link}])
    
 
    soup = BeautifulSoup(summary_list, "lxml")
    text = soup.text
    return text
    return {
        'statusCode': 200,
        'body': json.dumps(text)
    }
