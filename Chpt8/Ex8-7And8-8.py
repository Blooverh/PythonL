def make_album(artist_name, album_title, songsNum=None): #songsNum= None -> OPTIONAL VALUE , None can be seen as a place holder
    artist_info={"Artist Name": artist_name, "Album Title":album_title}
    if songsNum: #if there is an argument for the optional value sognsNum, then we create a new dictionary variable to store the optional value if it exists
        artist_info['Number of Songs']=songsNum
    return artist_info

#print(make_album("skrillex", "Monsters"))
#print(make_album("Angerfist", "Anger",8))

while True:
    print("\nTell me the artists name: ")
    print("(Enter 'q' at any time to quit the program)")
    ar_name=input("Artist name: ")
    if ar_name == 'q':
        break

    alb_name=input("Name of the album: ")
    if alb_name == 'q':
        break

    songMessage=input("Do you want to add number of songs? ")
    if songMessage =='yes':
        songNum=input("How many songs do you want put: ")
        formatted_info= make_album(ar_name, alb_name, songNum)
        print(formatted_info)
    elif songMessage =='no':
        formatted_info= make_album(ar_name, alb_name)
        print(formatted_info)
    elif songMessage =='q':
        break