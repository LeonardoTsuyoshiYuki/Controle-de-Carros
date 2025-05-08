from django.db import models

# Criando a classe de Marca para o Banco de dados.
class Brand(models.Model):
    id = models.AutoField (primary_key = True)
    name = models.CharField (max_length = 200)
    
    #Definindo a o padrão de exibição do tabela Brand, para Nome do carro
    def __str__(self):
        return self.name

# Criando a classe de Carros para o Banco de dados.
class Car(models.Model):
    
    id =  models.AutoField (primary_key=True)
    model = models.CharField (max_length=200)
    #Criando um select e vinculando a classe Brand, e protegento caso delete um Marca vinculado ao um carro cadastrado.
    brand = models.ForeignKey (Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=200, blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField (blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    #Definindo a o padrão de exibição do tabela Car, para Modelos
    def __str__(self):
        return self.model   
