
Usuarios = Usuario.objects.all()


firstUsuario = Usuario.objects.first()


lastUsuario = Usuario.objects.last()


UsuarioByName = Usuario.objects.get(name='Peter Piper')


UsuarioById = Usuario.objects.get(id=4)


firstUsuario.order_set.all()


order = Order.objects.first() 
parentName = order.Usuario.name


Productos = Producto.objects.filter(category="Out Door")


leastToGreatest = Producto.objects.all().order_by('id') 
greatestToLeast = Producto.objects.all().order_by('-id') 


ProductoosFiltered = Producto.objects.filter(tags__name="Sports")

ballOrders = firstUsuario.order_set.filter(Productoo__name="Ball").count()


allOrders = {}


for order in firstUsuario.order_set.all():
	if order.Productoo.name in allOrders:
		allOrders[order.Productoo.name] += 1
	else:
		allOrders[order.Productoo.name] = 1


class ParentModel(models.Model):

	name = models.CharField(max_length=200, null=True)


class ChildModel(models.Model):

	parent = models.ForeignKey(ParentModel)
	name = models.CharField(max_length=200, null=True)


parent = ParentModel.objects.first()
parent.childmodel_set.all()