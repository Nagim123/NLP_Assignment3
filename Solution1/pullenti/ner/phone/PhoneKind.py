﻿# SDK Pullenti Lingvo, version 4.22, february 2024. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter Unisharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru

from enum import IntEnum

class PhoneKind(IntEnum):
    """ Тип телефонного номера """
    UNDEFINED = 0
    HOME = 1
    """ Домашний """
    MOBILE = 2
    """ Мобильный """
    WORK = 3
    """ Рабочий """
    FAX = 4
    """ Факс """
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)