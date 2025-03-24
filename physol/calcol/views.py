from django.shortcuts import render

# Create your views here.

#def home(request):
#    return render(request, 'home.html')

def scalc(request):
    if request.method == 'POST':
        expression = request.POST['expression']
        try:
            result = eval(expression)
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
