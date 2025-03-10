from typing import Any, Protocol, List


class DriverInterface(Protocol):
    """Interface defining regular Selenium WebDriver methods for better IDE autocompletion."""

    __slots__ = ()

    def get_url(self) -> str:
        """Get the current URL."""
        ...

    def get_title(self) -> str:
        """Get the title of the current page."""
        ...

    def execute_script(self, script: str, *args) -> Any:
        """Execute JavaScript in the current window/frame."""
        ...

    def switch_to_frame(self, frame_reference: Any) -> None:
        """Switch to the specified frame."""
        ...

    def switch_to_default_content(self) -> None:
        """Switch back to the default content (the main frame)."""
        ...

    def switch_to_window(self, window_handle: str) -> None:
        """Switch to the specified window."""
        ...

    def get_window_handles(self) -> List[str]:
        """Get all window handles."""
        ...

    def save_cookies(self, name: str = "cookies.txt") -> None:
        """Save browser cookies to file."""
        ...

    def load_cookies(self, name: str = "cookies.txt") -> None:
        """Load cookies from file into browser."""
        ...
