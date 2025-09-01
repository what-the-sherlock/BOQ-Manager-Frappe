BOQ Manager:
This is a custom Frappe app built to manage Bills of Quantities (BOQ) and streamline the flow from customer requirements all the way to project execution.

End-to-End Flow :-

1. Bill of Quantities and BOQ Items Creation

- Users can create a Bill of Quantities document (Bill of Quantities Doctype), contains customer, items, and cost details.
- on_update hook to automatically calculate and update the total_amount

2. Quotation Linking

- From a BOQ, a Quotation can be created/linked.
- Added a button "Create Quotation", seen only when status = "Submitted". A common link field is boq_reference.
- After creating quotation, status changes to "Quoted" 

3. Sales Order Generation

- Once a quotation is approved, a Sales Order can be generated and linked back to the BOQ.
- after_insert  automatically copy the value of the boq_reference from the Quotation to the new Sales Order.

4. Project Creation

- A Project can be initiated and tied to the Sales Order.
- It is created using button "Create Project", usable when status = "Quoted"

5. Custom Report

- Shows a unified view of entire flow
