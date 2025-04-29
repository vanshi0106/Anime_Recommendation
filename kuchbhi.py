'''
length=10
breadth=5
result=2*(length+breadth)
print("area of rectangle is : ",result)


a=10
b=20
c=a
a=b
b=c
print(a,b)



a=int(input("enter a number :"))
b=int(input("enter a number :"))
a=a+b
b=a-b
a=a-b
print(a,b)


a=10
b=20
a,b=b,a
print(a,b)


text="vanshika"
print((type)text)

text='vanshika'
print(text[0])


text='vanshika mahajan'
last_index=len(text)-1
print(last_index)


text='vanshika mahajan'
last_index=len(text)-1
print(text[last_index])

text='vanhika'
print(text[-1])

text='vanshika mahajan'
#[start,end,step]
print(text[9:16])

text='vanshika mahajan'
print(text[-7:-1])

text='vanshika mahajan'
print(text[-7: ])

text='vanshika mahajan'
print(text[ : ])

text='vanshika mahajan'
print(text[0:15:2])

text='vanshika mahajan'
print(text[ : :-2])

msg = "W4hfa35nhdffhsfd sfeJ45dids5 kj4W5tjafg5h46fh" 
print(msg[ 0: 45:4])

text='VaNsHika mAhajan'
#text=text.lower()
#text=text.title()
#text=text.find('a',11)
#text=text.count('a')
#text=text.replace('a','k')
text=text.replace('a','k',12)
print(text)


num1=float(input("enter a number 1 :"))
num2=int(input("enter a number 2 :"))
result=num1+num2
print(result)
print(type(num1),type(num2))


num1=eval(input("enter a number 1 :")) #eval for int and float both can be used
num2=eval(input("enter a number 2 :"))
result=num1+num2
print(result)
print(type(num1),type(num2))

a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=a
a=b
b=c
print(a,b)


first_name='vanshika'
last_name='mahajan'
full_name=first_name + " " +last_name
print(full_name)


first_name='vanshika'
age=19
full_name=f'my name is {first_name} and my age is {age}'            #f' for format to print variable 
print(full_name)


word=str(input("enter a word"))
word=word[0:2].capitalize()+word[2:].capitalize()
print(word)


word1='laptop'
word2='mouse'
word1=word1.replace('la','mo')
word2=word2.replace('mo','la')
print(word1,word2)


word1='laptop'
word2='mouse'
w1first2=word1[0:2]
w2first2=word2[0:2]
word1=word1.replace(w1first2,w2first2)
word2=word2.replace(w2first2,w1first2)
print(word1,word2)


word1='laptop'
word2='mouse'
word1=word1[0:2].replace(word1,word2)
word2=word2[0:2].replace(word2,word1)
print(word1,word2)

### listtttttt


cars=['ford','audi','supra','nano']    # by help of listing duplicaing is also allowed
print(cars[ : :-1])

cars=['ford','audi','supra','nano','ford','audi','supra','nano',[2,4,6,8]] 
print(cars[-1][2])

cars=['ford','nishan','audi','supra','nano'] 
print(cars[1][2:5])

cars=['ford','nishan','audi','supra','nano'] 
cars[-1]='maruti'
print(cars)

cars=['ford','nishan','audi','supra','nano','ford','nishan','audi','supra','nano'] 
#cars.append('maruti')           #for list methods
#cars.pop(1)           #index no is used to rempove specific if index no not given it pop last element in the list
#cars.remove('audi')           #remove m name should be given
#n=cars.count('audi')        #an variable should be initailize
#print(n)
#n=cars.index('nano',4)
#cars.sort()
#cars.insert(2,'maruti')      #insert a element in the list in somewheree
print(cars)

numbers=[3,6,7,5,7,78,854,456]
total=sum(numbers)
print(total)


marks=[
     [34,65,76,87,45,'suman'],
    [34,55,76,87,43,'riya'],
    [67,36,35,87,45,'mohit'],
]
stu1=marks[0]
stu2=marks[1]
stu3=marks[2]

percentage= sum(stu1[0:5])/500*100
percentage2=sum(stu2[0:5])/500*100
percentage3=sum(stu3[0:5])/500*100

print(stu1[-1],percentage)
print(stu2[-1],percentage2)
print(stu3[-1],percentage3)


#method of extend
cars1=['ford','toyota','supra']
cars2=['nishan','maruti','audi']
cars.extend(cars2)



cars = 'ford,nishan,volvo,fortan'
new_list = cars.split(',')               #used to mAKE a list
print(new_list)


cars = ['ford','nishan','volvo','fortan']
cars= ' #'.join(cars)              ## join with hastaq      
print(cars)


cars = ['ford','nishan','volvo','fortan']
cars= ' car name :'.join(cars)              ## join with hastaq      
print(cars)



                  ######### conditional statement
# //  used for float division
#print(7//2)
#print(5**2)       ## ** is used for square root first number is base nd second is power

##### if else 
# syntax   if condition:
#code
#else :
#code


a=int(input("enter a number :"))
if(a%2==0):
    print("even")
else:
    print("odd")



age =10
if age>=18:
    print("you can vote")
else :
    print("you cannot vote")



word=str(input("enter a word : "))
if word==word[ : :-1]:
    print("palindrome")
else :
    print("not palindrome")


age=34
if age>18:
    print("young")
elif  age <7:           ##elif for else if
    print("child")
elif age>7:
    print("teenager")
else:
    print("alien")


units=350
if units<=100:
    print("free")
elif units>200:
    print((units-200)*10+500)
elif units>100:
    print((units-100)*5)



name=str(input("enter a name : "))
bp=float(input("enter a number : "))
pf=0.12*bp

print(pf)

hra=0.20*bp
if hra>=2000:
   hra=2000
  

if bp<300000:
        da=0.20*bp

       
else:
        da=0.30*bp
        print(da)
grosspray=bp+da+hra-pf
print(f"grosspray : {grosspray}" )

netpay=grosspray-pf
print(f"netpay : {netpay}")



########## tuples
cars=('ford','nishan','volvo','honda','toyota')
print(cars)

####tuples cant be changed

cars=('ford','nishan','volvo','honda','toyota')
print(cars[2:])                      #########indexing

######sets
#indexing is not allowed
##duplacing is not there
#directly cant access any value
#with help of method it can access
cars={'ford','nishan','volvo','honda','toyota','ford','nishan','volvo','honda','toyota'}
print(cars)


#methods
cars={'ford','nishan','volvo','honda','toyota'}
#cars.add('nano')
#cars.pop()
#cars.remove('honda')
print(cars)


### to make tuple to list
cars=('ford','nishan','volvo','honda','toyota')
cars=list(cars)
cars.remove('volvo')
print(cars)

cars=('ford','nishan','volvo','honda','toyota','ford','nishan','volvo','honda','toyota')
cars=set(cars)


line='The quick brown fox jumps over the lazy dog'
line=line.lower()
line=line.replace(' ','')
line = set(line)
#line_text=len(line)-1
if line==26:
    print("panagram")
else:
    print("not panagram")
    

a=int(input("enter a number :"))
if a%2==0:
    print("even")
else:
    print("odd")

age=23
if age>18:
    print('young')
else:
    if age>7:
        print("teenager")
    else:
        print("child")
        


year=int(input("enter a year :"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
            print("leap year")
else:
   print("not a leap year")


   ###logical
name=input("enter name :")
password=input("enter a password :")
if name=='vanshi' and password=='123@123':
    print("login")
else:
    print("invalid name and password")



name=input("enter name :")
password=input("enter a password :")
if name=='vanshi' or password=='123@123':
    print("login")
else:
    print("invalid name and password")



name=input("enter name :")
password=input("enter a password :")
if not(name=='vanshi' or password=='123@123'):
    print("login")
else:
    print("invalid name and password")



#progarm to check vowel
word=input("enter a character :")
if word=='a' or word=='e' or word=='i' or word=='o' or word=='u':
    print("vowel")
else:
    print("not vowel")

    #### by using in operator
word=input("enter a character :")
if word in 'aeiou':
    print("vowel")
else:
    print("not vowel")



word=input("enter a word")
word=word.lower()
if len(word)==1:
    if word.isalpha():
        if word in'aeiou':
            print("vowel")
        else:
            print('consonent')
    else:
        print('invalid input')
else:
    print('please enter a single character')
    


word=input("enter a word")
word=word.lower()
if len(word)==1:
    if word.isnumeric():
        print('its a number')
    else:
        if word.isalpha():
            if word in'aeiou':
              print("vowel")
            else:
               print('consonent')
        else:
         print('invalid input')
else:
    print('please enter a single character')




########### program
name=input('enter your name :')
hotel_days=int(input("enter the number to stay :"))
car_days=int(input("enter no of days to rent :"))
city=input('enter destination :')

budget=eval(input('enter budget :'))

hotel_cost=hotel_days*1200
if hotel_days>=6:
    hotel_cost=hotel_cost-1000

    car_cost=car_days*700
if car_cost>=7:
        car_cost=car_cost-800
elif car_cost>=4:
        car_cost=car_cost-500

if city=='goa':
            plane_cost=20000
           
elif city=='ladakh':
             plane_cost=70000
             
elif city=='srilanka':
             plane_cost=80000
            
elif city=='nepal':
            plane_cost=40000
           

total_cost=hotel_cost+car_cost+plane_cost
if total_cost>=budget:
                print(total_cost)
else:
        print("invalid input")
     # print(name)
      #print(hotel_cost)
      #print(car_cost)
      #print(plane_cost)
      #print(total_cost)


######loops(for and while loop)
name=input("enter name :")
password=input("enter a password :")

flag='red'
while  flag=='red':
  if name=='vanshi' and password=='abc':
    print("login")
    flag='green'
  else:
    print("invalid name and password")
    name=input("enter name :")
    password=input("enter a password :")


num1=int(input("enter a num1 :"))
num2=int(input("enter a num2 :"))
flag='num1/num2'
while flag=='numm1/num2':
    if num1==0 or num2==0 or num1==num2==0:
        print("exit")
        flag=='go'
    else:
        print("num1/num2") 
        num1=input("enter a num1 :")
        num2=input("enter a num2 :")


                

# word=input("enter a character :")
# flag='red'
# while flag=='red':
#     if word=='a' or word=='e' or word=='i' or word=='o' or word=='u':
#       print("vowel")
#       flag='go'
#     else:
#       print("not vowel")
#       word=input("enter a character :")





word=input("enter a word")
#word=word.lower()
flag='red'
while flag=='red':
    if len(word)==1:
         if word.isalpha():
             word=word.lower()
             if word in'aeiou':
               print("vowel")
               flag='go'
             else:
                print('consonent')
                word=input("enter a word")
         else:
             print('invalid input')
             word=input("enter a word")
    else:
        print('please enter a single character')
        word=input("enter a word")




#### program for game guess the number

# print('==================== welcome to guess the number ===================')
# print()

# ###random_number=45
# import random    ###module
# random_number=random.randint(1,100)

# user_guess=input("enter your guess : ")
# flag=0
# while flag==0:
#     ### checking if value is number or not
#     if user_guess.isnumeric():
#         ### if number then converting into integer
#           user_guess=int(user_guess)
          
#           if user_guess==random_number:
#             print('======== you won======')
#             flag=1
#           elif user_guess>random_number:
#              print('======== you guess is higher than my number======')
#              user_guess=input("enter your guess : ")
#           elif user_guess<random_number:
           
#               print('======== you guess is lower than my number======')
#               user_guess=input("enter your guess : ")
#     else:
#         print("inavlid input")
#         user_guess=input("enter your guess : ")





counter=int(input("enter the number :"))
a=int(input("enter the number :"))
while counter<=10:
    print(f'{a} x {counter} = {counter *2}')
    counter=counter+1



a=eval(input("enter a number : "))
while a<=30:
    if a%2!=0:
        print(a)
   
    a=a+1




count=1
while count<=100:
    if count%3==0 and count%5==0:
        print("fizbuzzz")
        
    elif count%3==0:
        print("fizz")
       
    elif count%5==0:
        print("buzz")
       
    else:
        print(count)
       
    count=count+1





brands='mi realme iphone samsung oppo vivo lg nokia '.split()
#print(len(brand))
# print(brands[0])
# print(brands[1])
# print(brands[2])
# print(brands[3])
# print(brands[4])
# print(brands[5])
index=0
while index<len(brands):
    print(index)
    index=index+1




brands='mi realme iphone samsung oppo vivo lg nokia '.split()
#print(len(brand))
# print(brands[0])
# print(brands[1])
# print(brands[2])
# print(brands[3])
# print(brands[4])
# print(brands[5])
index=0
while index<len(brands):
    print(brands[index])
    index=index+1



brands='mi realme iphone samsung oppo vivo lg nokia '.split()
brands2='oneplus motorola techno'.split()
#print(len(brand))
# print(brands[0])
# print(brands[1])
# print(brands[2])
# print(brands[3])
# print(brands[4])
# print(brands[5])
index=0
while index<len(brands):
    brands.append(brands2[index])
   
    index=index+1
print(brands)



brands='mi realme iphone samsung oppo vivo lg nokia '.split()
sales=[30000,40000,70000,80000,30000,20000,1200,15000]
index=0
while index<len(brands):
    brands.append(sales[index])
   
    index=index+1
print(f'brands : {brands} ,sales : {sales} ')




marks=[
    [34,67,65,75,75,'Rahul'],
    [34,56,97,97,75,'dupinder'],
    [34,97,65,67,75,'sonia'],
    [34,67,65,34,67,'suman'],
    [0,17,25,35,5,'nobita'],

]
new=[]
i=0
while i<len(marks):
   highestmarks=(marks[i][ :-1])
   name=marks[i][-1]
   percentage=round(sum(highestmarks)/500*100)
   new.append([percentage, name])
   i=i+1
print(new)
'''

