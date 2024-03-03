from django.db import models
from django.utils import timezone

class User(models.Model):
	login = models.CharField("Логин", max_length=100, unique=True)
	password = models.CharField("Пароль", max_length=100, unique=True)
	email = models.EmailField("Почта", unique=True)
	join_date = models.DateField("Дата", auto_now_add=True)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "Пользователь"

class Genre(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
			return self.name
	
	class Meta:
		verbose_name = "Жанр"

class Anime(models.Model):
	name = models.CharField("Название", max_length=100)
	description = models.TextField("Описание")
	release_date = models.DateField("Дата")
	rating = models.DecimalField("Рейтинг", default=0, max_digits=3, decimal_places=2)
	cover_image = models.ImageField("Обложка", null=True, blank=True)
	genres = models.ManyToManyField(Genre)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "Аниме"

class Rating(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	series = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='series_rating')
	score = models.IntegerField()
	session = models.CharField(max_length=40, null=True, blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		ratings = Rating.objects.filter(series=self.series)
		total = sum(r.score for r in ratings)
		self.series.rating = total / ratings.count()
		self.series.save()

	def __str__(self):
		return f'{self.score} - {self.series}'

	class Meta:
		verbose_name = "Рейтинг"

class Episode(models.Model):
	series = models.ForeignKey(Anime, related_name='episodes', on_delete=models.CASCADE)
	title = models.CharField("Название", max_length=100)
	video = models.FileField("Загрузить")

	def save(self, *args, **kwargs):
		if not self.id:
				max_number = Episode.objects.filter(series=self.series).count()
				self.number = max_number + 1
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = "Эпизоды"

class Comments(models.Model):
	user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
	anime = models.ForeignKey(Anime, related_name='comments', on_delete=models.CASCADE)
	comment_text = models.TextField("Комментарий")
	name = models.CharField(max_length=200, null=True, blank=True)
	session = models.CharField(max_length=40, null=True, blank=True)
	post_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'Comment by {self.user.username} on {self.episode.title}'

	class Meta:
		verbose_name = "Комментарии"