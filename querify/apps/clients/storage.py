import datetime
import pwd
import pydantic
import os
import os.path


class File(
    pydantic.BaseModel,
):
    name: str
    size_in_bytes: str
    owner: str
    update_date: datetime.datetime
    access_date: datetime.datetime



class Client:
    @staticmethod
    def get_files() -> list[File]:
        dir_path = '/Users/obadihi/Downloads/'

        files = []

        for obj in os.listdir(dir_path):
            if os.path.isfile(obj):
                files.append(
                    File(
                        name=str(obj),
                        size_in_bytes=os.stat(obj).st_size,
                        owner=pwd.getpwuid(os.stat(obj).st_uid).pw_name,
                        update_date=datetime.datetime.fromtimestamp(os.path.getmtime(obj)),
                        access_date=datetime.datetime.fromtimestamp(os.path.getatime(obj)),
                    )
                )

        return files
