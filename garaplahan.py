import os
import csv
import pandas as pd
from tabulate import tabulate

def cekakun() :
    if not os.path.exists('akun.csv'):
        with open('akun.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password'])

def login() :
    global usernamelogin
    os.system('cls')
    print('==================================================')
    print('                 LOGIN CUSTOMER                   ')
    print('==================================================')
    cekakun()
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')

    loginsukses = False
    with open('akun.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username and row['Password'] == password :
                loginsukses = True
                break

    if loginsukses :
        usernamelogin = username
        print('Login berhasil.')
        input('Tekan Enter untuk melanjutkan.')
        os.system('cls')
        menucustomer()  
    else :
        print('Username atau Password salah.')
        input('Tekan Enter untuk mencoba lagi.')
        os.system('cls')
        tampilanawal()  
 
def register() :
    os.system('cls')  
    print('==================================================')
    print('                    REGISTER                      ')
    print('==================================================') 
    cekakun()
    with open('akun.csv', mode='r') as file :
        username_sama = {row['Username'] for row in csv.DictReader(file)}
    
    username = input('Daftarkan Username anda : ')
    if len(username) < 2 :
        input('Username minimal 2 huruf. Tekan Enter untuk melanjutkan.')
        register()  
        
    elif username in username_sama :
        print('Username sudah digunakan!')
        input('Tekan Enter untuk melanjutkan.')
        register() 
        
    while True :
        password = input('Masukkan Kata Sandi: ')
        if len(password) < 8 :
            print('Password minimal 8 karakter.')
            continue  

        while True :
            cek = input('Apakah nama user dan password sudah sesuai (y/t): ').lower()
            if cek == 'y' :
                with open('akun.csv', mode='a', newline='') as file :
                    writer = csv.writer(file)
                    writer.writerow([username, password])
                print('Registrasi berhasil! Silahkan login.')
                input('Tekan Enter untuk melanjutkan.')
                tampilanawal()
            elif cek == 't' :
                input('Silahkan tekan Enter untuk kembali.')
                tampilanawal()    
            else :
                print('Input invalid, ulangi.')

def loginadmin() :
    os.system('cls' )
    print('==================================================')
    print('                   LOGIN ADMIN                    ')
    print('==================================================')
    if not os.path.exists('admin.csv') :
        with open('admin.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password'])  
            writer.writerow(['admin', 'admin123']) 

    Username = input('Masukkan Nama Pengguna Anda : ')
    Password = input('Masukkan Kata Sandi Anda : ')

    login_sukses = False
    with open('admin.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == Username and row['Password'] == Password:
                login_sukses = True
                break

    if login_sukses :
        print("Login Anda Sebagai Admin Berhasil")
        input('Tekan Enter Untuk Melanjutkan')
        os.system('cls')
        menuadmin()  
    else :
        print('Username atau Password salah')
        while True:
            cek = input('Apakah anda ingin melanjutkan (y/t) : ').lower()
            if cek == 'y':
                loginadmin()  
            elif cek == 't':
                input('Silahkan tekan Enter untuk kembali ke menu sebelumnya')
                os.system('cls')
                tampilanawal() 
            else:
                print('Inputan invalid')
                

# ===============================================================================================
def tampilanawal() :
    os.system('cls')
    print('===========================================================')
    print('     SELAMAT DATANG DI JASA PERAWATAN LAHAN PERTANIAN      ')
    print('                         "GARAP"                           ')
    print('===========================================================')
    print('Silahkan pilih menu login atau register')
    print('1. LOGIN CUSTOMER')
    print('2. LOGIN ADMIN')
    print('3. REGISTER')
    pilihan = input('Masukkan menu pilihan anda : ').lower()
    if pilihan == '1' or pilihan == 'login customer' :
        login()
    elif pilihan == '2' or pilihan == 'login admin' :
        loginadmin()
    elif pilihan == '3' or pilihan == 'register' :
        register()
    else :
        input('Pilihan tidak valid,tekan enter untuk melanjutkan')
        tampilanawal()

def cek_jadwalcsv() :
    if not os.path.exists('jadwal.csv'):
        with open('jadwal.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Tanggal', 'Nama Jasa', 'Harga', 'Jam Kerja', 'Slot Ketersediaan'])
            writer.writeheader()

