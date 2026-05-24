import data_pusat
import fitur_survivor
import fitur_eksplorasi
import fitur_log
import fitur_camp

# SURVIVAL COLONY SIMULATOR
# Tugas Akhir Praktikum Algoritma Pemrograman dan Struktur Data
# MAIN PROGRAM
def main():

    while True:

        print("\n===========================================")
        print("         SURVIVAL COLONY SIMULATOR")
        print("===========================================")
        print(f"Hari       : {data_pusat.hari}")
        print(f"Level Camp : {data_pusat.camp_level}")
        print("===========================================")
        print("\n📌 MENU SURVIVOR")
        print("[1]  Tambah Survivor")
        print("[2]  Tampilkan Survivor")
        print("[3]  Cari Survivor")
        print("[4]  Urutkan Survivor")
        print("[5]  Hapus Survivor")
        print("\n📌 MENU RESOURCE")
        print("[6]  Tampilkan Sumber Daya")
        print("\n📌 MENU EVENT")
        print("[7]  Beri Makanan")
        print("[8]  Perbaiki Camp")
        print("[9]  Sembuhkan Survivor")
        print("\n📌 MENU CAMP")
        print("[10] Info Upgrade Camp")
        print("[11] Upgrade Camp")
        print("\n📌 MENU EKSPLORASI")
        print("[12] Eksplorasi Area")
        print("\n📌 MENU WAKTU & EVENT")
        print("[13] Hari Berikutnya")
        print("\n📌 MENU LOG & STRUKTUR DATA")
        print("[14] Tampilkan Log Single Linked List")
        print("[15] Tampilkan Double Linked List Forward")
        print("[16] Tampilkan Double Linked List Backward")
        print("[17] Tampilkan Giliran Survivor")
        print("[18] Traversal Area Rekursif")
        print("\n📌 MENU SAVE / LOAD")
        print("[19] Simpan Game")
        print("[20] Load Game")
        print("[21] Keluar")
        print("===========================================")

        choice = input("Pilih Menu: ")

        if choice == "1":
            fitur_survivor.add_survivor()

        elif choice == "2":
            fitur_survivor.view_survivors()

        elif choice == "3":
            fitur_survivor.search_survivor()

        elif choice == "4":
            fitur_survivor.sort_survivors()

        elif choice == "5":
            fitur_survivor.delete_survivor()

        elif choice == "6":
            fitur_camp.show_resources()

        elif choice == "7":
            fitur_camp.eat_food()

        elif choice == "8":
            fitur_camp.repair_camp()

        elif choice == "9":
            fitur_camp.heal_survivor()
        
        elif choice == "10":
            fitur_camp.show_upgrade_info()

        elif choice == "11":    
            fitur_camp.upgrade_camp()

        elif choice == "12":
            fitur_eksplorasi.explore_area()

        elif choice == "13":
            fitur_camp.next_day()

        elif choice == "14":
            fitur_log.show_single_log()

        elif choice == "15":
            fitur_log.show_double_forward()

        elif choice == "16":
            fitur_log.show_double_backward()

        elif choice == "17":
            fitur_log.show_circular_survivor()
        
        elif choice == "18":
            fitur_eksplorasi.recursive_area()

        elif choice == "19":
            fitur_camp.save_game()

        elif choice == "20":
            fitur_camp.load_game()

        elif choice == "21":
            print("\nProgram selesai")
            break

        else:
            print("\nMenu tidak valid")


# Menjalankan program
if __name__ == "__main__":
    main()
