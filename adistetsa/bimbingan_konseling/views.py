from django.shortcuts import render

# # Create your views here.
# def booked_event_page_view(request):
#    # getting queryset
#     currentUser = request.user
#     bookedEvents = models.BookedEvent.objects.filter(user=currentUser)
#     # adding event filter
#     filter = JurusanFilter(request.GET, queryset=bookedEvents)
#     bookedEvents = filter.qs
#     context = {'bookedEvents': bookedEvents, 'filter':filter}
#     return render(request, 'booked_events.html', context)