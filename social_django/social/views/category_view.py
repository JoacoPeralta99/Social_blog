from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from ..forms import CategoryForm
from ..models import Category


class CategoryListView(LoginRequiredMixin, View):
    template_name = 'blog/category/list.html'

    def get(self, request):
        categories = Category.objects.all()
        return render(request, self.template_name, {'categories': categories})


class CreateCategoryView(LoginRequiredMixin, View):
    template_name = 'blog/category/create_category.html'

    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['name']
            if Category.objects.filter(name=category_name).exists():
                form.add_error('name','Ya existe una categoria con este nombre.')
            else:
                form.save()
                return redirect('blog:category_list')
        return render(request, self.template_name, {'form': form})


class UpdateCategoryView(LoginRequiredMixin, View):
    template_name = 'blog/category/update_category.html'

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryForm(instance=category)
        return render(request, self.template_name, {'form': form, 'category': category})

    def post(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('blog:category_list')
        return render(request, self.template_name, {'form': form, 'category': category})


class DeleteCategoryView(LoginRequiredMixin, View):
    template_name = 'blog/category/delete_category.html'

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        return render(request, self.template_name, {'category': category})

    def post(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('blog:category_list')


class CategoryDetailView(LoginRequiredMixin, View):
    template_name = 'blog/category/detail.html'

    def get(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        return render(request, self.template_name, {'category': category})
