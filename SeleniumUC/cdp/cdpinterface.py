from typing import Optional, Any, Union, Protocol, List, Callable, Dict, Tuple


class CDPInterface(Protocol):
    """Interface defining CDP methods for better IDE autocompletion."""

    __slots__ = ()

    def sleep(self, seconds: Union[int, float]) -> None:
        """Sleep for the specified number of seconds."""
        ...

    def type(self, selector: str, text: str, timeout: Optional[int] = None) -> None:
        """Type text into an element matching the selector."""
        ...

    def mouse_click(self, selector: str, timeout: Optional[int] = None) -> None:
        """Click on an element matching the selector."""
        ...

    def reload(
        self,
        ignore_cache: Optional[bool] = None,
        script_to_evaluate_on_load: Optional[str] = None,
    ) -> None:
        """Reload the current page."""
        ...

    def refresh(self) -> None:
        """Refresh the current page."""
        ...

    def find_element(
        self, selector: str, best_match: bool = False, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """Find an element matching the selector."""
        ...

    def get(self, url: str) -> None:
        """Navigate to the specified URL."""
        ...

    def open(self, url: str) -> None:
        """Open the specified URL (alias for get)."""
        ...

    def get_event_loop(self) -> Any:
        """Get the event loop for CDP."""
        ...

    def add_handler(self, event: str, handler: Callable) -> None:
        """Add a handler for a CDP event."""
        ...

    def find(
        self, selector: str, best_match: bool = False, timeout: Optional[int] = None
    ) -> Any:
        """Find an element matching the selector (alias for find_element)."""
        ...

    def locator(
        self, selector: str, best_match: bool = False, timeout: Optional[int] = None
    ) -> Any:
        """Get a locator for an element matching the selector."""
        ...

    def find_element_by_text(
        self, text: str, tag_name: Optional[str] = None, timeout: Optional[int] = None
    ) -> Any:
        """Find an element by its text content."""
        ...

    def find_all(self, selector: str, timeout: Optional[int] = None) -> List[Any]:
        """Find all elements matching the selector."""
        ...

    def find_elements_by_text(
        self, text: str, tag_name: Optional[str] = None
    ) -> List[Any]:
        """Find all elements by their text content."""
        ...

    def select(self, selector: str, timeout: Optional[int] = None) -> Any:
        """Select an element matching the selector."""
        ...

    def select_all(self, selector: str, timeout: Optional[int] = None) -> List[Any]:
        """Select all elements matching the selector."""
        ...

    def find_elements(self, selector: str, timeout: Optional[int] = None) -> List[Any]:
        """Find all elements matching the selector."""
        ...

    def find_visible_elements(
        self, selector: str, timeout: Optional[int] = None
    ) -> List[Any]:
        """Find all visible elements matching the selector."""
        ...

    def click_nth_element(self, selector: str, number: int) -> None:
        """Click the nth element matching the selector."""
        ...

    def click_nth_visible_element(self, selector: str, number: int) -> None:
        """Click the nth visible element matching the selector."""
        ...

    def click_link(self, link_text: str) -> None:
        """Click a link with the specified text."""
        ...

    def go_back(self) -> None:
        """Navigate back in browser history."""
        ...

    def go_forward(self) -> None:
        """Navigate forward in browser history."""
        ...

    def get_navigation_history(self) -> Dict:
        """Get the browser's navigation history."""
        ...

    def tile_windows(
        self, windows: Optional[List] = None, max_columns: int = 0
    ) -> None:
        """Tile browser windows."""
        ...

    def get_all_cookies(self, *args, **kwargs) -> List[Dict]:
        """Get all cookies."""
        ...

    def set_all_cookies(self, *args, **kwargs) -> None:
        """Set all cookies."""
        ...

    def save_cookies(self, *args, **kwargs) -> None:
        """Save cookies to file."""
        ...

    def load_cookies(self, *args, **kwargs) -> None:
        """Load cookies from file."""
        ...

    def clear_cookies(self) -> None:
        """Clear all cookies."""
        ...

    def bring_active_window_to_front(self) -> None:
        """Bring the active window to the front."""
        ...

    def bring_to_front(self) -> None:
        """Bring the active window to the front (alias)."""
        ...

    def get_active_element(self) -> Any:
        """Get the active element."""
        ...

    def get_active_element_css(self) -> str:
        """Get the CSS of the active element."""
        ...

    def click(self, selector: str, timeout: Optional[int] = None) -> None:
        """Click an element matching the selector."""
        ...

    def click_active_element(self) -> None:
        """Click the active element."""
        ...

    def click_if_visible(self, selector: str) -> bool:
        """Click an element if it is visible."""
        ...

    def click_visible_elements(self, selector: str, limit: int = 0) -> int:
        """Click all visible elements matching the selector."""
        ...

    def nested_click(self, parent_selector: str, selector: str) -> None:
        """Click a nested element."""
        ...

    def get_nested_element(self, parent_selector: str, selector: str) -> Any:
        """Get a nested element."""
        ...

    def select_option_by_text(self, dropdown_selector: str, option: str) -> None:
        """Select a dropdown option by text."""
        ...

    def flash(
        self, selector: str, duration: int = 1, color: str = "44CC88", pause: int = 0
    ) -> None:
        """Flash an element."""
        ...

    def highlight(self, selector: str) -> None:
        """Highlight an element."""
        ...

    def focus(self, selector: str) -> None:
        """Focus on an element."""
        ...

    def highlight_overlay(self, selector: str) -> None:
        """Highlight an element with an overlay."""
        ...

    def get_parent(self, element: Any) -> Any:
        """Get the parent element."""
        ...

    def remove_element(self, selector: str) -> None:
        """Remove an element from the DOM."""
        ...

    def remove_from_dom(self, selector: str) -> None:
        """Remove an element from the DOM (alias)."""
        ...

    def remove_elements(self, selector: str) -> None:
        """Remove all elements matching the selector from the DOM."""
        ...

    def send_keys(
        self, selector: str, text: str, timeout: Optional[int] = None
    ) -> None:
        """Send keys to an element."""
        ...

    def press_keys(
        self, selector: str, text: str, timeout: Optional[int] = None
    ) -> None:
        """Press keys in an element."""
        ...

    def set_value(
        self, selector: str, text: str, timeout: Optional[int] = None
    ) -> None:
        """Set the value of an element."""
        ...

    def evaluate(self, expression: str) -> Any:
        """Evaluate JavaScript expression."""
        ...

    def js_dumps(self, obj_name: str) -> str:
        """Dump a JavaScript object as string."""
        ...

    def maximize(self) -> None:
        """Maximize the browser window."""
        ...

    def minimize(self) -> None:
        """Minimize the browser window."""
        ...

    def medimize(self) -> None:
        """Set the browser window to a medium size."""
        ...

    def set_window_rect(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> None:
        """Set the browser window rectangle dimensions."""
        ...

    def reset_window_size(self) -> None:
        """Reset the browser window size to the default."""
        ...

    def open_new_window(self, url: Optional[str] = None, switch_to: bool = True) -> Any:
        """Open a new browser window."""
        ...

    def switch_to_window(self, window: Union[str, int]) -> None:
        """Switch to a specific browser window."""
        ...

    def switch_to_newest_window(self) -> None:
        """Switch to the newest browser window."""
        ...

    def open_new_tab(self, url: Optional[str] = None, switch_to: bool = True) -> Any:
        """Open a new browser tab."""
        ...

    def switch_to_tab(self, tab: Union[str, int]) -> None:
        """Switch to a specific browser tab."""
        ...

    def switch_to_newest_tab(self) -> None:
        """Switch to the newest browser tab."""
        ...

    def close_active_tab(self) -> None:
        """Close the currently active tab."""
        ...

    def get_active_tab(self) -> str:
        """Get the handle of the active tab."""
        ...

    def get_tabs(self) -> List[str]:
        """Get all open tab handles."""
        ...

    def get_window(self) -> str:
        """Get the handle of the active window."""
        ...

    def get_text(self, selector: str) -> str:
        """Get the text of an element."""
        ...

    def get_title(self) -> str:
        """Get the title of the current page."""
        ...

    def get_current_url(self) -> str:
        """Get the URL of the current page."""
        ...

    def get_origin(self) -> str:
        """Get the origin of the current page."""
        ...

    def get_page_source(self) -> str:
        """Get the source code of the current page."""
        ...

    def get_user_agent(self) -> str:
        """Get the user agent being used."""
        ...

    def get_cookie_string(self) -> str:
        """Get all cookies as a string."""
        ...

    def get_locale_code(self) -> str:
        """Get the locale code being used."""
        ...

    def get_screen_rect(self) -> Dict[str, int]:
        """Get the screen rectangle dimensions."""
        ...

    def get_window_rect(self) -> Dict[str, int]:
        """Get the window rectangle dimensions."""
        ...

    def get_window_size(self) -> Dict[str, int]:
        """Get the window size."""
        ...

    def get_window_position(self) -> Dict[str, int]:
        """Get the window position."""
        ...

    def get_element_rect(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """Get the rectangle dimensions of an element."""
        ...

    def get_element_size(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """Get the size of an element."""
        ...

    def get_element_position(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """Get the position of an element."""
        ...

    def get_gui_element_rect(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """Get the rectangle dimensions of a GUI element."""
        ...

    def get_gui_element_center(
        self, selector: str, timeout: Optional[int] = None
    ) -> Tuple[int, int]:
        """Get the center coordinates of a GUI element."""
        ...

    def get_document(self) -> Dict[str, Any]:
        """Get the document object."""
        ...

    def get_flattened_document(self) -> Dict[str, Any]:
        """Get the flattened document object."""
        ...

    def get_element_attributes(self, selector: str) -> Dict[str, str]:
        """Get all attributes of an element."""
        ...

    def get_element_attribute(self, selector: str, attribute: str) -> str:
        """Get the value of an element attribute."""
        ...

    def get_element_html(self, selector: str) -> str:
        """Get the HTML of an element."""
        ...

    def set_locale(self, locale: str) -> None:
        """Set the locale code."""
        ...

    def set_attributes(self, selector: str, attribute: str, value: str) -> None:
        """Set attributes on an element."""
        ...

    def gui_press_key(self, key: str) -> None:
        """Press a key using GUI automation."""
        ...

    def gui_press_keys(self, keys: str) -> None:
        """Press multiple keys using GUI automation."""
        ...

    def gui_write(self, text: str) -> None:
        """Write text using GUI automation."""
        ...

    def gui_click_x_y(self, x: int, y: int) -> None:
        """Click at specific coordinates using GUI automation."""
        ...

    def gui_click_element(self, selector: str) -> None:
        """Click an element using GUI automation."""
        ...

    def gui_drag_drop_points(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Drag and drop from one point to another using GUI automation."""
        ...

    def gui_drag_and_drop(self, drag_selector: str, drop_selector: str) -> None:
        """Drag and drop from one element to another using GUI automation."""
        ...

    def gui_hover_x_y(self, x: int, y: int) -> None:
        """Hover at specific coordinates using GUI automation."""
        ...

    def gui_hover_element(self, selector: str) -> None:
        """Hover over an element using GUI automation."""
        ...

    def gui_hover_and_click(self, hover_selector: str, click_selector: str) -> None:
        """Hover over one element and click another using GUI automation."""
        ...

    def internalize_links(self) -> None:
        """Internalize all links on the page to make them open within the current window."""
        ...

    def is_checked(self, selector: str) -> bool:
        """Check if a checkbox or radio button is checked."""
        ...

    def is_selected(self, selector: str) -> bool:
        """Check if an element is selected."""
        ...

    def check_if_unchecked(self, selector: str) -> bool:
        """Check a checkbox or radio button if it is unchecked."""
        ...

    def select_if_unselected(self, selector: str) -> bool:
        """Select an element if it is unselected."""
        ...

    def uncheck_if_checked(self, selector: str) -> bool:
        """Uncheck a checkbox or radio button if it is checked."""
        ...

    def unselect_if_selected(self, selector: str) -> bool:
        """Unselect an element if it is selected."""
        ...

    def is_element_present(self, selector: str) -> bool:
        """Check if an element is present in the DOM."""
        ...

    def is_element_visible(self, selector: str) -> bool:
        """Check if an element is visible."""
        ...

    def is_text_visible(self, text: str, selector: str = "body") -> bool:
        """Check if text is visible on the page."""
        ...

    def is_exact_text_visible(self, text: str, selector: str = "body") -> bool:
        """Check if exact text is visible on the page."""
        ...

    def wait_for_text(
        self, text: str, selector: str = "body", timeout: Optional[int] = None
    ) -> bool:
        """Wait for text to appear on the page."""
        ...

    def wait_for_text_not_visible(
        self, text: str, selector: str = "body", timeout: Optional[int] = None
    ) -> bool:
        """Wait for text to disappear from the page."""
        ...

    def wait_for_element_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> bool:
        """Wait for an element to become visible."""
        ...

    def wait_for_element_not_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> bool:
        """Wait for an element to become not visible."""
        ...

    def wait_for_element_absent(
        self, selector: str, timeout: Optional[int] = None
    ) -> bool:
        """Wait for an element to be removed from the DOM."""
        ...

    def assert_element(self, selector: str, timeout: Optional[int] = None) -> None:
        """Assert that an element exists in the DOM."""
        ...

    def assert_element_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """Assert that an element is visible."""
        ...

    def assert_element_present(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """Assert that an element is present in the DOM."""
        ...

    def assert_element_absent(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """Assert that an element is absent from the DOM."""
        ...

    def assert_element_not_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """Assert that an element is not visible."""
        ...

    def assert_element_attribute(
        self, selector: str, attribute: str, value: Optional[str] = None
    ) -> None:
        """Assert that an element has a specific attribute value."""
        ...

    def assert_title(self, title: str) -> None:
        """Assert that the page title matches the expected title."""
        ...

    def assert_title_contains(self, substring: str) -> None:
        """Assert that the page title contains a substring."""
        ...

    def assert_url(self, url: str) -> None:
        """Assert that the current URL matches the expected URL."""
        ...

    def assert_url_contains(self, substring: str) -> None:
        """Assert that the current URL contains a substring."""
        ...

    def assert_text(
        self, text: str, selector: str = "html", timeout: Optional[int] = None
    ) -> None:
        """Assert that text appears on the page."""
        ...

    def assert_exact_text(
        self, text: str, selector: str = "html", timeout: Optional[int] = None
    ) -> None:
        """Assert that exact text appears on the page."""
        ...

    def assert_text_not_visible(
        self, text: str, selector: str = "body", timeout: Optional[int] = None
    ) -> None:
        """Assert that text does not appear on the page."""
        ...

    def assert_true(self, expr: bool) -> None:
        """Assert that an expression is True."""
        ...

    def assert_false(self, expr: bool) -> None:
        """Assert that an expression is False."""
        ...

    def assert_equal(self, first: Any, second: Any) -> None:
        """Assert that two values are equal."""
        ...

    def assert_not_equal(self, first: Any, second: Any) -> None:
        """Assert that two values are not equal."""
        ...

    def assert_in(self, first: Any, second: Any) -> None:
        """Assert that a value is in a collection."""
        ...

    def assert_not_in(self, first: Any, second: Any) -> None:
        """Assert that a value is not in a collection."""
        ...

    def scroll_into_view(self, selector: str) -> None:
        """Scroll an element into view."""
        ...

    def scroll_to_y(self, y: int) -> None:
        """Scroll to a specific Y position."""
        ...

    def scroll_to_top(self) -> None:
        """Scroll to the top of the page."""
        ...

    def scroll_to_bottom(self) -> None:
        """Scroll to the bottom of the page."""
        ...

    def scroll_up(self, amount: int = 25) -> None:
        """Scroll up by a specific amount."""
        ...

    def scroll_down(self, amount: int = 25) -> None:
        """Scroll down by a specific amount."""
        ...

    def save_screenshot(
        self, name: str, folder: Optional[str] = None, selector: Optional[str] = None
    ) -> str:
        """Save a screenshot of the current page."""
        ...
