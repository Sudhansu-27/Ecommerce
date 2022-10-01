import graphene
from graphene_django import DjangoObjectType
from orders.models import Order
from .models import(
    Category,
    SubCategory,
    Product,
    ProductImage,
)

class OrderType(DjangoObjectType):
    class Meta:
        model=Order 

class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        
class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)   
    
    class Arguments:
        name = graphene.String()  
          
 
    def mutate(self,info, name:str):
       category = Category(
           name=name
        )
       
       category.save() 
       
       return CreateCategory(name=name)   
   
class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()   
        
class SubCategoryType(DjangoObjectType):
    class Meta:
        model= SubCategory
        
class ProductImageType(DjangoObjectType):
    class Meta:
        model=ProductImage
        fields = ("id" , "image")
        
    def resolve_image(self,info):
        if self.image:
            self.image = info.context.build_absolute_url(self.image.url)
        return self.image            

class ProductType(DjangoObjectType):
    class Meta:
        model=Product

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    product = graphene.Field(ProductType , id=graphene.Int(required=True))
    category = graphene.Field(CategoryType , id=graphene.Int(), name=graphene.String())
    subCategory = graphene.Field(SubCategoryType, id=graphene.Int(), name=graphene.String())
    
    def resolve_all_products(root , info):
        return Product.objects.all()
        
    def resolve_product(root, info , id):
        try:
            return Product.objects.get(pk=id)   
        except Product.DoesNotExist:
            return None
        
    def resolve_category(root, info, id=None, name=None):
        try:
            if(id):
                return Category.objects.get(pk=id)
            if(name):
                return Category.objects.get(name=name)
            else:
                return None
        except Category.DoesNotExist:
            return None
        
    def resolve_subCategory(root , info , id=None , name=None):
        try:
            if(id):
                return SubCategory.objects.get(pk=id)
            if(name):
                return SubCategory.objects.get(name=name)
            else:
                return None
        except SubCategory.DoesNotExist:
            return None  
    
schema = graphene.Schema(query=Query, mutation=Mutation)