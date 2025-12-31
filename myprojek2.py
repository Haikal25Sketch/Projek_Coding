class Transaksi:

    def __init__(self,tipe:str,jumlah:int):
        if tipe not in ("SETOR","TARIK"):
            raise ValueError ("Tipe hanya bisa\n'SETOR'dan'TARIK")
        if jumlah <=0:
            raise ValueError ("Jumlah transaksi harus angka positif")
        self.tipe = tipe
        self.jumlah = jumlah

    def __str__(self):
        return f'{self.tipe} : {self.jumlah}'

    def __repr__(self):
        return f'Transaksi("{self.tipe}" ":" "{self.jumlah}")'



class dompet:

    def __init__(self,nama,saldo):
        self.nama = nama
        self.__saldo = saldo
        self.riwayat =[]

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,other):
        if other < 0:
            return None
        self.__saldo = other

    def setor(self,value):
        if value < 0:
            print ('Saldo tidak bisa negatif')
        self.__saldo += value
        hasil = Transaksi ("SETOR",value)
        self.riwayat.append(hasil)

    def tarik(self,value):
        if self.__saldo < value:
            print ('Saldo anda tidak cukup')
        self.__saldo -= value
        hasil = Transaksi('TARIK',value)
        self.riwayat.append(hasil)

    def total_setor(self):
        hasil = 0
        for s in self.riwayat:
            if s.tipe == "SETOR":
                hasil += s.jumlah
        return hasil
        
    def transaksi_setor(self):
        return[s for s in self.riwayat if s.tipe == "SETOR"]
    def total_tarik(self):
        hasil = 0
        for t in self.riwayat:
            if t.tipe == "TARIK":
                hasil += jumlah
        return hasil
    def transaksi_tarik(self):
        return [t for t in self.riwayat if t.tipe == "TARIK"]
        
    def __add__(self,other):
        return dompet (self.nama,self.__saldo + other)

    def __sub__(self,other):
        return dompet (self.nama,self.__saldo - other)

    def __eq__(self,other):
        if not isinstance(other,dompet):
            return NotImplemented
        return self.__saldo == other.__saldo and self.nama == other.nama

    def __iter__(self):
        for item in self.riwayat:
            yield item

    def __enter__(self):
        self.saldo_awal = self.__saldo
        print ('Saldo awal :',self.saldo_awal)
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.saldo_akhir = self.__saldo
        selisih = self.saldo_akhir - self.saldo_awal
        print ('Saldo akhir :',self.saldo_akhir)
        if self.saldo_akhir >= self.saldo_awal:
            print (f'Bertambah +{selisih}')
        elif self.saldo_akhir <= self.saldo_awal:
            print (f'Berkurang -{selisih}')
      
d1 = dompet ('Haikal',8000)
d2 = dompet ('Yaemiko',9000)
d1.setor(8977)
d1.tarik(76)
print (f'Saldo {d1.nama} :Rp.{d1.saldo}')
print (f'Saldo {d2.nama} :Rp.{d2.saldo}')
d1 +=8000
print (d1.saldo)
d1.setor(8)
d1.setor(89)
print ('Apakah d1 dan d2 sama ?',d1 == d2)
for a in d1:
  print (a)
print()
d2.setor(645484546)
d2.tarik (87)
for b in d2:
  print (b)

print ('Total setor d1 :',d1.transaksi_setor())
print (d2.saldo)
