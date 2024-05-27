Roles.py:from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'access_uye_beslenme_page': True,  # Bu izni 'Admin' rolüne verebilirsiniz
    }

class Lecturer(AbstractUserRole):
    available_permissions = {
        'uye_giris': True,  # 'Öğretim Üyesi' rolüne bu izni vermeyin
    }

models.py:class User(AbstractUser):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    sifre = models.CharField(max_length=100)
    rutbe = models.CharField(max_length=20, default='uye')
    dogum_tarihi = models.DateField()
    cinsiyet = models.CharField(max_length=10)
    telefon = models.CharField(max_length=20)

    class Meta:
        swappable = 'AUTH_USER_MODEL'



User.groups.related_name = 'custom_user_groups'
User.user_permissions.related_name = 'custom_user_permissions'

settings.py:ROLEPERMISSIONS_MODULE = 'sayfalar.roles'
AUTH_USER_MODEL = 'sayfa.User'
INSTALLED_APPS = [
    'sayfa.apps.SayfaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rolepermissions',
    'sayfalar',  
    

]

views.py: Kaydol-> # Kullanıcı modelini al ve kaydet
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

giris_yap_view-> eski_uye = Uye2( email, sifre)
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


imports->
from grpc import AuthMetadataContext, AuthMetadataPlugin, AuthMetadataPluginCallback
from rolepermissions.roles import assign_role
from django.core.cache import cache
from rolepermissions.checkers import has_permission
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




Projemizde bulunan uye ye kişisel rol tanımı yapıldı ve roles.py sayfasında izin verilen sayfalara erişim sağlayabiliyor izin i olmayan sayfalara ise rol tanımı sayesinde giriş yapamıyor.


                            


