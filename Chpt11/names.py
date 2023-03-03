from name_function import get_formatted_name

print("Enter 'q' at any time to quit")
while True:
    first= input("\n Please give first name: ")
    if first =='q':
        break

    second= input("\n Please gives last name: ")
    if second== 'q':
        break

    formatted_name= get_formatted_name(first, second)
    print(f"\tNeatly formatted name: {formatted_name}")