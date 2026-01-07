import csv
import os

FILE = "Kendaraan.csv"


def init_csv():
    if not os.path.exists(FILE):
        with open(FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["kode", "jenis", "nama", "harga", "status"])
            writer.writerow(["MTR01", "motor", "Beat", "70000", "Tersedia"])
            writer.writerow(["MTR02", "motor", "Vario", "90000", "Tersedia"])
            writer.writerow(["MBL01", "mobil", "Avanza", "300000", "Tersedia"])
            writer.writerow(["MBL02", "mobil", "Xenia", "280000", "Tersedia"])


def load_data():
    data = []
    with open(FILE, mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def save_data(data):
    with open(FILE, mode="w", newline="") as f:
        fieldnames = ["kode", "jenis", "nama", "harga", "status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def menu():
    print("=" * 45)
    print("      RENTAL MOTOR & MOBIL")
    print("=" * 45)
    print("1. Lihat Kendaraan")
    print("2. Sewa Kendaraan")
    print("3. Kembalikan Kendaraan")
    print("4. Keluar")
    print("=" * 45)


def tampil():
    data = load_data()

    if len(data) == 0:
        print("Data kendaraan kosong!")
        return

    print("\nDAFTAR KENDARAAN")
    print("-" * 60)
    print("Kode | Jenis | Nama    | Harga     | Status")
    print("-" * 60)
    for d in data:
        print(
            d["kode"], "|",
            d["jenis"], "|",
            d["nama"], "| Rp",
            d["harga"], "|",
            d["status"]
        )


def sewa():
    data = load_data()
    kode = input("Masukkan kode kendaraan: ").upper()

    for d in data:
        if d["kode"] == kode:
            if d["status"] == "Tersedia":
                hari = int(input("Lama sewa (hari): "))
                total = hari * int(d["harga"])
                d["status"] = "Disewa"
                save_data(data)
                print("Total bayar: Rp", total)
                return
            else:
                print("Kendaraan sedang disewa!")
                return

    print("Kode kendaraan tidak ditemukan!")

def kembali():
    data = load_data()
    kode = input("Masukkan kode kendaraan: ").upper()

    for d in data:
        if d["kode"] == kode:
            if d["status"] == "Disewa":
                d["status"] = "Tersedia"
                save_data(data)
                print("Kendaraan berhasil dikembalikan")
                return
            else:
                print("Kendaraan belum disewa!")
                return

    print("Kode kendaraan tidak ditemukan!")


init_csv()

while True:
    menu()
    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        tampil()
    elif pilih == "2":
        sewa()
    elif pilih == "3":
        kembali()
    elif pilih == "4":
        print("Terima kasih!")
        break
    else:
        print("Menu tidak valid!")

    input("\nTekan ENTER untuk lanjut...")
    os.system("cls" if os.name == "nt" else "clear")