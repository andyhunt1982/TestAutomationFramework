from enum import Enum
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Auth(Enum):
    API_KEY = "apiKey"
    EMPTY = ""
    O_AUTH = "OAuth"
    USER_AGENT = "User-Agent"
    X_MASHAPE_KEY = "X-Mashape-Key"


class Cors(Enum):
    NO = "no"
    UNKNOWN = "unknown"
    UNKOWN = "unkown"
    YES = "yes"


class Entry:
    api: Optional[str]
    description: Optional[str]
    auth: Optional[Auth]
    https: Optional[bool]
    cors: Optional[Cors]
    link: Optional[str]
    category: Optional[str]

    def __init__(self, api: Optional[str], description: Optional[str], auth: Optional[Auth], https: Optional[bool], cors: Optional[Cors], link: Optional[str], category: Optional[str]) -> None:
        self.api = api
        self.description = description
        self.auth = auth
        self.https = https
        self.cors = cors
        self.link = link
        self.category = category

    @staticmethod
    def from_dict(obj: Any) -> 'Entry':
        assert isinstance(obj, dict)
        api = from_union([from_str, from_none], obj.get("API"))
        description = from_union([from_str, from_none], obj.get("Description"))
        auth = from_union([Auth, from_none], obj.get("Auth"))
        https = from_union([from_bool, from_none], obj.get("HTTPS"))
        cors = from_union([Cors, from_none], obj.get("Cors"))
        link = from_union([from_str, from_none], obj.get("Link"))
        category = from_union([from_str, from_none], obj.get("Category"))
        return Entry(api, description, auth, https, cors, link, category)

    def to_dict(self) -> dict:
        result: dict = {}
        result["API"] = from_union([from_str, from_none], self.api)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["Auth"] = from_union([lambda x: to_enum(Auth, x), from_none], self.auth)
        result["HTTPS"] = from_union([from_bool, from_none], self.https)
        result["Cors"] = from_union([lambda x: to_enum(Cors, x), from_none], self.cors)
        result["Link"] = from_union([from_str, from_none], self.link)
        result["Category"] = from_union([from_str, from_none], self.category)
        return result


class PublicAPIEntriesResponse:
    count: Optional[int]
    entries: Optional[List[Entry]]

    def __init__(self, count: Optional[int], entries: Optional[List[Entry]]) -> None:
        self.count = count
        self.entries = entries

    @staticmethod
    def from_dict(obj: Any) -> 'PublicAPIEntriesResponse':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        entries = from_union([lambda x: from_list(Entry.from_dict, x), from_none], obj.get("entries"))
        return PublicAPIEntriesResponse(count, entries)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        result["entries"] = from_union([lambda x: from_list(lambda x: to_class(Entry, x), x), from_none], self.entries)
        return result


def public_api_entries_response_from_dict(s: Any) -> PublicAPIEntriesResponse:
    return PublicAPIEntriesResponse.from_dict(s)


def public_api_entries_response_to_dict(x: PublicAPIEntriesResponse) -> Any:
    return to_class(PublicAPIEntriesResponse, x)
