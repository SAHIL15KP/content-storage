from django import forms
from django.db.models import Sum
from .models import UserFile

class UserFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file', 'name']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'block w-full text-sm ... hover:file:bg-blue-100',
                'accept': 'image/*,video/*'
            }),
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm',
                'placeholder': 'Optional explicit name for your file'
            })
        }

    def __init__(self, *args, **kwargs):
        # We grab the user object from the view
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file:
            return file

        if self.user and self.user.is_authenticated:
            # FREE TIER LIMIT: 80 MB (Hardlocked for all users)
            limit_mb = 80

            # Calculate how much space they have used so far
            usage_dict = UserFile.objects.filter(user=self.user).aggregate(total=Sum('size'))
            current_usage_bytes = usage_dict['total'] or 0

            limit_bytes = limit_mb * 1024 * 1024
            new_total = current_usage_bytes + file.size

            if new_total > limit_bytes:
                friendly_limit = f"{limit_mb / 1024:.0f} GB" if limit_mb >= 1024 else f"{limit_mb} MB"
                raise forms.ValidationError(f"File upload exceeds your storage limit of {friendly_limit}. Please upgrade your subscription!")
            
        return file
