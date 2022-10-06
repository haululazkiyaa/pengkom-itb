# buat simpen nilai
dataNilai = []
mahasiswaLulus = []
mahasiswaTidakLulus = []

# bikin input berapa mahasiswanya
n = int(input("Masukan jumlah mahasiswa:"))

# bikin perulangan sebanyak n mahasiswa
while len(dataNilai) + 1 <= n:
    # bikin input untuk nilai setiap mahasiswa
    nilai = input("Masukan nilai mahasiswa:").upper()
    # simpan setiap nilainya
    dataNilai.append(nilai)

for i, value in enumerate(dataNilai):
    if value == "A" or value == "B" or value == "C" or value == "D":
        mahasiswaLulus.append(value)
    if value == "E" or value == "F":
        mahasiswaTidakLulus.append(value)

print("Lulus =", len(mahasiswaLulus))
print("Tidak lulus =", len(mahasiswaTidakLulus))