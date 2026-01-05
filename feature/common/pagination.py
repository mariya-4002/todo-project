def paginate_queryset(queryset, page=1, limit=10):
    try:
        page = int(page)
        limit = int(limit)
    except (TypeError, ValueError):
        page = 1
        limit = 10

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": queryset.count(),
        "results": queryset[start:end]
    }
