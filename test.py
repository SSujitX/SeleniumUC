from SeleniumUC import UC

with UC(
    uc=True,
    test=True,
    maximize=True,
) as sb:
    sb.activate_cdp_mode("https://signup.cloud.oracle.com/")
    sb.cdp.sleep(2)
    sb.cdp.save_cookies("cookies.json")
    sb.cdp.sleep(5)
