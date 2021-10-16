# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # details = {'name':'Faisal', 'place':'Nizamabad'}
    return render(request, 'index.html')

    # return HttpResponse('''<h1>CBIT-LMS PORTAL</h1> <a href="http://learning.cbit.org.in/my/" target="_main"> CBIT LMS Portal</a>''')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# text = "mohammed faisal hussain"

def punc_remover(text):
    #print(text)
    _analysed = ""
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    for i in text:
        if i not in punctuations:
            _analysed += i
    #print(_analysed)
    return str(_analysed)

def first_letter_capitalizer(text):
    #print(text)
    _analysed = ""
    for word in text.split():
        _analysed += word.capitalize() + ' '
    #print(_analysed)
    return str(_analysed)
# print(first_letter_capitalizer(text))

def char_counter(text):
    #print(text)
    list_char = list(text)
        #print(list_char)
    set_char = set(list_char)
        #print(set_char)
    dict_char = {}
    for i in set_char:
        if i != ' ':
            dict_char[i] = text.count(i)
    #print(dict_char)
    return str(dict_char)

def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')
    #print(djtext)
    #Get the checkbox
    rempunc = request.GET.get('removepunc', 'default')
    capfirst = request.GET.get('capitalizefirst', 'default')
    charcount = request.GET.get('charcount', 'default')
    

    if rempunc == "on" and capfirst != "on" and charcount != "on":
        parameters = {'purpose':'Removing Punctuations', 'analysed_text':punc_remover(djtext)}
        return render(request, 'analyse.html', parameters)
    elif rempunc != "on" and capfirst == "on" and charcount != "on":
        parameters = {'purpose':'Capitalize First letter', 'analysed_text':first_letter_capitalizer(djtext)}
        return render(request, 'analyse.html', parameters)
    elif rempunc != "on" and capfirst != "on" and charcount == "on":
        parameters = {'purpose':'Counting Characters', 'analysed_text':char_counter(djtext)}
        return render(request, 'analyse.html', parameters)
    elif rempunc == "on" and capfirst == "on" and charcount == "default":
        djtext = punc_remover(djtext)
        parameters = {'purpose':'Removing Punctuations and Capitalizing First letter', 'analysed_text':first_letter_capitalizer(djtext)}
        return render(request, 'analyse.html', parameters)
    elif rempunc == "on" and capfirst != "on" and charcount == "on":
        #djtext = punc_remover(djtext)
        parameters = {'purpose':'Removing Punctuations and Counting Characters', 'analysed_text':punc_remover(djtext) + '\n' + char_counter(djtext)}
        return render(request, 'analyse.html', parameters)
    elif rempunc != "on" and capfirst == "on" and charcount == "on":
        #djtext = first_letter_capitalizer(djtext)
        parameters = {'purpose':'Capitalizing First letter and Counting Characters', 'analysed_text':first_letter_capitalizer(djtext) + '\n' + char_counter(djtext)}
        return render(request, 'analyse.html', parameters)
    elif rempunc == "on" and capfirst == "on" and charcount == "on":
        djtext = punc_remover(djtext)
        djtext = first_letter_capitalizer(djtext)
        parameters = {'purpose':'Removing Punctuations, Capitalizing First letter and Counting Characters', 'analysed_text':first_letter_capitalizer(djtext) + '   ' + char_counter(djtext)}
        return render(request, 'analyse.html', parameters)
    
    # _analysed = ""
    # if rempunc == "on":
    #     punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    #     for i in djtext:
    #         if i in punctuations:
    #             i = ""
    #         _analysed += i
    #     parameters = {'purpose':'Removing Punctuations', 'analysed_text':_analysed}
    #     return render(request, 'analyse.html', parameters)
    # elif capfirst == 'on':
    #     for word in djtext.split():
    #         _analysed += word.capitalize() + ' '
    #     parameters = {'purpose':'Capitalize First letter', 'analysed_text':_analysed}
    #     return render(request, 'analyse.html', parameters)
    # elif charcount == 'on':
    #     list_char = list(djtext)
    #     #print(list_char)
    #     set_char = set(list_char)
    #     #print(set_char)
    #     dict_char = {}
    #     for i in set_char:
    #         if i != ' ':
    #             dict_char[i] = djtext.count(i)
    #     #print(dict_char)
    #     parameters = {'purpose':'Capitalize First letter', 'analysed_text':str(dict_char)}
    #     return render(request, 'analyse.html', parameters)

    else:
        return HttpResponse("ERROR!")

# def removepunc(request):
#     #Get the guest
#     djtext = request.GET.get('text', 'default')
#     rempunc = request.GET.get('removepunc', 'default')
#     #print(rempunc)
#     #print(djtext)
#     _analysed = ""
#     punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#     for i in djtext:
#         if i in punctuations:
#             i = ""
#         _analysed += i
#     print(_analysed)
#     parameters = {'purpose':'Removing Punctuations', 'analysed_text':_analysed}
#     return render(request, 'analyse.html', parameters)
#     #return HttpResponse("Remove Punctuation")


# def capitalizefirst(request):
#     djtext = request.GET.get('text', 'default')
#     _analysed = ""
#     for word in djtext.split():
#         word = word.capitalize()
#         _analysed += word + "  "
#     print(_analysed)
#     parameters = {'purpose':'Capitalizing first letter of the word', 'analysed_text':_analysed}
#     return render(request, 'analyse.html', parameters)

#     #return HttpResponse('''<a href='/'>Go Back</a> <br> Capitalize First''')
