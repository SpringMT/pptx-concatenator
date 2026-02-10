"""
Unit tests for pptx_concatenator module.
"""

from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

from pptx_concatenator import PptxConcatenator, concat_pptx


class TestPptxConcatenator:
    """Test cases for PptxConcatenator class."""

    @patch('pptx_concatenator.concatenator.Presentation')
    @patch('pptx_concatenator.concatenator.SlideCopier')
    def test_concat_with_file_paths(self, mock_copier, mock_presentation):
        """Test concatenation with file path arguments."""
        # Setup mocks
        mock_src = MagicMock()
        mock_target = MagicMock()
        mock_target.slides = [Mock(), Mock(), Mock()]  # 3 slides
        mock_presentation.side_effect = [mock_src, mock_target]

        # Execute
        result = PptxConcatenator.concat("src.pptx", "target.pptx", "output.pptx")

        # Verify
        assert mock_presentation.call_count == 2
        mock_presentation.assert_any_call("src.pptx")
        mock_presentation.assert_any_call("target.pptx")
        assert mock_copier.copy_slide.call_count == 3
        mock_src.save.assert_called_once_with("output.pptx")
        assert result == mock_src

    @patch('pptx_concatenator.concatenator.SlideCopier')
    def test_concat_with_presentation_objects(self, mock_copier):
        """Test concatenation with Presentation object arguments."""
        # Setup mocks
        mock_src = MagicMock()
        mock_target = MagicMock()
        mock_target.slides = [Mock(), Mock()]  # 2 slides

        # Execute
        result = PptxConcatenator.concat(mock_src, mock_target)

        # Verify
        assert mock_copier.copy_slide.call_count == 2
        mock_copier.copy_slide.assert_any_call(mock_target, 0, mock_src)
        mock_copier.copy_slide.assert_any_call(mock_target, 1, mock_src)
        assert result == mock_src

    @patch('pptx_concatenator.concatenator.SlideCopier')
    def test_concat_without_output_path(self, mock_copier):
        """Test concatenation without saving to file."""
        # Setup mocks
        mock_src = MagicMock()
        mock_target = MagicMock()
        mock_target.slides = [Mock()]

        # Execute
        result = PptxConcatenator.concat(mock_src, mock_target)

        # Verify
        mock_src.save.assert_not_called()
        assert result == mock_src

    @patch('pptx_concatenator.concatenator.Presentation')
    @patch('pptx_concatenator.concatenator.SlideCopier')
    def test_concat_multiple_with_file_paths(self, mock_copier, mock_presentation):
        """Test concatenation of multiple files."""
        # Setup mocks
        mock_src = MagicMock()
        mock_target1 = MagicMock()
        mock_target2 = MagicMock()
        mock_target1.slides = [Mock(), Mock()]  # 2 slides
        mock_target2.slides = [Mock()]  # 1 slide
        mock_presentation.side_effect = [mock_src, mock_target1, mock_target2]

        # Execute
        result = PptxConcatenator.concat_multiple(
            "src.pptx",
            ["target1.pptx", "target2.pptx"],
            "output.pptx"
        )

        # Verify
        assert mock_presentation.call_count == 3
        assert mock_copier.copy_slide.call_count == 3  # 2 + 1 slides
        mock_src.save.assert_called_once_with("output.pptx")
        assert result == mock_src

    @patch('pptx_concatenator.concatenator.SlideCopier')
    def test_concat_multiple_with_presentation_objects(self, mock_copier):
        """Test concatenation of multiple Presentation objects."""
        # Setup mocks
        mock_src = MagicMock()
        mock_target1 = MagicMock()
        mock_target2 = MagicMock()
        mock_target1.slides = [Mock()]
        mock_target2.slides = [Mock()]

        # Execute
        result = PptxConcatenator.concat_multiple(
            mock_src,
            [mock_target1, mock_target2]
        )

        # Verify
        assert mock_copier.copy_slide.call_count == 2
        mock_src.save.assert_not_called()
        assert result == mock_src

    @patch('pptx_concatenator.concatenator.SlideCopier')
    def test_concat_multiple_empty_targets(self, mock_copier):
        """Test concatenation with empty targets list."""
        # Setup mocks
        mock_src = MagicMock()

        # Execute
        result = PptxConcatenator.concat_multiple(mock_src, [])

        # Verify
        mock_copier.copy_slide.assert_not_called()
        assert result == mock_src

    @patch('pptx_concatenator.concatenator.SlideCopier')
    def test_concat_with_pathlib_path(self, mock_copier):
        """Test concatenation with pathlib.Path objects."""
        # Setup mocks
        with patch('pptx_concatenator.concatenator.Presentation') as mock_presentation:
            mock_src = MagicMock()
            mock_target = MagicMock()
            mock_target.slides = [Mock()]
            mock_presentation.side_effect = [mock_src, mock_target]

            # Execute
            result = PptxConcatenator.concat(
                Path("src.pptx"),
                Path("target.pptx"),
                Path("output.pptx")
            )

            # Verify
            mock_presentation.assert_any_call("src.pptx")
            mock_presentation.assert_any_call("target.pptx")
            mock_src.save.assert_called_once_with("output.pptx")
            assert result == mock_src


class TestConcatPptxFunction:
    """Test cases for concat_pptx convenience function."""

    @patch('pptx_concatenator.PptxConcatenator.concat')
    def test_concat_pptx_calls_concatenator(self, mock_concat):
        """Test that concat_pptx calls PptxConcatenator.concat."""
        # Execute
        concat_pptx("src.pptx", "target.pptx", "output.pptx")

        # Verify
        mock_concat.assert_called_once_with("src.pptx", "target.pptx", "output.pptx")
