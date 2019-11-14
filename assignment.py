'''this program is prepared by Hassan Afridi on Visual Studio Code 
email = hassanyousufzai786@hotmail.com
cell number = 0310-2635440
former Saylani MOS Batch 2 Student'''


def goto(linenum):
    global line
    line = linenum

line = 1
while True:
    if line == 1:
        print();print(" 1. twinkle twinkle \n 2. check python version\n 3. check date and time\n 4. find area of circle by giving radius\n 5. concanating name last name then first name\n 6. addition of two numbers\n or type exit or stop to terminate the program")
        response = input("please type any number in alphabatical or numerical order to run the above program ")
        if response == "one":
            goto(2)
        elif response == "1":
            goto(2)
        elif response == "two":
            goto(3)
        elif response == "2":
            goto(3)
        elif response == "three":
            goto(4)
        elif response == "3":
            goto(4)    
        elif response == "four":
            goto(5)
        elif response == "4":
            goto(5)
        elif response == "five":
            goto(6)
        elif response == "5":
            goto(6)
        elif response == "six":
            goto(7)
        elif response == "6":
            goto(7)
        elif response == "exit":
            goto(8)
        elif response == "stop":
            goto(8)
        else:
            goto(100)
    elif line == 2:

# Twinkle poem program #

        print();print ("Twinkle, twinkle, little star,\n      How I wonder what you are! \n            Up above the world so high, \n            Like a diamond in the sky.\nTwinkle, twinkle, little star,\n      How I wonder what you are")
        goto(20)

    elif line == 3:

# python version program #

        from platform import python_version
        print();print ("your python version is " + python_version())
        goto(20)

    elif line == 4:

# date and time program   

        from datetime import datetime
        now = datetime. now()
        dt_string = now. strftime("%d/%m/%Y/ %H:%M:%S")
        print();print ("date and time = ", dt_string)
        goto(20)

    elif line == 5:

# radius of circle to compute area program

        rc = int(input("please give radius of circle to calculate its area "))
        pi = (3.1415926535897932384626433832795)
        area_of_circle = ( (rc**2) * pi)
        print();print ("Area of the circle is", area_of_circle)
        goto(20)

    elif line == 6:

# concatinating name program
        
        first_name = (input("please enter your first name "))
        last_name = input("please enter your last name ")
        print();print (last_name + " " + first_name)
        goto(20)

    elif line == 7:

# addition program

        no_one = int(input("give first number to make addition with second number "))
        no_two = int(input("please give second number "))
        print();print ("Addition for", no_one, "and", no_two,"is", no_one + no_two)
        goto(20)
    
    elif line == 8:
        break
    
    elif line == 20:
        goto(1)
    
    elif line == 100:
        print();print ("You're annoying me - answer the question!")
        goto(1)