#NAZWAHARDIANAA
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import KasirFungsi 
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='beberas',
    port=3307
)

cursor = conn.cursor()
class login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.5, relheight=1)

        tk.Label(left_frame, text="Selamat datang  |  Semangat Bekerja", font=("Arial", 12, "bold"), bg="#162daf", fg="white").pack(pady=29)
        
        self.image = tk.PhotoImage(file="D:\\tugas\\Pbo\\bakal uas\\Uas_LogoApp.png")  
        self.image = self.image.subsample(3, 3)  

 
        image_label = tk.Label(left_frame, image=self.image, bg="#162daf")
        image_label.pack(pady=15)
        tk.Label(left_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12), bg="#162daf", fg="white").pack(pady=29)

        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.5, relwidth=0.5, relheight=1)

        tk.Label(right_frame, text="Login", font=("Arial", 20, "bold"), bg="#ffffff", fg="black").pack(pady=35)
        tk.Label(right_frame, text="Awali semua dengan Bismillah.", font=("Arial", 12), bg="#ffffff", fg="#7f8c8d").pack(pady=5)

        # Form Username
        tk.Label(right_frame, text="Username", font=("Arial", 12), bg="#ffffff").pack(pady=(20, 5))
        self.username_entry = tk.Entry(right_frame, font=("Arial", 12), width=30, relief="solid", bd=1)
        self.username_entry.pack(pady=5)

        tk.Label(right_frame, text="Password", font=("Arial", 12), bg="#ffffff").pack(pady=(20, 5))
        self.password_entry = tk.Entry(right_frame, font=("Arial", 12), show="•", width=30, relief="solid", bd=1)
        self.password_entry.pack(pady=5)
        tk.Button(right_frame, text="Login", font=("Arial", 12, "bold"), bg="#162daf", fg="white", width=20, command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login Berhasil", "Hai, semoga PBO A, amin!")
            root.destroy()  # Tutup jendela login saat ini
            buka_dasbor() 
        else:
            messagebox.showerror("Login Gagal", "Cek kembali username atau password")
def buka_dasbor():
    dasbor_root = tk.Tk()
    dasbor(dasbor_root)  # Memanggil kelas dasbor dari log1.py
    dasbor_root.mainloop()

class dasbor:
    def __init__(self, root):
        self.root = root
        self.root.title("Dasbor")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)

        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1,command=self.buka_login).pack(side="bottom", fill="x", pady=51, padx=12)
        tk.Button(left_frame, text="order", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1, command=self.buka_order).pack(side="top", fill="x", pady=10, padx=12)
        tk.Button(left_frame, text="tambah stok", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1, command=self.buka_addstok).pack(fill="x", pady=5, padx=12)
        tk.Button(left_frame, text="batal order", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1, command=self.buka_batal).pack(fill="x", pady=5, padx=12)
        tk.Button(left_frame, text="cari penjualan", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1,command=self.buka_cari).pack(fill="x", pady=5, padx=12)
        tk.Button(left_frame, text="banyak penjualan", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1,command=self.buka_banyakpj).pack( fill="x", pady=5, padx=12)
        tk.Button(left_frame, text="rekap penjualan", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1,command=self.buka_rekappj).pack( fill="x", pady=5, padx=12)
        tk.Button(left_frame, text="transaksi keluar", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1,command=self.buka_tk).pack( fill="x", pady=5, padx=12)
        tk.Button(left_frame, text="transaksi masuk", font=("Arial", 9, "normal"), bg="white", fg="#162daf", anchor="center", width=1,command=self.buka_tm).pack( fill="x", pady=5, padx=12)

        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.3, relwidth=0.5, relheight=1)

        tk.Label(right_frame, text="Halaman menu utama | Grosir Maju Jaya", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=21)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom", fill="x", pady=51, padx=12)

        self.image = tk.PhotoImage(file="D:\\tugas\\Pbo\\bakal uas\\Uas_LogoApp.png")
        self.image = self.image.subsample(3, 3)
        image_label = tk.Label(right_frame, image=self.image, bg="white")
        image_label.pack(pady=15)

        tk.Label(right_frame, text="Awali semua dengan Bismillah.", font=("Arial", 12), bg="white", fg="#7f8c8d").pack(pady=5)
    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()
    def buka_order(self):
        order_root = tk.Toplevel(self.root)  
        orderapp = order(order_root)  
        order_root.mainloop()
    def buka_addstok(self):
        addstok_root = tk.Toplevel(self.root)  
        addstokapp = addstok(addstok_root)  
        addstok_root.mainloop()
    def buka_batal(self):
        batal_root = tk.Toplevel(self.root)  
        batalapp = batal(batal_root)  
        batal_root.mainloop()
    def buka_cari(self):
        Cari_root = tk.Toplevel(self.root)  
        cariapp = Cari(Cari_root)  
        Cari_root.mainloop()
    def buka_banyakpj(self):
        banyak_penjualan_root = tk.Toplevel(self.root)  
        banyakapp = banyak_penjualan(banyak_penjualan_root)  
        banyak_penjualan_root.mainloop()
    def buka_rekappj(self):
        rekap_penjualan_root = tk.Toplevel(self.root)  
        rekapapp = rekap_penjualan(rekap_penjualan_root)  
        rekap_penjualan_root.mainloop()
    def buka_tk(self):
        t_keluar_root = tk.Toplevel(self.root)  
        tkeluarapp = t_keluar(t_keluar_root)  
        t_keluar_root.mainloop()
    def buka_tm(self):
        t_masuk_root = tk.Toplevel(self.root)  
        tmasukapp = t_masuk(t_masuk_root)  
        t_masuk_root.mainloop()

