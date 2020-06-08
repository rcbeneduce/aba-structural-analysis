#I call this section of code the brains because this initiates each defining function of the program. Without this section of code, Aba
could not function.

if (loading=='distributed load'):
            if (constraint1=='pinned' and constraint2=='roller' or constraint1=='roller' and constraint2=='pinned'):simpledistbeam(w,L,x,a,b,E,I)
            elif (constraint1=='fixed' and constraint2=='none' or constraint1=='none' and constraint2=='fixed'):cantileverdistbeam(w,L,x,a,b,E,I)
            elif (constraint1=='fixed' and constraint2=='fixed'):fixedfixeddist(w,L,x,a,b,E,I)

        elif(loading=='point load'):        
            if (constraint1=='pinned' and constraint2=='roller' or constraint1=='roller' and constraint2=='pinned'):simplepointbeam(P,L,x,a,b,E,I)
            elif (constraint1=='fixed' and constraint2=='none' or constraint1=='none' and constraint2=='fixed'):cantileverpointbeam(P,L,x,a,b,E,I)
            elif (constraint1=='fixed' and constraint2=='fixed'):fixedfixedpoint(P,L,x,a,b,E,I)
        return
