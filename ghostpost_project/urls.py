"""ghostpost_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from ghostpost_api import views as api_views

router = routers.DefaultRouter()
router.register(r"post",api_views.PostViewSet)

# router.register(r"shoecolors",api_views.ShoeColorSet)
# router.register(r"shoetype",api_views.ShoeTypeSet)
# router.register(r"manufacturer",api_views.ManufacturerTypeSet)


# urlpatterns = [
#     path('', views.index, name="homepage"),
#     path('add_post/', views.createpost_view, name="addpost"),
#     path('roast/', views.roast_view, name="roast"),
#     path('boast/', views.boast_view, name="roast"),
#     path('sorted_by/', views.sorted_view, name="sortedby"),
#     path('upvote/<int:upvote_id>', views.upvote_view, name="upvote_page"),
#     path('downvote/<int:downvote_id>', views.downvote_view, name="downvote_page"),
#     path('detail/<str:sec_key>', views.detail_view, name="detail_page"),
#     path('deletepost/<int:post_id>', views.delete_view, name="delete_page"),
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),

]


