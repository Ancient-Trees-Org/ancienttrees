"""A reply that comes as HTML only is read, not "(no plain-text part)"
(2026-11-27, feedback 1715: a reader's question about ambassadors never
reached the digest)."""
import os
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from outreach_inbox import body_of  # noqa: E402


def test_html_only_multipart():
    m = MIMEMultipart("alternative")
    m.attach(MIMEText("<div>What is the role of the ambassador&nbsp;?</div><br><p>Andrea</p>", "html"))
    out = body_of(m)
    assert "What is the role of the ambassador ?" in out, out
    assert "<" not in out, out


def test_plain_still_wins():
    m = MIMEMultipart("alternative")
    m.attach(MIMEText("plain words", "plain"))
    m.attach(MIMEText("<p>html words</p>", "html"))
    assert body_of(m) == "plain words"


def test_html_single_part():
    assert body_of(MIMEText("<p>Hello <b>there</b></p>", "html")) == "Hello there"


if __name__ == "__main__":
    test_html_only_multipart()
    test_plain_still_wins()
    test_html_single_part()
    print("ok")
