from bs4 import BeautifulSoup
import requests
import pandas as pd


Names = []
Prices = []
Descriptions = []
Reviews = []
for i in range(1,7):
    url = "https://www.flipkart.com/search?q=dslr&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as="+str(i)
    res = requests.get(url)
    # print(res)

    soup = BeautifulSoup(res.text, "html.parser")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
    names = box.find_all("div", class_= "_4rR01T")
    for i in names:
        n = i.text
        Names.append(n)
    # print(len(Names))

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        p = i.text
        Prices.append(p)
    # print(len(Prices))

    descriptions = box.find_all("ul", class_ = "_1xgFaf")
    for i in descriptions:
        d = i.text
        Descriptions.append(d)
    # print(len(Descriptions))

    reviews = box.find_all("div", class_ = "_3LWZlK")
    for i in reviews:
        r= i.text
        Reviews.append(r)
    # print(len(Reviews))

df = pd.DataFrame({"Product Name": Names, "Product Prices": Prices, "Product Description": Descriptions, "Product Reviews": Reviews})
print(df)

df.to_csv("Dslr_lists.csv")
# print(df["Product Prices"])