###### for loop

# for i in range(10):
#     print(i)

# for i in range(2,10):
#     print(i)



# for i in range(10,50,2):
#     print(i)

# a=int(input("enter the number :"))
# b=int(input("enter number :"))
# for i in range(a,b):
#       if i%2==0:
#         print(i)

# a=int(input("enter the number is :"))
# for i in range(1,11):
#     print(a*1)


# a=int(input("enter the number is :"))

# for i in range(a,10):

#        print(f'{a} x {i} = {a*i}')


# word="hello"
# for i in word:
#     print(i)




# word="hello"
# count=0
# for i in word:
#     count=count+1

# print(count)



# list1=[42,453,63,524,533,42,53]
# for i in list1:
#     print(i)



# list1=[34,"apple",5.5,"banana","cherry",1,4,6,7,"mango"]
# int_list=[]
# float_list=[]
# str_list=[]
# for item in list1:
#     if type(item)==int:
#         int_list.append(item)
#     elif type(item)==float:
#         float_list.append(item)
#     elif type(item)==str:
#         str_list.append(str)
# print(int_list)
# print(float_list)
# print(str_list)



###list2=['apple','kiwi',guava','cherry','pine apple','water melon','grape']




# dictionary=[
#     'name'='vanshika',
#     'age'=19,
#     'course':'b.tech'
# ]

