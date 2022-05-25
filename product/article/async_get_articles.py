import aiohttp

url = 'https://wbx-content-v2.wbstatic.net/ru/'


async def get_articles(article, json_response):
    """ Функция для асинхронной отправки запросов"""

    async with aiohttp.ClientSession() as session:
        # Отрпавляем запрос и получаем полное описание товара
        async with session.get(f'{url}{article}.json') as response:

            # Создаём пустой словарь, куда будем помещать необходимые значения ответа
            description = {}

            # Помещаем необходимые значения ответа в словарь
            json = await response.json()
            description['Article'] = json.get('nm_id')
            description['Title'] = json.get('imt_name')
            if json.get('selling'):
                description['Brand'] = json['selling'].get('brand_name')
            else:
                description['Brand'] = None

            # Словарь со значениями помещаем в глобальный список
            json_response.append(description)
