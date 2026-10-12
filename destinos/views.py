from django.shortcuts import render, redirect
from .models import Destino
from .forms import DestinoForm


def inicio(request):
    return render(request, 'paginas/inicio.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def destinos_list(request):
    destinos = Destino.objects.all()
    return render(request, 'destinos/index.html', {'destinos': destinos})


def crear_destino(request):
    formulario = DestinoForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('destinos')

    return render(
        request,
        'destinos/crear.html',
        {'formulario': formulario}
    )


def editar_destino(request, id):
    destino = Destino.objects.get(id=id)

    formulario = DestinoForm(
        request.POST or None,
        request.FILES or None,
        instance=destino
    )

    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('destinos')

    return render(
        request,
        'destinos/editar.html',
        {'formulario': formulario}
    )


def eliminar_destino(request, id):
    destino = Destino.objects.get(id=id)
    destino.delete()
    return redirect('destinos')


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import DestinoSerializer
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', 'POST'])
def api_destinos(request):
    if request.method == 'GET':
        destinos = Destino.objects.all()
        serializer = DestinoSerializer(
            destinos, many=True, context={'request': request}
        )
        return Response(serializer.data)

    elif request.method == 'POST':
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Debes iniciar sesion para crear un destino.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = DestinoSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



@api_view(['GET', 'PUT', 'DELETE'])
def api_destino_detalle(request, id):
    try:
        destino = Destino.objects.get(pk=id)
    except Destino.DoesNotExist:
        return Response(
            {'error': 'Destino no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = DestinoSerializer(
            destino, context={'request': request}
        )
        return Response(serializer.data)

    elif request.method == 'PUT':
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Debes iniciar sesion para actualizar un destino.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        serializer = DestinoSerializer(
            destino,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response(
                {'detail': 'Debes iniciar sesion para eliminar un destino.'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        destino.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
