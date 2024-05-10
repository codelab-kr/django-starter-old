from mangum import Mangum

from core.asgi import application

handler = Mangum(application, lifespan="off")
