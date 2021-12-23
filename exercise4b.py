list = ["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzatziki", "paidakia"]

symbols = "".join(list)


dct = {}

for i in symbols:
    if i in dct:
        dct[i] +=1
    else:
        dct[i] =1

print("a:",dct.get('a'),"e:", dct.get('e'),"i:", dct.get('i'), "o:", dct.get('o'), "u:",dct.get('u'))
