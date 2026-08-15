# =================================================================
# FUNGSI & FORMATTING
# =================================================================

# Membuat fungsi untuk membungkus logika pencetakan output
def print_trip_summary(destination, country, days, budget, currency, travel_month):
    # Menggunakan f-strings agar tampilan rapi, terstruktur, dan mudah dibaca
    print("=======================")
    print("KelanaAI")
    print("=======================")
    print(f"Destination : {destination}")
    print(f"Country     : {country}")
    print(f"Days        : {days}")
    # Menampilkan budget tanpa angka desimal (.0) agar sama persis seperti contoh
    print(f"Budget      : {int(budget)} {currency}") 
    print(f"Currency    : {currency}")
    print(f"Travel Month: {travel_month}")


# =================================================================
# INPUT INTERAKTIF (BAGIAN UTAMA)
# =================================================================

# Minta input dari pengguna untuk masing-masing variabel
destination = input("Masukkan Destination: ")
country = input("Masukkan Country: ")

# Minta input 'days' dan pastikan melakukan konversi tipe data ke int()
days = int(input("Masukkan Days (Angka): "))

# Minta input 'budget' dan pastikan melakukan konversi tipe data ke float()
budget = float(input("Masukkan Budget (Angka): "))

currency = input("Masukkan Currency: ")
travel_month = input("Masukkan Travel Month: ")

# Memanggil fungsi yang sudah dibuat di atas untuk menampilkan hasilnya
print("\n💻 Contoh Tampilan Output")
print_trip_summary(destination, country, days, budget, currency, travel_month)