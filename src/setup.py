import json

CONFIG_FILE_PATH = "../config/api-config.json"


def loadBasicInfo() -> dict:
    basicInfo = {}
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            basicInfo = json.load(file)
    except FileNotFoundError:
        print("basic info file not found")
        return {}
    if not basicInfo:
        return {}
    return basicInfo
