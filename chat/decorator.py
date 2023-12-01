from functools import wraps
from django.shortcuts import redirect
from .models import  Chat # Import the User Profile model
from food_system.models import Delivery
from accounts.models import UserProfile

#To access the chat just if you're member of it 

def is_chat_member(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(username=user)

            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return redirect('accounts/login')
            
            chat_id = kwargs.get('id_chat')
            if chat_id:
                try:
                    chat = Chat.objects.get(id_chat=chat_id)
                    delivery = Delivery.objects.get(id_delivery=chat.fk_id_delivery.id_delivery)
                    cliente = delivery.fk_id_client
                    repartidor = delivery.fk_id_delivery_man

                    if user == cliente or user == repartidor:
                        return view_func(request, *args, **kwargs)
                    else:
                        return redirect('/')  # Redirect to a different page if the user is not associated with the delivery

                except Chat.DoesNotExist:
                    return redirect('/')
            
        except Exception as e:
            print(str(e))
            return redirect('/') 
    
    return _wrapped_view