#check whether a number is armstrong is not

# num=input("enter any number :")
# new_num=0
# length=len(num)
# for i in num:
#     new_num+=int(i)**length
#     if   int(num)==new_num:
#         print("armstrong")
#     else:
#        print("not an armstrong" )






# check weather the number is armstrong or not
# 153 ------> 1*3 + 53 + 3*3 = 1 + 125 + 27 --------> 153

# num=input('enter your number:')
# length=len(num)
# new_num=0
# for i in num:
#     new_num += int(i)**length
# if int(num)== new_num:
#     print('armstrong number.')
# else:
#     print('number is not armstrong.')



# list2=['apple','kiwi','guava','cherry','pine apple','water melon','grape']
# for i in list2:
#     if 'p' in i :
#        print(i)




# num=int(input("enter any number :"))
# new_num=0
# length=len(str(num))
# temp=num
# while temp>0:
#    last_digit=temp%10
#    new_num+=last_digit**length
#    temp//=10
# if int(num)== new_num:
#     print('armstrong number.')
# else:
#       print('number is not armstrong.')





# a=int(input("Enter any number: "))
# f=1
# for i in range(a,0,-1):
#     f=f* i
# print(f)





# a=0
# b=1
# series_length=4
# print(a,b,end=' ')
# for i in range(series_length):
#     c = a + b
#     print(c,end=' ')
#     a = b
#     b = c




