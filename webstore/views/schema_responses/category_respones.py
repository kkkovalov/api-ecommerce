from drf_yasg import openapi
from rest_framework import status

from webstore.serializers import CategorySerializer

get_responses = {
    status.HTTP_200_OK: openapi.Response(
        description = 'Sorted categories from the database',
        schema = CategorySerializer(many=True),
        examples = {
            "application/json": {
                        "name": "string",
                        "description": "string",
                        "slug_name": "string",

            }
        }
    ),
    status.HTTP_404_NOT_FOUND: openapi.Response(
        description="No categories found in the database."
    )
}

post_responses = {
    status.HTTP_200_OK: openapi.Response(
        description = "Category added to the database",
        schema = CategorySerializer,
        examples = {
            "application/json": {
                    "name": "string",
                    "description": "string",
                    "slug_name": "string",
            }
        }
    ),
    status.HTTP_400_BAD_REQUEST: openapi.Response(
        description = 'Missing name or description to create a new category. Otherwise, not valid data.',
    ),
    status.HTTP_401_UNAUTHORIZED: openapi.Response(
        description = "Unauthorized. JWToken is missing."
    ),
    status.HTTP_403_FORBIDDEN: openapi.Response(
        description = "Unauthorized. Staff only can access this endpoint."
    ),
}

put_responses = {
    status.HTTP_200_OK: openapi.Response(
        description = "Category updated.",
        schema = CategorySerializer,
        examples = {
            "application/json": {
                    "name": "string",
                    "description": "string",
                    "slug_name": "string",
            }
        }
    ),
    status.HTTP_404_NOT_FOUND: openapi.Response(
        description = "Category not found with specified slug_name",
    ),
    status.HTTP_400_BAD_REQUEST: openapi.Response(
        description = "Data is invalid for this model."
    ),
    status.HTTP_401_UNAUTHORIZED: openapi.Response(
        description = "Unauthorized. JWToken is missing."
    ),
    status.HTTP_403_FORBIDDEN: openapi.Response(
        description = "Unauthorized. Staff only can access this endpoint."
    ),
}


