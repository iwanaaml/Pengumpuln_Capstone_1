japan_tourist_spot = [
                        {'spot': 'Tokyo Tower', 'region': 'Tokyo', 'price': 122400},
                        {'spot': 'Tokyo Skytree', 'region': 'Tokyo', 'price': 214200},
                        {'spot': 'Senso-ji', 'region': 'Tokyo', 'price': 0},
                        {'spot': 'Fushimi Inari', 'region': 'Kyoto', 'price': 0},
                        {'spot': 'Bamboo Grove', 'region': 'Kyoto', 'price' : 0},
                        {'spot': 'Kiyomizu-dera', 'region': 'Kyoto', 'price': 40800},
                        {'spot': 'Osaka Castle', 'region': 'Osaka', 'price': 61200},
                        {'spot': 'Dotonbori', 'region': 'Osaka', 'price': 0},
                        {'spot': 'Universal Studio', 'region': 'Osaka', 'price': 836400}
]
cart = []


def menampilkan_MenuJelajah():
    while True:
        pilihanMenuJelajah = input('''
                        Sub Menu Jelajah Atraksi
                        1.  Jelajahi Semua Atraksi Wisata
                        2.  Cari Spot Atraksi
                        3.  Kembali ke Menu Utama
                    Masukkan Pilihan Menu sesuai kebutuhan Anda:        
                                                                    ''')
        
        if pilihanMenuJelajah=='1':
            print('\nPilihan Atraksi Wisata\n')
            print(f'{60*"="}\n| Nomor |Atraksi Wisata\t| Kota\t| Harga Tiket (IDR)| \n{60*"="}') 
            nomor = 1
            for val in japan_tourist_spot:
                print(f'''| {nomor}\t| {val['spot']}\t| {val['region']}\t| {val['price']}\t| ''')
                nomor += 1
            print(f'{60*"="}')
        elif pilihanMenuJelajah=='2':
            user_input_spot = input('Masukkan nama atraksi: ').title()
            user_input_region = input('Masukkan nama wilayah: ').title()

            found = False
            for val in japan_tourist_spot:
                print(val)
                if val['spot'].title() == user_input_spot and val['region'].title() == user_input_region:
                    print(f"Atraksi ditemukan: {val['spot']} di {val['region']} dengan harga {val['price']} IDR.")
                    found = True
                    break
            else:
                print(f'{user_input_spot} belum terdaftar, silahkan ke menu "Menambah Atraksi Wisata Baru"')
        else:
            main_menu()

def menambah_atraksi():
    while True:
        pilihanMenuTambah = input('''
                        Sub Menu Tambah Atraksi
                        1.  Tambah Atraksi Wisata
                        2.  Kembali ke Menu Utama
                    Masukkan Pilihan Menu sesuai kebutuhan Anda:        
                                                            ''')
        if pilihanMenuTambah =='1':
            print('Menambahkan Atraksi Wisata Baru\n')
            spot_name = input('Masukkan tempat atraksi yang ingin ditambahkan: ')
            region = input('Masukkan wilayah atraksi wisata: ')
            harga_tiket = int(input('Masukkan harga tiket(IDR): '))
            confirm_save = input(f"\nApakah Anda ingin menyimpan data berikut? (y/n):\n"
                f"Nama Atraksi: {spot_name}\n"
                f"Wilayah: {region}\n"
                f"Harga Tiket: {harga_tiket} IDR\nPilihan Anda: ").lower()

            if confirm_save == 'y':
                duplicate = False
                for val in japan_tourist_spot:
                    if val['spot'].lower() == spot_name.lower() and val['region'].lower() == region.lower():
                        duplicate = True
                        break
            
                if duplicate:
                    print(f'Data "{spot_name}" di wilayah "{region}" sudah tersedia pada "Tabel Atraksi Wisata".')
                else:
                    japan_tourist_spot.append({'spot': spot_name, 'region': region, 'price': harga_tiket})
                    print(f'\nAtraksi "{spot_name}"-"{region}" berhasil ditambahkan!\n')
                    print('Pilihan Atraksi Wisata\n')
                    print(f'{60*"="}\n| Nomor\t| Atraksi Wisata\t| Kota\t| Harga Tiket (IDR)| \n{60*"="}') 
                    nomor = 1
                    for val in japan_tourist_spot:
                        print(f'''| {nomor}\t| {val['spot']}\t| {val['region']}\t| {val['price']}\t| ''') 
                        nomor += 1
                        print(f'{60*"="}')
        else:
            main_menu()

def menghapus_atraksi():
    while True:
        pilihanMenuHapus = input('''
                        Sub Menu Hapus Atraksi
                        1.  Hapus Atraksi Wisata
                        2.  Kembali ke Menu Utama
                    Masukkan Pilihan Menu sesuai kebutuhan Anda:        
                                                            ''')
        if pilihanMenuHapus == '1':
            print('\nPilihan Atraksi Wisata')
            print(f'{60*"="}\n| Nomor\t| Atraksi Wisata\t| Kota\t| Harga Tiket (IDR)\t| \n{60*"="}') 
            nomor = 1
            for val in japan_tourist_spot:
                print(f'''| {nomor}\t| {val['spot']}\t| {val['region']}\t| {val['price']}\t| ''')
                nomor += 1
            print(f'{60*"="}')
            
            del_spot = input('Masukkan nama atraksi wisata yang ingin dihapus: ')
            del_region = input('Masukkan wilayah atraksi wisata tersebut: ')

            found = False
            for val in japan_tourist_spot:
                if val['spot'].lower() == del_spot.lower() and val['region'].lower() == del_region.lower():
                    print(f"\nAtraksi wisata yang ingin Anda hapus adalah:\n{60*'='}\n"
                        f"| {val['spot']}\t| {val['region']}\t| {val['price']} IDR |\n{60*'='}")
                    validasi = input('Apakah Anda yakin ingin menghapus atraksi wisata ini? (y/n): ').lower()

                    if validasi == 'y':
                        japan_tourist_spot.remove(val)  
                        print(f'\nAtraksi "{del_spot}" di "{del_region}" berhasil dihapus.')
                    else:
                        print('\nData batal dihapus.')
                    found = True
                    break 
                
        else:
            main_menu()

