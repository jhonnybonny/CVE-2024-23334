from aiohttp import web
import asyncio

async def index(request):
    return web.Response(text="CVE-2024-23334 PoC")

async def main():
    app = web.Application()
    app.router.add_get('/', index)

    app.router.add_static('/static/',
                          path='static/',
                          follow_symlinks=True)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8081)

    await site.start()

    print("Server started on http://localhost:8081")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
