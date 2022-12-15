import json
import requests, display

harga = requests.get('https://jibs.my.id/api/harga_komoditas')
hargaSuccess = harga.json()
data = hargaSuccess['national_commodity_price'] 
a = data['Gula Pasir']
provinsi = 0
h = 0 

def tebak() :
    print('\nKAMU MEMILIKI 3 NYAWA\n   SELAMAT BERMAIN\n')
    while True:
        provinsi = input("Masukkan Provinsi\t : ")
        for i in a:
            if provinsi.title() == i['name']:
                status = True
                break
            else:
                status = False
                continue
        if(status):
            break
        else:
            print("Provinsi tidak ada dalam data!")
            continue
    print("\nSilahkan masukkan tebakanmu dibawah ini!")
    j = 3
    while (j>0) : 
        try :
            guess = int(input("\nTebakan\t\t\t : "))
        except ValueError : 
            print('Inputan yang kamu masukkan tidak valid nih, silahkan masukkan kembali!')
        print("")
        for i in a : 
            if provinsi.title() == i['name'] : 
                harga = int(i['value'])
                if guess > harga :
                    print("Tebakanmu Terlalu Besar")
                    ratarata(guess, provinsi)
                elif guess < harga :
                    print("Tebakanmu Terlalu Kecil")
                    ratarata(guess, provinsi)
                else : 
                    print('MANTAP JIWA KAMU BERHASIL')
                    display.display()
                    quit() 
        j=j-1
        print("Sisa Nyawa\t\t :", j)
    print("/nKesempatanmu untuk menebak telah habis!/n")


def ratarata(guess, provinsi) :
    global h 
    total = 0 
    count = 0
    for i in a : 
        harga = int(i['value'])
        total += harga 
        count += 1 
    rataBeras = int(total/count)
    for i in a : 
        if provinsi.title() == i['name'] :
            harga = int(i['value'])
            if guess > harga : 
                h = rataBeras + harga
            elif guess < harga :
                h = rataBeras - harga
    print('-----------------------------------')
    print('|HINT                             |')
    print('|Rata-Rata Harga Beras\t : ', rataBeras,'|')
    print('|Ini Petunjuk Untukmu\t : ', h,'  |')
    print('-----------------------------------')





