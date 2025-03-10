from seleniumbase import SB
from typing import Optional, Any

from .driver.driverwrapper import DriverWrapper
from .driver.driverinteface import DriverInterface
from .cdp.cdpinterface import CDPInterface
from .cdp.cdpwrapper import CDPWrapper


class UC:
    """Main class combining SeleniumBase methods with CDP functionality."""

    def __init__(
        self,
        uc=None,
        undetected=None,
        headless=None,
        test=None,
        incognito=None,
        guest_mode=None,
        dark_mode=None,
        devtools=None,
        rtf=None,
        raise_test_failure=None,
        browser=None,
        headless1=None,
        headless2=None,
        locale_code=None,
        protocol=None,
        servername=None,
        port=None,
        proxy=None,
        proxy_bypass_list=None,
        proxy_pac_url=None,
        multi_proxy=None,
        agent=None,
        cap_file=None,
        cap_string=None,
        recorder_ext=None,
        disable_cookies=None,
        disable_js=None,
        disable_csp=None,
        enable_ws=None,
        enable_sync=None,
        use_auto_ext=None,
        undetectable=None,
        uc_cdp_events=None,
        uc_subprocess=None,
        log_cdp_events=None,
        remote_debug=None,
        enable_3d_apis=None,
        swiftshader=None,
        ad_block_on=None,
        host_resolver_rules=None,
        block_images=None,
        do_not_track=None,
        chromium_arg=None,
        firefox_arg=None,
        firefox_pref=None,
        user_data_dir=None,
        extension_zip=None,
        extension_dir=None,
        disable_features=None,
        binary_location=None,
        driver_version=None,
        skip_js_waits=None,
        wait_for_angularjs=None,
        use_wire=None,
        external_pdf=None,
        window_position=None,
        window_size=None,
        is_mobile=None,
        mobile=None,
        device_metrics=None,
        xvfb=None,
        xvfb_metrics=None,
        start_page=None,
        rec_print=None,
        rec_behave=None,
        record_sleep=None,
        data=None,
        var1=None,
        var2=None,
        var3=None,
        variables=None,
        account=None,
        environment=None,
        headed=None,
        maximize=None,
        disable_ws=None,
        disable_beforeunload=None,
        settings_file=None,
        position=None,
        size=None,
        uc_cdp=None,
        uc_sub=None,
        locale=None,
        log_cdp=None,
        ad_block=None,
        server=None,
        guest=None,
        wire=None,
        pls=None,
        sjw=None,
        wfa=None,
        cft=None,
        chs=None,
        save_screenshot=None,
        no_screenshot=None,
        page_load_strategy=None,
        timeout_multiplier=None,
        js_checking_on=None,
        slow=None,
        demo=None,
        demo_sleep=None,
        message_duration=None,
        highlights=None,
        interval=None,
        time_limit=None,
        **kwargs,
    ) -> None:
        """Initialize SeleniumCDP with extensive SeleniumBase options.
                Example:
        --------
        .. code-block:: python
            from seleniumbase import SB

            with SB() as sb:  # Many args! Eg. SB(browser="edge")
                sb.open("https://google.com/ncr")
                sb.type('[name="q"]', "SeleniumBase on GitHub")
                sb.submit('[name="q"]')
                sb.click('a[href*="github.com/seleniumbase"]')
                sb.highlight("div.Layout-main")
                sb.highlight("div.Layout-sidebar")
                sb.sleep(0.5)

        Args:
            test (bool):  Test Mode: Output, Logging, Continue on failure unless "rtf".
            rtf (bool):  Shortcut / Duplicate of "raise_test_failure".
            raise_test_failure (bool):  If "test" mode, raise Exception on 1st failure.
            browser (str):  Choose from "chrome", "edge", "firefox", or "safari".
            headless (bool):  Use the default headless mode for Chromium and Firefox.
            headless1 (bool):  Use Chromium's old headless mode. (Fast, but limited)
            headless2 (bool):  Use Chromium's new headless mode. (Has more features)
            locale_code (str):  Set the Language Locale Code for the web browser.
            protocol (str):  The Selenium Grid protocol: "http" or "https".
            servername (str):  The Selenium Grid server/IP used for tests.
            port (int):  The Selenium Grid port used by the test server.
            proxy (str):  Use proxy. Format: "SERVER:PORT" or "USER:PASS@SERVER:PORT".
            proxy_bypass_list (str):  Skip proxy when using the listed domains.
            proxy_pac_url (str):  Use PAC file. (Format: URL or USERNAME:PASSWORD@URL)
            multi_proxy (bool):  # Allow multiple proxies with auth when multithreaded.
            agent (str):  Modify the web browser's User-Agent string.
            cap_file (str):  The desired capabilities to use with a Selenium Grid.
            cap_string (str):  The desired capabilities to use with a Selenium Grid.
            recorder_ext (bool):  Enables the SeleniumBase Recorder Chromium extension.
            disable_cookies (bool):  Disable Cookies on websites. (Pages might break!)
            disable_js (bool):  Disable JavaScript on websites. (Pages might break!)
            disable_csp (bool):  Disable the Content Security Policy of websites.
            enable_ws (bool):  Enable Web Security on Chromium-based browsers.
            enable_sync (bool):  Enable "Chrome Sync" on websites.
            use_auto_ext (bool):  Use Chrome's automation extension.
            undetectable (bool):  Use undetected-chromedriver to evade bot-detection.
            uc_cdp_events (bool):  Capture CDP events in undetected-chromedriver mode.
            uc_subprocess (bool):  Use undetected-chromedriver as a subprocess.
            log_cdp_events (bool):  Capture {"performance": "ALL", "browser": "ALL"}
            incognito (bool):  Enable Chromium's Incognito mode.
            guest_mode (bool):  Enable Chromium's Guest mode.
            dark_mode (bool):  Enable Chromium's Dark mode.
            devtools (bool):  Open Chromium's DevTools when the browser opens.
            remote_debug (bool):  Enable Chrome's Debugger on "http://localhost:9222".
            enable_3d_apis (bool):  Enable WebGL and 3D APIs.
            swiftshader (bool):  Chrome: --use-gl=angle / --use-angle=swiftshader-webgl
            ad_block_on (bool):  Block some types of display ads from loading.
            host_resolver_rules (str):  Set host-resolver-rules, comma-separated.
            block_images (bool):  Block images from loading during tests.
            do_not_track (bool):  Tell websites that you don't want to be tracked.
            chromium_arg (str):  "ARG=N,ARG2" (Set Chromium args, ","-separated.)
            firefox_arg (str):  "ARG=N,ARG2" (Set Firefox args, comma-separated.)
            firefox_pref (str):  SET (Set Firefox PREFERENCE:VALUE set, ","-separated)
            user_data_dir (str):  Set the Chrome user data directory to use.
            extension_zip (str):  Load a Chrome Extension .zip|.crx, comma-separated.
            extension_dir (str):  Load a Chrome Extension directory, comma-separated.
            disable_features (str):  "F1,F2" (Disable Chrome features, ","-separated.)
            binary_location (str):  Set path of the Chromium browser binary to use.
            driver_version (str):  Set the chromedriver or uc_driver version to use.
            skip_js_waits (bool):  Skip JS Waits (readyState=="complete" and Angular).
            wait_for_angularjs (bool):  Wait for AngularJS to load after some actions.
            use_wire (bool):  Use selenium-wire's webdriver over selenium webdriver.
            external_pdf (bool):  Set Chrome "plugins.always_open_pdf_externally":True.
            window_position (x,y):  Set the browser's starting window position: "X,Y"
            window_size (w,h):  Set the browser's starting window size: "Width,Height"
            is_mobile (bool):  Use the mobile device emulator while running tests.
            mobile (bool):  Shortcut / Duplicate of "is_mobile".
            device_metrics (w,h,pr):  Mobile metrics: "CSSWidth,CSSHeight,PixelRatio"
            xvfb (bool):  Run tests using the Xvfb virtual display server on Linux OS.
            xvfb_metrics (w,h):  Set Xvfb display size on Linux: "Width,Height".
            start_page (str):  The starting URL for the web browser when tests begin.
            rec_print (bool):  If Recorder is enabled, prints output after tests end.
            rec_behave (bool):  Like Recorder Mode, but also generates behave-gherkin.
            record_sleep (bool):  If Recorder enabled, also records self.sleep calls.
            data (str):  Extra test data. Access with "self.data" in tests.
            var1 (str):  Extra test data. Access with "self.var1" in tests.
            var2 (str):  Extra test data. Access with "self.var2" in tests.
            var3 (str):  Extra test data. Access with "self.var3" in tests.
            variables (dict):  Extra test data. Access with "self.variables".
            account (str):  Set account. Access with "self.account" in tests.
            environment (str):  Set the test env. Access with "self.env" in tests.
            headed (bool):  Run tests in headed/GUI mode on Linux, where not default.
            maximize (bool):  Start tests with the browser window maximized.
            disable_ws (bool):  Reverse of "enable_ws". (None and False are different)
            disable_beforeunload (bool):  Disable the "beforeunload" event on Chromium.
            settings_file (str):  A file for overriding default SeleniumBase settings.
            position (x,y):  Shortcut / Duplicate of "window_position".
            size (w,h):  Shortcut / Duplicate of "window_size".
            uc (bool):  Shortcut / Duplicate of "undetectable".
            undetected (bool):  Shortcut / Duplicate of "undetectable".
            uc_cdp (bool):  Shortcut / Duplicate of "uc_cdp_events".
            uc_sub (bool):  Shortcut / Duplicate of "uc_subprocess".
            locale (str):  Shortcut / Duplicate of "locale_code".
            log_cdp (bool):  Shortcut / Duplicate of "log_cdp_events".
            ad_block (bool):  Shortcut / Duplicate of "ad_block_on".
            server (str):  Shortcut / Duplicate of "servername".
            guest (bool):  Shortcut / Duplicate of "guest_mode".
            wire (bool):  Shortcut / Duplicate of "use_wire".
            pls (str):  Shortcut / Duplicate of "page_load_strategy".
            sjw (bool):  Shortcut / Duplicate of "skip_js_waits".
            wfa (bool):  Shortcut / Duplicate of "wait_for_angularjs".
            save_screenshot (bool):  Save a screenshot at the end of each test.
            no_screenshot (bool):  No screenshots saved unless tests directly ask it.
            page_load_strategy (str):  Set Chrome PLS to "normal", "eager", or "none".
            timeout_multiplier (float):  Multiplies the default timeout values.
            js_checking_on (bool):  Check for JavaScript errors after page loads.
            slow (bool):  Slow down the automation. Faster than using Demo Mode.
            demo (bool):  Slow down and visually see test actions as they occur.
            demo_sleep (float):  SECONDS (Set wait time after Slow & Demo Mode actions)
            message_duration (float):  SECONDS (The time length for Messenger alerts.)
            highlights (int):  Number of highlight animations for Demo Mode actions.
            interval (float):  SECONDS (Autoplay interval for SB Slides & Tour steps.)
            time_limit (float):  SECONDS (Safely fail tests that exceed the time limit)
        """

        self._sb_context = SB(
            test=test,
            rtf=rtf,
            raise_test_failure=raise_test_failure,
            browser=browser,
            headless=headless,
            headless1=headless1,
            headless2=headless2,
            locale_code=locale_code,
            protocol=protocol,
            servername=servername,
            port=port,
            proxy=proxy,
            proxy_bypass_list=proxy_bypass_list,
            proxy_pac_url=proxy_pac_url,
            multi_proxy=multi_proxy,
            agent=agent,
            cap_file=cap_file,
            cap_string=cap_string,
            recorder_ext=recorder_ext,
            disable_cookies=disable_cookies,
            disable_js=disable_js,
            disable_csp=disable_csp,
            enable_ws=enable_ws,
            enable_sync=enable_sync,
            use_auto_ext=use_auto_ext,
            undetectable=undetectable,
            uc_cdp_events=uc_cdp_events,
            uc_subprocess=uc_subprocess,
            log_cdp_events=log_cdp_events,
            incognito=incognito,
            guest_mode=guest_mode,
            dark_mode=dark_mode,
            devtools=devtools,
            remote_debug=remote_debug,
            enable_3d_apis=enable_3d_apis,
            swiftshader=swiftshader,
            ad_block_on=ad_block_on,
            host_resolver_rules=host_resolver_rules,
            block_images=block_images,
            do_not_track=do_not_track,
            chromium_arg=chromium_arg,
            firefox_arg=firefox_arg,
            firefox_pref=firefox_pref,
            user_data_dir=user_data_dir,
            extension_zip=extension_zip,
            extension_dir=extension_dir,
            disable_features=disable_features,
            binary_location=binary_location,
            driver_version=driver_version,
            skip_js_waits=skip_js_waits,
            wait_for_angularjs=wait_for_angularjs,
            use_wire=use_wire,
            external_pdf=external_pdf,
            window_position=window_position,
            window_size=window_size,
            is_mobile=is_mobile,
            mobile=mobile,
            device_metrics=device_metrics,
            xvfb=xvfb,
            xvfb_metrics=xvfb_metrics,
            start_page=start_page,
            rec_print=rec_print,
            rec_behave=rec_behave,
            record_sleep=record_sleep,
            data=data,
            var1=var1,
            var2=var2,
            var3=var3,
            variables=variables,
            account=account,
            environment=environment,
            headed=headed,
            maximize=maximize,
            disable_ws=disable_ws,
            disable_beforeunload=disable_beforeunload,
            settings_file=settings_file,
            position=position,
            size=size,
            uc=uc,
            undetected=undetected,
            uc_cdp=uc_cdp,
            uc_sub=uc_sub,
            locale=locale,
            log_cdp=log_cdp,
            ad_block=ad_block,
            server=server,
            guest=guest,
            wire=wire,
            pls=pls,
            sjw=sjw,
            wfa=wfa,
            cft=cft,
            chs=chs,
            save_screenshot=save_screenshot,
            no_screenshot=no_screenshot,
            page_load_strategy=page_load_strategy,
            timeout_multiplier=timeout_multiplier,
            js_checking_on=js_checking_on,
            slow=slow,
            demo=demo,
            demo_sleep=demo_sleep,
            message_duration=message_duration,
            highlights=highlights,
            interval=interval,
            time_limit=time_limit,
            **kwargs,
        )
        self.sb = None
        self.cdp: Optional[CDPInterface] = None
        self.driver: Optional[DriverInterface] = None

    def __enter__(self) -> "UC":
        """Enter the context manager and initialize SeleniumBase instance."""
        self.sb = self._sb_context.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager and clean up resources."""
        return self._sb_context.__exit__(exc_type, exc_val, exc_tb)

    def activate_cdp_mode(self, url: Optional[str] = None) -> "UC":
        """Activate the Chrome DevTools Protocol (CDP) mode.

        Args:
            url (str, optional): The starting URL for CDP mode.
        Returns:
            SeleniumCDP: The current instance with CDP enabled.
        """
        self.sb.activate_cdp_mode(url)
        self.cdp = CDPWrapper(self.sb.cdp)
        self.driver = DriverWrapper(self.sb)
        return self

    open = activate_cdp_mode
    get = activate_cdp_mode

    def __getattr__(self, name: str) -> Any:
        """Delegate attribute access to SeleniumBase instance if available."""
        if self.sb:
            return getattr(self.sb, name)
        raise AttributeError(f"'{self.__class__.__name__}' has no attribute '{name}'")
