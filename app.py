from fastapi import FastAPI

from jollymax import JollyMaxParser

app = FastAPI(
    title="JollyMax Parser API",
    description="API for parsing **PUBG Mobile** User data",
    contact={
        "name": "Github",
        "url":  "https://github.com/hoosnick/jollymax-parser",
    },
    license_info={
        "name": "Apache 2.0",
        "url":  "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    docs_url="/",
    redoc_url=None
)


@app.get("/get", tags=["GET"])
async def fetch_user_data(pubg_id: int):
    async with JollyMaxParser(pubg_id) as pubg_user:
        return {
            "id":       pubg_user.id,
            "nickName": pubg_user.nick_name
        }
