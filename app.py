'''
Eric Born

18 May 2020


'''
import eel
from checks import check_for_mod, inv_stash_check as isc, \
                   check_for_magic as magic, check_for_currency as currency
from roll_item import roll_item

eel.init('static')

# 1st test is inventory stash check, 2nd is magic rarity, 3rd is currency
# present in inventory
@eel.expose
def status_check(num):
    if num == 0:
        return(isc())
    if num == 1:
        return(magic())
    if num == 2:
        return(currency())
        
        
#@eel.expose
#def status_check(num):
#    return(num)

#for i in range(3):
#    print(status_check(i))
#status_check(3)

test = 'TEXT'

new_test = test.lower()

@eel.expose
def roll_function(desired_rolls, desired_mod):
    
    mod_to_roll = desired_mod.lower()
    num_of_rolls = int(desired_rolls)
    for i in range(num_of_rolls):
        mod_check = check_for_mod(mod_to_roll)
        return(mod_check)
        if mod_check == -1:
            break
        else:
            roll_item()
            return('roll', i, 'out of', num_of_rolls, \
                   'looking for', mod_to_roll)
     
    
    
#desired_rolls = eel.webData()()

#print(len(desired_rolls))
#print(desired_rolls)
#desired_mod = ''


#def print_data(data):
#    print(data[0], data[1])
#    
#eel.webData()(print_data)
    
#desired_rolls, desired_mod = eel.webData()
#print(desired_rolls, desired_mod)

eel.start('index.html')