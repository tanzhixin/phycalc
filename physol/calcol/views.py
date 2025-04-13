from django.shortcuts import render
from django.conf import settings



# Create your views here.
import math
import scipy
import scipy.constants
from passlib import pwd



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
    energy_eV = planck*light_c/( float(lbda)*1.0e-9)/e_chargenumber
    return(energy_eV)

def energy_ev2wavenumber_cm1(en_eV):    
    en_float = float(en_eV)
    planck = scipy.constants.Planck
    light_c = scipy.constants.speed_of_light
    e_chargenumber = scipy.constants.e
    lbda =  planck * light_c / (en_float * e_chargenumber)
    wavenumber = 1.0/(lbda*100)                     
    return(wavenumber)
    
def wavenumber_cm2energy_eV(wn):        
    lbda = 1/(float(wn)*100)
    energy_eV = lambda_nm2energy_eV(lbda)
    return(energy_eV)
    

# ncm = energy_ev2wavenumber_cm1('1.0')
# print(ncm)


def neutron_energy2velocity(vE):                    #vE: neutron energy in eV
    # m0 = 1.6749286E-27
    m0 = scipy.constants.neutron_mass
    # c_const = 299792458
    # e_const = 1.602e-19
    c_const = scipy.constants.speed_of_light
    e_const = scipy.constants.e

    e_static = m0*c_const*c_const/e_const;                # eV
    gamma = (e_static + vE)/e_static
    beta = math.sqrt(1-math.pow(1/gamma, 2))
    velo = beta*c_const
    return(velo)

def time_tof(ev, dist):
    velo = neutron_energy2velocity(ev)
    return(dist/velo)



def printanno():
    anno = [
        "100MeV        1.583E8            2.0648E3   m",  \
        "10MeV         4.3E7", \
        "1MeV          1.382E7            4.34E-6 us", \
        "115keV        4.6E6              13.043 us", \
        "10keV         1.383E6 ", \
        "1keV          4.3E5              5m", \
        "100eV         1.38E5", \
        "10eV          4.374E4", \
        "1eV           1.383E4"]
    txt = ""
    txt = [ txt + t  for t in anno]
    print("常见速度和时长(60m):")
    [print(t) for t in anno] 
    return(txt)

en = 100
v = neutron_energy2velocity(en)
print(v)
print(time_tof(115000, 60))
printanno()




def pcalc(request):
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
        elif 'nm1' in request.POST:
            wavelength1 = request.POST['nm1']
            try:
                result3 = lambda_nm2energy_eV(wavelength1)
            except SyntaxError:
                result = 'Syntax error'
            except ZeroDivisionError:
                result = 'Cannot divide by zero.'
            except ValueError:
                result = 'Invalid input'
            context = {'result3': result3}
        elif 'nm2' in request.POST:
            wavelength2 = request.POST['nm2']
            try:
                result4 = wavenumber_cm2energy_eV(wavelength2)
            except SyntaxError:
                result = 'Syntax error'
            except ZeroDivisionError:
                result = 'Cannot divide by zero.'
            except ValueError:
                result = 'Invalid input'
            context = {'result4': result4}
        else:
            context = {}

    return render(request, 'pcalc.html', context)


def mcalc(request):
    context = {}
    return render(request, 'mcalc.html', context)


def pwg(request):
    history = request.session.get('history', [])
    pswd = "123456"
    lenz = 12
    if request.method == 'POST':
        lenz = int(request.POST['lenz'])
        pswd = pwd.genword(length=lenz, charset='ascii_62')
        history.insert(0, pswd)
        if len(history)>8:
            history = history[:8]
        request.session['history'] = history 
    return render(request, 'pwg.html', {"pswd":history})

def ncalc(request):
    context = {}

    if request.method == 'POST':
        if 'ev1' in request.POST and 'ev1' in request.POST:	
            dist = float(request.POST['dist1'])
            ev = float(request.POST['ev1'])
            try:
                velo = neutron_energy2velocity(ev)
                tof = dist/velo
            except SyntaxError:
                result = 'Syntax error'
            except ZeroDivisionError:
                result = 'Cannot divide by zero.'
            except ValueError:
                result = 'Invalid input'
            context = {'velo1':velo, "tof1":tof }
        else:
            context = {}

    return render(request, 'ncalc.html', context)



def index(request):
    return render(request, 'index.html')

