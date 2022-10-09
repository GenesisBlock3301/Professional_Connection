from rest_framework import status, serializers

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
