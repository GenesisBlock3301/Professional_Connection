from rest_framework import status

"""All dynamic response exist here...
"""

POST_SUCCESS_RESPONSE = {
    "success": "Request success",
    "status": status.HTTP_200_OK
}

POST_ERROR_RESPONSE = {
    "error": "Request failed for error",
    "status": status.HTTP_400_BAD_REQUEST
}

POST_EXCEPTION_ERROR_RESPONSE = {
    "error": "Request failed for exception",
    "status": status.HTTP_400_BAD_REQUEST
}

GET_DATA_FROM_SERIALIZER = lambda serializer: {"data": serializer.data, "status": status.HTTP_200_OK}

ELEMENT_NOT_EXIST = {
    "message": "Element doesn't exist.",
    "status": status.HTTP_204_NO_CONTENT
}

FRIEND_ACTION_RESPONSE = {
    "sent_request": {"message": "Successfully send friend request"},
    "sent_request_failed": {"message": "Request already sent waiting for further action."},
    "request_critical_failed": {"message": "send request not working properly"},
    "already_friend": {"message": "Both are already friend"},
    "has_profile": {"message": "Before send request create profile"},
    "accept_request": {"message": "Request accept successfully."},
    "unauthorized_for_accept": {"message": "You are not authorized to accept this request"},
    "delete_successfully": {"message": "friend deleted successfully."},
    "block_failed": {"message": "blocked failed."},
    "blocked": {"message": "blocked successfully."}
}
