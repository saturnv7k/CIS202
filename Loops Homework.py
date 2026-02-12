#starting values
muffin = 10
cupcake = 10

#purchase loop
while True:
    purchase = (input('Please enter your desired purchase: '))

    if purchase == '0':
        break
    if purchase == 'muffin':
        if muffin > 0:
            muffin -= 1
        else:
            print('Out of stock')

    elif purchase == 'cupcake':
        if cupcake > 0:
            cupcake -= 1
        else:
            print('Out of stock')

#end item values
print('Muffins: ', muffin)
print('Cupcakes: ', cupcake)
