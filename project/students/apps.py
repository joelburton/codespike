from django.apps import AppConfig
from watson import search as watson


class StudentSearchAdapter(watson.SearchAdapter):
    def get_title(self, obj):
        return obj.title

    def get_description(self, obj):
        return obj.description


class StudentsConfig(AppConfig):
    name = 'students'

    # define models to be searched by django-watson
    def ready(self):
        Enrollment = self.get_model("enrollment")
        watson.register(Enrollment.public.all(),
                        StudentSearchAdapter,
                        fields=[
                            'student__username',
                            'student__bio',
                            'student__nickname',
                            'student__formal_name',
                            'student__pronoun',
                            'student__location',
                            'student__github_username',
                            'student__twitter_username',
                        ],
                        store=['cohort_id', "search_type"])
