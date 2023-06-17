from django import forms
from django.forms import ModelMultipleChoiceField, ModelChoiceField

# AREA_CODES = (
#     ("S08000015", "NHS Ayrshire and Arran"),
#     ("S08000016", "NHS Borders"),
#     ("S08000017", "NHS Dumfries and Galloway"),
# )

AREA_CODES = (
    ("S08000015", "S08000015"),
    ("S08000016", "S08000016"),
    ("S08000017", "S08000017"),
)


class InputForm(forms.Form):
    area_code = forms.MultipleChoiceField(
        label="Area Code",
        choices=AREA_CODES,
    )


DRUG_NAME = (
    ("SENNA_TAB 7.5MG", "SENNA_TAB 7.5MG"),
    ("ANUSOL_CRM", "ANUSOL_CRM"),
    ("QV INTENSIVE OINT", "QV INTENSIVE OINT"),
)


class EntryForm(forms.Form):
    area_code = forms.MultipleChoiceField(
        label="Drugs",
        choices=DRUG_NAME,
    )