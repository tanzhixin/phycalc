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
    planck = scipy.constants.Planck
    light_c = scipy.constants.speed_of_light
    e_chargenumber = scipy.constants.e
    lbda =  planck*light_c/(en_eV*e_chargenumber)
    wavenumber = 2*scipy.pi
    return(wavenumber*100, ' cm-1')
    
def wavenumber_cm2energy_eV(wn):         #
    energy_eV = 2;
    return(energy_eV, ' eV')
    

nm = energy_ev2lambda_nm(5.38)

print(nm)


def scalc(request):
    if request.method == 'POST':
        expression = request.POST['expression']
        try:
            result = energy_ev2lambda_nm(expression)
        except SyntaxError:
            result = 'Syntax error'
        except ZeroDivisionError:
            result = 'Cannot divide by zero.'
        except ValueError:
            result = 'Invalid input'
        context = {'result': result}

    else:
        context = {}

    return render(request, 'scalc.html', context)
