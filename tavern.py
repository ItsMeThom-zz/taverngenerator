###
### random tavern generator
###

"""
TODO:

    New structure + nouns lists:
        the NOUN's POSSESIVE (E.g. Kings head, princes secret, trouts bounty)
        "The NOUN(s) TAVERN_SYNONYM" (The Toads Inn, The Pugs Pub) #DONE
    Refine the lists (remove awkward words)
    Alliteration? (Hen & Hare, Prince & Pony)

    next goal: #done
        descriptors of the inn: #done
            sleeping accomadation #done
            general descriptors (low cielings, rough walls, etc etc)
            patrons of interest # done
            
    

"""

import random
import os
import loadfile
    
#load files ----> thats a long fuckin' line.
adj, nouns, numbers, numbers_count, colours, tavern_synonyms, food_prep, menu_meat_poor, menu_meat_std, menu_meat_excel, menu_bread, menu_cheese, menu_veg, menu_drinks_poor, menu_drinks_std, menu_drinks_excel = loadfile.load()
tav_desc_building_poor, tav_desc_building_std, tav_desc_building_excel, tav_desc_misc_poor, tav_desc_misc_std, tav_desc_misc_excel, tav_desc_misc_all, tav_desc_sleep_poor, tav_desc_sleep_std, tav_desc_sleep_excel, tav_desc_patrons, tav_desc_atmos = loadfile.load_tav_desc()


master_structure_dict = { 'ADJ': lambda : pick(adj),
                          'NOUN': lambda : pick(nouns),
                          'NUM': lambda : pick(numbers),
                          'NUM2': lambda : pick(numbers_count),
                          'COL': lambda : pick(colours),
                          'COOK': lambda: pick(food_prep),
                          'VEG': lambda : pick(menu_veg),
                          'MEAT_P': lambda : pick(menu_meat_poor),
                          'MEAT_S': lambda : pick(menu_meat_std),
                          'MEAT_E': lambda : pick(menu_meat_excel),
                          'BREAD' : lambda : pick (menu_bread),
                          'CHEESE' : lambda : pick(menu_cheese)}


structure_list = ['The ADJ NOUN',
                'The NOUN & NOUN',
                'The COL NOUN',
                'The NUM NOUN (s)',
                'The NUM2 NOUN',
                'The COL NOUN & NOUN',
                'The COL NOUN & COL NOUN',
                'The ADJ COL NOUN',
                'The NUM2 COL NOUN',
                'The ADJ NOUN',
                'The NOUN (s) NOUN',
                'The NOUN (s)']


inn_rating_list = ['POOR', 'STANDARD', 'EXCELLENT']


menu_struct_poor = ['VEG',
                'COOK VEG',
                'MEAT_P & VEG',
                'Vegetable Stew',
                'VEG Soup',
                'BREAD and CHEESE',
                'VEG Soup and BREAD']

menu_struct_std = ['COOK MEAT_S',
                  'COOK MEAT_S and VEG',
                  'COOK MEAT_S and COOK VEG or VEG',
                  'Vegetable Stew',
                  'VEG Soup and BREAD']

menu_struct_excel = ['COOK MEAT_E and VEG',
                  'COOK MEAT_E and COOK VEG or VEG',
                  'Vegetable Stew',
                  'VEG Soup and BREAD'
                  'BREAD and CHEESE',
                  'VEG Soup with BREAD and CHEESE',
                  'COOK MEAT_E with BREAD , CHEESE and VEG']



#get current location of python file
directory = os.getcwd()



def pick(seq):
    ''' home-rolled randon sequence index selection'''
    if seq != []:
        i = random.randint(0,len(seq) - 1)
        return seq[i]
    else:
        print "Warning, empty sequence"
        




def create_name():
    ''' builds a name by picking random words based on the structre'''
    structure = random.choice(structure_list)
    name = build_string(structure)
    #40% chance for the tavern to be titled (i.e. Bar, Pub, Inn, etc etc)
    titled_chance = random.randint(1,100)
    if titled_chance <= 40:
        title = pick(tavern_synonyms)
        name = name + " " + title
    return name.title()


