from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, RegexValidator
from django.db import IntegrityError, models
from django.utils.translation import gettext_lazy as _

from community.models import Guest, Staff
from general_app.validators import image_max_size


class Destination(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(
        upload_to="segment/images", validators=[image_max_size], null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Branch(models.Model):
    ACTIVE = "Active"
    DRAFT = "Draft"
    COMING_SOON = "Coming Soon"
    BRANCH_STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (DRAFT, "Draft"),
        (COMING_SOON, "Coming Soon"),
    ]

    name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255, null=True, blank=True)
    destination = models.ForeignKey(
        Destination, on_delete=models.PROTECT, related_name="branches"
    )
    initial = models.CharField(max_length=7)
    address = models.CharField(max_length=255)
    status = models.CharField(
        max_length=15, choices=BRANCH_STATUS_CHOICES, default=COMING_SOON
    )
    logo = models.ImageField(upload_to="segment/images", validators=[image_max_size])
    overview = models.TextField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=14)
    mobile = models.CharField(max_length=14)
    location_iframe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class BranchSlider(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="sliders")
    type = models.CharField(
        max_length=15,
        choices=[
            ("Single Video", "Single Video"),
            ("Static Sliders", "Static Sliders"),
        ],
    )
    featured_image = models.ImageField(
        upload_to="segment/images", validators=[image_max_size]
    )
    # video slider
    video_slider_title = models.CharField(max_length=255, null=True, blank=True)
    video_slider_subtitle = models.CharField(max_length=255, null=True, blank=True)
    video_slider_button_one_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    video_slider_button_one_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    video_slider_button_two_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    video_slider_button_two_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    video_slider_youtube_link = models.CharField(max_length=255, null=True, blank=True)
    # static slider one
    static_slider_one_title = models.CharField(max_length=255, null=True, blank=True)
    static_slider_one_subtitle = models.CharField(max_length=255, null=True, blank=True)
    static_slider_one_button_one_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_one_button_one_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_one_button_two_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_one_button_two_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_one_image_link = models.ImageField(
        upload_to="segment/images", null=True, blank=True
    )
    # static slider two
    static_slider_two_title = models.CharField(max_length=255, null=True, blank=True)
    static_slider_two_subtitle = models.CharField(max_length=255, null=True, blank=True)
    static_slider_two_button_one_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_two_button_one_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_two_button_two_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_two_button_two_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_two_image_link = models.ImageField(
        upload_to="segment/images", null=True, blank=True
    )
    # static slider three
    static_slider_three_title = models.CharField(max_length=255, null=True, blank=True)
    static_slider_three_subtitle = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_three_button_one_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_three_button_one_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_three_button_two_title = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_three_button_two_link = models.CharField(
        max_length=255, null=True, blank=True
    )
    static_slider_three_image_link = models.ImageField(
        upload_to="segment/images", null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class BranchStaff(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("branch", "staff")

    def __str__(self):
        return f"{self.staff.name} at {self.branch.name} as {self.staff.role}"


class RoomCategory(models.Model):
    ACTIVE = "Active"
    OUT_OF_ORDER = "Out Of Order"
    ROOM_STATUS_CHOICES = [(ACTIVE, "Active"), (OUT_OF_ORDER, "Out Of Order")]

    room_name = models.CharField(max_length=50)
    status = models.CharField(
        max_length=15, choices=ROOM_STATUS_CHOICES, default=OUT_OF_ORDER
    )
    featured_image = models.ImageField(upload_to="segment/images")
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    overview = models.TextField()
    panorama = models.ImageField(upload_to="segment/images")
    adults = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    children = models.PositiveSmallIntegerField()
    regular_price = models.DecimalField(max_digits=9, decimal_places=2)
    discount_in_percentage = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["room_name", "branch"]

    def __str__(self) -> str:
        return f"{self.room_name}-{self.branch.name}"


class Gallery(models.Model):
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="segment/images")


class Amenities(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class RoomAmenities(models.Model):
    room_category = models.ForeignKey(
        RoomCategory, on_delete=models.CASCADE, related_name="room_amenities_set"
    )
    amenity = models.ForeignKey(Amenities, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["room_category", "amenity"]


class Room(models.Model):
    ACTIVE = "Active"
    OUT_OF_ORDER = "Out Of Order"

    ROOM_STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (OUT_OF_ORDER, "Out Of Order"),
    ]

    room_number = models.CharField(max_length=15)
    room_category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, choices=ROOM_STATUS_CHOICES, default=ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Right now a category of a branch will not have same room number twice.
    # But this is not enough.Eventually we need to enforce a unique constraint so that no branch end up with same room number twice.
    class Meta:
        unique_together = ["room_number", "room_category"]

    def __str__(self) -> str:
        return f"{self.room_number}-{self.room_category.room_name}-{self.room_category.branch.name}"


class Booking(models.Model):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    CHECKED_IN = "Checked In"
    CHECKED_OUT = "Checked Out"
    BOOKING_STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (CANCELLED, "Cancelled"),
        (CHECKED_IN, "Checked In"),
        (CHECKED_OUT, "Checked Out"),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=14)
    guest = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=15, choices=BOOKING_STATUS_CHOICES, default=PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    additional_info = models.TextField(null=True, blank=True)
    placed_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if self.check_out <= self.check_in:
            raise ValidationError(
                {"check_out": _("Check-out date must be later than check-in date.")}
            )

    def __str__(self):
        return f"Booking for {self.full_name} from {self.check_in} to {self.check_out}"


# We're saving rack rate and discount in percentage when the booking is placed.
class BookingItem(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    room_category = models.ForeignKey(
        RoomCategory, on_delete=models.SET_NULL, null=True, blank=True
    )
    assigned_room = models.ForeignKey(
        Room, on_delete=models.SET_NULL, null=True, blank=True
    )
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["booking", "assigned_room"]

    def __str__(self):
        return f"{self.booking.full_name} booked room number {self.assigned_room.room_number}"


# we can easily subtotal,due from these fields
class Billing(models.Model):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"
    PARTIAL = "Partial"
    PAYMENT_STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (PARTIAL, "Partial"),
        (CANCELLED, "Cancelled"),
    ]
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, unique=True)
    payment_status = models.CharField(
        max_length=15, choices=PAYMENT_STATUS_CHOICES, default=PENDING
    )
    total = models.DecimalField(
        max_digits=9, decimal_places=2, validators=[MinValueValidator(1)]
    )
    discount = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    paid = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billing for booking {self.booking.full_name}"

    @property
    def total_due(self):
        return self.total - self.discount - self.paid

    def clean(self):
        super().clean()
        if self.discount > self.total:
            raise ValidationError(
                {"discount": _("Discount cannot be greater than total.")}
            )
        if self.paid > self.total - self.discount:
            raise ValidationError(
                {"paid": _("Paid amount cannot be greater than the charge.")}
            )
