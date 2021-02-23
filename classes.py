import pandas

from db import sql


class Application(object):

    def __init__(self, input_file: str, out_file_path: str):

        """
        Методы и атрибуты(еще называют полями или свойствами) класса, которые не должны быть доступны
        снаружи(т.е. за пределами класса в котором определены) принято называть с нижним подчеркиванием в начале.
        Это не запретит доступ к ним снаружи(в python это к сожалению не возможно без костылей), но нормальные IDE,
        такие как pyCharm, понимают эти названия и не выдают их в списке автодополнения при наборе кода и
        подчеркивают их при попытке вызвать снаружи.
        С двумя подчеркиваниями в начале называют методы и атрибуты которые не доступны с наружи и не доступны
        в дочерних классах, а с одним подчеркиванием которые не доступные снаружи, но доступны в дочерних классах.
        """

        # Создаем списки в конструкторе, а не передаем в параметрах.
        # Даем имена с одним нижнем подчеркиванием, что бы они были доступны только в дочернем классе
        self._uuids = []
        self._products = []
        self._images = []
        self._videos = []

        self._catalog = pandas.read_excel(input_file, engine='openpyxl')
        self._out_file_path = out_file_path

    def _build_migration(self) -> None:
        """Write SQL migration to file"""
        delete_all = sql.DELETE_ALL % (self._uuids, self._uuids, self._uuids)
        with open(self._out_file_path, 'w') as file_handle:
            file_handle.write(sql.PIG_INSERT_ITEMS)
            for list_item in self._products:
                file_handle.write('%s\n' % list_item)
            file_handle.write('\n')
            for list_item in self._videos:
                file_handle.write('%s\n' % list_item)
            file_handle.write('\n')
            for list_item in self._images:
                file_handle.write('%s\n' % list_item)
            file_handle.write('\n\n-- +pig Down\n')
            file_handle.write('%s\n' % delete_all.replace("[", "").replace("]", ""))
