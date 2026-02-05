#This file is supposed to fade mo bamba out and fade sicko mode in
import math
f1 = open("mo.wav", "rb")
f2 = open("SICKOMODE.wav", "rb")
#y=-2.04118\ln\left(x^{3.68869}+1.58185\right)+1.93607 - equation for fade out
#y=0.0449488e^{\left(3.28128x-0.140744\right)}-0.0390475 - equation for fade in

def fadeout(kabloom):

    x = math.pow(kabloom, 3.68869) + 1.58185
    supersecretspecialequationoutput = -2.04118 * math.log(x) + 1.93607
    if 0 <= supersecretspecialequationoutput <= 1:
        return supersecretspecialequationoutput
    else:
        if supersecretspecialequationoutput < 0:
            return 0.0
        else:
            return 1.0

def fadein(kablow):

    x = 3.28128 * kablow - 0.140744
    supersecretspecialequationoutput2 = 0.0449488 * math.exp(x) - 0.0390475
    if 0<=supersecretspecialequationoutput2<=1:
        return supersecretspecialequationoutput2
    else:
        if supersecretspecialequationoutput2 < 0:
            return 0.0
        else:
            return 1.0


