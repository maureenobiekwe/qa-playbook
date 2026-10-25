# Public forms (anyone can submit)

- Which fields are required? The asterisks, the error messages and the API must agree.
- Spam: captcha or similar, rate limit. Many people share one mobile-network IP address, so a strict per-IP limit can block real users.
- Duplicate submission: what does a returning person see? "You already applied" reveals who applied.
- Input safety: HTML and script in text fields, very long text, emoji, right-to-left text.
- Phone and address formats for people outside the main country.
- Consent: wording, version stored with the submission, link to the privacy notice.
- Open and close dates: which date closes the form, in which time zone, to the minute?
- Confirmation: on-screen message and email, and what happens if the email fails.
- Load: peak simultaneous submissions; what the user sees when the service is slow.
- Embedding on another site: framing, cross-origin requests and content security policy.
- Accessibility: labels, error association, keyboard-only completion, mobile keyboards.
- What the public response must not contain: counts, internal ids, prices, other people's data.
