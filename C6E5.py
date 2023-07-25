# P4E - Chapter 6, Exercise 5

str = 'X-DSPAM-Confidence:0.8475'

novaStr = str[(str.find(":") + 1):]
novaStr = float(novaStr)
print(novaStr)
print(type(novaStr))