#This section of code is for defining the fixed-fixed point load beam.

def fixedfixedpoint(P,L,x,a,b,E,I):
            if (a==L/2):
                supportA= P/2
                supportB= -P/2
                def shear(x):
                    return P/2
                if (x<=a):
                    def bending(x):
                        return(P/8)*((4*x)-L)
                    def deflection(x):
                        return((P*x**2)/(48*E*I))*(3*L-4*x)
                else:
                    def bending(x):
                        return (P/8)*((4*(L-x))-L)
                    def deflection(x):
                        return((P*(L-x)**2)/(48*E*I))*(3*L-4*(L-x))
            elif (x<=a):
                supportA=(P*b**2)/(L**3)*(3*a+b)
                supportB=-(P*a**2)/(L**3)*(3*b+a)
                def deflection(x):
                    return(P*b**2*x**2)/(6*E*I*L**3)*(3*a*L-3*a*x-b*x)
                def shear(x):
                    return P*b**2/L**3*(3*a+b)
                def bending(x):
                    return (supportA*x)-(P*a*b**2)/(L**2)
            elif (x>a):
                supportA=(P*b**2)/L**3*(3*a+b)
                supportB=-P*a**2/L**3*(3*b+a)
                def deflection(x):
                    return(P*a**2*(b-(x-a))**2)/(6*E*I*L**3)*(3*b*L-3*b*(b-(x-a))-a*(b-(x-a)))
                def shear(x):
                    return P*a**2/L**3*(3*b+a)
                def bending(x):
                    return(((P*a*b**2)/L**2)-P*a-((P*x*b**2)/(L**3))*(3*a+b)+P*x)*-1
            print ('The reaction force at support A is:',round(supportA,5),'kips')
            print ('The reaction force at support B is:',round(supportB,5),'kips')
            print ('The shear force at',x,'inches is:',round(shear(x),5),'kips')
            print ('The bending moment at',x,'inches is:',round(bending(x),5),'kips-in')
            print ('The deflection of the beam at',x,'inches is:',round(deflection(x),5),'inches')
            
#This section of code is for graphical representation.
            
            G=np.arange(0.0,L,0.01)
            Gp=np.arange(0.0,a,0.01)
            Gn=np.arange(a,L,0.01)
            Gx=np.arange(0.0,b,0.01)
            Sxp=[0,a]
            Sxn=[a,L]
            if (a==L/2):
                Syp=[shear(x),shear(x)]
                Syn=[supportB,supportB]
                Smx=[a,a]
                Smy=[shear(x),-shear(x)]
                def Bn(x):
                    return(P/8)*((4*(L-x))-L)
                def Bp(x):
                    return(P/8)*((4*x)-L)
                def Dp(x):
                    return((P*x**2)/(48*E*I))*(3*L-4*x)*-1
                def Dn(x):
                    return((P*(L-x)**2)/(48*E*I))*(3*L-4*(L-x))*-1
                plt.subplot(313)
                plt.plot(Gp,Dp(Gp),'r')
                plt.plot(Gn,Dn(Gn),'r')
                plt.plot(G,(G*0),'k')
                plt.xlabel('Length (in.)')
                plt.ylabel('Deflection (in)')
                plt.grid(True)
                plt.fill_between(Gp,Dp(Gp),alpha=0.2, hatch = '/')
                plt.fill_between(Gn,Dn(Gn),alpha=0.2, hatch = '/')
                plt.subplot(311)
                plt.title('Analysis of your Member')
                plt.plot(Sxp,Syp,Sxn,Syn,Smx,Smy,'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Shear (kips)')
                plt.grid(True)
                plt.fill_between(Sxp,shear(x),alpha=0.2, hatch = '/')
                plt.fill_between(Sxn,-shear(x),alpha=0.2, hatch = '/')
                plt.subplot(312)
                plt.plot(Gp,Bp(Gp),Gn,Bn(Gn),'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Bending Moment (kips-in)')
                plt.fill_between(Gp,Bp(Gp),alpha=0.2, hatch = '/')
                plt.fill_between(Gn,Bn(Gn),alpha=0.2, hatch = '/')
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            else:
                Syp=[shear(x),shear(x)]
                Syn=[supportB,supportB]
                Smx=[a,a]
                Smy=[shear(x),supportB]
                def Bn(x):
                    return(((P*a*b**2)/L**2)-P*a-((P*x*b**2)/(L**3))*(3*a+b)+P*x)*-1
                def Bp(x):
                    return supportA*x-P*a*b**2/L**2
                def Dp(x):
                    return(P*b**2*x**2/6*E*I*L**3)*(3*a*L-3*a*x-b*x)*-1
                def Dn(x):
                    return(P*a**2*(b-x)**2/6*E*I*L**3)*(3*b*L-3*b*(b-x)-a*(b-x))*-1
                plt.subplot(313)
                plt.plot(Gp,Dp(Gp),'r')
                plt.plot(Gn,np.squeeze(Dn(Gx)),'r')
                plt.plot(G,(G*0),'k')
                plt.xlabel('Length (in.)')
                plt.ylabel('Deflection (in)')
                plt.grid(True)
                plt.fill_between(Gp,Dp(Gp),alpha=0.2, hatch = '/')
                plt.fill_between(Gn,Dn(Gx),alpha=0.2, hatch = '/')
                plt.subplot(311)
                plt.title('Analysis of your Member')
                plt.plot(Sxp,Syp,Sxn,Syn,Smx,Smy,'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Shear (kips)')
                plt.grid(True)
                plt.fill_between(Sxp,shear(x),alpha=0.2, hatch = '/')
                plt.fill_between(Sxn,Syn,alpha=0.2, hatch = '/')
                plt.subplot(312)
                plt.plot(Gp,Bp(Gp),Gn,np.squeeze(Bn(Gn)),'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Bending Moment (kips-in)')
                plt.fill_between(Gp,Bp(Gp),alpha=0.2, hatch = '/')
                plt.fill_between(Gn,np.squeeze(Bn(Gn)),alpha=0.2, hatch = '/')
                plt.grid(True)
                plt.tight_layout()
                plt.show()
            return
