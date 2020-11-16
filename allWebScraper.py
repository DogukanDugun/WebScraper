import requests
from bs4 import BeautifulSoup
import xlsxwriter
import time
import tkinter as tk
import urllib3

urllib3.disable_warnings()
timestr = time.strftime("%Y%m%d-%H%M%S")
tim = timestr + ".xlsx"
form = tk.Tk()
form.geometry('600x600')
form.title("WEB SCRAPER")
def robotparcaları():
    def robotparcalarırun():

        nameitem = []
        salesitem = []
        discountitem = []
        detailitem = []
        URLitem = []
        selleritem = []
        i = 0
        s = 0

        url = entry.get()

        r = requests.get(url)

        soup = BeautifulSoup(r.content, "html.parser")
        items = soup.find_all("ul", attrs={"class": "products columns-4"})
        i = 0
        items1 = items[0].contents
        while i < len(items1):
            if items1[i] == '\n':
                del items1[i]

            i += 1

        i = 0
        while i < len(items1):
            items2 = items1[i].find_all("a")
            urlitem = items2[0].get("href")
            URLitem.append(urlitem)

            i += 1
        i = 0

        while i < len(URLitem):
            url1 = URLitem[i]
            r = requests.get(url1)
            soup = BeautifulSoup(r.content, "html.parser")
            items3 = soup.find_all("h1", attrs={"class": "product_title entry-title"})
            nameitem.append(items3[0].text)
            items4 = soup.find_all("p", attrs={"class": "price"})
            salesitem.append(items4[0].text)
            items5 = soup.find_all("div", attrs={"id": "tab-description"})
            detailitem.append(items5[0].text)


            i += 1



        outWorkbook = xlsxwriter.Workbook("robotparçaları_" + tim)
        outSheet = outWorkbook.add_worksheet()

        outSheet.write(0, 0, "NAMES")
        outSheet.write(0, 1, "SALES")
                # outSheet.write(0, 3, "SELLER")
                # outSheet.write(0, 3, "OLD PRİCE")
        outSheet.write(0, 2, "DETAİL")
        outSheet.write(0, 3, "LİNK")


        for i in range(len(nameitem)):
            outSheet.write(i + 1, 0, nameitem[i])
            outSheet.write(i + 1, 1, salesitem[i])
            outSheet.write(i + 1, 2, detailitem[i])
            outSheet.write(i + 1, 3, URLitem[i])
                    # outSheet.write(i + 1, 2, selleritem[i])
                    # outSheet.write(i + 1, 3, discountitem[i])

        outWorkbook.close()
        form.destroy()
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

    sumbit = tk.Button(text="SUBMİT", command=robotparcalarırun)
    sumbit.place(x=100, y=250)
def kartalotomasyon():

    def kartalrun():
        s=0

        pagenumber = entry2.get()
        pagenumber = int(pagenumber)
        while s < pagenumber:
            print(s)
            if s == 0:
                url1 = entry.get()
            else:
                a = s + 1
                b = str(a)
                url2 = entry.get() + "?tp=" + b
                url1 = url2
            s += 1


            print(url1)
            r = requests.get(url1)

            soup = BeautifulSoup(r.content, "html.parser")

            items = soup.find_all("div", attrs={"class": "_productItem"})
            lenght = len(items)
            urllist = []
            i = 0
            while i < lenght:
                itemurl = items[i].find_all("a")
                url1 = itemurl[0].get("href")
                urllist.append(url1)

                i += 1
            i = 0
            while i < lenght:
                urlitem = "https://www.kartalotomasyon.com.tr" + urllist[i]
                r1 = requests.get(urlitem)
                soup1 = BeautifulSoup(r1.content, "html.parser")
                itemname = soup1.find_all("div", attrs={"class": "productTitle"})
                itemsales = soup1.find_all("div", attrs={"class": "salesPrice"})
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
                # print(urlitem)
                # try:
                #     print("ürün isim : " + itemname[0].text)
                # except AttributeError:
                #     print("stokta yok")
                # print("ürün orijinal fiyat : " + itemsales[0].text)
                # try:
                #     print("ürün indirimli fiyat : " + itemdiscount[0].text)
                # except IndexError:
                #     print("indirim yok")
                # print("ürün detay : " + itemdetail[0].text)
                # i += 1
                print(i)
                # print("****************************************************************************************")
                i+=1

        outWorkbook = xlsxwriter.Workbook("kartalotomasyon"+tim)
        outSheet = outWorkbook.add_worksheet()

        outSheet.write(0, 0, "NAMES")
        outSheet.write(0, 1, "SALES")
        outSheet.write(0, 2, "DİSCOUNT SALES")
        outSheet.write(0, 3, "DETAİL")
        outSheet.write(0, 4, "LİNK")
        form.destroy()
        for i in range(len(nameitem)):
            outSheet.write(i + 1, 0, nameitem[i])
            outSheet.write(i + 1, 1, salesitem[i])
            outSheet.write(i + 1, 2, discountitem[i])
            outSheet.write(i + 1, 3, detailitem[i])
            outSheet.write(i + 1, 4, URLitem[i])

        outWorkbook.close()
        form.mainloop()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    tim = timestr + ".xlsx"
    nameitem = []
    salesitem = []
    discountitem = []
    detailitem = []
    URLitem = []
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

    sumbit = tk.Button(text="SUBMİT", command=kartalrun)
    sumbit.place(x=100, y=250)
