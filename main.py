import cmath, math, numpy
def addComplex( z1, z2):
    return z1 + z2
def subComplex(z1, z2):
  return z1-z2
z1 = complex(2, 3)
z2 = complex(1, 2)
print( "Addition is : ", addComplex(z1, z2))
Addition is :  (3+5j)
z1= complex(2,3)
z2= complex(1,2)
print("substraction is: ", subComplex(z1,z2))
substraction is:  (1+1j)
z = complex(2,5)
print(" conjugate is: ", z.conjugate())
 conjugate is:  (2-5j)
c = 4+ 4j
# phase
phase = cmath.phase(c)
print('4+ 4j Phase =', phase)
print('Phase in Degrees =', numpy.degrees(phase))
print('-4-4j Phase =', cmath.phase(-4-4j), 'radians. Degrees =', numpy.degrees(cmath.phase(-4-4j)))
# we can get phase using math.atan2() function too
print('Complex number phase using math.atan2() =', math.atan2(2, 1))
4+ 4j Phase = 0.7853981633974483
Phase in Degrees = 45.0
-4-4j Phase = -2.356194490192345 radians. Degrees = -135.0
Complex number phase using math.atan2() = 1.1071487177940904
