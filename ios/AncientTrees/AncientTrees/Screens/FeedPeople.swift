// PEOPLE YOU MAY KNOW, in the Feed (Hidde, 2026-11-26: the feed is there to
// get people following each other, "het hartjes geven, het volgen van
// mensen"; his Polarsteps screenshots, Activity's "Mensen die je misschien
// kent").
//
// Convention: Polarsteps' Activity row, as on his screenshot, which is also
// Instagram's "Suggested for you" in the feed: a row of cards that scrolls
// sideways, each a big round face, the name, one line why, a filled Follow
// button and an X top right that takes the card away; "See all" goes to the
// full list (our Find people). Signed in only: names and the follow graph are
// (CLAUDE.md, Privacy and accounts). Who comes from what Find people already
// suggests (Kit/SuggestedPeople.swift); a card taken away is gone for this
// opening only, nothing kept on the device (hard rule 11).
import SwiftUI

struct FeedPeopleRow: View {
    @Environment(Account.self) private var account
    @Environment(Profiles.self) private var profiles
    @Environment(Navigator.self) private var navigator
    @Environment(Moderation.self) private var moderation

    /// Whom you follow already, so nobody you follow is suggested.
    let following: Set<String>

    @State private var people: [SuggestedPerson] = []
    @State private var gone: Set<String> = []
    @State private var followed: Set<String> = []

    private static let cardWidth: CGFloat = 164

    var body: some View {
        let shown = people.filter { !gone.contains($0.profile.user_id) }
        // A stack that is always there, so its task runs before it has
        // anybody to show (an empty Group never appears, and never loads).
        VStack(spacing: 0) {
            if !shown.isEmpty {
                VStack(alignment: .leading, spacing: 12) {
                    ShelfHeader(title: "People you may know", seeAll: { navigator.push = .findPeople })
                        .padding(.horizontal, -16)
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: 12) {
                            ForEach(shown, id: \.profile.user_id) { card($0) }
                        }
                        .padding(.horizontal, 16)
                    }
                    .padding(.horizontal, -16)
                }
                .accessibilityElement(children: .contain)
                .accessibilityIdentifier("feed-people")
            }
        }
        .task(id: account.session?.userId) { await load() }
    }

    private func card(_ s: SuggestedPerson) -> some View {
        let p = s.profile
        let on = followed.contains(p.user_id)
        return VStack(spacing: 6) {
            Button { navigator.push = .person(p.user_id) } label: {
                VStack(spacing: 10) {
                    face(p).frame(width: 84, height: 84)
                    VStack(spacing: 3) {
                        Text(p.display_name)
                            .font(.system(size: 15, weight: .semibold))
                            .foregroundStyle(Brand.ink)
                            .lineLimit(1)
                        Text(s.reason)
                            .font(.system(size: 13))
                            .foregroundStyle(Brand.inkSoft)
                            .multilineTextAlignment(.center)
                            .lineLimit(2, reservesSpace: true)
                    }
                }
                .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityIdentifier("feed-person")
            Button { Task { await toggle(p.user_id) } } label: {
                Text(on ? "Following" : "Follow")
                    .font(.system(size: 15, weight: .semibold))
                    .foregroundStyle(on ? Brand.ink : .white)
                    .padding(.horizontal, 22).frame(height: 36)
                    .background(on ? Color.clear : Brand.ink, in: .capsule)
                    .overlay { if on { Capsule().strokeBorder(Brand.hairline, lineWidth: 1) } }
                    .frame(minHeight: 44)
                    .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityIdentifier("feed-person-follow")
        }
        .padding(.horizontal, 12).padding(.top, 18).padding(.bottom, 10)
        .frame(width: Self.cardWidth)
        .background(Brand.surfaceMuted, in: .rect(cornerRadius: 20, style: .continuous))
        .overlay(alignment: .topTrailing) {
            Button {
                withAnimation(.snappy(duration: 0.2)) { _ = gone.insert(p.user_id) }
            } label: {
                Image(systemName: "xmark")
                    .font(.system(size: 10, weight: .bold))
                    .foregroundStyle(.white)
                    .frame(width: 22, height: 22)
                    .background(Brand.ink, in: .circle)
                    .frame(width: 44, height: 44)
                    .contentShape(.rect)
            }
            .buttonStyle(.plain)
            .accessibilityLabel("Not now, \(p.display_name)")
            .accessibilityIdentifier("feed-person-dismiss")
        }
    }

    private func face(_ p: Profiles.Profile) -> some View {
        ZStack {
            Circle().fill(Brand.moss.opacity(0.12))
            if let url = p.avatar_url, let u = URL(string: url) {
                TreePhoto(url: u) { Color.clear }.clipShape(.circle)
            } else if let first = p.display_name.first {
                Text(String(first).uppercased())
                    .font(.brand(32, .black, relativeTo: .title))
                    .foregroundStyle(Brand.moss)
            }
        }
    }

    private func load() async {
        guard let me = account.session?.userId else { people = []; return }
        if DemoPeople.on { people = DemoPeople.suggestions; return }
        let token = await account.freshToken()
        guard let rows = await profiles.morePhotographers(skip: Array(following), n: 12, token: token) else { return }
        people = SuggestedPeople.more(rows, after: [], me: me, blocked: { moderation.hides($0) })
            .filter { !following.contains($0.profile.user_id.lowercased()) }
    }

    private func toggle(_ id: String) async {
        guard let me = account.session?.userId, let t = await account.freshToken() else { return }
        if followed.contains(id) {
            if await profiles.unfollow(id, me: me, token: t) { followed.remove(id) }
        } else {
            let ok = DemoPeople.on ? true : await profiles.follow(id, me: me, token: t)
            if ok { followed.insert(id) }
        }
    }
}
