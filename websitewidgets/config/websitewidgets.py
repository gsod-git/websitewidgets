from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Widgets"),
			"items": [
				{
					"type": "doctype",
					"name": "Widgets"
				},				
				{
					"type": "doctype",
					"name": "Widget Placeholder"
				}
				# {
				# 	"type": "doctype",
				# 	"name": "Screen"
				# }
			]
		}
		# {
		# 	"label": _("Bug & Error Tracking "),
		# 	"items": [
		# 		{
		# 			"type": "doctype",
		# 			"name": "Bug Sheet",
		# 			"label": "Bug Sheets"
		# 		},			
		# 		{
		# 			"type": "doctype",
		# 			"name": "Test Case"
		# 		},
		#  	# 	{
		# 		# 	"type": "page",
		# 		# 	"name": "pms",
		# 		# 	"label": _("PMS"),
		# 		# 	"description": _("PMS")
		# 		# },
		# 	]
		# },
		# {
		# 	"label": _("Setup"),
		# 	"items": [
		# 		{
		# 			"type": "doctype",
		# 			"name": "Field Type"
		# 		},			
		# 		{
		# 			"type": "doctype",
		# 			"name": "Validation"
		# 		}
		# 	]
		# },		
	] 