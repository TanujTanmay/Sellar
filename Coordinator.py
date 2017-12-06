from Disciplines    import Discipline1, Discipline2

def GaussSeidelCoordinator(x1, z1, z2, y2_old):
    
    """
        DESCRIPTION
        ----------
        This script coordinates the value of y1 & y2 until they converge
        to the values consistent with the definition of the Sellar problem
        
        INPUTS
        ----------
        x1:
        z1:
        z2:
        y2_old:     initial estimate of the value of y2
        
        OUTPUTS
        ----------
        y1:         final value of y1 that is consistent with x1, z1 and z2
        y2:         final value of y2 that is consistent with x1, z1 and z2
    """
    
    tolerance   = 1.0e-6
    y2          = 1.0e6
    counter     = 0
    
    while abs(y2 - y2_old)/y2 > tolerance:
        
        if counter > 0:
            y2_old = y2
            
        y1 = Discipline1(x1, y2_old, z1, z2)    
        y2 = Discipline2(y1, z1, z2)
        counter += 1
        
    return [y1, y2, counter]     





def main():
    """
        DESCRIPTION
        ----------
        unit testing         
    """
    
    res =  GaussSeidelCoordinator(1,1,1,1)
    print(res) 
    


if __name__ == '__main__':
    main()    
    