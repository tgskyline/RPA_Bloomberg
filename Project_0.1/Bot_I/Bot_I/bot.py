"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from gettext import find
from botcity.core import DesktopBot
from botcity.plugins.excel import BotExcelPlugin
import numpy as np


# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
bot_excel = BotExcelPlugin()


class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        # self.browse("http://www.botcity.dev")

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )
        # bot_excel.active_sheet()
        bot_excel.read("Arquivo Excel\ExemploExcel.xlsx")
        
        list_exemplo = bot_excel.as_list()
        # x = [float('nan'), 0, 1]
        # print(f"It's np.isnan  : {np.isnan(x)}")
        
        list_len = len(list_exemplo)
        print(list_len)

        for  list_index in range(2, list_len):
                print(list_exemplo[list_index])
                for list_nan in list_exemplo[list_index]:
                    # print(list_nan)
                    # nan = np.isnan(float(list_nan))
                    # print(list_nan)
                    if list_nan== 'nan':
                        print(f"\n" "Há células com = " + str(list_nan))
            
    
        # for list in list_exemplo.length():
        #     if list_exemplo[list] == 'nan':
        #         print("Há células vazias") 
        # print(list_exemplo) 
        # lista = ['nan', 0, 1]
        
        # print(list_exemplo[0]) 

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
