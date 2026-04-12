from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserFile
from .forms import UserFileForm

@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = UserFileForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            user_file = form.save(commit=False)
            user_file.user = request.user
            user_file.save()
            messages.success(request, f"Successfully uploaded {user_file.name}")
            return redirect('home')
        else:
            messages.error(request, "Error uploading file. Please check the form.")
    else:
        form = UserFileForm(user=request.user)

    files = UserFile.objects.filter(user=request.user).order_by('-uploaded_at')

    context = {
        'form': form,
        'files': files
    }
    return render(request, "dashboard/main.html", context)