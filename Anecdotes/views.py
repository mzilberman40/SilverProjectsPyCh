from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import *
from .funcs import *
from .models import *


class Anecdotes:
    base_app_template = 'anecdotes/base_anecdotes.html'
    objects_per_page = WORDS_PER_PAGE
    raise_exception = True
    user_form_model = UserForm


class UsersList(ObjectsListMixin, View):
    template_name = 'anecdotes/users.html'
    model = User
    objects_per_page = TAGS_PER_PAGE
    query_fields = ['user']
    function_name = 'users_list_url'

# class UserCreate(LoginRequiredMixin, View):
#     form_model = UserForm


class Anecdote(Anecdotes):
    model = Anecdote
    form_model = AnecdoteForm
    objects_per_page = ANECDOTES_PER_PAGE
    query_fields = ['body', 'id']
    object_redirect_url = 'anecdotes_list_url'
    function_name = object_redirect_url


class AnecdotesList(Anecdote, ObjectsListMixin, View):
    template_name = 'anecdotes/index.html'


class AnecdoteDetails(Anecdote, View):
    template_name = 'anecdotes/anecdote_detail.html'

    def get(self, request, id):
        object = get_object_or_404(self.model, id=id)
        user_object = get_user(request.user)
        context = {
            f'{self.model.__name__.lower()}': object,
            'admin_object': object,
            'details': True,
            'user': user_object,
            'rate': object.get_rate(user_object)
            }
        return render(request, self.template_name, context=context)

    def post(self, request, id):
        anecdote_object = self.model.objects.get(id=id)
        user_object = get_user(request.user)
        rate = request.POST.get('rate', 0)
        rate_object, status = \
            Rates.objects.get_or_create(user=user_object, anecdote=anecdote_object, defaults={'rate': rate})
        if not status:
            rate_object.rate = rate
            rate_object.save()

        context = {
            f'{self.model.__name__.lower()}': anecdote_object,
            'admin_object': object,
            'details': True,
            'rate': rate_object.rate
            }

        return render(request, self.template_name, context=context)


class AnecdoteCreate(Anecdote, LoginRequiredMixin, ObjectCreateMixin, View):
    template_name = 'anecdotes/anecdote_create.html'


class AnecdoteUpdate(Anecdote, LoginRequiredMixin, ObjectUpdateMixin, View):
    template_name = 'anecdotes/anecdote_update.html'


class AnecdoteDelete(Anecdote, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass


class AnecdotesCheckDups(Anecdote, LoginRequiredMixin, View):
    template_name = 'anecdotes/anecdote_dups.html'

    def compare(self, source1, source2):
        same = 0
        for i in range(len(source1)):
            if source1[i] in source2:
                same = same + 1
        return same * 2 / float(len(source1) + len(source2)) * 100

    def compare_text(self, anecdot1, anecdot2):
        k = 2  # Will assume if lengthes of  texts after canonization differ more then k times then
        # texts are different
        x1 = anecdot1.canonize()
        x2 = anecdot2.canonize()
        if len(x1) > k * len(x2) or len(x2) > k * len(x1):
            return False
        shinglelen = min(4, len(x1), len(x2))
        return self.compare(anecdot1.gen_shingle(shinglelen), anecdot2.gen_shingle(shinglelen)) > 0

    def get_dubs(self):
        all = self.model.objects.all()
        dublicates = [{i, k} for i in all for k in all if i.id > k.id and self.compare_text(i, k)]
        print(dublicates)
        return dublicates

    def get(self, request):
        dups = self.get_dubs()
        context = {
            'dups': dups
            }
        return render(request, self.template_name, context=context)


class Tags(Anecdotes):
    model = Tag
    form_model = TagForm
    objects_per_page = TAGS_PER_PAGE
    query_fields = ['title']
    object_redirect_url = 'tags_list_url'
    function_name = object_redirect_url


class TagsList(Tags, ObjectsListMixin, View):
    template_name = 'anecdotes/tags.html'


class TagDetails(Tags, View):
    template_name = 'anecdotes/tag_detail.html'

    def get(self, request, id):
        object = get_object_or_404(self.model, id=id)
        context = {
            f'{self.model.__name__.lower()}': object,
            'admin_object': object,
            'details': True,
            'counter': object.anecdotes.count
            }
        return render(request, self.template_name, context=context)


class TagCreate(Tags, LoginRequiredMixin, ObjectCreateMixin, View):
    template_name = 'anecdotes/tag_create.html'


class TagUpdate(Tags, LoginRequiredMixin, ObjectUpdateMixin, View):
    template_name = 'anecdotes/tag_update.html'


class TagDelete(Tags, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass
