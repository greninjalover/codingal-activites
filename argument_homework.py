def shutdown(answer):
    if answer == "Yes":
        return "shutting down"
    elif answer == "No":
        return "abort shut down"
    

user_input = input("Do you want to shut down? ")
print(shutdown(user_input))
