from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'access_uye_beslenme_page': True,  # Bu izni 'Admin' rolüne verebilirsiniz
    }

class Lecturer(AbstractUserRole):
    available_permissions = {
        'uye_giris': True,  # 'Öğretim Üyesi' rolüne bu izni vermeyin
    }



