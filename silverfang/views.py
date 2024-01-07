from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    """
    API endpoint that returns a simple 'Hello, World!' message.
    """
    return Response({'message': 'Hello, World!'})

@api_view(['POST'])
def create_user(request):
    """
    API endpoint that creates a new user.
    """
    # Your code to create a new user goes here
    return Response({'message': 'User created successfully'})

@api_view(['GET'])
def get_user(request, user_id):
    """
    API endpoint that retrieves a user by ID.
    """
    # Your code to retrieve a user by ID goes here
    return Response({'message': f'Retrieving user with ID: {user_id}'})

@api_view(['PUT'])
def update_user(request, user_id):
    """
    API endpoint that updates a user by ID.
    """
    # Your code to update a user by ID goes here
    return Response({'message': f'Updating user with ID: {user_id}'})

@api_view(['DELETE'])
def delete_user(request, user_id):
    """
    API endpoint that deletes a user by ID.
    """
    # Your code to delete a user by ID goes here
    return Response({'message': f'Deleting user with ID: {user_id}'})
#implement a search api endpoint across all users and posts
@api_view(['GET'])
def search(request, query):
    """
    API endpoint that searches for users and posts by a query string.
    """
    
    return Response({'message': f'Searching for query: {query}'})