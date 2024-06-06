from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer


# Create your views here.

@api_view(['GET','POST'])
def index(request):
    course = {
        'name': 'Python',
        'frameworks':['django', 'django rest framework','fast api'],
        'course_provider': 'youtube'
    }
    if request.method == 'GET':
        q=dict(request.query_params)
        print(f'params: {q.keys()}')
        print(request.GET.get('name'))
        print('you have hit a GET method')
    elif request.method == 'POST':
        data = request.data
        print('***************')
        print(data)
        print('you have hit a POST method')
    elif request.method == 'PUT':
        print('you have hit a PUT method')
    return Response(course)


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many = True)

        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors)   
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        obj = Person.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'Person deleted successfully'})

