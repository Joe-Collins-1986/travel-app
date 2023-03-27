from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include("home.urls")),
    path('updates/', include("site_updates.urls")),
    path('diary/', include("diary.urls")),
    path('profile/', include("user_profile.urls")),
    path('to_do/', include("to_do_list.urls")),
]

handler404 = "travel_app.views.page_not_found_view"
handler500 = "travel_app.views.my_custom_error_view"
handler403 = 'travel_app.views.error_403'
handler400 = "travel_app.views.my_custom_bad_request_view"
