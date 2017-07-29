# pullup ; @nishantpatel ; July 28, 2017
# IA - 62: Car dimensions

from bs4 import BeautifulSoup
with open("toyota-car-dimensions.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

for vehicleDetails in soup.find_all(class_="unit"):
    print vehicleDetails.text.encode('utf-8')