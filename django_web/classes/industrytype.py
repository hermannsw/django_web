# -*- coding: utf-8 -*-


class IndustryType(object):

    @staticmethod
    def __list() -> dict:
        return {
            '01': 'etc_industry',
        }

    @staticmethod
    def get(industry_type_code: int) -> str:
        r = IndustryType.__list()
        return r[str(industry_type_code)]

    @staticmethod
    def all() -> dict:
        return IndustryType.__list()

    @staticmethod
    def all_tuple() -> tuple:
        return tuple(IndustryType.__list().items())
