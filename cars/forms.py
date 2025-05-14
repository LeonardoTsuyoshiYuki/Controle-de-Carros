from django import forms
from cars.models import Car

#Metodo ModelForm
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        #Utiliza o Model para cadastrar um novo carro
        fields = '__all__'
    
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error( 'value', 'Valor minimo do carro deve ser de R$ 20.000') 
        return value       
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não e possivel cadastrar carros fabricados antes de 1975')
        return factory_year

    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year < 1975:
            self.add_error('model_year', 'Não é possivel cadastrar carros com o ano de fabricação menor de o ano do modelo')
        return model_year    
#Metodo Form
'''
class CarForm(forms.Form):   
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()
    def save(self):
        car = Car( 
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
'''