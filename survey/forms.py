from django import forms

from .models import Survey, Question, Option


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ["title"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["prompt"]


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ["text"]


class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop("options")
        # Options must be a list of Option objects
        choices = {(o.pk, o.text) for o in options}
        choices2 = {(i + 1, i + 1) for i in range(10)}
        super().__init__(*args, **kwargs)
        option_field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, required=True)
        power_field = forms.ChoiceField(choices=choices2, widget=forms.RadioSelect)
        self.fields["option"] = option_field
        self.fields["power"] = power_field


class PowerOfChoiceForm(forms.Form):
    def __init__(self, *args):
        choices = {i + 1 for i in range(10)}
        super().__init__(*args)
        option_field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, required=True)
        self.fields["option"] = option_field


class BaseAnswerFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs["options"] = kwargs["options"][index]
        return kwargs
