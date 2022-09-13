from .models import Company


class CompanyHelper:
    def __init__(self, request):
        self.request = request

    @staticmethod
    def get_all_companies():
        companies = Company.objects.select_related("manager").all().order_by("name")
        return companies

    @staticmethod
    def get_company(id):
        company = Company.objects.select_related("manager").filter(id=id).first()
        return company
