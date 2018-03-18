#Zadanie 8

s={"chleb":2.0, "woda":1.5,"cukier":5.0, "mleko":1.9, "pomidory":6.2}
list=["chleb", "cukierki", "mleko", "woda"]

def merge(slownik, lista):
        new_sl={}
        a=0
        for x in range(len(lista)):
            new_sl[lista[a]]=slownik.get(lista[a])
            a+=1
        print(new_sl.items())


merge(s,list)