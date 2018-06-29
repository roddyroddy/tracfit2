from django.shortcuts import render, redirect

from apps.leaderboard.models import *


def index(request):
    request.session.flush()

    a = User.objects.all()
    b = Wod.objects.last()
    currentwod = b.id
    c = Score.objects.filter(wod_id = currentwod).order_by("timed_score")
    d = Score.objects.filter(wod_id = currentwod).order_by("-amrap_score")
    
    
    
    rank = 1
    rank_amrap = 1
    for score in c:
        user = score.user
        user.rank = rank
        rank += 1
        user.save()

    for score in d:
        user = score.user
        user.rank_amrap = rank_amrap
        rank_amrap += 1
        user.save()


    numbers = []

    for i in range(1, len(c)+1):
        numbers.append(i)


    context = {
        "user": a,
        "wod": b,
        "score": c,
        "amrap": d,
        "numbers": numbers
    }
    print(context)
    return render(request, 'leaderboard/index.html', context)

def student(request):
    a = User.objects.filter(name = request.POST['name'])
    if len(a) == 0:
        User.objects.create(name = request.POST['name'])
        b = User.objects.get(name = request.POST['name'])
        request.session['user_id'] = b.id
        

    else:
        a = User.objects.get(name = request.POST['name'])
        request.session['user_id'] = a.id
    return render(request, 'leaderboard/student.html')

def adminloginpage(request):
    return render(request, 'leaderboard/login.html')

def adminlogin(request):
    entry = True
    b = User.objects.filter(name = request.POST['login_name'])
    b = b[0]
    if b.name != request.POST['login_name']:
        entry = False
    if b.admin != 9:
        entry = False
    if entry == True:
        request.session['user_id'] = b.id
        return redirect('/admin')
    else:
        return redirect('/')
def admin(request):
    
    return render(request, 'leaderboard/admin.html')

def createwod(request):
    title = request.POST['title']
    description = request.POST['description']
    styles = request.POST['style']

    Wod.objects.create(
        title = title,
        description = description,
        style = styles,
        user_id = request.session['user_id']
    )
    return redirect('/')

def addscore(request):
    minutes = int(request.POST['minutes'])
    minutes *= 60
    sec = int(request.POST['seconds'])



    wod = Wod.objects.last()
    print(wod.id)
    fortime = minutes + sec
    user = request.session['user_id']
    wod_key = wod.id
    amrap = request.POST['amrap_score']

    time = fortime

    minutes = 0
    seconds = 0

    while time >= 60:
        time -= 60
        minutes += 1
        seconds = time
    print("*********", minutes, ":", seconds)
    z = str(minutes)+":"+str(seconds)
    # print(timearr)

    Score.objects.create(
        amrap_score = amrap,
        timed_score = fortime,
        # string = 
        user_id = user,
        wod_id = wod_key,
        string = z
    )
    return redirect('/')