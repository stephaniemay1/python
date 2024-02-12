print("Grades Calculator")

maths = int(input("maths: "))
eng = int(input("eng: "))
phy = int(input("phy: "))
kisw = int(input("kisw: "))
histo = int(input("histo: "))


total = maths + eng + phy + kisw + histo

avg = total/5
print(avg)

if avg>=71 and avg<=100:
    print("A")
elif avg>=61 and avg<=70:
    print("B")
elif avg>=51 and avg<=60:
    print("C")
elif avg>=50 and avg<=40:
    print("D")
elif avg>=0 and avg<=39:
    print("E")
else:
    print("invalid")



