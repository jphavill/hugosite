import re
line = 'this a test <code>12 = 1 + 2 if int str'
line2 = 'ab2aa2'
line2 = re.sub(r"[0-9]", r"test", line2)
#line = re.sub(r"(<code>.*?)(\b([0-9]+)\b)", r"\1<span class='number'>\2</span>", line)
# line = re.sub(r"(<code>.*?)(\b(print|int|str|chr|list|tuple|set|dict|quit|enumerate|range)\b)", r"\1<span class='nativeFunc'>\2</span>", line)
line = re.sub(r"(<code>.*?)([0-9])", r"\1<span class='number'>\2</span>", line)
print(line2)




# test regex for a number at the beginnning middle and end of string