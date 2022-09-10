from datetime import datetime

import requests
import csv

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

with open('curs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow("Курсы валют ЦБ РФ на: " + str(datetime.today().strftime("%d.%m.%Y")) + " число")
    spamwriter.writerow("Курс доллара США: " + str(data['Valute']['USD']['Value']) + " за 1 доллар")
    spamwriter.writerow("Курс Евро: " + str(data['Valute']['EUR']['Value']) + " за 1 евро")
    spamwriter.writerow("Курс китайских юаней: " + str(data['Valute']['CNY']['Value']) + " за 10 юаней")
    spamwriter.writerow("Курс индийской рупий: " + str(data['Valute']['INR']['Value']) + " за 100 рупий")
    spamwriter.writerow("Курс турецкой лиры: " + str(data['Valute']['TRY']['Value']) + " за 10 лир")
    spamwriter.writerow("Курс таджикских сомони: " + str(data['Valute']['TJS']['Value']) + " за 10 сомони")
    spamwriter.writerow("Курс узбекских сумов: " + str(data['Valute']['UZS']['Value']) + " за 10 000 сомони")
    spamwriter.writerow("Курс армянских драм: " + str(data['Valute']['AMD']['Value']) + " за 100 драмов")
    spamwriter.writerow("Курс казахских тенге: " + str(data['Valute']['KZT']['Value']) + " за 100 тенге")
    spamwriter.writerow("Курс киргизских сомов: " + str(data['Valute']['KGS']['Value']) + " за 100 сомов")
    spamwriter.writerow("Курс туркменского маната: " + str(data['Valute']['TMT']['Value']) + " за 1 манат")