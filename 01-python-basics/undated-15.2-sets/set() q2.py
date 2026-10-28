codes = {101, 102, 103, 104}

removed_code = codes.pop()
print(removed_code)

if 999 in codes:
    codes.remove(999)

codes.discard(999)

print(codes)
