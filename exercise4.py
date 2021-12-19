list = ["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzatziki", "paidakia"]

symbols = "".join(list)


print(symbols)

dct = {}

for i in symbols:
    if i in dct:
        dct[i] +=1
    else:
        dct[i] =1

print(dct)
