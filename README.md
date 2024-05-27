kaydol->yeni_uye = Uye(ad, soyad, telefon, email, sifre, dogum_tarihi, cinsiyet)
        request.session['uye_id'] = yeni_uye.uye_id

 courselistview->id = request.session.get('uye_id')
        id2 = request.session.get('uye_id2')

 giris_yap_view-> eski_uye = Uye2( email, sifre)
        request.session['uye_id2'] = eski_uye.uye_id

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





