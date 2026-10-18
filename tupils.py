stuDetails=('Surabhi', 89)

#Packing
address = ('227', 'Brickfield Sheltors', 'Banglore', 'Karnataka', '562107')#

for x in address:
    print  (x, end = ' ')


#Unpacking
houseno, apartName, city, state, pin = address

print()
print('HNO', houseno)
print('APT NO ', apartName)
print(city)
print(state)
print(pin)

#A tuple can also be created without using parentheses
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1,2,3))

#nested index
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4