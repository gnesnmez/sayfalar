import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
import firebase_admin
from firebase_admin import credentials, db, initialize_app
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from grpc import AuthMetadataContext, AuthMetadataPlugin, AuthMetadataPluginCallback
from rolepermissions.roles import assign_role
from django.core.cache import cache
from rolepermissions.checkers import has_permission
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



if not firebase_admin._apps:
    # If not initialized, initialize the Firebase app
 cred=credentials.Certificate('sayfa\istanbul-bd37f-firebase-adminsdk-mrbss-1fd2eb9363.json')
 firebase_admin.initialize_app(cred,{'databaseURL':"https://istanbul-bd37f-default-rtdb.firebaseio.com"})



import firebase_admin
from firebase_admin import credentials, db

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
            
class AnasayfaView(TemplateView):
    template_name = 'sayfa.html'

    def get_context_data(self, **kwargs):
        ref = db.reference("/hesaplar")
        firebase_data = ref.get()
        return {'firebase_data': firebase_data}
    
class GirisYapView(TemplateView):
    template_name = 'girisYap.html'


class UyeGirisiView(TemplateView):
    template_name = 'uye.html'
    def dispatch(self, request, *args, **kwargs):
        if not has_permission(request.user, 'uye_giris'):
            # Eğer kullanıcı bu sayfaya erişim iznine sahip değilse, istediğiniz başka bir sayfaya yönlendirin
            return redirect('sayfa')  # Örneğin, 'sayfa_erisim_yok' isimli bir URL'ye yönlendirin
        return super().dispatch(request, *args, **kwargs)


class UyeOlView(TemplateView):
    template_name = 'uyeOl.html'
    

class EgitmenGirisiView(TemplateView):
    template_name = 'egitmen.html'

class ProfilView(TemplateView):
    template_name = 'profil.html'   
    
class FirebaseDataView(TemplateView):
    template_name = 'firebase_data.html'

    def get_context_data(self, **kwargs):
        ref = db.reference("/hesaplar")
        firebase_data = ref.get()
        # Add logic to process and display Firebase data as needed
        return {'firebase_data': firebase_data}


from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from firebase_admin import db
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


def giris_yap_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        sifre = request.POST.get('sifre')
        ref = db.reference("/hesaplar")
        users = ref.order_by_child('email').equal_to(email).get()

        eski_uye = Uye2( email, sifre)
        request.session['uye_id2'] = eski_uye.uye_id

        if users:
            for user_key, user_data in users.items():
                
                if user_data.get('sifre') == sifre:
                    try:
                        # Attempt to find the user in Django's auth system by email
                        user = authenticate(request, username=email, password=sifre)
                        login(request, user)
                        rutbe = user_data.get('rutbe')
                        if rutbe == 'uye':
                            assign_role(user, 'lecturer')
                            return redirect('uyeGirisi')
                        elif rutbe == 'egitmen':
                            return redirect('egitmen')
                        elif rutbe == 'admin':
                            return redirect('adminGirisi')
                    except ObjectDoesNotExist:
                        # User does not exist in Django's auth system, handle accordingly
                        messages.error(request, 'Kullanıcı bulunamadı')
                        return render(request, 'girisYap.html')

        messages.error(request, 'Geçersiz e-posta veya şifre')
        return render(request, 'girisYap.html')
    
    return render(request, 'girisYap.html')




from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from firebase_admin import db

def kaydol(request):
    if request.method == 'POST':
        # Form verilerini al
        ad = request.POST.get('ad')
        soyad = request.POST.get('soyad')
        telefon = request.POST.get('telefon')
        email = request.POST.get('email')
        sifre = request.POST.get('sifre')
        dogum_tarihi = request.POST.get('yil')
        cinsiyet = request.POST.get('cinsiyet')
        
        # Yeni kullanıcı oluştur
        yeni_uye = Uye(ad, soyad, telefon, email, sifre, dogum_tarihi, cinsiyet)
        request.session['uye_id'] = yeni_uye.uye_id
        
        # Kullanıcı modelini al ve kaydet
        User = get_user_model()
        user = User.objects.create_user(
            username=email,
            password=sifre,
            dogum_tarihi=dogum_tarihi, 


        )
        # Özel alanları atayın
        
        user.soyad = soyad
        user.telefon = telefon
        user.cinsiyet = cinsiyet
        user.rutbe = "uye"
        user.save()

        # Role ataması yap
        assign_role(user, 'lecturer')

        # Veriyi Firebase Realtime Database'e kaydet
        ref = db.reference("/hesaplar")
        new_entry_ref = ref.push()
        new_entry_ref.set({
            'uye_id': yeni_uye.uye_id,
            'ad': yeni_uye.ad,
            'soyad': yeni_uye.soyad,
            'telefon': yeni_uye.telefon,
            'email': yeni_uye.email,
            'sifre': yeni_uye.sifre,
            'dogum_tarihi': yeni_uye.dogum_tarihi,
            'cinsiyet': yeni_uye.cinsiyet,
            'rutbe': 'uye'  # Varsayılan olarak yeni kayıtlar 'uye' olarak kaydedilir
        })

