import phonenumbers
from phonenumbers import geocoder, carrier

print("=======================================")
print("=       TOOL CEK PROVIDER NOMOR HP     =")
print("=======================================\n")

while True:
    Nomor_Telpon = input("Masukan nomor HP (ketik 'exit' untuk keluar) >> ")

    if Nomor_Telpon.lower() == "exit":
        print("Program selesai.")
        break

    if Nomor_Telpon.strip() == "":
        print("Nomor tidak boleh kosong!\n")
        continue

    try:
        # Parse nomor Indonesia
        parsed = phonenumbers.parse(Nomor_Telpon, "ID")

        # Cek provider
        provider = carrier.name_for_number(parsed, "id")

        # Cek lokasi umum (hanya asal nomor, BUKAN lokasi pengguna)
        lokasi = geocoder.description_for_number(parsed, "id")

        print("\n====================================")
        print(f"Nomor Telpon : {Nomor_Telpon}")
        print(f"Provider     : {provider if provider else 'Tidak diketahui'}")
        print(f"Area Nomor   : {lokasi if lokasi else 'Tidak diketahui'}")
        print("====================================\n")

    except Exception as e:
        print("Nomor tidak valid! Coba lagi.\n")