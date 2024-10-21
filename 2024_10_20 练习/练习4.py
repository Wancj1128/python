def is_prime(n):
    if n <= 3:
        return n > 1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_huiwen(n):
    n = int(n)
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def wjj_main():
    huiwen_prime = []
    a = 1
    while len(huiwen_prime) < 100:
        if is_prime(a) and is_huiwen(a) == True:
            huiwen_prime.append(a)
            a+=1
        else:
            a+=1
    for i in range(100):
        i = 1
        if i%10 ==0:
            huiwen_prime.insert(i-1,'\n')
            i+=1
        else:
            i+=1
    print(huiwen_prime)
    f = 0
    while f < len(huiwen_prime):
        if (f + 1) % 10 == 0:
            print(huiwen_prime[f], end='\n')
            f += 1
        else:
            print(huiwen_prime[f], end=' ')
            f += 1

n = 131
print(is_prime(n))
print(is_huiwen(n))
wjj_main()
