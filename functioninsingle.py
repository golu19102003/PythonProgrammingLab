def nearly_equal(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        differences = sum(1 for i in range(len(str1)) if str1[i] != str2[i])
        return differences == 1
    
   
    if len(str1) > len(str2):
        str1, str2 = str2, str1 
    i = j = 0
    differences = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            differences += 1
            j += 1  
        else:
            i += 1
            j += 1
        if differences > 1:
            return False
    
    return True
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if nearly_equal(str1, str2):
    print("Strings are nearly equal.")
else:
    print("Strings are not nearly equal.")
