# Copyright (c) 2025, boq and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import nowdate
from frappe.model.document import Document
from frappe import _

class BillofQuantities(Document):
    pass

def update_total_amount(doc, method=None):
    """Recalculate total_amount whenever BOQ is updated"""
    total = 0
    for item in doc.items:  
        if item.quantity and item.rate:
            item.amount = item.quantity * item.rate
            total += item.amount

    doc.total_amount = total
    frappe.db.set_value(doc.doctype, doc.name, "total_amount", total)




@frappe.whitelist()
def create_quotation_from_boq(boq_name):
    boq = frappe.get_doc("Bill of Quantities", boq_name)

    if boq.status != "Submitted":
        frappe.throw("BOQ must be marked as Submitted before creating Quotation")

    quotation = frappe.new_doc("Quotation")
    quotation.customer = boq.customer
    quotation.quotation_date = nowdate()
    quotation.boq_reference = boq.name

    for item in boq.items:
        quotation.append("items", {
            "item_code": item.item_code,
            "qty": item.quantity,
            "rate": item.rate,
            "description": item.description
        })

    quotation.insert(ignore_permissions=True)

    boq.db_set("status", "Quoted")

    return quotation.name



def copy_boq_reference_from_quotation(doc, method=None):
    """
    DocEvent: Sales Order.after_insert
    If Sales Order was created from a Quotation, copy quotation.boq_reference -> sales_order.boq_reference
    """
    try:
        quotation_name = doc.get("quotation")
        if not quotation_name:
            return

        try:
            quotation = frappe.get_doc("Quotation", quotation_name)
        except frappe.DoesNotExistError:
            return

        boq_ref = quotation.get("boq_reference")
        if boq_ref:
            doc.db_set("boq_reference", boq_ref)

    except Exception:
        frappe.log_error(frappe.get_traceback(), "copy_boq_reference_from_quotation")


@frappe.whitelist()
def create_project_from_boq(boq_name):
    boq = frappe.get_doc("Bill of Quantities", boq_name)

    sales_order = frappe.db.get_value("Sales Order", 
        {"boq_reference": boq.name, "docstatus": 1}, "name")
    if not sales_order:
        frappe.throw("No Submitted Sales Order linked with this BOQ")

    project = frappe.new_doc("Project")
    project.project_name = boq.title
    project.customer = boq.customer
    project.boq_reference = boq.name
    project.save(ignore_permissions=True)

    for item in boq.items:
        task = frappe.new_doc("Task")
        task.subject = item.item_name
        task.project = project.name
        task.boq_quantity_needed = item.quantity
        task.save(ignore_permissions=True)

    return project.name
