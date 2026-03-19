import sqlite3 as sql

con = sql.connect("otomasyon/Database/otomasyon.db")

cursor = con.cursor()

#Kullanıcı giris tabloları
def create_kullanici():
    cursor.execute("""CREATE TABLE KullaniciGiris(KullaniciAdi TEXT PRIMARY KEY NOT NULL,
                                    Sifre TEXT NOT NULL) """)
    cursor.execute("""CREATE TABLE KullaniciBilgi(KullaniciAdi TEXT PRIMARY KEY NOT NULL,
                                    email TEXT SECONDARY KEY NOT NULL,
                                    Ad TEXT NOT NULL, Soyad TEXT NOT NULL,
                                    Cinsiyet TEXT NOT NULL)""")

#Metotlarımızı çağırdığımız yer ana yapımız
#create_kullanici()

con.commit()