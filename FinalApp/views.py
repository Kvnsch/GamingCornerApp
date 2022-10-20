from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from FinalApp.forms import RegistrationForm,GameForm, UpcomingGameForm
from FinalApp.models import Game, upcomingGame
from FinalApp.forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# Create your views here.

#HTML Views

def main(request):
    return render(request, "FinalApp/main.html")

def about(request):
    return render(request,"FinalApp/About.html")

def searchHTML(request):
    return render(request,"FinalApp/Games/Search.html")
    
def register(request):
    return render(request,"User/Register.html")

def list_games(request):
    upcoming_Game = upcomingGame.objects.all()
    old_Game = Game.objects.all()
    return render(request, "FinalApp/Games/allGames.html",{'results_release':upcoming_Game,
    'results_oldGame':old_Game})

def newGame(request):
    return render(request,"FinalApp/Games/NewGame.html")

#### #### #### ####

# Register
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()

            return render(request,"FinalApp/main.html",{'message':"Usuario registrado con éxito"})
    else:
        form = RegistrationForm()
    return render(request,"FinalApp/User/Register.html",{'form':form})
 
# Login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")
            userID = authenticate(username=user, password=passwd)

            if userID: 
                login(request,userID)
                return render(request,"FinalApp/main.html", {'message':f"Bienvenido {userID}"})
    else:
        form = AuthenticationForm()
    return render(request, "FinalApp/User/Login.html",{'form':form})

#Edit User
@login_required
def user_edit(request):
    user = request.user
    if request.method == 'POST':
        myForm=RegistrationForm(request.POST)
        if myForm.is_valid():
            infoForm=myForm.cleaned_data
            user.username = infoForm['username']            
            user.email = infoForm['email']
            user.password1 = infoForm['password1']
            user.password2 = infoForm['password2']
            user.save()
            return render(request, "FinalApp/main.html")
    else:
        myForm=RegistrationForm(initial={'username':user.username,'email':user.email})
    return render(request,"FinalApp/User/userEdit.html",{'myForm':myForm,'user':user.username})

#Add Game
@login_required
def addnewGame(request):
    if request.method == 'POST':
        myForm= GameForm(request.POST)
        if myForm.is_valid():
            infoForm=myForm.cleaned_data
            game = Game (gameDeveloper=request.user,gameName=infoForm['gameName'],
            gameGenre=infoForm['gameGenre'],gameRelease=infoForm['gameRelease'],
            gameScore=infoForm['gameScore'],gameReview=infoForm['gameReview'])
            game.save()
            return render(request,'FinalApp/mother.html')
    else:
        myForm=GameForm()
    return render (request,'FinalApp/Games/NewGame.html',{'form':myForm})

#Add UpcomingGame
@login_required
def add_upcomingGame(request):
    if request.method == 'POST':
        myForm= UpcomingGameForm(request.POST, request.FILES)
        if myForm.is_valid():
            infoForm= myForm.cleaned_data

            gameRelease=upcomingGame (upcomingName=infoForm['upcomingName'],
            upcomingRelease=infoForm['upcomingRelease'],upcomingsWallpaper=infoForm['upcomingsWallpaper'],)
            gameRelease.save()
            return render(request,'FinalApp/Games/allGames.html')
    else:
        myForm=UpcomingGameForm()
    return render(request,'FinalApp/Games/addRelease.html',{'myForm':myForm})

#Edit UpcomingGame
@login_required
def edit_upcomingGame(request,releaseGame_name):

    relGame = upcomingGame.objects.get(upcomingName = releaseGame_name)
    
    if request.method == 'POST':
        myForm = UpcomingGameForm(request.POST,request.FILES)

        if myForm.is_valid():
            infoForm= myForm.cleaned_data

            relGame.upcomingName = infoForm['upcomingName']
            relGame.upcomingRelease = infoForm['upcomingRelease']
            relGame.upcomingsWallpaper = infoForm['upcomingsWallpaper']
            
            relGame.save()
            return render(request,"FinalApp/main.html")
    else:
        myForm = UpcomingGameForm(initial=
        {
        'upcomingName':relGame.upcomingName,
        'upcomingRelease':relGame.upcomingRelease,
        'upcomingsWallpaper':relGame.upcomingsWallpaper,
        })

    return render(request,"FinalApp/Games/editGame.html",{'myForm':myForm,'results':releaseGame_name})

#Delete UpcomingGame
@login_required
def delete_upcomingGame(request,releaseGame_name):
    releaseGame = upcomingGame.objects.get(upcomingName = releaseGame_name)
    releaseGame.delete()
    upcoming_Game = upcomingGame.objects.all()
    
    return render(request,"FinalApp/Games/editGame.html",{'results':upcoming_Game})

#Search
def searchResult(request):
    if request.GET['gameName']:
        name=request.GET['gameName']
        results=Game.objects.filter(gameName__icontains=name)
        return render(request,"FinalApp/Games/searchResult.html",{"search":name,"results":results})
    else:
        errorMessage="No information was searched"
        return HttpResponse(errorMessage)


