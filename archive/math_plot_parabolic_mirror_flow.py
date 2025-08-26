#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SESA237770
#
# Created:     18.07.2023
# Copyright:   (c) SESA237770 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass


## For most practical purposes, you can think of the conditional block that you open
## with if __name__ == "__main__"
## as a way to store code that should only run when your file is executed as a script.

if __name__ == '__main__':
    main()

    #-------------------------------------------------------------------------------

def GetNamedCellValue(sCellName,workbook,sheet):

    address = list(workbook.defined_names[sCellName].destinations)
    #[('Sheet1', '$B$7:$E$10')]
    #removing the $ from the address
    #------------------------------------------------------
    for sheetname, cellAddress in address:
        cellAddress = cellAddress.replace('$','')
        #'B7:E10'

    sValue=sheet[cellAddress].value
##    sValue=sheet[cellAddress][0][0].value
    print(f'Named Range {sCellName} has Cell Address scalar: {cellAddress} and value= {sValue}')

    return sValue
#-------------------------------------------------------------------------------
import sys
sys.path.append('C:\\ProgrammeApps\\python3')
sys.path.append('C:\\ProgrammeApps\\python3\\Lib\\site-packages')

import matplotlib.pyplot as plt
import numpy as np
import os
#-------------------------------------------------------------------------------
# open workbook and load all variables
#-------------------------------------------------------------------------------
from openpyxl import load_workbook
from scipy import integrate
from scipy.integrate import quad

print('=====<ARGUMENTS>========================================')
print( 'Arguments:', len(sys.argv), 'arguments.')
print('Argument:', str(sys.argv[0]))

lArguments=[]
for i in range(len(sys.argv)):
 if len(sys.argv) == 3:
        lArguments.append(sys.argv[1])

print('Arguments:', lArguments)

print('=====</ARGUMENTS>========================================')

if len(sys.argv) == 2:
    print('Argument:', str(sys.argv[1]))
    WBname=str(sys.argv[1])
else:
    WBname='ParabolicMirror_OoCalc.xlsx'

print('=====================================================')

print('=====================================================')
print('====<Loading Workbook Constraints> ==================')
print('=====================================================')

##WBname='ParabolicMirror_OoCalc_02.xlsx'
WBpath='C:\\Users\\sesa237770\\Documents\\Mathbox\\Python_Samples\\01-ParabolicMirror'
WBpath=os.path.dirname(__file__)
WBpathname=WBpath +'\\'+ WBname

##WBname='ParabolicMirror.ods'

wb = load_workbook(WBpathname)
ws = wb.active  # work sheet
#-------------------------------------------------------------------------------
# @ jumbo mirror = 1000 x 500

print('====Loading Constraints======')

Xmax=450  # mirror X size
Ymax=500  # mirror Y size
Lmax=500  # mirror Y size

Xmax=float(GetNamedCellValue('rngXmax',wb,ws))
Ymax=float(GetNamedCellValue('rngYmax',wb,ws) )
LengthMirrorArc=GetNamedCellValue('rngLength',wb,ws)



print('\n Xmax==' + str(Xmax))
print('\n Ymax==' + str(Ymax))
print('\n Lmax==' + str(Lmax))


print('=====================================================')
print('====</ Loading Workbook Constraints> ==================')
print('=====================================================')
#-------------------------------------------------------------------------------
# open workbook and load all variables
#-------------------------------------------------------------------------------

Larc=LengthMirrorArc*1.1


while Larc > LengthMirrorArc:
##if 1==1:

    # Parabola; y = a(b+x)**2 + c
    # a= Y/(X**2)
    # b = Xmax/2

    a=round(4*Ymax/Xmax/Xmax,5)   # a= +/- 0.05

    c =0
    b=-Xmax/2

    Yfocus=round(c+ 1/a/4,1)
    Xfocus=b

    print('======================================')
    print('====Calculating Parabola constraints======')
    print('======================================')

    print('\n Equation=' +"a(X + b)^2 + c")
    print('a=' + str(a))
    print('b=' + str(b))
    print('c=' + str(c))

    print(' Equation= ' + str(a)+"(X + "+ str(b)+")^2 +"+ str(c))
    print(' Y Focus = ' + str(Yfocus))

    print('\n==========================================')
    print('\n===========================================')

    x = np.linspace(0, Xmax, 20)
    ##y = np.sin(x)
    y = a*(x+b)**2 + c

    x2=np.linspace(0.9*Xmax/2,  1.1*Xmax/2, 20)
    y2 = Yfocus + 0*x


    print('\n===========================================')
    print('\n===========================================')
    # import scipy.integrate.quad

    arcLength = lambda x: (1+  4*a**2*(x+b)**2)**0.5

    # using scipy.integrate.quad() method
    Iresult = integrate.quad(arcLength, 0, Xmax)

    ##print(geek)

    print('\n===========================================')
    print('\n===Calculating arc Length of Parabola=====')
    Larc=round(Iresult[0],0)
    print('arc Length=' + str(Larc) +" mm")

    print('==========================================')
    print('=========Arc Coordinates ===========')

    print('\n X and y vectors:')

    print(x)
    print(y)
    ## xy = np.meshgrid(x,y)

    xy =np.array([[X1, Y1] for X1 ,Y1 in zip(x,y)])
    xy=np.around(xy, 0)



    print('\n X and y Matrix:')
    ARCpathname=os.path.realpath(__file__) +'\\'+ 'arc'
    ARCpathname= 'arc'
    np.save(ARCpathname,xy) # binary array
    np.savetxt(WBpath+'\\'+"ARC.csv", xy, delimiter="\t")
    print(xy)

    #itterating up or down
    if Larc > LengthMirrorArc:
        Ymax=Ymax*0.99
    if Larc < LengthMirrorArc:
        Ymax=Ymax*1.01

    Ymax_round=round(Ymax,0)
    print('=Iteration Ymax(i)=',Ymax_round)

    print('==========================================')


fig, ax = plt.subplots()
ax.plot(x, y,'r')
ax.plot(x2, y2, 'g')

ax.annotate('Focus Y= '+ str(Yfocus), xy=(Xfocus, Yfocus), xytext=(100, 400), arrowprops=dict(facecolor='black', shrink=0.05),      )

ax.annotate('Arc L=' + str(Larc)  +" Ymax="+str(Ymax_round)+' Focus Y= '+ str(Yfocus) +" mm",
            xy=(.025, .975), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=20)

ax.set_xlim([0, 500])
ax.set_ylim([0, 500])

print('==========================================')

print('==========================================')

ax.plot(100,100)
plt.savefig(WBpath+'\\'+'Parabola.jpg')

plt.show()
plt.show(block=True)

print('=====PROGRAM COMPLETED=================================')