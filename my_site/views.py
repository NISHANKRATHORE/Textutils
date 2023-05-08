# i have created this file--- Ricky
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    # return HttpResponse("Home")
    return render(request,"index.html")


def analyze(request):
    # get the text
    djtext= request.POST.get('text','default')
    # check checkbox value
    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    newlineremover= request.POST.get('newlineremover','off')
    spaceremover= request.POST.get('spaceremover','off')
    charcount= request.POST.get('charcount','off')
    # check which checkbox on 
    if removepunc == "on":
        Punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        # remove checkbox code
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuation','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
        # uppercase code 
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Change to Capitalized text','analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request,'analyze.html',params)
        
        # New line remover text
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
                params = {'purpose':'Remove lines','analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request,'analyze.html',params)
        
        # Space remover coding
    if(spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index+1] == " "):
                analyzed = analyzed + char
                params = {'purpose':'Remove lines','analyzed_text': analyzed}
        # analyze the text
        djtext = analyzed
        # return render(request,'analyze.html',params)
    

    if(charcount == "on"):
        analyzed = ""
        for char in djtext:
            analyzed =len(djtext)
            analyzed = analyzed 
            params = {'purpose':'Character Count','analyzed_text': analyzed}
    if(removepunc != "on" and fullcaps!="on" and newlineremover != "on" and spaceremover != "on"):
            return HttpResponse("Please select any operator and try again")
  
    return render(request,'analyze.html',params)

def about(request):
    return render(request,"about.html")
