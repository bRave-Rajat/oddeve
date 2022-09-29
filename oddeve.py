

from getpass import getpass

from click import prompt

wlcm="""
################################################################################

Welcome to odd eve

A will bat first 

if A wins game will show winner page and end

If B wins game will end automaticallly

################################################################################


"""
print(wlcm)
a=1
user_listA=[]

while a<10:
    
    userA=int(getpass(prompt = "Player A move: "))
    if userA >6:
        print("Dont enter a number greater than 6")
        exit()
        

    userB=int(input("Player B move: "))
    if userB>6:
        print("Dont enter a number greater than 6")
        exit()
        

        
    
    
    if userA != userB:
        user_listA.append(userA)
        print("A chose:", userA)
        print("Score of A: ",sum(user_listA))
        print("############################################################################")
        a=1

    else:
        print("A chose:", userA)
        print("Final Score 😣😣 : ",sum(user_listA))
        print("############################################################################")
        a=11
        

    

    
    
    
    

    
        

    
        


    
    

    

#CHASE CODE

user_listB=[]

while sum(user_listA)>=sum(user_listB):
    userB=int(getpass(prompt = "Player b move: "))
    if userB >6:
        print("Dont enter a number greater than 6")
        exit()

    userA=int(input("Player A move: "))
    if userA>6:
        print("Dont enter a number greater than 6")
        exit()

    
    if userA==userB:
        print("B chose ", userB)
        print("A won yesssssssss")
        print("###################################################################")
        break

    else:    
        user_listB.append(userB)
        print("B chose: ", userB)
        print("Current score:" , sum(user_listB) )
        print("####################################################################")
        


