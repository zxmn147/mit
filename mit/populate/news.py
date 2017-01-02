from populate import base
from news.models import News
import random

def populate():
    print('Populate News...')
    titles = ['MIT創新服務網正式啟用', '0811舉辦『縮短學用落差論壇』']
    comments = ['正式啟用', '論壇']
    News.objects.all().delete()
    for title in titles:
        news = News()
        news.title = title
        for i in range(10):
            news.content += comments[title.length()-1] + '\n'
    print('done')
    
    
    if __name__ == '__main__':
        populate()