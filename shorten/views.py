from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from shorten.forms import shorten_form
from shorten.models import bitly
import string
import random


def generate_shortcode():

	generated_shortcode = ""
	for i in range(6):
		random_value = random.choice(string.ascii_lowercase +
									string.ascii_uppercase +
									string.digits)
		generated_shortcode+=random_value

	final_short_code = check(generated_shortcode)
	print(final_short_code)
	return final_short_code


def check(generated_shortcode):

	queryset = bitly.objects.filter(model_short_code__exact=generated_shortcode).exists()
	print(queryset)

	if queryset==True:
		generate_shortcode()
	else:
		return generated_shortcode


def create_shortcode(request):
	form = shorten_form(request.POST or None)

	if form.is_valid():
		instance = form.save(commit=False)
		long_url_from_form = form.cleaned_data["long_url"]
		print(long_url_from_form)

		queryset = bitly.objects.filter(long_url__exact=long_url_from_form).exists()
		print(queryset)

		if queryset==True:
			print("this url is already shortened")
		else:
			new_shortcode = generate_shortcode()
			print(new_shortcode)

			instance.model_short_code = new_shortcode
			instance.save()

			return HttpResponseRedirect('/'+str(instance.id))

	context = {
			"form": form,
	}
	return render(request, "home.html", context)


def new_url(request, id=None):
	instance = get_object_or_404(bitly, id=id)

	context = {
		"queryset": instance,
	}

	return render(request, "new.html", context)


def details_view(request, shortcode=None):
	instance = get_object_or_404(bitly, model_short_code=shortcode)
	instance.count += 1
	instance.save()

	return HttpResponseRedirect(instance.long_url)
