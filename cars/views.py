from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    
    #Busca todos os objetos de carros e esta ordenando por modelos de A - Z, caso coloque '-model' o sinal de menos, oredena de Z - A
    cars = Car.objects.all().order_by('model')
    #Fazendo uma requisição na barra de pesquisa
    search = request.GET.get('search')

    #Condição para saber se o usuário passou uma requisição
    if search:
        #fazendo a requisição com o parametro passado no Search
        cars = cars.filter(model__icontains=search)

    #rendelizando os dados
    return render(
        request,
        'cars.html',
        {'cars': cars}
    )
