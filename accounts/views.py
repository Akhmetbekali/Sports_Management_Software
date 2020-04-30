from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import RegistrationForm, ProfileEditForm, PasswordChangeForm, ClubForm, ClubEditForm
from django.contrib.auth import update_session_auth_hash

from accounts.models import ClubProfile


def home(request):
    args = {'current_user': request.user
            }
    return render(request, 'home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
        else:
            args = {'form': form,
                    'current_user': request.user
                    }
            return render(request, 'profiles/registration_form.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form,
                'current_user': request.user
                }
        return render(request, 'profiles/registration_form.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            return redirect('/account/profile/' + str(request.user.id))
        else:
            return redirect('/account/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form,
                'current_user': request.user
                }
        return render(request, 'profiles/change_password.html', args)


@login_required
def profile(request, id):
    user = get_object_or_404(User, id=id)
    args = {'user': user,
            'current_user': request.user
            }
    return render(request, 'profiles/profile.html', args)


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile/' + str(request.user.id))
    else:
        form = ProfileEditForm(instance=request.user)
        args = {'form': form,
                'current_user': request.user
                }
        return render(request, 'profiles/edit_profile.html', args)


def all_profiles(request):
    profiles = User.objects.all()

    args = {'profiles': profiles,
            'current_user': request.user
            }
    return render(request, 'profiles/all_profiles.html', args)


def create_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            data = request.POST.copy()
            leaders_group = Group.objects.get(name='club_leader')
            user = User.objects.get(id = data.get('leader'))
            change_group(user, leaders_group)
            return redirect('../clubs')
        else:
            args = {'form': form,
                    'current_user': request.user}
            return render(request, 'clubs/create_club.html', args)
    else:
        form = ClubForm()
        args = {'form': form,
                'current_user': request.user
                }
        return render(request, 'clubs/create_club.html', args)


def club_page(request, id):
    club = get_object_or_404(ClubProfile, id=id)
    args = {'club': club,
            'current_user': request.user
            }
    return render(request, 'clubs/club_page.html', args)


def edit_club(request, id):
    club = get_object_or_404(ClubProfile, id=id)
    old_leader = club.leader
    students_group = Group.objects.get(name='student')
    leaders_group = Group.objects.get(name='club_leader')
    if request.method == 'POST':
        form = ClubEditForm(request.POST, instance=club)
        if form.is_valid():
            if str(old_leader.groups.all().get()) != 'manager':
                change_group(old_leader, students_group)
                form.save()
                new_leader = club.leader
                if str(new_leader.groups.all().get()) != 'manager':
                    change_group(new_leader, leaders_group)
            else:
                form.save()
                new_leader = club.leader
                if str(new_leader.groups.all().get()) != 'manager':
                    change_group(new_leader, leaders_group)
            return redirect('/account/club_page/' + id)
    else:
        form = ClubEditForm(instance=club)
        args = {'form': form,
                'current_user': request.user
                }
        return render(request, 'clubs/edit_club.html', args)


def all_clubs(request):
    clubs = ClubProfile.objects.all()
    args = {'clubs': clubs,
            'current_user': request.user}
    return render(request, 'clubs/all_clubs.html', args)


def delete_club(request, id):
    club = get_object_or_404(ClubProfile, id=id)
    club.delete()
    return redirect('all_clubs')


def participate(request, id=None):
    project = get_object_or_404(ClubProfile, id=id)
    project.participants.add(request.user.id)
    project.save()
    return redirect('/account/club_page/' + id)


def change_group(user, group):
    user.groups.clear()
    user.groups.add(group)
    return

