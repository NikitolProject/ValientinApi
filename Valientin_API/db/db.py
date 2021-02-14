from tortoise import Tortoise


class Database:
  def __init__(self):
    pass

  async def init(self):
    await Tortoise.init(db_url="sqlite://test.sqlite3", modules={"models": ["Valientin_API.db.models"]})
    await Tortoise.generate_schemas()

  async def add(self, model, **kwargs):
    await model.create(**kwargs)

  async def delete(self, model, **kwargs):
    await model.filter(**kwargs).delete()

  async def update(self, model, filter, **kwargs):
    await model.filter(**filter).update(**kwargs)

  async def get_values(self, model, *args):
    return await model.all().values(*args)

  async def get_value(self, model, **kwargs):
    return await model.filter(**kwargs).values()
