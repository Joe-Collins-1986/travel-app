from django.shortcuts import render
from django.views.generic import (
    View,
)
from .models import Country, Visit


class MapView(View):

    def get(self, request):

        country_code_list = ['AL', 'BY', 'BE', 'BA', 'BG', 'HR', 'CZ', 'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IS',
                             'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'MD', 'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'SK',
                             'SI', 'ES', 'SE', 'CH', 'UA', 'GB']

        dict = {}
        for country_code in country_code_list:
            key = country_code
            dict[key] = Country.objects.get(code=country_code)

            status_dict = {}
            if dict[key].country_map.filter(user=request.user.id).exists():
                key = f"{country_code}_status"
                status_dict[key] = dict[country_code].country_map.get(user=request.user.id)
            else:
                key = f"{country_code}_status"
                status_dict[key] = "not_visited"

            dict.update(status_dict) # MERGE DICTIONARIES - https://favtutor.com/blogs/merge-dictionaries-python#:~:text=You%20can%20merge%20two%20dictionaries,other%20one%20by%20overwriting%20it.

        countries = Country.objects.all()
        visited_countries = Visit.objects.filter(user=request.user.id)

        dict['countries'] = countries
        dict['visited_countries'] = visited_countries
            
        return render(request, "diary/map.html", dict)