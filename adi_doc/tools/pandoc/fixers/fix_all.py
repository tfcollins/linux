import logging

all_logger = logging.getLogger("fix_all")



def run_all_fixers(text, target_dir, to_skip=None):

    if not isinstance(to_skip, list):
        to_skip = [to_skip]

    # Conditional import necessary to avoid circular imports

    if "process" not in to_skip:
        from .fixup_wrap_tags import preprocess, process
        preprocess(text)
        text = process(text)

    if "adjust_heading" not in to_skip:
        from .heading_fixup import adjust_heading
        text = adjust_heading(text)

    if "update_xterm_blocks" not in to_skip:
        from .fixup_term_tags import update_xterm_blocks
        text = update_xterm_blocks(text)

    if "update_graphviz_blocks" not in to_skip:
        from .fixup_graphviz_tags import update_graphviz_blocks
        text = update_graphviz_blocks(text)

    if "fixup_images" not in to_skip:
        from .fixup_images import fixup_images
        text = fixup_images(text, target_dir)

    if "fix_poor_formatting" not in to_skip:
        from .fix_poor_formatting import fix_poor_formatting
        text = fix_poor_formatting(text)

    if "fix_includes" not in to_skip:
        from .fix_includes import fix_includes
        text = fix_includes(text, target_dir)

    return text