from django.db import models
from django.contrib.auth.models import User

# 1. Venue Model
class Venue(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

# 2. Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()
    allocated_budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def available_seats(self):
        confirmed_count = self.booking_set.filter(status='CONFIRMED').count()
        return self.total_seats - confirmed_count

    def __str__(self):
        return self.title

# 3. Booking & Waiting List
class Booking(models.Model):
    STATUS_CHOICES = (
        ('CONFIRMED', 'Confirmed'),
        ('WAITING', 'Waiting List'),
        ('CANCELLED', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CONFIRMED')

    class Meta:
        ordering = ['booking_time']

# 4. Expense Tracking
class Expense(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# 5. Feedback System
class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)