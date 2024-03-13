from django.http import HttpResponse
from django.shortcuts import render

    
def index(request):
    return render(request,'index.htm')

def analyze(request):
    userText  = request.POST.get('text','')
    removePunctuations  = request.POST.get('removePunctuations','off')
    removeExtraSpaces  = request.POST.get('removeExtraSpaces','off')
    capatalize  = request.POST.get('capatalize','off')
    print(userText," ",removePunctuations," ",removeExtraSpaces," ",capatalize)
    tranformedText=""
    if removePunctuations=='on':
        punctuation_characters = '''.,!?;:'\"()[]{}-–—.../\&@%$#€+-=*_|~'''
        for ch in userText:
            if ch not in punctuation_characters:
                tranformedText += ch
    if removeExtraSpaces=='on':
        if tranformedText!="" :
            userText=tranformedText
            tranformedText=""
        for index,ch in enumerate(userText):
            if index == len(userText) - 1 :
                pass
            if not (userText[index]==' ' and userText[index+1]==' '):
                tranformedText += ch
    if capatalize=='on':
        if tranformedText!="" :
            userText=tranformedText
            tranformedText=""
        for ch in userText:
            tranformedText += ch.upper()
    params={
        'analyzedText' : f'{tranformedText}'
    }
    return render(request,'output.htm',params)

        