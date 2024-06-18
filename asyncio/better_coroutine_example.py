"""
The aiohttp package is designed for 
creating asynchronous HTTP clients and servers
"""

import aiohttp
import asyncio
import os
import async_timeout

async def download_coroutine(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            filename = os.path.basename(url)
            with open(filename, 'wb') as f_handle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f_handle.write(chunk)
            return await response.release()
        

async def main(loop):
    urls =[]
    
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [download_coroutine(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))


