# i=0
# while i<10:
#     i+=1
#     if i==6 or i==8:
#      continue
#     print(i)

string = "navgurukul"

counter = 0
# string = "navgurukul"
while (counter < len(string)):
    counter += 1
    if string[counter] == "a":
        continue
    if string[counter] == "u":
        continue
    print(string[counter])
print("The end", string[counter])


