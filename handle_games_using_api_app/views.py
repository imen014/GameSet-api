from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from handle_games_using_api_app.serializers import GameSerializer
from handle_games_using_api_app.models import GamesSet


class Paginator(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000

class GameView(ModelViewSet):

    serializer_class = GameSerializer
    def get_queryset(self,*args,**kwargs):
        pagination_class = Paginator
        creator = self.request.GET.get('creator')
        queryset = GamesSet.objects.filter()
        if creator:
            queryset = queryset.filter(creator=creator)
        return queryset