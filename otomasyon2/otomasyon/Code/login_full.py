import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
import os

# Veritabanı ayarları
os.makedirs("Database", exist_ok=True)
con = sql.connect("Database/otomasyon.db")
cursor = con.cursor()

# --- Fonksiyonlar ---
def giris_yap():
    kullanici = kullaniciad_Entry.get().strip()
    sifre = sifre_Entry.get().strip()

    if not kullanici or not sifre:
        messagebox.showwarning("Eksik Bilgi", "Kullanıcı adı ve şifre gerekli.")
        return

    cursor.execute("SELECT Sifre FROM KullaniciGiris WHERE KullaniciAdi=?", (kullanici,))
    sonuc = cursor.fetchone()

    if sonuc and sonuc[0] == sifre:
        messagebox.showinfo("Başarılı", f"Hoş geldin, {kullanici}!")
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış.")

def kayit_penceresi():
    pencere2 = tk.Toplevel()
    pencere2.title("Kayıt Ol")
    pencere2.geometry("300x400")
    pencere2.configure(bg="#0189e3")

    # Etiketler ve girişler
    tk.Label(pencere2, text="Kullanıcı Adı", bg="#0189e3", fg="white").pack(pady=5)
    k_entry = tk.Entry(pencere2)
    k_entry.pack()

    tk.Label(pencere2, text="Şifre", bg="#0189e3", fg="white").pack(pady=5)
    s_entry = tk.Entry(pencere2, show="•")
    s_entry.pack()

    tk.Label(pencere2, text="E-posta", bg="#0189e3", fg="white").pack(pady=5)
    e_entry = tk.Entry(pencere2)
    e_entry.pack()

    tk.Label(pencere2, text="Ad", bg="#0189e3", fg="white").pack(pady=5)
    a_entry = tk.Entry(pencere2)
    a_entry.pack()

    tk.Label(pencere2, text="Soyad", bg="#0189e3", fg="white").pack(pady=5)
    so_entry = tk.Entry(pencere2)
    so_entry.pack()

    tk.Label(pencere2, text="Cinsiyet", bg="#0189e3", fg="white").pack(pady=5)
    c_entry = tk.Entry(pencere2)
    c_entry.pack()

    def kayit_ol():
        k = k_entry.get().strip()
        s = s_entry.get().strip()
        e = e_entry.get().strip()
        a = a_entry.get().strip()
        so = so_entry.get().strip()
        c = c_entry.get().strip()

        if not k or not s:
            messagebox.showwarning("Eksik Bilgi", "Kullanıcı adı ve şifre zorunludur.")
            return

        cursor.execute("SELECT 1 FROM KullaniciGiris WHERE KullaniciAdi=?", (k,))
        if cursor.fetchone():
            messagebox.showerror("Hata", "Bu kullanıcı adı zaten alınmış.")
            return

        try:
            cursor.execute("INSERT INTO KullaniciGiris VALUES (?,?)", (k, s))
            cursor.execute("INSERT INTO KullaniciBilgi VALUES (?,?,?,?,?,?)", (k, e, a, so, c))
            con.commit()
            messagebox.showinfo("Başarılı", "Kayıt oluşturuldu!")
            pencere2.destroy()
        except Exception as err:
            con.rollback()
            messagebox.showerror("Hata", f"Kayıt eklenemedi: {err}")

    tk.Button(pencere2, text="Kaydı Oluştur", command=kayit_ol, width=20).pack(pady=20)

# --- Ana pencere ---
pencere = tk.Tk()
pencere.title("Otomasyon Giriş")
pencere.geometry("400x300")
pencere.configure(bg="#0189e3")

tk.Label(pencere, text="Kullanıcı Adınızı Giriniz", bg="#0189e3", fg="white").pack(pady=10)
kullaniciad_Entry = tk.Entry(pencere)
kullaniciad_Entry.pack()

tk.Label(pencere, text="Şifrenizi Giriniz", bg="#0189e3", fg="white").pack(pady=10)
sifre_Entry = tk.Entry(pencere, show="•")
sifre_Entry.pack()

tk.Button(pencere, text="Giriş", command=giris_yap, width=15).pack(pady=10)
tk.Button(pencere, text="Yeni Kayıt Oluştur", command=kayit_penceresi, width=15).pack()

pencere.mainloop()
