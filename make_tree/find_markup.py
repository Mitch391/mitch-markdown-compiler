def find_all_first_spans(text, track_node):
    all_first_spans = []
    found_bold = track_node.check_for_bold_in_text(text)
    found_horizontal_rule = track_node.check_for_horizontal_rule(text)
    if found_bold:
        found = found_bold + ("bold",)
        all_first_spans.append(found)
    if found_horizontal_rule:
        found = found_horizontal_rule + ("horizontal_rule",)
        all_first_spans.append(found)

    return all_first_spans


def compare_spans(found_span_array):
    if not found_span_array:
        return ()
    curr_first_span = found_span_array[0]
    for found in found_span_array:
        if found[0] < curr_first_span[0]:
            curr_first_span = found
    return curr_first_span

def find_first_markup_in_text(track_node, curr_node):
    text = curr_node.get_text()
    all_first_spans = find_all_first_spans(text, track_node)
    first_span = compare_spans(all_first_spans)
    if first_span == ():
        return False, None, None

    return True, curr_node, first_span
