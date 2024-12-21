from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClickDataSerializer

from .models import ClickData
class ClickView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        click_data, created = ClickData.objects.get_or_create(user=user)
        click_data.clicks += 1
        click_data.save()
        return Response({"message": "Click registered!", "clicks": click_data.clicks}, status=status.HTTP_200_OK)

class LeaderboardView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        leaderboard = ClickData.objects.order_by('-clicks')[:10]  # Top 10 users
        serializer = ClickDataSerializer(leaderboard, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)