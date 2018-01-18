import os

import asyncio

from aiohttp import web


async def cutty_cats(request):
    await asyncio.sleep(5)
    return web.HTTPFound('https://static.pexels.com/photos/45170/kittens-cat-cat-puppy-rush-45170.jpeg')


async def longcat(request):
    return web.HTTPFound('http://i0.kym-cdn.com/photos/images/facebook/000/002/110/longcat.jpg')


if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/cutty_cats.jpg', cutty_cats)
    app.router.add_get('/longcat.jpg', longcat)
    web.run_app(app, port=int(os.getenv('PORT', 5000)))
