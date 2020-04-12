from django.shortcuts import render

# Create your views here.





def home(request):

    '''
    View home function that returns the home page
    '''
  
    voice_card = VoiceCard.objects.all()
    print(voice_card)

    apartments = Listing.objects.filter(category__contains="apartments").all()
    print(apartments)

    mansionattes = Listing.objects.filter(category__contains="mansionattes").all()
    print(mansionattes)

    bungalows = Listing.objects.filter(category__contains="bungalows").all()
    print(bungalows)
    

    
    return render(request, 'home.html', {"listings":listings, "apartments": apartments,"mansionattes":mansionattes,"bungalows":bungalows})
