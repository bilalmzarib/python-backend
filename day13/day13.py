import asyncio
import aiohttp
import time

URLS = [
    "https://picsum.photos/200/300",
    "https://picsum.photos/300/300",
    "https://picsum.photos/400/300",
    "https://picsum.photos/500/300"
]

# دالة لتحميل ملف واحد
async def download_file(session, url, index):
    async with session.get(url) as response:
        content = await response.read()
        filename = f"file_{index}.jpg"
        with open(filename, "wb") as f:
            f.write(content)
        print(f" تم تحميل {filename}")


async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(URLS):
            tasks.append(download_file(session, url, i + 1))
        await asyncio.gather(*tasks)
    print(f"⏱️ المدة الإجمالية: {time.time() - start_time:.2f} ثانية")

# تشغيل البرنامج
if __name__ == "__main__":
    asyncio.run(main())
