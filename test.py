


context =  {
    "teamName": "sterling",
    "actionName": "Auto-create a Transposit activity",
    "integratorResponse": {
      "name": "[Site24x7] education-v2-prod-api status is: TROUBLE",
      "externalUrl": "https://sterlingcheck.app.opsgenie.com/alert/detail/6552a02b-ff34-4e65-a1cc-83eb3fccdcef-1625246953480",
      "metadata": {
        "app_name": "Sterling Opsgenie Data Parser",
        "match_alert": "false",
        "tags": "sterling,webhook,alert_update",
        "parsed_body": {
          "action": "Create",
          "alert": {
            "alertId": "6552a02b-ff34-4e65-a1cc-83eb3fccdcef-1625246953480",
            "message": "[Site24x7] education-v2-prod-api status is: TROUBLE",
            "tags": [
              "st:sla:100",
              "st:environment:prod",
              "st:application:education",
              "account_site24x7:AWS PROD",
              "st:owner:Dipesh Billimoria",
              "st:sev:2",
              "Name:education-v2-prod-api"
            ],
            "tinyId": "45173",
            "entity": "",
            "alias": "-",
            "createdAt": 1625246953480,
            "updatedAt": "1625246954020000000",
            "username": "Site24x7",
            "description": "Incident Reason : Health Percentage is below 100 %\nIncident Time : July 2, 2021 1:28 PM EDT\nFailed Locations :",
            "team": "team-fulfillment-verification-deltaapi",
            "responders": [
              {
                "id": "83611818-c286-4f3f-8467-86036d298f56",
                "type": "team",
                "name": "team-fulfillment-verification-deltaapi"
              }
            ],
            "teams": [
              "83611818-c286-4f3f-8467-86036d298f56"
            ],
            "actions": [],
            "addedTags": "st:sla:100,st:environment:prod,st:application:education,account_site24x7:AWS PROD,st:owner:Dipesh Billimoria,st:sev:2,Name:education-v2-prod-api",
            "details": {
              "Monitor Dashboard Link": "https://www.site24x7.com/app/client#/home/monitors/79963000032090390/Summary",
              "Monitor ID": "79963000032090390",
              "Monitor Type": "R53_HEALTHCHECK",
              "Monitor Url": "-",
              "Poll Frequency": "1"
            },
            "priority": "P3",
            "source": "Site24x7"
          },
          "source": {
            "name": "",
            "type": "Site24x7"
          },
          "integrationName": "Transposit",
          "integrationId": "700d52ac-2adc-4371-a182-02b81a72e9d6",
          "integrationType": "Webhook"
        }
      }
    },
    "triggerId": 258,
    "parameters": {},
    "runbookRunId": "601bdd9b-78f2-4fdf-9d84-b49fbe366b09",
    "runbookTriggeringEventId": "9d1a4b97-edd4-4ea5-8e66-b5c37f99cee5"
  }


new_incident_name  = context["integratorResponse"]["name"]
incident_url  = context["integratorResponse"]["externalUrl"]
alert_idi  = context["integratorResponse"]["metadata"]["parsed_body"]["alert"]["alertId"]
alert_message  = context["integratorResponse"]["metadata"]["parsed_body"]["alert"]["message"]
alert_description  = context["integratorResponse"]["metadata"]["parsed_body"]["alert"]["description"]



