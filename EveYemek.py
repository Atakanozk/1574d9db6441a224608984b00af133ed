# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify
import traceback
import requests
import xml.etree.ElementTree as ET
from urllib.request import urlopen



app = Flask(__name__)


class KurGosterme:
    x_rate_base = requests.get('https://api.exchangeratesapi.io/latest?base=TRY')
    x_rate_dict = x_rate_base.json()
    eur = x_rate_dict.get('rates').get('EUR')
    usd = x_rate_dict.get('rates').get('USD')
    real_eur = float(format((1 / eur),'.4f'))
    real_usd = float(format((1 / usd),'.4f'))
    x_rate_kurlar = [real_usd,real_eur]
    
    
    tcmb_url = 'https://www.tcmb.gov.tr/kurlar/today.xml'
    tree = ET.parse(urlopen(tcmb_url))
    root = tree.getroot()
    tcmb_kurlar = []
    for kurs in root.findall('Currency'):
        if kurs.find('CurrencyName').text == 'US DOLLAR':
            tcmb_kurlar.append(float(kurs.find('ForexBuying').text))
        elif kurs.find('CurrencyName').text == 'EURO':
            tcmb_kurlar.append(float(kurs.find('ForexBuying').text))
    
    def predict_usd(self):
        try:
    
    
            if self.x_rate_kurlar[0] > self.tcmb_kurlar[0]:
                return'X rate USD kuru = {} TCMB USD Kurundan {} daha büyüktür.'.format(self.x_rate_kurlar[0], self.tcmb_kurlar[0])
            elif self.x_rate_kurlar[0] < self.tcmb_kurlar[0]:
                return'TCMB USD Kuru = {} X rate USD kurundan {} daha büyüktür.' .format(self.tcmb_kurlar[0],self.x_rate_kurlar[0])
           
        except:
    
            return jsonify({'trace': traceback.format_exc()})
        
    def yalin_usd(self):
        try:
            
            if self.x_rate_kurlar[0] > self.tcmb_kurlar[0]:
                return str(self.tcmb_kurlar[0])
            elif self.x_rate_kurlar[0] < self.tcmb_kurlar[0]:
                return str(self.x_rate_kurlar[0])
            
        except:
    
            return jsonify({'trace': traceback.format_exc()})
        
    def predict_eur(self):
        try:
    
    
            if self.x_rate_kurlar[1] > self.tcmb_kurlar[1]:
                return'X rate EUR kuru = {} TCMB EUR Kurundan {} daha büyüktür.' .format(self.x_rate_kurlar[1], self.tcmb_kurlar[1])
            elif self.x_rate_kurlar[1] < self.tcmb_kurlar[1]:
                return'TCMB EUR Kuru = {} X rate EUR kurundan {} daha büyüktür.' .format(self.tcmb_kurlar[1],self.x_rate_kurlar[1])
        
        except:
    
            return jsonify({'trace': traceback.format_exc()})

    def yalin_eur(self):
        try:
            
            if self.x_rate_kurlar[1] > self.tcmb_kurlar[1]:
                return str(self.tcmb_kurlar[1])
            elif self.x_rate_kurlar[1] < self.tcmb_kurlar[1]:
                return str(self.x_rate_kurlar[1])
            
        except:
    
            return jsonify({'trace': traceback.format_exc()})
        
