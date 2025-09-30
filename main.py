# example_module.py
from .. import loader, utils  # type: ignore


@loader.tds
class ExampleModule(loader.Module):
    """Описание модуля"""  # ЭТО ОБЯЗАТЕЛЬНО!

    strings = {"name": "ExampleModule"}  # И ЭТО ТОЖЕ!

    async def testcmd(self, message):
        """Тестовая команда"""
        await utils.answer(message, "✅ Модуль работает!")

    async def sumcmd(self,message):
        """сумма двух чисел. вводить в формате .sum [число] [число]"""
        a=message.split(" ")
        if len(a)==3:
            if a[1].typeof()==int and a[2].typeof()==int:
                await utils.answer(message, f"сумма{a[1]} и {a[2]} =", a[1]+a[2])
            else:
                await utils.answer(message, f"введены не числа!")
        else:
            await utils.answer(message, f"неверный формат!")