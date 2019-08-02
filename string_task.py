#this program is a game called MADLIPS 



print("\t\t\tWelcome to MadLips")
cont = "y"
while(cont.lower() != "n"):
	time = input("please enter a time:   ")
	items = input("enter an item:  ")
	name = input("please enter a name:   ").capitalize()
	scream = input("please enter a scream sentence:   ").upper()
	action = input("please enter an action:   ")

	story = """\n\nIt was {} o'clock when I heard a knock at the door.
I opened the door and there was a box full of {} with a note saying "From Mr. {}".
Just as I closed the door I heard a scream "{}".
I froze in place and all I could do was {}."""

	print(story.format(time,items,name,scream,action))

	cont = input("do you want to continue (Y/N):   ")