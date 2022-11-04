from abc import ABC, abstractmethod


class CommonIterableItem(ABC):
    """Common operation for some module"""
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
    """Try to use dependency injection and  follow SOLID principle here"""
    def __init__(self, common_helper: CommonIterableItem):
        self.common_helper = common_helper

    def my_items(self, user):
        """Get all user's item"""
        return self.common_helper.my_items(user)

    def all_items(self):
        """Get all available item"""
        return self.common_helper.all_items()

    def get_item(self, _id):
        """Get single item using ID"""
        return self.common_helper.get_item(_id)

    def pagination(self, data, serializer_class):
        """Paginate item based on data and serializer class"""
        return self.common_helper.pagination(data, serializer_class)

