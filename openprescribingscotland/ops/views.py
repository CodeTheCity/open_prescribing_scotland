from django.http import HttpResponse
from django.shortcuts import render, redirect
import json
from .forms import InputForm, EntryForm
import pandas as pd
import time
import requests
import json


def index(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            resource_id = {
                "January 2022": "53a53d61-3b3b-4a12-888b-a788ce13db9c",
                "February 2022": "bd7aa5c9-d708-4d0b-9b28-a9d822c84e34",
                "March 2022": "a0ec3bf2-7339-413b-9c66-2891cfd7919f",
                "April 2022": "7de8c908-86f8-45ac-b6a4-e21d1df30584",
                "May 2022": "1b4e3200-b6e6-415f-b19a-b9ef927db1ab",
                "June 2022": "debeadd8-2bbb-4dd3-82de-831531bab2cb",
                "July 2022": "26ce66f1-e7f2-4c71-9995-5dc65f76ecfb",
                "August 2022": "49fa5784-be06-4015-bc6d-9b5db8726473",
                "September 2022": "9d0a518d-9d9c-4bcb-afd8-51f6abb7edf1",
                "October 2022": "bd7bc2cf-4de5-4711-bd5a-9e3b77305453",
                "November 2022": "023986c0-3bb2-43cb-84e8-2e0b3bb1f55f",
                "December 2022": "00213ffa-941e-4389-9e6f-3bca8067da8c"
            }
            all_res = []
            for value in resource_id.values():
                url = 'https://www.opendata.nhs.scot/api/3/action/datastore_search?resource_id=' + value
                r = requests.get(url)
                content = json.loads(r.text)
                df = pd.DataFrame(pd.json_normalize(pd.DataFrame([content]).result[0])['records'][0])
                all_res.append(df)
            df_res = pd.concat(all_res)

            drug_name = request.POST.get("drug_name")
            df_res = df_res.loc[df_res['BNFItemDescription'] == drug_name]
            print(df_res['PaidQuantity'].sum())
            return HttpResponse(f"The aggregate result will be: {df_res['PaidQuantity'].sum()}!")
    else:
        context = {}
        context["form"] = EntryForm()
        return render(request, "ops/index.html", context)


def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            resource_id = "652ff726-e676-4a20-abda-435b98dd7bdc"  # Eventually, we will have to get this from a mapping
            r = requests.get(f"https://www.opendata.nhs.scot/api/3/action/datastore_search?resource_id={resource_id}")
            data = json.loads(r.text)["result"]
            health_boards = pd.DataFrame(data["records"])
            health_boards = health_boards.set_index("HB")

            area_code = request.POST.get("area_code")
            area_name = health_boards.loc[area_code]["HBName"]

            # TODO: fancy data handling

            return HttpResponse(f"The area code ist {area_name}!")
    else:
        context = {}
        context["form"] = InputForm()
        return render(request, "ops/ops.html", context)

    # return HttpResponse("Hello world, this is Isi!")
    # return render(request, "ops/home.html") # Eventually use HTML template