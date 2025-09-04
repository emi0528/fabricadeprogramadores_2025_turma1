"""
tupla = ("a" , "b" , "c")
tupla
('a', 'b' ,'c')
tupla = 100, 200, 300
tupla
(100, 200, 300)
"""

L=[5,9,13,6,9,10,15,3,2,7,]

for x, e in enumerate(L):
    print(" %d /  %d = %f" % (x,e, x/e))

for x, e in enumerate(L):
    print(" %d /  %d = %d" % (x,e, x*e))

for x, e in enumerate(L):
    print(" %d /  %d = %d" % (x,e, x-e))

for x, e in enumerate(L):
    print(" %d /  %d = %d" % (x,e, x+e))
    

    

