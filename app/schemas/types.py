from enum import Enum
class FriendshipStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


class TripStatus(str, Enum):
    INCOMING = "incoming"
    ONGOING = "ongoing"
    COMPLETE = "complete"


class MemberRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"


class InviteStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"


class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"