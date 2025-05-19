# Gala projekts
Programma, kas izmantojot webscraping no ss.lv parāda izdevīgākos dzīvokļus, ko īrēt pēc tā cenas. Lietotājs ievada to dzīvokļu saites, kuras pašam interesē un tad programma pārbaudīs cenu, un ja dzīvokļa īres cena nokrītas tad terminālī parādas paziņojums. Dzīvokļa cenu programma pārbauda vienu reizi pa dienu, kā arī lai pārbaudītu vai programma strādā tā cenu pārbuda ik pa minūtei.
Kā arī ja tiek izņemts sludinājums kāds no lietotāja iesūtītajiem dzīvokļiem, tad programma to paziņo terminālī
 

## Izmantotās bibliotēkās
import requests
from bs4 import BeautifulSoup
import schedule
import time

## Datu struktūras programmā
Salīdzināšana

## Programmatūras izmantošanas metodes
Var izmantot lai sekoti līdzi dzīvokļu cenām ss.lv, varētu arī strādat uz citiem sludinājuma veidiem izņemot automašīnām (tur būtu nepieciešams modificēt programmas kodu)

# A first-level heading
## A second-level heading
### A third-level heading

**This is bold text**
_This text is italicized_
~~This was mistaken text~~
**This text is _extremely_ important**
***All this text is important***
This is a <sub>subscript</sub> text
This is a <sup>superscript</sup> text
This is an <ins>underlined</ins> text
