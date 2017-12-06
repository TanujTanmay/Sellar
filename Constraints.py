import coupling

def Constraint1(x):
    """
        DESCRIPTION
        ----------
        Constraint1 of the Sellar Problem.
        
        INPUTS
        ----------
        x:        array of design variables
        
        OUTPUTS
        ----------
        c_ineq:   value of inequality constraint  
    """
    
    c_ineq  = 3.16 - coupling.y1
    #print('C1', c_ineq)
    return c_ineq




def Constraint2(x):
    """
        DESCRIPTION
        ----------
        Constraint2 of the Sellar Problem.
        
        INPUTS
        ----------
        x:        array of design variables
        
        OUTPUTS
        ----------
        c_ineq:   value of inequality constraint  
    """
    
    c_ineq  = coupling.y2 - 24
    #print('C2', c_ineq)
    return c_ineq





def main():
    """
        DESCRIPTION
        ----------
        unit testing         
    """
    
    c_ineq1 =  Constraint1(0)
    print("c_ineq1 = " +  str(c_ineq1))
    
    c_ineq2 =  Constraint2(0)
    print("c_ineq2 = " +  str(c_ineq2))
    
    

if __name__ == '__main__':
    main()    