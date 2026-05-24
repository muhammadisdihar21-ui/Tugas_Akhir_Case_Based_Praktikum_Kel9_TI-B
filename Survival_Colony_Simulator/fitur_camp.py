import json
import random
import data_pusat
import fitur_survivor
import fitur_log
from komponen_game import Survivor

# MENAMPILKAN RESOURCE
def show_resources():
    print("\n=========== SUMBER DAYA KOLONI ============")

    for key, value in data_pusat.sumber_daya.items():
        print(f"{key:<10}: {value}")

    print("===========================================")

# MAKANAN
# Fungsi untuk memberikan makanan kepada survivor
def eat_food():
    if not data_pusat.survivors:
        print("\nBelum ada survivor")
        return
        
    fitur_survivor.view_survivors()

    try:
        index = int(input("Pilih survivor: ")) - 1
        if index < 0 or index >= len(data_pusat.survivors):
            print("\nNomor survivor tidak valid")
            return
        survivor = data_pusat.survivors[index]
    except ValueError:
        print("\nInput harus berupa angka")
        return
        
    # Survivor yang sakit tidak bisa makan
    if survivor.nama.lower() in data_pusat.sick_survivors:
        print(f"\n{survivor.nama} sedang sakit!")
        print("Tidak bisa diberi makan sebelum disembuhkan")
        return
        
    try:
        amount = int(input("Jumlah makanan: "))
    except:
        print("\nInput tidak valid")
        return
        
    if amount <= 0:
        print("\nJumlah makanan harus lebih dari 0")
        return
        
    if data_pusat.sumber_daya["Makanan"] < amount:
        print("\nMakanan tidak cukup")
        return
        
    data_pusat.sumber_daya["Makanan"] -= amount
    survivor.energi += amount * 10

    if survivor.energi > 100:
        survivor.energi = 100
        
    print(f"\n{survivor.nama} mendapatkan + {amount * 10} energi")
    
# REPAIR CAMP
# Fungsi untuk memperbaiki camp
def repair_camp():
    if not data_pusat.camp_damaged:
        print("\nCamp tidak rusak")
        return
        
    repair_cost = 5

    if data_pusat.sumber_daya["Material"] < repair_cost:
        print("\nMaterial tidak cukup")
        return
        
    data_pusat.sumber_daya["Material"] -= repair_cost
    data_pusat.camp_damaged = False
    print("\nCamp berhasil diperbaiki")

# HEAL SURVIVOR
# Fungsi mengobati survivor yang sakit
def heal_survivor():
    if not data_pusat.sick_survivors:
        print("\nTidak ada survivor yang sakit")
        return
        
    print("\n============= SURVIVOR SAKIT ==============")

    for name in data_pusat.sick_survivors:
        print("-", name)

    print("===========================================")

    name = input("Masukkan nama survivor: ").strip().lower()

    if not name:
        print("\nInput tidak boleh kosong")
        return

    survivor_exists = any(s.nama.lower() == name for s in data_pusat.survivors)

    if not survivor_exists:
        print("\nSurvivor ini tidak ada dalam koloni")
        return

    if name not in data_pusat.sick_survivors:
        print("\nSurvivor ini tidak sedang sakit")
        return
        
    medicine_cost = 10

    if data_pusat.sumber_daya["Obat"] < medicine_cost:
        print("\nObat tidak cukup")
        return
        
    data_pusat.sumber_daya["Obat"] -= medicine_cost
    del data_pusat.sick_survivors[name]

    for s in data_pusat.survivors:
        if s.nama.lower() == name:
            s.energi = 10
            break
        
    print(f"\n{name} berhasil sembuh")
    print("Energi rendah, beri makanan untuk menambah energi")
    
# INFO UPGRADE
def show_upgrade_info():

    next_level = data_pusat.camp_level + 1

    print("\n============ INFO UPGRADE CAMP ============")
    print(f"Level Camp Saat Ini: {data_pusat.camp_level}")

    if next_level > 5:
        print("Camp sudah level maksimum (Lv5)")
        print("===========================================")
        return

    print(f"\nUntuk Upgrade ke Level {next_level}:")

    if next_level == 2:
        print("- 20 Makanan")
        print("- 20 Material")
        print("- 5 Obat")
        print("- Minimal 1 survivor level 10")

    elif next_level == 3:
        print("- 30 Makanan")
        print("- 30 Material")
        print("- 10 Obat")
        print("- Minimal 1 survivor level 20")

    elif next_level == 4:
        print("- 40 Makanan")
        print("- 40 Material")
        print("- 20 Obat")
        print("- Minimal 2 survivor level 30")

    elif next_level == 5:
        print("- 80 Makanan")
        print("- 80 Material")
        print("- 50 Obat")
        print("- Minimal 1 survivor level 100")

    print("===========================================")

