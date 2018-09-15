import logging

from django.contrib import messages
from django.shortcuts import render, redirect

from parcours_imi.models import UserParcours


logger = logging.getLogger(__name__)


def user_parcours_unlock_courses_view(request, object_id):
    try:
        user_parcours = UserParcours.objects.get(pk=object_id)
    except UserParcours.DoesNotExist:
        raise Exception

    try:
        course_choice = user_parcours.course_choice
    except UserParcours.course_choice.RelatedObjectDoesNotExist:
        messages.warning(request, 'L\'étudiant n\'a pas encore choisi ses cours.')
        return redirect('admin:index')

    course_choice.submitted = False
    course_choice.save()

    messages.success(request, 'Cours dévérouillés avec succès.')
    return redirect('admin:index')