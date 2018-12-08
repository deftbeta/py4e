text = "X-DSPAM-Confidence:    0.8475";
findletter = text.find(':')
startslice = findletter+1
print(float(text[startslice:]))
