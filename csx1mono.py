from pylab import *
import vlspgm

def runit():
    LEG = [70.00, 0.03838, 2.8e-6, 0.0] # CSX-1
    R = [40500.0, 14000.0] #CSX-1
    E = 520 # arange(200.0, 1200.0, 0.1)
    lam = vlspgm.hc_over_e / E
    c,p = vlspgm.calcC(LEG, R, lam, True)
    print "c = ", c
    print c, p

    alp, beta = vlspgm.calcAngles(LEG, c, lam)
    print 'Alpha =',vlspgm.deg(alp)
    print 'Beta =',vlspgm.deg(beta)
    mir, grt = vlspgm.gratingToPGM(alp, beta)
    print 'Mirror =',vlspgm.deg(mir)
    print 'Grating =',vlspgm.deg(grt)

if __name__ == "__main__":
    runit()
