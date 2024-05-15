from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .serializers import AdditionRequestSerializer, AdditionResponseSerializer
from .utils import add_lists, logger


class AdditionController(APIView):
    def post(self, request):
        logger.info(f"Received request: {request.data}")

        serializer = AdditionRequestSerializer(data=request.data)
        if serializer.is_valid():
            try:
                batchid = serializer.validated_data['batchid']
                payloada = serializer.validated_data['payloada']
                started_at = datetime.utcnow()

                result = add_lists(payloada)
                completed_at = datetime.utcnow()

                response_data = {
                    'batchid': batchid,
                    'response': result,
                    'status': 'complete',
                    'started_at': started_at,
                    'completed_at': completed_at
                }

                response_serializer = AdditionResponseSerializer(response_data)
                logger.info(f"Response: {response_serializer.data}")
                return Response(response_serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                logger.error(f"Error occurred: {e}")
                return Response({"detail": "An error occurred while processing the request"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
