# Mengimpor sebagian dari modul datetime
from datetime import datetime, timedelta 

# Daftar buku untuk setiap genre
Novel = ["Laskar Pelangi", "Negeri 5 Menara", "Bumi Manusia", "Rumah Kaca"] 
Romansa = ["Dilan: Dia adalah Dilanku Tahun 1990", "Rindu", "Kirana", "London: Angel"]
Biografi = ["Habibie & Ainun", "Soekarno: An Autobiography as Told to Cindy Adams", "Chairul Tanjung: Si Anak Singkong", "Tan Malaka: Gerakan Kiri dan Revolusi Indonesia"]
Motivasi = ["Zero to Hero", "Mindset", "Atomic Habits", "Think and Grow Rich"]
Horror = ["Gadis Kretek", "Pintu Terlarang", "Klub Bulan", "Jejak Langkah"]
Drama = ["Amba", "Saman", "Tanah Tabu", "Jelita Sejuba"]

# Inisialisasi variabel untuk menyimpan buku yang dipinjam
pinjaman = {}  

# Menggabungkan setiap daftar genre buku ke dalam satu nama array
daftarBuku = Novel + Romansa + Biografi + Motivasi + Horror + Drama

# Loop utama program
while True:
    # Menu Aplikasi
    print('\nDaftar Menu Perpustakaan')
    print('1. Daftar Buku')
    print('2. Mencari Buku')
    print('3. Meminjam Buku')
    print('4. Kembalikan Buku')
    print('5. Keluar')
    
    pil = input("Masukkan Pilihan anda (1-5) : ") 

    # Kondisi saat memilih Nomor 1 untuk melihat daftar suatu buku dengan memilih sesuai genre
    if pil == '1':
        print('\nDaftar Genre Buku')
        print('1. Novel')
        print('2. Romansa')
        print('3. Biografi')
        print('4. Motivasi')
        print('5. Horror')
        print('6. Drama')

        genre = input("Masukkan Pilihan anda (1-6) : ")

        # Output dari pilihan daftar genre buku yang diinginkan 
        if genre == '1':
            print("\nJudul-judul Buku Novel:")
            for i in range(len(Novel)) :
                print(f"{i+1}. {Novel[i]}")
                
        elif genre == '2':
            print("\nJudul-judul Buku Romansa :")
            for i in range(len(Romansa)) :
                print(f"{i+1}. {Romansa[i]}")
                
        elif genre == '3':
            print("\nJudul-judul Buku Biografi :")
            for i in range(len(Biografi)) :
                print(f"{i+1}. {Biografi[i]}")
                
        elif genre == '4':
            print("\nJudul-judul Buku Motivasi :")
            for i in range(len(Motivasi)) :
                print(f"{i+1}. {Motivasi[i]}")
                
        elif genre == '5':
            print("\nJudul-judul Buku Horror :")
            for i in range(len(Horror)) :
                print(f"{i+1}. {Horror[i]}")
                
        elif genre == '6':
            print("\nJudul-judul Buku Drama :")
            for i in range(len(Drama)) :
                print(f"{i+1}. {Drama[i]}")

        else:
            print('Input anda tidak valid, silakan ulang!')
            
    # Kondisi saat memilih Nomor 2 untuk mencari suatu buku
    elif pil == '2':
        cari = input("Masukkan Buku yang anda cari : ")
        if cari in daftarBuku:
            print("Buku", cari, "ada")
        else:
            print("Maaf, Buku yang anda cari belum tersedia")

    # Kondisi saat memilih Nomor 3 untuk meminjanm Buku
    elif pil == '3':
        pinjam = input("Input nama buku yang ingin dipinjam : ") 
        # Mengecek kondisi apakah buku yang ingin dipinjam sudah dipinjam orang lain atau belum
        if pinjam in daftarBuku:
            if pinjam in pinjaman:
                print("Maaf, buku ini sudah dipinjam orang lain.") # Kondisi dimana Buku sudah dipinjam orang lain
            else: # Kondisi jika buku belum dipinjam orang lain akan lanjut ke form peminjaman
                print("Masukkan Data Peminjaman")
                nama = input("Masukkan Nama anda : ")
                nim = input("Masukkan NIM anda : ") 
                hari = input("Masukkan tanggal (dd): ")
                bulan = input("Masukkan bulan (mm): ")
                tahun = input("Masukkan tahun (yyyy): ")

                tanggal = hari + ' ' + bulan + ' ' + tahun # Variabel untuk menampung tanggal peminjaman buku

                # Exception Handling (Kondisi untuk menangani jika terjadi hal yang tak terduga pada program)
                try:
                    # Code untuk Mengonversi string tanggal menjadi objek datetime
                    datetime_object = datetime.strptime(tanggal, "%d %m %Y")
                    # Code untuk menambahkan 7 hari dari tanggal peminjaman yang menunjukkan tanggal pengembalian
                    tanggal_pengembalian = datetime_object + timedelta(days=7) 
                    pinjaman[pinjam] = tanggal_pengembalian  # Simpan tanggal pengembalian
                    print("Selamat", nama,"(", nim, ("),"), "Buku", pinjam, "berhasil dipinjam pada", datetime_object.strftime("%d-%m-%Y"))
                    print("Tanggal pengembalian adalah", tanggal_pengembalian.strftime("%d-%m-%Y"))
                    print("Terima Kasih sudah meminjam buku!")

                # Code untuk menangani situasi di mana format tanggal yang dimasukkan tidak sesuai dengan yang diharapkan.
                except ValueError:
                    print("Tanggal yang Anda masukkan tidak valid.")
        else:
            print("Maaf, Buku yang anda ingin pinjam tidak tersedia")
    
    # Kondisi saat memilih Nomor 4 untuk mengembalikan Buku
    elif pil == '4':
        kembali = input("Input nama Buku yang ingin dikembalikan : ")
        if kembali in daftarBuku:
            if kembali in pinjaman:
                print("Masukkan Tanggal Pengembalian")
                hari = input("Masukkan tanggal (dd): ")
                bulan = input("Masukkan bulan (mm): ")
                tahun = input("Masukkan tahun (yyyy): ")

                # Variabel untuk menampung tanggal peminjaman buku
                tanggal_kembali = hari + ' ' + bulan + ' ' + tahun 

                # Exception Handling (Kondisi untuk menangani jika terjadi hal yang tak terduga pada program)
                try:
                    # Code untuk Mengonversi string tanggal menjadi objek datetime
                    tanggal_kembali_object = datetime.strptime(tanggal_kembali, "%d %m %Y") 
                    # Code ini untuk mengambil tanggal pengembalian dari variabel pinjaman berdasarkan judul buku yang dikembalikan.
                    tanggal_pengembalian = pinjaman[kembali] 

                    # Kondisi saat buku dikembalikan terlambat atau tidak 
                    # Jika buku telat dikembalikan maka akan akan dikenakan denda 2 ribu per hari
                    if tanggal_kembali_object > tanggal_pengembalian:  
                        terlambat = (tanggal_kembali_object - tanggal_pengembalian).days
                        denda = terlambat * 2000
                        print("Anda terlambat mengembalikan buku selama", terlambat, "hari.")
                        print("Denda yang harus dibayar adalah Rp", denda)
                    else:
                        print("Buku dikembalikan tepat waktu.") # Kondisi saat buku tepat waktu dikembalikan 
                    
                    del pinjaman[kembali]  # Hapus data pinjaman setelah pengembalian

                # Code untuk menangani situasi di mana format tanggal yang dimasukkan tidak sesuai dengan yang diharapkan.
                except ValueError:
                    print("Tanggal yang Anda masukkan tidak valid.")
            else:
                print("Buku ini tidak sedang dipinjam.")
        else:
            print("Maaf, Buku yang anda ingin kembalikan tidak tersedia")

    # Kondisi saat memilih Nomor 5 untuk keluar dari program
    elif pil == '5':
        break

    # Kondisi saat input yang diinputkan salah dan akan mengulang program yang dijalankan
    else:
        print("Pilihan tidak valid, silakan coba lagi.")