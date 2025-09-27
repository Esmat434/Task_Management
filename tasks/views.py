from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import (
    Category,Board,Task
)

from .serializers import (
    CategoryCreateSerializer,CategoryUpdateSerializer,BoardCreateSerializer,BoardUpdateSerializer,
    TaskCreateSerializer,TaskUpdateSerializer
)

class CategoryCreateListView(IsAuthenticated,APIView):
    def get(self,request):
        categories = Category.objects.filter(user=request.user)
        serializer = CategoryCreateSerializer(categories, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serilalizer = CategoryCreateSerializer(data=request.data, user=request.user)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_201_CREATED)
        return Response(serilalizer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailUpdateDestroyView(IsAuthenticated,APIView):
    def get(self,request,pk):
        category = get_object_or_404(Category, id=pk, user=request.user)
        serializer = CategoryCreateSerializer(category, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        category = get_object_or_404(Category, id=pk, user=request.user)
        serializer = CategoryUpdateSerializer(instance=category, data=request.data, user=request.user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        category = get_object_or_404(Category, id=pk, user=request.user)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BoardCreateListView(IsAuthenticated,APIView):
    def get(self,request):
        boards = Board.objects.filter(user=request.user)
        serializer = BoardCreateSerializer(boards, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = BoardCreateSerializer(data=request.data, user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetailUpdateDestroyView(IsAuthenticated,APIView):
    def get(self,request,pk):
        board = get_object_or_404(Board, id=pk, user=request.user)
        serializer = BoardCreateSerializer(board, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        board = get_object_or_404(Board, id=pk, user=request.user)
        serializer = BoardUpdateSerializer(instance=board, data=request.data, user=request.user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        board = get_object_or_404(Board, id=pk, user=request.user)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskCreateListView(IsAuthenticated,APIView):
    def get(self,request):
        tasks = Task.objects.filter(user=request.user, status=Task.TaskStatus.enable)
        serializer = TaskCreateSerializer(tasks, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = TaskCreateSerializer(data=request.data, user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDisableListView(IsAuthenticated,APIView):
    def get(self,request):
        tasks = Task.objects.filter(user=request.user, status=Task.TaskStatus.disable)
        serializer = TaskCreateSerializer(tasks, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TaskDisableDetailView(IsAuthenticated,APIView):
    def get(self,request,pk):
        task = get_object_or_404(Task, id=pk, user=request.user, status=Task.TaskStatus.disable)
        serializer = TaskCreateSerializer(task, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TaskDetailUpdateDestroyView(IsAuthenticated,APIView):
    def get(self,request,pk):
        task = get_object_or_404(Task, id=pk, user=request.user, status=Task.TaskStatus.enable)
        serializer = TaskCreateSerializer(task, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        task = get_object_or_404(Task, id=pk, user=request.user)
        serializer = TaskUpdateSerializer(instance=task, data=request.data, user=request.user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        task = get_object_or_404(Task, id=pk, user=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
