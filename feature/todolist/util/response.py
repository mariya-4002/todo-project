from rest_framework.response import Response
from rest_framework import status
from math import ceil


# -----------------------------
# COMMON RESPONSE FUNCTIONS
# -----------------------------

def success_response(data=None, message="Success", status_code=status.HTTP_200_OK):
    return Response(
        {
            "status": "success",
            "message": message,
            "data": data
        },
        status=status_code
    )


def error_response(message="Error", errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    return Response(
        {
            "status": "error",
            "message": message,
            "errors": errors
        },
        status=status_code
    )


# -----------------------------
# PAGINATION
# -----------------------------

def paginate_queryset(queryset, page=1, limit=5):
    """
    Splits queryset into pages
    """
    if limit <= 0:
        limit = 5

    total_items = queryset.count()
    total_pages = ceil(total_items / limit) if total_items > 0 else 1

    start = (page - 1) * limit
    end = start + limit

    paginated_data = queryset[start:end]

    return {
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages,
        "results": paginated_data
    }


# -----------------------------
# DATA PARSING
# -----------------------------

def parse_int(value, default=1):
    """
    Safely parse integer values
    """
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def parse_string(value, default=""):
    """
    Safely parse string values
    """
    if value is None:
        return default
    return str(value).strip()


# -----------------------------
# DATA SPLITTING
# -----------------------------

def split_by_comma(value):
    """
    Converts 'a,b,c' → ['a', 'b', 'c']
    """
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]
