# Python'un resmi Docker imajını kullan
FROM python:3.11.4

# Çalışma dizinini ayarla
WORKDIR /C:\Users\user\Desktop\sayfalar

# Gereksinimleri yükle
COPY requirements.txt .
RUN pip install -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

EXPOSE 8000
# Django projesini çalıştır
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]