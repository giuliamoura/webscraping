from bs4 import BeautifulSoup

import requests

tempmail = requests.get("https://temp-mail.org/en/").content

soupMail = BeautifulSoup(tempmail, 'html.parser')

mail = soupMail.find("input", class_="emailbox-input opentip")

print (mail)

# html = requests.get("https://thenewscc.com.br/indicacao?grsf=i9xv6q").content

# soup = BeautifulSoup(html, 'html.parser')

# print(soup)

# sendlink = soup.find("span", class_="elementor-button-icon")

# print(sendlink)
