from summarizer import summarize_text

def test_summary_response():
    sample_text = """Artificial Intelligence (AI) is the simulation of human intelligence processes by machines,
    especially computer systems. These processes include learning, reasoning, and self-correction."""
    summary = summarize_text(sample_text)
    assert isinstance(summary, str)
    assert len(summary) > 0