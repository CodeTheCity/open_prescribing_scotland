from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field


AREA_CODES = (
    ("S08000015", "S08000015"),
    ("S08000016", "S08000016"),
    ("S08000017", "S08000017"),
)


class InputForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    area_code = forms.MultipleChoiceField(
        label="Area Code",
        choices=AREA_CODES,
    )


DRUG_NAME = (('MEZZOPRAM', 'MEZZOPRAM'), ('LACTULOSE', 'LACTULOSE'), ('GLYCEROL', 'GLYCEROL'), ('URSOFALK',
                                                                                                'URSOFALK'), ('XYLOPROCT', 'XYLOPROCT'), ('SENNA', 'SENNA'), ('NEXIUM', 'NEXIUM'), ('ALVERIN', 'ALVERIN'), ('DULCOLA', 'DULCOLA'), ('LOSE', 'LOSE'), ('LAXIDO', 'LAXIDO'), ('DOCUSAT', 'DOCUSAT'), ('SALOFALK', 'SALOFALK'), ('PICOLAX', 'PICOLAX'), ('CYTOTEC', 'CYTOTEC'), ('GAVISCO', 'GAVISCO'), ('LANSOPRAZOLE', 'LANSOPRAZOLE'), ('ANUSO', 'ANUSO'), ('RABEPRAZOL', 'RABEPRAZOL'), ('ISPA', 'ISPA'), ('MEZAVAN', 'MEZAVAN'), ('CO-MAGALDROX', 'CO-MAGALDROX'), ('FYBOGE', 'FYBOGE'), ('HYOSCIN', 'HYOSCIN'), ('MEBEVERIN', 'MEBEVERIN'), ('BUSCOPAN', 'BUSCOPAN'), ('MICRALAX', 'MICRALAX'), ('OMEPRAZOL', 'OMEPRAZOL'), ('FYBOGEL', 'FYBOGEL'), ('FAMOTIDINE', 'FAMOTIDINE'), ('PEPTAC', 'PEPTAC'), ('MOVENTIG', 'MOVENTIG'), ('Q', 'Q'), ('ESOMEPRAZOLE', 'ESOMEPRAZOLE'), ('ACIDEX', 'ACIDEX'), ('OMEPRAZOLE', 'OMEPRAZOLE'), ('OCTASA', 'OCTASA'), ('URSODEOXYCHOLI', 'URSODEOXYCHOLI'), ('ANTACID/OXETACAINE', 'ANTACID/OXETACAINE'), ('CONSTELLA', 'CONSTELLA'), ('BISACODYL', 'BISACODYL'), ('IMODIU', 'IMODIU'), ('PANTOPRAZOLE', 'PANTOPRAZOLE'), ('LOPERAMID', 'LOPERAMID'), ('PROCTOSEDYL', 'PROCTOSEDYL'), ('PREPARATIO', 'PREPARATIO'), ('MESALAZINE', 'MESALAZINE'), ('PENTAS', 'PENTAS'), ('ZOTON', 'ZOTON'), ('PENTASA', 'PENTASA'), ('SO', 'SO'), ('UNIROI', 'UNIROI'), ('PEPPERMIN', 'PEPPERMIN'), ('SCHERIPROCT', 'SCHERIPROCT'), ('COLPERMIN', 'COLPERMIN'), ('SULFASALAZINE', 'SULFASALAZINE'))

class EntryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

    drugs = forms.MultipleChoiceField(
        label="Drugs",
        choices=DRUG_NAME,
    )
