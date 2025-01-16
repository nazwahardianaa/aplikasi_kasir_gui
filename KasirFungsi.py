#NAZWAHARDIANAA
import mysql.connector
import datetime
from collections import Counter
from prettytable import PrettyTable
harga_jual = {
    5: {1: 69000, 3: 68500, 5: 68000, 10: 67750},
    10: {1: 136000, 3: 135000, 5: 134000, 10: 133750},
    25: {1: 335000, 3: 334000, 5: 333000, 10: 332000}
}
harga_beli = {
    5: {1: 64000, 3: 63500, 5: 65000, 10: 62750},
    10: {1: 131000, 3: 130000, 5: 129000, 10: 128750},
    25: {1: 330000, 3: 329000, 5: 328000, 10: 327000}
}

conn = mysql.connector.connect(
    host='localhost', 
    user='root',  
    password='',  
    database='beberas',      
    port=3307                
)

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS stok (
    barang VARCHAR(255) PRIMARY KEY,
    jumlah INT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transaksi_masuk (
    id_masuk VARCHAR(255) PRIMARY KEY,
    tanggal_masuk DATE,
    barang_masuk VARCHAR(255),
    jumlah_masuk INT,
    harga_total_masuk FLOAT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS transaksi_keluar (
    id_keluar VARCHAR(255) PRIMARY KEY,
    tanggal_keluar DATE,
    barang_keluar VARCHAR(255),
    jumlah_keluar INT,
    harga_total_keluar FLOAT,
    total_harga_kulak FLOAT,
    keuntungan FLOAT
)
''')

'''def buat_idmasuk(counter):
    today = datetime.datetime.now()
    date_str = today.strftime('%Y%m%d')
    masuk = f"M{date_str}{counter:02d}"
    return masuk
simpan_idmasuk = {}

def token_masuk():
    today = datetime.datetime.now().strftime('%Y%m%d')  
    if today in simpan_idmasuk:
        simpan_idmasuk[today] += 1
    else:
        simpan_idmasuk[today] = 1    
    return buat_idmasuk(simpan_idmasuk[today])
'''
def ambil_id_masuk_terakhir():
    cursor.execute("SELECT id_masuk FROM transaksi_masuk ORDER BY id_masuk DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

def buat_idmasuk(counter):
    today = datetime.datetime.now()
    date_str = today.strftime('%Y%m%d')
    masuk = f"M{date_str}{counter:02d}"
    return masuk

def token_masuk():
    today = datetime.datetime.now().strftime('%Y%m%d')    
    last_id_masuk = ambil_id_masuk_terakhir()
    
    if last_id_masuk:
        last_date_str = last_id_masuk[1:9]  # Mengambil 8 karakter setelah 'K'
        if last_date_str == today:
            last_counter = int(last_id_masuk[9:])  # Mengambil bagian nomor urut
            counter = last_counter + 1
        else:
            counter = 1
    else:
        counter = 1
    
    return buat_idmasuk(counter)


def ambil_id_keluar_terakhir():
    cursor.execute("SELECT id_keluar FROM transaksi_keluar ORDER BY id_keluar DESC LIMIT 1")
    result = cursor.fetchone()
    if result:
        return result[0]
    return None

def buat_idkeluar(counter):
    today = datetime.datetime.now()
    date_str = today.strftime('%Y%m%d')
    keluar = f"K{date_str}{counter:02d}"
    return keluar

def token_keluar():
    today = datetime.datetime.now().strftime('%Y%m%d')    
    last_id_keluar = ambil_id_keluar_terakhir()
    
    if last_id_keluar:
        last_date_str = last_id_keluar[1:9]  # Mengambil 8 karakter setelah 'K'
        if last_date_str == today:
            last_counter = int(last_id_keluar[9:])  # Mengambil bagian nomor urut
            counter = last_counter + 1
        else:
            counter = 1
    else:
        counter = 1
    
    return buat_idkeluar(counter)


def simpan_transaksi_masuk(transaksim):
    cursor.execute('''
    INSERT INTO transaksi_masuk (id_masuk, tanggal_masuk, barang_masuk, jumlah_masuk, harga_total_masuk)
    VALUES (%s, %s, %s, %s, %s)
    ''', (transaksim['id_masuk'], transaksim['tanggal_masuk'], transaksim['barang_masuk'], transaksim['jumlah_masuk'], transaksim['harga_total_masuk']))
    conn.commit()

def simpan_transaksi_keluar(transaksik):
    cursor.execute('''
    INSERT INTO transaksi_keluar (id_keluar, tanggal_keluar, barang_keluar, jumlah_keluar, harga_total_keluar, total_harga_kulak, keuntungan)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (transaksik['id_keluar'], transaksik['tanggal_keluar'], transaksik['barang_keluar'], transaksik['jumlah_keluar'], transaksik['harga_total_keluar'], transaksik['total_harga_kulak'], transaksik['keuntungan']))
    conn.commit()

def tambah_stok(barang, jumlah):
    cursor.execute('''
    INSERT INTO stok (barang, jumlah) VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE jumlah = jumlah + %s
    ''', (barang, jumlah, jumlah))
    conn.commit()

def kurangi_stok(barang, jumlah):
    cursor.execute('''
    UPDATE stok SET jumlah = jumlah - %s WHERE barang = %s
    ''', (jumlah, barang))
    conn.commit()

def beli_beras(berat, jumlah):
    if berat not in harga_beli:
        print('Berat tidak valid, pilih antara 5, 10, atau 25 kg.')
        return 0

    jenis_kemasan = sorted(harga_beli[berat].keys(), key=lambda x: harga_beli[berat][x])    
    total_harga = 0
    sisa_jumlah = jumlah

    for kemasan in jenis_kemasan:
        jumlah_kemasan = sisa_jumlah // kemasan
        total_harga += jumlah_kemasan * harga_beli[berat][kemasan] * kemasan
        sisa_jumlah %= kemasan
        
        if sisa_jumlah == 0:
            break

    masuk = {
        'id_masuk': token_masuk(),  
        'tanggal_masuk': datetime.datetime.now().strftime("%Y-%m-%d"),
        'barang_masuk': f"{berat}kg",
        'jumlah_masuk': jumlah,
        'harga_total_masuk': total_harga
    }
    
    simpan_transaksi_masuk(masuk)
    tambah_stok(f"{berat}kg", jumlah)  # Tambah stok barang
    return total_harga

def kulak(berat, jumlah):
    if berat not in harga_beli:
        print('Berat tidak valid, pilih antara 5, 10, atau 25 kg.')
        return 0

    jenis_kemasan = sorted(harga_beli[berat].keys(), key=lambda x: harga_beli[berat][x])    
    total_harga = 0
    sisa_jumlah = jumlah

    for kemasan in jenis_kemasan:
        jumlah_kemasan = sisa_jumlah // kemasan
        total_harga += jumlah_kemasan * harga_beli[berat][kemasan] * kemasan
        sisa_jumlah %= kemasan
        
        if sisa_jumlah == 0:
            break
    return total_harga

# Fungsi jual beras
def jual_beras(berat, jumlah):
    if berat not in harga_jual:
        print('Berat tidak valid, pilih antara 5, 10, atau 25 kg.')
        return 0

    jenis_kemasan = sorted(harga_jual[berat].keys(), key=lambda x: harga_jual[berat][x])   
    total_harga = 0
    sisa_jumlah = jumlah

    for kemasan in jenis_kemasan:
        jumlah_kemasan = sisa_jumlah // kemasan
        total_harga += jumlah_kemasan * harga_jual[berat][kemasan] * kemasan
        sisa_jumlah %= kemasan

        if sisa_jumlah == 0:
            break
            
    total_harga_kulak = kulak(berat, jumlah)
    keuntungan = total_harga - total_harga_kulak

    # Simpan transaksi keluar
    keluar = {
        'id_keluar': token_keluar(),  
        'tanggal_keluar': datetime.datetime.now().strftime("%Y-%m-%d"),
        'barang_keluar': f"{berat}kg",
        'jumlah_keluar': jumlah,
        'harga_total_keluar': total_harga,
        'total_harga_kulak': total_harga_kulak,
        'keuntungan': keuntungan
    }
    
    simpan_transaksi_keluar(keluar)
    kurangi_stok(f"{berat}kg", jumlah)  # Kurangi stok barang
    return total_harga

def batal_keluar(id_keluar, keterangan):
    cursor.execute("SELECT barang_keluar, jumlah_keluar FROM transaksi_keluar WHERE id_keluar = %s", (id_keluar,))
    result = cursor.fetchone()

    if result:
        barang, jumlah = result
        cursor.execute("SELECT * FROM batal_keluar WHERE id_keluar = %s", (id_keluar,))
        if cursor.fetchone():
            print("Transaksi sudah dibatalkan sebelumnya.")
            return
        
        cursor.execute("UPDATE stok SET jumlah = jumlah + %s WHERE barang = %s", (jumlah, barang))
        
        tanggal_sekarang = datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO batal_keluar (id_keluar, tanggal_batal, keterangan) VALUES (%s, %s, %s)",
                       (id_keluar, tanggal_sekarang, keterangan))
        
        cursor.execute("""
            UPDATE transaksi_keluar 
            SET jumlah_keluar = 0, 
                harga_total_keluar = 0, 
                total_harga_kulak = 0, 
                keuntungan = 0 
            WHERE id_keluar = %s
        """, (id_keluar,))
        
        conn.commit()
        print("Order berhasil dibatalkan.")
    else:
        print("ID penjualan tidak ditemukan.")

