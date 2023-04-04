from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from .forms import CreateNewArticle, SearchForm
from .models import Article, Question, Answer,Upvote
import datetime

#Rendering the homepage
def index(request):
    user = request.user #gets the information of the user
    if not user.is_authenticated: #checks whether if user is logged in
        return redirect('login/') #Redirects to login page
    articles = Article.objects.filter(author=user)
    if request.GET.get("DeleteBtn"): #If delete button is pressed, the article with the associated author is deleted
        articles.filter(id = request.GET.get("DeleteBtn")).delete()
    if request.GET.get("Search"): #Navigates to the search results page if search bar contains a searched article
        search = request.GET.get('search')
        documents = articles.objects.filter(name__contains=search)
        return render(request, 'searchresults.html', {'documents': documents})
    searchForm = SearchForm()
    form = CreateNewArticle()
    return render(request, 'home.html', {'form': form, 'articles': articles, 'user': user, 'searchForm': searchForm})

#Rendering the edit page when edit button is pressed
def edit(request, id):
    article = Article.objects.get(id=id) #get the article id and querys the database for that id
    inital_input = {
        'title': article.title,
        'text': article.body
    }
    form = CreateNewArticle(initial=inital_input) #setting the form field with the data correlated to the article id
    if request.method == 'POST': #if form submitted
        form = CreateNewArticle(request.POST)  #getting the data of the submitted form
        if form.is_valid: #updating the database with the submitted information
            title = form.data['title']
            text = form.data['text']
            current_date = datetime.date.today()
            current_time = datetime.datetime.now().time()
            article.title = title
            article.body = text
            article.date = current_date
            article.time = current_time
            article.save()
            return redirect('/') #Redirects to homepage
    return render(request, 'edit.html', {'form': form, 'article': article})

#Rendering the create document page
def create(request):
    user = request.user
    if request.method == 'POST': #if form submitted
        form = CreateNewArticle(request.POST)
        current_date = datetime.date.today() #gets the current date
        current_time = datetime.datetime.now().time() #gets the current time
        if form.is_valid(): #creating a new row in the database with the submitted information
            title = form.cleaned_data['title']
            txt = form.cleaned_data['text']
            art = Article(author = user, title=title, body=txt, date=current_date, time=current_time) 
            art.save() #saving the information to the database
            return redirect('/') #Redirects to homepage
    form = CreateNewArticle()
    return render(request, 'create.html', {'form': form})

#Rendering the page after the user querys the database for their document
class search(ListView):
    model = Article
    template_name = 'searchresults.html'
    def get_queryset(self): 
        user = self.request.user #getting the current user
        query = self.request.GET.get('q') #getting the submitted document information by the variable name in forms
        userList = Article.objects.filter(author=user) #filters all of the documents created by the user
        object_list = userList.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        ) #filters the database to check whether if part of the title or the body of article matches with the searched information
        return object_list

#Renders the dashboard page where all questions with the correlated answers are displated
def dashboard(request):
    all_question=Question.objects.all()
    all_answer=Answer.objects.all()
    return render(request,"dashboard.html",{"all_question":all_question,"all_answer":all_answer})

#Renders the page where all questions created are listed
def questions(request):
    if request.method == "POST": #if question form is submitted, a new question is created
        question = request.POST["question"]
        question_instance = Question.objects.create(
            question=question,
            author=request.user
            )
        return redirect("/questions/") #Redirects to questions page

    all_question=Question.objects.all().order_by('-timestamp')
    return render(request,"question.html",{"all_question":all_question})

#Renders the page unique to the question, will also contain the answers correlated to the question
def discussion(request,question_id):
    question=Question.objects.get(pk=question_id)
    if request.method == "POST": #if answer form is submitted, a new answer is posted
        answer=request.POST["answer"]
        answer_instance=Answer.objects.create(
            answer=answer,
            question=question,
            author=request.user,
            upvotes=1
            )
        return redirect(f"/discussion/{question_id}/") #Redirects to discussions page
    all_answer=Answer.objects.filter(question=question_id)
    return render(request,"discussion.html",{"question":question,"answer":all_answer})

#Allows the upvoting of a submitted answer
def upvote(request,answer_id):
    answer=Answer.objects.get(pk=answer_id)
    upvotes=Upvote.objects.filter(reader=request.user,answer=answer)
    if len(upvotes) == 0:
        answer.upvotes += 1
        answer.save()
        upvote = Upvote(reader=request.user, answer=answer)
        upvote.save()

    return redirect(f"/discussion/{answer.question.id}") #Redirects to discussions page

#Deletes the related question if delete button is pressed
def delete_ques(request, question_id):
    question = Question.objects.get(pk=question_id)
    print(question_id)
    question.delete()

    return redirect("/questions/") #Redirects to questions page

#Deletes the related answer if delete button is pressed
def delete_ans(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    print(answer_id)
    answer.delete()

    return redirect("/questions/") #Redirects to questions page