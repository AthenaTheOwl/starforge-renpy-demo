## bee_protocol.rpy — BEE protocol text parser and formatter
##
## Parses {BEE:: message | STATUS: x | DETAIL: y} format from dialogue JSON.

init python:
    import re as _re

    _BEE_PATTERN = _re.compile(r'\{BEE::\s*(.+?)\}')

    def parse_bee_protocol(text):
        """Parse {BEE:: msg | STATUS | DETAIL} into structured dict.
        Returns None if no BEE protocol found."""
        match = _BEE_PATTERN.search(text)
        if not match:
            return None
        inner = match.group(1)
        parts = [p.strip() for p in inner.split("|")]
        return {
            "message": parts[0] if len(parts) > 0 else "",
            "status": parts[1] if len(parts) > 1 else "",
            "detail": parts[2] if len(parts) > 2 else "",
            "raw": match.group(0),
        }

    def has_bee_protocol(text):
        """Check if text contains a BEE protocol block."""
        return "{BEE::" in text

    def strip_bee_protocol(text):
        """Remove BEE protocol tags from text for clean display."""
        return _BEE_PATTERN.sub('', text).strip()

    def format_bee_for_display(text):
        """Format BEE protocol text with styling tags for Ren'Py display."""
        parsed = parse_bee_protocol(text)
        if not parsed:
            return text
        # Format as styled monospace-looking block
        lines = []
        if parsed["message"]:
            lines.append(parsed["message"])
        if parsed["status"]:
            lines.append(parsed["status"])
        if parsed["detail"]:
            lines.append(parsed["detail"])
        return "{color=#f1c40f}{size=-2}" + " | ".join(lines) + "{/size}{/color}"
