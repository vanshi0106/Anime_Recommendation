# num=int(input("enter a number :"))
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#       print('prime')





# for i in range(1,6):       
#     for j in range(1,i+1):
#         print(i,end='')                                                                                                                                                             1
#     print()




# for i in range(1,6):
#     for j in range(i-1,5):
#         print(" ",end='')
#     for j in range(i):
#            print('*',end='')
#     print()




# for i in range(1,5):
#      for j in range(i):
#            print('*',end='')
#      print()
# for i in range(5,0):
#     for j in range(i):
#             print('*',end='')
#     print()








# for i in range(1,6):
#     for j in range(i-1,5):
#         print('*',end='')
#     print()
# for i in range(1,6):
#     for j in range(i+1,5):
#         print('*',end='')
#     print()





num=input('enter your number:')
length=len(num)
new_num=0
for i in num:
    new_num += int(i)**length
if int(num)== new_num:
    print('armstrong number.')
else:
    print('number is not armstrong.')

