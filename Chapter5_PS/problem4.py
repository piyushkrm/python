'''Question 4 : What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations? '''

se = set()
se.add(20)
se.add(20.0)
se.add('20') 
print(len(se))          #output is 2 because in python 20 == 20.0 is equal. python compare value and values are same then don't yhink about data type so output is 2 is True
print(se)
