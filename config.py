
NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'
UP= 'up'
DOWN='down'
DESC= 'desc'#Description of room
LOCKVALUE='lockvalue'
EXITS=(NORTH,EAST,SOUTH,WEST,UP,DOWN)
ITEMS='items'
KEYWORD = 'keyword'
VALUEWORD = 'valueword'
LOCKVALUE = 1
LOCKROOM = 'lockroom'

worldRooms = {
    'Loading Dock' : {
       SOUTH : 'Koinonia',
        NORTH: 'Garbo Central',
        DESC : """Welcome.....\n to the Holden Game!!!(made by Nico & Alex.)\nYou are a new staff member at Holden Village, a lutheran retreat center in the North Cascade mountains.\nYou have had an arduous journey, taking planes, buses, boats and more buses, until....\nFinally.\nThe bus is pulling in to the village.\nBut.........\nThere's no one there, waving at you and celebrating your arrival.\nAbsolutely nobody.\nYou turn around to ask your bus driver what the heck is going on,\nbut they're gone.\njust.... not there.\nYou can tell that something weird is going on, and you are going to get to the bottom of it.\nAnd so starts your adventure...\n\n\n\nMove from room to room with north,east,south,west,up,and down.\n\nCOMMANDS\n##########\ntake or get + item in room - puts an item in your inventory\nuse + item in room or item in inventory - uses an item(primarily keys)\ninventory - displays all items in your inventory\nlook or read + item in room or inventory - displays an item's description\n\n\n\nIMPORTANT!!!!!!! YOU MUST TYPE ITEMS EXACTLY THE WAY THEY ARE SHOWN or else it won't work. IT'S CASE-SENSITIVE TOO!!!!!\n\n Type in a keyword to get out of a room that you are locked into.""",
        ITEMS : {
        }
    },

    'Koinonia' : {
        SOUTH : 'Railroad Creek',
        LOCKROOM:'Office Hallway',
        LOCKVALUE:1,
        DOWN:'Craft Cave',
        WEST:'Library',
        EAST : 'Fireside',
        NORTH : 'Loading Dock',
        DESC : 'This building is used for lots of stuff. or at least, it used to be....\n there seems to be a gate with a bronze lock blocking the upstairs.',
        ITEMS : {
        }
    },

    'Railroad Creek' : {
        NORTH : 'Koinonia',
        DESC : 'The creek rushes by as you look at the abandoned construction vehicles.\n You feel very lonely.....',
        ITEMS : { 'Bronze Key': 1
        }
    },

    'Office Hallway' : {
        DOWN : 'Koinonia',
        DESC : 'This hallway was once filled with offices.\n Now, all the doors have metal bars on them.',
        ITEMS : {'Silver Key': 1
        }
    },

    'Craft Cave' : {
        UP : 'Koinonia',
        DESC : 'This room is full of looms, although there is a thick coating of dust on all of them.',
        ITEMS : {
        }
    },

    'Library' : {
        EAST : 'Koinonia',
        DESC : '''You think that you see a person reading a book,\nbut when you get closer you see that it\'s just a mannequin.\nWhat the heck!!!! Why would there be a mannequin here!!!\nthe book that it\'s reading has a large word scrawled on the page that it's open to.''',
        ITEMS : {'Mannequin Book' : 1
        }
    },

    'Fireside' : {
        #you should trap the player in here and have them find something
        KEYWORD : '12345',
        VALUEWORD : 'Koinonia',
        DESC : 'The door closes and locks.\nWhat the heck, there\'s a keypad here, in this old-timey village place!\n you obviously need to find something to help you out of here',
        ITEMS : { 'Note': 1
        }
    },

    'Garbo Central' : {
        UP : 'Dining Hall',
        SOUTH:'Loading Dock',
        DESC : 'This room has garbage cans overflowing with multiple different types of recycling.\n Rummaging around in the trash, you find......\nTrash.',
        ITEMS : { 'Trash':100
        }
    },

    'Dining Hall' : {
        LOCKVALUE:2,
        LOCKROOM:'Hotel',
        DOWN:'Garbo Central',
        EAST:'Ark',
        NORTH:'Sauna',
        DESC : 'There\'s a kitchen and stuff here.\n "Aw yeah!!" you think hungrily as you check the walk-in refrigerator,\nbut there is no food.\nyou do some more exploring and find out that the upstairs is locked.\nyou have no idea where the key is,cbut you think the lock is made of silver.',
        ITEMS : {

        }
    },

    'Hotel' : {
        DOWN : 'Dining Hall',
        DESC : 'People used to sleep in these rooms, but now they are all barred.',
        ITEMS : {'Gold Key' :1
        }
    },

    'Ark' : {
        WEST:'Dining Hall',
        DESC: 'There\'s a tree stump on this wooden platform with benches\nYou can tell that this has no place in the story.',
        ITEMS : {

        },
    },

    'Sauna' : {
        SOUTH:'Dining Hall',
        DESC : 'This room has a stove and wooden benches.\nIt seems like it would have been a lot of fun, but that\'s not what\'s catching your attention.\nThere is a very mysterious trapdoor in the middle of the room.\nand on it is a golden lock.',
        ITEMS : {
                 },
        LOCKVALUE : 3,
        LOCKROOM : 'Mysterious Trapdoor'
    },

    'Mysterious Trapdoor' : {
        DESC: 'Mysterious sounds are coming from this long, cold hallway.  You can see fluorescent lighting in the distance.',
        ITEMS: {
        },
        NORTH: 'The Great Unknown'

    },

    'The Great Unknown' : {
        DESC : 'After walking for about 2 minutes, the hallway slopes downward.\nhere, there is a seat with a wheel on it that attaches to the railing on the ground.\nyou sit in the seat.\nAfter a rather fun ride, you look through a window and see a extremely large cavernous room filled with people milling about.  A sign says:\nNEW HOLDEN VILLAGE\nyou are really confused!!! what could have happened to drive the villagers underground?\nIt must have happened a while ago because this couldn\'t have been built in a day.\n And WHY THE HECK DID THEY INVITE YOU TO COME!?!?!?!?!\n you look down the hallway and see a museum-type thing which probably explains everything.',
        WEST : 'Museum-Type Thing',
        ITEMS: {
        },
    },

    'Museum-Type Thing' : {
        DESC : 'THE STORY OF NEW HOLDEN VILLAGE\n50 YEARS AGO, ALIENS CAME TO EARTH AND LANDED AT HOLDEN VILLAGE\nTHEY TAUGHT US THE SECRET OF ETERNAL LIFE IN EXCHANGE FOR ALL THE COPPER IN COPPER MOUNTAIN\n(COPPER IS AN EXTREME RARTIY, GALACTICALLY SPEAKING)\nHOWEVER, THERE WAS ANOTHER COST.\nTO PROTECT THE REST OF THE WORLD FROM KNOWING ABOUT ALIENS, THEY SEALED HOLDEN IN A TIME RIFT.\nBUSINESS WENT AS USUAL IN THE REAL WORLD, WHILE WE ARE TRAPPED IN A RIFT ETERNALLY.\nOCCASIONALLY, VISITORS TO HOLDEN VILLAGE WILL DISAPPEAR WITHOUT A TRACE.\nTHIS IS BECAUSE THEY ARE PASSING THROUGH THE TIME RIFT INTO OUR WORLD\nWHICH WE HAVE ENHANCED WITH ALIEN TECHNOLOGY.\nIF YOU ARE READING THIS, YOU HAVE PASSED THROUGH THE TIME RIFT.\n\n\n\nTHERE IS NO KNOWN WAY TO GET BACK THROUGH.\nUNTIL A WAY IS FOUND, YOU ARE TRAPPED.  YOU WILL BE TREATED AS AN HONORABLE MEMBER OF OUR COMMUNITY AND WE WILL GLADLY SHARE THE SECRET OF ETERNAL LIFE.\n\n\n\n\n\n\n\n\n\n\n\n\n\nSo that\'s what\'s going on.  You\'re not sure how to feel.\n  You guess you should just hope for the best and try to enjoy your new life.\n  You did want to live in community, didn\'t you?\n\n\n\n\n\ntype "end" to end the game',
        ITEMS : {

        }
    }
}

