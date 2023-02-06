from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.models import User
from django.views.generic import (
    View,
    ListView,
    DetailView,
)
from .models import Country, Visit
from .forms import VisitForm


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

            # globals().update(status_dict) # https://stackoverflow.com/questions/18090672/convert-dictionary-entries-into-variables
            dict.update(status_dict) # MERGE DICTIONARIES - https://favtutor.com/blogs/merge-dictionaries-python#:~:text=You%20can%20merge%20two%20dictionaries,other%20one%20by%20overwriting%20it.

        # globals().update(dict)
        countries = Country.objects.all()
        visited_countries = Visit.objects.filter(user=request.user.id)

        dict['countries'] = countries
        dict['visited_countries'] = visited_countries
            
        return render(request, "map/home.html", dict)
    

class CountryView(View):

    def get(self, request, pk):
        countries = Country.objects.all()
        country = get_object_or_404(countries, pk=pk)

        visited = Visit.objects.filter(user_id=request.user.id)

        if visited.filter(country=country).exists():
            country_visited = visited.get(country=country)

            return render(
                    request,
                    "map/country.html",
                    {
                        "country": country,
                        "visit_form": VisitForm(instance=country_visited)
                    },
            )
        else:
            return render(
                    request,
                    "map/country.html",
                    {
                        "country": country,
                        "visit_form": VisitForm()
                    },
            )

    def post(self, request, pk, *args, **kwargs):
        countries = Country.objects.all()
        country = get_object_or_404(countries, pk=pk)
        visited = Visit.objects.filter(user_id=request.user.id)

        print(visited)

        if visited.filter(country=country).exists():
            country_visited = visited.get(country=country)

            visit_form = VisitForm(data=request.POST)
            if visit_form.is_valid():
                visit_form.instance.user_id = request.user.id
                visit_form.instance.country = country
                visit_form.instance.id = country_visited.id
                country_visited = visit_form.save(commit=False)
                country_visited.save()
                print(country_visited.id)
            else:
                visit_form = VisitForm()

        else:
            visit_form = VisitForm(data=request.POST)
            if visit_form.is_valid():
                visit_form.instance.user_id = request.user.id
                visit = visit_form.save(commit=False)
                visit.country = country
                visit.save()
            else:
                visit_form = VisitForm()

        return HttpResponseRedirect(reverse('country', args=[pk]))
