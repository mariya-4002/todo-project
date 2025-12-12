from .serializers import TodoRequestSerializer, TodoIdSerializer
from .dataclass import TodoData

def parse_create_request(data):
    serializer = TodoRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return TodoData(**serializer.validated_data)

def parse_update_request(data):
    serializer = TodoRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return TodoData(**serializer.validated_data)

def parse_id_request(data):
    serializer = TodoIdSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data['id']
