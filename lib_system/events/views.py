from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Event
from .serializers import EventSerializer
from django.db.models import Q
from .models import Event
from rest_framework.pagination import PageNumberPagination


class EventPagination(PageNumberPagination):
    page_size = 2


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = EventPagination

    def list(self, request):
        search_query = request.GET.get('search', '')
        date_order = request.GET.get('date_order', 'asc')

        events = Event.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

        if date_order == 'asc':
            events = events.order_by('date')
        else:
            events = events.order_by('-date')

        page = self.paginate_queryset(events)
        serializer = EventSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

def create(self, request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)