from datetime import datetime


class PublicationDate(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")

        split_string = v.split(":  ")
        if split_string[0] != "Fonte/Data da Publicação":
            raise ValueError("wrong text for publication date")

        publication_date = datetime.strptime(split_string[1], "%d/%m/%Y")
        return publication_date.strftime("%Y%m%d")


class JudgementDate(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")

        split_string = v.split(": ")

        if split_string[0] != "Data do Julgamento":
            raise ValueError("wrong text for judgement date")

        judgement_date = datetime.strptime(split_string[1], "%d/%m/%Y %H:%M:%S")
        return judgement_date.strftime("%Y%m%d")


class JusticeSecret:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v) -> bool:
        split_string = v.split(": ")
        if split_string[0] != "Segredo de Justiça":
            raise ValueError("wrong text for justice secret")
        match split_string[1]:
            case "Não":
                return False
            case "Sim":
                return True
            case _:
                raise ValueError("invalid justice secret")


class District(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")

        split_string = v.split(": ")

        if split_string[0] != "Comarca":
            raise ValueError("wrong text for district")

        return split_string[1]


class DecisionText(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")
        split_string = v.split("\n\n")
        # TODO: add validation for base string
        # if ("Decisão" not in split_string[0]) or ("Ementa" not in split_string[0]):
        #     raise ValueError("wrong text for decision text")
        return split_string[1]


class Judge(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")
        split_string = v.split(": ")

        if "Relator(a)" not in split_string[0]:
            raise ValueError("wrong text for judge")
        judge_name, _ = split_string[1].split("\n")
        return judge_name


class JudgingBody(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")

        split_string = v.split(": ")

        if split_string[0] != "Órgão Julgador":
            raise ValueError("wrong text for judging body")

        return split_string[1]


class DocumentHref(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            raise TypeError("string required")

        split_string = v.split(".replace('")

        if split_string[0] != "javascript:document.location":
            raise ValueError("wrong href text")

        base_website = "https://portal.tjpr.jus.br"
        return base_website + split_string[1].split("%")[0]