# CEK UPGRADE
def check_upgrade():

    next_level = data_pusat.camp_level + 1

    if next_level > 5:
        print("\nCamp sudah level maksimum")
        return False

    kurang = []

    # RESOURCE CHECK
    if next_level == 2:
        if data_pusat.sumber_daya["Makanan"] < 20:
            kurang.append("Makanan kurang (butuh 20)")
        if data_pusat.sumber_daya["Material"] < 20:
            kurang.append("Material kurang (butuh 20)")
        if data_pusat.sumber_daya["Obat"] < 5:
            kurang.append("Obat kurang (butuh 5)")
        if sum(1 for s in data_pusat.survivors if s.level >= 10) < 1:
            kurang.append("Butuh 1 survivor level 10")

    elif next_level == 3:
        if data_pusat.sumber_daya["Makanan"] < 30:
            kurang.append("Makanan kurang (butuh 30)")
        if data_pusat.sumber_daya["Material"] < 30:
            kurang.append("Material kurang (butuh 30)")
        if data_pusat.sumber_daya["Obat"] < 10:
            kurang.append("Obat kurang (butuh 10)")
        if sum(1 for s in data_pusat.survivors if s.level >= 20) < 1:
            kurang.append("Butuh 1 survivor level 20")

    elif next_level == 4:
        if data_pusat.sumber_daya["Makanan"] < 40:
            kurang.append("Makanan kurang (butuh 40)")
        if data_pusat.sumber_daya["Material"] < 40:
            kurang.append("Material kurang (butuh 40)")
        if data_pusat.sumber_daya["Obat"] < 20:
            kurang.append("Obat kurang (butuh 20)")
        if sum(1 for s in data_pusat.survivors if s.level >= 30) < 2:
            kurang.append("Butuh 2 survivor level 30")

    elif next_level == 5:
        if data_pusat.sumber_daya["Makanan"] < 80:
            kurang.append("Makanan kurang (butuh 80)")
        if data_pusat.sumber_daya["Material"] < 80:
            kurang.append("Material kurang (butuh 80)")
        if data_pusat.sumber_daya["Obat"] < 50:
            kurang.append("Obat kurang (butuh 50)")
        if sum(1 for s in data_pusat.survivors if s.level >= 100) < 1:
            kurang.append("Butuh 1 survivor level 100")

    if kurang:
        print("\n❌ Tidak bisa upgrade! Syarat belum terpenuhi:")
        for k in kurang:
            print("-", k)
        return False

    return True

# UPGRADE CAMP
def upgrade_camp():

    next_level = data_pusat.camp_level + 1

    print(f"\nMencoba upgrade ke Level {next_level}...")

    if not check_upgrade():
        return

    # KURANG RESOURCE
    if next_level == 2:
        data_pusat.sumber_daya["Makanan"] -= 20
        data_pusat.sumber_daya["Material"] -= 20
        data_pusat.sumber_daya["Obat"] -= 5

    elif next_level == 3:
        data_pusat.sumber_daya["Makanan"] -= 30
        data_pusat.sumber_daya["Material"] -= 30
        data_pusat.sumber_daya["Obat"] -= 10

    elif next_level == 4:
        data_pusat.sumber_daya["Makanan"] -= 40
        data_pusat.sumber_daya["Material"] -= 40
        data_pusat.sumber_daya["Obat"] -= 20

    elif next_level == 5:
        data_pusat.sumber_daya["Makanan"] -= 80
        data_pusat.sumber_daya["Material"] -= 80
        data_pusat.sumber_daya["Obat"] -= 50

    data_pusat.camp_level = next_level

    print(f"\nCamp berhasil upgrade ke Level {next_level}!")

