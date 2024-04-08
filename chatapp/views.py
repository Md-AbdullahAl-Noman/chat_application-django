from django.shortcuts import render, redirect
from chatapp.models import Room, Message
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get("username")
    
    # retrieve the Room object
    room_details = Room.objects.filter(name=room).first()
    
    if room_details is not None:
        return render(request, 'room.html', {
            'username': username,
            'room_details': room_details,
            'room': room
        })
    else:
        # if the Room object does not exist
        return HttpResponse("Room does not exist.")

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')
        room_id = request.POST.get('room_id')

        # Retrieve the Room instance corresponding to room_id
        try:
            room_instance = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return HttpResponse('Room does not exist')

        # Create a new Message instance with the Room instance
        new_message = Message.objects.create(message=message, user=username, room=room_instance)
        new_message.save()
        return HttpResponse('Message sent successfully')
    else:
        return HttpResponse('Invalid request method')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})