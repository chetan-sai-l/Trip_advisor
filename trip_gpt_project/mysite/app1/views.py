from django.shortcuts import render,redirect
from django.http import JsonResponse 
import openai 
from .forms import TravelPreferenceForm
from .models import TravelPreference
# from .forms import InterestsAndActivitiesForm
# from .models import InterestsAndActivities

openai.api_key = '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'

def get_completion(prompt): 
	#print(prompt) 
	query = openai.completions.create( 
		model="gpt-3.5-turbo-instruct",
		#model="text-davinci-003", will not work as it got depriciated from 1st jan 2024
		prompt=prompt, 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5,
	) 

	response = query.choices[0].text
	#print(response) 
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		response = get_completion(prompt) 
		return JsonResponse({'response': response}) 
	return render(request, 'index.html') 

def travel_preference_view(request):
    if request.method == 'POST':
        form = TravelPreferenceForm(request.POST)
        if form.is_valid():
            group_type = form.cleaned_data['group_type']
            transportation = form.cleaned_data['transportation']
            accommodation = form.cleaned_data['accommodation']
            outdoor_adventures=form.cleaned_data['outdoor_adventures']
            cultural_experiences=form.cleaned_data['cultural_experiences']
            specific_cuisine=form.cleaned_data['specific_cuisine']
            num_days = form.cleaned_data['num_days']
            
            # Save the answers to the database or perform any other action
            a = f" suggest me a place based on details given I am travelling with {group_type}, like to use {transportation} , prefer the {accommodation} accommodation, like to do {outdoor_adventures} , like to visit {cultural_experiences} , prefer {specific_cuisine} food and give me a day by day plan for {num_days} days make it a good looking plan"
            obj_exists = TravelPreference.objects.filter(question = a).exists()
            if obj_exists :
                #print("obj exists")
                obj = TravelPreference.objects.get(question = a)
                print(obj.plan)
                return render(request,'travel_suggestion_1.html',{'response':obj.plan})
            response = get_completion(a)
            #print(a)
            travel_preference = TravelPreference(
                group_type=group_type,
                transportation=transportation,
                accommodation=accommodation,
                outdoor_adventures = outdoor_adventures,
                cultural_experiences = cultural_experiences,
                specific_cuisine = specific_cuisine,
                num_days = num_days,
                plan = response,
                question = a,
            )
            travel_preference.save()
            return render(request,'travel_suggestion_1.html',{'response':response})
            # return render(request,'travel_suggestion.html',{'group_type':group_type, 'transportation':transportation, 'accommodation':accommodation, 'outdoor_adventures':outdoor_adventures,'cultural_experiences':cultural_experiences,'specific_cuisine':specific_cuisine})
    else:
        form = TravelPreferenceForm()
    return render(request, 'travel_preference.html', {'form': form})
# def interests_and_activities_view(request):
#     if request.method == 'POST':
#         form = InterestsAndActivitiesForm(request.POST)
#         if form.is_valid():
#             outdoor_adventures=form.cleaned_data['outdoor_adventures']
#             cultural_experiences=form.cleaned_data['cultural_experiences']
#             specific_cuisine=form.cleaned_data['specific_cuisine']

#             Interests_Activities = InterestsAndActivities(
#                 outdoor_adventures = outdoor_adventures,
#                 cultural_experiences = cultural_experiences,
#                 specific_cuisine = specific_cuisine

#             )
#             Interests_Activities.save()
#             return redirect('http://127.0.0.1:8000/')  # Redirect to home page or any other URL
#     else:
#         form = InterestsAndActivitiesForm()
#     return render(request, 'travel_preference.html', {'form': form})