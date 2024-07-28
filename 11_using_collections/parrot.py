text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

 # The first index printed refers to the index of the substring
 # between the 21st and 35th indices of the whole string.
 
 # The second index is in relation to the full string.
