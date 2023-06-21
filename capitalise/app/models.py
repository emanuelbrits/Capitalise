from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    cod_usr = models.AutoField(primary_key=True)
    nom_usr = models.CharField(max_length=60)
    num_cpf = models.CharField(max_length=11)
    num_telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)

class Carteira(models.Model):
    id_carteira = models.AutoField(primary_key=True)
    valor_aplicado = models.DecimalField(max_digits=20, decimal_places=2)
    saldo_bruto = models.DecimalField(max_digits=20, decimal_places=2)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Acao(models.Model):
    id_acao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)

class Cotacao(models.Model):
    id_cotacao = models.AutoField(primary_key=True)
    id_acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    data_cotacao = models.DateField()
    valor_cotacao = models.DecimalField(max_digits=20, decimal_places=2)

class Dividendo(models.Model):
    id_dividendo = models.AutoField(primary_key=True)
    id_acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    data_dividendo = models.DateField()
    valor_dividendo = models.DecimalField(max_digits=20, decimal_places=2)
    quantidade = models.IntegerField()

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    id_carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    data_compra = models.DateField()
    quantidade = models.IntegerField()
    valor_compra = models.DecimalField(max_digits=20, decimal_places=2)

class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True)
    id_acao = models.ForeignKey(Acao, on_delete=models.CASCADE)
    id_carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    data_venda = models.DateField()
    quantidade = models.IntegerField()
    valor_venda = models.DecimalField(max_digits=20, decimal_places=2)