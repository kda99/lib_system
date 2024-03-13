from django.http import JsonResponse
import asyncio
from rest_framework import viewsets, status
from rest_framework.response import Response
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

    async def create(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()

            # Асинхронное ожидание в течение 60 секунд
            await asyncio.sleep(60)

            return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        serialized_event = EventSerializer(event).data
        organizations_info = {}

        for organization in event.organizations.all():
            users_info = []
            for user in organization.user_set.all():
                users_info.append(user.id)

            organization_info = {
                'users': users_info,
                'postal_code': organization.postcode,
                'address': organization.address
            }
            organizations_info[organization.title] = organization_info

        serialized_event['organizations_info'] = organizations_info
        return JsonResponse(serialized_event)