from bs4 import BeautifulSoup

file=open("index.html")
contents=file.read()
file.close()
#print(contents)

soup=BeautifulSoup(contents,"html.parser")
#print(soup.prettify())
#print(soup.title)
#print(soup.a)
#print(soup.find_all(name="a"))
#print(soup.find(name="a").get('href'))
#for link in soup.find_all(name="a"):
 #   print(link.get("href"))
first=soup.find(class_="para")
print(first.getText())
