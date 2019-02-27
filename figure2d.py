import math
class Segitiga:
	jumlah_sisi = 3

class Segiempat:
	jumlah_sisi = 4

class Samasisi(Segitiga):
	def __init__(Self,sisi,tinggi):
		self.sisi = sisi
		self.tinggi = tinggi
	def hitung_luas(self):
		luas=float((self.sisi*self.tinggi)/2)
		return luas
	def hitung_keliling(self):
		keliling=self.sisi*3
		return keliling

class Samakaki(Segitiga):
	def __init__(self,alas,tinggi):
		self.alas=alas
		self.tinggi=tinggi
	def hitung_luas(self):
		luas=float((self.alas*self.tinggi)/2)
		return luas
	def hitung_keliling(self):
		sisi_samping = math.sqrt((self.alas**2) + (self.tinggi**2))
		keliling = self.alas+(sisi_samping*2)
		return keliling

class Persegi(Segiempat):
	def __init__(self,panjang,lebar):
		self.panjang=panjang
		self.lebar=lebar
	def hitung_luas(self):
		luas = self.panjang*self.lebar
		return luas
	def hitung_keliling(self):
		keliling = (self.panjang*2)+(self.lebar*2)
		return keliling

class Trapesium(Segiempat):
	def __init__(self,alas,tutup,tinggi):
		self.alas=alas
		self.tutup=tutup
		self.tinggi=tinggi
	def htiung_luas(self):
		luas = float(((self.alas+self.tutup)*self.tinggi)/2)
		return luas
	def hitung_keliling(self):
		temp = self.alas-self.tutup
		temp = float(temp/2)
		sisi_samping = ((temp**2)+(self.tinggi**2))
		keliling = self.alas + self.tutup + (sisi_samping*2)
		return keliling

class Jajargenjang(Segiempat):
	def __init__(self,alas,tinggi):
		self.alas=alas
		self.tinggi=tinggi
	def hitung_luas(self):
		luas=self.alas*self.tinggi
		return luas
	def hitung_keliling(self):
		luas=alas*4
		return luas