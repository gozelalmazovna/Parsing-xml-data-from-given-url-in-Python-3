#Importing url , xml , ssl libraries
import urllib.request , urllib.parse , urllib.error
import xml.etree.ElementTree as ET
import ssl

#Ignore security certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Ask for url from user
url_name = input("Enter - ")
fhand = urllib.request.urlopen(url_name)

#Read data from url
data = fhand.read()
print("Retrieved:" ,len(data) ,"characaters")

#From xml form tree obj
tree = ET.fromstring(data)

#Find relevant tags <Count> in my case
counts = tree.findall('comments/comment/count')
print("Count:" , len(counts))

#From <Count> tag sum all values and return it
sum = 0
for x in range (0,len(counts)):
    sum = sum + int(counts[x].text)
print(sum)
