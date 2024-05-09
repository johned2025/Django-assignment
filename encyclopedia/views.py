from django.shortcuts import render

from . import util
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entryPage(request,title):
    return render(request, "encyclopedia/entryPage.html", {
        "entryName": title,
        "entry": markdown2.markdown(util.get_entry(title))
    })

