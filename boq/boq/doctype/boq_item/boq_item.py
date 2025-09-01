# Copyright (c) 2025, boq and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class BOQItem(Document):
    pass

def update_parent_total(doc, method=None):
    """Update parent BOQ total when a child row changes"""
    if doc.parent and doc.parenttype == "Bill of Quantities":
        parent_doc = frappe.get_doc("Bill of Quantities", doc.parent)
        parent_doc.run_method("update_total_amount")

