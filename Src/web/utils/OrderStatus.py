from enum import IntEnum


class OrderStatus(IntEnum):

    inActive = -1

    inProgress = 0

    delivery = 1

    delivered = 2


