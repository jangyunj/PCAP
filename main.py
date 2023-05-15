#FALSY: (), [], '', {}, 0

print(not('false'))     #False = String is truthy
print(not(0))           #True = 0 is falsy
print(not(''))          #True = Empty sequence is falsy
print(not(' '))         #False = String is truthy
print(not(['Python']))  #False = String is truthy
print(not([]))          #True = Empty sequence is falsy

