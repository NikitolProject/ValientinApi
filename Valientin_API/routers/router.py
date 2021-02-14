from fastapi import APIRouter

from Valientin_API.db.db import Database
from Valientin_API.utils.parser import parser
from Valientin_API.utils.generator import generator


api_router = APIRouter()
db = Database()


@api_router.get("/get")
async def get():
  test = await parser("https://www.google.com/search?q=%D0%92%D0%B0%D0%BB%D0%B5%D0%BD%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&hl=ru&sxsrf=ALeKk01H83JnwPDds2hA3yxoSeWeMSCa1g:1613297294665&source=lnms&tbm=isch&sa=X&ved=2ahUKEwilh6nhkOnuAhUrxosKHZfFAeoQ_AUoAXoECBoQAw&biw=1745&bih=819")
  generate = await generator(test)
  return {"success": True, "images": generate}
