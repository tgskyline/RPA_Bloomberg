from botcity.base.utils import find_bot_class
from . import bot
from botcity.plugins.excel import BotExcelPlugin

klass = find_bot_class(bot)[0]
klass.main()
bot_excel = BotExcelPlugin()