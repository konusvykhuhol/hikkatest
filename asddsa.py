# example_module.py
from .. import loader, utils  # type: ignore

turn = False
@loader.tds
class hikka1(loader.Module):
    """модуль для замены да на пизда"""

    strings = {"name": "пизда"}
    async def oncmd(self, message):
        """включить замену"""
        global turn
        turn = True
        await utils.reply(message, "замена включена")

    async def offcmd(self, message):
        """выключить замену"""
        global turn
        turn = False
        await utils.reply(message, "замена выключена")

    async def watcher(self, message):
        """Перехватывает ВСЕ сообщения"""
        if not self.enabled:
            return

        if not getattr(message, "text", None) or message.out:
            return

        text = message.text

        global turn

        if turn:
            new_text = text.replace("да", "пизда").replace("Да", "Пизда").replace("дА","пиздА").replace("ДА","пизДА")
        else:
            new_text = text

        if new_text != text:
            await message.edit(new_text)