class WeeklySummaryPublisher:
    def publish_weekly_summary(self, team_name: str, tasks: list[dict[str, str]]) -> None:
        ready_tasks = []
        for task in tasks:
            if task["status"] == "done":
                ready_tasks.append(task)

        title = f"{team_name} Weekly Summary"
        body_lines = [title, "=" * len(title), ""]

        if not ready_tasks:
            body_lines.append("No completed tasks this week.")
        else:
            for task in ready_tasks:
                owner = task["owner"].strip().title()
                summary = task["summary"].strip()
                body_lines.append(f"- {summary} (owner: {owner})")

        message = "\n".join(body_lines)
        print("Sending weekly summary...")
        print(message)


if __name__ == "__main__":
    tasks = [
        {"summary": "fix login bug", "owner": "ava", "status": "done"},
        {"summary": "prepare Q3 roadmap", "owner": "liam", "status": "planned"},
        {"summary": "update onboarding guide", "owner": "mia", "status": "done"},
    ]

    publisher = WeeklySummaryPublisher()
    publisher.publish_weekly_summary("Platform Team", tasks)
