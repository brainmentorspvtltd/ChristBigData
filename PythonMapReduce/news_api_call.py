import urllib.request as url
import json
path = "https://newsapi.org/v2/everything?q=tesla&from=2022-08-07&sortBy=publishedAt&apiKey=695e07af402f4b119f0703e9b19f4683"
response = url.urlopen(path)
data = json.load(response)
articles = data["articles"]
file = open("news.txt", 'ab')
for i in range(len(articles)):
    try:
        print(f"Written : {i} articles")
        news = articles[i]["description"].encode()
        file.write(news)
    except:
        pass
file.close()
