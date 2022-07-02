def find_nos(n =9, k =3):
    main = []
    max_digit = n -(k-1)
    
    if k ==1:
        return [[n]]
    for i in range(1, max_digit+1):
        curr =i
        comb = find_nos(n = n-i, k = k-1)
        for lst in comb:
            lst.append(curr)
        main.extend(comb)
    return main

print(find_nos())