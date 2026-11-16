import Foundation

/// "DID YOU MEAN ...?" UNDER THE EMAIL FIELD (Hidde, 2026-11-16: "can we give
/// a warning before sending"; CONVENTIONS.md "A mistyped email address").
///
/// The Guardian weekend's sign-up mails bounced on addresses typed a letter
/// off (outlook.co for outlook.com). The mailcheck.js convention: when the part
/// after the @ is one or two edits from a provider people actually use, offer
/// the corrected address, and a tap puts it in. It never refuses an address.
///
/// The same rule as the website (site/src/lib/email-suggest.ts) and Android
/// (account/EmailSuggest.kt): unknown domain, the nearest listed one by edit
/// distance, at most 2 apart (1 for six letters or fewer), never on a tie. The
/// list is data/email-domains.json, copied in below; qa's
/// check_one_email_domain_list() fails a push when the copies differ.
enum EmailSuggest {
    // DOMAINS-BEGIN
    static let domains: [String] = [
        "gmail.com", "googlemail.com", "outlook.com", "outlook.fr", "outlook.de", "outlook.es",
        "outlook.it", "outlook.pt", "hotmail.com", "hotmail.co.uk", "hotmail.fr", "hotmail.de",
        "hotmail.es", "hotmail.it", "hotmail.nl", "hotmail.be", "live.com", "live.co.uk",
        "live.nl", "live.fr", "live.be", "msn.com", "yahoo.com", "yahoo.co.uk", "yahoo.fr",
        "yahoo.de", "yahoo.es", "yahoo.it", "yahoo.gr", "yahoo.com.au", "ymail.com",
        "rocketmail.com", "icloud.com", "me.com", "mac.com", "aol.com", "aol.co.uk",
        "protonmail.com", "proton.me", "pm.me", "gmx.com", "gmx.de", "gmx.net", "gmx.at", "gmx.ch",
        "web.de", "t-online.de", "freenet.de", "mail.com", "zoho.com", "fastmail.com",
        "btinternet.com", "sky.com", "virginmedia.com", "talktalk.net", "ntlworld.com", "ziggo.nl",
        "kpnmail.nl", "xs4all.nl", "planet.nl", "home.nl", "hetnet.nl", "telenet.be", "skynet.be",
        "orange.fr", "free.fr", "laposte.net", "sfr.fr", "wanadoo.fr", "libero.it", "tiscali.it",
        "virgilio.it", "alice.it", "sapo.pt", "telefonica.net", "comcast.net", "verizon.net",
        "att.net", "sbcglobal.net", "bellsouth.net", "cox.net", "charter.net", "bigpond.com",
        "optusnet.com.au", "shaw.ca", "rogers.com", "sympatico.ca", "naver.com", "qq.com",
        "163.com", "yandex.com"
    ]
    // DOMAINS-END

    /// The corrected address, or nil.
    static func suggestion(for raw: String) -> String? {
        let addr = raw.trimmingCharacters(in: .whitespacesAndNewlines)
        guard let at = addr.lastIndex(of: "@"), at != addr.startIndex,
              addr.index(after: at) != addr.endIndex else { return nil }
        let local = String(addr[..<at])
        let domain = String(addr[addr.index(after: at)...]).lowercased()
        if domains.contains(domain) { return nil }
        var best: String?
        var bestDistance = Int.max
        var tie = false
        for candidate in domains {
            let d = distance(domain, candidate)
            if d < bestDistance { bestDistance = d; best = candidate; tie = false }
            else if d == bestDistance { tie = true }
        }
        let limit = domain.count <= 6 ? 1 : 2
        guard let best, !tie, bestDistance <= limit else { return nil }
        return local + "@" + best
    }

    /// Levenshtein distance, the same as the website's dist().
    static func distance(_ a: String, _ b: String) -> Int {
        let a = Array(a), b = Array(b)
        if a.isEmpty { return b.count }
        if b.isEmpty { return a.count }
        var prev = Array(0...b.count)
        for i in 1...a.count {
            var cur = [i] + Array(repeating: 0, count: b.count)
            for j in 1...b.count {
                cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] == b[j - 1] ? 0 : 1))
            }
            prev = cur
        }
        return prev[b.count]
    }
}
