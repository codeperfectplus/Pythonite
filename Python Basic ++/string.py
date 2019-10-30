names=['jeff','jerry','micky','donald','grinderward']


"""for x in names:
    statement='Hello There '+x
    print(statement)"""

'''when we have to join 2 string we can use .join'''

for x in names:
    statement=' '.join(['Hello There',x])
    print(statement)

print(' , '.join(names))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

who='Jammy'
how_many=12

print('{} bought {} mangoes in morning.'.format(who,how_many))
