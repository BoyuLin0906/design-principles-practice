class TicketActions:
    def close(self, title: str) -> None:
        print(f"Closed ticket: {title}")

    def escalate(self, title: str) -> None:
        print(f"Escalated unassigned ticket: {title}")

    def ping_agent(self, agent: str, title: str) -> None:
        print(f"Pinged {agent} about: {title}")

    def skip(self, title: str) -> None:
        print(f"No action needed for: {title}")


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

    def follow_up(self, actions: TicketActions) -> None:
        if self.status == "resolved":
            actions.close(self.title)
            return

        if self.assigned_agent is None:
            actions.escalate(self.title)
            return

        if self.days_since_update > 3:
            actions.ping_agent(self.assigned_agent, self.title)
            return

        actions.skip(self.title)


if __name__ == "__main__":
    ticket = SupportTicket(
        title="Customer cannot reset password",
        status="open",
        days_since_update=5,
        assigned_agent="Mia",
    )
    actions = TicketActions()
    ticket.follow_up(actions)
