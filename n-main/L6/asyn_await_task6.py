import asyncio
import time

async def ioioio(wela, chue):
    print('เริ่ม%s ผ่านไปแล้ว %.6f วินาที' % (chue, time.time() - t0))
    await asyncio.sleep(wela)
    print('%sเสร็จสิ้น ผ่านไปแล้ว %.6f วินาที' % (chue, time.time() - t0))

async def main():
    cococoru = [ioioio(1.5, 'เพลง'), ioioio(2.5, 'โหลดอนิเมะ'), ioioio(0.5, 'โหลดหนัง'), ioioio(2, 'โหลดเกม')]
    await asyncio.gather(*cococoru)

t0 = time.time()
asyncio.run(main())
