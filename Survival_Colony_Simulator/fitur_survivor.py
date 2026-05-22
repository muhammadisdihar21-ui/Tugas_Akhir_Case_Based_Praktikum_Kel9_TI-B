import data_pusat
from komponen_game import Survivor
import fitur_log

# MENAMBAHKAN SURVIVOR
def add_survivor():
    nama = input("Masukkan nama survivor: ").strip()

    if not nama:
        print("\nNama tidak boleh kosong")
        return
        
    if len(nama) > 18:
        print("\nNama terlalu panjang! Maks 18 karakter")
        return
        
    for s in data_pusat.survivors:
        if s.nama.lower() == nama.lower():
            print("\nNama survivor sudah ada")
            return
            
    survivor = Survivor(nama)

    data_pusat.survivors.append(survivor)

    # Menambahkan survivor ke circular linked list
    fitur_log.add_circular_survivor(survivor)

    # Menambahkan log
    fitur_log.add_single_log(f"{nama} bergabung ke koloni")
    fitur_log.add_double_log(f"{nama} bergabung ke koloni")

    print("\nSurvivor berhasil ditambahkan")

# MENAMPILKAN SURVIVOR
def view_survivors():
    if not data_pusat.survivors:
        print("\nBelum ada Survivor")
        return

    print("\n============= DAFTAR SURVIVOR =============")

    for i, s in enumerate(data_pusat.survivors, start=1):
        status = " [SAKIT]" if s.nama.lower() in data_pusat.sick_survivors else ""
        print(f"{i}. {s.nama}{status}")
        print(f"   Energi : {s.energi}")
        print(f"   Level  : {s.level}")
        print("-------------------------------------------")

# SEARCHING SURVIVOR
def search_survivor():
    keyword = input("Masukkan nama survivor: ").lower()

    found = False

    for s in data_pusat.survivors:
        if s.nama.lower() == keyword:
            print("\n=========== SURVIVOR DITEMUKAN ============")
            print(f"Nama   : {s.nama}")
            print(f"Energi : {s.energi}")
            print(f"Level  : {s.level}")
            print("===========================================")
            found = True

    if not found:
        print("\nSurvivor tidak ditemukan")

# SORTING SURVIVOR
def sort_survivors():

    if not data_pusat.survivors:
        print("\nBelum ada survivor")
        return

    print("1. Urutkan berdasarkan Energi")
    print("2. Urutkan berdasarkan Level")

    choice = input("Pilih: ")

    if choice == "1":
        sorted_list = sorted(
            data_pusat.survivors,
            key=lambda x: x.energi,
            reverse=True
        )
        kategori = "ENERGI"

    elif choice == "2":
        sorted_list = sorted(
            data_pusat.survivors,
            key=lambda x: x.level,
            reverse=True
        )
        kategori = "LEVEL "

    else:
        print("\nPilihan tidak valid")
        return

    print(f"\n==== DATA SURVIVOR BERDASARKAN {kategori} =====")
    print("-------------------------------------------")
    print(f"{'No':<5}{'Nama':<20}{'Energi':^10}{'Level':^12}")
    print("-------------------------------------------")

    for i, s in enumerate(sorted_list, start=1):
        print(f"{str(i) + '.':<5}{s.nama:<20}{str(s.energi):^10}{str(s.level):^12}")

    print("-------------------------------------------")

# MENGHAPUS SURVIVOR
def delete_survivor():
    nama = input("Masukkan nama survivor: ")

    for s in data_pusat.survivors:
        if s.nama.lower() == nama.lower():
            data_pusat.survivors.remove(s)
            data_pusat.sick_survivors.pop(s.nama.lower(), None)

            data_pusat.circular_head = None
            for surv in data_pusat.survivors:
                fitur_log.add_circular_survivor(surv)

            fitur_log.add_single_log(f"{nama} dihapus")
            fitur_log.add_double_log(f"{nama} dihapus")

            print("\nSurvivor berhasil dihapus")
            return

    print("\nSurvivor tidak ditemukan")