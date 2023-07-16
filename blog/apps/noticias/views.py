from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria, Comment
from django.views.generic.list import ListView #para las vistas clases
from .forms import NoticiaForm, CommentForm

def ListarNoticias(request):
    contexto = {} #diccionario
    
    id_categoria = request.GET.get("id", None)

    if id_categoria:
        n = Noticia.objects.filter(categoria_noticia = id_categoria)
    else:
        n = Noticia.objects.all() #SELECT * FROM Noticias / lista objetos

    contexto['noticias'] = n

    cat = Categoria.objects.all().order_by('nombre') #ordena por nombre
    contexto['categorias'] = cat
    
    return render(request,'noticias/listar.html', contexto)


class mostrarNoticia(ListView):
    model = Noticia
    template_name = "noticias/listarNoticia.html"


'''def DetalleNoticias(request, pk): #vista obsoleta
    contexto = {} #diccionario
        
    n = Noticia.objects.get(pk = pk) #select * from noticias where pk --> 1 objeto
        
    contexto['noticia'] = n
        
    return render(request,'noticias/detalle.html', contexto)'''
    
def DetalleNoticias(request, pk): #nueva vista
    noticia = get_object_or_404(Noticia, pk=pk)
    comments = noticia.comments.all()

    #BORRAR NOTICIA
    if request.method == 'POST' and 'delete_noticia' in request.POST: #metodo para borrar noticias
        noticia.delete()
        return redirect('noticias:listar')

    # COMENTARIO
    if request.method == 'POST' and 'add_comment' in request.POST: 
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) #que se guarde el form solo cuando tenga todos lso campos cargados
            comment.noticia = noticia
            comment.author = request.user
            comment.save()
            return redirect('noticias:detalle', pk=pk) #una vez que termina redirecciona donde estabamos
    else:
        form = CommentForm()

    context = {
        'noticia': noticia,
        'comments': comments,
        'form': form,
    }

@login_required
def AddNoticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES) ##REQUEST FILE PARA LAS IMAGENES
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.author = request.user #autor de la noticia
            noticia.save()
            return redirect('home')
    else:
        form = NoticiaForm()
    
    return render(request, 'noticias/addNoticia.html', {'form': form})


'''def AddComentario(request,pk):
    noticia = get_object_or_404(Noticia, pk)
    form = CommentForm(request, pk = pk)
    if form.isvalid():
        comment = form.save()'''
#Borrar comentario
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user.username:
        comment.delete()
    return redirect('noticias:detalle', pk=comment.noticia.pk)

#Agregar comentario
@login_required
def add_comment(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        author = request.user.username
        # creacion de comentario
        Comment.objects.create(noticia=noticia, author=author, text=text)
    return redirect('noticias:detalle', pk=noticia_id)
    