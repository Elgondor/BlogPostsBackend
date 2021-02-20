from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status

class ListPosts(generics.ListAPIView):
    # serializer_class = PostSerializer
    http_method_names = ['get']
    def get_queryset(self):
        queryset = Post.objects.all()
        tags = self.request.query_params.get('tags', None)
        sortBy = 'id'
        direction = ''
        if tags is not None:
            tagsList = tags.split(',')
            for tag in tagsList:
                queryset = queryset.filter(tags__name=tag)

        if self.request.query_params.get('sortBy', None) is not None:
            sortBy = self.request.query_params.get('sortBy', None)
            if self.request.query_params.get('direction', None) == 'desc':
                direction = '-'
        queryset = queryset.order_by(direction + sortBy)
        return queryset
        # context = {'error': 'something happen', 'success': "false", 'message': 'Failed To Get contents.'}
        # return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def check_sort_by(self, value):
        sort_by = 'id'
        if value not in ('reads', 'likes', 'popularity'):
            sort_by = value
        return sort_by

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)

        # append serializer's data with some additional value
        response_list = [{
            'posts':serializer.data
        }]
        return Response(response_list)


        