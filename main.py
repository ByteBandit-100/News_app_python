import  requests
import datetime

def search(i):
    title = data['articles'][i]['title']
    descp = data['articles'][i]['description']
    context = data['articles'][i]['content']
    link = str(data['articles'][i]['url'])
    pub_at = data['articles'][i]['publishedAt']
    return title,descp,context,link,pub_at

def today_date():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')

#Use your own api key free from newsapi.org
key = "8******************f"

while True:
        print('-------------- * Global News * -------------- \n')
        print('---> Press Q for quit.\n')
        query = input('Enter what type of news you want : ')
        if query.lower().strip(' ') =='q':
            break
        url = f"https://newsapi.org/v2/everything?q={query}&from={today_date}&sortBy=publishedAt&apiKey={key}"
        try:
            r = requests.get(url)
            data = r.json()
            if data['totalResults'] == 0:
                print(f"🤕 No news found about {query}\n")
                continue
            for index in range(len(data)):
                title,description,content,url_r,published_at = search(index)
                print(f'\n|----- News {index+1}')
                print(f'-> Title : : {title}\n')
                print(f'-> Description :\n{description}\n')
                print(f'-> Content :\n{content}\n')
                print(f'-> URL (For more details..):\n{url_r}\n')
                print(f'-> Published Date-Time:\n{published_at}\n')
                print(f'----- End ---|\n')
        except:
            print('⚠️ No Connection. \n')