def jadwal() :
    cek_jadwalcsv()
    df = pd.read_csv('jadwal.csv')
    if df.empty :
        print("Saat ini tidak ada jasa yang tersedia.")
    else :
        print("Jasa yang tersedia : ")
        print(tabulate(df, headers=["No"] + list(df.columns), tablefmt="fancy_grid", showindex=range(1, len(df) + 1)))

def menucustomer() :
    os.system('cls')
    print('==========================================================')
    print('                     SELAMAT DATANG                       ')
    print('               "GARAP" JASA PERAWATAN LAHAN               ')
    print('==========================================================')
    jadwal()
    print(f'Halo !! "{usernamelogin}" kami siap untuk anda')
    print('Pilih Menu anda : ')
    print('1. Pilih Jasa')
    print('2. Cek Riwayat Pemesanan')
    print('0. Keluar')
    while True :
        pilihan = input('Masukkan pilihan anda : ').lower()
        if pilihan == '1' or pilihan == 'pilih jasa' :
            os.system('cls')
            pilihjasa()
        elif pilihan == '2' or pilihan == 'cek riwayat pemesanan' :
            os.system('cls')
            riwayatpesanan()
        elif pilihan == '0' or pilihan == 'keluar' :
            os.system('cls')
            tampilanawal()
        else :
            input('Pilihan invalid,enter untuk ulang')
            os.system('cls')
            menucustomer()

def pilihjasa() :
    os.system('cls')
    jadwal()
    print(f'Silahkan pilih {usernamelogin}')
    print('1. Lanjut Pilih Jasa')
    print('0. Keluar')
    pilihan = input('Masukkan pilihan : ').lower()
    if pilihan == '1' or pilihan == 'lanjut pilih jasa' :
        os.system('cls')
        lanjutanjasa()
    elif pilihan == '0' or pilihan == 'keluar' :
        os.system('cls')
        menucustomer()
    else :
        input('pilihan invalid, enter untuk melanjutkan')
        os.system('cls')
        pilihjasa()

def cek_riwayatcsv() :
    if not os.path.exists('riwayat.csv'):
        with open('riwayat.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Username','Tanggal','Nama Jasa','Harga','Jam Kerja','Nomor Telfon','Alamat','Pembayaran','Kembalian','status'])
            writer.writeheader()

def lanjutanjasa():
    os.system('cls')
    tambahanpilihan = []
    jadwal()
    df = pd.read_csv('jadwal.csv')

    while True:
        try:
            pilihan = int(input("Masukkan nomor jasa yang ingin dipilih: "))
            if pilihan < 1 or pilihan > len(df):
                print("Nomor tidak valid")
                continue
        except ValueError:
            print("Input harus berupa angka")
            continue

        layanan = df.iloc[pilihan - 1]
        tanggal = layanan['Tanggal']
        jasa = layanan['Nama Jasa']
        jam = layanan['Jam Kerja']
        slot_tersedia = layanan['Slot Ketersediaan'] 

        if slot_tersedia <= 0 :
            print(f"Maaf, slot untuk jasa '{jasa}' pada tanggal {tanggal} jam {jam} sudah habis.")
            continue
        
        df.at[pilihan - 1, 'Slot Ketersediaan'] -= 1
        tambahanpilihan.append({
            'Index': pilihan - 1,
            'Tanggal': tanggal,
            'Nama Jasa': jasa,
            'Harga': layanan['Harga'],
            'Jam Kerja': jam
        })
        print(f"Jasa '{jasa}' pada tanggal '{tanggal}' berhasil ditambahkan ke daftar pemesanan.")
        print(f'Jumlah slot jasa yang tersisa {slot_tersedia - 1} ')

        while True:
            print('1. Lanjut Tambah Jasa')
            print('2. Lanjut Pembayaran')
            print('0. Keluar')

            lagi = input('Masukkan Pilihan: ').lower()

            if lagi == '1' or lagi == 'lanjut tambah jasa':
                 break
            elif lagi == '2' or lagi == 'lanjut pembayaran':
                os.system('cls')
                if pembayaran(tambahanpilihan):  
                    return
            elif lagi == '0' or lagi == 'keluar':
                os.system('cls')
                pilihjasa()
                return  
            else:
                print('Input tidak valid. Silakan coba lagi.')

