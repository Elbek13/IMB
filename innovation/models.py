from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Matn")
    image = models.ImageField(upload_to='news_images/', null=True, blank=True, verbose_name="Rasm")
    video = models.FileField(upload_to='news_videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
