from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()

    worddict = {}
    for word in wordcount:
        if word in worddict:
            #increase
            worddict[word] += 1
        else:
            #add to dictionary
            worddict[word] = 1
        sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordcount),'sortedwords':sortedwords})
def about(request):
    return render(request,'about.html')
