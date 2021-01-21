import matplotlib.pyplot as plt 
import numpy as np

def structuralanalysis(t):
    def UX(q):
        loading= input('Is there a point load or distributed load?')
        complex= input('Is there complex loading?')
        if complex=='no':
            complex2='1'
            right='0'
        elif complex=='yes':
            complex2= input('Is the complex load triangular?')
            if complex2=='yes':
                triangle=input('What type of triangle describes the loading... isosceles or right?')
                w=float(input('What is the total load on beam of the triangular loading in kips?'))
                if triangle==('right'):right='1'
                elif triangle==('isosceles'):right='0'
                else:
                    print('Program error, please try again')
                    UX(1)
        else:
            print('Spelling error please retry program')
            UX(1)
        if (loading=='point load'):
            P=float(input('What is the point load in kips?'))
        elif (loading=='distributed load'):
            if complex2=='yes':
                pass
            else:
                w=float(input('What is the distributed load in kips/in?'))
                w1='1'
        else:
            print('Spelling error, please retry program')
            UX(1)
        constraint1= input('Describe the constraints on support A.')
        if (constraint1=='fixed' or constraint1=='pinned' or constraint1=='roller' or constraint1=='none'): pass
        else:
            print('Support type error, please try again')
            UX(1)
        constraint2= input('Describe the constraints on support B.')
        if (constraint2=='fixed' or constraint2=='pinned' or constraint2=='roller' or constraint2=='none'):pass
        else:
            print('Support type error, please try again')
            UX(1)
        I=float(input('What is the moment of inertia (I), in^4?'))
        if I==str:
            print('Program error, please try again')
            UX(1)
        E=float(input('What is the modulus of elasticity (E), ksi?'))
        if E==str:
            print('Program error, please try again')
            UX(1)
        L=float(input('What is the length of the span in inches?'))
        x=float(input('Where is the desired location on the beam for analysis purposes, from the left constraint, inches?'))
        a=float(input('What is the location of the loading respective to the left constraint?'))
        b=float(input('What is the location of the loading respective to the right constraint?'))
