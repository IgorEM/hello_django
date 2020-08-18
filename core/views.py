from django.shortcuts import render, HttpResponse

# Create your views here.
#os dados da requisição que são enviados pra mim
#http response interpreta os colocar como parametro e vai jogar como resposta http
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos </h1>'.format(nome, idade))

