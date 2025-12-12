from rest_framework import serializers
from .dataclass import TodoData
from .models import Todo


class TodoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()

    # Validation example
    def validate_title(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Title cannot be empty")
        return value

    # Convert validated data → dataclass object
    def to_dataclass(self):
        return TodoData(
            title=self.validated_data["title"],
            description=self.validated_data["description"]
        )

    # CREATE OPERATION (returns dataclass)
    def create(self):
        return self.to_dataclass()

    # UPDATE OPERATION (returns dataclass)
    def update(self, instance):
        data = self.validated_data
        return TodoData(
            title=data.get("title", instance.title),
            description=data.get("description", instance.description)
        )
