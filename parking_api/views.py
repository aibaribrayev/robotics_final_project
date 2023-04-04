from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Parking
from .serializers import ParkingSerializer

class ParkingDetailApiView(APIView):
    def get_object(self, lot_id):
        try:
            return Parking.objects.get(id=lot_id)
        except Parking.DoesNotExist:
            return None

    #3. Retrieve
    def get(self, request, lot_id, *args, **kwargs):
        '''
        Retrieves the parking lot with given id
        '''
        lot_instance = self.get_object(lot_id)
        if not lot_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ParkingSerializer(lot_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


         # 4. Update
    def put(self, request, lot_id, *args, **kwargs):
        lot_instance = self.get_object(lot_id)
        if not lot_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'status': request.data.get('status'),
        }
        serializer = ParkingSerializer(instance = lot_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, lot_id, *args, **kwargs):
        lot_instance = self.get_object(lot_id)
        if not lot_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        lot_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )



class ParkingApiView(APIView):
    #1. get list of lots
    def get(self, request, *args, **kwargs):
        '''
        List all the parking lots
        '''
        lots = Parking.objects
        serializer = ParkingSerializer(lots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'status': request.data.get('status'),
        }
        serializer = ParkingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


