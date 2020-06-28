"""
Modelos Probabilísticos de Señales y Sistemas
Tarea 3
Estudiante: Kevin Alvarado Araya
Carnet: B60295
Grupo: 01
""" 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D

# Lectura de los .csv con pandas
xy=pd.read_csv("xy.csv")
xyp=pd.read_csv("xyp.csv")

# Creación de matrices 
m_xy = np.array(xy.to_numpy()).astype("float")
m_xyp = np.array(xyp.to_numpy()).astype("float")


# Punto 1

# Cálculo de las funciones de densidad marginales
fX = np.sum(m_xy, axis=1)
fY = np.sum(m_xy, axis=0)

# Vectores de variables aleatorias
x=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
y=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,25]

# Consideranto que fX(x) y FY(y) se aproximan a una distribución gaussina:

def gauss(k,mu,sigma):
  return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(k-mu)**2/(2*sigma**2))

# Parámetros de una func. de densidad gaussiana
# justada a fX(x)
param1, _ = curve_fit(gauss, x, fX)
print("fX(x) se aproxima como una función normal con media {} y varianza {}".format(param1[0],param1[1]))

# Parámetros de una func. de densidad gaussiana
# justada a fY(y)
param2, _ = curve_fit(gauss, y, fY)
print("fY(y) se aproxima como una función normal con media {} y varianza {}".format(param2[0],param2[1]))


# Punto 2 (se desarrolla en el archivo README.md)

# Punto 3

# Se leen las columnas de la matriz de valores  creada 
# con los valores del archivo xyp.csv 
X= m_xyp[:,0]
Y= m_xyp[:,1]
P= m_xyp[:,2]

# Cálculo de la correlación
Rxy = 0
for i in  range(len(X)):
  if i == 0:
    i = i + 1
  else:
    va_x = X[i];
    va_y = Y[i];
    proba = P[i];
    Rxy += va_x*va_y*proba;

print("Correlación: ", Rxy)

# Cálculo de covarrianza
Cxy=Rxy-(param1[0]*param2[0])
print("Covarianza: ", Cxy)

# Coeficiente de correlación
coef_p=Cxy/(param1[1]*param2[1])
print("Coef. de correlación: ",coef_p)

# Punto 4

# Gráficas de las funciones de densidad marginales
plt.plot(x, fX, 'ro')
plt.title('Función marginal fX(x)')
plt.xlabel('X')
plt.ylabel('fx(x)')
plt.savefig("fX.png")
plt.close()

plt.plot(y, fY, 'go')
plt.title('Función marginal fY(y)')
plt.xlabel('Y')
plt.ylabel('fY(y)')
plt.savefig("fY.png")
plt.close()

# Comparación de la aproximación y la distribución fX(x)
aprox_x=norm.pdf(x,param1[0], param1[1])
plt.plot(x, fX, 'ro')
plt.plot(x, aprox_x)
plt.title('Función marginal fX(x) y aproximación gaussiana')
plt.xlabel('X')
plt.ylabel('fx(x)')
plt.savefig("gaussX.png")
plt.close()

# Comparación de la aproximación y la distribución fY(y)
aprox_y=norm.pdf(y,param2[0], param2[1])
plt.plot(y, fY, 'go')
plt.plot(y, aprox_y)
plt.title('Función marginal fY(y) y aproximación gaussiana')
plt.xlabel('Y')
plt.ylabel('fY(y)')
plt.savefig("gaussY.png")
plt.close()

# Función de densidad conjunta
P1 = np.reshape(P, -1);

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(X, Y, P, c=P1, cmap='hsv', s=10, linewidth=2)
plt.title('Función de densidad conjunta')
ax.set_xlabel('X')
ax.set_ylabel('Y')
plt.savefig("fXY.png")
plt.close()