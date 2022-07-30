from drf_yasg import openapi

signup_request_schema_body = openapi.Schema(
    name='body',
    description="Signup Request Schema",
    type=openapi.TYPE_OBJECT,
    properties={
        "email": openapi.Schema(type=openapi.TYPE_STRING),
        "password1": openapi.Schema(type=openapi.TYPE_STRING),
        "password2": openapi.Schema(type=openapi.TYPE_STRING),
    }
)

signup_response_schema_body = {
    "200": openapi.Response(
        description="Signup Response",
        schema=openapi.Schema(
            name="body",
            description="Signup Response Schema",
            type=openapi.TYPE_OBJECT,
            properties={
                "code": openapi.Schema(type=openapi.TYPE_STRING),
                "status": openapi.Schema(type=openapi.TYPE_STRING)
            }
        )
    )
}
