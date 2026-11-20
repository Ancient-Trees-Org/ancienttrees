// WHEN A VISITOR'S PHOTOGRAPH WAS SENT (Hidde, 2026-11-20: "aangeven hoelaat
// iets is gepost, om het platform meer actueel te maken"; "A, met boomnaam";
// CONVENTIONS.md "A heart for a visitor's photograph ... who and when on it").
// The website's lib/time-ago-js.ts in Swift, so the three surfaces print the
// same thing: short on a tile ("2h", "3d", Instagram's way), written out under
// the hero and in the opened photograph ("2 hours ago"), and month and year
// after four weeks ("Oct 2026", the way Google Maps dates a photograph). The
// system's formatters do the words in the phone's language. The time is the
// server's published_at, when it was sent, never when it was taken.
import Foundation

enum SentAgo {
    /// "2h", "3d", "1w"; "Oct 2026" after four weeks; nil without a time.
    static func short(_ iso: String?, now: Date = Date()) -> String? {
        guard let d = date(iso) else { return nil }
        if let month = old(d, now) { return month }
        let (unit, n) = unit(d, now)
        let f = DateComponentsFormatter()
        f.unitsStyle = .abbreviated
        switch unit {
        case .minute: f.allowedUnits = [.minute]
        case .hour: f.allowedUnits = [.hour]
        case .day: f.allowedUnits = [.day]
        default: f.allowedUnits = [.weekOfMonth]
        }
        f.maximumUnitCount = 1
        var c = DateComponents()
        c.setValue(n, for: unit)
        return f.string(from: c)
    }

    /// "2 hours ago", "3 days ago"; "Oct 2026" after four weeks.
    static func long(_ iso: String?, now: Date = Date()) -> String? {
        guard let d = date(iso) else { return nil }
        if let month = old(d, now) { return month }
        let (unit, n) = unit(d, now)
        let f = RelativeDateTimeFormatter()
        f.unitsStyle = .full
        f.dateTimeStyle = .numeric
        var c = DateComponents()
        c.setValue(-n, for: unit)
        return f.localizedString(from: c)
    }

    private static func old(_ d: Date, _ now: Date) -> String? {
        now.timeIntervalSince(d) >= 28 * 86400 ? d.formatted(.dateTime.month(.abbreviated).year()) : nil
    }

    private static func unit(_ d: Date, _ now: Date) -> (Calendar.Component, Int) {
        let s = max(0, now.timeIntervalSince(d))
        if s < 3600 { return (.minute, max(1, Int(s / 60))) }
        if s < 86400 { return (.hour, Int(s / 3600)) }
        if s < 7 * 86400 { return (.day, Int(s / 86400)) }
        return (.weekOfMonth, Int(s / (7 * 86400)))
    }

    static func date(_ iso: String?) -> Date? {
        guard let iso, !iso.isEmpty else { return nil }
        let f = ISO8601DateFormatter()
        f.formatOptions = [.withInternetDateTime, .withFractionalSeconds]
        if let d = f.date(from: iso) { return d }
        // Postgres sends six fractional digits ("…05.629106+00:00"); without
        // them the plain form reads it to the second, which is all we print.
        f.formatOptions = [.withInternetDateTime]
        let plain = iso.replacingOccurrences(of: #"\.\d+"#, with: "", options: .regularExpression)
        return f.date(from: plain)
    }
}
