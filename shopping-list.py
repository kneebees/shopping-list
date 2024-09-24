itemnumber = 1

print("This is your online shopping list.\n")

name = input("What's your name? ").strip().capitalize()
item = input("\nWhat do you need to shop for (1 item)? ").lower().strip()
yourlist = [item]
print(yourlist)

add = 'y'

def itemAdd(add, yourlist):
  while add == 'y':
    global item
    add = input("\nWould you like to continue adding items to the list (y/n)? ")
    if add == 'y':
      item = input("\nWhat else do you need to shop for (1 item)? ").lower().strip()
      yourlist.append(item)
      yourlist.sort(reverse = True)
      print("{}'s shopping list:".format(name))
      print(yourlist)
    elif add == 'n':
      break
    else: 
      add == 'y'
      print("Write either 'y' or 'n.'")

itemAdd(add, yourlist)
print("{}'s final shopping list: \n".format(name))
print(yourlist)





