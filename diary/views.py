from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.views.generic import (
    View,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Country, Visit, Diary
from to_do_list.models import ToDoList
from .forms import VisitForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import Count


class MapView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request):

        country_code_list = ['AL', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CZ',
                             'DK', 'EE', 'FI', 'FR', 'DE', 'GR', 'HU', 'IS',
                             'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'MD', 'ME',
                             'NL', 'NO', 'PL', 'PT', 'RO', 'RS', 'SK', 'SI',
                             'ES', 'SE', 'CH', 'UA', 'GB']

        """
        loop through country codes and create a country dict
        using codes as dict key
        """
        dict = {}
        for country_code in country_code_list:
            key = country_code
            dict[key] = Country.objects.get(code=country_code)

            """
            loop through country codes and if country has status
            assign assign the status to the value else assign
            not visited
            """
            status_dict = {}
            if dict[key].country_map.filter(user=request.user.id).exists():
                key = f"{country_code}_status"
                status_dict[key] = dict[country_code].country_map.get(
                    user=request.user.id)
            else:
                key = f"{country_code}_status"
                status_dict[key] = "not_visited"

            # MERGE DICTIONARIES -
            # https://favtutor.com/blogs/merge-dictionaries-python#:~:text=You%20can%20merge%20two%20dictionaries,other%20one%20by%20overwriting%20it.
            dict.update(status_dict)

        """
        get countries, visited countries and wish list countries and
        assign to dict
        """
        countries = Country.objects.all()
        visited_countries = Visit.objects.filter(user=request.user.id)
        visited_countries_wish_list = visited_countries.filter(
            status="wish_list")
        visited_countries_travelled_to = visited_countries.filter(
            status="visited")

        dict['countries'] = countries
        dict['visited_countries'] = visited_countries
        dict['visited_countries_wish_list'] = visited_countries_wish_list
        dict['visited_countries_travelled_to'] = visited_countries_travelled_to

        # get data for pie chart
        t_countries = countries.count()
        t_visited = visited_countries_travelled_to.count()
        t_wish = visited_countries_wish_list.count()

        remaining_countries = t_countries - t_visited - t_wish

        labels = ["wish List", "Visited", "Not Visited"]
        data = [
            t_wish,
            t_visited,
            remaining_countries]

        percentage_visited = round(
            (t_visited / t_countries) * 100, 2)

        dict.update({"labels": labels,
                     "data": data,
                     "percentage_visited": percentage_visited,
                     "tab_title": "Map"})

        return render(request, "diary/map.html", dict)


class CountryView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk, *args, **kwargs):
        countries = Country.objects.all()
        country = get_object_or_404(countries, pk=pk)
        lists = ToDoList.objects.filter(user=request.user, country=country)
        visited = Visit.objects.filter(user_id=request.user.id)

        # country has visit_status
        if visited.filter(country=country).exists():
            country_visited = visited.get(country=country)

            return render(
                request,
                "diary/country.html",
                {
                    "country": country,
                    "visit_form": VisitForm(instance=country_visited),
                    'lists': lists,
                    "tab_title": "Country Info"
                },
            )
        # country does not have visit_status
        else:
            return render(
                request,
                "diary/country.html",
                {
                    "country": country,
                    "visit_form": VisitForm(),
                    'lists': lists,
                    "tab_title": "Country Info"

                },
            )

    def post(self, request, pk, *args, **kwargs):
        countries = Country.objects.all()
        country = get_object_or_404(countries, pk=pk)
        visited = Visit.objects.filter(user_id=request.user.id)

        # add visit_status
        if visited.filter(country=country).exists():
            country_visited = visited.get(country=country)

            visit_form = VisitForm(data=request.POST)
            if visit_form.is_valid():
                visit_form.instance.user_id = request.user.id
                visit_form.instance.country = country
                visit_form.instance.id = country_visited.id
                country_visited = visit_form.save(commit=False)
                country_visited.save()
            else:
                visit_form = VisitForm()

        # update visit_status
        else:
            visit_form = VisitForm(data=request.POST)
            if visit_form.is_valid():
                visit_form.instance.user_id = request.user.id
                visit = visit_form.save(commit=False)
                visit.country = country
                visit.save()
            else:
                visit_form = VisitForm()

        url = reverse('country', args=[country.pk])
        return redirect(
            f'{url}#visited_list_location'
        )


