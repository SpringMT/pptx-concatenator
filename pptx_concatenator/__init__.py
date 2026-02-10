"""
PowerPoint concatenation library using pptx-slide-copier.
Concatenates multiple PPTX files by appending target slides to source presentation.
"""

from pptx_concatenator.concatenator import PptxConcatenator, concat_pptx

__all__ = ["PptxConcatenator", "concat_pptx"]
