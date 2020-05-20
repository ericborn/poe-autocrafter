'''
Eric Born

18 May 2020


'''
import eel

eel.init('static')

def test_a():
    a=1
    return a
    
def test_b():
    a=0
    return a
    
def test_c():
    a=-1
    return a

#test_list = [test_a, test_b, test_c]

#@eel.expose
#def status_check():
#    for func in [test_a, test_b, test_c]:
#        print(func())
#        return(func())
#    #return(test_list[num]())

@eel.expose
def status_check(num):
    if num == 0:
        return(test_a())
    if num == 1:
        return(test_b())
    if num == 2:
        return(test_c())

#for i in range(3):
#    print(status_check(i))
#status_check(3)

@eel.expose
def roll_function(roll_input, mod_input):
    desired_rolls = roll_input
    desired_mod = mod_input
    print('1', desired_rolls, '\n2', desired_mod)
    return('1', desired_rolls, '\n2', desired_mod)

eel.start('index.html')