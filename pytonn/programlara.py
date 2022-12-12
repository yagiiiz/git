
#a=1
#if(a==5):
#    print("a beşe eşittir")
#elif(a>5):
#    print("a beşten büyük")
#else:
#    print("a beşten küçük")
yildiz=5
for(i=1;i<=yildiz;++i):
    for(j=1;j<=i;j++):
        if(i+j<=yildiz+1):
            print("*")
        else:
            print(" ")
        