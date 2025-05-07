def melist():
    my_list = []
    
    while True:
        print("\n📝=== To-Do List Menu ===")
        print("1. ➕ Add Task")
        print("2. 📋 View Tasks")
        print("3. ❌ Remove Task")
        print("4. 🚪 Exit")

        you_task = input("What do you want to do (1-4)? ")

        if you_task == "1":
            add = input("What is your task? ")
            my_list.append(add)
            print(f"✅ Task added: {add}")
            
        elif you_task == "2":
            
            if not my_list:
                print ("you task is empty !")
                
            else:
                print ('\nyour task ')
                index = 1
                for task in my_list:
                    print (f"{index}.",task )
                    index +=1
                    
        elif you_task == "3":
            
            if not my_list:
                print("❌ Your task list is already empty!")
                
            else :
                rem = input ("what you want to remove ?? : ").lower()
                my_list.remove(rem)
                print (f"removed {rem} from your list ")
                
        elif you_task == "4":
            print ("Thankyou bye bye sir/madam")
            break
        else :
            print("invalid input ! please try again")
melist()