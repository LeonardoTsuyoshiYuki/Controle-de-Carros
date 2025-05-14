from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarForm

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

def create_cars_view(request):
    if request.method == 'POST':
        create_car_form = CarForm(request.POST, request.FILES)
        if create_car_form.is_valid():
            create_car_form.save()
            return redirect('cars_list')
    else:
        create_car_form = CarForm()
    return render(request, 'create_car.html', {'create_car_form': create_car_form})