from django import forms
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.mail import send_mass_mail
from django.shortcuts import render


admin.site.unregister(User)


class FollowUpEmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


@admin.register(User)
class CustomerUserAdmin(UserAdmin):
    """Adds a private bulk follow-up email action to the Users admin page."""

    actions = ["send_follow_up_email"]

    @admin.action(description="Send follow-up email to selected users")
    def send_follow_up_email(self, request, queryset):
        if "send" in request.POST:
            form = FollowUpEmailForm(request.POST)
            if form.is_valid():
                recipients = list(
                    queryset.exclude(email="").values_list("email", flat=True)
                )
                if not recipients:
                    self.message_user(
                        request,
                        "None of the selected users has an email address.",
                        level=messages.WARNING,
                    )
                    return None

                subject = form.cleaned_data["subject"]
                body = form.cleaned_data["message"]
                emails = [(subject, body, None, [recipient]) for recipient in recipients]
                send_mass_mail(emails, fail_silently=False)
                self.message_user(
                    request,
                    f"Follow-up email sent to {len(recipients)} user(s).",
                    level=messages.SUCCESS,
                )
                return None
        else:
            form = FollowUpEmailForm()

        return render(
            request,
            "admin/accounts/user/send_follow_up_email.html",
            {
                "form": form,
                "users": queryset,
                "title": "Send follow-up email",
            },
        )
