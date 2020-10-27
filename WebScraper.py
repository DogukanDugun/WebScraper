import  requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
tim = timestr+".xlsx"
nameitem = []
salesitem = []
discountitem=[]
detailitem=[]
URLitem=[]
url = "https://www.kartalotomasyon.com.tr/kategori/servo-motorlar-1"

r = requests.get(url)

soup = BeautifulSoup(r.content,"html.parser")

items = soup.find_all("div", attrs={"class":"_productItem"})
lenght =len(items)
urllist=[]
i=0
while i<lenght:
    itemurl = items[i].find_all("a")
    url1 = itemurl[0].get("href")
    urllist.append(url1)

    i+=1
i=0
while i<lenght:
    urlitem = "https://www.kartalotomasyon.com.tr"+urllist[i]
    r1 = requests.get(urlitem)
    soup1 = BeautifulSoup(r1.content,"html.parser")
    itemname = soup1.find_all("div", attrs={"class": "productTitle"})
    itemsales =soup1.find_all("div", attrs={"class": "salesPrice"})
    itemdiscount = soup1.find_all("div", attrs={"class": "discountPrice"})
    itemdetail = soup1.find_all("div", attrs={"class": "ProductDetail"})

    nameitem.append(itemname[0].text)
    salesitem.append(itemsales[0].text)
    try:
        discountitem.append(itemdiscount[0].text)
    except IndexError:
        discountitem.append("indirim yok")
    detailitem.append(itemdetail[0].text)
    URLitem.append(urlitem)
    print(urlitem)
    try:
        print("ürün isim : " + itemname[0].text)
    except AttributeError:
        print("stokta yok")
    print("ürün orijinal fiyat : " + itemsales[0].text)
    try:
        print("ürün indirimli fiyat : " + itemdiscount[0].text)
    except IndexError:
        print("indirim yok")
    print("ürün detay : " + itemdetail[0].text)
    i+=1
    print(i)
    print("****************************************************************************************")

outWorkbook = xlsxwriter.Workbook(tim)
outSheet = outWorkbook.add_worksheet()

outSheet.write(0,0 , "NAMES")
outSheet.write(0,1,"SALES")
outSheet.write(0,2 , "DİSCOUNT SALES")
outSheet.write(0,3,"DETAİL")
outSheet.write(0,4,"LİNK")

for i in range(len(nameitem)):
    outSheet.write(i + 1,0,nameitem[i])
    outSheet.write(i + 1, 1,salesitem[i])
    outSheet.write(i + 1, 2,discountitem[i])
    outSheet.write(i + 1, 3,detailitem[i])
    outSheet.write(i + 1, 4,URLitem[i])

outWorkbook.close()



