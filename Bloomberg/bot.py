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
# Instantiate the plugin

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


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
        
        # self.read(r'.\Arquivo Excel\ExemploExcel.xlsx')
        
        # Abri o Bloomberg
        self.execute(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Bloomberg\Bloomberg.lnk')
        
        if not self.find( "TXT_Bloomberg", matching=0.97, waiting_time=80000):
            self.not_found("TXT_Bloomberg")
        print('\n>>> Bloomberg aberto com sucesso!\n')
        
        # Preenche o Usuário
        if not self.find( "FLD_LoginName", matching=0.97, waiting_time=10000):
            self.not_found("FLD_LoginName")
        self.click_relative(61, 27)
        self.paste('ABC123')
        print('>>> Preenchido Usuario!\n')
        
        # Preenche o Senha
        if not self.find( "FLD_Password", matching=0.97, waiting_time=10000):
            self.not_found("FLD_Password")
        self.click_relative(70, 27)
        self.paste('123ABC')
        print('>>> Preenchido Senha!\n')
        
        # Clica no Botão Login
        if not self.find( "BTN_Login", matching=0.97, waiting_time=10000):
            self.not_found("BTN_Login")
        self.click()
        print('>>> Click no Botao Login!\n')
        
        # Valida mensagem de Usuário e Senha Incorreto
        if not self.find( "MSG_LoginOrPassIncorrect", matching=0.97, waiting_time=10000):
            self.not_found("MSG_LoginOrPassIncorrect")
            
        if not self.find_text( "TXT_LoginOrPassIncorrect", waiting_time=10000):    self.not_found("TXT_LoginOrPassIncorrect")
        print('>>> Exibido mensagem de Usuario e Senha Incorreto, conforme esperado!\n')
        
    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()
