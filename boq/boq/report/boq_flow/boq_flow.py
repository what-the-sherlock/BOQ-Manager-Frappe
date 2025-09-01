# Copyright (c) 2025, boq and contributors
# For license information, please see license.txt

# import frappe

import frappe

def execute(filters=None):
    columns = [
        {"label": "Title", "fieldname": "title", "fieldtype": "Data", "width": 180},
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Link", "options": "Customer", "width": 180},
        {"label": "BOQ Date", "fieldname": "boq_date", "fieldtype": "Date", "width": 120},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 120},
        {"label": "Total Amount", "fieldname": "total_amount", "fieldtype": "Currency", "width": 150},
    ]

    data = frappe.db.sql("""
        SELECT
            boq.title,
            boq.customer,
            boq.boq_date,
            boq.status,
            boq.total_amount
        FROM `tabBill of Quantities` boq
    """, as_dict=True)

    return columns, data


