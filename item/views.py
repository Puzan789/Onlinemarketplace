from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewitemForm

# Create your views here.


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=pk
    )[0:3]
    return render(
        request, "item/detail.html", {"item": item, "related_items": related_items}
    )


@login_required
def newitem(request):
    if request.method == "POST":
        form = NewitemForm(request.POST, request.FILES)  # files that users upload
        if form.is_valid():
            item = form.save(commit=False)
              # commit=false will create and object but doesnot save in a database
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = NewitemForm()

    return render(request, "item/newitemform.html", {"form": form, "title": "New Item"})
