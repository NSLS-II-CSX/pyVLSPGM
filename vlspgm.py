import numpy as np
hc_over_e = 299792458*4.1356673310e-15*1e3

def deg(r):
    """Convert radians to degrees"""
    return 180 * r / np.pi

def rad(d):
    """Convert degrees to radians"""
    return np.pi * d / 180

def calcC(grating, R, lam, allParams = False):
    """Calculate "c" factor for PGM from grating exp. geometry"""
    
    """
    a0 = grating[0]
    a1 = grating[1]
    a2 = grating[2]
    a3 = grating[3]
    """
    
    k = grating[0]
    b2 = -grating[1] / (2 * k)
    b3 = grating[2] / (3 * k)
    b4 = grating[3] / (4 * k)
    rA = R[0] 
    rB = R[1]

    r = rB / rA
    A0 = k * lam
    A2 = k * lam * rB * b2

    c = (2 * A2) + (4 * np.power(A2 / A0, 2)) + ((4 + (2*A2) - np.power(A0,2)) * r)
    c = c - (4 * (A2/A0) * (np.power(np.power(1 + r, 2) + (2 * A2 * (1 + r)) - (np.power(A0, 2)*r),0.5)))
    c = c / (-4.0 + np.power(A0, 2) - (4 * A2) + (4 * np.power(A2/A0, 2)))
    c = np.power(c, 0.5)

    if allParams:
        params = {}
        params['k'] = k
        params['b2'] = b2
        params['b3'] = b3
        params['b4'] = b4
        params['rA'] = rA
        params['rB'] = rB
        params['r'] = r
        params['A0'] = A0
        params['A2'] = A2
        rtn = (c, params)
    else:
        rtn = c
        
    return rtn

def calcAngles(grating, c, lam, allParams = False):
    """Calculate grating angles and focus parameters"""

    k = grating[0]

    alp = -1.0 * k * lam / (np.power(c,2) - 1)
    alp = alp + np.power(1 + ((c**2 * k**2 * lam**2) / (c**2 - 1)**2), 0.5)
    alp = np.arcsin(alp)

    bet = c * np.cos(alp)
    bet = np.arccos(bet)

    if allParams:
        M20 = (((np.cos(alp)**2/ rA) + (np.cos(bet)**2 / rB)) / 2) + (k * lam * b2)
        M30 = ((np.cos(alp)**2 * np.sin(alp) / rA**2) - (np.cos(bet)**2 * np.sin(bet) / rB**2)) / 2
        M30 = M30 + (k * lam * b3)
        M40 = ((np.cos(alp)**2 * (4 * np.sin(alp)**2 - np.cos(alp)**2) / rA**3) + (np.cos(bet)**2 * (4 * np.sin(bet)**2 - np.cos(bet)**2) / rB**3)) / 8
        M40 = M40 + (k * lam * b4)

    if allParams:
        params = {}
        params['M20'] = M20
        params['M30'] = M30
        params['M40'] = M40
        
        rtn = alp, bet, params
    else:
        rtn = alp, bet

    return rtn

if __name__ == "__main__":
    """Test the routines!"""
    #LEG = [70.00, 0.03838, 2.8e-6, 0.0] # CSX-1
    LEG = [150.0, 0.0540, 8.09e-6, 0.0] # CSX-2
    #R = [40500, 13000] #CSX-1
    R = [np.inf, 10000]
    lam = hc_over_e / 200.0
    c,p = calcC(LEG, R, lam, True)
    print c,p
    alp, beta = calcAngles(LEG, c, lam)
    print deg(alp), deg(beta)