class TarihKurGosterme:
    def __init__(self,tarih):
        self.tarih = tarih
    
    def kur_ayarı(self):
        x_rate_tarih = requests.get('https://api.exchangeratesapi.io/{}?base=TRY'.format(self.tarih))
        x_rate_dict = x_rate_tarih.json()
        eur = x_rate_dict.get('rates').get('EUR')
        usd = x_rate_dict.get('rates').get('USD')
        real_eur = float(format((1 / eur),'.4f'))
        real_usd = float(format((1 / usd),'.4f'))
        x_rate_kurlar = [real_usd,real_eur]
    
        def zaman_belirle(Gun,Ay,Yil):
        	if len (str(Gun)) == 1 :
        		Gun="0"+str(Gun)
        	if len (str(Ay)) == 1 :
        		Ay="0"+str(Ay)
        
        	url = ("http://www.tcmb.gov.tr/kurlar/"+str(Yil)+str(Ay)+"/"+str(Gun)+str(Ay)+str(Yil)+".xml")
        	return url
        return x_rate_kurlar
        
    def kur_ayarı_tcmb(self):
        
        def zaman_belirle(Gun,Ay,Yil):
        	if len (str(Gun)) == 1 :
        		Gun="0"+str(Gun)
        	if len (str(Ay)) == 1 :
        		Ay="0"+str(Ay)
        
        	url = ("http://www.tcmb.gov.tr/kurlar/"+str(Yil)+str(Ay)+"/"+str(Gun)+str(Ay)+str(Yil)+".xml")
        	return url
        
        tarih2 = self.tarih.split('-')
        zaman = zaman_belirle(tarih2[2],tarih2[1],tarih2[0])
        
        tree = ET.parse(urlopen(zaman))
        root = tree.getroot()
        tcmb_kurlar = []
        for kurs in root.findall('Currency'):
            if kurs.find('CurrencyName').text == 'US DOLLAR':
                tcmb_kurlar.append(float(kurs.find('ForexBuying').text))
            elif kurs.find('CurrencyName').text == 'EURO':
                tcmb_kurlar.append(float(kurs.find('ForexBuying').text))
        
        return tcmb_kurlar
    
    def yalin_usd(self,x_rate,tcmb):
        try:
            
            if x_rate[0] > tcmb[0]:
                return str(tcmb[0])
            elif x_rate[0] < tcmb[0]:
                return str(x_rate[0])
            
        except:
    
            return jsonify({'trace': traceback.format_exc()})
        
    def yalin_eur(self,x_rate,tcmb):
        try:
            
            if x_rate[1] > tcmb[1]:
                return str(tcmb[1])
            elif x_rate[1] < tcmb[1]:
                return str(x_rate[1])
            
        except:
    
            return jsonify({'trace': traceback.format_exc()})
    
    def predict_usd(self,x_rate,tcmb):
        try:
    
    
            if x_rate[0] > tcmb[0]:
                return'X rate USD kuru = {} TCMB USD Kurundan {} daha büyüktür.'.format(x_rate[0], tcmb[0])
            elif x_rate[0] < tcmb[0]:
                return'TCMB USD Kuru = {} X rate USD kurundan {} daha büyüktür.' .format(tcmb[0],x_rate[0])
           
        except:
    
            return jsonify({'trace': traceback.format_exc()})
    
    def predict_eur(self,x_rate,tcmb):
        try:
    
    
            if x_rate[1] > tcmb[1]:
                return'X rate EUR kuru = {} TCMB EUR Kurundan {} daha büyüktür.'.format(x_rate[1], tcmb[1])
            elif x_rate[1] < tcmb[1]:
                return'TCMB EUR Kuru = {} X rate EUR kurundan {} daha büyüktür.' .format(tcmb[1],x_rate[1])
           
        except:
    
            return jsonify({'trace': traceback.format_exc()})
    

