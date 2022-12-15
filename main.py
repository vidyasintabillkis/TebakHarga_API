import tebakBeras, tebakGula, player, display

while True:
    a = ('1. Pilih Menu', '2. Exit')
    b = ['1. Tebak Harga Beras', '2. Tebak Harga Gula']
    pilih = 0 

    def pilihan() :
        display.display()
        global pilih
        for i in a : 
            print(i)
        while True :
            try : 
                pilih = int(input("\nMasukkan Pilihanmu\t : "))
                if pilih<=0 or pilih>2 :
                    raise ValueError
                print("")
                break
            except :
                print("Pilihan yang kamu masukkan tidak valid")
        choose() 
        

    def choose() :
        global pilih 
        if pilih == 1 : 
            for i in b : 
                print(i)
            pilihTebak = int(input("\nMasukkan Pilihanmu\t : "))
            nama = input("\nMasukkan Nama\t\t : ")
            playerIdentity = player.Player(nama)
            identityPlayer = open("identityPlayer.txt", "w")
            identityPlayer.write(playerIdentity.nama)
            identityPlayer.close()
            if pilihTebak == 1 : 
                tebakBeras.tebak()
            elif pilihTebak == 2 :
                tebakGula.tebak() 
            else :
                pilih()
        elif pilih == 2 :
            display.makasi()
            loopStatus = False
            quit()


    pilihan()