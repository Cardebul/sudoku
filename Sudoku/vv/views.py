from django.shortcuts import render
from .resh import solution, complete
from .valid import ff

def index(request):
    context = {'data': False}
    r = []
    e = 10
    while e < 83:
        r.append([i for i in range(e-9, e)])
        e += 9
    context['numbers'] = r
    try:
        if request.method == "POST":
            if ff(complete(list(request.POST.values()))):
                w = solution(list(request.POST.values()))
                context = {'data': w}
            else:
                raise Exception
    except Exception:
        error = 'Ошибка ввода'
        context['error']=error
    return render(request, 'base.html', context)


