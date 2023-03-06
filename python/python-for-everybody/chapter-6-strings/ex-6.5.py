str = 'X-DSPAM-Confidence: 0.8475    '

ipos = str.find(':') # returns index of `:` in the defined string 
piece = float(str[ipos+1:]) #don't have to call .strip(); float strips off the white space
print(piece)