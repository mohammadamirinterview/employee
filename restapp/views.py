from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
import logging

logger = logging.getLogger(__name__)


class EmployeeList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        emp_obj = Employee.objects.all()
        emp_list = EmployeeSerializer(emp_obj, many=True)
        logger.info('get employees list calling')
        return Response(emp_list.data)


class EmployeeListById(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Employee.objects.get(employee_id=pk)
        except Employee.DoesNotExist:
            return None

    def get(self, request, pk):
        emp_obj = self.get_object(pk)
        if emp_obj is None:
            logger.error('employee with id ' + str(pk) + ' not found')
            return Response({'error': 'Give object not found'}, status=status.HTTP_404_NOT_FOUND)

        emp_list = EmployeeSerializer(emp_obj)
        logger.info("get employee with employee id " + str(pk))
        return Response(emp_list.data)


def redirect_view(request):
    response = redirect('/docs/')
    return response