class DiaryAllPostsView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        diary_posts = Diary.objects.filter(
            country=country, author=request.user)

        # filter results
        if request.GET.get('q') is not None:
            q = request.GET.get('q')
        else:
            q = ""

        diary_posts = diary_posts.filter(
            Q(content__icontains=q) |
            Q(tags__name__icontains=q) |
            Q(exp_rating__icontains=q)
        )

        # stop tag duplication
        diary_posts = diary_posts.distinct()

        # pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(diary_posts, 2)

        try:
            diary_posts = paginator.page(page)
        except PageNotAnInteger:
            diary_posts = paginator.page(1)
        except EmptyPage:
            diary_posts = paginator.page(paginator.num_pages)

        return render(
            request,
            "diary/diary-posts.html",
            {
                "diary_posts": diary_posts,
                "country": country,
                "search_query": q,
                "tab_title": "Diary Posts"
            }
        )


class DiaryTagsView(LoginRequiredMixin, View):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        country = get_object_or_404(Country, pk=pk)
        diary_posts = Diary.objects.filter(
            country=country, author=request.user)

        # list out tags in order of user
        tags_list = diary_posts.values('tags__name').annotate(
            count=Count('tags__name')).order_by('-count')
        tags_list = tags_list.exclude(
            tags__name__isnull=True).exclude(
            tags__name='')

        # pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(tags_list, 5)

        try:
            tags_list = paginator.page(page)
        except PageNotAnInteger:
            tags_list = paginator.page(1)
        except EmptyPage:
            tags_list = paginator.page(paginator.num_pages)

        return render(
            request,
            "diary/diary-tags.html",
            {
                "country": country,
                "tags": tags_list,
                "tab_title": "Diary Tags"
            }
        )


class DiaryCreateView(
        LoginRequiredMixin,
        CreateView):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    model = Diary
    fields = ['content', 'content_image', 'tags', 'exp_rating']

    def form_valid(self, form):
        country = get_object_or_404(Country, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.country = country

        """
        Convert tag names to uppercase to avoid duplication based
        on case sensitivity
        """
        tag_names = form.cleaned_data.get('tags')
        if tag_names:
            for i, tag_name in enumerate(tag_names):
                tag, created = Tag.objects.get_or_create(name=tag_name.upper())
                tag_names[i] = tag.name

        response = super().form_valid(form)

        # create no_tags tag if not tag added to be filtered against
        tags = form.instance.tags.all()
        if not tags.exists():
            no_tags = Tag.objects.get_or_create(name='NO TAGS')[0]
            form.instance.tags.add(no_tags)

        return response


class DiaryUpdateView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        UpdateView):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    model = Diary
    fields = ['content', 'content_image', 'tags', 'exp_rating']

    # form validation
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # restrict if request user is not author
    def test_func(self):
        diary_post = self.get_object()
        if self.request.user == diary_post.author:
            return True
        return False


class DiaryDeleteView(
        LoginRequiredMixin,
        UserPassesTestMixin,
        DeleteView):
    login_url = '/login/required'
    redirect_field_name = 'redirect_to'

    model = Diary
    context_object_name = 'diary'

    # on success go to diary posts
    def get_success_url(self):
        diary = self.get_object()
        return reverse('diary-all-posts', args=[str(diary.country.id)])

    # restrict if request user is not author
    def test_func(self):
        diary = self.get_object()
        if self.request.user == diary.author:
            return True
        return False
