# menyimpan inputan user kedalam variabel
n = int(input("N: "))
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

# melakukan perluangan sampai N kali
for i in range(n):
    # karena dalam pemrogramman nilai dimulai dari nol maka kita harus menambahkan satu dari nilai i
    i += 1
    # melakukan pengecekan menggunakan metode if
    # 1. cek apabila i habis dibagi a (i adalah kelipatan a) maka print "Siap"
    if i % a == 0:
        print("Siap", end = "")
    # 2. cek apabila i habis dibagi b (i adalah kelipatan b) maka print "Bang"
    if i % b == 0:
        print("Bang", end = "")
    # 3. cek apabila i habis dibagi c (i adalah kelipatan c) maka print "Jago"
    if i % c == 0:
        print("Jago", end = "")
    # 4. membuat spasi apabila salahsatu kondisi diatas terpenuhi (jika i adalah kelipatan a atau b atau c maka berikan spasi)
    if i % a == 0 or i % b == 0 or i % c == 0:
        print(" ", end = "")
    # 5. mengeluarkan nilai i ditambah spasi apabila semua kondisi tidak terpenuhi
    if i % a != 0 and i % b != 0 and i % c != 0:
        print(i, end = " ")

# keterangan end = "" berfungsi agar metode print ditampilkan dalam satu baris ditambah string yang diinginkan