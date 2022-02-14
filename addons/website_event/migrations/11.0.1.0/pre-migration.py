# Copyright 2019 Eficent <http://www.eficent.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

_field_renames = [
    ('event.event', 'event_event', 'show_menu', 'website_menu'),
]


@openupgrade.migrate()
def migrate(env, version):
    if not openupgrade.column_exists(env.cr, "event_event", "show_menu"):
        openupgrade.rename_fields(env, _field_renames)
