from rest_framework.serializers import ModelSerializer
from handle_games_using_api_app.models import   GamesSet


class GameSerializer(ModelSerializer):
    class Meta:
        model = GamesSet
        fields = ['name','creator','player','subscriber']