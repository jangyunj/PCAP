var1 = "Tom"
string1 = "Variable is %s" % var1    #placeholder with a string, then fill it with the variable
print(string1)

var2 = 3
string2 = "Variable is %d" % var2
print(string2)

var3 = 3.14159
string3 = "Variable is %f" % var3     #default is 6 digits
print(string3)

var4 = 1.23456
string4 = "Variable is %.2f" % var4   #.2 = 2 digits AFTER the decimal point
print(string4)

var5 = 1.23456789
string5 = "Variable is {}".format(var5)  #placeholder is {} 
print(string5)

var6 = 1.2345678910
string6 = "Variable is {:.2f}".format(var6) #2 digits AFTER decimal
print(string6)

string7 = "Variable is {:.2f} and {}".format(var5, var6)
print(string7)

#---NEWEST WAY IS F(ORMATTED) STRING---
string8 = f"Variable is {var5} and {var6}"
print(string8)

string9 = f"Variable is {var5*2} and {var6*3}"  #Evaluated at runtime --variables can also be manipulated
print(string9)

string10 = f"Variable is {var1*10}"
print(string10)