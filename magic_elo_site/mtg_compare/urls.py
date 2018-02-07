from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cardrankings/', views.CardRankingListView.as_view(), name='cardrankings'),
    path('cardrankings/<int:pk>', views.CardRankingDetailView.as_view(), name='cardranking-detail'),
]