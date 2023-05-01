string = input(str())

lower_case = sum(1 for char in string if char.islower())
upper_case = sum(1 for char in string if char.isupper())

print(f"count of lower cases - {lower_case}; count of upper cases - {upper_case}")
