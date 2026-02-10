"""Command-line interface for pptx-concatenator."""

import argparse
import sys
from pathlib import Path

from pptx_concatenator import PptxConcatenator


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Concatenate PowerPoint presentations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Concatenate two presentations
  pptx-concat source.pptx target.pptx -o output.pptx

  # Concatenate multiple presentations
  pptx-concat source.pptx file1.pptx file2.pptx file3.pptx -o output.pptx
        """,
    )

    parser.add_argument("source", help="Source PPTX file (base presentation)")
    parser.add_argument("targets", nargs="+", help="Target PPTX file(s) to append")
    parser.add_argument(
        "-o", "--output", required=True, help="Output PPTX file path"
    )

    args = parser.parse_args()

    # Validate input files
    source_path = Path(args.source)
    if not source_path.exists():
        print(f"Error: Source file '{args.source}' not found", file=sys.stderr)
        sys.exit(1)

    for target in args.targets:
        target_path = Path(target)
        if not target_path.exists():
            print(f"Error: Target file '{target}' not found", file=sys.stderr)
            sys.exit(1)

    # Perform concatenation
    try:
        if len(args.targets) == 1:
            print(f"Concatenating {args.source} + {args.targets[0]}...")
            PptxConcatenator.concat(args.source, args.targets[0], args.output)
        else:
            print(f"Concatenating {args.source} + {len(args.targets)} files...")
            PptxConcatenator.concat_multiple(args.source, args.targets, args.output)

        print(f"Successfully created: {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
