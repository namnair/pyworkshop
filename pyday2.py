#questions


#QUESTION1
"""
import re
def valid(email):
    regex = r'^(?!.*@(yahoo\.com|hotmail\.com))(?:\S+)@(?:\S+\.(?:com|in|org))$'
    if re.match(regex, email):
        return "valid"
    else:
        return "Invalid"
email= input("Enter an email address: ")
ans = valid(email)
print(ans)
"""

#QUESTION2
#Create a regex pattern to validate phone numbers in a specific format, like (555) 555-5555.
"""
import re
def valid(phno):
    tenregex= r'^\d{10}$'
    countryregex= r'^\+\d{1,4}\s?\d{10}$'
    if re.match(tenregex, phno):
        return f"Valid phone number: {phno} "
    elif re.match(countryregex, phno):
        return "Valid with country code"
    else:
        return "Invalid"
no = input("Enter a phone number: ")
ans = valid(no)
print(ans)
"""

#QUESTION3
#Write a regex pattern to extract the domain (e.g., "example.com") from a URL like "https://www.example.com/page&quot;.
"""
import re
url = input("Enter a URL: ")
regex= r'^https?://(www\.)?([a-zA-Z0-9.-]+).*'
match = re.match(regex, url)
if match:
    domain = match.group(2)
    print(f"Domain extracted: {domain}")
else:
    print("Invalid")
"""

#QUESTION4
#Construct a regex pattern to match dates in the format "MM/DD/YYYY" (e.g., "01/25/2023").
"""
import re
date= input("Enter a date (MM/DD/YYYY): ")
regex = r'(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})'
match = re.findall(regex, date)
if match:
        print("Found date:", date)
else:
    print("Invalid")
"""

#QUESTION5
#Create a regex pattern to remove all HTML tags from a string.
"""
import re
regex = r'<[^>]*>'
date= input("Enter string with HTML tags: ")
strwithout = re.sub(regex, '', date)
print("String: ")
print(strwithout)
"""

#QUESTION6
#Write a regex pattern to match valid IPv4 addresses, e.g., "192.168.1.1".
"""
import re
regex = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
ip=input("Enter ip address: ")
match = re.findall(regex, ip)
if match:
        print("Correct:", ip)
else:
    print("Invalid.")
"""

#QUESTION7
#Build a regex pattern to check the strength of a password, including conditions like at least one uppercase letter, one digit, and a minimum length.
"""
import re
regex = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
pw = input("Enter password: ")
if re.match(regex, pw):
    print("Valid")
else:
    print("Invalid")
"""

#QUESTION8
#Create a regex pattern to extract hashtags from a social media post, e.g., "#regex #practice".
"""
import re
post = input("Enter a social media post: ")
htag = re.findall(r'#\w+', post)
if htag:
    print("Extracted: ")
    for hashtag in htag:
        print(hashtag)
else:
    print("Not found")
"""

#QUESTION9
#Write a regex pattern to find all URLs in a text.
"""
import re
text = input("Enter text: ")
regex = r'https?://\S+|www\.\S+'
urls = re.findall(regex, text)
if urls:
    print("Found URLs:")
    for url in urls:
        print(url)
else:
    print("Not found")
"""

#QUESTION10
#Create a regex pattern to extract all the numbers from a given text.
"""
import re
text = input("Enter text: ")
regex = r'\d+'
matches = re.findall(regex, text)
if matches:
    print("Found:")
    for number in matches:
        print(number)
else:
    print("Not found")
"""


    




