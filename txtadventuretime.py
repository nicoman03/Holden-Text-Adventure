import config

"""

COLOR CODES FOR TEXT



If you want to color a string include the color variable BEFORE the string and always END with the ENDC variable

Example:

print bcolors.PINK + "Hello World" + bcolors.ENDC

Will output "Hello World" in a pinkish color



print bcolors.PINK + "Hello " + bcolors.ENDC + bcolors.GREEN + "World" + bcolors.ENDC

Will output a pink "Hello" and a green "World"



Real usage examples in show_room function

"""

class bcolors:

    PINK = '\033[95m'  #Item Marker

    BLUE = '\033[94m'  #Direction Marker

    GREEN = '\033[92m'

    YELLOW = '\033[93m'

    RED = '\033[91m'

    BOLD = '\033[1m'  #Location Marker

    ENDC = '\033[0m'



"""

GAME SETUP

"""

def move_loc(direction):

    global location



    if direction in config.worldRooms[location]:

        location = config.worldRooms[location][direction]

        show_room()

    else:        print('you can\'t go that way!')



def move_secret(newLocation):

    global location



    location = newLocation

    show_room()



def get_secret():

    if config.KEYWORD in config.worldRooms[location]:

        return config.worldRooms[location][config.KEYWORD]



    return False



def show_room():

    print('\n'+bcolors.BOLD + location + "\n####" + bcolors.ENDC)

    print config.worldRooms[location][config.DESC] + '\n'



    for obvious_exit in config.worldRooms[location]:

        if obvious_exit in config.EXITS:

            print bcolors.BLUE + obvious_exit + bcolors.ENDC + ": " + config.worldRooms[location][obvious_exit]

            #print "%s: %s" % (obvious_exit , config.worldRooms[location][obvious_exit])



    if len( config.worldRooms[location][config.ITEMS])>0:

        print("Around the room you see:")

        for item in config.worldRooms[location][config.ITEMS]:

            print(bcolors.PINK + item + bcolors.ENDC + " - " + config.worldItems[item][config.GRNDDESC])



def do_destroy(itemToBreak):

    if itemToBreak in config.worldRooms[location][config.ITEMS]:  # check if item is there

        # check if item is DESTROYABLE

        if config.DESTROYABLE in config.worldItems[itemToBreak]:

            if config.worldItems[itemToBreak][config.DESTROYABLE]==True:

                #check if there are any left

                if config.worldRooms[location][config.ITEMS][itemToBreak] > 0:

                    config.worldRooms[location][config.ITEMS][itemToBreak] -= 1

                    print 'You destroyed the %s!'%itemToBreak

                else:

                    print 'You already destroyed the %s...'%itemToBreak

            else:

                print 'No! You might need that!'

        else:

            print 'No! You might need that!'

    else:

        print 'there\'s no %s'%itemToBreak



def do_take(itemToTake):

    #If itemToTake is in location

    if itemToTake in config.worldRooms[location][config.ITEMS]:

        #Check if TAKABLE

        if config.worldItems[itemToTake][config.TAKEABLE] == True:

            # check if there is any left

            """

            if config.worldItems[itemToTake][config.AMOUNT]>0:

                inventory.append(itemToTake)

                print 'you got the %s'%itemToTake

                config.worldItems[itemToTake][config.AMOUNT] -= 1

            """

            if config.worldRooms[location][config.ITEMS][itemToTake] > 0:

                inventory.append(itemToTake)

                print 'You got the %s!'%itemToTake

                config.worldRooms[location][config.ITEMS][itemToTake] -= 1

            else:

                print 'You picked up all the %s\'s'%itemToTake



        else:

            print 'uh, you can\'t take that.'

            #Not takable

    else:

        #Item is not there

        print 'there is no %s' % itemToTake



def show_inv():

    #create dictionary of inventory

    if len(inventory) > 0:

        dict_inv = {}


        for i in inventory:

                dict_inv[i] = inventory.count(i)





        """

        For each item in the inventory they should be counted and sorted into two catagories

        1) dict_inv

        dict_inv is a dictionary that will keep track of the item and how many of that item there are.

        If an item is already in dict_inv, it's value will be increased by 1

        If an item is not in dict_inv, it will be added with a value of 1



        2) list_note

        list_note is a list because Notes are unique items. There should only ever be one of them.

        Notes will always start with the word "Note - " and after the hyphen will be a title to remind you what this note is.



        Once all of them are counted and sorted into the two variables, the code below will print out the inventory

        """




        if len(dict_inv) > 0:

            print "INVENTORY\n===="

            for i in dict_inv:

                print bcolors.PINK + i + bcolors.ENDC + "\tx" + str(dict_inv[i])



    else:

        'You have nothing in your inventory!'


