# example_module.py
from .. import loader, utils  # type: ignore


@loader.tds
class ExampleModule(loader.Module):
    """Описание модуля"""  # ЭТО ОБЯЗАТЕЛЬНО!

    strings = {"name": "ExampleModule"}  # И ЭТО ТОЖЕ!

    async def testcmd(self, message):
        """Тестовая команда"""
        await utils.answer(message, "✅ Модуль работает!")