import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
page_nr = int(soup.find_all("a", {"class": "Page"})[-1].text)
print("Total {} pages".format(page_nr))


l = []
base_url = "http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

for page in range(0, page_nr * 10, 10):
    print("Scrapping page {}...".format((page // 10) + 1))
    r = requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')
    all = soup.find_all("div", {"class": "propertyRow"})

    for item in all:
        d = {}
        d["Address"] = item.find_all("span", {"class": "propAddressCollapse"})[0].text
        try:
            d["Locality"] = item.find_all("span", {"class": "propAddressCollapse"})[1].text
        except:
            d["Locality"] = None
        d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n", "").replace(" ", "")

        try:
            d["Beds"] = item.find("span", {"class": "infoBed"}).text
        except:
            d["Beds"] = None

        try:
            d["InfoSqFt"] = item.find("span", {"class": "infoSqFt"}).text
        except:
            d["InfoSqFt"] = None

        try:
            d["InfoValueFullBath"] = item.find("span", {"class": "infoValueFullBath"}).text
        except:
            d["InfoValueFullBath"] = None

        try:
            d["InfoValueHalfBath"] = item.find("span", {"class": "infoValueHalfBath"}).text
        except:
            d["InfoValueHalfBath"] = None

        for column_group in item.find_all("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span", {"class": "featureGroup"}), column_group.find_all("span", {"class": "featureName"})):
                # print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lots"] = feature_name.text
        l.append(d)
df = pandas.DataFrame(l)
df.to_csv("Output.csv")
print("Done. Check Output.csv")