def do_use(itemToUse):



    if itemToUse in inventory:
        if 'Key' in itemToUse:
            if config.worldItems[itemToUse][config.KEYNUMBER] == config.worldRooms[location][config.LOCKVALUE]:
                move_secret(config.worldRooms[location][config.LOCKROOM])
            else:
                print "that's not the right key!!!!!!"
        elif 'read' == usable(itemToUse):
            print 'you\'ve got to read this, not use it!!'
        else:
            print "you can only use keys..."
    elif itemToUse in config.worldRooms[location][config.ITEMS] :
        if 'Key' in itemToUse:
            if config.worldItems[itemToUse][config.KEYNUMBER] == config.worldRooms[location][config.LOCKVALUE]:
                move_secret(config.worldRooms[location][config.LOCKROOM])
            else:
                print "that's not the right key!!!!!!"
        elif 'read' == usable(itemToUse):
            print 'you\'ve got to read this, not use it!!'
        else:
            print "you can only use keys...."
    else:
        print "what %s?"%itemToUse





    """

    Keys are implemented, but no other items are.

    I tried to make it tell you to do the read command if it was a readable item, but that didn't work.

    If you want to make a key, you should make each one specific and have a different lock number(or purposely have one key for multiple rooms).
    make sure that the name has 'Key' in it.
    """





def do_look(itemToLook):
    if itemToLook in inventory:
            if readable(itemToLook) == True:
                print config.worldItems[itemToLook][config.LONGDESC]
            else:
                print "you can't read that."
    elif itemToLook in config.worldRooms[location][config.ITEMS]:
        if readable(itemToLook) == True:
            print config.worldItems[itemToLook][config.LONGDESC]
        else:
            print "you can't read that."
    else:
            print "what %s?"%itemToLook

    #TODO for Nico



    """

    This class will check to see if the itemToLook is in the room or inventory

    Then it should check if the item is readable (check out the new helper functions below!!!)

    Then if readable it should print out the LONGDESC of the item

    """

    #TODO END




"""

This is a helper class usable

This class will return True or False based on whether the item has a config.USAGE attribute

"""

def usable(item):

    return config.USAGE in config.worldItems[item]



"""

This is a helper class readable

This class will return True or False based on whether the item has a config.LONGDESC attribute

"""

def readable(item):

    return config.LONGDESC in config.worldItems[item]



#Inventory variable and starting items

inventory = ['Note - FORWARD']




#Location variable and starting location

location = 'Mysterious Trapdoor'



#Game running flag

end = False



"""

GAME LOOP

"""

show_room()

while(not(end)):

    #Raw input from user

    usr_in = raw_input(">_ ")



    #Exploded input into array of words split by spaces

    #Ex:

    #usr_in: take Coffee    =>  mod_in: ['take', 'Coffee']

    mod_in = usr_in.split(' ')



    #Decision Tree

    #Move Branch

    if usr_in in config.EXITS:

        move_loc(usr_in)



    #Secret Keyword branch

    elif usr_in.upper() == get_secret():

        move_secret(config.worldRooms[location][config.VALUEWORD])



    #Take Branch

    elif 'take' == mod_in[0] or 'get' == mod_in[0]:

        item_in = ' '.join(mod_in[1:])

        do_take(item_in)



    #Use Branch

    elif 'use' == mod_in[0]:

        item_in = ' '.join(mod_in[1:])

        do_use(item_in)



    #Destroy Branch

    elif 'destroy' == mod_in[0]:

        item_in = ' '.join(mod_in[1:])

        do_destroy(item_in)



    #Inventory Branch

    elif 'inventory' == usr_in:

        show_inv()



    #Look Branch

    elif 'look' == mod_in[0] or 'read' == mod_in[0]:

        item_in = ' '.join(mod_in[1:])

        do_look(item_in)




    #End Branch

    elif usr_in == 'end':

        end= True
        print 'Made by Nico and Alex'
        print 'THE END'



    #Typo Branch

    else:

       print 'please use valid command'

