from django.shortcuts import render
from django.http import JsonResponse

def products(request):
    products_list = [
        {"name": "Product A", "price": 100},
        {"name": "Product B", "price": 200}
        ]
    return JsonResponse(products_list, safe=False)


# The issue here is that there is no exception handling
# def get_employee_name(employee_id):
#     employees = {"1": "John", "2": "Alice"}
#     try:
#         return employees[employee_id]
#     except KeyError as e:
#         return (e, 404)