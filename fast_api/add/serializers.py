from rest_framework import serializers

class AdditionRequestSerializer(serializers.Serializer):
    batchid = serializers.CharField(max_length=100)
    payloada = serializers.ListField(
        child=serializers.ListField(
            child=serializers.IntegerField()
        )
    )

class AdditionResponseSerializer(serializers.Serializer):
    batchid = serializers.CharField(max_length=100)
    response = serializers.ListField(child=serializers.IntegerField())
    status = serializers.CharField(max_length=10)
    started_at = serializers.DateTimeField()
    completed_at = serializers.DateTimeField()
