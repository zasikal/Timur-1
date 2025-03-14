import re
#1
txt = input()
if re.fullmatch("ab*", txt):
 print ("matches the pattern", '\n')
else:
 print ("doesn't match", '\n')
#2
txt = input()
if re.fullmatch("ab{2,3}", txt):
 print ("matches the pattern", '\n')
else:
 print ("doesn't match", '\n')
#3
txt = input()
if re.fullmatch(r"[a-z]+(_[a-z]+)+", txt):
 print ("matches the pattern", '\n')
else:
 print ("doesn't match", '\n')
#4
txt = input()
if re.fullmatch(r"[A-Z][a-z]+", txt):
 print ("matches the pattern", '\n')
else:
 print ("doesn't match", '\n')
#5
txt = input()
if re.fullmatch(r"^a.*b$", txt):
 print ("matches the pattern", '\n')
else:
 print ("doesn't match", '\n')
#6
txt = input()
txt2 = re.sub(r"[ .,]", ":", txt)
print (txt2)
#7
txt = input()
print(re.sub(r'_([a-z])', lambda m: m.group(1).upper(), txt))
#8, 9
txt = input()
a = re.findall(r"[A-Z][^A-Z]*",txt)
print (a)
#10
txt= input()
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)).lower())