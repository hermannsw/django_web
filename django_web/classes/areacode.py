# -*- coding: utf-8 -*-


class AreaCode(object):

    @staticmethod
    def __list() -> dict:
        return {
            '01': 'Area_01',
            '02': 'Area_02',
        }

    @staticmethod
    def get(area_code: int) -> str:
        r = AreaCode.__list()
        return r[str(area_code)]

    @staticmethod
    def all() -> dict:
        return AreaCode.__list()

    @staticmethod
    def all_tuple() -> tuple:
        return tuple(AreaCode.__list().items())
