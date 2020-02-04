a_string = 'this is\na string split\t\t and tabbed'
print(a_string)

raw_string = r"this is\na string split\t\t and tabbed"
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backlash_string = "This is a backlash \\followed by text"
print(backlash_string)