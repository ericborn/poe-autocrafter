'''
Eric Born

18 May 2020


'''
import eel

eel.init('static')

@eel.expose
def roll_function(roll_input, mod_input):
    desired_rolls = roll_input
    desired_mod = mod_input
    print('1', desired_rolls, '\n2', desired_mod)
    return('1', desired_rolls, '\n2', desired_mod)

eel.start('index.html')