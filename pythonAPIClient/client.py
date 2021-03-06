import requests
from .error import Error, AuthenticationError, InternalError, InvalidClientIdError, InvalidClientSecretError, ResourceNotFoundError
from .camera import Camera, IPCamera, NonIPCamera, StreamCamera

class Client(object):
    # Static variable to store the base URL.
    base_URL = 'https://cam2-api.herokuapp.com/'
    """
    Represent a CAM2 client application.
    """
    def request_token(self):
        url = Client.base_URL +'auth/?clientID='+self.id+'&clientSecret='+self.secret
        response = requests.get(url)
        if(response.status_code == 200):
            self.token = response.json()['token']
        elif(response.status_code == 404 ):
            raise ResourceNotFoundError(response.json()['message'])
        elif (response.status_code == 401):
            raise AuthenticationError(response.json()['message'])
        else:
            raise InternalError()

    def header_builder(self):
        head = {'Authorization': 'Bearer ' + str(self.token)}
        return head

    def __init__(self, id, secret):
        #clientId are of a fixed length of 96 characters.
        if len(id) != 96:
            raise InvalidClientIdError
        # clientSecret are of a fixed length of 71 characters.
        if len(secret) != 71:
            raise InvalidClientSecretError
        self.id = id
        self.secret = secret
        self.token = None

    """
    Functions for webUI
    """
    # TODO: return clientID and client secret
    def register(self, owner, permissionLevel='user'):
        pass
    
    # TODO: update client's owner
    def update_owner(self, clientID, owner):
        pass

    # TODO: update client's permissionLevel
    def update_permission(self, clientID, permissionLevel):
        pass

    # TODO: get clientID by owner
    def client_ids_by_owner(self, owner):
        pass

    # TODO: get api usage count by client
    def usage_by_client(self, clientID):
        pass

    """
    Function for admin
    """

    # TODO: add a camera to database
    def add_camera(self, Camera):
        pass

    # TODO: update a camera in database
    # replace others with desired field names
    def update_camera(self, camID, others):
        pass

    """
    Function for user
    """

    # TODO: get a camera
    def camera_by_id(self, cameraID):
        pass

    # TODO: search a camera
    # replace others with desired field names
    def search_camera(self, others):
        pass