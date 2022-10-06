a = int(input("Nilai pertama:"))
b = int(input("Nilai kedua:"))
c = int(input("Nilai ketiga:"))

bilangan = [a, b, c]

for i in sorted(bilangan):
  print(i, end=" ")