'''ini Judul'''
def header():
    print(f"{'PROGRAM MENGHITUNG LINGKARAN' : ^60}")
    print(f"{'-' *30: ^60}")

'''ini untuk input'''
def input_user():
     jari = float(int(input('Masukkan Jari-Jari : ' )))    
     return jari

'''ini untuk Keliling'''
def keliling(jari):
        if jari %7 ==0 :
            keliling = 2*( 22/7) * jari 
        else:
            keliling = 2 * 3.14 * jari 
        return keliling

'''ini untuk Luas''' 
def luas(jari):
    if jari %7 == 0:
        luas = (22/7) * jari **2
    else:
        luas = 3.14 * jari **2   
    return luas   

'''ini untuk hasil'''
def hasil(luas,keliling):
    print(f"hasil untuk luas adalah {ls}")
    print('-'*30)
    print(f"hasil untuk keliling adalah {kl}")


'''Program'''
while True:
    
    header()
    jari=input_user()
    kl=keliling(jari)
    ls=luas(jari)
    hasil(luas,keliling)
    
    lanjut = input('Apakah lanjut (y/n) :  ')
    if lanjut == 'n':
        break
print('Program Selesai,Terima Kasih')        