@app.route('/', methods=['GET']) 
def home():
    return """
<h1>Sayın Charlie Bey</h1>
<ul>
    <h2>Bugünün tarihinde kur karşılaştırması için aşağıdaki routelar kullanılmalıdır</h2>
    <li>USD karşılaştırmasını görmek için <mark>/USD</mark> kullanın lütfen</li>
    <ul>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/USD</b></li>
    </ul>
    <br></br>
    <li>EUR karşılaştırmasını görmek için <mark>/EUR</mark> kullanın lütfen</li>
    <ul>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/EUR</b></li>
    </ul>
    <br></br>
    <li>USD karşılaştırmasını sayı olarak almak isterseniz <mark>/USD/RATE</mark> kullanın lütfen</li>
    <ul>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/USD/RATE</b></li>
    </ul>
    <br></br>
    <li>EUR karşılaştırmasını sayı olarak almak isterseniz <mark>/EUR/RATE</mark> kullanın lütfen</li>
    <ul>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/EUR/RATE</b></li>
    </ul>
    
    <h2>İstenilen bir tarihte sorgulama yapılmak isteniyorsa aşağıdaki routelar kullanılmalıdır</h2>
    <li>USD karşılaştırması için <mark>/USD/<strong>tarih</strong></mark> kullanılcak. Tarih formatı <strong>2019-01-23</strong> olmalı </li>
    <ul>
        <li>Tarih Formatı:<b>Yıl-ay-gün</b></li>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/USD/2019-01-23</b></li>
    </ul>
    
    <br></br>

    <li>EUR karşılaştırması için <mark>/EUR/<strong>tarih</strong></mark> kullanılcak. Tarih formatı <strong>2019-01-23</strong> olmalı </li>
    <ul>
        <li>Tarih Formatı:<b>Yıl-ay-gün</b></li>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/EUR/2019-01-23</b></li>
    </ul>
    <br></br>

    <li>Küçük EUR değeri için <mark>/EUR/RATE/<strong>tarih</strong></mark> kullanılcak. Tarih formatı <strong>2019-01-23</strong> olmalı </li>
    <ul>
        <li>Tarih Formatı:<b>Yıl-ay-gün</b></li>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/EUR/RATE/2019-01-23</b></li>
    </ul>
    <br></br>

    <li>Küçük USD değeri için <mark>/USD/RATE/<strong>tarih</strong></mark> kullanılcak. Tarih formatı <strong>2019-01-23</strong> olmalı </li>
    <ul>
        <li>Tarih Formatı:<b>Yıl-ay-gün</b></li>
        <li>Örnek Kullanım:<b>http://127.0.0.1:5000/USD/RATE/2019-01-23</b></li>
    </ul>
    
</ul>
    """       
        
        
@app.route('/USD', methods=['GET'])
def usd():    
    sonuc = KurGosterme()
    response = sonuc.predict_usd()
    return response
    
@app.route('/EUR', methods=['GET'])
def eur():    
    sonuc = KurGosterme()
    response = sonuc.predict_eur()
    return response

@app.route('/USD/RATE', methods=['GET'])
def usd_rate():    
    sonuc = KurGosterme()
    response = sonuc.yalin_usd()
    return response

@app.route('/EUR/RATE', methods=['GET'])
def eur_rate():    
    sonuc = KurGosterme()
    response = sonuc.yalin_eur()
    return response

@app.route('/USD/RATE/<uuid>', methods=['GET', 'POST'])
def usd_rate_tarihli(uuid):
    content = request.get_json(silent=True)
    sonuc = TarihKurGosterme(uuid)
    response_xrate = sonuc.kur_ayarı()
    response_tcmb = sonuc.kur_ayarı_tcmb()
    real_response = sonuc.yalin_usd(response_xrate,response_tcmb)
    return real_response


@app.route('/EUR/RATE/<uuid>', methods=['GET', 'POST'])
def eur_rate_tarihli(uuid):
    content = request.get_json(silent=True)
    sonuc = TarihKurGosterme(uuid)
    response_xrate = sonuc.kur_ayarı()
    response_tcmb = sonuc.kur_ayarı_tcmb()
    real_response = sonuc.yalin_eur(response_xrate,response_tcmb)
    return real_response

@app.route('/USD/<uuid>', methods=['GET', 'POST'])
def usd_tarihli(uuid):
    content = request.get_json(silent=True)
    sonuc = TarihKurGosterme(uuid)
    response_xrate = sonuc.kur_ayarı()
    response_tcmb = sonuc.kur_ayarı_tcmb()
    real_response = sonuc.predict_usd(response_xrate,response_tcmb)
    return real_response

@app.route('/EUR/<uuid>', methods=['GET', 'POST'])
def eur_tarihli(uuid):
    content = request.get_json(silent=True)
    sonuc = TarihKurGosterme(uuid)
    response_xrate = sonuc.kur_ayarı()
    response_tcmb = sonuc.kur_ayarı_tcmb()
    real_response = sonuc.predict_eur(response_xrate,response_tcmb)
    return real_response

if __name__ == '__main__':
    app.run(debug=True)
