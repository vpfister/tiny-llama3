"""Sphinx configuration."""

project = "tiny_llama3"
author = "Vincent Pfister"
copyright = "2024, Vincent Pfister"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
