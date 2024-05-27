from django.urls import path
from .views import AnasayfaView
from .views import GirisYapView
from .views import ProfilView
from .views import UyeGirisiView
from .views import UyeOlView
from .views import CourseRegistrationView
from .views import CourseListView
from .views import kaydol
from .views import giris_yap_view
from .views import profil_view
from .views import get_instructor_by_interest
from . import views

urlpatterns=[
    path('',AnasayfaView.as_view(),name='sayfa'),
    path('girisYap/',GirisYapView.as_view(),name='girisYap'),
    path('antrenorGirisi/',GirisYapView.as_view(),name='antrenorGirisi'),
    path('profil/',ProfilView.as_view(),name='profil'),
    path('uyeGirisi/',UyeGirisiView.as_view(),name='uyeGirisi'),
    path('uyeOl/',UyeOlView.as_view(),name='uyeOl'),
    path('kaydol/', views.kaydol, name='kaydol'),
    path('giris_yap_view/', views.giris_yap_view, name='giris_yap_view'),
     path('course-registration/', CourseRegistrationView.as_view(), name='course_registration'),
      path('course-list/', CourseListView.as_view(), name='course_list'),
        path('get_instructor_by_interest/', get_instructor_by_interest, name='get_instructor_by_interest'),
    path('profil_view/', profil_view, name='profil_view'),
]