def idcari_penjualan(id_keluar):
    cursor.execute("SELECT * FROM transaksi_keluar WHERE id_keluar = %s", (id_keluar,))
    result = cursor.fetchone()

    if result:
        return result  # Kembalikan hasil transaksi
    else:
        return None  # Kembalikan None jika tidak ditemukan

# Fungsi untuk mencari transaksi berdasarkan tanggal
def tglcari_penjualan(tanggal_keluar):
    cursor.execute("SELECT * FROM transaksi_keluar WHERE tanggal_keluar = %s", (tanggal_keluar,))
    result = cursor.fetchall()
    return result  # Kembalikan semua hasil yang ditemukan

# Fungsi untuk menampilkan rekap penjualan
def terbanyak():
    cursor.execute('SELECT barang_keluar, SUM(jumlah_keluar), SUM(harga_total_keluar) FROM transaksi_keluar GROUP BY barang_keluar')
    rows = cursor.fetchall()    
    # Hitung total penjualan per jenis kemasan
    kemasan_count = Counter()
    total_penjualan = 0
    
    for row in rows:
        barang = row[0]
        jumlah = row[1]
        harga_total = row[2]
        
        kemasan_count[barang] += jumlah
        total_penjualan += harga_total
    
    print("Rekap Penjualan:")
    print("----------------")
    for kemasan, jumlah in kemasan_count.items():
        print(f"{kemasan}: {jumlah} kemasan")
    print(f"Total penjualan keseluruhan: Rp {total_penjualan:.2f}")    
    # Cari barang terlaris
    if kemasan_count:
        barang_terlaris = kemasan_count.most_common(1)[0][0]
        print(f"Barang terjual paling banyak: {barang_terlaris}")

