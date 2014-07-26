from pylab import *
import vlspgm

def runit():
    LEG = [70.00, 0.03838, 2.8e-6, 0.0] # CSX-1
    R = [40500.0, 14000.0] #CSX-1
    E = 640.0 # arange(200.0, 1200.0, 0.1)
    lam = vlspgm.hc_over_e / E
    c,p = vlspgm.calcC(LEG, R, lam, True)
    print c, p
    #plot(E, c)
    alp, beta = vlspgm.calcAngles(LEG, c, lam)
    print 'Mirror =',90 - vlspgm.deg(alp)
    print 'Grating =',90 - vlspgm.deg(beta)

if __name__ == "__main__":
    runit()
    show()
