# Copyright 2018 Eficent <http://www.eficent.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

def delete_website_menus(cr):
    openupgrade.logged_query(
        cr,
        """
        DELETE FROM website_menu
        where name = 'Help'
        """,
    )

@openupgrade.migrate(use_env=True)
def migrate(env, version):
    cr = env.cr
    delete_website_menus(cr)
