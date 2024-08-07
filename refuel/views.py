from rest_framework.viewsets import ModelViewSet

from general_app.format_response import CustomResponseMixin

from .models import Gym, GymMembership, Reservation, Restaurant
from .paginations import CustomPagination
from .serializers import (
    GymMembershipSerializer,
    GymSerializer,
    ReservationSerializer,
    RestaurantSerializer,
)

# Create your views here.


class RestaurantViewSet(CustomResponseMixin, ModelViewSet):
    http_method_names = ["get"]

    def get_queryset(self):
        branch_id = self.request.query_params.get("branch_id")
        queryset = (
            Restaurant.objects.filter(status="Active")
            .select_related("branch")
            .prefetch_related("cuisines__cuisine", "gallery_set")
            .order_by("-discount_in_percentage")
        )

        if branch_id is not None:
            queryset = queryset.filter(branch_id=branch_id)

        return queryset

    serializer_class = RestaurantSerializer
    pagination_class = CustomPagination
    list_message = "All the restaurants are fetched successfully"
    retrieve_message = "The restaurant is fetched successfully"
    retrieve_error_message = "There is no restaurant with this id"


class ReservationViewSet(CustomResponseMixin, ModelViewSet):
    http_method_names = ["post"]
    queryset = Reservation.objects.all().select_related("restaurant")
    serializer_class = ReservationSerializer
    create_message = "We have received your reservation request. You will get a call from our staff very soon."


class GymViewSet(CustomResponseMixin, ModelViewSet):
    http_method_names = ["get"]

    def get_queryset(self):
        branch_id = self.request.query_params.get("branch_id")
        queryset = (
            Gym.objects.filter(status="Active")
            .select_related("branch")
            .prefetch_related("gallery", "gender_allowance__gender")
            .order_by("-discount_in_percentage")
        )

        if branch_id is not None:
            queryset = queryset.filter(branch_id=branch_id)

        return queryset

    serializer_class = GymSerializer
    list_message = "All the gyms are fetched successfully"
    retrieve_message = "The gym is fetched successfully"
    retrieve_error_message = "There is no gym listed with this id"
    pagination_class = CustomPagination


class GymMembershipViewSet(CustomResponseMixin, ModelViewSet):
    http_method_names = ["post"]
    queryset = GymMembership.objects.all().select_related("gym")
    serializer_class = GymMembershipSerializer

    def get_serializer_context(self):
        return {"gym_id": self.kwargs["gym_pk"]}

    create_message = "We have received your membership request. You will get a call from our staff very soon."
