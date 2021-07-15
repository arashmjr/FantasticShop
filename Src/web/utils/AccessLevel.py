from enum import IntEnum


class AccessLevel(IntEnum):

    guest = 0

    authorize_user = 1

    super_user = 2
