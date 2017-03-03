"""Demo extension."""

from django.utils.translation import ugettext_lazy

from modoboa.admin.factories import DomainFactory, MailboxFactory
from modoboa.core import models as core_models
from modoboa.core.extensions import ModoExtension, exts_pool


class Demo(ModoExtension):

    """The demo extension."""

    name = "modoboa_demo"
    label = ugettext_lazy("Demo")
    version = "1.0.0"
    description = ugettext_lazy("Demonstration features for Modoboa")

    def load_initial_data(self):
        """Load demo data."""
        domain = DomainFactory.create(name="demo.local")
        dadmin = MailboxFactory.create(
            address="admin", domain=domain, user__username="admin@demo.local",
            user__groups=["DomainAdmins"]
        )
        dadmin.user.set_password("admin")
        dadmin.user.save()
        domain.add_admin(dadmin.user)
        user = MailboxFactory.create(
            address="user", domain=domain, user__username="user@demo.local",
            user__groups=["SimpleUsers"]
        )
        user.user.set_password("user")
        user.user.save()

        # Configure parameters
        lc = core_models.LocalConfig.objects.first()
        lc.parameters.set_value("handle_mailboxes", True, app="admin")
        lc.parameters.set_value("am_pdp_mode", "inet", app="modoboa_amavis")
        lc.parameters.set_value(
            "rrd_rootdir", "/srv/modoboa/rrdfiles", app="modoboa_stats")
        lc.parameters.set_value(
            "storage_dir", "/srv/modoboa/pdfcredentials",
            app="modoboa_pdfcredentials")
        lc.save()

exts_pool.register_extension(Demo)
