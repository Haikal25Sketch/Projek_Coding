class dompet:

  def __init__(self,nama,saldo):
    self.nama = nama
    self._saldo = saldo
    self.riwayat = []

  @property
  def saldo(self):
    return self._saldo

  @saldo.setter
  def saldo(self,value):
    if value < 0:
      return

    self._saldo = value

  def __str__(self):
    return f'Dompet milik {self.nama} | Saldo : {self._saldo}'

  def tambah(self,value):
    if value < 0:
      print ('Saldo tidak bisa negatif')
    self._saldo += value
    hasil = f'+{value}'
    self.riwayat.append(hasil)

  def kurang(self,value):
    if value > 0 and self._saldo >= value:
      self._saldo -= value
      hasil = f'-{value}'
      self.riwayat.append(hasil)
    else:
      print ('Saldo Tidak Cukup')

  def __eq__(self,other):
    if not isinstance(other, dompet):
      return NotImplemented
    return self._saldo == other._saldo

  def __len__(self):
    return len(self.riwayat)

  def __iter__(self):
    for item in self.riwayat:
      yield item

  def __enter__(self):
    self.saldo_awal = self._saldo
    print (f'saldo awal anda {self.saldo_awal}')

  def __exit__(self,exc_type,exc_val,exc_tb):
    self.saldo_akhir = self._saldo
    selisih = self.saldo_akhir - self.saldo_awal
    if self.saldo_akhir > self.saldo_awal:
      print (f'Saldo anda +{selisih}')
    elif self.saldo_akhir < self.saldo_awal:
      print (f'Saldo anda -{selisih}')
    else:
      print ('Saldo anda tidak berubah')

    if selisih != 0:
      print (f'Selisih saldo anda {selisih}')
    else:
      None
    return False

wallet = dompet('Haikal',0)
wallet2 = dompet('HuTao',0)
# setter
wallet.saldo = 9000
wallet2.saldo = 8000
# print
print (wallet)
print (wallet2)
print()
# add and sub
wallet.tambah(1000)
wallet2.tambah(7000)
wallet.kurang(90)
wallet2.kurang(765)
print()
# eq
print ('Apakah wallet 1 dan 2 sama ?',wallet == wallet2)
# for
for wl in wallet:
  print (wl)
print()
for wl2 in wallet2:
  print (wl2)
print()
# with
with wallet as wl:
  wallet.tambah(1000000)
print()
with wallet2 as wl2:
  wallet2.tambah(980076)
