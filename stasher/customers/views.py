from rest_framework import views, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from stasher.customers.models import Customer


class CustomerListAPIView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        customers = Customer.objects.all()
        return Response([c.as_dict() for c in customers])

    def post(self, request, format=None):
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password = request.data['password']
        gender = request.data.get('gender')

        if gender not in {'M', 'F', 'O'}:
            raise ValidationError({"gender": "Expected M, F or O"})

        country_code = request.data.get('country_code')

        if country_code not in {'GBR', 'USA'}:
            raise ValidationError({"country_code": "Unsupported country"})

        customer = Customer(
            email=email,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            country_code=country_code,
        )

        customer.set_password(password)
        customer.save()

        return Response(customer.as_dict())


class CustomerDetailAPIView(views.APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, id_, format=None):
        customer = Customer.objects.get(id=id_)
        return Response(customer.as_dict())

    def patch(self, request, id_, format=None):
        customer = Customer.objects.get(id=id_)

        if 'first_name' in request.data:
            customer.first_name = request.data['first_name']

        if 'last_name' in request.data:
            customer.last_name = request.data['last_name']

        if 'password' in request.data:
            customer.password = request.data['password']

        if 'gender' in request.data:
            customer.gender = request.data['gender']

        if 'country_code' in request.data:
            customer.country_code = request.data['country_code']

        if 'email' in request.data:
            customer.email = request.data['email']

        customer.save()
        return Response(customer.as_dict())
