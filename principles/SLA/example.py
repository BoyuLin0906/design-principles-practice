class WeeklySummaryPublisher:
    def publish_weekly_summary(self, team_name: str, tasks: list[dict[str, str]]) -> None:
        completed_tasks = self.completed_tasks(tasks)
        title = self.summary_title(team_name)
        body = self.summary_body(title, completed_tasks)
        self.deliver(body)

    def completed_tasks(self, tasks: list[dict[str, str]]) -> list[dict[str, str]]:
        return [task for task in tasks if task["status"] == "done"]

    def summary_title(self, team_name: str) -> str:
        return f"{team_name} Weekly Summary"

    def summary_body(self, title: str, tasks: list[dict[str, str]]) -> str:
        lines = [title, "=" * len(title), ""]

        if not tasks:
            lines.append("No completed tasks this week.")
        else:
            lines.extend(self.task_lines(tasks))

        return "\n".join(lines)

    def task_lines(self, tasks: list[dict[str, str]]) -> list[str]:
        return [self.task_line(task) for task in tasks]

    def task_line(self, task: dict[str, str]) -> str:
        owner = task["owner"].strip().title()
        summary = task["summary"].strip()
        return f"- {summary} (owner: {owner})"

    def deliver(self, message: str) -> None:
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
