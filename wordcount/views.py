from django.shortcuts import render

from .forms import *


def WordView(request, pk):
    form = WordForm()
    if request.method == "GET":
        return render(request, 'word.html', context={'form': form})
    if request.method == 'POST':
        word = request.POST['word']
        file = File.objects.get(id=pk)
        with open(file.file.path, "r", encoding='utf-8') as f:
            d = word
            t = list(f.readlines())
            tt = [i.rstrip() for i in t]
            count = 0
            for i in range(0, len(tt)):
                if d.casefold() in tt[i].casefold():
                    count += 1
                    if ' ' in tt[i]:
                        r = tt[i].split(' ')
                        if d.casefold() in r:
                            count += 1
    return render(request, 'file.html', context={'d': word,
                                                 'count': count,
                                                 'number': pk})


def HomePage(request):
    if request.method == "POST":
        form = StartForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            file = form.cleaned_data.get('file')
            obj = form.save(commit=False)
            obj.file = file
            obj.save()
            word = form.cleaned_data.get('word')
            with open(obj.file.path, "r", encoding='utf-8') as f:
                d = word
                t = list(f.readlines())
                tt = [i.rstrip() for i in t]
                count = 0
                for i in range(0, len(tt)):
                    if d.casefold() in tt[i].casefold():
                        count += 1
                        if ' ' in tt[i]:
                            r = tt[i].split(' ')
                            if d.casefold() in r:
                                count += 1
                number = File.objects.get(file=obj.file).id
        return render(request, 'file.html', context={'d': word,
                                                     'count': count,
                                                     'number': number})
    if request.method == "GET":
        form = StartForm(request.POST or None, request.FILES or None)
        return render(request, template_name='start.html', context={'form': form})