class order:
    def __init__(self, root):
        self.root = root
        self.root.title("Order")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)

        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1, command=self.buka_login).pack(side="bottom", fill="x", pady=51, padx=12)

        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.27, relwidth=0.577, relheight=1)

        tk.Label(right_frame, text="HALAMAN PELAYANAN PENJUALAN", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=12)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom", fill="x", pady=51, padx=12)

        tk.Label(right_frame, text="berat (5/10/25)", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.kemasan_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.kemasan_entry.place(relx=0.037, rely=0.19, relwidth=0.3)

        tk.Label(right_frame, text="jumlah (kg)", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.jumlah_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.jumlah_entry.place(relx=0.037, rely=0.32, relwidth=0.3)

        rp = tk.Label(right_frame,text="Rp.",font=("Arial", 12),bg="white",anchor="w")
        rp.place(relx=0.037, rely=0.46, relwidth=0.3)  # Menggunakan place() untuk tata letak

        tk.Label(right_frame, text="Total belanja", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.total_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.total_entry.place(relx=0.135, rely=0.45, relwidth=0.3)

        tambah_button = tk.Button(right_frame, text="tambahkan", font=("Arial", 9, "normal"), bg="#162daf", fg="white", anchor="center", command=self.penjualan)
        tambah_button.place(relx=0.037, rely=0.68, relwidth=0.2)

        self.tree = ttk.Treeview(right_frame, columns=("kemasan", "jumlah"), show="headings")
        self.tree.place(relx=0.66, rely=0.17, relwidth=0.25, relheight=0.3)

        self.tree.heading("kemasan", text="Kemasan")
        self.tree.heading("jumlah", text="Jumlah")
        self.tree.column("kemasan", width=50, anchor="center")
        self.tree.column("jumlah", width=50, anchor="center")

        self.load_data()  # Memuat data saat inisialisasi

    def load_data(self):
        # Clear the existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            cursor.execute("SELECT * FROM stok")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def penjualan(self):
        try:
            # Ambil input dari entry
            berat = int(self.kemasan_entry.get())
            jumlah = int(self.jumlah_entry.get())

            # Panggil fungsi jual_beras dari KasirFungsi
            total_harga = KasirFungsi.jual_beras(berat, jumlah)
            # Tampilkan total_harga di total_entry
            self.total_entry.delete(0, tk.END)
            self.total_entry.insert(0, str(total_harga))
            self.load_data()  # Memperbarui tampilan data setelah transaksi

        except ValueError:
            self.total_entry.delete(0, tk.END)
            self.total_entry.insert(0, "Input tidak valid")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()

    def buka_dasbor():
        dasbor_root = tk.Tk()
        dasbor(dasbor_root)  # Memanggil kelas dasbor dari log1.py
        dasbor_root.mainloop()     
class addstok:
    def __init__(self, root):
        self.root = root
        self.root.title("tambah stok")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)  # Adjust width to 0.15
        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1, command=self.buka_login).pack( side="bottom",fill="x", pady=51, padx=12)
        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.27, relwidth=0.577, relheight=1.051)  # Adjust x position
        tk.Label(right_frame, text="HALAMAN TAMPILAN PEMBELIAN (kulak)", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=12)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom",fill="x", pady=31, padx=12)

        tk.Label(right_frame, text="kemasan (5/10/25)", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.kemasan_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.kemasan_entry.place(relx=0.037, rely=0.19, relwidth=0.3)  # relwidth mengontrol proporsi lebar

        stok =tk.Label(right_frame, text="stok barang saat ini", font=("Arial", 10), bg="white",fg="#162daf", anchor="w")
        stok.place(relx=0.65, rely=0.121, relwidth=0.3)  # relwidth mengontrol proporsi lebar
        tk.Label(right_frame, text="jumlah (kg)", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.jumlah_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.jumlah_entry.place(relx=0.037, rely=0.32, relwidth=0.3)  # relwidth mengontrol proporsi lebar
        # JUMLAH entry
        rp = tk.Label(right_frame,text="Rp.",font=("Arial", 12),bg="white",anchor="w")
        rp.place(relx=0.037, rely=0.46, relwidth=0.3)  # Menggunakan place() untuk tata letak

        tk.Label(right_frame, text="Total belanja stok (kulak)", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.total_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.total_entry.place(relx=0.155, rely=0.46, relwidth=0.3)  # relwidth mengontrol proporsi lebar

        tambah_button = tk.Button(right_frame,text="tambah",font=("Arial", 9, "normal"),bg="#162daf",fg="white",anchor="center",command=self.pembelian)
        tambah_button.place(relx=0.037, rely=0.68, relwidth=0.2)  # Mengatur lebar relatif
        
        # Treeview untuk tabel
        self.tree = ttk.Treeview(right_frame, columns=("barang", "jumlah"), show="headings")
        self.tree.place(relx=0.66, rely=0.17, relwidth=0.25, relheight=0.25)  # Menggunakan place() untuk lebih kontrol

        # Konfigurasi kolom
        self.tree.heading("barang", text="kemasan")
        self.tree.heading("jumlah", text="jumlah")
        self.tree.column("barang", width=50, anchor="center")
        self.tree.column("jumlah", width=50, anchor="center")
        self.load_data()

    def load_data(self):
        try:
            cursor.execute("SELECT * FROM stok")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def pembelian(self):
        try:
        # Ambil input dari entry
            berat = int(self.kemasan_entry.get())
            jumlah = int(self.jumlah_entry.get())
        
        # Panggil fungsi jual_beras dari KasirFungsi
            total_harga = KasirFungsi.beli_beras(berat, jumlah)
        
            self.total_entry.delete(0, tk.END)  # Hapus isi sebelumnya
            self.total_entry.insert(0, str(total_harga))  # Masukkan total_harga
        
        except ValueError:
            self.total_entry.delete(0, tk.END)
            self.total_entry.insert(0, "Input tidak valid")  # Menangani input yang tidak valid
        except Exception as e:
            messagebox.showerror("Error", str(e))  # Menangani kesalahan lain
    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()

class batal:
    def __init__(self, root):
        self.root = root
        self.root.title("batal")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)  # Adjust width to 0.15
        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1,command=self.buka_login).pack( side="bottom",fill="x", pady=51, padx=12)

        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.3, relwidth=0.55, relheight=1)  
        tk.Label(right_frame, text="HALAMAN PELAYANAN PEMBATALAN ORDER", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=12)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom",fill="x", pady=51, padx=12)

        tk.Label(right_frame, text="id_penjualan", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.keluar_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.keluar_entry.place(relx=0.037, rely=0.19, relwidth=0.3)  # relwidth mengontrol proporsi lebar
        # KETERANGAN entry
        tk.Label(right_frame, text="keterangan", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.keterangan_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.keterangan_entry.place(relx=0.037, rely=0.32, relwidth=0.3)  # relwidth mengontrol proporsi lebar

        tk.Label(right_frame, text="Status pembatalan transaksi", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.total_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.total_entry.place(relx=0.037, rely=0.46, relwidth=0.5, relheight=0.05)  # relwidth mengontrol proporsi lebar

        batal_button = tk.Button(right_frame,text="batalkan",font=("Arial", 9, "normal"),bg="#162daf",fg="white",anchor="center",command=self.batal)
        batal_button.place(relx=0.037, rely=0.65, relwidth=0.2)  # Mengatur lebar relatif
        
        tampil_button = tk.Button(right_frame,text="tampilkan",font=("Arial", 9, "normal"),bg="#162daf",fg="white",anchor="center",command=self.buka_tampilbatal)
        tampil_button.place(relx=0.037, rely=0.73, relwidth=0.2)  # Mengatur lebar relatif

        hasilid =tk.Label(right_frame, text="transaksi penjualan", font=("Arial", 10), bg="white",fg="#162daf", anchor="w")
        hasilid.place(relx=0.6, rely=0.13, relwidth=0.3)  # relwidth mengontrol proporsi lebar  
        self.tree = ttk.Treeview(right_frame, columns=("id_keluar", "barang_keluar"), show="headings")
        self.tree.place(relx=0.6, rely=0.19, relwidth=0.39, relheight=0.25)  # Menggunakan place() untuk lebih kontrol

        self.tree.heading("id_keluar", text="id_keluar")
        self.tree.heading("barang_keluar", text="jenis kemasan")
        for column in ["id_keluar", "barang_keluar"]:
            self.tree.column(column, width=43, anchor="center")
        self.load_data()
    def load_data(self):
        try:
            cursor.execute('SELECT id_keluar, barang_keluar FROM transaksi_keluar') 
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")    
    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()

    def batal(self):
        try:
            id_keluar = self.keluar_entry.get().strip()
            keterangan = self.keterangan_entry.get().strip()

            if not id_keluar or not keterangan:
                messagebox.showwarning("Input Error", "ID Penjualan dan Keterangan harus diisi.")
                return

            KasirFungsi.batal_keluar(id_keluar, keterangan)

            cursor.execute("""
                UPDATE transaksi_keluar 
                SET jumlah_keluar = 0,
                    harga_total_keluar = 0, 
                    total_harga_kulak = 0, 
                    keuntungan = 0 
                WHERE id_keluar = %s
            """, (id_keluar,))
            conn.commit()  

            self.total_entry.delete(0, tk.END)  
            self.total_entry.insert(0, "Pembatalan berhasil.")  
            self.load_data()

        except ValueError:
            self.total_entry.delete(0, tk.END)
            self.total_entry.insert(0, "Input tidak valid")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def buka_tampilbatal(self):
        tampil_batal_root = tk.Tk()
        tampil_batal(tampil_batal_root)
        tampil_batal_root.mainloop()

class tampil_batal:
    def __init__(self, root):
        self.root = root
        self.root.title("tampil_batal")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)  # Adjust width to 0.15
        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1,command=self.buka_login).pack( side="bottom",fill="x", pady=51, padx=12)

        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.3, relwidth=0.55, relheight=1)  # Adjust x position
        tk.Label(right_frame, text="Menampilkan Transaksi yang Dibatalkan", font=("Arial", 10, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=12)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom",fill="x", pady=51, padx=12)

        self.tree = ttk.Treeview(right_frame, columns=("id_keluar", "tanggal_batal","keterangan"), show="headings")
        self.tree.place(relx=0.037, rely=0.1, relwidth=0.79, relheight=0.69)  # Menggunakan place() untuk lebih kontrol

        self.tree.heading("id_keluar", text="id_keluar")
        self.tree.heading("tanggal_batal", text="tanggal_batal")
        self.tree.heading("keterangan", text="keterangan")
        self.tree.column("id_keluar", width=50, anchor="center")
        for column in ["id_keluar","tanggal_batal", "keterangan"]:
            self.tree.column(column, width=20, anchor="center")
        self.load_data()

    def load_data(self):
        try:
            cursor.execute('SELECT*FROM batal_keluar') 

            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()

class Cari:
    def __init__(self, root):
        self.root = root
        self.root.title("Cari")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)
        tk.Button(left_frame, text="Keluar", font=("Arial", 9), bg="yellow", fg="#162daf", command=self.buka_login).pack(side="bottom", fill="x", pady=51, padx=12)

        right_frame = tk.Frame(self.root, bg="white")
        right_frame.place(relx=0.27, relwidth=0.7, relheight=1)
        tk.Label(right_frame, text="HALAMAN PENCARIAN TRANSAKSI PENJUALAN", font=("Arial", 12), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=12)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12), bg="white", fg="#162daf", anchor="w").pack(side="bottom", fill="x", pady=51, padx=12)

        a=tk.Label(right_frame, text="id_penjualan (ex: K2024122701)", font=("Arial", 11), bg="white", anchor="w")
        a.place(relx=0.037, rely=0.13, relwidth=0.43)
        self.keluar_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.keluar_entry.place(relx=0.037, rely=0.19, relwidth=0.3)  # relwidth mengontrol proporsi lebar

        # KETERANGAN entry
        b=tk.Label(right_frame, text="tanggal penjualan (ex: 2024-12-27)", font=("Arial", 11), bg="white", anchor="w")
        b.place(relx=0.037, rely=0.27, relwidth=0.43)
        self.tanggal_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.tanggal_entry.place(relx=0.037, rely=0.32, relwidth=0.3)  # relwidth mengontrol proporsi lebar

        tacari= tk.Label(right_frame, text="Transaksi yang dicari", font=("Arial", 11), bg="white", anchor="w")
        tacari.place(relx=0.037, rely=0.5, relwidth=0.3)
      
        cari_button = tk.Button(right_frame, text="Cari", font=("Arial", 9), bg="#162daf", fg="white", command=self.cari_transaksi)
        cari_button.place(relx=0.83, rely=0.19, relwidth=0.13)

        hasil_label = tk.Label(right_frame, text="Transaksi Penjualan", font=("Arial", 10), bg="white", fg="#162daf", anchor="w")
        hasil_label.place(relx=0.5, rely=0.13, relwidth=0.3)

        # Treeview untuk hasil awal
        self.tree = ttk.Treeview(right_frame, columns=("id_keluar", "barang_keluar"), show="headings")
        self.tree.place(relx=0.5, rely=0.19, relwidth=0.29, relheight=0.25)

        self.tree.heading("id_keluar", text="ID Keluar")
        self.tree.heading("barang_keluar", text="Jenis Kemasan")

        # Mengatur lebar kolom
        self.tree.column("id_keluar", width=50, anchor="center")
        self.tree.column("barang_keluar", width=50, anchor="center")

        # Treeview untuk hasil pencarian
        self.tree_hasil = ttk.Treeview(right_frame, columns=("id_keluar", "tanggal_keluar", "barang_keluar", "jumlah_keluar", "harga_total_keluar"), show="headings")
        self.tree_hasil.place(relx=0.037, rely=0.55, relwidth=0.93, relheight=0.27)

        # Menambahkan heading untuk kolom hasil pencarian
        self.tree_hasil.heading("id_keluar", text="ID Keluar")
        self.tree_hasil.heading("tanggal_keluar", text="Tanggal Keluar")
        self.tree_hasil.heading("barang_keluar", text="Jenis Kemasan")
        self.tree_hasil.heading("jumlah_keluar", text="Jumlah Keluar")
        self.tree_hasil.heading("harga_total_keluar", text="Harga Total")

        # Mengatur lebar kolom hasil pencarian
        self.tree_hasil.column("id_keluar", width=50, anchor="center")
        self.tree_hasil.column("tanggal_keluar", width=50, anchor="center")
        self.tree_hasil.column("barang_keluar", width=50, anchor="center")
        self.tree_hasil.column("jumlah_keluar", width=50, anchor="center")
        self.tree_hasil.column("harga_total_keluar", width=50, anchor="center")

        self.load_data()  # Memuat data awal

    def load_data(self):
        try:
            cursor.execute('SELECT id_keluar, barang_keluar FROM transaksi_keluar')
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def cari_transaksi(self):
        # Clear previous results dari tree_hasil
        for item in self.tree_hasil.get_children():
            self.tree_hasil.delete(item)

        # Mengambil ID Penjualan
        id_penjualan = self.keluar_entry.get().strip()
        if id_penjualan:
            try:
                result = KasirFungsi.idcari_penjualan(id_penjualan)
                if result:
                    self.tree_hasil.insert("", "end", values=result)
                else:
                    messagebox.showinfo("Info", "ID transaksi tidak ditemukan.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        # Mengambil Tanggal Penjualan
        tanggal_penjualan = self.tanggal_entry.get().strip()
        if tanggal_penjualan:
            try:
                results = KasirFungsi.tglcari_penjualan(tanggal_penjualan)
                if results:
                    for row in results:
                        self.tree_hasil.insert("", "end", values=row)
                else:
                    messagebox.showinfo("Info", "Tanggal tidak ditemukan.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()

class banyak_penjualan:
    def __init__(self, root):
        self.root = root
        self.root.title("banyak_penjualan")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)  # Adjust width to 0.15
        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1,command=self.buka_login).pack( side="bottom",fill="x", pady=51, padx=12)

        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.3, relwidth=0.55, relheight=1)  # Adjust x position
        tk.Label(right_frame, text="Menampilkan Banyak Penjualan", font=("Arial", 10, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=12)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom",fill="x", pady=51, padx=12)
        tk.Label(right_frame, text="id_penjualan", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.keluar_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.keluar_entry.place(relx=0.037, rely=0.19, relwidth=0.3)  # relwidth mengontrol proporsi lebar
        # KETERANGAN entry
        tk.Label(right_frame, text="keterangan", font=("Arial", 12), bg="white", anchor="w").pack(fill="x", pady=21, padx=12)
        self.keterangan_entry = tk.Entry(right_frame, font=("Arial", 12), width=15, relief="solid", bd=1)
        self.keterangan_entry.place(relx=0.037, rely=0.32, relwidth=0.3)  # relwidth mengontrol proporsi lebar

        self.tree = ttk.Treeview(right_frame, columns=("tanggal_keluar", "5kg","10kg","25kg"), show="headings")
        self.tree.place(relx=0.037, rely=0.1, relwidth=0.79, relheight=0.69)  # Menggunakan place() untuk lebih kontrol

        self.tree.heading("tanggal_keluar", text="tanggal_keluar")
        self.tree.heading("5kg", text="5kg")
        self.tree.heading("10kg", text="10kg")
        self.tree.heading("25kg", text="25kg")
        self.tree.column("tanggal_keluar", width=50, anchor="center")
        for column in ["tanggal_keluar","5kg", "10kg", "25kg"]:
            self.tree.column(column, width=20, anchor="center")
        self.load_data()

    def load_data(self):
        try:
            cursor.execute('''
            SELECT 
                tanggal_keluar, 
                SUM(jumlah_keluar * (barang_keluar = '5kg')) AS "5Kg", 
                SUM(jumlah_keluar * (barang_keluar = '10kg')) AS "10Kg", 
                SUM(jumlah_keluar * (barang_keluar = '25kg')) AS "25Kg" 
            FROM 
                transaksi_keluar 
            GROUP BY 
                tanggal_keluar 
            ORDER BY 
                tanggal_keluar
''')
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()

class rekap_penjualan:
    def __init__(self, root):
        self.root = root
        self.root.title("rekap_penjualan")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)  # Adjust width to 0.15
        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1,command=self.buka_login).pack( side="bottom",fill="x", pady=51, padx=12)
        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.23, relwidth=0.75, relheight=1)  # Adjust x position
        tk.Label(right_frame, text="Menampilkan Rekap Penjualan", font=("Arial", 10, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=20)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom",fill="x", pady=51, padx=12)

        self.tree = ttk.Treeview(right_frame, columns=("tanggal_keluar", "5kg","10kg","25kg","Total Penjualan","Total Modal","Keuntungan"), show="headings")
        self.tree.place(relx=0.033, rely=0.1, relwidth=0.95, relheight=0.69)  # Menggunakan place() untuk lebih kontrol

        self.tree.heading("tanggal_keluar", text="tanggal_keluar")
        self.tree.heading("5kg", text="5kg")
        self.tree.heading("10kg", text="10kg")
        self.tree.heading("25kg", text="25kg")
        self.tree.heading("Total Penjualan", text="Total Penjualan")
        self.tree.heading("Total Modal", text="Total Modal")
        self.tree.heading("Keuntungan", text="Keuntungan")
        for column in ["tanggal_keluar", "Total Penjualan", "Total Modal", "Keuntungan"]:
            self.tree.column(column, width=43, anchor="center")
        for column in ["5kg", "10kg", "25kg"]:
            self.tree.column(column, width=20, anchor="center")

        self.load_data()

    def load_data(self):
        try:
            cursor.execute('''
                SELECT 
                    tanggal_keluar,
                    barang_keluar,
                    SUM(jumlah_keluar) AS total_jumlah_keluar,
                    SUM(harga_total_keluar) AS total_harga_keluar,
                    SUM(total_harga_kulak) AS total_harga_kulak,
                    SUM(keuntungan) AS total_keuntungan
                FROM 
                    transaksi_keluar
                GROUP BY 
                    tanggal_keluar, barang_keluar
                ORDER BY 
                    tanggal_keluar, barang_keluar;
''')
            rows = cursor.fetchall()
            rekap_data = {}
    
            for row in rows:
                tanggal, barang, total_jumlah, total_harga, total_modal, total_keuntungan = row
                if tanggal not in rekap_data:
                    rekap_data[tanggal] = {
                        "5Kg": 0,
                        "10Kg": 0,
                        "25Kg": 0,
                        "Total Penjualan": 0,
                        "Total Modal": 0,
                        "Keuntungan": 0
                }        
                if barang == '5kg':
                    rekap_data[tanggal]["5Kg"] += total_harga
                elif barang == '10kg':
                    rekap_data[tanggal]["10Kg"] += total_harga
                elif barang == '25kg':
                    rekap_data[tanggal]["25Kg"] += total_harga            
                rekap_data[tanggal]["Total Penjualan"] += total_harga
                rekap_data[tanggal]["Total Modal"] += total_modal
                rekap_data[tanggal]["Keuntungan"] += total_keuntungan
            for tanggal, data in rekap_data.items():
                self.tree.insert("", "end", values=(tanggal, data["5Kg"], data["10Kg"], data["25Kg"], data["Total Penjualan"], data["Total Modal"], data["Keuntungan"]))
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

    def buka_login(self):
        login_root = tk.Toplevel(self.root)  
        loginapp = login(login_root)  
        login_root.mainloop()

class t_keluar:
    def __init__(self, root):
        self.root = root
        self.root.title("Transaksi Keluar")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)
        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1).pack(side="bottom", fill="x", pady=51, padx=12)
        
        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.23, relwidth=0.75, relheight=1)
        tk.Label(right_frame, text="Menampilkan Seluruh Transaksi Penjualan", font=("Arial", 10, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=20)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom", fill="x", pady=51, padx=12)

        self.tree = ttk.Treeview(right_frame, columns=("id_keluar", "tanggal_keluar", "barang_keluar", "jumlah_keluar", "harga_total_keluar", "total_harga_kulak", "keuntungan"), show="headings")
        self.tree.place(relx=0.033, rely=0.1, relwidth=0.95, relheight=0.69)

        # Mengatur judul kolom
        self.tree.heading("id_keluar", text="ID Penjualan")
        self.tree.heading("tanggal_keluar", text="Tanggal Penjualan")
        self.tree.heading("barang_keluar", text="Jenis Kemasan")
        self.tree.heading("jumlah_keluar", text="Terjual (kg)")
        self.tree.heading("harga_total_keluar", text="Harga Jual")
        self.tree.heading("total_harga_kulak", text="Total Harga Kulak")
        self.tree.heading("keuntungan", text="Keuntungan")

        # Mengatur lebar kolom
        for column in ["id_keluar", "tanggal_keluar", "harga_total_keluar", "total_harga_kulak", "keuntungan"]:
            self.tree.column(column, width=50, anchor="center")
        for column in ["barang_keluar", "jumlah_keluar"]:
            self.tree.column(column, width=20, anchor="center")

        self.load_data()

    def load_data(self):
        # Membersihkan Treeview sebelum memuat data
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            cursor.execute("SELECT * FROM transaksi_keluar")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

class t_masuk:
    def __init__(self, root):
        self.root = root
        self.root.title("Transaksi Masuk")
        self.root.geometry("800x500")
        self.root.configure(bg="#ffffff")

        left_frame = tk.Frame(self.root, bg="#162daf")
        left_frame.place(relwidth=0.2, relheight=1)
        tk.Button(left_frame, text="keluar", font=("Arial", 9, "normal"), bg="yellow", fg="#162daf", anchor="center", width=1).pack(side="bottom", fill="x", pady=51, padx=12)
        
        right_frame = tk.Frame(self.root, bg="#ffffff")
        right_frame.place(relx=0.23, relwidth=0.75, relheight=1)
        tk.Label(right_frame, text="Menampilkan Seluruh Transaksi Pembelian (KULAK)", font=("Arial", 10, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="top", fill="x", pady=12, padx=20)
        tk.Label(right_frame, text="Toko Maju Jaya, JL.Brawijaya No.56 Nganjuk", font=("Arial", 12, "normal"), bg="white", fg="#162daf", anchor="w").pack(side="bottom", fill="x", pady=51, padx=12)

        self.tree = ttk.Treeview(right_frame, columns=("id_masuk", "tanggal_masuk","barang_masuk", "jumlah_masuk", "harga_total_masuk"), show="headings")
        self.tree.place(relx=0.033, rely=0.1, relwidth=0.95, relheight=0.69)

        # Mengatur judul kolom
        self.tree.heading("id_masuk", text="ID Kulak")
        self.tree.heading("tanggal_masuk", text="Tanggal Kulak")
        self.tree.heading("barang_masuk", text="Jenis Kemasan")
        self.tree.heading("jumlah_masuk", text="Terbeli (kg)")
        self.tree.heading("harga_total_masuk", text="Harga Kulak")

        for column in ["id_masuk", "tanggal_masuk", "harga_total_masuk"]:
            self.tree.column(column, width=50, anchor="center")
        for column in ["barang_masuk", "jumlah_masuk"]:
            self.tree.column(column, width=20, anchor="center")

        self.load_data()

    def load_data(self):
        # Membersihkan Treeview sebelum memuat data
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            cursor.execute("SELECT * FROM transaksi_masuk")
            rows = cursor.fetchall()
            for row in rows:
                self.tree.insert("", "end", values=row)
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

if __name__=="__main__":
    root = tk.Tk()
    app = login(root)
    root.mainloop()

conn.close()  # Close database connection