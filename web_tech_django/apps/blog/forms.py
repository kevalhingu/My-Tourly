from .models import Tour, Customer, Hotel
from django.forms import ModelForm, TextInput, Textarea, NumberInput, DateInput


class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = "__all__"
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter the name'
            }),
            "description": Textarea(attrs={
                'class': 'form-control', 'placeholder': 'Enter the description'
            }),
            "started": DateInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter started date', 'type': 'date'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter price of the tour'
            }),
            "duration": NumberInput(attrs={
                'class': 'form-control', 'placeholder': 'Enter duration'
            }),
        }


class HotelForm(ModelForm):
    class Meta:
        model = Hotel
        fields = "__all__"
        # widgets = {
        #     "name": TextInput(attrs={
        #         'class': 'form-control', 'placeholder': 'Enter the name of Hotel'
        #     }),
        #     "city": Textarea(attrs={
        #         'class': 'form-control', 'placeholder': 'Enter the city'
        #     }),
        #     "hotelClass": DateInput(attrs={
        #         'class': 'form-control', 'placeholder': 'Enter the class of a hotel'
        #     }),
        #     "price": NumberInput(attrs={
        #         'class': 'form-control', 'placeholder': 'Enter price of the hotel to the one person'
        #     }),
        # }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        widgets = {
            "phone": TextInput(attrs={'class':'form-control'}),
            "place": TextInput(attrs={'class': 'form-control'}),
        }