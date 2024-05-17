text = "Ahoj svete, ucime se Python!"

# print(text.split(" "))

# print(text.split(","))

text_split = text.split()

seznam = []
for i in text_split:
    i_s_hvezdickou = i + "***"
    seznam.append(i_s_hvezdickou)
    print(i_s_hvezdickou)

print(seznam)
