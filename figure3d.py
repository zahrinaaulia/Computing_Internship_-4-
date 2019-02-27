class Kubus:
	jumlah_sisi = 6
	def __init__(self,sisi):
		self.sisi = sisi
	def hitung_luas(self):
		luas = (self.sisi**2)*jumlah_sisi
		return luas
	def hitung_volume(self):
		volume = self.sisi**3
		return volume

class Balok:
	jumlah_sisi = 6
	def __init__(self, panjang, lebar, tinggi):
		self.panjang=panjang
		self.lebar=lebar
		self.tinggi=tinggi
	def hitung_luas(self):
		luas = (2*self.panjang*self.lebar)+(2*self.panjang*self.tinggi)+(2*self.lebar*self.tinggi)
		return luas
	def hitung_volume(self):
		volume = self.panjang*self.lebar*self.tinggi
		return volume

class Tabung:
	jumlah_sisi = 3
	def __init__(self,jari_jari,tinggi):
		self.jari_jari = jari_jari
		self.tinggi = tinggi
	def hitung_luas(self):
		luas = 2*3.14*self.jari_jari*(self.jari_jari + self.tinggi)
		return luas
	def hitung_volume(self):
		volume = 3.14*self.tinggi*(self.jari_jari**2)
		return volume

class Kerucut:
	jumlah_sisi = 2
	def __init__(self,jari_jari,tinggi):
		self.jari_jari=jari_jari
		self.tinggi=tinggi
	def hitung_luas(self):
		garis_pelukis = sqrt((self.jari_jari**2)+(self.tinggi**2))
		luas = 3.14 * self.jari_jari * (self.jari_jari + garis_pelukis)
		return luas
	def hitung_volume(self):
		luas = hitung_luas(self)
		volume = float(luas*self.tinggi/3)
		return volume