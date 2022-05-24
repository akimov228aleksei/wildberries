import asyncio

from rest_framework.response import Response
from rest_framework.views import APIView

from .async_get_articles import get_articles
from .conversion_xlsx import xlsx_to_tuple
from .async_eventloop import get_or_create_eventloop


class ListArticles(APIView):
    """ Класс для отображения товаров и описания """

    def post(self, request):
        # Создаём глобальный список, куда будет помещенна информация о товаре
        json_response = []

        # Проверяем наличие файла
        file = request.data.get('file')
        if not file:
            return Response({"Error": "You must upload a file"})

        # Преобразуем xlsx файл в кортеж
        articles = xlsx_to_tuple(file=file)

        # Устанавливаем текущее значение политики
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        ioloop = get_or_create_eventloop()

        # Создаём задачи
        tasks = [ioloop.create_task(get_articles(article, json_response))
                 for article in articles]
        ioloop.run_until_complete(asyncio.wait(tasks))
        ioloop.close()

        # Если всего один элемент, то достаём его из списка
        if len(json_response) == 1:
            json_response = json_response[0]

        return Response(json_response)