def build_menu(rating):
    '''build a tavern menu based on tav rating, returns list'''

    temp_menu = []
    menu = []
    if rating == "POOR":
        
        items = random.randint(2,5)      
        for i in range(0,items):
            temp_menu.append(pick(menu_struct_poor) + " , with a " + pick(menu_drinks_poor))

    elif rating == "STANDARD":
        items = random.randint(3,7)
        for i in range(0,items):
            temp_menu.append(pick(menu_struct_std) + " , with a " + pick(menu_drinks_std))   


    elif rating == "EXCELLENT":
        items = random.randint(5,8)
        for i in range(0,items):
            temp_menu.append(pick(menu_struct_excel)+ " , with a " + pick(menu_drinks_excel))


    for item in temp_menu:
        dish = build_string(item).title()
        menu.append(dish)

    return menu


    
def build_string(string):
    '''builds a new string using provided structure'''
    split_string = string.split()
    name = []
    for word in split_string:
        if word in master_structure_dict:
            tmp = ""
            tmp = master_structure_dict[word]()
            #print tmp
            name.append(tmp)
        else: name.append(word)

            

    final_string = ' '.join(name)
    return final_string


def build_description(rating):
    ''' builds a description of the tavern based on its rating'''
    

    desc = []
    desc.extend(["It is a"])
    items = random.randint(2,4)

    if rating == "POOR":
        floors = pick(["single-story", "two-story"])
        desc.append(floors) #no of floors
        desc.append(pick(tav_desc_building_poor))
        #sleeping arrangements
        desc.append("Accomadation is")
        desc.append(pick(tav_desc_sleep_poor))
        for i in range(1,items): #add rated expositions
            exposition = pick(tav_desc_misc_poor)
            desc.append(exposition)
        for j in range(0,2): #generic expositions
            misc_expos = pick(tav_desc_misc_all)
            desc.append(misc_expos)
            

        #general atmosphere of the tavern
        atmos = pick(tav_desc_atmos)
        desc.append(atmos)
        
        pat = 1 #1 max intersting patrons for poor bar
        for p in range(0,pat):
            patron = pick(["Some ", "A few ", "Some of the "])
            activity = pick(tav_desc_patrons)
            patron = patron + activity
            desc.append(patron)


        
    elif rating == "STANDARD":
        floors = pick(["single-story", "two-story", "three-story"])
        desc.append(floors) #no of floors
        desc.append(pick(tav_desc_building_std))
        #sleeping arrangements
        desc.append("Accomadation is")
        desc.append(pick(tav_desc_sleep_std))
        for i in range(1,items): #add rated expositions
            exposition = pick(tav_desc_misc_std)
            desc.append(exposition)
        for j in range(0,2): #generic expositions
            misc_expos = pick(tav_desc_misc_all)
            desc.append(misc_expos)
            

        #general atmosphere of the tavern
        atmos = pick(tav_desc_atmos)
        desc.append(atmos)
        
        pat = 2 #1 max intersting patrons for poor bar
        for p in range(0,pat):
            patron = pick(["Some ", "A few ", "Some of the "])
            activity = pick(tav_desc_patrons)
            patron = patron + activity
            desc.append(patron)

            
        
    elif rating == "EXCELLENT":
        floors = pick(["single-story", "two-story", "three-story", "four story"])
        desc.append(floors) #no of floors
        desc.append(pick(tav_desc_building_excel))
        #sleeping arrangements
        desc.append("Accomadation is")
        desc.append(pick(tav_desc_sleep_excel))
        for i in range(1,items): #add rated expositions
            exposition = pick(tav_desc_misc_excel)
            desc.append(exposition)
        for j in range(0,2): #generic expositions
            misc_expos = pick(tav_desc_misc_all)
            desc.append(misc_expos)
            

        #general atmosphere of the tavern
        atmos = pick(tav_desc_atmos)
        desc.append(atmos)
        
        pat = 3 #1 max intersting patrons for poor bar
        for p in range(0,pat):
            patron = pick(["Some ", "A few ", "Some of the "])
            activity = pick(tav_desc_patrons)
            patron = patron + activity
            desc.append(patron)


    final_description = ' '.join(desc)
    return final_description



##run
def main():

    tavern_name = create_name()
    rating = pick(["POOR", "STANDARD", "EXCELLENT"])
    menu = build_menu(rating)
    description = build_description(rating)
    print tavern_name
    print "========================================================================================"
    print description
    print "\n========================================================================================"
    print "MENU:"
    for item in menu:    
        print "\n"
        print "\t" + item


if __name__ == "__main__":
    main()



    





















    



