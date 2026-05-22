class SupportTicket:
    def __init__(
        self,
        title: str,
        status: str,
        days_since_update: int,
        assigned_agent: str | None,
    ) -> None:
        self.title = title
        self.status = status
        self.days_since_update = days_since_update
        self.assigned_agent = assigned_agent


def follow_up_ticket(ticket: SupportTicket) -> None:
    if ticket.status == "resolved":
        print(f"Closed ticket: {ticket.title}")
        return

    if ticket.assigned_agent is None:
        print(f"Escalated unassigned ticket: {ticket.title}")
        return

    if ticket.days_since_update > 3:
        print(f"Pinged {ticket.assigned_agent} about: {ticket.title}")
        return

    print(f"No action needed for: {ticket.title}")


if __name__ == "__main__":
    ticket = SupportTicket(
        title="Customer cannot reset password",
        status="open",
        days_since_update=5,
        assigned_agent="Mia",
    )
    follow_up_ticket(ticket)
