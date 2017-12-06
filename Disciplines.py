import math

def Discipline1(x1, y2, z1, z2):
    """
        DESCRIPTION
        ----------
        Discipline1 of the Sellar Problem.
        
        INPUTS
        ----------
        x1:
        y2:
        z1:
        z2:
        
        OUTPUTS
        ----------
        y1:
    """
    
    y1 = z1**2 + x1 + z2 - 0.2*y2
    return y1



def Discipline2(y1, z1, z2):
    """
        DESCRIPTION
        ----------
        Discipline2 of the Sellar Problem.
        
        INPUTS
        ----------
        y1:
        z1:
        z2:
        
        OUTPUTS
        ----------
        y2:
    """
    
    y2 = math.sqrt(abs(y1)) + z1 + z2
    return y2
    
    


def main():
    """
        DESCRIPTION
        ----------
        unit testing         
    """
    
    y1 =  Discipline1(1,1,1,1)
    print("y1 = " + str(y1)) 
    
    y2 =  Discipline2(1,1,1)
    print("y2 = " + str(y2))   
    


if __name__ == '__main__':
    main()    