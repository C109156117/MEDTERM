student= set(['John', 'Mary', 'Tina', 'Fiona', 'Claire', 'Eva', 'Ben', 'Bill', 'Bert'])
eng= set(['John', 'Mary', 'Fiona', 'Claire', 'Ben', 'Bill'])
math = set(['Mary', 'Fiona', 'Claire', 'Eva', 'Ben']) 
print('英文及數學都及格:',eng&math)
print("數學不及格:",student^math)
print("英文及格且數學不及格:",eng&(student^math))