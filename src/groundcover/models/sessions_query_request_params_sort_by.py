from __future__ import annotations

from enum import Enum


class SessionsQueryRequestParamsSortBy(str, Enum):
    BROWSER = "browser"
    COUNTRY = "country"
    DEVICEMODEL = "deviceModel"
    DURATIONMILLI = "durationMilli"
    ENDTIME = "endTime"
    ISMOBILE = "isMobile"
    OSNAME = "osName"
    PAGECOUNT = "pageCount"
    SESSIONERRORS = "sessionErrors"
    SESSIONID = "sessionID"
    STARTTIME = "startTime"
    USEREMAIL = "userEmail"
    USERID = "userId"

    def __str__(self) -> str:
        return str(self.value)
