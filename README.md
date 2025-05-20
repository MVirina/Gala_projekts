# Gala projekts
Programma, kas izmantojot webscraping no ss.lv parāda vai dzīvokļa cena ir samazinājusies. 
Lietotājs ievada to dzīvokļa saiti, kura pašam interesē un tad programma vienreiz dienā pārbaudīs vai dzīvokļa cena ir mainījusies. Ja dzīvokļa īres cena nokrītas tad terminālī parādas paziņojums par kādu summu tā ir nokritusies un jauno dzīvokļa cenu. Dzīvokļa cenu programma pārbauda vienu reizi pa dienu, programma strādā ar bezgalīgu while ciklu, kurš strāda ik pa vienai minūtei, gadījumā ja cena nomainās tiek izvadīts paziņojums par cenas maiņu.
Kā arī ja tiek izņemts lietotāja iesūtītā dzīvokļa sludinājums, tad programma to paziņo terminālī.

# Iespējamie uzlabojumi
- Informāciju par cenas nomaiņu varētu paziņot atsūtot e-pastu vai ar skaņas paziņojumu.
- Terminālī izvadīt informāciju tikai par cenas nomaiņu.
- Pielāgot programmu, lai tā strādā ar visiem ss.lv sludinājumiem, tai skaitā automašīnu sludinājumiem.
- Pievienot iespēju iesniegt vairākus sludinājumus reizē un pārbaudīt vai to cena krītās.
- Pārbaudīt arī vai cena nav palielinājusies, nevis tikai samazinājusies.

## Izmantotās bibliotēkās
### requests un BeautifulSoup
Šīs bibliotēkas izmanto priekš webscraping, lai no HTML saites iegūtu informāciju.
### schedule un time
Šīs bibliotēkas tiek izmantotas, lai nodrošinātu programmas darbību konkrētā dienas laikā. Kā arī, lai samazinātu while cikla izpildes biežumu līdz tikai 1 reizei minūtē, tādā veidā samazinot slodzi uz datoru.

## Time complexity
Programmas laika sarežģītībās līmenis pieaug atkarībā no tā, cik ilgi tā strādā, jo tajā tiek izmantots bezgalīgs while cikls, while cikla laika sarežģītības līmenis atbilst O(n), bet to var pārtraukt tikai lietotājs. Teorētiski programmas laika sarežģītība ir bezgalīga.

## Metodes
### split(txt)
Metode, kura no teksta atdala un atgriež tikai pirmo vārdu, skatoties, kad parādās pirmā atstarpe. Izmantota, lai iegūtu tikai dzīvokļa īres cenu no ss.lv izgūtā cenas lauka "370 €/mēn. (7.55 €/m²)". Šīs metodes laika sarežģītība ir O(n), jo tā izmantojot for ciklu iet cauri visam tekstam līdz atrod atstarpi.
### checkprice(x)
Metode, kura pārbauda vai dzīvokļa cena ir mainījusies. Tā pirmajā strādāšanas reizē saglabā esošu dzīvokļa cenu, un nākamajās reizēs pārbauda vai tā ir samazinājusies. Ja cena samazinās, tad metode atgriež cenu starpību, pretējā gadījumā False. Šīs metodes laika sarežģītība ir O(1), jo tā veic tikai cenas pārbaudi izmantojot if.

## Programmatūras izmantošanas metodes
- Var izmantot lai sekoti līdzi dzīvokļu cenām ss.lv.
- Strādā arī ar citiem sludinājuma veidiem izņemot automašīnām (tur būtu nepieciešams modificēt programmas kodu).
- Sekot līdzi vai sludinājumam beidzās termiņš vai arī tas tiek izņemts.


