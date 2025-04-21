from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    ano_lancamento = models.PositiveSmallIntegerField()
    imagem = models.ImageField(upload_to='filmes/')
    diretor = models.CharField(max_length=255, default='')
    generos = models.CharField(max_length=255, default='')
    duracao = models.DurationField(
        help_text="Duration in HH:MM:SS format",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-ano_lancamento']