def direncnet():
    def direncnetrun():


        url = entry3.get()

        r = requests.get(url)

        soup = BeautifulSoup(r.content, "html.parser")

        items = soup.find_all("div", attrs={"class": "fl col-3 col-md-4 col-sm-6 col-xs-12 productItem ease"})
        lenght = len(items)
        urllist = []
        i = 0
        while i < lenght:
            itemurl = items[i].find_all("a")
            url1 = itemurl[0].get("href")
            urllist.append(url1)

            i += 1

        i = 0
        while i < lenght:
            urlitem = "https://www.direnc.net" + urllist[i]
            print(urlitem)
            r1 = requests.get(urlitem)
            soup1 = BeautifulSoup(r1.content, "html.parser")
            itemname = soup1.find_all("h1", attrs={"class": "col col-12"})

            itemsales = soup1.find_all("span", attrs={"class": "product-price-tl"})
            # # itemdiscount = soup1.find_all("div", attrs={"class": "discountPrice"})
            itemdetail = soup1.find_all("div", attrs={"id": "productDetailTab"})

            nameitem.append(itemname[0].text)
            salesitem.append(itemsales[0].text + " TL")
            # try:
            #     discountitem.append(itemdiscount[0].text)
            # except IndexError:
            #     discountitem.append("indirim yok")
            detailitem.append(itemdetail[0].text)
            URLitem.append(urlitem)

            try:
                print("ürün isim : " + itemname[0].text)
            except AttributeError:
                print("stokta yok")
            print("ürün fiyat : " + itemsales[0].text + " TL")
            # try:
            #     print("ürün indirimli fiyat : " + itemdiscount[0].text)
            # except IndexError:
            #     print("indirim yok")
            print("ürün detay : " + itemdetail[0].text)
            i += 1
            print(i)
            print("****************************************************************************************")
        outWorkbook = xlsxwriter.Workbook("direncnet"+tim)
        outSheet = outWorkbook.add_worksheet()

        outSheet.write(0, 0, "NAMES")
        outSheet.write(0, 1, "SALES")
        outSheet.write(0, 2, "DETAİL")
        outSheet.write(0, 3, "LİNK")

        for i in range(len(nameitem)):
            outSheet.write(i + 1, 0, nameitem[i])
            outSheet.write(i + 1, 1, salesitem[i])
            outSheet.write(i + 1, 2, detailitem[i])
            outSheet.write(i + 1, 3, URLitem[i])

        outWorkbook.close()
        form.destroy()
    nameitem = []
    salesitem = []
    discountitem = []
    detailitem = []
    URLitem = []
    entry3 = tk.Entry()
    entry3.place(x=100, y=100)
    label4 = tk.Label(text="URL:",
                      font="times 15"
                      )
    label4.place(x=45, y=96)
    # entry3 = tk.Entry()
    # entry3.place(x=200, y=200)
    # label3 = tk.Label(text="SAYFA SAYISI:",
    #                   font="times 15"
    #                   )
    # label3.place(x=45, y=196)
    sumbit1 = tk.Button(text="SUBMİT", command=direncnetrun)
    sumbit1.place(x=100, y=250)
    form.mainloop()
