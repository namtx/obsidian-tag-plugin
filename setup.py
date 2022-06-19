from setuptools import setup, find_packages

setup(
  name='mkdocs-obsidian-tag-plugin',
  version='0.0.1',
  description='A simple plugin to enable Obsidian tag feature on mkdocs',
  author='Tran Xuan Nam',
  author_email='namtx.93@gmail.com',
  license='MIT',
  install_requires=["mkdocs"],
  packages=find_packages(),
  entry_points={
    'mkdocs.plugins': [
      'mkdocs-obsidian-tag-plugin = mkdocs_obsidian_tag_plugin.plugin:MkdocsObsidianTagPlugin',
    ]
  }
)
