from django.shortcuts import render
from django.http import HttpResponse
def chindex(request):
    return render(request, 'index.html' )


def analyze(request):

    # get the text
    djtext = request.POST.get('text','default')

    #check the value of check box
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    
    # analyzing text = djtext
    
    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[]/^_`{|}~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        djtext = analyzed
    
    if fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed+char.upper()
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed +char
        djtext = analyzed

    if spaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed = analyzed+char
        djtext = analyzed

    
    if (removepunc !='on'and fullcaps !='on' and newlineremover!='on'and spaceremover!='on'):
        return HttpResponse('error')
    
    params = {'purpose':'Anaysed text','analysed_text':analyzed}
    return render(request, 'analyse.html', params)
    

