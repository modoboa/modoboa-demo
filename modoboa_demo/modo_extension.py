"""Demo extension."""

from django.utils.translation import ugettext_lazy

from modoboa.core.extensions import ModoExtension, exts_pool

from modoboa_admin.factories import DomainFactory, MailboxFactory


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
        domain.add_admin(dadmin)
        MailboxFactory.create(
            address="user", domain=domain, user__username="user@demo.local",
            user__groups=["SimpleUsers"]
        )

exts_pool.register_extension(Demo)

