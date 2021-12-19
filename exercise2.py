list = ["pizza", "loukoumades", "melomakarona", "kourampiedes", "tzatziki", "paidakia"]
symbols = "".join(list)


a_counter = 0
e_counter = 0
i_counter = 0
o_counter = 0
u_counter = 0

for x in symbols:
 if x == 'a':
   a_counter = a_counter +1

 if x == 'e':
   e_counter = e_counter +1

 if x == 'i':
   i_counter = i_counter +1

 if x == 'o':
   o_counter = o_counter +1

 if x=='u':
   u_counter = u_counter +1

print('The letter a appears:', a_counter, 'times')
print('The letter e appears:', e_counter, 'times')
print('The letter i appears:', i_counter, 'times')
print('The letter o appears:', o_counter, 'times')
print('The letter u appears:', u_counter, 'times')
