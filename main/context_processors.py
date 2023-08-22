from users.models import Member

def list_member_profile(request):
    return {'member_profile': Member.objects.filter(account=request.user)}