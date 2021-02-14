from tortoise import Model, fields


class ImageModel(Model):
  url = fields.TextField()
  image = fields.TextField()

  def __str__(self):
    return self.url
    