def menu_beli():
   while True:
        pilihanMenuBeli = input(''' 
                        Sub Menu Beli Atraksi Wisata:
                        1. Beli Atraksi Wisata
                        2. Kembali ke Menu Utama
                    Masukkan Pilihan Menu sesuai kebutuhan Anda:        
                ''')

        if pilihanMenuBeli == '1':
            while True:    
                print('\nPilihan Atraksi Wisata\n')
                print(f'{60*"="}\n| Nomor | Atraksi Wisata\t| Kota\t| Harga Tiket (IDR) |\n{60*"="}') 
                nomor = 1
                for val in japan_tourist_spot:
                    print(f'| {nomor}\t| {val["spot"]}\t| {val["region"]}\t| {val["price"]}\t|')
                    nomor += 1
                print(f'{60*"="}')

                del_spot = input("Masukkan nama atraksi wisata yang ingin dibeli: ").strip()
                del_region = input("Masukkan wilayah atraksi wisata tersebut: ").strip()

                selected_item = None
                for val in japan_tourist_spot:
                    if val['spot'].lower() == del_spot.lower() and val['region'].lower() == del_region.lower():
                        selected_item = val
                        break

                if selected_item:
                    jumlah_tiket = int(input("Masukkan jumlah tiket yang dibutuhkan: "))
                    cart.append({
                        'spot': selected_item['spot'],
                        'region': selected_item['region'],
                        'qty': jumlah_tiket,
                        'price': selected_item['price'] * jumlah_tiket
                    })

                    print('\nIsi Cart') 
                    print(f'{60*"="}')
                    print('| No | Atraksi Wisata\t| Kota\t| Jumlah\t| Total Harga\t|') 
                    print(f'{60*"="}')
                    total = 0
                    nomor = 1
                    for item in cart:
                        print(f"| {nomor}\t| {item['spot']}\t| {item['region']}\t| {item['qty']}\t| {item['price']} IDR |")
                        nomor += 1
                        total += item['price']
                    print(f'{60*"="}')
                    print(f'Total : {total} IDR')
                    
                else:
                    print("\nAtraksi wisata tidak ditemukan, silakan coba lagi.")
                    continue

                beli_lagi = input('Mau beli lagi? (y/n): ').lower()
                if beli_lagi == 'y':
                    continue 
                elif beli_lagi == 'n':
                    break
                else: 
                    print('Invalid Input !!!')

            if total == 0:
                print("Transaksi Anda gratis, tidak perlu bayar!")
                break
            else:
                uang_masuk = int(input('Masukkan jumlah uang: ')) 
                if uang_masuk < total: 
                    print(f'''
                        Transaksi Anda dibatalkan
                        uangnya kurang sebesar {total - uang_masuk}
                    ''')
                elif uang_masuk == total: 
                    print('Terima kasih') 
                    break
                else: 
                    print(f'''
                        Terima kasih
                        Uang kembalian Anda : {uang_masuk - total}
                    ''')    
                    break

        elif pilihanMenuBeli == '2':
            break
        else:
            print('Pilihan tidak valid, silakan pilih 1 atau 2.')

def menampilkan_isi_cart():
    print('\nIsi Cart') 
    print(f'{60*"="}')
    print('| No | Atraksi Wisata\t| Kota\t| Jumlah\t| Total Harga\t|') 
    print(f'{60*"="}')
    total = 0
    nomor = 1
    for item in cart:
        print(f"| {nomor}\t| {item['spot']}\t| {item['region']}\t| {item['qty']}\t| {item['price']} IDR |")
        nomor += 1
        total += item['price']
    print(f'{60*"="}')
    print(f'Total : {total} IDR')

def main_menu():


    while True:
        pilihanMenu = input('''
                                                Selamat Datang di Japan Wanderlust!
                            
                                Silahkan pilih opsi di bawah ini untuk memulai perjalananmu:
                            
                                1.  Jelajahi Atraksi Wisata
                                2.  Menambah Atraksi Wisata Baru
                                3.  Menghapus Atraksi Wisata
                                4.  Membeli Tiket Atraksi Wisata
                                5.  Keluar dari menu           
                            
                            Masukkan Pilihan Menu sesuai kebutuhan Anda:        
        ''')

        if pilihanMenu == '1':
            menampilkan_MenuJelajah()
    
        elif pilihanMenu == '2':
            menambah_atraksi()

        elif pilihanMenu == '3':
            menghapus_atraksi() 
        elif pilihanMenu == '4':
            menu_beli()
        elif pilihanMenu == '5': 
            print('Keluar dari program')
            break 
        else:
            print('Invalid Input !!!')
    
                

main_menu()



