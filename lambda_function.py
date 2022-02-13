import json
import feedparser
from bs4 import BeautifulSoup
import lxml

def lambda_handler(event, context):
    a = feedparser.parse("https://reddit.com/r/java.rss")
    summary_list = 'Title: ' + a.entries[1].title + '. ' + '\n' + 'Post: ' + a.entries[1].summary + '\n' + a.entries[1].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[2].title + '. ' + '\n' + 'Post: ' + a.entries[2].summary + '\n' + a.entries[2].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[3].title + '. ' + '\n' + 'Post: ' + a.entries[3].summary + '\n' + a.entries[3].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[4].title + '. ' + '\n' + 'Post: ' + a.entries[4].summary + '\n' + a.entries[4].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[5].title + '. ' + '\n' + 'Post: ' + a.entries[5].summary + '\n' + a.entries[5].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[6].title + '. ' + '\n' + 'Post: ' + a.entries[6].summary + '\n' + a.entries[6].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[7].title + '. ' + '\n' + 'Post: ' + a.entries[7].summary + '\n' + a.entries[7].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[8].title + '. ' + '\n' + 'Post: ' + a.entries[8].summary + '\n' + a.entries[8].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[9].title + '. ' + '\n' + 'Post: ' + a.entries[9].summary + '\n' + a.entries[9].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[10].title + '. ' + '\n' + 'Post: ' + a.entries[10].summary + '\n' + a.entries[10].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[11].title + '. ' + '\n' + 'Post: ' + a.entries[11].summary + '\n' + a.entries[11].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[12].title + '. ' + '\n' + 'Post: ' + a.entries[12].summary + '\n' + a.entries[12].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[13].title + '. ' + '\n' + 'Post: ' + a.entries[13].summary + '\n' + a.entries[13].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[14].title + '. ' + '\n' + 'Post: ' + a.entries[14].summary + '\n' + a.entries[14].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[15].title + '. ' + '\n' + 'Post: ' + a.entries[15].summary + '\n' + a.entries[15].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[16].title + '. ' + '\n' + 'Post: ' + a.entries[16].summary + '\n' + a.entries[16].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[17].title + '. ' + '\n' + 'Post: ' + a.entries[17].summary + '\n' + a.entries[17].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[18].title + '. ' + '\n' + 'Post: ' + a.entries[18].summary + '\n' + a.entries[18].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[19].title + '. ' + '\n' + 'Post: ' + a.entries[19].summary + '\n' + a.entries[19].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[20].title + '. ' + '\n' + 'Post: ' + a.entries[20].summary + '\n' + a.entries[20].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[21].title + '. ' + '\n' + 'Post: ' + a.entries[21].summary + '\n' + a.entries[21].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[22].title + '. ' + '\n' + 'Post: ' + a.entries[22].summary + '\n' + a.entries[22].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[23].title + '. ' + '\n' + 'Post: ' + a.entries[23].summary + '\n' + a.entries[23].link + ' .\n' + '\n'\
    + 'Title: ' + a.entries[24].title + '. ' + '\n' + 'Post: ' + a.entries[24].summary + '\n' + a.entries[24].link + ' .\n' + '\n' 

    soup = BeautifulSoup(summary_list, "lxml")
    text = soup.text
    return text
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
