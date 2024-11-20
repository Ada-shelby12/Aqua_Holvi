marks={'python':67,'english':87,1:'one'}
print(marks.items())
dictionarykeys=marks.keys()
print('dictionarykeys')
print(marks.values())
print("***update()marks***")
internal_marks={'python-lab':23}
marks.update(internal_marks)
print(marks)
print("***copy()***")
copied_marks=marks.copy()
print('original marks:',marks)
print('copied marks:',copied_marks)      
