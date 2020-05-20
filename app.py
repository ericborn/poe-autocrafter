'''
Eric Born

18 May 2020


'''
import eel

eel.init('static')

def test_a():
    a=1
    return(a, 1)
    
def test_b():
    a=0
    return(a, 2)
    
def test_c():
    a=-1
    return(a, 3)

test_list = [test_a, test_b, test_c]

@eel.expose
def status_check(num):
    return(test_list[num]())

#status_check(2)

#for func in [test_a, test_b, test_c]:
#    print(func())
#    result = func()
    
@eel.expose
def roll_function(roll_input, mod_input):
    desired_rolls = roll_input
    desired_mod = mod_input
    print('1', desired_rolls, '\n2', desired_mod)
    return('1', desired_rolls, '\n2', desired_mod)

eel.start('index.html')