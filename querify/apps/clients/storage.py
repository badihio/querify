import datetime
import pwd
import pydantic
import os
import os.path


class File(
    pydantic.BaseModel,
):
    name: str
    size_in_bytes: int
    owner: str
    update_date: datetime.datetime
    access_date: datetime.datetime



class Client:
    @staticmethod
    def get_files() -> list[File]:
        dir_path = os.getcwd()

        files = []

        for obj in os.listdir(dir_path):
            full_obj = os.path.join(dir_path, obj)
            if os.path.isfile(full_obj):
                files.append(
                    File(
                        name=str(obj),
                        size_in_bytes=os.stat(full_obj).st_size,
                        owner=pwd.getpwuid(os.stat(full_obj).st_uid).pw_name,
                        update_date=datetime.datetime.fromtimestamp(os.path.getmtime(full_obj)),
                        access_date=datetime.datetime.fromtimestamp(os.path.getatime(full_obj)),
                    )
                )

        return files
