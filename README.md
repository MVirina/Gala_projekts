# Gala projekts
Programma, kas izmantojot webscraping no ss.lv atrod izdevīgākos dzīvokļus, ko īrēt pēc tā cenas uz m<sup>2</sup> un kopējās platības.
Tā izvadīs 5.lētākos dzīvokļus pēc cenas uz m<sup>2</sup>, kā arī izvadīs kopējo dzīvokļa platību un sludinājuma saiti.

Ja, programma tiks atkārtoti palaista tā salīdzinās iepriekšējos lētākos dzīvokļus ar tagadējiem un atzīmēs jaunos sludinājumus sarakstā ar vārdu NEW, lai lietotājs zinātu, ka sludinājumu vēl nav apskatījis. 
Jaunos sludinājumus atradīs salīdzinot pagājša saraksta un jaunā saraksta ievietošanas datumus un laikus. 

NEW 1. cena, platiba, links
09/04/2025 10:23     
09/04/2025 10:23   
09/04/2025 10:23   
09/04/2025 10:23   
09/04/2025 10:23   

12/06/2025 20:30 NEW
09/04/2025 10:23 
12/06/2025 20:30
12/06/2025 20:30
12/06/2025 20:30
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
