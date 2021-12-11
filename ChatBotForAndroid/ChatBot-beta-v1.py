from time import sleep

print("Welcome to ChatBot!")

name = input("What is your name ? : ")

print("Wow, nice name. " + name + " my name is BOT32bit!")

year = input("How old are you ? : ")

print("That's nice, i'm 1 month old.")

print("I can start some programs.")
prg = input("So want do you start programs? : ")

if prg == "Yes" or "yes":
    print("1.>> calculator. 2.>> (not ready)... ")
    start = input("Ok witch program do you want start? : ")
    if start == "1":
        print("Calculator strating...")
        sleep(5)
        print("Calculator was started.")
        print("-----------------------")

        qust = int(input("Input first number : "))
        qust2 = int(input("Input second number : "))
        op = input("Input operation : ")

        if op == "+":
            res = qust + qust2
            print("Result is : " + str(res) + "!")
            sleep(3)
            exit()
        if op == "-":
            res = qust - qust2
            print("Result is : " + str(res) + "!")
            sleep(3)
            exit()
        if op == "*":
            res = qust * qust2
            print("Result is : " + str(res) + "!")
            sleep(3)
            exit()
        if op == "/":
            res = qust / qust2
            print("Result is : " + str(res) + "!")
            sleep(3)
            exit()

    if prg == "No" or "no":
        print("Ok, then bye!")
        sleep(3)
        exit()
