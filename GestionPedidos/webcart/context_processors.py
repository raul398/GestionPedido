def Count_Total(request):
    total = 0 #Contador de articulos
    #ver si el usuario esta autenticado
    if request.user.is_authenticated:
        for key, value in request.session['webcart'].items():
            total = total+(float(value['precio'])*value['cantidad'])
    return {'Count_Total': total}