from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("branch", views.branch, name="branch"),
    path("add-branch", views.crud_branch, name="crud_branch"),
    path("edit-branch/<int:id>", views.edit_branch, name="edit_branch"),
    path("booking", views.booking, name="booking"),
    path("add-booking", views.crud_booking, name="crud_booking"),
    path("rooms", views.rooms, name="rooms"),
    path("add-room", views.crud_room, name="crud_rooms"),
    path("room-categories", views.room_categories, name="room_categories"),
    path(
        "add-room-categories", views.crud_room_categories, name="crud_room_categories"
    ),
    path("guests", views.guests, name="guests"),
    path("add-guests", views.crud_guests, name="crud_guests"),
    path("expected-guests", views.expected_guests, name="expected_guests"),
    path("departing-guests", views.departing_guests, name="departing_guests"),
    path("inhouse-guests", views.inhouse_guests, name="inhouse_guests"),
    path("restaurants", views.restaurants, name="restaurants"),
    path("add-restaurants", views.crud_restaurants, name="crud_restaurants"),
    path("restaurant-booking", views.restaurant_booking, name="restaurant_booking"),
    path(
        "add-restaurant-booking",
        views.crud_restaurant_booking,
        name="crud_restaurant_booking",
    ),
    path("gym", views.gym, name="gym"),
    path("add-gym", views.crud_gym, name="crud_gym"),
    path("gym-members", views.gym_members, name="gym_members"),
    path("add-gym-members", views.crud_gym_members, name="crud_gym_members"),
    path(
        "gym-membership-request",
        views.gym_membership_request,
        name="gym_membership_request",
    ),
    path("users", views.sys_users, name="users"),
    path("add-user", views.crud_sys_users, name="crud_users"),
    path("login", views.login, name="login"),
    path("sliders", views.cms_sliders, name="cms_sliders"),
    path("edit-slider", views.crud_cms_sliders, name="crud_cms_sliders"),
    path("nearby-attractions", views.cms_attractions, name="cms_attractions"),
    path(
        "edit-nearby-attraction", views.crud_cms_attraction, name="crud_cms_attraction"
    ),
    path("lead-dashboard", views.lead_dashboard, name="lead_dashboard"),
]