# fabonacci series by using while loop:-
# num = int(input('enter your number:'))
# num1, num2 = 0, 1
# count = 0
# if num == 1:
#    print('Fibonacci series till',num,':')
#    print(num1,end=' ')
# else:
#    print('fibonacci series:')
#    while count < num:
#        print(num1,end=' ')
    #        num3 = num1 + num2
#        num1 = num2
#        num2 = num3
#    count += 1

# brands='mi realme oppo vivo samsung'.split()

# # index=0
# # for index in range(len(brands)):
# #    print(brands[index])
# for mobile in brands:
#    print(mobile) 






# students=[
#     [34,67,65,75,75,'Rahul'],
#     [34,56,97,97,75,'dupinder'],
#     [34,97,65,67,75,'sonia'],
#     [34,67,65,34,67,'suman'],
#     [0,17,25,35,5,'nobita'],

# ]
# new=[]
# for stu in students:
#    percentage=sum(stu[:-1])/500*100
#    name=stu[-1]
#    new.append([percentage,name])
# print(new)


########dictionaries

# populations={
#     'IND':8948543534,
#     'USA':334958354,
#     'JAP':345634534,
#     'SRI':4359340,
#     'NEP':45094850,
#     'courses':['python','php','data science'],
#     'person':{
#         'name':'riyaa',
#         'age':21
#     }
#     }
# # print(populations['IND'])
# print(populations['person']['age'])