GRNDDESC = 'GRNDDESC'
LONGDESC = 'longdesc'
TAKEABLE = 'takeable'
USAGE = 'usage'
PRICE = 'price'
DESTROYABLE = 'destroyable'
KEYNUMBER = 1



worldItems = {
    'Mannequin Book' : {
        TAKEABLE : True,
        GRNDDESC : 'a book that has a word or something written on page 82 and 83',
        LONGDESC : 'www.nico3000.com - Great Website!',
        USAGE : 'read'
    },

    'Note' : {
        TAKEABLE : True,
        GRNDDESC : 'a note taped to the fire ring',
        LONGDESC:'12345',
        USAGE : 'read'
    },

    'Bronze Key' : {
        TAKEABLE : True,
        GRNDDESC : 'a key made of bronze',
        LONGDESC : 'this key is really old-looking, yet it gleams in the sun.',
        USAGE : 'unlock',
        KEYNUMBER : 1
    },

    'Silver Key' : {
        TAKEABLE : True,
        GRNDDESC : 'a key made of silver',
        LONGDESC : 'this key is completely flat with just one notch.\nisn\'t that weird?',
        USAGE : 'unlock',
        KEYNUMBER : 2
    },

    'Gold Key' : {
        TAKEABLE : True,
        GRNDDESC : 'a key made of gold',
        LONGDESC:'it blows your mind that this key is made of solid gold.  you just can\'t believe it.',
        USAGE : 'unlock',
        KEYNUMBER : 3
    },

    'Trash' : {
        TAKEABLE : True,
        GRNDDESC : 'complete garbage, there is literally nothing that you can do with this.',
        LONGDESC:'why would you try to read this garbage?',
        USAGE : 'read'
    },


}