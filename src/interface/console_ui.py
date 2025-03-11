from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.layout import Layout
from rich import print
from rich.markdown import Markdown
from agents.weatherAgent import WeatherAgent

class WeatherConsoleUI:
    def __init__(self):
        self.console = Console()
        self.weather_agent = WeatherAgent()
        self.layout = Layout()

    def display_header(self):
        self.console.print(Panel.fit(
            "[bold blue]Weather Agent Assistant[/bold blue]\n"
            "[italic]Ask me anything about the weather![/italic]",
            border_style="cyan"
        ))

    def display_help(self):
        help_text = """
        **Available Commands:**
        - /help - Show this help message
        - /exit - Exit the application
        
        **Example Questions:**
        - What's the weather like in London?
        - Will it rain tomorrow in New York?
        - What's the temperature in Paris?
        """
        self.console.print(Markdown(help_text))

    def run(self):
        self.display_header()
        self.display_help()

        while True:
            try:
                user_input = Prompt.ask("\n[bold green]Ask your question[/bold green]")
                
                if user_input.lower() == '/exit':
                    self.console.print("[yellow]Goodbye![/yellow]")
                    break
                elif user_input.lower() == '/help':
                    self.display_help()
                    continue

                with self.console.status("[bold blue]Thinking...[/bold blue]"):
                    response = self.weather_agent.process_query(user_input)
                
                self.console.print(Panel(
                    f"[bold white]{response}[/bold white]",
                    border_style="blue"
                ))

            except KeyboardInterrupt:
                self.console.print("\n[yellow]Exiting...[/yellow]")
                break
            except Exception as e:
                self.console.print(f"[red]Error: {str(e)}[/red]")

if __name__ == "__main__":
    ui = WeatherConsoleUI()
    ui.run()