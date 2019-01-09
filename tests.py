import turtle as t 

def writePos(x,y):
    t.goto(x,y)
    t.write("("+ str(x) + "," + str(y) + ")") 
    return 

def main(): 
    s = t.getscreen() 
    s.onclick(writePos)

main() 
