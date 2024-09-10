from django import forms

class TravelPreferenceForm(forms.Form):
    GROUP_TYPE_CHOICES = [
        ('solo', 'Solo'),
        ('family', 'Family'),
        ('friends', 'Friends'),
    ]
    TRANSPORTATION_CHOICES = [
        ('public_transport', 'Public Transport'),
        ('rental', 'Rental'),
        ('guide','Guide'),
    ]
    ACCOMMODATION_CHOICES = [
        ('budget', 'Budget'),
        ('luxury', 'Luxury'),
        ('homestay', 'Homestay'),
    ]
    OUTDOOR_ADVENTURES_CHOICES = [
        ('trekking', 'Trekking'),
        ('hiking', 'Hiking'),
        ('water_sports', 'Water Sports'),
    ]
    CULTURAL_EXPERIENCES_CHOICES = [
        ('holy_places', 'Holy Places'),
        ('museums', 'Museums'),
        ('forts', 'Forts'),
    ]
    SPECIFIC_CUISINE_CHOICES = [
        ('north_indian', 'North Indian'),
        ('south_indian', 'South Indian'),
        ('italian', 'Italian'),
        ('local_food', 'Local Food'),
    ]

    group_type = forms.ChoiceField(choices=GROUP_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    transportation = forms.ChoiceField(choices=TRANSPORTATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    accommodation = forms.ChoiceField(choices=ACCOMMODATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    outdoor_adventures = forms.ChoiceField(choices=OUTDOOR_ADVENTURES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    cultural_experiences = forms.ChoiceField(choices=CULTURAL_EXPERIENCES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    specific_cuisine = forms.ChoiceField(choices=SPECIFIC_CUISINE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    num_days = forms.IntegerField(label='Enter number of days', widget=forms.NumberInput(attrs={'class': 'form-control'}))

# class InterestsAndActivitiesForm(forms.Form):
#     OUTDOOR_ADVENTURES_CHOICES = [
#         ('trekking', 'Trekking'),
#         ('hiking', 'Hiking'),
#         ('water_sports', 'Water Sports'),
#     ]
#     CULTURAL_EXPERIENCES_CHOICES = [
#         ('holy_places', 'Holy Places'),
#         ('museums', 'Museums'),
#         ('forts', 'Forts'),
#     ]
#     SPECIFIC_CUISINE_CHOICES = [
#         ('north_indian', 'North Indian'),
#         ('south_indian', 'South Indian'),
#         ('italian', 'Italian'),
#         ('local_food', 'Local Food'),
#     ]

#     outdoor_adventures = forms.ChoiceField(choices=OUTDOOR_ADVENTURES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
#     cultural_experiences = forms.ChoiceField(choices=CULTURAL_EXPERIENCES_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
#     specific_cuisine = forms.ChoiceField(choices=SPECIFIC_CUISINE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
