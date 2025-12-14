#hacknet.exe
import random
import time
import string

computer = 87
hacked_computer = 1
money = 100
bitcoin = 1
orgnitation = ["CIA","FBI","anonymous","WHO","DPRD","Python","Youtube"]
security_system = 100
password = ("LOLXD")
server = 1842

while True:
    order = input("Type: run hack.net.exe or run exit.exe: ")
    if order == "run exit.exe":
        print("computer will shutdown in 3 seconds...")
        time.sleep(3)
        break
    elif order == "run hack.net.exe":
        print("installing hack.net.exe....")
        time.sleep(3)
        print("installing hack.net/sytem..")
        time.sleep(3)
        print("installing all data..")
        time.sleep(2)
        print("hack.net.exe installed!")
        print("Welcome to hack.net.exe hacker!")
        
        while True:  # inner loop for hacknet commands
            hacknet = input("Type your commands (bitcoin mining / scan computer / password cracker / exit): ")
            
            if hacknet == "run bitcoin mining":
                print("bitcoin mining started...")
                computer -= 1
                hacked_computer += 1
                time.sleep(3)
                print("bitcoin mining ended...")
                money += 5000
                bitcoin += 49
                print(f"You now have ${money} and {bitcoin} bitcoins.")
            
            elif hacknet == "scan computer":
                print("scanning all nearby computers...")
                time.sleep(2)
                print(f"{computer} computers found.")
            
            elif hacknet == "run password cracker":
                print("cracking password...")
                time.sleep(3)
                chars = string.ascii_letters + string.digits
                password = ''.join(random.choice(chars) for _ in range(10))
                print(f"Password cracked: {password}")
            
            elif hacknet == "hack organitation":
                print("attempting to hack organitation...")
                time.sleep(5)
                if random.random() < 0.4:
                    print("Hacking failed! your system is bypassed and your security_system is down  24%")
                    money -= 5000
                    security_system -= 24
                    
                    if security_system <= 0:
                        print("your security  system is 0 now. so your computer is hackable for everyone")
                        print("your computer will shutdown in 3 seconds")
                        time.sleep(3)
                        exit()
                else:
                    hacked_organitation = random.choice(orgnitation)
                    print(f"Hacking success! you hacked {hacked_organitation}.")
                    print(f"you get 25.000$ and 25 bitcoin after hacking {hacked_organitation}")
                    hacked_computer += 75
                    bitcoin += 25
                    money += 25000
            elif hacknet == "open hacker log 1":
                print("11 febuary 2023 8:12AM. we found a secret information of WHO research. WHO is hire a professional author for making them Fake research. we are already say that information but WHO is denied that. WHO say it just a fake news. the police and FBI is taking down binercode. so some True news is no longer avalaible. -binercode team 2")
            elif hacknet == "open hacker log 2":
                print("march 18 2006 9:11 AM. we found an EX anonymous hacker named 'unkown' but his code name his 'john'.we founded that john is hacking a multiplayer game named roblox. we are successfull to taking down him from hacking that game but before he 100% takedowned he is attacking our system with unbeatable worm. so unk0wn is no longer avalaible. -unk0wnn leader")
            elif hacknet == "open unkown log ?":
                print("i made hacknet to test how smart the hacker now... but 'john' is taking down hacknet i know how to beat 'john' wrom. first  you must ERROR SYNTAX! WORM DETECTED! QU1TT N0W!!!!")
            elif hacknet == "reset all":
                option = input("are you sure want to reset all data all hacker have?")
                if option == "no":
                    print("good... YOU ARE MAKE ME MORE POWERFULL HAHAHAHA")
                    print("ERROR unkown error found! automatic break start in 3 seconds")
                    time.sleep(3)
                    print("m-must reset all option yes")
                    exit()
                elif option == "yes":
                    print("no no NO WHAT ARE YOY DO-")
                    print("all data will be reset in 3 seconds..")
                    time.sleep(1)
                    print("NO THIS CAN'T BE")
                    print("3")
                    time.sleep(1)
                    print("M-M-M-MUST ERAAAASEEEEE ALL FOR JOHN")
                    print("2")
                    time.sleep(1)
                    print("Z4RN:good now we all get erased. included john worm")
                    print("1")
                    time.sleep(1)
                    print("ERROR ALL DATA ERASED PLEASE LEAVE N-N-N0E00FSAID9WUEF98W8QWWNDW WEOEOWHEPOE WEOEEH  ERROR!!!!!!!! PASSWORD DWJWUDBDJNBBAYBABSW")
                    exit()
            elif hacknet == "total money":
                print(f"your money now is:{money}")
            elif hacknet == "total bitcoin":
                print(f"your total bitcoin is:{bitcoin}")
            elif hacknet == "hack user":
                hack_user = input("type username: ")
                print("hacking...")
                time.sleep(3)
                print(f"{hack_user} HACKED YOU GET 3000$!")
                money += 3000
                hacked_computer += 1
                hacknet = input("Type your commands (bitcoin mining / scan computer / password cracker / exit): ")
        
            elif hacknet == "open hacker log 3":
                print("binercode. the first hackr group in the  hacknet make by a guy named Mr.doe. binrcode is take downed by FBI after developing an organitaion hack sytem.")
            elif hacknet == "show all system":
                print("system1")
                print("system2")
                print("system3-7")
                print("system8-12")
                print("all public system showed.")
            elif hacknet == "sudo$ show private system":
                print("system 32")
                print("system 67")
                print("system 912")
                print("system:/john.worm")
            elif hacknet == "sudo$ erase system:/john.worm":
                erase_system = input("are you sure what to erase sytem:/john.worm?")
                if erase_system == "no":
                    print("you make a  bad decission")
                    break
                elif erase_system == "yes":
                    print("deleting...(3 seconds)")
                    time.sleep(3)
                    print("system deleted")
                    hacknet = input("Type your commands (bitcoin mining / scan computer / password cracker / exit): ")
            elif hacknet == "run open system file mode":
                print("system file opener mode active! type the system like system1, system2, ETC.")
                systemopen = input("type the name of the system:")
                if systemopen == "system1":
                    print("system file:\n type_system.exe\n screen_system.exe")
                elif systemopen == "system2":
                    print("system file:\n hacker_verified.exe\n [erased]anti_malware/virus/worm.exe\n anti_hack.system.exe")
                elif systemopen == "system3-7":
                    print("error! file is encrypted ")
                elif systemopen == "system8-12":
                    print("1 program found in the file. the other encrypted.:\n exit.exe")
                elif systemopen == "sudo$ system 32":
                    print("all program avalaible:\n exit(2).exe\n other encryptep")
                elif systemopen == "sudo$ system:/john.worm":
                    print("encrypt.exe\n hijack.exe\n malware.exe")
                elif systemopen == "exit":
                    print("exiting system file opener...")
                    hacknet = input("Type your commands (bitcoin mining / scan computer / password cracker / exit): ")                               
                elif systemopen == "sudo$ system 67":
                    print("67.exe")
            elif hacknet == "exit":
                print("computer will shutdown in 3 seconds...")
                time.sleep(3)
                exit()
            elif hacknet == "open hacker log 4":
                print("we are detected the john.worm at the private system. erase it..")
            elif hacknet == "import malware":
                malware = input("type the target username:")
                print("sending...")
                time.sleep(5)
                print("sending sucsses! you get 300$!")
                money += 300
                hacked_computer += 1
                hacknet = input("Type your commands (bitcoin mining / scan computer / password cracker / exit):")
            elif hacknet == "sudo$ hack$%.net userid(9119372) rank admin":
                log_in = input("type password: ")
                if log_in == password:
                    print("log-in sucsses admin. ")
                    print("WARNING! you cannot switch to user mode again when you enter this mode")
                    admin = input("type admin commands: ")
                    if admin == "shutdown server":
                        print("1 server shutdowned...")
                        server -= 1
                    elif admin == "shutdown server :404":
                        print("john.worm:HOW YOU F-F-F-FIND M-M-E?>")
                        print("shutdown server at 3 seconds")
                        time.sleep(3)
                    elif admin == "open admin log1":
                        print("friday, 13, 2019. i found john.worm at server 'not found' the id is encrypted")

                    else:
                        break
            elif hacknet == "sudo$ hack account_name:admin":
                print("sudo cmd active! hacking admin...")
                time.sleep(3)
                print("IP FOUND! hacking ip...")
                time.sleep(2)
                print("HACKING SUCCSESS!")
                money += 10000
                bitcoin += 1000
            else:
                print("SYNTAX ERROR! did you forgot to use run?")
                    
    else:
        print("UNKOWN FILE!")
