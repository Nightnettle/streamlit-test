import asyncio
import zendriver as zd
import sys
from pathlib import Path
import shutil, os, tempfile

import streamlit as st


async def scraper():

    browser = await zd.start(
        headless=False,
        no_sandbox=True
    )

    page = await browser.get('https://maps.app.goo.gl/CeRMHb8v5ZjKejhu7')
    
    await page.wait_for_ready_state("complete")
    
    # do a full page reload
    await page.reload()

    await asyncio.sleep(4)

    await page.save_screenshot()

    await asyncio.sleep(5)

    await browser.stop()


def main():
    st.title("Web Scraper with Zendriver and Streamlit")

    if st.button("Start Scraping"):
        st.write("Scraping started...")
        asyncio.run(scraper())
        st.write("Scraping completed!")


if __name__ == '__main__':
    main()
