from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
 


#views 
from system.views.AdminCourseListView import AdminCourseListView
from system.views.TrainerCourseListView import TrainerCourseListView
from system.views.AdminCreateCourseView import AdminCreateCourseView
from system.views.TrainerInProgressCourseListView import TrainerInProgressCourseListView
from system.views.TrainerInProgressCourseDetailsView import TrainerInProgressCourseDetailsView
from system.views.ReorderCourseView import ReorderCourseView
from system.views.AddSkillToCourse import AddSkillToCourse
from system.views.AddAdditionalResourcesToCourse import AddAdditionalResourcesToCourse


urlpatterns = [
    path(
        'admin/company/<int:company_id>/courses', 
        AdminCourseListView.as_view(), 
        name='company-course-admin-list'
    ),
    path(
        'trainer/company/<int:company_id>/courses', 
        TrainerCourseListView.as_view(), 
        name='company-course-trainer-list'
    ),
    path(
        'trainer/company/<int:company_id>/courses', 
        TrainerCourseListView.as_view(), 
        name='company-course-trainer-list'
    ),
      path(
        'trainer/company/<int:company_id>/course/<course_id>/reorder', 
        ReorderCourseView.as_view(), 
        name='company-course-trainer-list'
    ),
    # path(
    #     'trainee/company/<int:company_id>/courses', 
    #     CompanyCourseList.as_view(), 
    #     name='company-course-trainee-list'
    # ),
    # path(
    #     'owner/company/<int:company_id>/courses', 
    #     AdminCourseListView.as_view(), 
    #     name='company-course-owner-list'
    # ),
    # path(
    #     'admin/company/<int:company_id>/pending_courses', 
    #     CompanyCourseListPending.as_view(), 
    #     name='company-pending-course-admin-list'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/pending_courses', 
    #     CompanyCourseListPending.as_view(), 
    #     name='company-pending-course-trainer-list'
    # ),
    path(
        'trainer/company/<int:company_id>/progress_courses', 
        TrainerInProgressCourseListView.as_view(),  
    ),
      path(
        'trainer/company/<int:company_id>/progress_courses/<int:course_id>', 
        TrainerInProgressCourseDetailsView.as_view(),  
    ),
    path(
        'admin/company/<int:company_id>/courses/create', 
        AdminCreateCourseView.as_view(),  
    ),
    path(
        'course/<id>/skills', 
        AddSkillToCourse.as_view(),  
    ),
      path(
        'course/<id>/additional-resources', 
        AddAdditionalResourcesToCourse.as_view(),  
    ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/publish', 
    #     CompanyCoursePublish.as_view(), 
    #     name='company-course-trainer-publish'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/approve', 
    #     CompanyCourseApprove.as_view(), 
    #     name='company-course-admin-approve'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/disapprove', 
    #     CompanyCourseDisapprove.as_view(), 
    #     name='company-course-admin-disapprove'
    # ),
    # path(
    #     'admin/company/<int:company_id>/pending_courses/<int:course_id>', 
    #     CompanyCourseRetrievePending.as_view(), 
    #     name='company-pending-course-admin-retrive'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/pending_courses/<int:course_id>', 
    #     CompanyCourseRetrievePending.as_view(), 
    #     name='company-pending-course-admin-retrive'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/progress_courses/<int:course_id>', 
    #     CompanyCourseRetrieveInProgress.as_view(), 
    #     name='company-progress-course-trainer-retrive'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>', 
    #     CompanyCourseRetrieve.as_view(), 
    #     name='company-course-admin-retrive'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>', 
    #     CompanyCourseRetrieve.as_view(), 
    #     name='company-course-trainer-retrive'
    # ),
    # path(
    #     'trainee/company/<int:company_id>/courses/<int:course_id>', 
    #     CompanyCourseRetrieve.as_view(), 
    #     name='company-course-trainee-retrive'
    # ),
    # path(
    #     'owner/company/<int:company_id>/courses/<int:course_id>', 
    #     CompanyCourseRetrieve.as_view(), 
    #     name='company-course-owner-retrive'
    # ),
    # path(
    #     'owner/company/<int:company_id>/courses/<int:course_id>/set_trainer_leader',
    #     CompanyCourseSetTrainerLeader.as_view(),
    #     name='company-course-owner-set-leader'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/set_trainer_leader',
    #     CompanyCourseSetTrainerLeader.as_view(),
    #     name='company-course-admin-set-leader'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/part_not_part_users', 
    #     CompanyCourseRetrievePartandNotPartUsers.as_view(), 
    #     name='company-course-admin-retrive-part-not-part-users'
    # ),
    # path(
    #     'owner/company/<int:company_id>/courses/<int:course_id>/part_not_part_users', 
    #     CompanyCourseRetrievePartandNotPartUsers.as_view(), 
    #     name='company-course-owner-retrive-part-not-part-users'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/update', 
    #     CompanyCourseUpdate.as_view(), 
    #     name='company-course-admin-update'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/update', 
    #     CompanyCourseUpdate.as_view(), 
    #     name='company-course-trainer-update'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/delete',
    #     CompanyCourseDelete.as_view(),
    #     name='company-course-admin-delete'
    # ),
    # path(
    #     'admin/company/<int:company_id>/courses/<int:course_id>/info',
    #     CompanyCourseRetriveInfo.as_view(),
    #     name='company-course-admin-info'
    # ),
    # path(
    #     'trainer/company/<int:company_id>/courses/<int:course_id>/info',
    #     CompanyCourseRetriveInfo.as_view(),
    #     name='company-course-trainer-info'
    # ),  
    # path(
    #     'trainee/company/<int:company_id>/courses/<int:course_id>/info',
    #     CompanyCourseRetriveInfo.as_view(),
    #     name='company-course-trainee-info'
    # ),
]
# adding the urls for the static files (course image)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)