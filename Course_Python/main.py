flat_number = 20


entrance_number = (flat_number - 1) // 20 + 1
floor_number = (flat_number - 1) % 20 // 4 + 1
print(entrance_number)
print(floor_number)