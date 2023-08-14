# The project is working on is "Own Assistant" .

# Required imports

import os 

if __name__=='__main__':

    """In the linux does not calculate the space 
       we created the function it replace the space with 
       undersocre.
    """
    def replaceStringWith(input_string):
        return input_string.replace(' ','_')
    
    print("Welcome Master")
    
    # loop itreate until user enter 'q'

    while True:
        x = input("What you wnat to speak:")

        #function call
        #espeak is the commnad that run over terminal.
        x = replaceStringWith(x)
        if x == "q":
            os.system("espeak 'byy byy my friends' ")
            break
        command = f"espeak{x}"
        os.system(command)
