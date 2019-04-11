# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

# Create your views here.
from .forms import BeverageForm
from .models import BeverageHistory, Beverage

import requests, json
import os
# Create your views here.
def beverage(request):

    if request.method == 'POST':
        form = BeverageForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_by = request.user
            do_api_call(instance.beverage.key, instance.bean_amount, 60)
            instance.save()
            return HttpResponseRedirect(reverse('beverage'))
    else:
        form = BeverageForm()

    context = {
        "form": form,
    }
    return render(request, "beverage.html", context)


def do_api_call(beverage, beanamount, fillquantity ):

    haID = os.environ['HAID']

    # defining the api-endpoint  
    API_ENDPOINT = os.environ['API_ENDPOINT'] + haID + "/programs/active"
    
    # your API key here 
    bearer = "Bearer " + os.environ['BEARER_TOKEN']
    
    headers = {'authorization': bearer,
               'Content-Type': 'application/vnd.bsh.sdk.v1+json',
               'accept': 'application/vnd.bsh.sdk.v1+json',
               'Accept-Language': 'de-DE'}
    
    beverage_key = "ConsumerProducts.CoffeeMaker.Program.Beverage." + beverage
    beanamount_key = "ConsumerProducts.CoffeeMaker.EnumType.BeanAmount." + beanamount
    # data to be sent to api 
    data = {"data": 
            {"key": beverage_key,
            "options": [
              {"key": "ConsumerProducts.CoffeeMaker.Option.BeanAmount",
               "value": beanamount_key
              },
              {"key": "ConsumerProducts.CoffeeMaker.Option.FillQuantity",
               "value": fillquantity,
               "unit": "ml"
              }
            ]
            }
           }

    # sending post request and saving response as response object 
    r = requests.put(url = API_ENDPOINT, json = data, headers = headers) 
    
    # extracting response text  
    print("Return code: %s"%r.status_code)
    if (r.status_code != 204):
      print("Data:")
      print(json.dumps(data, indent=4, sort_keys=True))
      print("Return message:")
      print(json.dumps(r.json(), indent=4, sort_keys=True))
      return True
    else:
      return False