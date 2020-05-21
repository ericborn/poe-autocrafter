'''
Eric Born

18 May 2020


'''
import eel
from checks import check_for_mod as mod, inv_stash_check as isc, \
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


@eel.expose
def roll_function(roll_number, desired_mod):
    #for i in range(roll_number):
    roll_item(roll_number, desired_mod)
    #print('1', desired_rolls, '\n2', desired_mod)
    #return('1', desired_rolls, '\n2', desired_mod)
 
    
    
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