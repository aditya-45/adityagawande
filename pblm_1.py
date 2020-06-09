for i in range(int(input())):
    n = int(input())
    j = 1
    k = n-1
    if n%2==0:
        for i in range(1,n//2+1):
            if i%2!=0:
                for i in range(k):
                    print("%",end="")
                for i in range(j):
                    print("#",end="")
                j += 1
                k -= 1
                print()
            else:
                for i in range(j):
                    print("#",end="")
                for i in range(k):
                    print("%",end="")
                j += 1
                k -= 1
                print()
        for i in range(n//2+1,n+1):
            if i%2!=0:
                for i in range(k+1):
                    print("%",end="")
                for i in range(j-1):
                    print("#",end="")
                k += 1
                j -= 1
                print()
            else:
                for i in range(j-1):
                    print("#",end="")
                for i in range(k+1):
                    print("%",end="")
                k += 1
                j -= 1
                print()
    else:
        for i in range(1,n//2+1):
            if i%2!=0:
                for i in range(k):
                    print("%",end="")
                for i in range(j):
                    print("#",end="")
                j += 1
                k -= 1
                print()
            else:
                for i in range(j):
                    print("#",end="")
                for i in range(k):
                    print("%",end="")
                j += 1
                k -= 1
                print()
        if (n//2+1)%2!=0:
            for i in range(n//2):
                print("%",end="")
            for i in range(n//2,n):
                print("#",end="")
            print()
        else:
            for i in range(n//2+1):
                print("#",end="")
            for i in range(n//2+1,n):
                print("%",end="")
            print()
        for i in range(n//2+2,n+1):
            if i%2!=0:
                for i in range(k+1):
                    print("%",end="")
                for i in range(j-1):
                    print("#",end="")
                k += 1
                j -= 1
                print()
            else:
                for i in range(j-1):
                    print("#",end="")
                for i in range(k+1):
                    print("%",end="")
                k += 1
                j -= 1
                print()
