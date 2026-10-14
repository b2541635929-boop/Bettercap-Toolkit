GUIDANCE = (
    "Proxy inspection requires a deliberately configured lab client and certificate trust. "
    "This toolkit does not silently install certificates or intercept credentials. "
    "Review Bettercap's current proxy module help before enabling any proxy functionality."
)
def proxy_guidance() -> str:
    return GUIDANCE
