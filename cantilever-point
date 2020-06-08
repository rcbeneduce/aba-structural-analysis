#This is the code for defining the cantilever beam

def cantileverpointbeam(P,L,x,a,b,E,I):
            if (a==0):
                supportA=0
                supportB=-1*P
                def shear(x):
                    return -1*P
                def bending(x):
                    return -1*P*x
                def deflection(x):
                    return(P/(6*E*I))*((2*L**3)-(3*x*L**2)+x**3)
            elif (x<=a):
                supportA=0
                supportB=-1*P
                def deflection(x):
                    return (P*b**2)/(6*E*I)*(3*L-3*x-b)
                def shear(x):
                    return 0
                def bending(x):
                    return 0
            elif (x>a):
                supportA=0
                supportB=-1*P
                def deflection(x):
                    return(P*(L-x)**2)/(6*E*I)*(3*b-L+x)
                def shear(x):
                    return-1*P
                def bending(x):
                    return P*(x-a)*-1
            print ('The reaction force at support A is:',round(supportA,5),'kips')
            print ('The reaction force at support B is:',round(supportB,5),'kips')
            print ('The shear force at',x,'inches is:',round(shear(x),5),'kips')
            print ('The bending moment at',x,'inches is:',round(bending(x),5),'kips-in')
            print ('The deflection of the beam at',x,'inches is:',round(deflection(x),5),'inches')

#This is the graphical representation section of code

            G=np.arange(0.0,L,0.01)
            Gp=np.arange(0.0,a,0.01)
            Gn=np.arange(a,L,0.01)
            Sxp=[0,L]
            Sxn=[a,L]
            Syp=[shear(x),shear(x)]
            if (a==0):
                plt.subplot(313)
                plt.plot(G,deflection(G)*-1,'r')
                plt.plot(G,(G*0),'k')
                plt.xlabel('Length (in.)')
                plt.ylabel('Deflection (in)')
                plt.grid(True)
                plt.fill_between(G,deflection(G)*-1,alpha=0.2, hatch = '/')
                plt.subplot(311)
                plt.title('Analysis of your Member')
                plt.plot(Sxp,Syp,'r')
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
            else:
                def Bn(x):
                    return P*(x-a)*-1
                def Dp(x):
                    return(P*b**2)/(6*E*I)*(3*L-3*x-b)*-1
                def Dn(x):
                    return(P*(L-x)**2)/(6*E*I)*(3*b-L+x)*-1
                Sn=[-P,-P]
                plt.subplot(313)
                plt.plot(Gp,Dp(Gp),'r')
                plt.plot(Gn,np.squeeze(Dn(Gn)),'r')
                plt.plot(G,(G*0),'k')
                plt.xlabel('Length (in.)')
                plt.ylabel('Deflection (in)')
                plt.grid(True)
                plt.fill_between(Gp,Dp(Gp),alpha=0.2, hatch = '/')
                plt.fill_between(Gn,np.squeeze(Dn(Gn)),alpha=0.2, hatch = '/')
                plt.subplot(311)
                plt.title('Analysis of your Member')
                plt.plot(Sxn,Sn,'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Shear (kips)')
                plt.grid(True)
                plt.fill_between(Sxn,Sn,alpha=0.2, hatch = '/')
                plt.subplot(312)
                plt.plot(Gn,np.squeeze(Bn(Gn)),'r')
                plt.plot(G,(G*0),'k')
                plt.ylabel('Bending Moment (kips-in)')
                plt.grid(True)
                plt.fill_between(Gn,np.squeeze(Bn(Gn)),alpha=0.2, hatch = '/')
                plt.tight_layout()
                plt.show()
            return 
