from dotenv import load_dotenv
from pathlib import Path
from os import path, environ

class Environment:
    def __init__(self):
        execPath = Path(__file__).parent.resolve()
        envFile = path.join(execPath, '.env')
        if not path.exists(envFile):
            print(f'Missing environment file \'{envFile}\'')
            exit(1)
        isEnvLoad = load_dotenv(dotenv_path=envFile)
        if not isEnvLoad:
            print('Couldn\'t load environment file')
            exit(1)
        self.originPath = environ.get('ORIGIN_PATH')