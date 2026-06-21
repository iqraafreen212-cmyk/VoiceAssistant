import requests
import xml.etree.ElementTree as ET
def get_news():
    articles=[]
    try:
        url="https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
        response=requests.get(url)
        root=ET.fromstring(response.content)
        for item in root.findall('.//item')[:3]:
            title=item.find('title').text
            articles.append({"title": title})
    except Exception as e:
        print(f"News Fetch Error: {e}")
    return articles