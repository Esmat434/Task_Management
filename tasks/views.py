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

class CategoryCreateListView(APIView):
    """
    Retrieve or create categories for the authenticated user.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request):
        """
        Retrieve all categories owned by the authenticated user.
        Returns a list of category objects.
        """
        categories = Category.objects.filter(user=request.user)
        serializer = CategoryCreateSerializer(categories, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        """
        Create a new category for the authenticated user.

        Expected JSON body:
        - title (string): The name of the category.

        Returns the created category object.
        """
        serilalizer = CategoryCreateSerializer(data=request.data, user=request.user)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data, status=status.HTTP_201_CREATED)
        return Response(serilalizer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailUpdateDestroyView(APIView):
    """
    Retrieve, update, or delete a specific category.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        """
        Retrieve a category by its ID for the authenticated user.
        """
        category = get_object_or_404(Category, id=pk, user=request.user)
        serializer = CategoryCreateSerializer(category, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        """
        Update an existing category by its ID.

        Expected JSON body:
        - title (string): Updated category name.
        """
        category = get_object_or_404(Category, id=pk, user=request.user)
        serializer = CategoryUpdateSerializer(instance=category, data=request.data, user=request.user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
        Delete a category by its ID.
        """
        category = get_object_or_404(Category, id=pk, user=request.user)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BoardCreateListView(APIView):
    """
    Retrieve or create boards for the authenticated user.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request):
        """
        Retrieve all boards created by the authenticated user.
        """
        boards = Board.objects.filter(user=request.user)
        serializer = BoardCreateSerializer(boards, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        """
        Create a new board.

        Expected JSON body:
        - title (string): The name of the board.
        - category (int): Category ID related to this board.
        """
        serializer = BoardCreateSerializer(data=request.data, user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetailUpdateDestroyView(APIView):
    """
    Retrieve, update, or delete a specific board.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        """
        Retrieve a board by its ID for the authenticated user.
        """
        board = get_object_or_404(Board, id=pk, user=request.user)
        serializer = BoardCreateSerializer(board, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        """
        Update a board.

        Expected JSON body:
        - title (string): Updated title.
        - category (int): Updated category ID.
        """
        board = get_object_or_404(Board, id=pk, user=request.user)
        serializer = BoardUpdateSerializer(instance=board, data=request.data, user=request.user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        """
        Delete a board by its ID.
        """
        board = get_object_or_404(Board, id=pk, user=request.user)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskCreateListView(APIView):
    """
    Retrieve or create active (enabled) tasks for the authenticated user.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request):
        """
        Retrieve all active tasks (status = Enable).
        """
        tasks = Task.objects.filter(user=request.user, status=Task.TaskStatus.enable)
        serializer = TaskCreateSerializer(tasks, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        """
        Create a new task.

        Expected JSON body:
        - title (string): Task title
        - description (string): Task details
        - board (int): Board ID
        - status (string): "Enable" or "Disable"
        """
        serializer = TaskCreateSerializer(data=request.data, user=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDisableListView(APIView):
    """
    Retrieve all disabled tasks for the authenticated user.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request):
        """
        Retrieve all tasks where status = Disable.
        """
        tasks = Task.objects.filter(user=request.user, status=Task.TaskStatus.disable)
        serializer = TaskCreateSerializer(tasks, many=True, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TaskDisableDetailView(APIView):
    """
    Retrieve details of a disabled task by its ID.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        """
        Retrieve a disabled task by its ID.
        """
        task = get_object_or_404(Task, id=pk, user=request.user, status=Task.TaskStatus.disable)
        serializer = TaskCreateSerializer(task, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TaskDetailUpdateDestroyView(APIView):
    """
    Retrieve, update, or delete a specific active task.
    """

    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        """
        Retrieve a task by its ID (status = Enable).
        """
        task = get_object_or_404(Task, id=pk, user=request.user, status=Task.TaskStatus.enable)
        serializer = TaskCreateSerializer(task, user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,pk):
        """
        Update an existing task.

        Expected JSON body:
        - title (string)
        - description (string)
        - board (int)
        - status (string)
        """
        task = get_object_or_404(Task, id=pk, user=request.user)
        serializer = TaskUpdateSerializer(instance=task, data=request.data, user=request.user, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        """
        Delete a task by its ID.
        """
        task = get_object_or_404(Task, id=pk, user=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
