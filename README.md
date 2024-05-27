class Egitmen:
    def __init__(self, egitmen_id, ad, soyad, telefon, email, sifre, dogum_tarihi, cinsiyet, ilgi_alani):
        self.egitmen_id = egitmen_id
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.email = email
        self.sifre = sifre
        self.dogum_tarihi = dogum_tarihi
        self.cinsiyet = cinsiyet
        self.ilgi_alani = ilgi_alani

# Firebase'e eğitmenleri ekleyen fonksiyon
def egitmenleri_ekle(egitmen_listesi):
    ref = db.reference('egitmenler')  # Firebase'de 'egitmenler' tablosuna referans oluşturulur
    for egitmen in egitmen_listesi:
        egitmen_dict = egitmen.__dict__  # Eğitmen nesnesini bir sözlüğe dönüştürür
        ref.push(egitmen_dict)  # Sözlüğü Firebase'e ekler







class User:
    def __init__(self, ad, soyad, email, sifre):
        self.ad_soyad = ad, soyad
        self.email = email
        self.sifre = sifre

class Admin(User):
    def __init__(self, id, ad, soyad, email, sifre):
        super().__init__(ad, soyad, email, sifre)
        self.id = id

class Egitmen(User):
    def __init__(self, egitmen_id, ad, soyad, telefon, email, sifre, dogum_tarihi, cinsiyet, ilgi_alani):
        super().__init__(ad, soyad, email, sifre)
        self.egitmen_id = egitmen_id
        self.telefon = telefon
        self.dogum_tarihi = dogum_tarihi
        self.cinsiyet = cinsiyet
        self.ilgi_alani = ilgi_alani


class Uye(User):
    latest_id = 0  # Initialize a class variable to keep track of the latest ID

    def __init__(self, ad, soyad, telefon, email, sifre, dogum_tarihi, cinsiyet):
        Uye.latest_id += 1  # Increment the latest ID for each new user
        self.uye_id = Uye.latest_id  # Assign the new ID to the user
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.email = email
        self.sifre = sifre
        self.dogum_tarihi = dogum_tarihi
        self.cinsiyet = cinsiyet

class Uye2(User):
    latest_id = 0  # Initialize a class variable to keep track of the latest ID

    def __init__( self,email, sifre):
        Uye.latest_id += 1  # Increment the latest ID for each new user
        self.uye_id = Uye.latest_id  # Assign the new ID to the user
        self.email = email
        self.sifre = sifre





        kaydol->yeni_uye = Uye(ad, soyad, telefon, email, sifre, dogum_tarihi, cinsiyet)
        request.session['uye_id'] = yeni_uye.uye_id

        giris_yap_view->eski_uye = Uye2( email, sifre)
        request.session['uye_id2'] = eski_uye.uye_id 
