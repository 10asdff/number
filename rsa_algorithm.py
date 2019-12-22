def asalmi(sayi):# p ile q sayısının asal olup olmadığına bakıyor
	for i in range(2,sayi):
		if(sayi%i==0):raise ValueError("HATA : p veya q Sayıları Asal Değildir")

def aralarindaasalmi(e,φ):#e sayısı ile φ sayısı aralarında asal olup olmadığına bakıyor
	if(e>1 and e<φ):pass
	else:raise ValueError("HATA : e Sayısı 1 ile φ Arasında Olmalıdır")

	if(φ%e==0):raise ValueError("HATA : e ve φ Aralarında Asal Değildir")

def modbirmi(d,e,φ):#girilen d sayısının e ile çarpımından mod φ'ye göre modun 1 olup olmadığına bakıyor
	de=d*e
	if(de%φ==1):pass
	else:raise ValueError("HATA : Böyle bir d Sayısı Veremezsiniz")

try:
	# p ile q sayıları giriliyor
	p=int(input("Birinci Asal Sayı Giriniz : "))
	q=int(input("İkinci Asal Sayı Giriniz: "))
	asalmi(p)
	asalmi(q)

	#girilen p ile q sayılarından n ve φ(n) sonucu bulunuyor
	n=p*q
	print("n = ",n)
	φ=(p-1)*(q-1)
	print("φ(n) : ",φ)

	#e sayısı giriliyor
	e=int(input("e Sayısını Giriniz(φ ile aralarında asal olmalıdır) : "))
	aralarindaasalmi(e,φ)

	#d sayısı giriliyor
	d=int(input("d Sayısını Giriniz : "))
	modbirmi(d,e,φ)

	#Mesaj giriliyor
	mesaj=int(input("Mesaj Gir : "))

	#Girilen mesajı şifreli haline dönüştürülüyor
	sifrelenmismesaj=(mesaj**e)%n
	print(sifrelenmismesaj)

	#Şifrelenmiş mesaj düz mesaj haline dönüştürülüyor
	duzmesaj=(sifrelenmismesaj**d)%n
	print(duzmesaj)

# Örnek input : p=61,q=53,e=17,d=2753

except ValueError as hata:

	print(hata.args[0])
	exit()