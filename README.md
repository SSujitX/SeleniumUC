# SeleniumUC 🚀

SeleniumUC is a Python package built on top of [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) that focuses on auto-completion and bypassing bot-detection using undetected-chromedriver (UC) CDP methods. This package leverages the powerful features of SeleniumBase while providing enhanced capabilities for undetected automation.

## Features ✨

- Auto-completion for Seleniumbase methods.
- Bypass bot-detection using undetected-chromedriver (UC).
- Extensive options for browser configuration and customization.

## Installation 📦

To install SeleniumUC, simply use pip:

```bash
pip install SeleniumUC
```

## Usage 🛠️

Here's a quick example to get you started with SeleniumUC:

```python
from SeleniumUC import UC

with UC(
    uc=True,
    test=True,
    maximize=True,
) as sb:
    sb.activate_cdp_mode("https://signup.cloud.oracle.com/")
    sb.cdp.sleep(2)
```

## More Information 📚

For more advanced usage and features, refer to the [SeleniumBase documentation](https://github.com/seleniumbase/SeleniumBase).

### SeleniumBase Method Summary

For a comprehensive list of SeleniumBase methods, visit the [SeleniumBase Methods API Reference](https://seleniumbase.io/help_docs/method_summary/#seleniumbase-methods-api-reference).

### CDP Mode Usage

To learn more about using CDP mode with SeleniumBase, check out the [CDP Mode Usage Guide](https://seleniumbase.io/examples/cdp_mode/ReadMe/#cdp-mode-usage).

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing 🤝

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

Happy Testing! 🎉