# d = {
#     'k1':[1,2,
#            {
#                'k2':['this is tricky',
#                      {
#                          'tough':[1,2,
#                                   ['hello'
#                                    ]
#                                    ]
#                                    }
#                                    ]
#                                    }
#                                    ]
#                                    }
# print(d['k1'][2]['k2'][1]['tough'][2])




# a=[4,2,4,8,7,0,1]
# a=[3,5,6,7,4,9]
# a=[4,5,2,6,7,5,3,9,2,1]
# if 6 in a:
#     idx_6=a.index(6)
#     idx_9=a.index(9)
#     print(sum(a[:idx_6]+a[idx_9+1:]))
# else:
#     print(sum(a))


# a=int(input("enter an number :"))
# f=1
# for i in range(a,0,-1):
#     f=f*i
# print(f)



# num=int(input("enter a number :"))

# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#       print('prime')



# # check weather the number is prime or not:-
# num = int(input('enter your number:'))
# flag = 0
# for i in range(2,num):
#   if num%i==0:
#     flag = 1
#     break
# if flag == 1:
#   print('Not Prime')
# else:
#   print("Prime")



# num=int(input("enter a number :"))
# is_prime=True
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         is_prime=False
#         break
# if is_prime==True:
#     print('prime')




# num=int(input("enter a number :"))
# if num==2:
#     print('prime')
# elif num%2==0:
#     print('not prime')
# else:
#      is_prime=True
#      for i in range(2,num):
#       if num%i==0:
#         print("not prime")
#         is_prime=False
#         break
#      if is_prime==True:
#         print('prime')
    


# for i in range(1,6):
#     for j in range(i-1,5):
#         print('*',end='')
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
# for i in range(5,0,-1):
#     for j in range(i):
#             print('*',end='')
#     print()


#######functions

# def sum_of_two():       #syntax
#     code



# def sum_of_two():
#     # num1=40
#     # num2=50
#     num1=int(input("enter the number :"))
#     num2=int(input("enter the number :"))
#     result = num1+num2
#     print(result)
# sum_of_two()





# def sum_of_two(x,y):   ###parameters x and y
#     num1=x
#     num2=y
#     result = num1+num2
#     print(result)
# sum_of_two(10,20)   ### actual values are agrguments


# def sum_of_two(x,y):
#     num1=x
#     num2=y
#     result = num1+num2
#     print(result)
# a=int(input("enter the a :"))
# b=int(input("enter the b :"))
# sum_of_two(10,20)  
# sum_of_two(a,b)




# def my_salary(no_of_days):
#     sal=no_of_days*12000
#     print('the salary is',sal)
# my_salary(23)
# my_salary(27)



# def number(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# a=int(input("enter the number :"))
# number(a)



# def series(a):

#     f=1
#     for i in range(a,0,-1):
#         f=f*i
#     print(f)
# a=int(input("enter a :"))

# series(a)



# def my_salary(no_of_days):
#     sal=no_of_days*12000
#     return sal
   
# a=my_salary(23)
# # print(a+1000)
# print(a)



# def series(a):

#     f=1
#     for i in range(a,0,-1):
#         f=f*i
#     return f
# a=int(input("enter a :"))
# b=series(a)
# print(b)



# def sum_of_69(num_list):
#     if 6 in num_list:
#         idx6=num_list.index(6)
#         idx9=num_list.index(9)
#         total=sum(num_list[:idx6]+num_list[:idx9])
#         return total
#     else:
#         return sum(num_list)
# a=sum_of_69([4,3,5,3,8,7,7,5])
# print(a)






# def sum_of_69(num_list):
#     if 6 in num_list:
#         idx6=num_list.index(6)
#         idx9=num_list.index(9)
#         total=sum(num_list[:idx6]+num_list[:idx9])
#         return total
#     else:
#         return sum(num_list)
# a=sum_of_69([4,3,5,3,8,7,7,5])
# print(a)




# def my_salary(no_of_days):
#     sal=no_of_days*12000
#     return sal
   
# a=my_salary(23)
# # print(a+1000)
# print(a)


