from django.contrib import admin
from .models import Student, CourseReview, Course, myUserModel, ModuleCourse, IntroductionInfo


admin.site.register(CourseReview)
admin.site.register(Course)
admin.site.register(IntroductionInfo)
admin.site.register(ModuleCourse)
admin.site.register(Student)
admin.site.register(myUserModel)