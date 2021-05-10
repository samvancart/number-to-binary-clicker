from django.shortcuts import render, redirect
import math

def index(request, number = 0):
     context = {"number" : number, "binary" : 0}
     return render(request, 'clicker/index.html', context)

def decrement(number):
     if number > 0: number -= 1
     return number

def increment(number):
     number += 1
     return number

def num_clicked(request, number):
     for key, value in request.POST.items():
          if value == 'decrement':
               number = decrement(number)
               break
          elif value == 'increment':
               number = increment(number)
               break
          elif value == 'reset':
               number = 0
               return redirect(index)
          else: continue

     binary = to_binary(number)
     context = {"number" : number, "binary" : binary}

     return render(request, 'clicker/index.html', context)


def to_binary(x):
    if x == 0:
        return "0" 
    ln = math.floor(math.log(x,2))
    b = ""
    for i in range(ln,-1,-1):
        p = 2**i
        if x > p:
            b += "1"
            x -= p
        elif x == p:
            b += "1"
            b += "0" * i
            break
        elif x < p:
            b += "0"

    return b