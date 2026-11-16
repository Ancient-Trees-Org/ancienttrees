package app.ancienttrees.account

/**
 * "DID YOU MEAN ...?" UNDER THE EMAIL FIELD (Hidde, 2026-11-16: "can we give a
 * warning before sending"; CONVENTIONS.md "A mistyped email address").
 *
 * Kit/EmailSuggest.swift ported line for line, and the website's rule
 * (site/src/lib/email-suggest.ts): unknown domain, the nearest listed one by
 * edit distance, at most 2 apart (1 for six letters or fewer), never on a tie.
 * The list is data/email-domains.json, copied in below; qa's
 * check_one_email_domain_list() fails a push when the copies differ.
 */
object EmailSuggest {
    // DOMAINS-BEGIN
    val DOMAINS = listOf(
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
    )
    // DOMAINS-END

    /** The corrected address, or null. */
    fun suggestion(raw: String): String? {
        val addr = raw.trim()
        val at = addr.lastIndexOf('@')
        if (at < 1 || at == addr.length - 1) return null
        val local = addr.substring(0, at)
        val domain = addr.substring(at + 1).lowercase()
        if (domain in DOMAINS) return null
        var best: String? = null
        var bestDistance = Int.MAX_VALUE
        var tie = false
        for (candidate in DOMAINS) {
            val d = distance(domain, candidate)
            if (d < bestDistance) { bestDistance = d; best = candidate; tie = false }
            else if (d == bestDistance) tie = true
        }
        val limit = if (domain.length <= 6) 1 else 2
        if (best == null || tie || bestDistance > limit) return null
        return "$local@$best"
    }

    /** Levenshtein distance, the same as the website's dist(). */
    fun distance(a: String, b: String): Int {
        if (a.isEmpty()) return b.length
        if (b.isEmpty()) return a.length
        var prev = IntArray(b.length + 1) { it }
        for (i in 1..a.length) {
            val cur = IntArray(b.length + 1)
            cur[0] = i
            for (j in 1..b.length) {
                cur[j] = minOf(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + if (a[i - 1] == b[j - 1]) 0 else 1)
            }
            prev = cur
        }
        return prev[b.length]
    }
}
