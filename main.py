import csv
import os

print ("SELAMAT DATANG DI PARIWISATA KAMI ")
kota=['1.wisata','2.biodata','3.Jadwal','4.harga_tiket','5.kembali']
database_file='wisata.csv'
database_file1='biodata.csv'
database_file2='jadwal.csv'
database_file3='harga_tiket'
wisata=[]
biodata=[]
jadwal=[]
harga_tiket=[]

print('\t'.join(kota))
aksi = input("Pilihan: ")
os.system("clear")
if aksi=='1':

    with open(database_file, mode='a') as db_file:
      csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      while True:
        nama_kota = input('Masukkan nama Kota: ')
        if nama_kota=='=':
          break
        nama_wisata = input('Masukkan nama wisata: ')
        csv_writer.writerow([nama_kota,nama_wisata])
        wisata.append([nama_kota, nama_wisata])
        os.system("clear")

elif aksi=='2':
    with open(database_file1, mode='a') as db_file:
      csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      while True:
        nama_lengkap = input('Masukkan nama lengkap : ')
        if nama_lengkap=='=':
          break
        tanggal_lahir = input('Masukkan tanggal/tahun/bulan : ')
        usia=input("Usia anda :")
        gaji=input(" gaji anda :")
        NIk=input("Masukkan NIK anda : ")
        pekerjaan=input("Masukkan pekerjaan anda : ")
        csv_writer.writerow([nama_lengkap,tanggal_lahir,usia,gaji,NIk,pekerjaan])
        biodata.append([nama_lengkap,tanggal_lahir,usia,gaji,NIk,pekerjaan])
        os.system("clear")

elif aksi=='3':
    with open(database_file2, mode='a') as db_file:
      csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      while True:     
        hari = input('Masukkan hari : ')
        if nama_lengkap=='=':
          break
        jam = input('Masukkan jam : ')           
        csv_writer.writerow([hari,jam])
        jadwal.append([hari,jam])
        os.system("clear")

elif aksi=='4':
    with open(database_file3, mode='a') as db_file:
      csv_writer = csv.writer(db_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      while True:     
        harga_anak = input('Masukkan hari : ')
        if harga_anak=='=':
          break
        harga_remaja = input('Masukkan jam : ')   
        harga_dewasa=()        
        csv_writer.writerow([harga_anak,harga_remaja,harga_dewasa])
        jadwal.append([harga_anak,harga_remaja,harga_dewasa])
        os.system("clear")


else :
  print('salah input')   
  


  