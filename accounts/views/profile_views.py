import logging
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.helpers.profile_helpers import ProfileHelper
from accounts.models.profile import Profile
from accounts.serializers.profile_serializers import CreateProfileSerializer, ProfileSerializer
from accounts.serializers.user_serializers import UserSerializer
from common.responses import POST_SUCCESS_RESPONSE, POST_ERROR_RESPONSE, POST_EXCEPTION_ERROR_RESPONSE, \
    GET_DATA_FROM_SERIALIZER

logger = logging.getLogger(__name__)


class ProfileApiView(APIView):
    """ User profile view"""
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            instance = Profile.objects.filter(user=request.user).first()
        except Profile.DoesNotExist:
            instance = None

        try:
            profile = ProfileHelper(request)
            data = profile.refectoring_profile_post_data()
            serializer = CreateProfileSerializer(instance=instance, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(POST_SUCCESS_RESPONSE)
            return Response(POST_ERROR_RESPONSE)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            return Response(POST_EXCEPTION_ERROR_RESPONSE)

    def get(self, request):
        profile = ProfileHelper(request)
        data = profile.get_profile_information()
        serializer = ProfileSerializer(data)
        return Response(GET_DATA_FROM_SERIALIZER(serializer))


class UserProfileView(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
