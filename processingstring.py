
#Write code using find() and string slicing (see section 6.10) to
#extract the number at the end of the line below. Convert the extracted
# value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

#find the first space
text_2 = text.find(' ')

#slicing the string to the end
text_3 = text[text_2:]

#strip the string
number = float(text_3)


print(number)
