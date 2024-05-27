UyeGirisiView->def dispatch(self, request, *args, **kwargs):
        if not has_permission(request.user, 'uye_giris'):

giris_yap_view->user = 
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
    
    
    
    ->>>authenticate(request, username=email, password=sifre)
                        login(request, user)
