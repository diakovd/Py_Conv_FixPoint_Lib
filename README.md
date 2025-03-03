
### FIXPOINT python convertion lib
In DSP FPGA aplication help in convertion  fixpoint <-> floating point 

Function list:

- to_fixed(f,e,nBit) convertion float number to fixpoint number 
	f - float number for convertion
	e - number bit of fractional
	nBit - fixpoint word size, number of bit  

- to_float(x,e,nBit) convertion fixpoint number to float number 
	x - fixpoint number for convertion
	e - number bit of fractional
	nBit - fixpoint word size, number of bit  

- convComlexFixToComplexFloat_fromFile(e,nBit,fnameIn) convertion complex values in fixpoint number ( IM - upper, RE lower part) from file to float comlex list 
	e - number bit of fractional
	nBit - size of IM/RE part, input complex word size - 2\*nBit
	fnameIn - input file name

- convFixToFloat_fromFile(e,nBit,fnameIn) convertion fixpoint numbers from file to float list 
	e - number bit of fractional
	nBit - fixpoint word size, number of bit  
	fnameIn - input file name
	
- convCmplxFloatToCmplxFix(symbs, e, nBit) convertion complex value to fixpoint number in format IM part in upper half, RE part in lower half 
	e - number bit of fractional
	nBit - size of IM/RE part, output complex word size - 2\*nBit
	symbs - compex simbol for convertion

- convFloatToFix(symbs, e, nBit) convertion list float value to fixpoint number 
	e - number bit of fractional
	nBit - output fixpoint word size 
	symbs - float simbol for convertion

- convFixToFloat(symbs,e,nBit) convertion list fix value to float number 
	e - number bit of fractional
	nBit - input fixpoint word size 
	symbs - fix simbol for convertion

- Float_wrFile(data,fnameOut) write list of float to file

- hex_wrFile(data,fnameOut) write list of int in hex format

- read_int(fnameIn) read file with int values 

- read_float(fname) read file with float values 

- read_IQ_to_complex(fname_I, fname_Q) read comlex value from separeit files I and Q, return list of comlex values 