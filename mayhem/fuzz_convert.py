#! /usr/bin/env python3
import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(include=['markdown_it']):
    import markdown_it
    import markdown_it.tree

def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    md = markdown_it.MarkdownIt().enable('table').enable('image')
    text = fdp.ConsumeRemainingString()
    if fdp.ConsumeBool():
        tokens = md.parse(text)
        markdown_it.tree.SyntaxTreeNode(tokens)
    else:
        md.render(text)
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
