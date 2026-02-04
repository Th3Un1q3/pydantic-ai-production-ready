import logfire
from pydantic_ai_shared.resolver import resolve_model

from course_navigator.agent import create_agent


def main() -> None:
    # Configure Logfire for development UI
    # Use 'if-token-present' to avoid crashing if not authenticated
    logfire.configure(send_to_logfire="if-token-present")
    logfire.instrument_pydantic_ai()

    # Resolve the model using our shared resolver
    try:
        model = resolve_model()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return

    # Create the agent
    agent = create_agent(model)

    print(f"Agent initialized with model: {model}")
    print("Running agent synchronously...")

    # Run synchronously
    try:
        # Simple "Hello" to verify connectivity
        result = agent.run_sync("Hello! Who are you?")
        print(f"Response: {result.output}")
        print(result.usage())
    except Exception as e:
        print(f"Error running agent: {e}")


if __name__ == "__main__":  # pragma: no cover
    main()
