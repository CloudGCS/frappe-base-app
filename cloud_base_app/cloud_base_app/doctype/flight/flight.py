# Copyright (c) 2024, CloudGCS and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Flight(Document):
    def validate(self):
        start = self.takeoff_time
        end = self.landing_time

        if start>=end:
            frappe.throw(_('Take-off Time has to be earlier than Landing Time'))

        # Calculate difference in seconds
        diff_seconds = frappe.utils.time_diff_in_seconds(end, start)

        # Convert seconds to hours
        hours = diff_seconds / 3600.0

        # Update the document or perform further actions
        self.flight_hours = hours
