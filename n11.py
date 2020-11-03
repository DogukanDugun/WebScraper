import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
import tkinter as tk
import urllib3
urllib3.disable_warnings()

def sumbit():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    tim = timestr + ".xlsx"
    nameitem = []
    salesitem = []
    # discountitem = []
    # detailitem = []
    URLitem = []
    selleritem = []
    i = 0
    s = 0
    pagenumber = entry2.get()
    pagenumber = int(pagenumber)
    while s < pagenumber:
        print(s)
        if s == 0:
            url = entry.get()
        else:
            a = s + 1
            b = str(a)
            url1 = entry.get() + "?pg=" + b
            url = url1

        s += 1

        print("---------------------------------------")
        r = requests.get(url)
        print(url)
        soup = BeautifulSoup(r.content, "html.parser")

        items = soup.find_all("section", attrs={"class": "group listingGroup resultListGroup import-search-view"})
        # items2 = items[0].find_all("ul", attrs={"class":"clearfix"})
        items3 = items[0].find_all("li", attrs={"class": "column"})

        lenght = len(items3)
        while i < lenght:
            itemsname4 = items3[i].find("h3")
            itemsname5 = str(itemsname4.text)
            itemsname5 = itemsname5.replace("\n", "")
            itemsname5 = itemsname5.replace("  ", "")
            nameitem.append(itemsname5)
            # print(itemsname5)
            i += 1
        i = 0
        while i < lenght:
            itemsprice = items3[i].find("ins")
            itemsprice2 = itemsprice.text
            itemsprice2 = itemsprice2.replace("\n", "")
            itemsprice2 = itemsprice2.replace(" ", "")
            salesitem.append(itemsprice2)
            # print(itemsprice2)
            i += 1
        i = 0
        while i < lenght:
            itemsellername = items3[i].find("span", attrs={"class": "sallerName"})
            itemsellername2 = itemsellername.text
            itemsellername2 = itemsellername2.replace("\n", "")
            itemsellername2 = itemsellername2.replace(" ", "")
            selleritem.append(itemsellername2)
            # print(itemsellername2)
            i += 1

        i = 0

        while i < lenght:
            itemurl = items3[i].find("a")
            url1 = itemurl.get("href")
            URLitem.append(url1)
            # print(url1)
            i += 1
        i = 0
        # while i < lenght:
        #     url = URLitem[i] + "#unf-info"
        #     print(url)
        #     r = requests.get(url)
        #     soup = BeautifulSoup(r.content, "html.parser")
        #     items = soup.find_all("div", attrs={"class": "unf-info"})
        #     try:
        #         itemdetail = items[0].text
        #     except IndexError:
        #         try:
        #             url = URLitem[i]
        #             r = requests.get(url)
        #             soup = BeautifulSoup(r.content, "html.parser")
        #             items = soup.find_all("section", attrs={"tabPanelItem details"})
        #
        #             itemdetail2 = items[0].text
        #             itemdetail2 = itemdetail2.replace("\n", "")
        #             detailitem.append(itemdetail2)
        #         except IndexError:
        #             detailitem.append("detay yok")
        #
        #     itemdetail = itemdetail.replace("\n", "")
        #     itemdetail = itemdetail[14:]
        #     detailitem.append(itemdetail)
        #     print(i)
        #     i += 1

    outWorkbook = xlsxwriter.Workbook(tim)
    outSheet = outWorkbook.add_worksheet()

    outSheet.write(0, 0, "NAMES")
    outSheet.write(0, 1, "SALES")
    outSheet.write(0, 2, "SALLER")
    outSheet.write(0, 3, "DETAİL")
    outSheet.write(0, 4, "LİNK")

    for i in range(len(nameitem)):
        outSheet.write(i + 1, 0, nameitem[i])
        outSheet.write(i + 1, 1, salesitem[i])
        outSheet.write(i + 1, 2, selleritem[i])
        # outSheet.write(i + 1, 3, detailitem[i])
        outSheet.write(i + 1, 4, URLitem[i])

    outWorkbook.close()
    form.destroy()


form = tk.Tk()
form.geometry('600x600')
form.title("N11 WEB SCRAPER")
entry = tk.Entry()
entry.place(x=100, y=100)
label1 = tk.Label(text="URL:",
                  font="times 15"
                  )
label1.place(x=45, y=96)
entry2 = tk.Entry()
entry2.place(x=200, y=200)
label2 = tk.Label(text="SAYFA SAYISI:",
                  font="times 15"
                  )
label2.place(x=45, y=196)
sumbit = tk.Button(text="SUMBİT", command=sumbit)
sumbit.place(x=100, y=250)

form.mainloop()
