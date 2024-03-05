class InitialApplication:
    def __init__(self):
        self.running = True

    def start(self):
        print("Welcome to the SolarCode Application!")
        print("Choose option:")
        print("1 - help")
        print("2 - exit")

        while self.running:
            command = input(">> ")
            self.handle_command(command)

    def handle_command(self, command):
        if command == "help":
            self.print_help()
        elif command == "exit":
            self.exit_application()
        else:
            print("Unknown command. Type 'help' or 'exit'.")

    def print_help(self):
        print("Available commands:")
        print("help - Show available commands")
        print("exit - Exit the application")

    def exit_application(self):
        print("Exiting the application. Goodbye!")
        self.running = False

if __name__ == "__main__":
    app = InitialApplication()
    app.start()