def tampilkan_menu():
    print("Menu Aplikasi Uas:")
    print("1. Melayani Penjualan")
    print("2. Menambah Stok")
    print("3. Membatalkan Penjualan")
    print("4. Menampilkan penjualan berdasarkan ID") 
    print("5. Menampilkan penjualan berdasarkan TANGGAL")
    print("6. Menampilkan Banyak Penjualan") #Lihat semua TK
    print("7. Menampilkan Rekap Penjualan") # TK beserta keuntungan
    print("8. Kemasan paling banyak terjual")
    print("9. Menampilkan transaksi masuk")
    print("10. Keluar Aplikasi")
'''
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        print('[ stok tersedia ]')
        cursor.execute('SELECT * FROM stok')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        berat = int(input('Masukkan jenis kemasan (5/10/25): '))
        jumlah = int(input('Masukkan banyak (kg): '))
        total_harga = float(jual_beras(berat, jumlah))
        print(f'Total penjualan: Rp {total_harga:.2f}')

    elif pilihan == '2':
        berat = int(input('Masukkan jenis kemasan (5/10/25): '))
        jumlah = int(input('Masukkan banyak (kg): '))
        total_harga = float(beli_beras(berat, jumlah))
        print(f'Total belanja: Rp {total_harga:.2f}')

    elif pilihan == '3':
        cursor.execute('SELECT * FROM transaksi_keluar')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        id_keluar = input("Masukkan ID transaksi yang ingin dibatalkan: ")
        keterangan = input('masukan alasan pembatalan order: ')
        batal_keluar(id_keluar,keterangan) 

    elif pilihan == '4':
        cariid = input("Masukkan ID penjualan yang ingin ditampilkan: ")      
        idcari_penjualan(cariid)

    elif pilihan == '5':
        caritgl = input("Masukkan tanggal penjualan yang ingin ditampilkan (ex= 2024-12-27): ")      
        tglcari_penjualan(caritgl)

    elif pilihan == '6':
        print('id_penjualan, tanggal (th-bln-tgl), kemasan, jumlah, total_penjualan')
        cursor.execute('SELECT id_keluar, tanggal_keluar, barang_keluar, jumlah_keluar, total_harga_kulak FROM transaksi_keluar')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif pilihan == '7':
        print('id_penjualan, tanggal (th-bln-tgl), kemasan, jumlah, total_penjualan, harga_kulak, keuntungan')
        cursor.execute('SELECT*FROM transaksi_keluar')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
    elif pilihan == '8':
        terbanyak()

    elif pilihan == '9':
        cursor.execute('SELECT * FROM transaksi_masuk')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
              
    elif pilihan == '10':
        print("Semoga Nilai A, amin")
        break
    else:
        print("Pilihan tidak valid.")
'''