def pembayaran(tambahanpilihan):
    os.system('cls')
    total_harga = 0
    print('==============================================================================')
    print('                     SELAMAT DATANG JASA PERAWATAN LAHAN                      ')
    print('                                   "GARAP"                                    ')
    print('==============================================================================')
    print("\nDaftar Pemesanan :")
    for layanan in tambahanpilihan:
        print(f"- Tanggal: {layanan['Tanggal']}, Jasa: {layanan['Nama Jasa']}, Harga: Rp {layanan['Harga']}, Jam Kerja: {layanan['Jam Kerja']}")
        total_harga += layanan['Harga']
    print(f"\nTotal Pembayaran: Rp. {total_harga}")
    while True:
        cek = input('Ingin melanjutkan pembayaran (y/t) : ')
        if cek == 'y':
            break
        elif cek == 't':
            os.system('cls')
            pilihjasa()
        else :
            print('Inputan Invalid')

    while True:
        try:
            bayar = int(input("Masukkan nominal pembayaran: Rp. "))
            if bayar < total_harga or bayar < 0:
                print("Nominal pembayaran kurang.")
            else:
                kembalian = bayar - total_harga
                print(f"Kembalian Anda: Rp. {kembalian}")
                break
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

    while True :
        alamat = input("\nMasukkan alamat Anda : ")

        while True :
                nomor_telepon = input("Masukkan nomor telepon Anda : ")
                if len(nomor_telepon) < 10:
                    print("Nomor telepon minimal 10 digit.")
                else:
                    break

        print(f"\nAlamat yang Anda masukkan: {alamat}")
        print(f"Nomor telepon yang Anda masukkan: {nomor_telepon}")

        konfirmasi = input("\nApakah informasi ini sudah benar? (y/t): ").lower()
        if konfirmasi == 'y':
            break
        elif konfirmasi == 't':
            print("Silakan masukkan kembali alamat dan nomor telepon.")
        else:
            print("Input tidak valid")

    cek_riwayatcsv()
    riwayat = []
    for layanan in tambahanpilihan:
        riwayat.append({
            'Username': usernamelogin,
            'Tanggal': layanan['Tanggal'],
            'Nama Jasa': layanan['Nama Jasa'],
            'Harga': layanan['Harga'],
            'Jam Kerja': layanan['Jam Kerja'],
            'Nomor Telepon': nomor_telepon,
            'Alamat': alamat,
            'Pembayaran': bayar,
            'Kembalian': kembalian,
            'Status': "Telah Dipesan"
        })

    riwayat_df = pd.DataFrame(riwayat)
    riwayat_df.to_csv('riwayat.csv', mode='a', header=False, index=False)

    df = pd.read_csv('jadwal.csv')
    for layanan in tambahanpilihan:
        index = layanan['Index']
        df.at[index, 'Slot Ketersediaan'] -= 1
    df.to_csv('jadwal.csv', index=False)

    print("\nPembayaran berhasil dilakukan!")
    input("Tekan Enter untuk melanjutkan.")
    os.system('cls')
    menucustomer()

    return True

def riwayatpesanan() :
    os.system('cls')
    print("==========================================================================================")
    print("                                 RIWAYAT PESANAN ANDA                                     ")
    print("==========================================================================================")
    cek_riwayatcsv()
    username = usernamelogin
    df = pd.read_csv('riwayat.csv', dtype={'Nomor Telfon': str})

    user_riwayat = df[df['Username'] == username]
    
    if user_riwayat.empty :
        print(f"Tidak ada riwayat pesanan")
    else :
        print(tabulate(user_riwayat[['Tanggal', 'Nama Jasa', 'Harga', 'Jam Kerja', 'Nomor Telfon', 'Alamat', 'Pembayaran', 'Kembalian', 'status']],
                       headers='keys', tablefmt='fancy_grid', showindex=False))
    
    input("\nTekan Enter untuk Kembali")
    os.system('cls')
    menucustomer()

