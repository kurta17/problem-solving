def is_polindrom(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_polindrom(s[1:-1])
    
print(is_polindrom("giorgi"))
print(is_polindrom("giooig"))



    
