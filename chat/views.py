from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChatSerializer
from .models import generate_response


class ChatView(APIView):
    def post(self, request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.validated_data['question']
            response = generate_response(question) 
            serializer.validated_data['response'] = response
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=400)
