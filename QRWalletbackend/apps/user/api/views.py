from rest_framework import generics
from apps.user.models import User
from rest_framework_simplejwt import views as jwt_views
from apps.user.api.serializers import UserSerializer, CreateUserSerializer, UserDetailsSerializer, UpdateUserSubscriberSerializer
from rest_framework_api_key.permissions import HasAPIKey
from django_rest_passwordreset.views import ResetPasswordRequestToken
from django_rest_passwordreset.models import ResetPasswordToken, clear_expired, get_password_reset_token_expiry_time, \
    get_password_reset_lookup_field
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from apps.utils.send_email import send_email_to_recovery_password
from django.utils.translation import gettext_lazy as _




HTTP_USER_AGENT_HEADER = getattr(
    settings, 'DJANGO_REST_PASSWORDRESET_HTTP_USER_AGENT_HEADER', 'HTTP_USER_AGENT')
HTTP_IP_ADDRESS_HEADER = getattr(
    settings, 'DJANGO_REST_PASSWORDRESET_IP_ADDRESS_HEADER', 'REMOTE_ADDR')

def _unicode_ci_compare(s1, s2):
    normalized1 = unicodedata.normalize('NFKC', s1)
    normalized2 = unicodedata.normalize('NFKC', s2)

    return normalized1.casefold() == normalized2.casefold()


class TokenObtainPairAPIView(jwt_views.TokenObtainPairView):
    permission_classes = [HasAPIKey]

class TokenRefreshAPIView(jwt_views.TokenRefreshView):
    permission_classes = [HasAPIKey]

class UserDetailsAPIView(generics.ListAPIView):

    permission_classes = [HasAPIKey, IsAuthenticated]
    serializer_class = UserDetailsSerializer

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.id)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    


class CreateTokenAPIView(ResetPasswordRequestToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password_reset_token_validation_time = get_password_reset_token_expiry_time()
        now_minus_expiry_time = datetime.now(
        ) - timedelta(hours=password_reset_token_validation_time)
        clear_expired(now_minus_expiry_time)
        users = User.objects.filter(
            **{'{}__iexact'.format(get_password_reset_lookup_field()): email})
        active_user_found = False
        for user in users:
            if user.eligible_for_reset():
                active_user_found = True
                break
        if not active_user_found and not getattr(settings, 'DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE', False):
            raise exceptions.ValidationError({
                'email': [_(
                    "We couldn't find an account associated with that email. Please try a different e-mail address.")],
            })
        for user in users:
            if user.eligible_for_reset() and \
                    _unicode_ci_compare(email, getattr(user, get_password_reset_lookup_field())):
                token = None
                if user.password_reset_tokens.all().count() > 0:
                    token = user.password_reset_tokens.all()[0]
                else:
                    token = ResetPasswordToken.objects.create(
                        user=user,
                        user_agent=request.META.get(
                            HTTP_USER_AGENT_HEADER, ''),
                        ip_address=request.META.get(
                            HTTP_IP_ADDRESS_HEADER, ''),
                    )
                try:
                    send_email_to_recovery_password(user=user, token=token.key)
                except:
                    pass
        return Response({'status': 'OK', "token": str(token.key)})


class UpdateSubscribeAPIView(generics.UpdateAPIView):

    serializer_class = UpdateUserSubscriberSerializer
    permission_classes = [HasAPIKey, IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)