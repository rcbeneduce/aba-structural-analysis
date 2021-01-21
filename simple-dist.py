#This section of code is for defining the simply span beam of a distributed load

def simpledistbeam(w,L,x,a,b,E,I):
            if(complex2=='1'):
                supportA=w*L/2
                supportB=w*L/2*-1
                def shear(x):
                    return w*((L/2)-x)
                def bending(x):
                    return(w*x/2)*(L-x)
                def deflection(x):
                    return((w*x)/(24*E*I))*((L**3)-(2*L*x**2)+(x**3))
            elif(right=='1'):
                supportA=w/3
                supportB=2*w/3*-1
                def shear(x):
                    return(w/3)-((w*x**2)/L**2)
                def bending(x):
                    return(w*x)/(3*L**2)*((L**2)-(x**2))
                def deflection(x):
                    return((w*x)/(180*E*I*L**2))*((3*x**4)-(10*L**2*x**2)+(7*L**4))
            elif(right=='0'):
                supportA=w/2
                supportB=w/2*-1
                if (x<=(L/2)):
                    def shear(x):
                        return(w/(2*L**2))*((L**2)-(4*x**2))
                    def bending(x):
                        return w*x*(0.5-((2*x**2)/(3*L**2)))
                    def deflection(x):
                        return((w*x)/(480*E*I*L**2))*((5*L**2)-(4*x**2))**2
                elif(x>(L/2)):
                    def shear(x):
                        return (w/(2*L**2))*((L**2)-(4*(L-x)**2))
                    def bending(x):
                        return w*(L-x)*(0.5-((2*(L-x)**2)/(3*L**2)))
                    def deflection(x):
                        return ((w*(L-x))/(480*E*I*L**2))*((5*L**2)-(4*(L-x)**2))**2
            print ('The reaction force at support A is:',round(supportA,5),'kips')
            print ('The reaction force at support B is:',round(supportB,5),'kips')
            print ('The shear force at',x,'inches is:',round(shear(x),5),'kips')
            print ('The bending moment at',x,'inches is:',round(bending(x),5),'kips-in')
            print ('The deflection of the beam at',x,'inches is:',round(deflection(x),5),'inches')
            
#This section of code is for graphical representation.
            
            G=np.arange(0.0,L,0.01)
            P=np.arange(0.0,(L/2),0.01)
            N=np.arange((L/2),L,0.01)
            if (complex=='no' or right=='1'):
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
            elif(right=='0'):
                def Sp(x):
                    return(w/(2*L**2))*((L**2)-(4*x**2))
                def Sn(x):
                    return(w/(2*L**2))*((L**2)-(4*(L-x)**2))*-1
                def Mp(x):
                    return w*x*(0.5-((2*x**2)/(3*L**2)))
                def Mn(x):
                    return w*(L-x)*(0.5-((2*(L-x)**2)/(3*L**2)))
                def Dp(x):
                    return((w*x)/(480*E*I*L**2))*((5*L**2)-(4*x**2))**2*-1
                def Dn(x):
                    return((w*(L-x))/(480*E*I*L**2))*((5*L**2)-(4*(L-x)**2))**2*-1
                plt.subplot(313)
                plt.plot(P,Dp(P),'r')
                plt.plot(N,Dn(N),'r')
                plt.xlabel('Length (in.)')
                plt.ylabel('Deflection (in)')
                plt.grid(True)
                plt.plot(G,(G*0),'k')
                plt.fill_between(P,Dp(P),alpha=0.2, hatch = '/')
                plt.fill_between(N,Dn(N),alpha=0.2, hatch = '/')
                plt.subplot(311)
                plt.plot(P,Sp(P),'r')
                plt.plot(N,Sn(N),'r')
                plt.title('Analysis of your Member')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Shear (kips)')
                plt.grid(True)
                plt.fill_between(P,Sp(P),alpha=0.2, hatch = '/')
                plt.fill_between(N,Sn(N),alpha=0.2, hatch = '/')
                plt.subplot(312)
                plt.plot(P,Mp(P),'r')
                plt.plot(N,Mn(N),'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Bending Moment (kips-in)')
                plt.grid(True)
                plt.fill_between(P,Mp(P),alpha=0.2, hatch = '/')
                plt.fill_between(N,Mn(N),alpha=0.2, hatch = '/')
                plt.tight_layout()
                plt.show()
            return
