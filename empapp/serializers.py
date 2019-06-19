from rest_framework import serializers

class EmpSeriallizer(serializers.Serializer):
    ename=serializers.CharField(max_length=20)
    email=serializers.EmailField(max_length=50)
