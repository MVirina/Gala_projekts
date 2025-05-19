# Gala projekts
Programma, kas izmantojot webscraping no ss.lv parāda vai dzīvokļa cena ir samazinājusies. 
Lietotājs ievada to dzīvokļa saiti, kura pašam interesē un tad programma vienreiz dienā pārbaudīs vai dzīvokļa cena ir mainījusies. Ja dzīvokļa īres cena nokrītas tad terminālī parādas paziņojums par kādu summu tā ir nokritusies un jauno dzīvokļa cenu. Dzīvokļa cenu programma pārbauda vienu reizi pa dienu, programma strādā ar bezgalīgu while ciklu, kurš strāda ik pa vienai minūtei, gadījumā ja cena nomainās tiek izvadīts paziņojums par cenas maiņu.
Kā arī ja tiek izņemts sludinājums kāds no lietotāja iesūtītajiem dzīvokļiem, tad programma to paziņo terminālī.

# Iespējamie uzlabojumi
- Informāciju par cenas nomaiņu varētu paziņot atsūtot e-pastu vai ar skaņas paziņojumu.
- Terminālī izvadīt informāciju tikai par cenas nomaiņu.
- Pielāgot programmu, lai tā strādā ar visiem ss.lv sludinājumiem, tai skaitā automašīnu sludinājumiem.
- Pievienot iespēju iesniegt vairākus sludinājumus reizē un pārbaudīt vai to cena krītās.

## Izmantotās bibliotēkās
### requests un BeautifulSoup
izmanto prieks webscarping
### schedule un time
izmanto prieks programmas atkārtotas darbības

## Time conplexity

## Metodes
### split(txt)
def split(txt):
    result = ''
    for char in txt:
        if char == ' ':
            break
        result = result + char
    return result
    
### checkprice(x)
def checkprice(x): 
    global temp_price
    x = int(x)
    if x < temp_price:
        a = x - temp_price
        temp_price = x
        return a
    else:
        temp_price = x
        return False

## Programmatūras izmantošanas metodes
- Var izmantot lai sekoti līdzi dzīvokļu cenām ss.lv.
- Strādā arī ar citiem sludinājuma veidiem izņemot automašīnām (tur būtu nepieciešams modificēt programmas kodu).
- Sekot līdzi vai sludinājumam beidzās termiņš vai arī tas tiek izņemts.

