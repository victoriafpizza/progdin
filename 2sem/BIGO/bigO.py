import numpy as numpy
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import math

#definição de algoritmos por função
#dificuldade computacional constante
def const(numbers, pos):
    if pos > len(numbers):
        return "Erro, tente outra"
    return numbers[pos]  