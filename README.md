# Open Prescribing Scotland

The aim of this project is to create an easy-to-use web interface to prescribing data in Scotland.

The relevant datasets are:

* [Prescribing Data](https://www.opendata.nhs.scot/dataset/prescriptions-in-the-community):
  - HBT 
  - GPPractice
  - BNFItemCode
  - BNFItemDescription
  - PaidDate
  - ClassOfPreparationCode
  - NumberOfPaidItems
  - PaidQuantity
  - GrossIngredientCost
  - PaidDate

* [Glossary of Terms](https://www.isdscotland.org/health-topics/prescribing-and-medicines/_docs/Open_Data_Glossary_of_Terms.pdf?1)

* [Health Boards](https://www.opendata.nhs.scot/dataset/geography-codes-and-labels/resource/652ff726-e676-4a20-abda-435b98dd7bdc) with their corresponding name and the country code for Scotland
* [GP Practices](https://www.opendata.nhs.scot/dataset/gp-practice-contact-details-and-list-sizes) Contact Details and List Sizes

## Project Setup

This webpage requires Python3 and uses the webframework Django.

Download python from https://www.python.org/downloads/.

As a suggestion, to install python from the terminal use:
```shell
sudo apt-get update
sudo apt-get install python3.8
```

Python dependencies are managed via pip. It is however advised to install those dependencies into an virtual 
environment. This can be created with:
```shell
python3 -m venv venv
```

To activate the environment use:
```shell
source venv/bin/activate
```
This needs to be done in every shell that should use our newly created environment.

We suggest installing the Python dependencies from the openprescribingscotland folder through the `requirements.txt` file:
```shell
pip install -r requirements.txt
```

Once the repository is cloned, the Django Webserver can be started with:
```shell
python manage.py runserver
```

## Deployment
The web application is deployed on Render!
<br>
Please click this link to access: https://open-prescribing-scotland.onrender.com/
