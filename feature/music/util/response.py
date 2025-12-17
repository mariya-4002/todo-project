from rest_framework.response import Response
from rest_framework import status
from math import ceil


# ---------------- SUCCESS RESPONSE ----------------
def success_response(data, meta=None):
    response = {
        "status": "success",
        "data": data
    }

    # add pagination details if present
    if meta is not None:
        response["meta"] = meta

    return Response(response, status=status.HTTP_200_OK)


# ---------------- ERROR RESPONSE ----------------
def error_response(errors):
    return Response(
        {
            "status": "error",
            "errors": errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )


# ---------------- PARSING ----------------
def parse_int(value, default):
    """
    Safely parse integer values
    """
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


# ---------------- PAGINATION + SPLITTING ----------------
def paginate_queryset(data_list, request):
    """
    Handles parsing, pagination and splitting
    """

    page = parse_int(request.GET.get("page"), 1)
    limit = parse_int(request.GET.get("limit"), 10)

    if page < 1:
        page = 1
    if limit < 1:
        limit = 10

    total_items = len(data_list)
    total_pages = ceil(total_items / limit) if limit else 1

    start = (page - 1) * limit
    end = start + limit

    paginated_data = data_list[start:end]

    meta = {
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages
    }

    return paginated_data, meta
