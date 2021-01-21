#This section of code is for defining the cantilever distributed load beam.

def cantileverdistbeam(w,L,x,a,b,E,I):
            if(right=='0'):
                supportA=0
                supportB=w*L*-1
                def shear(x):
                    return -1*w*x
                def bending(x):
                    return -1*(w*x**2)/2
                def deflection(x):
                    return(w/(24*E*I))*((x**4)-(4*x*L**3)+(3*L**4))
            elif(right=='1'):
                supportA=0
                supportB=w*-1
                def shear(x):
                    return -1*w*((x**2)/(L**2))
                def bending(x):
                    return -1*(w*x**3)/(3*L**2)
                def deflection(x):
                    return ((w/(60*E*I*L**2))*((x**5)-(5*x*L**4)+(4*L**5)))
            print ('The reaction force at support A is:',round(supportA,5),'kips')
            print ('The reaction force at support B is:',round(supportB,5),'kips')
            print ('The shear force at',x,'inches is:',round(shear(x),5),'kips')
            print ('The bending moment at',x,'inches is:',round(bending(x),5),'kips-in')
            print ('The deflection of the beam at',x,'inches is:',round(deflection(x),5),'inches')
            
 #This section of code is for graphical representation
            
            G=np.arange(0.0,L,0.01)
            plt.subplot(313)
            plt.plot(G,-1*deflection(G),'r')
            plt.plot(G,(G*0),'k')
            plt.xlabel('Length (in.)')
            plt.ylabel('Deflection (in)')
            plt.grid(True)
            plt.fill_between(G,-1*deflection(G),alpha=0.2, hatch = '/')
            plt.subplot(311)
            plt.title('Analysis of your Member')
            plt.plot(G,shear(G),'r')
            plt.plot(G,(G*0),'k')
            plt.ylabel('Shear (kips)')
            plt.grid(True)
            plt.fill_between(G,shear(G),alpha=0.2, hatch = '/')
            plt.subplot(312)
            plt.plot(G,bending(G),'r')
            plt.plot(G,(G*0),'k')
            plt.ylabel('Bending Moment (kips-in)')
            plt.grid(True)
            plt.fill_between(G,bending(G),alpha=0.2, hatch = '/')
            plt.tight_layout()
            plt.show()
            return 
