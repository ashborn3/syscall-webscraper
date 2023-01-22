import requests
from bs4 import BeautifulSoup
import csv

url = "https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/"

flist=[]

source = requests.get(url)
content = BeautifulSoup(source.content,"lxml")

list_tr = content.find_all("tr")

list_head = list_tr[0].find_all("th")

for i in range(len(list_head)):
    list_head[i] = list_head[i].text

flist.append(list_head)

for i in range(1,len(list_tr)):
    list_row = list_tr[i].find_all("td")
    for i in range(len(list_row)):
        list_row[i] = list_row[i].text
    flist.append(list_row)

file = "linux-syscall-table-for-x86_64.csv"

with open(file,"w") as handle:
    writer = csv.writer(handle)
    writer.writerows(flist)

print(0)