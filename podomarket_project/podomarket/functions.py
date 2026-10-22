from django.shortcuts import redirect
from allauth.account.models import EmailAddress, EmailConfirmation

def confirmation_required_redirect(request):
    # 현재 유저의 이메일 주소 객체를 가져오거나 생성
    email_address, created = EmailAddress.objects.get_or_create(
        user=request.user,
        email=request.user.email,
    )
    
    # 인증 메일 생성 및 발송
    confirmation = EmailConfirmation.create(email_address)
    confirmation.send(request)
    
    return redirect("account_email_confirmation_required")