from rest_framework.response import Response
from rest_framework import status


def success_response(data=None, message="Success", status_code=status.HTTP_200_OK):
    return Response(
        {
            "success": True,
            "message": message,
            "data": data
        },
        status=status_code
    )


def error_response(message="Error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    return Response(
        {
            "success": False,
            "message": message,
            "errors": errors
        },
        status=status_code
    )


def error_400(errors=None):
    return error_response(
        message="Validation failed",
        errors=errors,
        status_code=status.HTTP_400_BAD_REQUEST
    )


def error_404():
    return error_response(
        message="Data not found",
        status_code=status.HTTP_404_NOT_FOUND
    )
