import bs4
import requests

url='https://www.mycodingzone.net/blog/english'
data= requests.get(url) #it get data from the url
soup = bs4.BeautifulSoup(data.text,'html.parser')

action=input('which thing you want (para / link) :  ')

def paragraph():
    #print(soup.prettify())
    for para in soup.find_all('p'):
        print(para.text)

        
def link():
    i=1
    for links in soup.find_all('a'):
        link = links.get('href')
        if link.startswith('/'):
            print(i,'https://www.mycodingzone.net' + link)
            i+=1
        elif link.startswith('../'):
            print(i,'https://www.mycodingzone.net' + link[:2])
            i+=1

            
if action.lower()=='para':
    paragraph()
elif action.lower()=='link':
    link()
else:
    print('please enter correct option')