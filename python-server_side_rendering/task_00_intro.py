def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees,
                      list) or any(not isinstance(x, dict) for x in attendees):
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):

        invitation_text = template

        for field in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(field, "N/A")
            if value is None:
                value = "N/A"
            invitation_text = invitation_text.replace(f"{{{field}}}", value)

        file_name = f"output_{index}.txt"
        try:
            with open(file_name, "w") as file:
                file.write(invitation_text)
        except Exception as e:
            print(f"Error writing {file_name}: {e}")
