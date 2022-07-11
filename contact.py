num = input("Enter the phone number: ")
names = {'1234567899' :'Amal' , '2222222222' : 'Ahmed' , '1009685284' : 'Mahmoud Mohmed','6666666666' : 'Khadijah' , '5555555555' : 'Rawan' }


if len(num) == 10:   
    if num in names.keys():
        print(f"this number for {names[num]}")

    else:
        print("Sorry, the number is not found ")
      
else:
    print("This is invalid number")