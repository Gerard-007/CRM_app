from django.shortcuts import render


# Create your views here.
# class Location(View):
#     def get(self, request):
#         return render()

def location(request):
    mapbox_access_token = 'pk.eyJ1IjoiZ2VldGVjaCIsImEiOiJjazNieTMwZGgwN2p6M21vMnBsMG1ldDd4In0.M162n_OVG3VT8hlN9Uw93g'
    return render(request, 'includes/location.html', {"mapbox_access_token": mapbox_access_token})