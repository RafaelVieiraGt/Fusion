import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path( _instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criacao', auto_now_add=True)
    modificado = models.DateField('Atualizacao', auto_now=True)
    ativo = models.BooleanField('ativo', default=True)


    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('servico',max_length=100)
    descricao = models.TextField('descricao', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico



class Cargo(Base):
    cargo = models.CharField('cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo



class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('facebook', max_length=100, default='#')
    twitter = models.CharField('twitter', max_length=100, default='#')
    instagram = models.CharField('instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome



class Features(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'foguete'),
        ('lni-laptop-phone', 'notebook'),
        ('lni-cog', 'engrenagem'),
        ('lni-leaf', 'leaf'),
        ('lni-layers', 'layer'),
        ('lni-leaf', 'leaf2'),
    )
    titulo = models.CharField('titulo', max_length=100)
    descricao = models.TextField('descricao', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'


    def __str__(self):
        return self.titulo



