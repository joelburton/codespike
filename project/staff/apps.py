from watson import search as watson
from django.apps import AppConfig


class StaffSearchAdapter(watson.SearchAdapter):
    def get_title(self, obj):
        return f"{obj.title}, {obj.job_title}"

    def get_description(self, obj):
        return obj.description


class StaffConfig(AppConfig):
    name = 'staff'

    # define models to be searched by django-watson
    def ready(self):
        Staffing = self.get_model("staffing")
        watson.register(Staffing.public.all(),
                        StaffSearchAdapter,
                        fields=[
                            'staffmember__username',
                            'staffmember__bio',
                            'staffmember__nickname',
                            'staffmember__formal_name',
                            'staffmember__pronoun',
                            'staffmember__location',
                            'staffmember__github_username',
                            'staffmember__twitter_username',
                        ],
                        store=['cohort_id', "search_type"])