def gittigidiyor():
    def submit():

        timestr = time.strftime("%Y%m%d-%H%M%S")
        tim = timestr + ".xlsx"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
        nameitem = []
        salesitem = []
        discountitem = []
        # detailitem = []
        URLitem = []
        selleritem = []
        pagenumber = entry2.get()
        pagenumber = int(pagenumber)
        s = 0
        while s < pagenumber:
            url = entry.get()
            if s == 0:
                pass
            else:
                a = s + 1
                b = str(a)
                url1 = url + "&sf=" + b
                url = url1

            s += 1
            print(url)
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")

            items = soup.find_all("li",
                                  attrs={"class": "gg-uw-6 gg-w-8 gg-d-8 gg-t-8 gg-m-24 gg-mw-12 catalog-seem-cell"})
            print(len(items))
            if len(items) == 0:
                c = s + 1
                d = str(c)
                url1 = url + "?sf=" + d
                url = url1
                r = requests.get(url, headers=headers)
                soup = BeautifulSoup(r.content, "html.parser")
                items = soup.find_all("li", attrs={
                    "class": "gg-uw-6 gg-w-8 gg-d-8 gg-t-8 gg-m-24 gg-mw-12 catalog-seem-cell"})
            lenght = len(items)
            i = 0
            while i < lenght:
                items1 = items[i].find_all("h3", attrs={"class": "product-title"})
                print(items1[0].text)
                nameitem.append(items1[0].text)
                items2 = items[i].find_all("div", attrs={
                    "class": "priceListener gg-w-24 gg-d-24 gg-t-24 gg-m-24 padding-none"})
                itemsale = items2[0].text
                itemsale = itemsale.replace(" ", "")
                itemsale = itemsale.replace("\n", "")
                salesitem.append(itemsale)
                print(itemsale)
                items3 = items[i].find_all("span", attrs={"class": "seller-nickname"})
                itemseller = items3[0].text
                itemseller = itemseller.replace("\n", "")
                itemseller = itemseller.replace("  ", "")
                selleritem.append(itemseller)
                print(itemseller)
                items4 = items[i].find_all("a")
                urlitem = items4[0].get("href")
                urlitem = urlitem[2:]
                URLitem.append(urlitem)
                print(urlitem)
                i += 1
        outWorkbook = xlsxwriter.Workbook("GİTTİGİDİYOR" + tim)
        outSheet = outWorkbook.add_worksheet()

        outSheet.write(0, 0, "NAMES")
        outSheet.write(0, 1, "SALES")
        outSheet.write(0, 2, "SELLER")
        # outSheet.write(0, 3, "OLD PRİCE")
        outSheet.write(0, 3, "LİNK")

        for i in range(len(nameitem)):
            outSheet.write(i + 1, 0, nameitem[i])
            outSheet.write(i + 1, 1, salesitem[i])
            outSheet.write(i + 1, 2, selleritem[i])
            # outSheet.write(i + 1, 3, discountitem[i])
            outSheet.write(i + 1, 3, URLitem[i])

        outWorkbook.close()
        form.destroy()
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

    sumbit = tk.Button(text="SUBMİT", command=submit)
    sumbit.place(x=100, y=250)
