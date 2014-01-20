import os
import random


nouns = []
adj = []
numbers = []
numbers_count = []
colours = []
tavern_synonyms = []

    #food 
food_prep = []
menu_veg = []
menu_meat_poor = []
menu_meat_std = []
menu_meat_excel = []

    #drink types
menu_drink_poor = []
menu_drink_std = []
menu_drink_excel = []

#tavern description details
tav_desc_building_poor = []
tav_desc_building_std = []
tav_desc_building_excel = []

tav_desc_misc_poor = []
tav_desc_misc_std = []
tav_desc_misc_excel = []
tav_desc_misc_all = []

tav_desc_sleep_poor = []
tav_desc_sleep_std = []
tav_desc_sleep_excel = []

tav_desc_patrons = []
tav_desc_atmos = []

#get current directory
directory = os.getcwd()



def load():


    
    with open(directory + '\\txt\\adjectives.txt') as f:
        adj_lists = f.read().splitlines()
        for i in adj_lists:
            with open('txt\\' + i) as f:
                temp_adj = f.read().splitlines()
                adj.extend(temp_adj)

    #load list of files with nouns, then loads those files
    with open(directory + '\\txt\\nouns.txt') as f:
        nouns_lists = f.read().splitlines()
        for i in nouns_lists:
            with open('txt\\' + i) as f:
                temp_nouns = f.read().splitlines()
                nouns.extend(temp_nouns)

    #load numbers.txt (one, two three)
    with open(directory + '\\txt\\numbers_noun.txt') as f:
        numbers = f.read().splitlines()
        numbers = strip_empty(numbers)

    #load numbers_count.txt (first, second, third)
    with open(directory + '\\txt\\numbers_count.txt') as f:
        numbers_count = f.read().splitlines()
        numbers_count = strip_empty(numbers_count)


    #load colours.txt
    with open(directory + '\\txt\\colours.txt') as f:
        colours = f.read().splitlines()
        colours = strip_empty(colours)


    #load tavern synonyms.txt
    with open(directory + '\\txt\\tavern_syn.txt') as f:
        tavern_synonyms = f.read().splitlines()
        tavern_synonyms = strip_empty(tavern_synonyms)

    #load food files
    with open(directory + '\\txt\\food_prep.txt') as f:
        food_prep = f.read().splitlines()
        food_prep = strip_empty(food_prep)

    with open(directory + '\\txt\\menu_meat_poor.txt') as f:
        menu_meat_poor = f.read().splitlines()
        menu_meat_poor = strip_empty(menu_meat_poor)

    with open(directory + '\\txt\\menu_meat_std.txt') as f:
        menu_meat_std = f.read().splitlines()
        menu_meat_std = strip_empty(menu_meat_std)

    with open(directory + '\\txt\\menu_meat_excel.txt') as f:
        menu_meat_excel = f.read().splitlines()
        menu_meat_excel = strip_empty(menu_meat_excel)

    with open(directory + '\\txt\\menu_bread.txt') as f:
        menu_bread = f.read().splitlines()
        menu_bread = strip_empty(menu_bread)

    with open(directory + '\\txt\\menu_cheese.txt') as f:
        menu_cheese = f.read().splitlines()
        menu_cheese = strip_empty(menu_cheese)

    with open(directory + '\\txt\\menu_veg.txt') as f:
        menu_veg = f.read().splitlines()
        menu_veg = strip_empty(menu_veg)

    with open(directory + '\\txt\\menu_drinks_poor.txt') as f:
        menu_drinks_poor = f.read().splitlines()
        menu_drinks_poor = strip_empty(menu_drinks_poor)

    with open(directory + '\\txt\\menu_drinks_std.txt') as f:
        menu_drinks_std = f.read().splitlines()
        menu_drinks_std = strip_empty(menu_drinks_std)

    with open(directory + '\\txt\\menu_drinks_excel.txt') as f:
        menu_drinks_excel = f.read().splitlines()
        menu_drinks_excel = strip_empty(menu_drinks_excel)


    generators = (adj, nouns, numbers, numbers_count, colours, tavern_synonyms, food_prep, menu_meat_poor, menu_meat_std, menu_meat_excel, menu_bread, menu_cheese, menu_veg, menu_drinks_poor, menu_drinks_std, menu_drinks_excel)

    return generators


def load_tav_desc():
    ''' load files pertaining to the tavern description only '''
    
    with open(directory + '\\txt\\tav_desc_building_poor.txt') as f:
        tav_desc_building_poor = f.read().splitlines()
        tav_desc_building_poor = strip_empty(tav_desc_building_poor)

    with open(directory + '\\txt\\tav_desc_building_std.txt') as f:
        tav_desc_building_std = f.read().splitlines()
        tav_desc_building_std = strip_empty(tav_desc_building_std)

    with open(directory + '\\txt\\tav_desc_building_excel.txt') as f:
        tav_desc_building_excel = f.read().splitlines()
        tav_desc_building_excel = strip_empty(tav_desc_building_excel)

    with open(directory + '\\txt\\tav_desc_misc_poor.txt') as f:
        tav_desc_misc_poor = f.read().splitlines()
        tav_desc_misc_poor = strip_empty(tav_desc_misc_poor)

    with open(directory + '\\txt\\tav_desc_misc_std.txt') as f:
        tav_desc_misc_std = f.read().splitlines()
        tav_desc_misc_std = strip_empty(tav_desc_misc_std)

    with open(directory + '\\txt\\tav_desc_misc_excel.txt') as f:
        tav_desc_misc_excel = f.read().splitlines()
        tav_desc_misc_excel = strip_empty(tav_desc_misc_excel)

    with open(directory + '\\txt\\tav_desc_misc_all.txt') as f:
        tav_desc_misc_all = f.read().splitlines()
        tav_desc_misc_all = strip_empty(tav_desc_misc_all)

    with open(directory + '\\txt\\tav_desc_sleep_poor.txt') as f:
        tav_desc_sleep_poor = f.read().splitlines()
        tav_desc_sleep_poor = strip_empty(tav_desc_sleep_poor)

    with open(directory + '\\txt\\tav_desc_sleep_std.txt') as f:
        tav_desc_sleep_std = f.read().splitlines()
        tav_desc_sleep_std = strip_empty(tav_desc_sleep_std)

    with open(directory + '\\txt\\tav_desc_sleep_excel.txt') as f:
        tav_desc_sleep_excel = f.read().splitlines()
        tav_desc_sleep_excel = strip_empty(tav_desc_sleep_excel)

    with open(directory + '\\txt\\tav_desc_patrons.txt') as f:
        tav_desc_patrons = f.read().splitlines()
        tav_desc_patrons = strip_empty(tav_desc_patrons)

    with open(directory + '\\txt\\tav_desc_atmos.txt') as f:
        tav_desc_atmos = f.read().splitlines()
        tav_desc_atmos = strip_empty(tav_desc_atmos)
        



    tav_desc_generators = (tav_desc_building_poor, tav_desc_building_std, tav_desc_building_excel, tav_desc_misc_poor, tav_desc_misc_std, tav_desc_misc_excel, tav_desc_misc_all, tav_desc_sleep_poor, tav_desc_sleep_std, tav_desc_sleep_excel, tav_desc_patrons, tav_desc_atmos)
    return tav_desc_generators



def strip_empty(iterable):
    '''strips empty values that appear at EOF when reading to list
        hacky as shit, a definite bug workaround, but meh '''
    iterable = [str for str in iterable if str]
    return iterable




