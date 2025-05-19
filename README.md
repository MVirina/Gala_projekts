# Gala projekts
Programma, kas izmantojot webscraping no ss.lv parāda vai dzīvokļa cena ir samazinājusies. 
Lietotājs ievada to dzīvokļa saiti, kura pašam interesē un tad programma vienreiz dienā pārbaudīs vai dzīvokļa cena ir mainījusies. Ja dzīvokļa īres cena nokrītas tad terminālī parādas paziņojums par kādu summu tā ir nokritusies un jauno dzīvokļa cenu. Dzīvokļa cenu programma pārbauda vienu reizi pa dienu, kā arī lai pārbaudītu vai programma strādā tā cenu pārbuda ik pa minūtei, gadījumā ja nomainās tiek izvadīts savādāks paziņojums.
Kā arī ja tiek izņemts sludinājums kāds no lietotāja iesūtītajiem dzīvokļiem, tad programma to paziņo terminālī.

# Iespējamie uzlabojumi
- Informāciju par cenas nomaiņu varētu paziņot atsūtot e-pastu vai ar skaņas paziņojumu.
- Terminālī izvadīt informāciju tikai par cenas nomaiņu.
- Pielāgot programmu, lai tā strādā ar visiem ss.lv sludinājumiem, tai skaitā automašīnu sludinājumiem.
- Pievienot iespēju iesniegt vairākus sludinājumus reizē un pārbaudīt vai to cena krītās.

## Izmantotās bibliotēkās
# requests un BeautifulSoup
izmanto prieks webscarping
# schedule un time
izmanto prieks programmas atkārtotas darbības

## Time conplexity

## Datu struktūras programmā
Salīdzināšana

## Programmatūras izmantošanas metodes
- Var izmantot lai sekoti līdzi dzīvokļu cenām ss.lv.
- Strādā arī ar citiem sludinājuma veidiem izņemot automašīnām (tur būtu nepieciešams modificēt programmas kodu).
- Sekot līdzi vai sludinājumam beidzās termiņš vai arī tas tiek izņemts.

