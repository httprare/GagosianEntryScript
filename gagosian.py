import random
import time
from time import sleep
import requests
from bs4 import BeautifulSoup
import string

print("Gagosian script made by @404isunknown on Twitter.\nIf you use this, make sure you give me a follow.\n")
url = "https://www.gagosian.com/shop/lib/lottery-form.php"
email = "youremailhere"

def main():
    entries = int(input("How many Times would you like to enter?: "))
    Size = ['XS','S','M','L','XL']
    i = 0
    while i < entries:
        tSize = random.choice(Size)
        print(tSize)
        entryEmail = email + "%2" + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
        print(entryEmail)
        print("Entry #" + str(i) +  " of " + str(entries) + ":")
        payload = "name=FirstName%20LastName&email=" + entryEmail + "@gmail.com&size-value=" + tSize + "&year=2018&lottery=yes"
        headers = {
        'authority': "www.gagosian.com",
        'method': "POST",
        'path': "/shop/lib/lottery-form.php",
        'scheme': "https",
        'accept': "*/*",
        'accept-language': "en-US,en;q=0.9",
        'content-length': "86",
        'content-type': "application/x-www-form-urlencoded",
        'cookie': "__cfduid=de5412d971ff12e9a377f83a13f6c92571523116808; VaeSession=a0eu790ksgvcaj49tptme510t5; _ga=GA1.2.654119312.1523116807; _gid=GA1.2.54298063.1523116807; __dwt=2819846|73.147.220.241|3034869|1523124010183; _gat=1; __atuvc=4%7C14; __atuvs=5ac8fe6a563e61b0000",
        'origin': "https://www.gagosian.com",
        'referer': "https://www.gagosian.com/shop/murakami--abloh--tshirt",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'cache-control': "no-cache"
        }
        response = requests.post(url, data=payload, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        EntryNum = soup.find("strong").text
        if "Your submission number is" in response.text:
            print("Successful Entry with Email: "+ entryEmail + "@gmail.com in size " + tSize +". Entry Number: " + EntryNum)
            i = i + 1
        if str(soup.find("div", attrs={'role': 'alert'})) in response.text:
            print('Duplicate Entry. Tryagain with a new set of info...')
        time.sleep(3)

if __name__ == '__main__':
    main()
