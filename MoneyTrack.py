import csv

filename = 'finance.csv'
temp_data = []

# Membaca data dari file CSV ke dalam list
with open(filename, mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['nominal'] = float(row['nominal'])
        temp_data.append(row)

# Menyimpan list ke dalam file CSV
def savedat():
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['id', 'tanggal', 'kategori', 'nominal']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in temp_data:
            writer.writerow(item)

# Menambahkan transaksi baru
def adds_data():
    no_transaksi = str(len(temp_data) + 1)
    tanggal = input("Masukkan Tanggal (DD/MM/YYYY): ")
    kategori = input("Masukkan kategori (Pemasukan/Pengeluaran): ")

    try:
        nominal = float(input("Nominal: "))
    except ValueError:
        print("Nominal tidak valid, input dibatalkan.")
        return

    data = {
        'id': no_transaksi,
        'tanggal': tanggal,
        'kategori': kategori,
        'nominal': nominal
    }
    temp_data.append(data)
    savedat()
    print("Data berhasil ditambahkan.\n")

# Menampilkan seluruh transaksi
def all_data():
    if not temp_data:
        print("Data Kosong!")
        return
    print("\n===== Daftar Mutasi Keuangan =====")
    for item in temp_data:
        print(f"{item['id']}. [{item['tanggal']}] {item['kategori'].capitalize()} - Rp{item['nominal']:.2f}")
    print("===================================\n")

# Menghapus transaksi berdasarkan ID
def hapus_data():
    id_hapus = input("Masukkan ID yang ingin dihapus: ")
    for i, item in enumerate(temp_data):
        if item['id'] == id_hapus:
            temp_data.pop(i)
            savedat()
            print("Data berhasil dihapus.\n")
            return
    print("ID tidak ditemukan.\n")

# Mengedit transaksi berdasarkan ID
def editdat():
    id_edit = input("Masukkan ID yang ingin diedit: ")
    for item in temp_data:
        if item['id'] == id_edit:
            item['tanggal'] = input(f"Tanggal baru ({item['tanggal']}): ") or item['tanggal']
            item['kategori'] = input(f"Kategori baru ({item['kategori']}): ") or item['kategori']
            nominal_baru = input(f"Nominal baru ({item['nominal']}): ")
            if nominal_baru:
                try:
                    item['nominal'] = float(nominal_baru)
                except ValueError:
                    print("Nominal tidak valid, tidak diubah.")
            savedat()
            print("Data berhasil diperbarui.\n")
            return
    print("ID tidak ditemukan.\n")

# Menampilkan laporan keuangan
def laporan_keuangan():
    pemasukan = sum(item['nominal'] for item in temp_data if item['kategori'].lower() == 'pemasukan')
    pengeluaran = sum(item['nominal'] for item in temp_data if item['kategori'].lower() == 'pengeluaran')
    saldo = pemasukan - pengeluaran

    print("\n===== Laporan Keuangan =====")
    print(f"Total Pemasukan   : Rp{pemasukan:,.2f}")
    print(f"Total Pengeluaran : Rp{pengeluaran:,.2f}")
    print(f"Saldo Akhir       : Rp{saldo:,.2f}")
    print("============================\n")

# Menu utama
def menu():
    while True:
        print("\n======MoneyTrack: Sistem Pelacak Pemasukan dan Pengeluaran Pribadi===== ")
        print("1. Tambah Pemasukan/Pengeluaran")
        print("2. Hapus Mutasi")
        print("3. Update Data")
        print("4. Tampilkan Mutasi")
        print("5. Laporan Keuangan")
        print("6. Keluar")
        pil = input("Pilih Menu: ")

        if pil == '1':
            adds_data()
        elif pil == '2':
            hapus_data()
        elif pil == '3':
            editdat()
        elif pil == '4':
            all_data()
        elif pil == '5':
            laporan_keuangan()
        elif pil == '6':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Menu tidak valid!")

# Jalankan aplikasi
menu()