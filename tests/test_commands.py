def test():
    from felix_django.management.commands.dev_admin_user import Command

    assert Command
    from felix_django.management.commands.wait_for_db import Command

    assert Command
