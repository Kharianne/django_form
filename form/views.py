from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseGone
from .forms import ContactForm
from .utils import replace_key_to_label


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            data = replace_key_to_label(ContactForm.Meta.labels,
                                        form.cleaned_data)
            request.session['form_data'] = data
            return HttpResponseRedirect('/summary/')
    else:
        form = ContactForm()

    return render(request, 'form/index.html', {'form': form})


def summary(request):
    if request.session.get('form_data'):
        return render(request, 'form/summary.html',
                      {
                          'form_data': request.session['form_data'],
                       })
    else:
        return HttpResponseGone("Ooops")