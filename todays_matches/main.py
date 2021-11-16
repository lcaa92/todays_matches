import asyncio
from time import sleep
from pyppeteer import launch

async def main():
    print("Starting script Today's Matches")
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.academiadasapostasbrasil.com/stats/livescores/popup')


    elementFooter = await page.querySelector('.footer')
    sleep(3)
    while elementFooter:
        elementContent = await page.evaluate('(element) => element.textContent', elementFooter)
        print('Hidden matches found ... Showing up. \n', elementContent)
        await page.click('.footer')
        sleep(3)
        elementFooter = await page.querySelector('.footer')
        
    elementTbody = await page.querySelector('tbody')
    elementContent = await page.evaluate('(element) => element.textContent', elementTbody)
    print(elementContent)

    await page.screenshot({'path': 'academia de apostas.png', 'fullPage': True})
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    
