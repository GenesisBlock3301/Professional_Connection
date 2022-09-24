from abc import ABC, abstractmethod


class CommonIterableItem(ABC):
    @abstractmethod
    def get_item(self, _id: int):
        pass

    @abstractmethod
    def my_items(self, user):
        pass

    @abstractmethod
    def all_items(self):
        pass

    @abstractmethod
    def pagination(self, data, serializer_class):
        pass


class HelperAdapter:
    def __init__(self, common_helper: CommonIterableItem):
        self.common_helper = common_helper

    def my_items(self, user):
        return self.common_helper.my_items(user)

    def all_items(self):
        return self.common_helper.all_items()

    def get_item(self, _id):
        return self.common_helper.get_item(_id)

    def pagination(self, data, serializer_class):
        return self.common_helper.pagination(data, serializer_class)