def trendyol():
    def submit():
        nameitem = []
        salesitem = []
        discountitem = []
        # detailitem = []
        URLitem = []
        selleritem = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
        i = 0

        pagenumber = entry2.get()
        pagenumber = int(pagenumber)
        s=0
        while s < pagenumber:
            url = entry.get()
            if s == 0:
                pass
            else:
                a = s + 1
                b = str(a)
                url1 = url + "&pi=" + b
                url = url1

            r = requests.get(url, headers=headers)

            soup = BeautifulSoup(r.content, "html.parser")

            items = soup.find_all("div", attrs={"class": "p-card-wrppr"})
            print("len items")
            print(len(items))
            if len(items) == 0:
                c = s + 1
                d = str(c)
                url = "https://www.trendyol.com/erkek+t-shirt"
                url1 = url + "?pi=" + b
                url = url1
                r = requests.get(url, headers=headers)

                soup = BeautifulSoup(r.content, "html.parser")

                items = soup.find_all("div", attrs={"class": "p-card-wrppr"})
                pass
            print(url)
            i = 0
            lenght = len(items)
            i = 0
            while i < lenght:
                print(i)
                items1 = items[i].find_all("a")
                url1 = items1[0].get("href")
                url1 = "https://www.trendyol.com" + url1
                URLitem.append(url1)
                i += 1

            s += 1

        i = 0
        lenght = len(URLitem)
        while i < lenght:
            print(i)
            url = URLitem[i]
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.content, "html.parser")
            item = soup.find_all("div", attrs={"class": "pr-cn-in"})
            items = item[0].find_all("h1", attrs={"class": "pr-new-br"})
            nameitem.append(items[0].text)

            items = item[0].find_all("span", attrs={"class": "prc-org"})
            try:
                discountitem.append(items[0].text)
            except IndexError:
                discountitem.append("indirim yok")
            items = item[0].find_all("span", attrs={"class": "prc-slg"})
            salesitem.append(items[0].text)

            items = item[0].find_all("div", attrs={"class": "sl-nm"})
            try:
                selleritem.append(items[0].text)
            except IndexError:
                selleritem.append("trendyol")

            i += 1
        outWorkbook = xlsxwriter.Workbook("hepsiburada_" + tim)
        outSheet = outWorkbook.add_worksheet()

        outSheet.write(0, 0, "NAMES")
        outSheet.write(0, 1, "SALES")
        outSheet.write(0, 2, "SELLER")
        outSheet.write(0, 3, "OLD PRİCE")
        outSheet.write(0, 4, "LİNK")

        for i in range(len(nameitem)):
            outSheet.write(i + 1, 0, nameitem[i])
            outSheet.write(i + 1, 1, salesitem[i])
            outSheet.write(i + 1, 2, selleritem[i])
            outSheet.write(i + 1, 3, discountitem[i])
            outSheet.write(i + 1, 4, URLitem[i])

        outWorkbook.close()
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

    sumbit = tk.Button(text="SUBMİT", command=submit)
    sumbit.place(x=100, y=250)
def hepsiburada():
    def sumbit():
        timestr = time.strftime("%Y%m%d-%H%M%S")
        tim = timestr + ".xlsx"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
        # form = tk.Tk()
        # form.geometry('600x600')
        # form.title("WEB SCRAPER")
        pagenumber = entry2.get()
        pagenumber = int(pagenumber)
        s = 0
        nameitem = []
        salesitem = []
        discountitem = []
        # detailitem = []
        URLitem = []
        selleritem = []
        while s < pagenumber:
            print(s)
            if s == 0:
                url = entry.get()
            else:
                a = s + 1
                b = str(a)
                url1 = entry.get() + "&sayfa=" + b
                url = url1

            s += 1

            i = 0

            # print(url)


            r = requests.get(url, headers=headers)


            soup = BeautifulSoup(r.content, "html.parser")

            items = soup.find_all("li", attrs={"class": "search-item col lg-1 md-1 sm-1 custom-hover not-fashion-flex"})
            # print(items[0])
            if len(items) == 0:
                url = entry.get() + "?sayfa=" + b
                r = requests.get(url, headers=headers)

                soup = BeautifulSoup(r.content, "html.parser")

                items = soup.find_all("li", attrs={"class": "search-item col lg-1 md-1 sm-1 custom-hover not-fashion-flex"})

            lenght = len(items)

            while i < lenght:

                items1 = items[i].find("span", attrs={"class": "price product-price"})
                try:
                    salesitem.append(items1.text)
                except AttributeError:
                    items1 = items[i].find("div", attrs={"class": "price-value"})
                    itemsales = items1.text
                    itemsales = itemsales.replace(" ","")
                    salesitem.append(itemsales)
                    # salesitem.append(items1.text)
                i += 1
            i = 0
            while i < lenght:
                items1 = items[i].find("del", attrs={"class": "price old product-old-price"})
                try:
                    discountitem.append(items1.text)
                except AttributeError:
                    discountitem.append("indirim yok")

                i += 1
            i = 0
            while i < lenght:
                itemurl = items[i].find_all("a")
                url1 = itemurl[0].get("href")
                url1 = "https://www.hepsiburada.com" + url1
                URLitem.append(url1)

                i += 1
            # print(URLitem)
            i = 0
        lenght = len(URLitem)
        while i < lenght:
            url1 = URLitem[i]
            print(url1)
            r1 = requests.get(url1, headers=headers)
            soup1 = BeautifulSoup(r1.content, "html.parser")
            items1 = soup1.find_all("h1", attrs={"class": "product-name best-price-trick"})
            itemname = items1[0].text
            itemname = itemname.replace(" ", "  ")
            itemname = itemname[18:]
            nameitem.append(itemname)
            items1 = soup1.find_all("span", attrs={"class": "seller"})
            itemseller = items1[0].text
            itemseller = itemseller.replace(" ", "")
            itemseller = itemseller.replace("\n", "")
            itemseller = itemseller[8:]
            # print(itemseller)
            selleritem.append(itemseller)
            # items1 = soup1.find_all("span", attrs={"class": "price merchant"})
            # # itemprice = items1[0].text
            # print(items1)

            # print("-------------------------------------------------------------------------")

            i += 1

        outWorkbook = xlsxwriter.Workbook("hepsiburada_" + tim)
        outSheet = outWorkbook.add_worksheet()

        outSheet.write(0, 0, "NAMES")
        outSheet.write(0, 1, "SALES")
        outSheet.write(0, 2, "SELLER")
        outSheet.write(0, 3, "OLD PRİCE")
        outSheet.write(0, 4, "LİNK")

        for i in range(len(nameitem)):
            outSheet.write(i + 1, 0, nameitem[i])
            outSheet.write(i + 1, 1, salesitem[i])
            outSheet.write(i + 1, 2, selleritem[i])
            outSheet.write(i + 1, 3, discountitem[i])
            outSheet.write(i + 1, 4, URLitem[i])

        outWorkbook.close()
        form.destroy()
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

    sumbit = tk.Button(text="SUBMİT", command=sumbit)
    sumbit.place(x=100, y=250)
