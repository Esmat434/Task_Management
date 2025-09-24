from rest_framework import serializers

from .models import (
    Category,Board,Task
)

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'user','title','created_at'
        )
        extra_kwargs = {
            'user':{'read_only':True},
            'title':{'required':True},
            'created_at':{'read_only':True}
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)

    def validate_title(self,title):
        if Category.objects.filter(title=title, user=self.user).exists():
            raise serializers.ValidationError("This title already exists.")
        
        return title
    
    def create(self, validated_data):
        validated_data['user'] = self.user
        return super().create(validated_data)
    
class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title',
        )
        extra_kwargs = {
            'title':{'required':True}
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
    
    def validate_title(self,title):
        if Category.objects.filter(title=title, user=self.user).exclude(id=self.instance.pk).exists():
            raise serializers.ValidationError("This title already exists.")
        return title

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'user','title','category','created_at'
        )
        extra_kwargs = {
            'user':{'read_only':True},
            'title':{'required':True},
            'category':{'required':False},
            'created_at':{'read_only':True}
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
    
    def validate_title(self,title):
        if Board.objects.filter(title=title, user=self.user).exists():
            raise serializers.ValidationError("This title already exists.")
        return title
    
    def create(self, validated_data):
        validated_data['user'] = self.user
        return super().create(validated_data)

class BoardUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'title','category','created_at'
        )
        extra_kwargs = {
            'title':{'required':True},
            'category':{'required':False},
            'created_at':{'read_only':True}
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
    
    def validate_title(self,title):
        if Board.objects.filter(title=title, user=self.user).exclude(pk=self.instance.pk).exists():
            raise serializers.ValidationError("This title already exists.")
        return title

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'user','board','title','description','status','published_at','created_at'
        )
        extra_kwargs = {
            'user':{'read_only':True},
            'board':{'required':True},
            'title':{'required':True},
            'description':{'required':False},
            'status':{'required':False},
            'published_at':{'read_only':True},
            'created_at':{'read_only':True}
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
    
    def validate_title(self,title):
        if Task.objects.filter(title=title, user=self.user).exists():
            raise serializers.ValidationError("This title already exists.")
        return title
    
    def create(self, validated_data):
        validated_data['user'] = self.user
        return super().create(validated_data)

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title','board','description','status'
        )
        extra_kwargs = {
            'title':{'required':True},
            'board':{'required':True},
            'description':{'required':False},
            'status':{'required':False}
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
    
    def validate_title(self,title):
        if Task.objects.filter(title=title, user=self.user).exclude(pk=self.instance.id).exists():
            raise serializers.ValidationError("This title already exists.")
        return title   