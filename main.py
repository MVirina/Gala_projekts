import requests
from bs4 import BeautifulSoup
import schedule
import time

parbaude = True
#temp_price = 0
temp_price = 400

def split(txt):
    result = ''
    for char in txt:
        if char == ' ':
            break
        result = result + char

    return result

def checkprice(x): 
    global temp_price
    x = int(x)
    if x < temp_price:
        a = temp_price - x
        temp_price = x
        return a
    else:
        temp_price = x
        return False

def set_parbaude():
    global parbaude
    parbaude = True
    
def site_check():
    global parbaude
    sludinājums = requests.get(adrese)

    if sludinājums.status_code == 200:
        saturs = BeautifulSoup(sludinājums.content, "html.parser")

        #Pārbauda vai sludinājuma termiņš nav beidzies (vai satur bildi - https://i.ss.lv/img/a_lv.gif)
        info = saturs.find_all(src="https://i.ss.lv/img/a_lv.gif")
        if len(info)!=0:
            print("Sludinājuma termiņš ir beidzies")
            exit()
        
        #Atrod dzīvokļa cenu
        cena = saturs.find(class_="ads_price")
        cena_string = cena.string

        print("Dzīvokļa cena: ", cena_string)

        clean_cena = split(cena_string)
        check = checkprice(clean_cena)

        if check != False:
            print("Cena ir samazinājusies par", check, "€")
            print("Jaunā dzīvokļa cena", clean_cena,"€/mēn")
        else:
            print("Cena nav mainījusies")
    
    else:
        print("Saite nedarbojas")

    parbaude = False
    
print('Iekopējiet sludinājuma saiti:')
adrese = input()

#schedule.every().day.at("11:19").do(set_parbaude) #Tagadējais laiks - 3h, jo github strāda uz UTC time zone
schedule.every(30).seconds.do(set_parbaude)

while True:
    schedule.run_pending()

    if parbaude:
        site_check()

    time.sleep(60)

