from Coordinator    import GaussSeidelCoordinator
import coupling
import math


def ObjectiveSimple(x1, y1, y2, z2):
    """
        DESCRIPTION
        ----------
        This script calculates the value of objective function from the 
        given values of design (x1, z1, z2) and intermediate variables (y1, y2)
        
        INPUTS
        ----------
        x1:
        y1:
        y2:
        z2:
        
        OUTPUTS
        ----------
        f:     value of objective function
    """
    
    f = x1**2 + z2 + y1 + math.exp(-y2)
    return f



def ObjectiveMain(x):
    
    """
        DESCRIPTION
        ----------
        This script calculates the value of objective function from the 
        given values of design variables (x1, z1, z2)
        
        INPUTS
        ----------
        x:     array of design variables
        
        OUTPUTS
        ----------
        f:     value of objective function
    """
    
    #print(x)
    
    [x1, z1, z2]    = x
    [y1, y2, _] = GaussSeidelCoordinator(x1, z1, z2, 1)
    
    # send the consistent value of y1 and y2 to coupling
    coupling.y1 = y1
    coupling.y2 = y2
    
    # calculate the value of objective function
    f   = ObjectiveSimple(x1, y1, y2, z2) 
    
    #print('y = ', y1, y2)
    #print('f = ', f)
    return f



def main():
    """
        DESCRIPTION
        ----------
        unit testing         
    """
    
    f =  ObjectiveSimple(1,1,1,1)
    print("f_simple = " + str(f))  
    
    x = [1, 1, 1]
    f =  ObjectiveMain(x)
    print("f_main = " + str(f))   
    print(coupling.y1, coupling.y2)    
    


if __name__ == '__main__':
    main()    