import graphene
from graphene_django import DjangoObjectType

from .models import(
    Category,
    SubCategory,
    Product,
    ProductImage,
)

class ProductType(DjangoObjectType):
    class Meta:
        model=Product

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    
    def resolve_all_products(root , info):
        return Product.objects.all()
        