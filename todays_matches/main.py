import asyncio
from time import sleep
from pyppeteer import launch
from bs4 import BeautifulSoup

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

    elementTable = await page.querySelector('.competition-today')
    elementTableContent = await page.evaluate('(element) => element.innerHTML', elementTable)
    await page.screenshot({'path': 'academia de apostas.png', 'fullPage': True})
    await browser.close()

    soupTable = BeautifulSoup(elementTableContent, 'html.parser')
    tbodyElement = soupTable.find('tbody')
    elements = tbodyElement.find_all('tr')

    for el in elements:
        soupEl = el.find_all('td')
        country_championship =  soupEl[1].find('a').get('title').split('-')
        country = country_championship[0].rstrip()
        championship = country_championship[1].lstrip()
        team_home = soupEl[4].find('p').text
        team_visitor = soupEl[6].find('p').text
        link_details = soupEl[7].find('a').get('href')
        jsonObj = {
            "country": country,
            "championship": championship,
            "team_home": team_home,
            "team_visitor": team_visitor,
            "link_details": link_details
        }
        print(jsonObj)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    
