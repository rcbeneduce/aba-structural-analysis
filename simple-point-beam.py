#This is the code for defining the simply supported beam problem with a point load

def simplepointbeam(P,L,x,a,b,E,I):
            if (a==L/2):
                supportA= P/2
                supportB= -P/2
                def shear(x):
                    return P/2
                if (x<=a):
                    def bending(x):
                        return P*x/2
                    def deflection(x):
                        return (P/(48*E*I))*((4*x**3)-(3*x*L**2))*-1
                else:
                    def bending(x):
                        return (P/2)*(-x+(L/2))
                    def deflection(x):
                        return (P/(48*E*I))*(4*(L-x)**3-(3*(L-x)*L**2))*-1
            else:
                supportA= P*b/L
                supportB= -P*a/L
                if (x<=a):
                    def shear(x):
                        return P*b/L
                    def bending(x):
                        return P*b*x/L
                    def deflection(x):
                        return((P*b)/(6*E*I*L))*((x**3)+(x*b**2)-(x*L**2))*-1
                elif (x>a):
                    def shear(x):
                        return P*a/L
                    def bending(x):
                        return (P*(-a-(b*x)/L+x))*-1
                    def deflection(x):
                        return(((P*a)*(L-x))/(6*E*I*L))*((x**2)+(a**2)-(2*L*x))*-1   
            print ('The reaction force at support A is:',round(supportA,5),'kips')
            print ('The reaction force at support B is:',round(supportB,5),'kips')
            print ('The shear force at',x,'inches is:',round(shear(x),5),'kips')
            print ('The bending moment at',x,'inches is:',round(bending(x),5),'kips-in')
            print ('The deflection of the beam at',x,'inches is:',round(deflection(x),5),'inches')
            
 #the below section of code is for graphical representation
            
            G=np.arange(0.0,L,0.01)
            Gp=np.arange(0.0,a,0.01)
            Gn=np.arange(a,L,0.01)
            Glp=np.arange(0.0,(L/2),0.01)
            Gln=np.arange((L/2),L,0.01)
            Sxp=[0,a]
            Sxn=[a,L]
            Smx=[a,a]
            if (a==L/2):
                Syp=[shear(x),shear(x)]
                Syn=[supportB,supportB]
                Smy=[shear(x),-shear(x)]
                def Bn(x):
                    return(P/2)*(-x+(L/2))
                def Bp(x):
                    return P*x/2
                def Dp(x):
                    return((P/(48*E*I))*((4*x**3)-(3*x*L**2)))
                def Dn(x):
                    return(P/(48*E*I))*(4*(L-x)**3-(3*(L-x)*L**2))
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
                plt.plot(Glp,Bp(Glp),Gln,Bn(Glp),'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Bending Moment (kips-in)')
                plt.grid(True)
                plt.fill_between(Glp,Bp(Glp),alpha=0.2, hatch = '/')
                plt.fill_between(Gln,Bn(Glp),alpha=0.2, hatch = '/')
                plt.tight_layout()
                plt.show()
            else:
                Syp=[shear(x),shear(x)]
                Syn=[supportB,supportB]
                Smy=[shear(x),supportB]
                def Bn(x):
                    return (P*(-a-(b*x)/L+x))*-1
                def Bp(x):
                    return P*b*x/L
                def Dp(x):
                    return((P*b)/(6*E*I*L))*((x**3)+(x*b**2)-(x*L**2))
                def Dn(x):
                    return(((P*a)*(L-x))/(6*E*I*L))*((x**2)+(a**2)-(2*L*x))
                plt.subplot(313)
                plt.plot(Gp,np.squeeze(Dp(Gp)),'r')
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
                plt.fill_between(Sxn,Syn,alpha=0.2, hatch = '/')
                plt.subplot(312)
                plt.plot(Gp,np.squeeze(Bp(Gp)),'r')
                plt.plot(Gn,np.squeeze(Bn(Gn)),'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Bending Moment (kips-in)')
                plt.grid(True)
                plt.fill_between(Gp,Bp(Gp),alpha=0.2, hatch = '/')
                plt.fill_between(Gn,Bn(Gn),alpha=0.2, hatch = '/')
                plt.tight_layout()
                plt.show()
            return
        
