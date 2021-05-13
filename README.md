## Task
### For ‘demo.demo’
- [x] - Create model "demo.demo" with fields Customer, Done Date, Salesperson,
State(Planned, Done, Cancelled) and Many2one field for model ‘crm.lead’.
- [x] - Add an auto-filling name like (Demo 01, Demo 02 ...)
- [x] - Add kanban view.
- [x] - Add list view 
- [x] - Add search view
- [x] - Add form view 
- [x] - Add chatter.
- [x] - Add state widget on the form for field State
- [x] - Add filter "My demos" by default.
- [x] - In the search by name add searching by lead and by customer
- [x] - Create list view with fields Name, Lead, Customer.

### For Lead(crm.lead)
- [x] - Add field One2many demo_ids and compute field demo_count.
- [x] - Create button "New demo". After pushing this button should be open demo form and
auto fill fields customer, Salesperson and lead from current lead.
- [x] - Add button Demo in button box with field demo_count. After pushing this button should be open list related demos.