# ================================================================================================
def menuadmin() :
    os.system('cls')
    print('==========================================================')
    print('                     SELAMAT DATANG                       ')
    print('               "GARAP" JASA PERAWATAN LAHAN               ')
    print('==========================================================')
    jadwal()
    print(f'Halo !! "Admin" ')
    print('Pilih Menu anda : ')
    print('1. Tambah Jadwal')
    print('2. Edit Jadwal')
    print('3. Hapus Jadwal')
    print('4. Cek Pemesanan Customer')
    print('0. Keluar')
    while True :
        pilihan = input('Masukkan pilihan anda : ').lower()
        if pilihan == '1' or pilihan == 'tambah jadwal' :
            os.system('cls')
            tambahjadwal()
        elif pilihan == '2' or pilihan == 'hapus jadwal' :
            os.system('cls')
            editjadwal()
        elif pilihan == '3' or pilihan == 'edit jadwal' :
            os.system('cls')
            hapusjadwal()
        elif pilihan == '4' or pilihan == 'cek pemesanan customer' :
            os.system('cls')
            pesanancustomer()
        elif pilihan == '0' or pilihan == 'keluar' :
            os.system('cls')
            tampilanawal()
        else :
            input('Pilihan invalid,enter untuk ulang')
            os.system('cls')
            menuadmin()

def tambahjadwal() :
    os.system('cls')
    jadwal()
    print('Pilih menu : ')
    print('1. Lanjut Tambah Jadwal')
    print('0. Keluar')
    pilihan = input('Masukkan Pilihan : ').lower()
    while True :
        if pilihan == '1' or pilihan == 'lanjut tambah jasa' :
            lanjuttambah()
        elif pilihan == '0' or pilihan == 'keluar' :
            menuadmin()
        else :
            input('Pilihan invalid,enter untuk ulang')
            os.system('cls')
            tambahjadwal()

