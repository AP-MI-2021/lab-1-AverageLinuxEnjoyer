'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False

    return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst: list) -> int:
    product = 1
    for item in lst:
        product*=item

    return product
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    if y == 0:
        return x
    else:
        return get_cmmdc_v1(y, x % y)
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    return get_cmmdc_v2(abs(x-y), min(x, y)) if (x-y) else y
  
  
def main():
    
    #cerinta 1
    x = int(input("Introduceti un intreg pentru a verifica daca este prim:"))
    if is_prime(x):
        print(f"{x} este prim.")
    else:
        print(f"{x} nu este prim.")
  
    #cerinta 2
    lst = []
    n = int(input("Introduceti numarul de numere din lista:"))
    for i in range(n):
        x = int(input("Introduceti nr:"))
        lst.append(x)
  
    #cerinta 3
    print(f"Produsul numerelor din lista este {get_product(lst)}")

    x = int(input("Introduceti primul numar pentru CMMDC:"))
    y = int(input("Introduceti al doilea numar pentru CMMDC:"))
    print(f"CMMDC dintre {x} si {y} e {get_cmmdc_v1(x,y)}")

  

if __name__ == '__main__':
    main()
