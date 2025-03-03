
# convertion flot number to fixpoint number 
# f - float number for convertion
# nBit - fixpoint word size, number of bit  
def to_fixed(f,e,nBit):
    a = f* (2**e)
    b = int(round(a))
    if a < 0:
        # next three lines turns b into it's 2's complement.
        b = abs(b)
        b = ~b & (2**nBit - 1)
        #b = b + 1
    return b

# convertion fixpoint number to float number 
# x - fixpoint number for convertion
# nBit - fixpoint word size, number of bit  
def to_float(x,e,nBit):
    c = abs(x)
    sign = ((1 << (nBit - 1)) & x) >> (nBit - 1)
    if sign == 1:
        # convert back from two's complement
        c = x - 1
        c = ~c & (2**nBit - 1)
        sign = -1
    else: sign = 1
    f = c / (2 ** e)
    f = f * sign
    return f

# convertion complex value in fixpoint number ( IM - upper, RE lower part) from file to float comlex list 
# e - number bit of fractional
# nBit - size of IM/RE part, input complex word size - 2*nBit
# fnameIn - input file name
def convComlexFixToComplexFloat_fromFile(e,nBit,fnameIn):

    fdataIn= open(fnameIn,"r") 
    data = [(int(line)) for line in fdataIn]
    fdataIn.close() 

    fl_symbs = []
    for n in range(len(data)) : 
        re = to_float(data[n] & (2**nBit - 1), e,nBit )
        im = to_float(data[n] >> nBit, e,nBit) 
        fl_symbs.append(complex(re,im)) 

    return fl_symbs

# convertion fixpoint number from file to float list 
# e - number bit of fractional
# nBit - fixpoint word size, number of bit  
# fnameIn - input file name
def convFixToFloat_fromFile(e,nBit,fnameIn):

    fdataIn= open(fnameIn,"r") 
    data = [(int(line)) for line in fdataIn]
    fdataIn.close() 

    fl_symbs = []
    for n in range(len(data)) : 
        re = to_float(data[n] & (2**nBit - 1), e,nBit )
        fl_symbs.append(re) 

    return fl_symbs

# convertion complex value to fixpoint number in format IM part in upper half, RE part in lower half 
# e - number bit of fractional
# nBit - size of IM/RE part, output complex word size - 2*nBit
# symbs - compex simbol for convertion
def convCmplxFloatToCmplxFix(symbs, e, nBit):
    
    fixp_symbs = []
    for n in range(len(symbs)) : 
        re = to_fixed(symbs[n].real, e, nBit)
        im = to_fixed(symbs[n].imag, e, nBit) << nBit
        fixp_symbs.append(im | re) 

    return fixp_symbs

# convertion list float value to fixpoint number 
# e - number bit of fractional
# nBit - output fixpoint word size 
# symbs - float simbol for convertion
def convFloatToFix(symbs, e, nBit):
    
    fixp_symbs = []
    for n in range(len(symbs)) : 
        re = to_fixed(symbs[n].real, e, nBit)
        fixp_symbs.append(re) 
    return fixp_symbs

# convertion list fix value to float number 
# e - number bit of fractional
# nBit - input fixpoint word size 
# symbs - fix simbol for convertion
def convFixToFloat(symbs,e,nBit):
    
    float_symbs = []
    for n in range(len(symbs)) : 
        re = to_float(symbs[n].real, e, nBit)
        float_symbs.append(re) 
    return float_symbs                                            
# write list of float to file
def Float_wrFile(data,fnameOut):
    fout = open(fnameOut,"w") 

    [fout.write( '%f\n' % d ) for d in data]  

    fout.close()

# write list of int in hex format
def hex_wrFile(data,fnameOut):
    fout = open(fnameOut,"w") 

    [fout.write( '%x\n' % d ) for d in data]  

    fout.close()

# read file with int values 
def read_int(fnameIn):
    fdataIn= open(fnameIn,"r") 
    data = [(int(line)) for line in fdataIn]
    fdataIn.close() 

    return data

# read file with float values 
def read_float(fname):
    fdataIn= open(fname,"r") 
    symbs = [float(line) for line in fdataIn]
    fdataIn.close() 

    return symbs

# read comlex value from separeit files I and Q, return list of comlex values 
def read_IQ_to_complex(fname_I, fname_Q):
    fdataIn= open(fname_I,"r") 
    data_I = [(line) for line in fdataIn]
    fdataIn.close() 

    fdataIn= open(fname_Q,"r") 
    data_Q = [(line) for line in fdataIn]
    fdataIn.close() 


    symbs = []

    for i in range(len(data_I)):
        symbs.append(complex(float(data_I[i]),float(data_Q[i])))
        
    return symbs

# check two list for identify 
# data - list for check
# ref_data - list with expected values
# typeComplex - type of values : true - complex/float type, false - int type
# precision - for float/complex values, if difference betwin vales will more than 0.001 (for exampl), this set error of compartion 
def check_data(data,ref_data,typeComplex,precision):
    check = 0
    err = 0
    checkAll = []
    err_num = []

    for i in range(len(ref_data)):
        check = data[i] - ref_data[i]
        checkAll.append(check)
        
        if typeComplex : 
            if abs(check.real) > precision or abs(check.imag) > precision : 
                err = err + 1
                err_num.append(i)
        else:
            if abs(check) > precision : 
                err = err + 1
                err_num.append(i)
    return err

#a = 0xf9cf6a
#b = 0xf351

#summ = add_16bit_signed(a, b)
# Example usage
#a = 10
#b = -5
#result = add_16bit_signed(a, b)
#print(result)  # Output: 5
#b = - 1/math.sqrt(2)
#c = to_fixed((1/(2*839)),64,64)
#c = to_fixed(math.sqrt(2),28,32)
#c= to_float(32439640301457, 60, 64)
#print(hex(c))
#print(hex(c))
