import uuid
from hashlib import md5


class AuthService:
    def get_token(self, username: str, password: str) -> str:
        """
        Get User Token for authorization
        """
        hash_password = get_password_hash(password)
        user = User.objects.filter(username=username, password=hash_password).first()

        if not user:
            raise UserNotFoundError(username=username)

        # user_token = md5(str(user).encode('utf-8')).hexdigest()  # md5 - is old, and always the same token!
        user_token = str(uuid.uuid4())
        user.token = user_token
        user.save()

        return user_token

    def authenticate(self, username: str, password: str) -> User:
        """
        Authenticate user
        """
        user = User.objects.filter(username=username, password=hash_password).first()

        if user is None:
            raise UserNotFoundError(username=username)

        if not user.is_active:
            raise UserNotActiveError(user_id=user.id)

        return user