def lanjuttambah() :
    os.system('cls')
    jadwal()
    cek_jadwalcsv()
    df = pd.read_csv('jadwal.csv')
    while True :
        print('Masukkan data jadwal baru :')
        tanggal = input('Tanggal (Contoh : 24 Mei 2024) : ').title()
        nama_jasa = input('Nama Jasa (Contoh : Membajak Sawah) : ').title()

        if not df[(df['Tanggal'] == tanggal) & (df['Nama Jasa'] == nama_jasa)].empty:
            print(f"Jadwal dengan Tanggal '{tanggal}' dan Jasa '{nama_jasa}' sudah ada")
            input("Tekan Enter untuk melanjutkan.")
            os.system('cls')
            lanjuttambah()

        while True :
            try :
                harga = int(input('Harga : Rp '))
                break
            except ValueError :
                print('Inputan harus berupa angka')

        jam_kerja = input('Jam Kerja (Contoh : 07:00-13:00) : ')
        while True :
            try:
                slot_ketersediaan = int(input('Jumlah Slot Ketersediaan: '))
                break
            except ValueError:
                print('Inputan harus berupa angka.')
        print('=========================================')
        print(f'Pastikan data berikut benar :')
        print(f'Tanggal : {tanggal}')
        print(f'Nama Jasa : {nama_jasa}')
        print(f'Harga : Rp {harga}')
        print(f'Jam Kerja : {jam_kerja}')
        print(f'Slot Ketersediaan : {slot_ketersediaan}')
        print('=========================================')
        print('1. Data sudah benar')
        print('2. Data Salah')
        print('0. Keluar')
        while True :
            konfirmasi = input('Masukkan Pilihan : ').lower()
            if konfirmasi == '1' or konfirmasi == 'data sudah benar' :
                break
            elif konfirmasi == '2' or konfirmasi == 'data salah':
                os.system('cls')
                lanjuttambah()
            elif konfirmasi == '0' or konfirmasi == 'keluar' :
                os.system('cls')
                tambahjadwal()
            else :
                print('Inputan invalid')
                
        df = pd.read_csv('jadwal.csv')
        new_row = {
            'Tanggal': tanggal,
            'Nama Jasa': nama_jasa,
            'Harga': harga,
            'Jam Kerja': jam_kerja,
            'Slot Ketersediaan': slot_ketersediaan
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv('jadwal.csv', index=False)
        print("\nJadwal berhasil ditambahkan!")
        input("Tekan Enter untuk kembali.")
        os.system('cls' )
        menuadmin()

def editjadwal() :
    os.system('cls')
    cek_jadwalcsv()
    print("Pilih Jadwal yang ingin diubah:")
    jadwal()
    df = pd.read_csv('jadwal.csv')
    
    while True :
        try :
            pilih = int(input("Pilih nomor jasa yang ingin diedit : "))-1
            if pilih < 0 or pilih >= len(df) :
                print("Nomor jasa tidak tersedia")
                os.system('cls')
                menuadmin()
            break
        except ValueError :
            print("Inputan harus berupa angka")

    baris = df.iloc[pilih]
          
    while True :
        jam_kerja = input(f'Masukkan jam kerja baru pada tanggal {baris['Tanggal']} jasa {baris['Nama Jasa']} (contoh 07:00-13:00) : ')
        try :
            harga = int(input(f"Masukkan harga baru dari {baris['Tanggal']} jasa {baris['Nama Jasa']} : Rp. "))
            slot_ketersediaan = int(input(f"Masukkan jumlah slot ketersediaan baru dari {baris['Tanggal']} jasa {baris['Nama Jasa']} : ")) 
            break
        except ValueError :
            print('Pastikan untuk harga dan slot ketersediaan berupa angka')
            
    while True :
        konfirmasi = input('Apakah anda yakin (y/t) : ')
        if konfirmasi == 'y' :
            break
        elif konfirmasi == 't' :
            os.system('cls')
            menuadmin()
        else :
            print('Inputan invalid')

    df.at[pilih, 'Jam Kerja'] = jam_kerja
    df.at[pilih, 'Harga'] = harga
    df.at[pilih, 'Slot Ketersediaan'] = slot_ketersediaan   

    df.to_csv('jadwal.csv', index=False)
    print("\nJadwal berhasil diperbarui!")
    input('Tekan enter untuk kembali')
    os.system('cls')
    menuadmin()

def hapusjadwal() :
    os.system('cls')
    cek_jadwalcsv()
    print("Pilih Jadwal yang ingin dihapus :")
    jadwal()
    df = pd.read_csv('jadwal.csv')

    while True:
        try:
            pilih = int(input('Pilih nomor jadwal yang ingin dihapus : '))-1
            if pilih < 0 or pilih >= len(df):
                print('Pilihan tidak ada di jadwal')
                continue
            break
        except ValueError:
            print('Inputan harus berupa angka')
    
    while True:
        konfirmasi = input('Apakah Anda yakin ingin menghapus jadwal ini (y/t) : ').lower()
        if konfirmasi == 'y' :
            df = df.drop(df.index[pilih])  
            df.to_csv('jadwal.csv', index=False)
            print("Jadwal berhasil dihapus!")
            input('Tekan enter untuk melanjutkan')
            os.system('cls')
            menuadmin()
        elif konfirmasi == 't' :
            print("Penghapusan jadwal dibatalkan")
            input('Tekan enter untuk kembali')
            os.system('cls')
            menuadmin()
        else :
            print('Inputan Invalid')

def pesanancustomer() :
    os.system('cls')
    print("Riwayat Pemesanan Seluruh Customer:")
    
    df = pd.read_csv('riwayat.csv', dtype={'Nomor Telfon': str})
    
    if df.empty:
        print("Tidak ada riwayat pemesanan.")
    else:
        print(tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))

    input("Tekan Enter untuk kembali.")
    os.system('cls')
    menuadmin()

tampilanawal()