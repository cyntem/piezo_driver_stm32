import math
Rt=[20*1e3,45.3*1e3,165*1e3]
FreqMax=[2.15*1e6, 1.08*1e6,0.327*1e6]
Choose=0 #MaxFreq low Noise
Rt=Rt[Choose]
FreqMax=FreqMax[Choose]

FreqMax=1.8*1e6 
Rt=((51.2/(FreqMax/1e6))-5.6)*1e3




MinimumOffTimeMAX=75*1e-9
MinimumOnTimeMAX=95*1e-9
print("MinimumOffTimeMAX",MinimumOffTimeMAX)

print("Rt",Rt,"FreqMax",FreqMax)

LCSC_DIODE="C14996" #SS210 100V 850mV@2A 2A SMA(DO-214AC) Schottky Diodes ROHS
Vd=0.85



Vout=75

R2=22
R1=round((R2*((Vout/1.6)-1))/1000)*1000
print("R1",round(R1,2),"k R2",round(R2,2),"k")
Vout=(R1*1.6+1.6*R2)/R2
print("VoutP",Vout)
R2N=10
R1N=round((R2N*((Vout/0.8)-1))/1000)*1000
print("R1N",round(R1N,2),"k R2N",round(R2N,2),"k")

Voutn=(R1N*0.8+0.8*R2N)/R2N

print("VoutN",Voutn)

VinMin=12
VinMax=24
IoutMax=0.120



Dmax=(Vout+Vd)/(VinMin+Vout+Vd)
Dmin=(Vout+Vd)/(VinMax+Vout+Vd)
print(Dmax,1-MinimumOffTimeMAX*FreqMax)
assert(Dmax<1-MinimumOffTimeMAX*FreqMax)
print(Dmin,MinimumOffTimeMAX*FreqMax)
assert(Dmin>MinimumOffTimeMAX*FreqMax)

Il1max=IoutMax*Dmax/(1-Dmax)
Il2max=IoutMax
print("Il1max",Il1max)
Iswmaxavg=Il1max+Il2max
print("Iswmaxavg",round(Iswmaxavg,2))

χ=0.65

dIsw=χ*Iswmaxavg
dIL1=0.5*dIsw
dIL2=dIL1
η=0.85
print(IoutMax,(1-Dmax)*(2-0.5*dIsw)*η)
assert(IoutMax<(1-Dmax)*(2-0.5*dIsw)*η)
L1=VinMin*Dmax/(0.5*dIsw*FreqMax)
print("L1",round(L1*1e6),"µH")
L1Widing=VinMin*Dmax/(dIsw*FreqMax)
print("L1Widing",round(L1Widing*1e6,2),"µH")

Il1peak=Il1max+0.5*dIL1
Il2peak=Il2max+0.5*dIL2
print("Il1peak",Il1peak,"Il2peak",Il2peak)

IrmsCout=IoutMax*math.sqrt(Dmax/(1-Dmax))
print("IrmsCout>=",IrmsCout)
Cout=IoutMax/(0.01*Vout*FreqMax)
print("Cout>=",round(Cout*1e6,2),"uF")
