output "name_prefix" {
  description = "Prefix for all resource names."
  value       = local.name_prefix
}

output "splunk_config" {
  description = "Splunk configuration."
  value = tomap({
    "index"         = "emea-tech"
    "source_prefix" = "/mp/${local.app_id}"
    "url"           = "https://http-inputs-nike.splunkcloud.com"
  })
}

output "tags" {
  description = "Tags to apply to every resource that supports them."
  value = tomap({
    "AppName"               = "Order Appointment Scheduler",
    "CostCenter"            = "116332",
    "nike-application"      = local.app_id
    "nike-department"       = "Nike Technology"
    "nike-distributionlist" = "Lst-GT.EMEA.MSCT.MPOF.Switzers@Nike.com"
    "nike-domain"           = "MSCT"
    "nike-environment"      = var.environment,
    "nike-owner"            = "serdar.tas@nike.com"
    "nike-org-geo"          = "EMEA"
    "nike-requestor"        = "Lst-GT.EMEA.MSCT.MPOF.Switzers@Nike.com"
    "nike-techsolution"     = "Order Appointment Scheduling tool"
  })
}