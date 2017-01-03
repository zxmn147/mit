from django.shortcuts import render, redirect, get_object_or_404


from project.models import Project
from project.forms import ProjectForm
# Create your views here.
def project(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project/project.html',context)


def projectCreate(request):
     '''
     Create a new article instance
     1. If method is GET, render an empty form
     2. If method is POST, perform form validation. Display error messages if the form is invalid
     3. Save the form to the model and redirect to the article page
     '''
     template = 'project/projectCreate.html'
     if request.method == 'GET':
         return render(request, template, {'projectForm':ProjectForm()})
     #post
     projectForm = ProjectForm(request.POST)
     if not projectForm.is_valid():
         return render(request, template, {'projectForm':projectForm})
     projectForm.save()
     return redirect('project:project')
 

def projectRead(request, projectId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with article instance and its
        associated comments
    '''
    projectToRead = get_object_or_404(Project, id=projectId)
    context = {'project':projectToRead}
  
    return render(request, 'project/projectRead.html', context) 

     
