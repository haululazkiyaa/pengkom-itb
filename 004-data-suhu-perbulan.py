n = int(input("Masukan jumlah hari dalam sebulan:"))

dataSuhu = []

while len(dataSuhu) + 1 <= n:
    suhu = int(input("Masukan suhu hari ke-" + str(len(dataSuhu) + 1) + ':'))
    dataSuhu.append(suhu)

average = sum(dataSuhu) / len(dataSuhu)

print("Suhu rata-rata:", round(average, 2))
print("Suhu tertinggi:", max(dataSuhu))
print("Suhu terendah:", min(dataSuhu))
