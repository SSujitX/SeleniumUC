from typing import Optional, Any, Union, List, Callable, Dict, Tuple
from .cdpinterface import CDPInterface


class CDPWrapper:
    """
    CDPWrapper wraps an underlying CDP implementation (such as SeleniumBase's CDP mode) and exposes
    a full set of methods for browser automation. Each method in this wrapper provides a detailed docstring
    with information on purpose, arguments, and return values. This comprehensive documentation ensures that
    every method call from the underlying interface is fully described.

    Attributes:
        _cdp: The underlying CDP object that implements the actual functionality.
    """

    __slots__ = ("_cdp",)

    def __init__(self, cdp: CDPInterface):
        """
        Initialize the CDPWrapper with a given CDP interface.

        Args:
            cdp (CDPInterface): The underlying CDP instance to wrap.
        """
        self._cdp = cdp

    def sleep(self, seconds: Union[int, float]) -> None:
        """
        Pause execution for a given number of seconds.

        Args:
            seconds (Union[int, float]): The number of seconds to sleep.
        """
        return self._cdp.sleep(seconds)

    def type(self, selector: str, text: str, timeout: Optional[int] = None) -> None:
        """
        Type a string into an element identified by the CSS selector.

        Args:
            selector (str): The CSS selector for the target element.
            text (str): The text to be typed.
            timeout (Optional[int]): Maximum time to wait (in seconds) before timing out.
        """
        return self._cdp.type(selector, text, timeout=timeout)

    def mouse_click(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Perform a mouse click on an element specified by the CSS selector.

        Args:
            selector (str): The CSS selector for the element to click.
            timeout (Optional[int]): Timeout in seconds.
        """
        return self._cdp.click(selector, timeout=timeout)

    def reload(
        self,
        ignore_cache: Optional[bool] = None,
        script_to_evaluate_on_load: Optional[str] = None,
    ) -> None:
        """
        Reload the current page.

        Args:
            ignore_cache (Optional[bool]): Whether to ignore the browser cache.
            script_to_evaluate_on_load (Optional[str]): JavaScript to execute when the page loads.
        """
        return self._cdp.reload(ignore_cache, script_to_evaluate_on_load)

    def refresh(self) -> None:
        """
        Refresh the current page. This is an alias for reload() without additional parameters.
        """
        return self._cdp.refresh()

    def find_element(
        self, selector: str, best_match: bool = False, timeout: Optional[int] = None
    ) -> Optional[Any]:
        """
        Find a single element matching the given CSS selector.

        Args:
            selector (str): The CSS selector to search for.
            best_match (bool): Whether to return the best matching element.
            timeout (Optional[int]): Maximum wait time in seconds.

        Returns:
            Optional[Any]: The found element or None if not found.
        """
        return self._cdp.find_element(selector, best_match, timeout)

    def get_attribute(self, selector: str, attribute: str) -> str:
        """
        Retrieve the value of a specific attribute from an element.

        Args:
            selector (str): The CSS selector for the element.
            attribute (str): The name of the attribute.

        Returns:
            str: The value of the attribute.
        """
        return self._cdp.get_attribute(selector, attribute)

    def is_element_visible(self, selector: str) -> bool:
        """
        Determine whether an element identified by the selector is visible on the page.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element is visible; otherwise, False.
        """
        return self._cdp.is_element_visible(selector)

    def get(self, url: str) -> None:
        """
        Navigate the browser to the specified URL.

        Args:
            url (str): The URL to navigate to.
        """
        return self._cdp.get(url)

    def open(self, url: str) -> None:
        """
        Open a new URL in the browser. This is an alias for the get() method.

        Args:
            url (str): The URL to open.
        """
        return self._cdp.open(url)

    def get_event_loop(self) -> Any:
        """
        Retrieve the current event loop for CDP operations.

        Returns:
            Any: The event loop object.
        """
        return self._cdp.get_event_loop()

    def add_handler(self, event: str, handler: Callable) -> None:
        """
        Add a handler function for a specific CDP event.

        Args:
            event (str): The name of the event.
            handler (Callable): The callback function to handle the event.
        """
        return self._cdp.add_handler(event, handler)

    def find(
        self, selector: str, best_match: bool = False, timeout: Optional[int] = None
    ) -> Any:
        """
        Find an element matching the given CSS selector (alias for find_element).

        Args:
            selector (str): The CSS selector for the element.
            best_match (bool): Whether to use the best matching element.
            timeout (Optional[int]): Maximum wait time in seconds.

        Returns:
            Any: The found element.
        """
        return self._cdp.find(selector, best_match, timeout)

    def locator(
        self, selector: str, best_match: bool = False, timeout: Optional[int] = None
    ) -> Any:
        """
        Obtain a locator for the element identified by the selector.

        Args:
            selector (str): The CSS selector for the element.
            best_match (bool): Whether to use the best matching element.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            Any: The locator for the element.
        """
        return self._cdp.locator(selector, best_match, timeout)

    def find_element_by_text(
        self, text: str, tag_name: Optional[str] = None, timeout: Optional[int] = None
    ) -> Any:
        """
        Locate an element based on its text content.

        Args:
            text (str): The text to search for.
            tag_name (Optional[str]): Filter by a specific tag name if provided.
            timeout (Optional[int]): Maximum wait time in seconds.

        Returns:
            Any: The found element.
        """
        return self._cdp.find_element_by_text(text, tag_name, timeout)

    def find_all(self, selector: str, timeout: Optional[int] = None) -> List[Any]:
        """
        Retrieve all elements that match the given CSS selector.

        Args:
            selector (str): The CSS selector for the elements.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            List[Any]: A list of matching elements.
        """
        return self._cdp.find_all(selector, timeout)

    def find_elements_by_text(
        self, text: str, tag_name: Optional[str] = None
    ) -> List[Any]:
        """
        Find all elements that contain the specified text.

        Args:
            text (str): The text to search for.
            tag_name (Optional[str]): Optionally, filter by tag name.

        Returns:
            List[Any]: A list of elements with the matching text.
        """
        return self._cdp.find_elements_by_text(text, tag_name)

    def select(self, selector: str, timeout: Optional[int] = None) -> Any:
        """
        Select an element based on the CSS selector.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            Any: The selected element.
        """
        return self._cdp.select(selector, timeout)

    def select_all(self, selector: str, timeout: Optional[int] = None) -> List[Any]:
        """
        Select all elements that match the CSS selector.

        Args:
            selector (str): The CSS selector for the elements.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            List[Any]: A list of selected elements.
        """
        return self._cdp.select_all(selector, timeout)

    def find_elements(self, selector: str, timeout: Optional[int] = None) -> List[Any]:
        """
        Find all elements matching the given CSS selector.

        Args:
            selector (str): The CSS selector for the elements.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            List[Any]: A list of found elements.
        """
        return self._cdp.find_elements(selector, timeout)

    def find_visible_elements(
        self, selector: str, timeout: Optional[int] = None
    ) -> List[Any]:
        """
        Retrieve all visible elements matching the CSS selector.

        Args:
            selector (str): The CSS selector for the elements.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            List[Any]: A list of visible elements.
        """
        return self._cdp.find_visible_elements(selector, timeout)

    def click_nth_element(self, selector: str, number: int) -> None:
        """
        Click the nth element in a list of elements matching the CSS selector.

        Args:
            selector (str): The CSS selector for the elements.
            number (int): The zero-based index of the element to click.
        """
        return self._cdp.click_nth_element(selector, number)

    def click_nth_visible_element(self, selector: str, number: int) -> None:
        """
        Click the nth visible element among those matching the CSS selector.

        Args:
            selector (str): The CSS selector for the elements.
            number (int): The index of the visible element to click.
        """
        return self._cdp.click_nth_visible_element(selector, number)

    def click_link(self, link_text: str) -> None:
        """
        Click a hyperlink on the page identified by its text.

        Args:
            link_text (str): The visible text of the link.
        """
        return self._cdp.click_link(link_text)

    def go_back(self) -> None:
        """
        Navigate back to the previous page in the browser history.
        """
        return self._cdp.go_back()

    def go_forward(self) -> None:
        """
        Navigate forward in the browser history.
        """
        return self._cdp.go_forward()

    def get_navigation_history(self) -> Dict:
        """
        Retrieve the navigation history of the browser.

        Returns:
            Dict: A dictionary containing navigation history details.
        """
        return self._cdp.get_navigation_history()

    def tile_windows(
        self, windows: Optional[List] = None, max_columns: int = 0
    ) -> None:
        """
        Arrange multiple browser windows in a tiled layout.

        Args:
            windows (Optional[List]): A list of window handles to tile.
            max_columns (int): Maximum number of columns to arrange the windows.
        """
        return self._cdp.tile_windows(windows, max_columns)

    def get_all_cookies(self, *args, **kwargs) -> List[Dict]:
        """
        Retrieve all cookies from the current browser session.

        Returns:
            List[Dict]: A list of dictionaries with cookie information.
        """
        return self._cdp.get_all_cookies(*args, **kwargs)

    def set_all_cookies(self, *args, **kwargs) -> None:
        """
        Set cookies for the browser session.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        return self._cdp.set_all_cookies(*args, **kwargs)

    def save_cookies(self, *args, **kwargs) -> None:
        """
        Save the current cookies to a file.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        return self._cdp.save_cookies(*args, **kwargs)

    def load_cookies(self, *args, **kwargs) -> None:
        """
        Load cookies from a file into the browser session.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        return self._cdp.load_cookies(*args, **kwargs)

    def clear_cookies(self) -> None:
        """
        Clear all cookies from the current browser session.
        """
        return self._cdp.clear_cookies()

    def bring_active_window_to_front(self) -> None:
        """
        Bring the active browser window to the front.

        This method ensures that the active window is focused.
        """
        return self._cdp.bring_active_window_to_front()

    def bring_to_front(self) -> None:
        """
        Bring the active window to the front (alias for bring_active_window_to_front).

        Returns:
            None
        """
        return self._cdp.bring_to_front()

    def get_active_element(self) -> Any:
        """
        Retrieve the currently active element on the page.

        Returns:
            Any: The active element.
        """
        return self._cdp.get_active_element()

    def get_active_element_css(self) -> str:
        """
        Get the computed CSS of the currently active element.

        Returns:
            str: A string representation of the active element's CSS.
        """
        return self._cdp.get_active_element_css()

    def click(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Click an element specified by the CSS selector.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Timeout in seconds.
        """
        return self._cdp.click(selector, timeout)

    def click_active_element(self) -> None:
        """
        Click on the element that is currently active.

        Returns:
            None
        """
        return self._cdp.click_active_element()

    def click_if_visible(self, selector: str) -> bool:
        """
        Click an element if it is visible.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element was visible and clicked; otherwise, False.
        """
        return self._cdp.click_if_visible(selector)

    def click_visible_elements(self, selector: str, limit: int = 0) -> int:
        """
        Click all visible elements matching the selector up to an optional limit.

        Args:
            selector (str): The CSS selector for the elements.
            limit (int): Maximum number of elements to click (0 for no limit).

        Returns:
            int: The number of elements clicked.
        """
        return self._cdp.click_visible_elements(selector, limit)

    def nested_click(self, parent_selector: str, selector: str) -> None:
        """
        Click on a nested element within a parent element.

        Args:
            parent_selector (str): The CSS selector for the parent element.
            selector (str): The CSS selector for the nested element.
        """
        return self._cdp.nested_click(parent_selector, selector)

    def get_nested_element(self, parent_selector: str, selector: str) -> Any:
        """
        Retrieve a nested element given a parent and child CSS selector.

        Args:
            parent_selector (str): The CSS selector for the parent element.
            selector (str): The CSS selector for the nested element.

        Returns:
            Any: The found nested element.
        """
        return self._cdp.get_nested_element(parent_selector, selector)

    def select_option_by_text(self, dropdown_selector: str, option: str) -> None:
        """
        Select an option from a dropdown element by matching its visible text.

        Args:
            dropdown_selector (str): The CSS selector for the dropdown.
            option (str): The visible text of the option to select.
        """
        return self._cdp.select_option_by_text(dropdown_selector, option)

    def flash(
        self, selector: str, duration: int = 1, color: str = "44CC88", pause: int = 0
    ) -> None:
        """
        Flash an element by temporarily changing its style.

        Args:
            selector (str): The CSS selector for the element.
            duration (int): Duration in seconds for which to flash.
            color (str): The flash color (default "44CC88").
            pause (int): Pause time between flashes in seconds.
        """
        return self._cdp.flash(selector, duration, color, pause)

    def highlight(self, selector: str) -> None:
        """
        Highlight an element on the page.

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.highlight(selector)

    def focus(self, selector: str) -> None:
        """
        Set focus to a specific element.

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.focus(selector)

    def highlight_overlay(self, selector: str) -> None:
        """
        Highlight an element using an overlay effect.

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.highlight_overlay(selector)

    def get_parent(self, element: Any) -> Any:
        """
        Get the parent element of a given element.

        Args:
            element (Any): The element whose parent is needed.

        Returns:
            Any: The parent element.
        """
        return self._cdp.get_parent(element)

    def remove_element(self, selector: str) -> None:
        """
        Remove an element from the DOM based on its CSS selector.

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.remove_element(selector)

    def remove_from_dom(self, selector: str) -> None:
        """
        Remove an element from the DOM (alias for remove_element).

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.remove_from_dom(selector)

    def remove_elements(self, selector: str) -> None:
        """
        Remove all elements matching the CSS selector from the DOM.

        Args:
            selector (str): The CSS selector for the elements.
        """
        return self._cdp.remove_elements(selector)

    def send_keys(
        self, selector: str, text: str, timeout: Optional[int] = None
    ) -> None:
        """
        Send keystrokes to an element.

        Args:
            selector (str): The CSS selector for the target element.
            text (str): The text or keys to send.
            timeout (Optional[int]): Timeout in seconds.
        """
        return self._cdp.send_keys(selector, text, timeout)

    def press_keys(
        self, selector: str, text: str, timeout: Optional[int] = None
    ) -> None:
        """
        Simulate pressing keys on an element.

        Args:
            selector (str): The CSS selector for the element.
            text (str): The keys to press.
            timeout (Optional[int]): Timeout in seconds.
        """
        return self._cdp.press_keys(selector, text, timeout)

    def set_value(
        self, selector: str, text: str, timeout: Optional[int] = None
    ) -> None:
        """
        Set the value of an input element.

        Args:
            selector (str): The CSS selector for the input element.
            text (str): The value to set.
            timeout (Optional[int]): Timeout in seconds.
        """
        return self._cdp.set_value(selector, text, timeout)

    def evaluate(self, expression: str) -> Any:
        """
        Evaluate a JavaScript expression in the context of the current page.

        Args:
            expression (str): The JavaScript expression to evaluate.

        Returns:
            Any: The result of the evaluation.
        """
        return self._cdp.evaluate(expression)

    def js_dumps(self, obj_name: str) -> str:
        """
        Dump a JavaScript object as a string.

        Args:
            obj_name (str): The name of the JavaScript object.

        Returns:
            str: A string representation of the JavaScript object.
        """
        return self._cdp.js_dumps(obj_name)

    def maximize(self) -> None:
        """
        Maximize the browser window.
        """
        return self._cdp.maximize()

    def minimize(self) -> None:
        """
        Minimize the browser window.
        """
        return self._cdp.minimize()

    def medimize(self) -> None:
        """
        Set the browser window to a medium size.
        """
        return self._cdp.medimize()

    def set_window_rect(
        self,
        x: Optional[int] = None,
        y: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ) -> None:
        """
        Set the dimensions and position of the browser window.

        Args:
            x (Optional[int]): The x-coordinate for the window.
            y (Optional[int]): The y-coordinate for the window.
            width (Optional[int]): The width of the window.
            height (Optional[int]): The height of the window.
        """
        return self._cdp.set_window_rect(x=x, y=y, width=width, height=height)

    def reset_window_size(self) -> None:
        """
        Reset the browser window to its default size.
        """
        return self._cdp.reset_window_size()

    def open_new_window(self, url: Optional[str] = None, switch_to: bool = True) -> Any:
        """
        Open a new browser window and optionally switch focus to it.

        Args:
            url (Optional[str]): An optional URL to open in the new window.
            switch_to (bool): If True, switch focus to the new window (default is True).

        Returns:
            Any: The handle of the new window.
        """
        return self._cdp.open_new_window(url=url, switch_to=switch_to)

    def switch_to_window(self, window: Union[str, int]) -> None:
        """
        Switch focus to a specific browser window.

        Args:
            window (Union[str, int]): The window handle or index.
        """
        return self._cdp.switch_to_window(window)

    def switch_to_newest_window(self) -> None:
        """
        Switch focus to the most recently opened browser window.
        """
        return self._cdp.switch_to_newest_window()

    def open_new_tab(self, url: Optional[str] = None, switch_to: bool = True) -> Any:
        """
        Open a new browser tab and optionally switch focus to it.

        Args:
            url (Optional[str]): An optional URL to open in the new tab.
            switch_to (bool): If True, switch focus to the new tab (default is True).

        Returns:
            Any: The handle of the new tab.
        """
        return self._cdp.open_new_tab(url=url, switch_to=switch_to)

    def switch_to_tab(self, tab: Union[str, int]) -> None:
        """
        Switch focus to a specific browser tab.

        Args:
            tab (Union[str, int]): The tab handle or index.
        """
        return self._cdp.switch_to_tab(tab)

    def switch_to_newest_tab(self) -> None:
        """
        Switch focus to the most recently opened browser tab.
        """
        return self._cdp.switch_to_newest_tab()

    def close_active_tab(self) -> None:
        """
        Close the currently active browser tab.
        """
        return self._cdp.close_active_tab()

    def get_active_tab(self) -> str:
        """
        Get the handle of the currently active tab.

        Returns:
            str: The active tab handle.
        """
        return self._cdp.get_active_tab()

    def get_tabs(self) -> List[str]:
        """
        Retrieve handles for all open tabs.

        Returns:
            List[str]: A list of all tab handles.
        """
        return self._cdp.get_tabs()

    def get_window(self) -> str:
        """
        Get the handle of the currently active window.

        Returns:
            str: The active window handle.
        """
        return self._cdp.get_window()

    def get_text(self, selector: str) -> str:
        """
        Retrieve the text content of an element.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            str: The text contained within the element.
        """
        return self._cdp.get_text(selector)

    def get_title(self) -> str:
        """
        Retrieve the title of the current page.

        Returns:
            str: The page title.
        """
        return self._cdp.get_title()

    def get_current_url(self) -> str:
        """
        Retrieve the URL of the current page.

        Returns:
            str: The current page URL.
        """
        return self._cdp.get_current_url()

    def get_origin(self) -> str:
        """
        Retrieve the origin (protocol + domain) of the current page.

        Returns:
            str: The origin string.
        """
        return self._cdp.get_origin()

    def get_page_source(self) -> str:
        """
        Retrieve the full HTML source of the current page.

        Returns:
            str: The HTML source code.
        """
        return self._cdp.get_page_source()

    def get_user_agent(self) -> str:
        """
        Retrieve the user agent string of the browser.

        Returns:
            str: The user agent.
        """
        return self._cdp.get_user_agent()

    def get_cookie_string(self) -> str:
        """
        Retrieve all cookies as a single string.

        Returns:
            str: The concatenated cookie string.
        """
        return self._cdp.get_cookie_string()

    def get_locale_code(self) -> str:
        """
        Retrieve the locale code used by the browser.

        Returns:
            str: The locale code.
        """
        return self._cdp.get_locale_code()

    def get_screen_rect(self) -> Dict[str, int]:
        """
        Retrieve the dimensions of the screen.

        Returns:
            Dict[str, int]: A dictionary with screen width and height.
        """
        return self._cdp.get_screen_rect()

    def get_window_rect(self) -> Dict[str, int]:
        """
        Retrieve the dimensions and position of the browser window.

        Returns:
            Dict[str, int]: A dictionary with window x, y, width, and height.
        """
        return self._cdp.get_window_rect()

    def get_window_size(self) -> Dict[str, int]:
        """
        Retrieve the size (width and height) of the browser window.

        Returns:
            Dict[str, int]: A dictionary with window width and height.
        """
        return self._cdp.get_window_size()

    def get_window_position(self) -> Dict[str, int]:
        """
        Retrieve the position (x and y coordinates) of the browser window.

        Returns:
            Dict[str, int]: A dictionary with window x and y positions.
        """
        return self._cdp.get_window_position()

    def get_element_rect(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """
        Retrieve the rectangle (position and size) of an element.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            Dict[str, int]: A dictionary with element x, y, width, and height.
        """
        return self._cdp.get_element_rect(selector, timeout=timeout)

    def get_element_size(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """
        Retrieve the size (width and height) of an element.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            Dict[str, int]: A dictionary with element width and height.
        """
        return self._cdp.get_element_size(selector, timeout=timeout)

    def get_element_position(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """
        Retrieve the position (x and y coordinates) of an element.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            Dict[str, int]: A dictionary with element x and y coordinates.
        """
        return self._cdp.get_element_position(selector, timeout=timeout)

    def get_gui_element_rect(
        self, selector: str, timeout: Optional[int] = None
    ) -> Dict[str, int]:
        """
        Retrieve the rectangle dimensions of a GUI element.

        Args:
            selector (str): The CSS selector for the GUI element.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            Dict[str, int]: A dictionary with GUI element dimensions.
        """
        return self._cdp.get_gui_element_rect(selector, timeout=timeout)

    def get_gui_element_center(
        self, selector: str, timeout: Optional[int] = None
    ) -> Tuple[int, int]:
        """
        Retrieve the center coordinates of a GUI element.

        Args:
            selector (str): The CSS selector for the GUI element.
            timeout (Optional[int]): Timeout in seconds.

        Returns:
            Tuple[int, int]: A tuple with the x and y coordinates of the element's center.
        """
        return self._cdp.get_gui_element_center(selector, timeout=timeout)

    def get_document(self) -> Dict[str, Any]:
        """
        Retrieve the full document object of the current page.

        Returns:
            Dict[str, Any]: A dictionary representing the document.
        """
        return self._cdp.get_document()

    def get_flattened_document(self) -> Dict[str, Any]:
        """
        Retrieve a flattened version of the document object.

        Returns:
            Dict[str, Any]: A dictionary representing the flattened document.
        """
        return self._cdp.get_flattened_document()

    def get_element_attributes(self, selector: str) -> Dict[str, str]:
        """
        Retrieve all attributes for an element.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            Dict[str, str]: A dictionary of attribute names and values.
        """
        return self._cdp.get_element_attributes(selector)

    def get_element_attribute(self, selector: str, attribute: str) -> str:
        """
        Retrieve a specific attribute's value from an element.

        Args:
            selector (str): The CSS selector for the element.
            attribute (str): The attribute name.

        Returns:
            str: The value of the attribute.
        """
        return self._cdp.get_element_attribute(selector, attribute)

    def get_element_html(self, selector: str) -> str:
        """
        Retrieve the HTML content of an element.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            str: The HTML string of the element.
        """
        return self._cdp.get_element_html(selector)

    def set_locale(self, locale: str) -> None:
        """
        Set the browser's locale.

        Args:
            locale (str): The locale code to set (e.g., "en-US").
        """
        return self._cdp.set_locale(locale)

    def set_attributes(self, selector: str, attribute: str, value: str) -> None:
        """
        Set a specific attribute to a new value for an element.

        Args:
            selector (str): The CSS selector for the element.
            attribute (str): The attribute name.
            value (str): The new value to set.
        """
        return self._cdp.set_attributes(selector, attribute, value)

    def gui_press_key(self, key: str) -> None:
        """
        Simulate pressing a single key using GUI automation.

        Args:
            key (str): The key to press.
        """
        return self._cdp.gui_press_key(key)

    def gui_press_keys(self, keys: str) -> None:
        """
        Simulate pressing multiple keys using GUI automation.

        Args:
            keys (str): A string representing the keys to press.
        """
        return self._cdp.gui_press_keys(keys)

    def gui_write(self, text: str) -> None:
        """
        Write text using GUI automation.

        Args:
            text (str): The text to write.
        """
        return self._cdp.gui_write(text)

    def gui_click_x_y(self, x: int, y: int) -> None:
        """
        Click on the screen at the specified x and y coordinates using GUI automation.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        return self._cdp.gui_click_x_y(x, y)

    def gui_click_element(self, selector: str) -> None:
        """
        Click an element using GUI automation based on its CSS selector.

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.gui_click_element(selector)

    def gui_drag_drop_points(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """
        Perform a drag-and-drop action from one point to another using GUI automation.

        Args:
            x1 (int): The starting x-coordinate.
            y1 (int): The starting y-coordinate.
            x2 (int): The ending x-coordinate.
            y2 (int): The ending y-coordinate.
        """
        return self._cdp.gui_drag_drop_points(x1, y1, x2, y2)

    def gui_drag_and_drop(self, drag_selector: str, drop_selector: str) -> None:
        """
        Drag an element and drop it onto another element using GUI automation.

        Args:
            drag_selector (str): The CSS selector for the element to drag.
            drop_selector (str): The CSS selector for the target element.
        """
        return self._cdp.gui_drag_and_drop(drag_selector, drop_selector)

    def gui_hover_x_y(self, x: int, y: int) -> None:
        """
        Hover over the screen at the specified coordinates using GUI automation.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        return self._cdp.gui_hover_x_y(x, y)

    def gui_hover_element(self, selector: str) -> None:
        """
        Hover over an element using its CSS selector with GUI automation.

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.gui_hover_element(selector)

    def gui_hover_and_click(self, hover_selector: str, click_selector: str) -> None:
        """
        Hover over one element and then click on another element using GUI automation.

        Args:
            hover_selector (str): The CSS selector for the element to hover over.
            click_selector (str): The CSS selector for the element to click.
        """
        return self._cdp.gui_hover_and_click(hover_selector, click_selector)

    def internalize_links(self) -> None:
        """
        Modify all links on the page so that they open in the current window instead of a new tab/window.
        """
        return self._cdp.internalize_links()

    def is_checked(self, selector: str) -> bool:
        """
        Check whether a checkbox or radio button is checked.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element is checked, otherwise False.
        """
        return self._cdp.is_checked(selector)

    def is_selected(self, selector: str) -> bool:
        """
        Check whether an element is selected.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element is selected, otherwise False.
        """
        return self._cdp.is_selected(selector)

    def check_if_unchecked(self, selector: str) -> bool:
        """
        If a checkbox or radio button is unchecked, check it.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element was unchecked and has now been checked; otherwise, False.
        """
        return self._cdp.check_if_unchecked(selector)

    def select_if_unselected(self, selector: str) -> bool:
        """
        If an element is not already selected, select it.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element was unselected and is now selected; otherwise, False.
        """
        return self._cdp.select_if_unselected(selector)

    def uncheck_if_checked(self, selector: str) -> bool:
        """
        Uncheck a checkbox or radio button if it is currently checked.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element was checked and has now been unchecked; otherwise, False.
        """
        return self._cdp.uncheck_if_checked(selector)

    def unselect_if_selected(self, selector: str) -> bool:
        """
        Unselect an element if it is currently selected.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element was selected and has now been unselected; otherwise, False.
        """
        return self._cdp.unselect_if_selected(selector)

    def is_element_present(self, selector: str) -> bool:
        """
        Check if an element exists in the DOM.

        Args:
            selector (str): The CSS selector for the element.

        Returns:
            bool: True if the element is present, otherwise False.
        """
        return self._cdp.is_element_present(selector)

    def is_text_visible(self, text: str, selector: str = "body") -> bool:
        """
        Check if a specific text is visible on the page.

        Args:
            text (str): The text to check for.
            selector (str): The CSS selector within which to search (default is "body").

        Returns:
            bool: True if the text is visible, otherwise False.
        """
        return self._cdp.is_text_visible(text, selector)

    def is_exact_text_visible(self, text: str, selector: str = "body") -> bool:
        """
        Check if an exact text string is visible on the page.

        Args:
            text (str): The exact text to check for.
            selector (str): The CSS selector within which to search (default is "body").

        Returns:
            bool: True if the exact text is visible, otherwise False.
        """
        return self._cdp.is_exact_text_visible(text, selector)

    def wait_for_text(
        self, text: str, selector: str = "body", timeout: Optional[int] = None
    ) -> bool:
        """
        Wait until a specific text appears on the page.

        Args:
            text (str): The text to wait for.
            selector (str): The CSS selector within which to check (default is "body").
            timeout (Optional[int]): Maximum time to wait in seconds.

        Returns:
            bool: True if the text appears before the timeout, otherwise False.
        """
        return self._cdp.wait_for_text(text, selector, timeout)

    def wait_for_text_not_visible(
        self, text: str, selector: str = "body", timeout: Optional[int] = None
    ) -> bool:
        """
        Wait until a specific text disappears from the page.

        Args:
            text (str): The text to wait to disappear.
            selector (str): The CSS selector within which to check (default is "body").
            timeout (Optional[int]): Maximum time to wait in seconds.

        Returns:
            bool: True if the text is no longer visible before the timeout, otherwise False.
        """
        return self._cdp.wait_for_text_not_visible(text, selector, timeout)

    def wait_for_element_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> bool:
        """
        Wait until an element becomes visible.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Returns:
            bool: True if the element becomes visible before the timeout, otherwise False.
        """
        return self._cdp.wait_for_element_visible(selector, timeout)

    def wait_for_element_not_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> bool:
        """
        Wait until an element is no longer visible.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Returns:
            bool: True if the element is not visible before the timeout, otherwise False.
        """
        return self._cdp.wait_for_element_not_visible(selector, timeout)

    def wait_for_element_absent(
        self, selector: str, timeout: Optional[int] = None
    ) -> bool:
        """
        Wait until an element is removed from the DOM.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Returns:
            bool: True if the element is absent before the timeout, otherwise False.
        """
        return self._cdp.wait_for_element_absent(selector, timeout)

    def assert_element(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Assert that an element exists in the DOM.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the element is not found within the timeout.
        """
        return self._cdp.assert_element(selector, timeout)

    def assert_element_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """
        Assert that an element is visible.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the element is not visible within the timeout.
        """
        return self._cdp.assert_element_visible(selector, timeout)

    def assert_element_present(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """
        Assert that an element is present in the DOM.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the element is not present within the timeout.
        """
        return self._cdp.assert_element_present(selector, timeout)

    def assert_element_absent(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """
        Assert that an element is absent from the DOM.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the element is still present within the timeout.
        """
        return self._cdp.assert_element_absent(selector, timeout)

    def assert_element_not_visible(
        self, selector: str, timeout: Optional[int] = None
    ) -> None:
        """
        Assert that an element is not visible.

        Args:
            selector (str): The CSS selector for the element.
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the element remains visible within the timeout.
        """
        return self._cdp.assert_element_not_visible(selector, timeout)

    def assert_element_attribute(
        self, selector: str, attribute: str, value: Optional[str] = None
    ) -> None:
        """
        Assert that an element has a specific attribute value.

        Args:
            selector (str): The CSS selector for the element.
            attribute (str): The attribute name.
            value (Optional[str]): The expected value of the attribute.

        Raises:
            AssertionError: If the attribute's value does not match.
        """
        return self._cdp.assert_element_attribute(selector, attribute, value)

    def assert_title(self, title: str) -> None:
        """
        Assert that the page title exactly matches the expected title.

        Args:
            title (str): The expected page title.

        Raises:
            AssertionError: If the title does not match.
        """
        return self._cdp.assert_title(title)

    def assert_title_contains(self, substring: str) -> None:
        """
        Assert that the page title contains the given substring.

        Args:
            substring (str): The substring that should be present in the title.

        Raises:
            AssertionError: If the substring is not found in the title.
        """
        return self._cdp.assert_title_contains(substring)

    def assert_url(self, url: str) -> None:
        """
        Assert that the current URL exactly matches the expected URL.

        Args:
            url (str): The expected URL.

        Raises:
            AssertionError: If the URL does not match.
        """
        return self._cdp.assert_url(url)

    def assert_url_contains(self, substring: str) -> None:
        """
        Assert that the current URL contains a specified substring.

        Args:
            substring (str): The substring that should be found in the URL.

        Raises:
            AssertionError: If the substring is not present in the URL.
        """
        return self._cdp.assert_url_contains(substring)

    def assert_text(
        self, text: str, selector: str = "html", timeout: Optional[int] = None
    ) -> None:
        """
        Assert that the given text appears on the page within the specified element.

        Args:
            text (str): The text to look for.
            selector (str): The CSS selector for the element (default "html").
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the text does not appear within the timeout.
        """
        return self._cdp.assert_text(text, selector, timeout)

    def assert_exact_text(
        self, text: str, selector: str = "html", timeout: Optional[int] = None
    ) -> None:
        """
        Assert that the given exact text appears on the page within the specified element.

        Args:
            text (str): The exact text to match.
            selector (str): The CSS selector for the element (default "html").
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the exact text does not appear within the timeout.
        """
        return self._cdp.assert_exact_text(text, selector, timeout)

    def assert_text_not_visible(
        self, text: str, selector: str = "body", timeout: Optional[int] = None
    ) -> None:
        """
        Assert that a specified text does not appear on the page.

        Args:
            text (str): The text that should not be visible.
            selector (str): The CSS selector for the element (default "body").
            timeout (Optional[int]): Maximum time to wait in seconds.

        Raises:
            AssertionError: If the text is visible within the timeout.
        """
        return self._cdp.assert_text_not_visible(text, selector, timeout)

    def assert_true(self, expr: bool) -> None:
        """
        Assert that a given expression is True.

        Args:
            expr (bool): The expression to evaluate.

        Raises:
            AssertionError: If the expression is not True.
        """
        return self._cdp.assert_true(expr)

    def assert_false(self, expr: bool) -> None:
        """
        Assert that a given expression is False.

        Args:
            expr (bool): The expression to evaluate.

        Raises:
            AssertionError: If the expression is not False.
        """
        return self._cdp.assert_false(expr)

    def assert_equal(self, first: Any, second: Any) -> None:
        """
        Assert that two values are equal.

        Args:
            first (Any): The first value.
            second (Any): The second value.

        Raises:
            AssertionError: If the two values are not equal.
        """
        return self._cdp.assert_equal(first, second)

    def assert_not_equal(self, first: Any, second: Any) -> None:
        """
        Assert that two values are not equal.

        Args:
            first (Any): The first value.
            second (Any): The second value.

        Raises:
            AssertionError: If the two values are equal.
        """
        return self._cdp.assert_not_equal(first, second)

    def assert_in(self, first: Any, second: Any) -> None:
        """
        Assert that a value exists within a collection.

        Args:
            first (Any): The value to search for.
            second (Any): The collection to search in.

        Raises:
            AssertionError: If the value is not found in the collection.
        """
        return self._cdp.assert_in(first, second)

    def assert_not_in(self, first: Any, second: Any) -> None:
        """
        Assert that a value does not exist within a collection.

        Args:
            first (Any): The value that should not be present.
            second (Any): The collection to check.

        Raises:
            AssertionError: If the value is found in the collection.
        """
        return self._cdp.assert_not_in(first, second)

    def scroll_into_view(self, selector: str) -> None:
        """
        Scroll the page such that the element specified by the selector comes into view.

        Args:
            selector (str): The CSS selector for the element.
        """
        return self._cdp.scroll_into_view(selector)

    def scroll_to_y(self, y: int) -> None:
        """
        Scroll the page vertically to a specific y-coordinate.

        Args:
            y (int): The y-coordinate to scroll to.
        """
        return self._cdp.scroll_to_y(y)

    def scroll_to_top(self) -> None:
        """
        Scroll to the very top of the page.
        """
        return self._cdp.scroll_to_top()

    def scroll_to_bottom(self) -> None:
        """
        Scroll to the very bottom of the page.
        """
        return self._cdp.scroll_to_bottom()

    def scroll_up(self, amount: int = 25) -> None:
        """
        Scroll upward by a given number of pixels.

        Args:
            amount (int): The number of pixels to scroll up (default is 25).
        """
        return self._cdp.scroll_up(amount)

    def scroll_down(self, amount: int = 25) -> None:
        """
        Scroll downward by a given number of pixels.

        Args:
            amount (int): The number of pixels to scroll down (default is 25).
        """
        return self._cdp.scroll_down(amount)

    def save_screenshot(
        self, name: str, folder: Optional[str] = None, selector: Optional[str] = None
    ) -> str:
        """
        Save a screenshot of the current page or a specific element.

        Args:
            name (str): The file name for the screenshot.
            folder (Optional[str]): The folder in which to save the screenshot.
            selector (Optional[str]): If provided, only capture the element matching this selector.

        Returns:
            str: The path to the saved screenshot file.
        """
        return self._cdp.save_screenshot(name, folder, selector)
