# main function
def coffee_shop():
    # list for queue  
    queue = []
    
    # loop to run the code back
    while True:
        print("*A customer walks in*")
        print("Welcome to the best coffee shop in the world\n")
        print("1. Place an order")
        print("2. Serve next customer")
        print("3. View queue")
        print("4. Exit\n")
        
        choice = input("Enter your choice: ")  # main menu input
      
        # choice logic
        if choice == "1":
            name = input("\nEnter your name: ")
            order = input("\nEnter your order (We serve everything!): ") 
            queue.append((name, order))
            print(f"\nThank you, {name}. Your order for {order} has been placed.\n")
        
        elif choice == "2":
            if queue:
                served_name, served_order = queue.pop(0)  # remove name and order from queue 
                print(f"{served_name}, your {served_order} is ready.\n")
            else:
                print("No orders are in the queue right now.\n")
        
        elif choice == "3":
            if queue:
                print("\nCurrent orders in queue:")
                for name, order in queue:
                    print(name, "-", order)
                print()
            else:
                print("No orders are queued.\n")
        
        elif choice == "4":
            print("\nThank you for visiting the best coffee shop in the world.")
            break
        
        else:
            print("Invalid choice, please try again.\n")
            
# runs the function
coffee_shop()
