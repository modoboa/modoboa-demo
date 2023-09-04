"""Demo handlers."""

from django.urls import reverse
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.translation import gettext as _


from modoboa.core import signals as core_signals
from modoboa.lib.web_utils import static_url


@receiver(core_signals.extra_user_menu_entries)
def menu(sender, location, user, **kwargs):
    if location != "top_menu_middle":
        return []
    if not hasattr(user, "mailbox"):
        return []
    return [
        {"name": "demo",
         "label": _("Test messages"),
         "img": static_url("pics/demo.png"),
         "class": "topdropdown",
         "menu": [
             {"name": "sendvirus",
              "label":  _("Send virus"),
              "url": reverse("modoboa_demo:virus_send")},
             {"name": "sendspam",
              "label":  _("Send spam"),
              "url": reverse("modoboa_demo:spam_send")}
         ]
         }
    ]


@receiver(core_signals.get_announcements)
def announcement(sender, location, **kwargs):
    if location == "loginpage":
        txt = render_to_string("modoboa_demo/login_announcement.html")
        return txt
    return ""


@receiver(core_signals.allow_password_change)
def password_change(sender, user, **kwargs):
    return [user.id == 1]


@receiver(core_signals.extra_static_content)
def get_static_content(sender, caller, st_type, user, **kwargs):
    if caller != 'top' or st_type != 'js' or not hasattr(user, "mailbox"):
        return ""

    return """<script type="text/javascript">
$(document).ready(function() {
    $(document).on('click', 'a[name=sendspam]', simple_ajax_request);
    $(document).on('click', 'a[name=sendvirus]', simple_ajax_request);
});
</script>"""
