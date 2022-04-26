""" Encode any known changes to the database here
to help the matching process
"""

renamed_modules = {
    # Odoo
    "base_action_rule": "base_automation",
    "crm_project_issue": "crm_project",
    "stock_picking_wave": "stock_picking_batch",
    "website_issue": "website_form_project",
    "website_rating_project_issue": "website_rating_project",
    # enterprise
    "account_contract_dashboard": "sale_subscription_dashboard",
    "grid": "web_grid",
    "sale_contract": "sale_subscription",
    "sale_contract_asset": "sale_subscription_asset",
    # OCA/account-invoice-reporting
    "invoice_comment_template": "account_invoice_comment_template",
    # OCA/credit-control
    "partner_financial_risk": "account_financial_risk",
    "partner_payment_return_risk": "account_payment_return_financial_risk",
    "partner_sale_risk": "sale_financial_risk",
    "partner_stock_risk": "stock_financial_risk",
    # OCA/crm
    "crm_sector": "crm_industry",
    # OCA/account-payment
    "account_due_list_aging_comments": "account_due_list_aging_comment",
    # OCA/l10n-netherlands:
    "l10n_nl_intrastat": "l10n_nl_tax_statement_icp",
    # OCA/partner-contact
    "partner_sector": "partner_industry_secondary",
    "partner_street_number": "base_address_extended",
    # OCA/product-attribute
    "product_uom": "product_uom_extra_data",  # -> OCA/community-data-files
    # OCA/purchase-workflow
    "purchase_request_to_rfq_order_approved": ("purchase_request_order_approved"),
    # OCA/sale-reporting
    "sale_report_delivered": "sale_report_delivered_subtotal",
    # OCA/server-tools
    "mail_log_message_to_process": "fetchmail_incoming_log",
    # OCA/stock-logistics-reporting
    "stock_valued_picking_report": "stock_picking_report_valued",
    # OCA/stock-logistics-workflow
    "stock_pack_operation_quick_lot": "stock_move_quick_lot",
    # OCA/hr
    "hr_public_holidays": "hr_holidays_public",
    # OCA/vertical-association
    "membership_prorrate": "membership_prorate",
    "membership_prorrate_variable_period": ("membership_prorate_variable_period"),
    # OCA/web
    "web_advanced_search_x2x": "web_advanced_search",
    # homepro_custom
    "ursa_stock_picking_wave": "ursa_stock_picking_batch",
    "osi_merge_task_do": "homepro_hr_department",
    "billy_pdf_reports": "homepro_reports",
    "osi_site_smart_button": "homepro_res_partner_enhance",
}

merged_modules = {
    # Odoo
    "account_tax_cash_basis": "account",
    "portal_gamification": "gamification",
    "portal_sale": "sale",
    "portal_stock": "portal",
    "procurement": "stock",
    "project_issue": "project",
    "project_issue_sheet": "hr_timesheet",
    "report": "base",
    "web_calendar": "web",
    "web_kanban": "web",
    "website_portal": "website",
    "website_portal_sale": "sale_payment",
    "website_project": "project",
    "website_project_issue": "project",
    "website_project_timesheet": "hr_timesheet",
    "test_pylint": "test_lint",
    # enterprise
    "website_contract": "sale_subscription",
    # OCA/account-analytic
    "purchase_procurement_analytic": "procurement_mto_analytic",
    "sale_procurement_analytic": "procurement_mto_analytic",
    # OCA/account-invoice-reporting
    "product_brand_invoice_report": "product_brand",
    # OCA/account-financial-reporting
    # Done here for avoiding problems if updating from a previous version
    # where account_financial_report exists as other kind of module
    "account_financial_report_qweb": "account_financial_report",
    # OCA/account-financial-tools
    "account_group": "account",
    # OCA/bank-payment
    "portal_payment_mode": "account_payment_mode",
    # OCA/crm
    "crm_lead_website": "crm",
    # OCA/hr-timesheet
    "hr_timesheet_sheet_week_start_day": "hr_timesheet_sheet",
    # OCA/l10n-italy:
    "l10n_it_fiscalcode_invoice": "l10n_it_fiscalcode",
    # OCA/l10n-spain:
    "l10n_es_account_group": "l10n_es",
    # OCA/product-variant
    "product_variant_supplierinfo": "product",
    "sale_stock_variant_configurator": "sale_variant_configurator",
    # OCA/project
    "project_issue_timesheet_time_control": "project_timesheet_time_control",
    # OCA/purchase-reporting
    "purchase_reporting_weight": "product_weight_through_uom",
    # OCA/purchase-workflow
    "product_by_supplier": "purchase",
    "purchase_request_procurement": "purchase_request",
    "purchase_request_to_rfq": "purchase_request",
    # OCA/sale-reporting
    "product_brand_sale_report": "product_brand",
    "sale_proforma_report": "sale",
    "sale_reporting_weight": "product_weight_through_uom",
    # OCA/social:
    "mail_activity": "mail",
    "mail_activity_crm": "crm",
    "mail_activity_calendar": "calendar",
    # OCA/stock-logistics-workflow
    "stock_disable_force_availability_button": "stock",
    "stock_picking_transfer_lot_autoassign": "stock_pack_operation_auto_fill",
    # OCA/web
    "web_sheet_full_width": "web_responsive",
    "web_widget_datepicker_options": "web",
    "web_widget_domain_v11": "web",
    # OCA/website
    "website_seo_redirection": "website",
    # OCA/bank-statement-import
    "account_bank_statement_import_camt": "account_bank_statement_import_camt_oca",
    "product_configurator_wizard": "product_configurator",
    # Custom-addons
    "ursa_analytic_department": "homepro_hr_department",
    "analytic_base_department": "homepro_hr_department",
    "project_department": "homepro_hr_department",
    "osi_purchase_analytic": "homepro_hr_department",
    "billy_crm_lead_salesupport": "billy_crm_lead_cms_corner",
    "billy_project_timeline_menu": "web_timeline_osi_user_filter",
    "billy_delivery_order_cancel": "osi_delivery_order_return",
    "ursa_site_cmis": "cmis_enhancements",
    "account_check_report": "homepro_reports",
    "ursa_us_check_layout": "homepro_reports",
    "billy_community_line_view_ext": "ursa_partner_builder",
    "osi_tech_can_install": "homepro_res_partner_enhance",
    "ursa_1099": "homepro_res_partner_enhance",
    "partner_aging_any_date": "homepro_res_partner_enhance",
    # "ursa_project_task_report": "homepro_reports",
    # "ursa_analytic_warehouse": "ursa_branch",
}

renamed_models = {
    "base.action.rule": "base.automation",
    "base.action.rule.lead.test": "base.automation.lead.test",
    "base.action.rule.line.test": "base.automation.line.test",
    "ir.actions.report.xml": "ir.actions.report",
    "stock.pack.operation": "stock.move.line",
    "stock.picking.wave": "stock.picking.batch",
}
