import re
from mkdocs.plugins import BasePlugin

class MkdocsObsidianTagPlugin(BasePlugin):
  def __init__(self):
    super().__init__

  def on_page_markdown(self, markdown, **kwargs):
    def repl(var):
      return "[#" + var.group()[1:] + "]" + "(/tags/" + var.group()[1:] + ")"

    copy = markdown
    return re.sub("\#\w+\-*\_*\w+", repl, copy)
