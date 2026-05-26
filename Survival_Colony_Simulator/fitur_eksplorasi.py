
import random
import data_pusat
import fitur_survivor
import fitur_log

# REKURSIF
# Traversal area
def recursive_area(current_area="Camp", visited=None):

    if visited is None:
        visited = set()

    print(current_area)

    visited.add(current_area)

    for next_area in data_pusat.area_graph[current_area]:
        if next_area not in visited:
            recursive_area(next_area, visited)

# # EXPLORE AREA
# EXPLORE AREA
def explore_area():

    if not data_pusat.survivors:
        print("\nBelum ada survivor")
        return

    fitur_survivor.view_survivors()

    try:
        index = int(input("Pilih survivor: ")) - 1
        survivor = data_pusat.survivors[index]
    except:
        print("\nInput tidak valid")
        return

    # 🔥 ENERGI BERDASARKAN EXPLORE HARI INI (RESET TIAP HARI)
    required_energy = (data_pusat.explore_count + 1) * 10
    if required_energy > 100:
        required_energy = 100

    print(f"\nEnergi yang dibutuhkan: {required_energy}")

    key = survivor.nama.lower()

    # 💀 MATI KARENA SAKIT
    if key in data_pusat.sick_survivors:
        print(f"\n💀 {survivor.nama} mati karena sakit")
        data_pusat.survivors.remove(survivor)
        data_pusat.sick_survivors.pop(key, None)
        return

    # 💀 MATI KARENA ENERGI
    if survivor.energi <= 0 or survivor.energi < required_energy:
        print(f"\n💀 {survivor.nama} mati karena energi tidak cukup")
        data_pusat.survivors.remove(survivor)
        data_pusat.sick_survivors.pop(key, None)
        return

    print("\n============== AREA TERSEDIA ==============")
    for area in data_pusat.data_area:
        print("-", area)
    print("===========================================")

    area_name = input("Pilih area: ").title()

    if area_name not in data_pusat.data_area:
        print("\nArea tidak ditemukan")
        return

    area = data_pusat.data_area[area_name]

    # 📌 Tracking eksplorasi
    data_pusat.queue_eksplorasi.append(survivor.nama)
    data_pusat.stack_eksplorasi.append(area.nama)
    data_pusat.area_dikunjungi.add(area.nama)

    # 🎲 Random resource
    found_resource = random.choice(area.sumber_daya)

    base_random = random.randint(1, 7)
    bonus_level = (survivor.level // 10) * 2

    base_amount = base_random + bonus_level

    bonus_camp = 0

    if data_pusat.camp_level >= 4:
        bonus_camp = 5


    amount = base_amount + bonus_camp
    data_pusat.sumber_daya[found_resource] += amount

    # 🔥 LEVEL SYSTEM FIX
    survivor.exp += 1

    # 🔥 RUMUS YANG SUDAH BENAR
    need_exp = (survivor.level // 10) + 1

    if survivor.exp >= need_exp:
        survivor.level += 1
        survivor.exp = 0
        print(f"Level Up! Sekarang level {survivor.level}")
    else:
        print(f"Progress Level: {survivor.exp}/{need_exp}")

    # 🔥 KURANGI ENERGI
    survivor.energi -= required_energy

    # 🔥 TAMBAH JUMLAH EXPLORE HARI INI
    data_pusat.explore_count += 1

    # 📝 LOG
    fitur_log.add_single_log(f"{survivor.nama} mengeksplor {area.nama}")
    fitur_log.add_double_log(f"{survivor.nama} mengeksplor {area.nama}")

    # 📊 HASIL
    print("\n============ HASIL EKSPLORASI =============")
    print(f"Survivor    : {survivor.nama}")
    print(f"Area        : {area.nama}")
    if bonus_camp > 0:
        print(f"Mendapat    : +{base_amount} {found_resource}")
        print(f"Bonus Camp  : +{bonus_camp} {found_resource}")
        print(f"Total       : +{amount} {found_resource}")
    else:
        print(f"Mendapat    : +{amount} {found_resource}")
    print(f"Energi      : -{required_energy}")
    print(f"Sisa Energi : {survivor.energi}")
    print(f"Level Up    : Level {survivor.level}")
    print("===========================================")
# def explore_area():

#     if not data_pusat.survivors:
#         print("\nBelum ada survivor")
#         return
        
#     required_energy = (data_pusat.explore_count + 1) * 10

#     if required_energy > 100:
#         required_energy = 100

#     print(f"\nEnergi yang dibutuhkan: {required_energy}")

#     fitur_survivor.view_survivors()

#     try:
#         index = int(input("Pilih survivor: ")) - 1
#         survivor = data_pusat.survivors[index]
#     except:
#         print("\nInput tidak valid")
#         return
        
#     # DIPAKSA EKSPLOR SAAT SAKIT = MATI
#     key = survivor.nama.lower()

#     if key in data_pusat.sick_survivors:
#         print(f"\n{survivor.nama} sedang sakit!")
#         print(f"{survivor.nama} dipaksa eksplorasi...")
#         print(f"💀 {survivor.nama} mati di perjalanan karena sakit")

#         data_pusat.survivors.remove(survivor)

#         data_pusat.sick_survivors.pop(key, None)

#         return

#     # ENERGI 0 = MATI
#     if survivor.energi <= 0:

#         print(f"\n{survivor.nama} memiliki energi 0")
#         print(f"{survivor.nama} dipaksa eksplorasi...")
#         print(f"💀 {survivor.nama} mati")
#         print("❌ Hasil eksplorasi NIHIL")

#         data_pusat.survivors.remove(survivor)

#         data_pusat.sick_survivors.pop(key, None)

#         return

#     # ENERGI KURANG = MATI
#     if survivor.energi < required_energy:

#         print(f"\nEnergi {survivor.nama} tidak cukup")
#         print(f"{survivor.nama} tetap mencoba eksplorasi...")
#         print(f"💀 {survivor.nama} mati karena energi tidak cukup")
#         print("❌ Hasil eksplorasi NIHIL")

#         data_pusat.survivors.remove(survivor)

#         data_pusat.sick_survivors.pop(key, None)

#         return

#     print("\n============== AREA TERSEDIA ==============")

#     for area in data_pusat.data_area:
#         print("-", area)

#     print("===========================================")

#     area_name = input("Pilih area: ").title()

#     if area_name not in data_pusat.data_area:
#         print("\nArea tidak ditemukan")
#         return

#     area = data_pusat.data_area[area_name]

#     # Queue
#     data_pusat.queue_eksplorasi.append(survivor.nama)

#     # Stack
#     data_pusat.stack_eksplorasi.append(area.nama)

#     # Set
#     data_pusat.area_dikunjungi.add(area.nama)

#     # Random resource
#     found_resource = random.choice(area.sumber_daya)

#     # Pengaruh level terhadap hasil eksplorasi
#     # HASIL DASAR
#     base_amount = random.randint(1, 3) + survivor.level

#     # BONUS TIAP LEVEL 10
#     bonus_level = survivor.level // 10

#     bonus_camp = 0

#     # BONUS CAMP LEVEL 4
#     if data_pusat.camp_level >= 4:
#         bonus_camp = 5

#     amount = base_amount + bonus_level + bonus_camp

#     data_pusat.sumber_daya[found_resource] += amount

#     # TAMBAHKAN EXP
#     survivor.exp += 1

#     # HITUNG KEBUTUHAN EXP BERDASARKAN LEVEL
#     need_exp = (survivor.level // 10) + 1

#     if survivor.exp >= need_exp:
#         survivor.level += 1
#         survivor.exp = 0
#         print(f"Level Up! Sekarang level {survivor.level}")

#     # Menambahkan log
#     fitur_log.add_single_log(f"{survivor.nama} mengeksplor {area.nama}")
#     fitur_log.add_double_log(f"{survivor.nama} mengeksplor {area.nama}")

#     print("\n============ HASIL EKSPLORASI =============")
#     print(f"Survivor    : {survivor.nama}")
#     print(f"Area        : {area.nama}")
#     if bonus_level > 0 or bonus_camp > 0:
#         print(f"Mendapat    : {base_amount} {found_resource}")
            
#         if bonus_level > 0:
#             print(f"Bonus Level : +{bonus_level} {found_resource}")

#         if bonus_camp > 0:
#             print(f"Bonus Camp  : +{bonus_camp} {found_resource}")

#         print(f"Total       : +{amount} {found_resource}")

#     else:
#         print(f"Mendapat    : +{amount} {found_resource}")
#     print(f"Energi      : -{required_energy}")
#     print(f"Sisa Energi : {survivor.energi}")
#     print(f"Level Up    : Level {survivor.level}")
#     print("===========================================")