from django.shortcuts import render

# Create your views here.

import scipy
import scipy.constants

def energy_ev2lambda_nm(en_eV):              # input photo energy in eV
    en_float = float(en_eV)
    planck = scipy.constants.Planck
    light_c = scipy.constants.speed_of_light
    e_chargenumber = scipy.constants.e
    lbda =  planck*light_c/(en_float*e_chargenumber)
    return(lbda*1.0e9)

def lambda_nm2energy_eV(lbda):               # input photon wavelength in nm
    planck = scipy.constants.Planck
    light_c = scipy.constants.speed_of_light
    e_chargenumber = scipy.constants.e
    energy_eV = planck*light_c/(lbda*1.0e-9)/e_chargenumber
    return(energy_eV, ' eV')

def energy_ev2wavenumber_cm1(en_eV):         #
    en_float = float(en_eV)
    planck = scipy.constants.Planck
    light_c = scipy.constants.speed_of_light
    e_chargenumber = scipy.constants.e
    lbda =  planck * light_c / (en_float * e_chargenumber)
    wavenumber = 1.0/(lbda*100)                     
    return(wavenumber)
    
def wavenumber_cm2energy_eV(wn):         #
    energy_eV = 2;
    return(energy_eV, ' eV')
    

# ncm = energy_ev2wavenumber_cm1('1.0')
# print(ncm)


def scalc(request):
    context = {}

    if request.method == 'POST':
        if 'ev1' in request.POST:	
            exp1 = request.POST['ev1']
            try:
                result1 = energy_ev2lambda_nm(exp1)
            except SyntaxError:
                result = 'Syntax error'
            except ZeroDivisionError:
                result = 'Cannot divide by zero.'
            except ValueError:
                result = 'Invalid input'
            context = {'result1': result1}
        elif 'ev2' in request.POST:
            exp2 = request.POST['ev2']
            try:
                result2 = energy_ev2wavenumber_cm1(exp2)
            except SyntaxError:
                result = 'Syntax error'
            except ZeroDivisionError:
                result = 'Cannot divide by zero.'
            except ValueError:
                result = 'Invalid input'
            context = {'result2': result2}
        else:
            context = {}

    return render(request, 'scalc.html', context)

def index(request):
    return render(request, 'index.html')

