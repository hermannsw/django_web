# -*- coding: utf-8 -*-


class JobType(object):

    @staticmethod
    def __list() -> dict:
        return {
            '01': 'etc_jobtype',
        }

    @staticmethod
    def get(job_type_code: int) -> str:
        r = JobType.__list()
        return r[str(job_type_code)]

    @staticmethod
    def all() -> dict:
        return JobType.__list()

    @staticmethod
    def all_tuple() -> tuple:
        return tuple(JobType.__list().items())
