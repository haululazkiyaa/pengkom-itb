# menyimpan inputan user kedalam variabel
a = int(input("Masukkan A: "))
b = int(input("Masukkan B: "))

# menyimpan seluruh bilangan prima yang didapatkan dalam bentuk array
bilPrima = []

# melakukan perulangan dengan interval a-b
for num in range(a, b + 1):
    # mengecek apakah nilai angka lebih dari satu (satu bukan bilangan prima, maka harus lebih dari satu)
    if num > 1:
        # kode dibawah untuk ngecek nilai satu satu apakah bil. prima atau bukan.
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            bilPrima.append(num)

# memberikan output yang berbeda
if num > 1:
    print(f"Banyaknya bilangan prima pada selang [{a},{b}] adalah {len(bilPrima)}. Bilangan prima terbesar di selang tersebut adalah {max(bilPrima)}.")
else:
    print(f"Tidak ditentukan bilangan prima pada selang [{a},{b}].")
