'''
Eric Born

18 May 2020

Framework for the apps front end
'''
import eel
from checks import check_for_mod, check_inv_stash as inv, \
                   check_for_magic as magic, check_for_currency as currency
from roll_item import roll_item

eel.init('static')

# 1st test is inventory stash check, 2nd is magic rarity, 3rd is currency
# present in inventory
@eel.expose
def roll_status_check(num, curr):
    if num == 0:
        return(inv())
    if num == 1:
        return(magic())
    if num == 2:
        return(currency(curr))

# check for inventory being open so sorting can start
@eel.expose
def sort_status_check():
    return(inv())

@eel.expose
def roll_function(desired_rolls, desired_curr, desired_mod):
    num_of_rolls = int(desired_rolls)
    mod_to_roll = desired_mod.lower()
    print(mod_to_roll, num_of_rolls)

    for i in range(num_of_rolls):
        mod_check = check_for_mod(mod_to_roll)
        print(mod_check)

        if mod_check == 0:
            break
        else:
            roll_item()
            print('roll', i, 'out of', num_of_rolls, \
                   'looking for', mod_to_roll)

@eel.expose
def sort_inventory():
    

eel.start('index.html')