#         egitmenler = [
#     Egitmen(egitmen_id="11", ad="Cem", soyad="Şenkal", telefon="123456789", email="egitmen1@example.com",
#             sifre="1", dogum_tarihi="01/01/1990", cinsiyet="Erkek", ilgi_alani="Piyano"),
#     Egitmen(egitmen_id="12", ad="Gözde", soyad="Şenkal", telefon="987654321", email="egitmen2@example.com",
#             sifre="2", dogum_tarihi="01/01/1995", cinsiyet="Kadın", ilgi_alani="Gitar"),
#             Egitmen(egitmen_id="13", ad="Akif", soyad="Ersoy", telefon="123456789", email="egitmen3@example.com",
#             sifre="3", dogum_tarihi="01/01/1990", cinsiyet="Erkek", ilgi_alani="Dans"),
#     Egitmen(egitmen_id="14", ad="Mehmet", soyad="Selam", telefon="987654321", email="egitmen4@example.com",
#             sifre="4", dogum_tarihi="01/01/1995", cinsiyet="Kadın", ilgi_alani="Karakalem"),
#             Egitmen(egitmen_id="15", ad="Sıla", soyad="Aydın", telefon="123456789", email="egitmen5@example.com",
#             sifre="5", dogum_tarihi="01/01/1990", cinsiyet="Erkek", ilgi_alani="Kişisel gelişim"),
#     Egitmen(egitmen_id="16", ad="Tuğçe", soyad="Hanım", telefon="987654321", email="egitmen6@example.com",
#             sifre="6", dogum_tarihi="01/01/1995", cinsiyet="Kadın", ilgi_alani="Dil eğitimi"),
#     # Diğer eğitmenler buraya eklenebilir
# ]

# # Firebase'e eğitmenleri ekleyin
#         egitmenleri_ekle(egitmenler)

        return redirect('uyeGirisi')
    return render(request, 'uyeOl.html')





def profil_view(request):
    ad_soyad = cache.get('ad_soyad', 'Default Value')
    kullanici_telefon = cache.get('kullanici_telefon', 'Default Value')
    kullanici_email = cache.get('kullanici_email', 'Default Value')
    kullanici_sifre = cache.get('kullanici_sifre', 'Default Value')
    kullanici_dogum_tarihi = cache.get('kullanici_dogum_tarihi', 'Default Value')
    kullanici_cinsiyet = cache.get('kullanici_cinsiyet', 'Default Value')
    kullanici_ilgi_alani=cache.get('kullanici_ilgi_alani', 'Default Value')
    return render(request, 'profil.html', {'ad_soyad': ad_soyad,'kullanici_telefon': kullanici_telefon,'kullanici_email': kullanici_email,'kullanici_sifre': kullanici_sifre,'kullanici_dogum_tarihi': kullanici_dogum_tarihi,'kullanici_cinsiyet': kullanici_cinsiyet,'kullanici_ilgi_alani': kullanici_ilgi_alani})



from django.shortcuts import render, redirect
from django.views import View
from firebase_admin import db
from datetime import datetime

class CourseRegistrationView(View):
    def get(self, request):
        return render(request, 'course_registration.html')

    def post(self, request):
        course = request.POST.get('course')
        course_date = request.POST.get('courseDate')

        if not course or not course_date:
            # If the form is not properly filled, you might want to handle it
            return render(request, 'uye.html', {'error': 'Lütfen bir kurs ve tarih seçin.'})
        
        id = request.session.get('uye_id')
        id2 = request.session.get('uye_id2')  # Get the id2 from session
        print(id)
        print(id2)
        # If id is None, use id2
        if id is None and id2 is not None:
            id = id2

        # Prepare data to save
        data = {
            'course': course,
            'date': course_date,
            'registered_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'id': id,
        }

        # Reference to 'Kurslarım' table
        ref = db.reference('Kurslarım')
        new_course_ref = ref.push()
        new_course_ref.set(data)
        
        
        return render(request, 'uye.html', {'success': 'Kurs başarıyla kayıt edildi.'})




class CourseListView(View):
    def get(self, request):
        ref = db.reference('Kurslarım')
        courses = ref.get()

        id = request.session.get('uye_id')
        id2 = request.session.get('uye_id2')

        # Kullanılacak ID'yi belirle
        kullanilacak_id = id if id is not None else id2

        print(kullanilacak_id)

        if not courses:
            courses = {}

        course_list = []
        for key, value in courses.items():
            # Her bir kursun sahip olduğu 'uye_id' ile kullanıcının 'uye_id'sini karşılaştır
            if 'id' in value and value['id'] == kullanilacak_id:
                course_list.append(value)

        return JsonResponse(course_list, safe=False)




from firebase_admin import db
def get_instructor_by_interest(request):
    if request.method == 'POST':
        selected_course = request.POST.get('course')
        if selected_course:
            ref = db.reference('egitmenler')
            instructors = ref.order_by_child('ilgi_alani').equal_to(selected_course).get()
            if instructors:
                instructor = next(iter(instructors.values()))  # İlk eğitmene odaklan
                instructor_name = f"{instructor['ad']} {instructor['soyad']}"
                return JsonResponse({'instructor_name': instructor_name})
    return JsonResponse({'error': 'Seçilen kurs için eğitmen bulunamadı.'}, status=400)
















