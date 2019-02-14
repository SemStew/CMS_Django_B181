from semstew.models import *


def show_menu(request):
    selected_lang = request.session.get('lang', 1)
    langs = Language.objects.all()
    branches = Branch.objects.all()
    menus = MenuName.objects.all()

    return {'selected_lang': selected_lang,
            'langs': langs,
            'branches': branches,
            'menus': menus}
