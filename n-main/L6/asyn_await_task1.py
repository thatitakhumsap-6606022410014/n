import asyncio

async def main():
    print('Pakin')
    task = asyncio.create_task(foo('I ol O')) # สร้าง task และส่งค่า text ไปให้ foo   
    
    print('finish')
   
async def foo(text):
    
    print(text)
    await asyncio.sleep(5)

    
asyncio.run(main())