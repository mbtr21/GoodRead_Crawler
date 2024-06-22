from rest_framework import generics
from .tasks import process_data_task  # Import the task
from rest_framework.response import Response
from rest_framework import status
from .serializers import SearchSerializer
from .models import Search
# Assuming process_data_task is properly imported


class SearchDetailView(generics.ListCreateAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

    def perform_create(self, serializer):
        # Here you can access the validated data
        if serializer.is_valid():
            selection = str(serializer.validated_data['category'])
            search = str(serializer.validated_data['search_bar'])
            print(selection, search)  # Example: Print the validated data to the console
            # Assuming process_data_task is an asynchronous task function
            process_data_task.delay(search, selection)

            return Response({"message": "Task is being processed"}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()





