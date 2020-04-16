from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from utils import *
from .config import *
from tools import *
from .hebrew_symbols import *


class Polyglot:
    base_app_template = 'polyglot/base_polyglot.html'
    objects_per_page = WORDS_PER_PAGE
    raise_exception = True


class Binyan(Polyglot):
    model = Binyan
    form_model = BinyanForm
    object_redirect_url = 'binyans_list_url'
    function_name = object_redirect_url


class BinyanList(Binyan, ObjectsListMixin, View):
    template_name = 'polyglot/binyans.html'


class BinyanCreate(Binyan, LoginRequiredMixin, ObjectCreateMixin, View):
    object_create_url = 'binyan_create_url'


class BinyanDetails(Binyan, ObjectDetailsMixin, View):
    template_name = 'polyglot/binyan_details.html'


class BinyanUpdate(Binyan, LoginRequiredMixin, ObjectUpdateMixin, View):
    template_name = 'polyglot/binyan_update.html'


class BinyanDelete(Binyan, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass


class POS(Polyglot):
    model = PartOfSpeech
    form_model = POSForm
    object_redirect_url = 'pos_list_url'
    function_name = object_redirect_url
    query_fields = ['rusname', 'engname']


class POSList(POS, ObjectsListMixin, View):
    template_name = 'polyglot/poss.html'


class POSCreate(POS, LoginRequiredMixin, ObjectCreateMixin, View):
    # template_name = 'polyglot/pos_create.html'
    object_create_url = 'pos_create_url'



class POSDetails(POS, ObjectDetailsMixin, View):
    template_name = 'polyglot/pos_details.html'


class POSUpdate(POS, LoginRequiredMixin, ObjectUpdateMixin, View):
    template_name = 'polyglot/pos_update.html'


class POSDelete(POS, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass


class RusWords(Polyglot):
    model = RusWord
    form_model = RusWordForm
    object_redirect_url = 'ruswords_list_url'
    function_name = object_redirect_url
    query_fields = ['word']


class RusWordsList(RusWords, ObjectsListMixin, View):
    template_name = 'polyglot/ruswords.html'


class RusWordCreate(RusWords, LoginRequiredMixin, ObjectCreateMixin, View):
    object_create_url = 'rusword_create_url'


class RusWordDetails(RusWords, ObjectDetailsMixin, View):
    template_name = 'polyglot/rusword_details.html'


class RusWordUpdate(RusWords, LoginRequiredMixin, ObjectUpdateMixin, View):
    pass


class RusWordDelete(RusWords, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass


class HebrewRoot(Polyglot):
    model = HebrewRoot
    form_model = HebrewRootForm
    object_redirect_url = 'hebrewroots_list_url'
    function_name = object_redirect_url
    query_fields = ['root']

    def request_proc(self, post):
        new_post = post.copy()
        def_pos = PartOfSpeech.objects.get(engname=DEFAULT_POS)
        defaults = {'pos': def_pos}
        words = post['ruswords'].split(',')
        clean_words = [clean_phrase(w) for w in words]
        objects = [RusWord.objects.get_or_create(word=w, defaults=defaults)[0] for w in clean_words]
        new_post['ruswords'] = objects
        return new_post


class HebrewRootsList(HebrewRoot, ObjectsListMixin, View):
    template_name = 'polyglot/hebrewroots.html'


class HebrewRootDetails(HebrewRoot, ObjectDetailsMixin, View):
    template_name = 'polyglot/hebrewroot_details.html'


class HebrewRootUpdate(HebrewRoot, LoginRequiredMixin, ObjectUpdateMixin, View):
    template_name = 'polyglot/hebrewroot_update.html'

    def get(self, request, id):
        obj = get_object_or_404(self.model, id=id)
        form = self.form_model(instance=obj)
        form.initial['ruswords'] = ', '.join([a['word'] for a in obj.ruswords.values()])
        context = {
            'form': form,
            self.model.__name__.lower(): obj
        }
        return render(request, self.template_name, context=context)


class HebrewRootDelete(HebrewRoot, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass


class HebrewRootCreate(HebrewRoot, LoginRequiredMixin, ObjectCreateMixin, View):
    object_create_url = 'hebrewroot_create_url'


class Theme(Polyglot):
    model = Theme
    form_model = ThemeForm
    object_redirect_url = 'themes_list_url'
    function_name = object_redirect_url
    objects_per_page = 100
    query_fields = ['rusname', 'engname']


class ThemeList(Theme, ObjectsListMixin, View):
    template_name = 'polyglot/themes.html'


class ThemeCreate(Theme, LoginRequiredMixin, ObjectCreateMixin, View):
    object_create_url = 'theme_create_url'


class ThemeDetails(Theme, ObjectDetailsMixin, View):
    template_name = 'polyglot/theme_details.html'


class ThemeUpdate(Theme, LoginRequiredMixin, ObjectUpdateMixin, View):
    # template_name = 'polyglot/theme_update.html'
    raise_exception = True


class ThemeDelete(Theme, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass


class Preposition(Polyglot):
    model = Preposition
    form_model = PrepositionForm
    object_redirect_url = 'prep_list_url'
    function_name = object_redirect_url
    objects_per_page = 100
    query_fields = ['ruswords', 'hword']


class PrepositionList(Preposition, ObjectsListMixin, View):
    template_name = 'polyglot/prepositions.html'


class PrepositionCreate(Preposition, LoginRequiredMixin, ObjectCreateMixin, View):
    object_create_url = 'prep_create_url'


class PrepositionDetailes(Preposition, ObjectDetailsMixin, View):
    template_name = 'polyglot/preposition_details.html'


class PrepositionUpdate(Preposition, LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True


class PrepositionDelete(Preposition, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass


class HebrewSymbols(View):
    template_name = 'polyglot/hebrewsymbols.html'
    letters = [Letter(r) for r in ALPHABET.items()]

    def get(self, request):
        context = {
            'letters': self.letters,
        }
        return render(request, self.template_name, context=context)

class HebrewSymbol(View):
    template_name = 'polyglot/hebrewsymbol.html'
    letters = [Letter(r) for r in ALPHABET.items()]

    def get(self, request):
        context = {
            'letters': self.letters,
        }
        return render(request, self.template_name, context=context)


class Pronoun(Polyglot):
    model = Pronoun
    form_model = PronounForm
    object_redirect_url = 'pron_list_url'
    function_name = object_redirect_url
    objects_per_page = 100
    query_fields = ['ruswords', 'hword']


class PronounList(Pronoun, ObjectsListMixin, View):
    template_name = 'polyglot/pronouns.html'


class PronounCreate(Pronoun, LoginRequiredMixin, ObjectCreateMixin, View):
    object_create_url = 'pron_create_url'


class PronounDetailes(Pronoun, ObjectDetailsMixin, View):
    template_name = 'polyglot/pronoun_details.html'


class PronounUpdate(Pronoun, LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True


class PronounDelete(Pronoun, LoginRequiredMixin, ObjectDeleteMixin, View):
    pass