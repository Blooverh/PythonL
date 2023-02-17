message_list=["Hey man how are u?","Im fire what about you? ", "How is school? "]
sent_messages=[]
# def show_messages(message_list):
#     for msg in message_list:
#         print(msg)

# show_messages(message_list)
# print()

def send_messages(message_list):
    
    while message_list:
        msg=message_list.pop()
        print(f"sending the following message '{msg}' to list of sent messages")
        sent_messages.append(msg)
    print()
    print(f"The sent_message list now contains the following messages: {sent_messages}")
    #print()
    #print("Original list has now inside function: ",message_list)

# send_messages(message_list) #this call modifies original list 
# print(message_list) #list will be empty after function call modified original list by poping values out of original list
# print()
send_messages(message_list[:]) #this function creates a copy of original list, original list stays intact
print(message_list) #original list prints original values as it was not modified due to list copy       