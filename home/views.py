from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer
from rest_framework import status


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
        person = Person.objects.all()
        serializer = PeopleSerializer(person, many = True)

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
        person = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(person,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors)   
    
    elif request.method == 'PATCH':
        data = request.data
        person = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(person,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        person = Person.objects.get(id=data['id'])
        person.delete()
        return Response({'message':'Person deleted successfully'})
    

@api_view(['GET','PUT','DELETE'])
def persondetails(request,pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)
        return Response('NOT_FOUND')

    if request.method == 'GET':
        serializer = PeopleSerializer(person)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PeopleSerializer(person, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status.HTTP_204_NO_CONTENT)



