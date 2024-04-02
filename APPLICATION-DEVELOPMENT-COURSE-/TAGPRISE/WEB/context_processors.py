



def authenticated_user(request):
    return {'authenticated_user': request.user}