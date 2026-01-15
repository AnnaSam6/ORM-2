from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        
        # Считаем количество основных разделов
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1
        
        if main_count == 0:
            raise ValidationError('Укажите основной раздел')
        if main_count > 1:
            raise ValidationError('Основным может быть только один раздел')
        
        return self.cleaned_data


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_at']
    list_filter = ['published_at']
    search_fields = ['title']
    inlines = [ScopeInline]
