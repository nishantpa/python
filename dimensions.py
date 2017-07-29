# @nishantpatel ; July 28, 2017
# IA - 62: Car dimensions
# Target file and script located in same dir

from bs4 import BeautifulSoup
with open("toyota-car-dimensions.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

for vehicleDetails in soup.find_all(class_="unit"):
    # print vehicleDetails.text.encode('utf-8')
    print vehicleDetails.text.split('L ')[0],
    print ",",  
    print vehicleDetails.text.replace(" ", "").split('H:')[1][0:14].replace("x", ",")
