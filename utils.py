from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.text import slugify
import functools
from polyglot.forms import *
from Anecdotes.forms import *
from Billing.forms import *



def do_nothing(classs, kwargs):
    return kwargs


def next_n_url(p_numbers, current_page_number, n, search_query):
    pn = current_page_number + n
    return f'?page={pn}&query={search_query}' if 1 <= pn <= p_numbers else ''


class Objects:
    template_name = None
    model = None
    base_app_template = None
    form_model = None
    object_redirect_url = None
    request_proc = do_nothing


class ObjectsListMixin(Objects):
    objects_per_page = 1
    query_fields = []
    function_name = None
    template_name = 'obj_list.html'

    def get(self, request):
        show_query = len(self.query_fields)
        search_query = slugify(request.GET.get('query', ''), allow_unicode=True)
        if search_query and self.function_name:
            z = [Q((f'{qq}__icontains', search_query)) for qq in self.query_fields]
            q = functools.reduce(lambda a, b: a | b, z)
            objects = self.model.objects.filter(q)
        else:
            objects = self.model.objects.all()

        page_number = request.GET.get('page', 1)
        paginator = Paginator(objects, self.objects_per_page)
        page_object = paginator.get_page(page_number)
        is_paginated = page_object.has_other_pages()
        p_numbers = paginator.num_pages
        page_number = int(page_number)

        context = {
            'show_query': show_query,
            'function_name': self.function_name,
            'search_query': search_query,
            'page_object': page_object,
            'is_paginated': is_paginated,
            'prev_url': next_n_url(p_numbers, page_number, -1, search_query),
            'next_url': next_n_url(p_numbers, page_number, 1, search_query),
            'prev10_url': next_n_url(p_numbers, page_number, -10, search_query),
            'next10_url': next_n_url(p_numbers, page_number, 10, search_query),
            'prev100_url': next_n_url(p_numbers, page_number, -100, search_query),
            'next100_url': next_n_url(p_numbers, page_number, 100, search_query),
            'number_pages_to_view_b': -NUMBER_PAGES_TO_VIEW,
            'number_pages_to_view_f': NUMBER_PAGES_TO_VIEW,
            'counter': objects.count
            }

        return render(request, self.template_name, context=context)


class ObjectDetailsMixin(Objects):
    template_name = 'obj_detailes.html'

    def get(self, request, id):
        # print(f"\nID = {id}\n")
        obj = get_object_or_404(self.model, id=id)
        context = {
            f'{self.model.__name__.lower()}': obj,
            'admin_object': obj,
            'details': True
            }
        # print(context)
        return render(request, self.template_name, context=context)


class ObjectCreateMixin(Objects):
    object_create_url = None
    template_name = 'obj_create.html'

    def get(self, request):
        form = self.form_model()
        print(self.object_create_url,  self.base_app_template, self.model.__name__.lower())
        context = {
            'form': form,
            'object_create_url': self.object_create_url,
            'base_app_template': self.base_app_template,
            'class_name': self.model.__name__.lower(),
        }
        return render(request, self.template_name, context=context)

    def post(self, request):
        # print(request.POST)
        new_dict = self.request_proc(request.POST)
        bound_form = self.form_model(new_dict)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            # print(new_obj)
            return redirect(reverse(self.object_redirect_url))
        # print(bound_form.errors)
        context = {
            'form': bound_form,
            'base_app_template': self.base_app_template,
            'object_create_url': self.object_create_url
        }

        return render(request, self.template_name, context=context)


class ObjectUpdateMixin(Objects):
    template_name = 'obj_update.html'

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        form = self.form_model(instance=obj)
        context = {
            'form': form,
            self.model.__name__.lower(): obj,
            'base_app_template': self.base_app_template,
            'object': obj
        }
        return render(request, self.template_name, context=context)

    def post(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        new_dict = self.request_proc(request.POST)
        bound_form = self.form_model(new_dict, instance=obj)
        if bound_form.is_valid():
            upd_obj = bound_form.save()
            return redirect(upd_obj)
        context = {
            'form': bound_form
            }
        return render(request, self.template_name, context=context)


class ObjectDeleteMixin(Objects):
    template_name = 'obj_delete.html'

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        context = {
            'object': obj,
            'class_name': self.model.__name__.lower(),
            'object_name': obj.__str__,
            'base_app_template': self.base_app_template,
            'object_redirect_url': self.object_redirect_url

        }
        return render(request, self.template_name, context=context)

    def post(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        obj.delete()
        return redirect(reverse(self.object_redirect_url))
