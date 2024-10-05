from rest_framework.response import Response


def does_not_exist():
    return Response({'error': 'Query Error'})
