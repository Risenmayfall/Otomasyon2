import tkinter as tk
from tkinter import ttk
from tkinter import messagebox #Mesaj kutusu kütüphanesi
import database as db #Bu benim database.py dosyam

pencere = tk.Tk() #Pencere oluşturan kod
pencere.title("Otomasyon Giriş")
width = 400
height = 400
pencere.geometry("400x400".format(400,400))
pencere.configure(bg="#0189e3")

#Kayıt Ol penceresi
def kayitol_pencere():
    pencere2 = tk.Toplevel(pencere) #Pencere oluşturan kod
    pencere2.title("Otomasyon Giriş")
    width = 600
    height = 800
    pencere2.geometry("800x600".format(width,height))
    pencere2.configure(bg="#0189e3")
    #KULLANICI ADI
    k_label1 = tk.Label(pencere2, text="Kullanıcı Adı", font=None, bg="#0189e3", fg="black")
    k_label1.pack(pady=5)
    k_adEntry = tk.Entry(pencere2, font=None, width=15, justify="left",fg="#000000")
    k_adEntry.pack(pady=5)
    #SIFRE YAZMA
    k_sifreLabel = tk.Label(pencere2, text="Şifrenizi Belirleyiniz", font=None, bg="#0189e3", fg="black")
    k_sifreLabel.pack(pady=5)
    k_sifre = tk.Entry(pencere2, font=None, width=15, justify="left",fg="#000000")
    k_sifre.pack(pady=5)
    #AD YAZMA
    k_AdLabel= tk.Label(pencere2, text="Adınızı Giriniz", font=None, bg="#0189e3", fg="black")
    k_AdLabel.pack(pady=5)
    k_ad = tk.Entry(pencere2, font=None, width=15, justify="left",fg="#000000")
    k_ad.pack(pady=5)
    #SOYAD
    k_SoyadLabel= tk.Label(pencere2, text="Soyadınızı Giriniz", font=None, bg="#0189e3", fg="black")
    k_SoyadLabel.pack(pady=5)
    k_soyad = tk.Entry(pencere2, font=None, width=15, justify="left",fg="#000000")
    k_soyad.pack(pady=5)
    #DOGUM TARİHİ
    k_dogLabel= tk.Label(pencere2, text="Doğum Tarihinizi Giriniz", font=None, bg="#0189e3", fg="black")
    k_dogLabel.pack(pady=5)
    k_dogum = tk.Entry(pencere2, font=None, width=15, justify="left",fg="#000000")
    k_dogum.pack(pady=5)
    #E-MAIL
    k_mailLabel= tk.Label(pencere2, text="Mailinizi Giriniz", font=None, bg="#0189e3", fg="black")
    k_mailLabel.pack(pady=5)
    k_mail = tk.Entry(pencere2, font=None, width=15, justify="left",fg="#000000")
    k_mail.pack(pady=5)
    #CİNSİYET
    k_cinsiyetLabel= tk.Label(pencere2, text="Cinsiyetinizi Belirtiniz", font=None, bg="#0189e3", fg="black")
    k_cinsiyetLabel.pack(pady=5)
    k_cinsiyet = tk.StringVar() #Bu tkinter'da özel değişken oluşturmaya sağlar.
    cinsiyet_combobox = ttk.Combobox(pencere2, width=27, textvariable=k_cinsiyet)
    cinsiyet_combobox.pack(pady=5)
    cinsiyet_combobox['values'] = ('Erkek','Kadın','Belirtmek İstemiyorum')
    cinsiyet_combobox.current(1) #Bu açılışta hangi değerle başlasın.
    #VERİTABANINA VERİ YOLLAMA FONKSİYONU
    def kayit_ol():
        kullanici_adi = k_adEntry.get()
        sifre = k_sifre.get()
        ad = k_ad.get()
        soyad = k_soyad.get()
        dog_tarih = k_dogum.get()
        mail = k_mail.get()
        cinsiyet = k_cinsiyet.get()
        
        try:
            db.cursor.execute("INSERT INTO KullaniciGiris(KullaniciAdi, Sifre) VALUES(?,?)",(kullanici_adi,sifre))
            db.cursor.execute("INSERT INTO KullaniciBilgi VALUES(?,?,?,?,?)",
                              (kullanici_adi,mail,ad,soyad,cinsiyet))
            db.con.commit()
            messagebox.showinfo("BAŞARILI!","Kullanıcı Kaydınız oldu. Ana sayfaya dönüp giriş yapın.")
            pencere2.destroy()
        except Exception as err:
            db.con.rollback()
            messagebox.showerror("HATA!","Eksik veya hatalı bilgi girdiniz.")

    #GONDER GİTSİN BUTONU
    button_gonder =tk.Button(pencere2, text="Gönder", fg="#0e9fff",
                             command=kayit_ol, width=15, justify="center")
    button_gonder.pack(pady=5)
    pencere2.mainloop()

def giris_yap():
    kullanici = kullaniciad_Entry.get()
    sifre = sifre_Entry.get()
    db.cursor.execute("SELECT Sifre FROM KullaniciGiris WHERE KullaniciAdi=?",(kullanici))
    sonuc = db.cursor.fetchone()
    if sonuc and sonuc[0] == sifre:
        messagebox.showinfo("BAŞARILI GİRİŞ", "HOŞGELDİNİZ")
    else:
        messagebox.showerror("HATA","Kullanıcı adı veya şifre hatalı!")

#UI -> User Interface
kullaniciad_label = tk.Label(pencere,text="Kullanıcı Adınızı Giriniz",font=None,
                            width=15, justify="left", bg="#0189e3", fg="#ffffff")
kullaniciad_label.place(x=100, y=50)

kullaniciad_Entry = tk.Entry(pencere, font=None, width=15, justify="left", fg="#000000")
kullaniciad_Entry.place(x=100, y=70)
#Şifre ve Butonlar
sifre_label = tk.Label(pencere,text="Şifrenizi Giriniz",font=None,
                            width=15, justify="left", bg="#0189e3", fg="#ffffff")
sifre_label.place(x=100, y=100)

sifre_Entry = tk.Entry(pencere, font=None, width=15, justify="left", fg="#000000")
sifre_Entry.place(x=100, y=120)

button_giris =tk.Button(pencere, text="Giriş", fg="#0e9fff",
                        command=giris_yap, width=15, justify="center")
button_giris.place(x=100, y=160)

button_kayit =tk.Button(pencere, text="Yeni Kayıt Oluştur", 
                        fg="#0e9fff",
                        command=kayitol_pencere, width=15, justify="center")
button_kayit.place(x=100, y=200)
pencere.mainloop()