# example_module.py
from .. import loader, utils  # type: ignore


@loader.tds
class calculator(loader.Module):
    """Описание модуля"""

    strings = {"name": "calculator :D"}


    async def sumcmd(self,message):
        """сумма двух чисел. вводить в формате .sum [число] [число]"""
        b=utils.get_args_raw(message)
        a=b.split(" ")
        if len(a)==2:
            if a[1].isdigit() and a[2].isdigit():
                await utils.answer(message, f"сумма{a[1]} и {a[2]} =", a[1]+a[2])
            else:
                await utils.answer(message, f"введены не числа!")
        else:
            await utils.answer(message, f"неверный формат!")