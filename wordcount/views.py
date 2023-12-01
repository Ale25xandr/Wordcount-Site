from django.shortcuts import render, redirect

from .forms import *


def WordView(request, pk):
    form = WordForm()
    if request.method == "GET":
        return render(request, 'word.html', context={'form': form})
    if request.method == 'POST':
        word = request.POST['word']
        file = File.objects.get(id=pk)
        w = Words.objects.filter(word=word, file=file)
        print(w)
        if w.exists():
            count = w.values('count')
            return render(request, 'file.html', context={'d': word,
                                                         'count': count[0]['count'],
                                                         'number': pk})
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
            Words.objects.create(word=word, count=count, file=file)
    return render(request, 'file.html', context={'d': word,
                                                 'count': count,
                                                 'number': pk,
                                                 'word': d})


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
                f = File.objects.get(file=obj.file)
                number = f.id
                Words.objects.create(word=word, count=count, file=f)
        return render(request, 'file.html', context={'d': word,
                                                     'count': count,
                                                     'number': number})
    if request.method == "GET":
        form = StartForm(request.POST or None, request.FILES or None)
        return render(request, template_name='start.html', context={'form': form})


def HistoryView(request, pk):
    if request.method == "GET":
        file = File.objects.get(id=pk)
        words = Words.objects.filter(file=file)
        return render(request, 'history.html', context={'number': pk,
                                                        'w': words.distinct()})


def TemplateDelete(request, pk):
    return render(request, 'delete.html', context={'number': pk})


def DeleteHistory(request, pk):
    words = Words.objects.filter(file=pk)
    words.delete()
    return redirect('history', pk=pk)
