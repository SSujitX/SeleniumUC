from typing import Optional, Any, Union, Protocol, List


class DriverWrapper:
    """Wrapper for SeleniumBase's regular driver operations."""

    __slots__ = ("_sb",)

    def __init__(self, sb):
        self._sb = sb

    def get_url(self) -> str:
        """Get the current URL."""
        return self._sb.get_current_url()

    def get_title(self) -> str:
        """Get the title of the current page."""
        return self._sb.get_title()

    def execute_script(self, script: str, *args) -> Any:
        """Execute JavaScript in the current window/frame."""
        return self._sb.execute_script(script, *args)

    def switch_to_frame(self, frame_reference: Any) -> None:
        """Switch to the specified frame."""
        self._sb.switch_to_frame(frame_reference)

    def switch_to_default_content(self) -> None:
        """Switch back to the default content (the main frame)."""
        self._sb.switch_to_default_content()

    def switch_to_window(self, window_handle: str) -> None:
        """Switch to the specified window."""
        self._sb.switch_to_window(window_handle)

    def get_window_handles(self) -> List[str]:
        """Get all window handles."""
        return self._sb.get_window_handles()

    def screenshot(self, filename: str = "screenshot.png") -> str:
        """Take a screenshot of the current page."""
        return self._sb.save_screenshot(filename)

    def set_window_size(self, width: int, height: int) -> None:
        """Set the window size."""
        self._sb.set_window_size(width, height)

    def maximize_window(self) -> None:
        """Maximize the browser window."""
        self._sb.maximize_window()

    def save_cookies(self, name: str = "cookies.txt") -> None:
        """Save browser cookies to file."""
        self._sb.save_cookies(name)

    def load_cookies(self, name: str = "cookies.txt") -> None:
        """Load cookies from file into browser."""
        self._sb.load_cookies(name)
