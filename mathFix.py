import math

def add_signed(a,b, size):
    overflow = 0
    msb = 2**(size - 1)
    result = (a + b) & (2**size - 1)
    a_msb = (a &  msb) >> size - 1 
    b_msb = (b &  msb) >> size - 1
    res_msb = (result & msb) >> size - 1
    if ( (not a_msb) and (not b_msb) and res_msb) or ( a_msb and b_msb and (not res_msb) ) :
        print('ERROR - overflow fix point signed addition')
        overflow = 1
    return result, overflow

def sub_signed(a,b, size):
    overflow = 0
    msb = 2**(size - 1)
    result = (a - b) & (2**size - 1)
    a_msb = (a &  msb) >> size - 1 
    b_msb = (b &  msb) >> size - 1
    res_msb = (result & msb) >> size - 1
    if ( (not a_msb) and ( b_msb) and res_msb) or (  a_msb and (not b_msb) and (not res_msb) ) :
        print('ERROR - overflow fix point signed substraction')
        overflow = 1
    return result, overflow

def div_signed(a,b, e, nbit):
    a_msb = (a &   2**(nbit - 1)) >> nbit - 1 
    b_msb = (b &   2**(nbit - 1)) >> nbit - 1
    if(a_msb) : a_abc =( ~a & (2**nbit - 1) )<< e 
    else : a_abc = a << e  

    if(b_msb) : b_abc = ~b & (2**nbit - 1)  
    else : b_abc = b 
    
    div  = math.floor(a_abc/b_abc) 
    sign = a_msb ^ b_msb    

    if(sign) : result = ~div & (2**(2*nbit) - 1) 
    else : result = div 

    return result

def mult_signed(a,b, e, nbit):
    a_msb = (a &   2**(nbit - 1)) >> nbit - 1 
    b_msb = (b &   2**(nbit - 1)) >> nbit - 1
    if(a_msb) : a_abc =( ~a & (2**nbit - 1) )
    else : a_abc = a 

    if(b_msb) : b_abc = ~b & (2**nbit - 1)  
    else : b_abc = b 
    
    mult  = a_abc * b_abc 
    sign = a_msb ^ b_msb    

    if(sign) : result = ~mult & (2**(2*nbit) - 1) 
    else : result = mult 

    return result

def add(a,b, size):
    overflow = 0
    msb = 2**size
    result = (a + b) 

    if (result & msb) >> size - 1 :
        print('ERROR - overflow fix point addition')
        overflow = 1
    result = result & (2**size - 1)
    return result, overflow

def sub(a,b, size):
    overflow = 0
    msb = 2**size
    result = (a - b)

    if (result & msb) >> size - 1 :
        print('ERROR - overflow fix point substraction')
        overflow = 1
    result = result & (2**size - 1)
    return result, overflow

def div(a,b, e):
    a_shift = a << e  
    
    div  = math.floor(a_shift/b) 

    return div

def mult(a,b):

    mult  = a * b 

    return mult
