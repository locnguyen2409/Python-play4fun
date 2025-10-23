def unique_numbers(numbers_list):
    unique_list = set(numbers_list)
    return unique_list

numbers_list = [0,8,1,9,7,3,0,6,0,0]
unique = unique_numbers(numbers_list)
print("Unique numbers: ",unique)
print("Count of unique numbers:" ,len(unique))