# SISTEM PERGANTIAN HARI   
def next_day():

    # Ketika event camp rusak muncul maka next_day = block
    if data_pusat.camp_damaged:
        print("\nCamp rusak, tidak bisa mengganti hari")
        print("Perbaiki camp terlebih dahulu")
        return
        
    if data_pusat.sick_survivors:
        print("\n💀 KORBAN PENYAKIT HARI INI:")

        dead = []

        for s in data_pusat.survivors:
            if s.nama.lower() in data_pusat.sick_survivors:
                print(f"- {s.nama} meninggal karena tidak segera diobati")
                dead.append(s)

        for s in dead:
            data_pusat.survivors.remove(s)

        data_pusat.sick_survivors.clear() 
       
    data_pusat.hari += 1

    # Reset eksplor cost
    data_pusat.explore_count = 0

    # Istirahat
    for s in data_pusat.survivors:
        if s.energi > 0 and s.nama.lower() not in data_pusat.sick_survivors:
            rest_energy = 50

            if data_pusat.camp_level >= 2:
                rest_energy = 70

            s.energi += rest_energy
            if s.energi > 100:
                s.energi = 100

    print(f"\n================= HARI {data_pusat.hari} ==================")

    # EVENT NORMAL
    events = [
        "Menemukan makanan tambahan",
        "Survivor sakit",
        "Camp rusak",
        "Menemukan peti logistik",
        "Tidak terjadi apa-apa"
    ]

    if data_pusat.camp_level >= 3:
        events.extend([
            "Tidak terjadi apa-apa",
            "Menemukan makanan tambahan"
        ])

    event = random.choice(events)

    print("\nEvent Hari Ini:", event)

    # Event makanan
    if event == "Menemukan makanan tambahan":
        data_pusat.sumber_daya["Makanan"] += 2
        print("\n+2 makanan")
            
    # Event sakit    
    elif event == "Survivor sakit" and data_pusat.survivors:
        if data_pusat.survivors:
            jumlah_sakit = random.randint(1, len(data_pusat.survivors))
            sick_list = random.sample(data_pusat.survivors, jumlah_sakit)
            print("\n💀 WABAH PENYAKIT MELANDA!")

            for sick in sick_list:
                sick.energi = 0
                data_pusat.sick_survivors[sick.nama.lower()] = True
                print(f"- {sick.nama} jatuh sakit (energi drop ke 0)")

    # Event camp rusak
    elif event == "Camp rusak":
        data_pusat.camp_damaged = True
        print("\nCamp rusak!")
        print("Camp harus diperbaiki")

    # Event peti logistik
    elif event == "Menemukan peti logistik":
        data_pusat.sumber_daya["Makanan"] += 5
        data_pusat.sumber_daya["Material"] += 10
        data_pusat.sumber_daya["Obat"] += 2
        print("\n📦 Jackpot! Menemukan peti persediaan militer kuno.")
        print("+5 Makanan, +10 Material, +2 Obat didapatkan")

    print("\n===========================================")

    fitur_log.add_single_log(f"Hari {data_pusat.hari}: {event}")
    fitur_log.add_double_log(f"Hari {data_pusat.hari}: {event}")

        
    

# SAVE GAME
def save_game():

    data = {
        "hari": data_pusat.hari,
        "sumber_daya": data_pusat.sumber_daya,
        "camp_damaged": data_pusat.camp_damaged,
        "camp_level": data_pusat.camp_level,
        "sick_survivors": data_pusat.sick_survivors,
        "survivors": [s.to_dict() for s in data_pusat.survivors]
    }

    with open("save_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nGame berhasil disimpan")

# LOAD GAME
def load_game():

    try:
        with open("save_data.json", "r") as file:
            data = json.load(file)

        data_pusat.hari = data["hari"]
        data_pusat.sumber_daya = data["sumber_daya"]
        data_pusat.camp_damaged = data.get("camp_damaged", False)
        data_pusat.camp_level = data.get("camp_level", 1)
        data_pusat.sick_survivors = data.get("sick_survivors", {})

        data_pusat.survivors.clear()
        data_pusat.circular_head = None

        for s in data["survivors"]:
            survivor = Survivor(
                s["nama"],
                s["energi"],
                s["level"]
            )

            data_pusat.survivors.append(survivor)
            fitur_log.add_circular_survivor(survivor)

        print("\nGame berhasil dimuat")

    except FileNotFoundError:
        print("\nSave data tidak ditemukan")