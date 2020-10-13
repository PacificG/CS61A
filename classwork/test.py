scores = [219, 240, 209, 227, 254, 174, 276, 181, 221, 252, 196, 261, 210, 216, 224, 244, 227, 187, 281, 204, 224, 189, 252, 250, 247, 240, 173, 188, 198, 210]

print('A: ',len([n for n in scores if n/3 >= 85]))
print('B: ',len([n for n in scores if n/3 < 85 and n/3 >= 70]))
print('C: ',len([n for n in scores if n/3 < 70 and n/3 >= 60]))
print('D: ',len([n for n in scores if n/3 < 60]))