import asyncio
import zendriver as zd
import sys
from pathlib import Path
import shutil, os, tempfile


async def main():

    browser = await zd.start(
        headless=False,
        no_sandbox=True
    )

    page = await browser.get('https://maps.app.goo.gl/CeRMHb8v5ZjKejhu7')
    
    await page.wait_for_ready_state("complete")
    
    # do a full page reload
    await page.reload()

    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        await browser.stop()


if __name__ == '__main__':
    # since asyncio.run never worked (for me)
    asyncio.run(main())
