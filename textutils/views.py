# i have created this file


from django.http import HttpResponse
from django.shortcuts import render        #


# def index(request):
#
#     return HttpResponse('''<h1>hello</h1> <a href="https://youtube.com"> my youtube</a>''')
#
#
# def about(request):
#     return HttpResponse("hello my name is tejas")

def index(request):
    #params = {'name':'tejas', 'place':'MArs'}
    return render(request, 'index.html')

    #return HttpResponse("Home")
#
#


def analyze(request):
    djtext=request.POST.get('text', 'default')    # get the text
    #check the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')

    #check which checckbox  is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+ char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to upper case', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed

    if newlineremover== "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext=analyzed

    if extraspaceremover =="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index +1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)




def ex1(request):
    s = ''' <h2>Navigation Bar <br> </h2>
        <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
        <a href="https://www.facebook.com/"> Facebook </a> <br>
        <a href="https://www.flipkart.com/"> Flipkart </a> <br>
        <a href="https://www.hindustantimes.com/"> News </a> <br>
        <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)

#
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
#
# def newlineremove(reuest):
#     return HttpResponse(" remove new line")
#
#
# def spaceremove(reuest):
#     return HttpResponse(" remove space")
#
#
# def charcount(reuest):
#     return HttpResponse(" charcount")