def N11():
    def sumbit():
        nameitem = []
        salesitem = []
        discountitem = []
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
                url1 = entry.get() + "&pg=" + b
                url = url1

            s += 1
            r = requests.get(url)

            soup = BeautifulSoup(r.content, "html.parser")

            items = soup.find_all("section", attrs={"class": "group listingGroup resultListGroup import-search-view"})
            if len(items) == 0:
                url = entry.get() + "?spg=" + b
                r = requests.get(url)

                soup = BeautifulSoup(r.content, "html.parser")

                items = soup.find_all("li", attrs={"class": "search-item col lg-1 md-1 sm-1 custom-hover not-fashion-flex"})

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
                try:
                    itemdiscount = items3[i].find("del")
                    discountitem.append(itemdiscount.text)

                except AttributeError:
                    discountitem.append("indirim yok")

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

        outWorkbook = xlsxwriter.Workbook("n11"+tim)
        outSheet = outWorkbook.add_worksheet()

        outSheet.write(0, 0, "NAMES")
        outSheet.write(0, 1, "SALES")
        outSheet.write(0, 2, "SELLER")
        outSheet.write(0, 3, "OLD PRİCE")
        outSheet.write(0, 4, "LİNK")

        for i in range(len(nameitem)):
            outSheet.write(i + 1, 0, nameitem[i])
            outSheet.write(i + 1, 1, salesitem[i])
            outSheet.write(i + 1, 2, selleritem[i])
            outSheet.write(i + 1, 3, discountitem[i])
            outSheet.write(i + 1, 4, URLitem[i])

        outWorkbook.close()
        form.destroy()

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

    sumbit = tk.Button(text="SUBMİT", command=sumbit)
    sumbit.place(x=100, y=250)


radioButton1= tk.Radiobutton(value=0,command = N11,text = "N11").place(x=50,y=50)
radioButton2= tk.Radiobutton(value=1,command = direncnet,text= "DıRENCNET").place(x=100,y=50)
radioButton3= tk.Radiobutton(value=2,command = kartalotomasyon,text= "KARTALOTOMASYON").place(x=190,y=50)
radioButton4= tk.Radiobutton(value=3,command = hepsiburada,text= "HEPSİBURADA").place(x=340,y=50)
radioButton5= tk.Radiobutton(value=4,command = trendyol,text= "TRENDYOL").place(x=450,y=50)
radioButton6= tk.Radiobutton(value=5,command = gittigidiyor,text= "GİTTİGİDİYOR").place(x=50,y=70)
radioButton7= tk.Radiobutton(value=6,command = robotparcaları,text= "ROBOTPARCALARI").place(x=150,y=70)
form.mainloop()
