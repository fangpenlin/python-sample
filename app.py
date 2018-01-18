import os

import asyncio

from aiohttp import web


async def loading_gif(request):
    await asyncio.sleep(5)
    return web.HTTPFound('https://i.giphy.com/media/y1ZBcOGOOtlpC/200.gif')


async def longcat(request):
    return web.HTTPFound('http://i0.kym-cdn.com/photos/images/facebook/000/002/110/longcat.jpg')


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/loading.gif', loading_gif)
    app.router.add_get('/longcat.jpg', longcat)
    web.run_app(app, port=os.getenv('PORT', 5000))
