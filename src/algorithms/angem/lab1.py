from src.datamodels.labs import AngemLab1Request, AngemLab1Response


def check_lab(condition: AngemLab1Request, user_answer: AngemLab1Response) -> bool:
    return