// When a visitor's photograph was sent (Kit/SentAgo.swift, 2026-11-20): the
// server's timestamp reads with Postgres's six fractional digits, a recent
// one prints as a span, an old one as month and year, and nothing prints
// without a time (photo_authors before photo-authors-time.sql is pasted).

import Testing
import Foundation
@testable import AncientTrees

struct SentAgoTests {
    let now = SentAgo.date("2026-11-20T16:00:00+00:00")!

    @Test func readsPostgresTimestamps() {
        #expect(SentAgo.date("2026-11-20T14:21:05.629106+00:00") != nil)
        #expect(SentAgo.date("2026-11-20T14:21:05+00:00") != nil)
        #expect(SentAgo.date("") == nil)
        #expect(SentAgo.date(nil) == nil)
    }

    @Test func recentIsASpanOldIsAMonth() {
        let twoHours = SentAgo.short("2026-11-20T14:00:00.000000+00:00", now: now)
        #expect(twoHours != nil)
        #expect(twoHours!.contains("2"))
        let longTwo = SentAgo.long("2026-11-20T14:00:00+00:00", now: now)
        #expect(longTwo != nil && longTwo!.contains("2"))
        let old = SentAgo.short("2026-09-01T10:00:00+00:00", now: now)
        #expect(old != nil && old!.contains("2026"))
    }

    @Test func noTimeNoText() {
        #expect(SentAgo.short(nil, now: now) == nil)
        #expect(SentAgo.long("not a date", now: now) == nil)
    }
}
