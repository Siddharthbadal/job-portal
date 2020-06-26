from django.contrib import admin
from .models import Candidate, CandidateJobMap
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CandidateResource(resources.ModelResource):
    class Meta:
        model = Candidate


class CandidateAdmin(ImportExportModelAdmin):
    list_display = ('name', 'gender', 'mobile', 'city',
                    'cand_will_relocate', 'is_engaged')
    list_filter = ('gender', 'city', 'will_relocate')
    resource_class = CandidateResource


class ReviewCandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'age', 'gender', 'city', 'status')
    list_filter = ('job',)
    list_editable = ('status',)
    list_display_links = None


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(CandidateJobMap, ReviewCandidateAdmin)
