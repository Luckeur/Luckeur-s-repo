import requests

api="40c003a4fcc668644c2f9be5e95a2bb1"
base="http://api.openweathermap.org/data/2.5/weather?"
sehir=input("hangi şehrin hava durumunu görmek istiyorsun")
tamurl=base+"q="+sehir+"&appid="+api+"&units=metric"
respo=requests.get(tamurl)
data=respo.json()
a=f"Sıcaklık: {data['main']['temp']}°C"
print(a)
print(f"Açıklama: {data['weather'][0]['description']}")