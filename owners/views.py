import email
import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(name=data['name'],
                             email=data['email'],
                             age=data['age'])
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        dogs = Dog.objects.all()
        result = []

        for owner in owners:
            for dog in dogs:
                if owner.name == dog.owner.name:
                    result.append(
                        {
                            "owner name" : owner.name,
                            "email" : owner.email,
                            "age" : owner.age,
                            "dog name" : dog.name,
                            "dog age" : dog.age
                        }
                    )
        # for owner in owners:
        #     dogs = owner.dog_set.all()
        #     dog_list = []

        #     for dog in dogs:
        #         dog_info = (
        #             {   
        #                 'age': dog.age,
        #                 'name': dog.name
        #             }
        #         )
        #         dog_list.append(dog_info)

        #     result.append(
        #         {
        #             'age': owner.age,
        #             'email': owner.email,
        #             'my_dog': dog_list,
        #             'name': owner.name
        #         }
        #     )
            
        return JsonResponse({'results' : result}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        Dog.objects.create(name=data['name'],
                           age = data['age'],
                           owner=Owner.objects.get(name=data['owner'])
                           )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        result = []

        for dog in dogs:
            result.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name
                }
            )
        return JsonResponse({'results' : result}, status=200)