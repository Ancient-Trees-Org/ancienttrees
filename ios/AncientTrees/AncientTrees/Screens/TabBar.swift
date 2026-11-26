// The bottom bar, copied from AllTrails rather than designed.
//
// Hidde, 2026-08-24, twice: "kun je deze meer precies zoals alltrails maken"
// and then, after I drew a make-button of my own invention, "please verzin geen
// eigen dingen maar zoek het mooiste voorbeeld en maak het zoveel mogelijk als
// alltrails". So this is his own screenshot, read off:
//
//   - four items, evenly spaced, full width, a hairline along the top
//   - one outline weight for every symbol, nothing filled, nothing heavier
//   - the selected item wears a PILL BEHIND THE ICON ONLY, and its symbol
//     inverts to sit dark on the bright fill
//   - the word sits under the pill, outside it, and is never inside it
//
// iOS draws its own capsule around icon AND label, which is the one thing that
// cannot be reached with the native bar however it is configured, and it is
// also the most visible difference between our bar and his screenshot. Hence a
// bar of our own: not because a custom control is nicer, but because copying
// the reference exactly is what was asked and the native one cannot.

import SwiftUI

struct TabBar: View {
    /// How deep the bar floats over whatever is behind it: the disc's own 58
    /// points plus the 4 it sits off the bottom. The sheet reads this so its
    /// content can end above the bar rather than under it; a number copied
    /// into BottomSheet would drift the first time this control is resized.
    static var floatDepth: CGFloat { 58 + bottomGap }

    /// How far the bar sits off the bottom of the SAFE AREA. Negative on a
    /// phone with a home indicator, so the bar reaches into that area the way
    /// Apple's own floating tab bars do: measured 2026-09-26 in the simulator
    /// beside Photos and Contacts on an iPhone 17 Pro, their bar ends 22
    /// points above the screen's edge and ours ended 38 (Hidde: "het menu
    /// lijkt te hoog te zitten"). A phone without one (the SE) has no area to
    /// reach into, and keeps the 4 points it always had.
    static var bottomGap: CGFloat {
        let safe = UIApplication.shared.connectedScenes
            .compactMap { ($0 as? UIWindowScene)?.keyWindow?.safeAreaInsets.bottom }
            .first ?? 0
        return safe > 20 ? 22 - safe : 4
    }

    struct Item {
        /// Empty on the action, which carries no word: see `items`.
        let title: String
        let symbol: String
        /// The TabView tag this item selects. Not its position: the Feed came
        /// in third on 2026-11-26 with tag 4, so My trees stays 2 and the
        /// camera 3 for every caller and launch argument that says so.
        var tag: Int
        /// An image in the asset catalogue instead of an SF Symbol, with a
        /// ".fill" twin for the chosen state (the Feed's two people).
        var asset = false
        /// The one slot that is a DEED rather than a place.
        var action: Bool = false
    }

    /// Same order as the TabView's tags.
    ///
    /// FIVE slots, with the deed in the MIDDLE and no word under it (Hidde,
    /// 2026-08-24: "toch profiel als 5e tab en dan de camera in het midden
    /// zonder tekst eronder omdat het een andere actie is - maar dan wel met
    /// een aparte visuele highlight").
    ///
    /// This is the same control I drew that morning and he rejected, and he was
    /// right then and right now: Instagram, TikTok and YouTube all put it in
    /// the centre of a bar of FIVE, and with four slots there is no centre, so
    /// what was left was an invention wearing a reference as an excuse. The
    /// pattern only transfers with its preconditions, and the fifth tab is the
    /// precondition.
    ///
    /// A camera and never a plus (Hidde, 2026-08-23): a plus promises a row in
    /// a list, a camera says what you are about to do.
    /// THREE PLACES, and the deed is not one of them (Hidde, 2026-08-26:
    /// "Map, discover, my trees en een camera button zoals bij polarsteps los
    /// ... dus 3 iconen samen en dan de camera los want dat is geen pagina
    /// maar een actie").
    ///
    /// The reference is his own Polarsteps screen: a rounded bar holding the
    /// destinations, and a SEPARATE circular button floating beside it. That
    /// separation is the whole argument. A camera in a row of tabs says "a
    /// fourth place to go"; a camera on its own disc says "do this now", and
    /// it is the only control in the app that makes something.
    ///
    /// This replaces the five-slot bar of 2026-08-24, which put the deed in
    /// the middle because Instagram, TikTok and YouTube do. That pattern was
    /// read correctly and its precondition is a bar of five; with three
    /// destinations there is no middle to sit in, and Polarsteps answers the
    /// same problem by taking the button out of the bar entirely.
    ///
    /// FOUR SINCE 2026-11-26: the Feed, third (Hidde: the feed "een eigen
    /// tab", Map · Discover · Feed · My trees, AllTrails' Explore · Community
    /// · ... · Saved). Its symbol is Polarsteps' Activity tab, one person in
    /// front of a smaller one (Hidde, 2026-11-26: "laten we het activiteit
    /// logo van polarsteps overnemen", then "die gespiegelde ... die heeft
    /// android ook"). SF has no such symbol (person.2 stands two alike side
    /// by side), so it is Material Symbols' `group`, the glyph Android draws,
    /// as a template image (Assets.xcassets/Symbols, Apache 2.0,
    /// ICONS-LICENSE-APACHE.txt): outlined, filled when chosen.
    static let items = [
        Item(title: "Map", symbol: "map", tag: 0),
        Item(title: "Discover", symbol: "magnifyingglass", tag: 1),
        Item(title: "Feed", symbol: "feed.group", tag: 4, asset: true),
        Item(title: "My trees", symbol: "leaf", tag: 2),
    ]

    /// The tag the camera carries in the TabView, intercepted rather than
    /// shown. It stays 2 so every launch argument and every caller that says
    /// -tab=2 still opens the collect sheet.
    static let collectTag = 3

    let selected: Int
    let select: (Int) -> Void
    /// The pill has to be ONE view that moves, not a different view appearing
    /// in each item, or the change happens by fading two rectangles in and out
    /// (Hidde, 2026-08-26: "de animatie is gek als je over de floating bar van
    /// selectiepagina wisselt, dat heeft volgens mij een standaard ios
    /// animatie die je niet gebruikt"). He is right that there is a standard
    /// one: iOS slides the selection between segments, and matchedGeometry is
    /// how SwiftUI does exactly that.
    @Namespace private var pill
    /// The deed, handed in rather than assumed, because it is not a tab.
    var collect: () -> Void = {}

    /// THE MENU OPTIONS for Hidde to choose from (2026-11-26: "de tekst en het
    /// icoon te ver van elkaar ... Polarsteps-titels dikker en kleiner ...
    /// geef me een paar opties"). `-tabstyle=N` picks one for the
    /// screenshots; the chosen one becomes the only one and this table goes.
    struct Style {
        var glyph: CGFloat, gap: CGFloat, label: CGFloat
        var weightOn: Font.Weight, weightOff: Font.Weight
        var off: Double, greyPill: Bool, item: CGFloat
    }
    static let styles: [Style] = [
        .init(glyph: 19, gap: 6, label: 11, weightOn: .semibold, weightOff: .regular, off: 0.72, greyPill: false, item: 46),
        .init(glyph: 20, gap: 2, label: 10, weightOn: .bold, weightOff: .semibold, off: 0.72, greyPill: false, item: 46),
        .init(glyph: 22, gap: 2, label: 10, weightOn: .bold, weightOff: .semibold, off: 0.9, greyPill: true, item: 46),
        .init(glyph: 18, gap: 1, label: 10, weightOn: .bold, weightOff: .semibold, off: 0.62, greyPill: false, item: 44),
        .init(glyph: 22, gap: 1, label: 9.5, weightOn: .heavy, weightOff: .bold, off: 0.72, greyPill: false, item: 46),
    ]
    static let style: Style = {
        let n = ProcessInfo.processInfo.arguments.first { $0.hasPrefix("-tabstyle=") }
            .flatMap { Int($0.dropFirst(10)) } ?? 1
        return styles[max(0, min(styles.count - 1, n - 1))]
    }()

    /// An item's glyph: the SF Symbol at 21 points, or the asset drawn at the
    /// same visual size (Material's 24 grid, 26 points across like Android's 26 dp).
    @ViewBuilder private func glyph(_ item: Item, on: Bool) -> some View {
        if item.asset {
            Image(on ? item.symbol + ".fill" : item.symbol)
                .renderingMode(.template)
                .resizable()
                .scaledToFit()
                .frame(width: Self.style.glyph + 6, height: Self.style.glyph + 6)
                .frame(height: Self.style.glyph + 3)
        } else {
            Image(systemName: item.symbol)
                .font(.system(size: Self.style.glyph, weight: .regular))
                .environment(\.symbolVariants, on ? .fill : .none)
                .frame(height: Self.style.glyph + 3)
        }
    }

    var body: some View {
        HStack(spacing: 10) {
            HStack(spacing: 4) {
                ForEach(Self.items, id: \.tag) { item in
                    let i = item.tag
                    Button {
                        // The slide, and nothing else animated: a tab change
                        // itself is instant on iOS and always has been.
                        withAnimation(.snappy(duration: 0.28)) { select(i) }
                    } label: {
                        // POLARSTEPS' BALANCE (Hidde, 2026-11-26: "de balans bij
                        // Polarsteps iets beter ... iconen iets kleiner"),
                        // measured on his screenshot: a 23 point glyph, 6
                        // points to the word, the pair centred with air above
                        // and below. Ours was 21 point type with 3 to the word.
                        VStack(spacing: Self.style.gap) {
                            glyph(item, on: i == selected)
                            Text(item.title)
                                .font(.system(size: Self.style.label,
                                              weight: i == selected ? Self.style.weightOn : Self.style.weightOff))
                                .lineLimit(1)
                        }
                        // MONOCHROME, and that is the reference rather than a
                        // preference (Hidde, 2026-08-26: "flikker op met dat
                        // hele groen, maak het gewoon zwart-wit en zoals zij
                        // doen met dat grijze overlay").
                        .foregroundStyle(i == selected ? Brand.ink : Brand.ink.opacity(Self.style.off))
                        .frame(maxWidth: .infinity)
                        .frame(height: Self.style.item)
                        // THE SECOND COLOUR, which is the part he asked for by
                        // name (2026-08-26: "ze hebben een tweede kleur extra
                        // die om het icoon zit naast de fill om aan te geven
                        // waar je zit"). Polarsteps says the selected tab
                        // twice: the glyph fills AND a lighter pill sits
                        // behind the whole item. Filling alone is a small
                        // difference at a glance on a bar this size, and the
                        // pill is what makes it readable without looking.
                        .background {
                            if i == selected {
                                // WIDER THAN ITS SLOT (Hidde, 2026-11-26, Polarsteps'
                                // bar: "het cirkeltje achter het icoon wat groter ...
                                // daardoor valt de tekst er goed onder"): measured on
                                // his screenshot, their pill is 79 points on a 71
                                // point slot, so the word sits well inside it. Ours
                                // reaches 4 into the bar's own padding each side.
                                Capsule()
                                    .fill(Self.style.greyPill ? Brand.ink.opacity(0.09) : Brand.ground.opacity(0.92))
                                    .padding(.horizontal, -4)
                                    .shadow(color: .black.opacity(0.06), radius: 3, y: 1)
                                    .matchedGeometryEffect(id: "tab-pill", in: pill)
                            }
                        }
                        .contentShape(.rect)
                    }
                    .buttonStyle(.plain)
                    .accessibilityLabel(item.title)
                    .accessibilityIdentifier("tab-\(item.title.lowercased().replacingOccurrences(of: " ", with: "-"))")
                    .accessibilityAddTraits(i == selected ? [.isSelected, .isButton] : .isButton)
                }
            }
            .padding(6)
            // A GREY BAR, not a white one. `.regularMaterial` alone renders
            // nearly white over a pale map, so the pill behind the selected
            // item had nothing to stand out against; the reference bar is
            // visibly grey and its selected pill is the light thing on it.
            // A thin wash of ink over the material gives that without
            // hardcoding a colour that would be wrong in the dark.
            .background {
                Capsule().fill(.regularMaterial)
                Capsule().fill(Brand.ink.opacity(0.06))
            }
            .overlay(Capsule().strokeBorder(.white.opacity(0.25), lineWidth: 0.5))
            .shadow(color: .black.opacity(0.10), radius: 10, y: 3)

            // The deed, on its own disc, the same height as the bar so the two
            // read as one row rather than as a bar with something stuck beside
            // it. Same glass, same grey, same edge.
            //
            // ITS GLYPH SITS 8.1 POINTS LOWER THAN THE THREE TAB ICONS, AND
            // THAT IS DECIDED RATHER THAN MISSED. Hidde asked about it on
            // 2026-09-13 and chose to leave it, so do not "fix" it: a fresh
            // pair of eyes finds it every time, and it is the third thing on
            // this control somebody has wanted to straighten.
            //
            // Measured off his own screenshot rather than argued about. The
            // shapes are right: bar and disc are both 58 points tall and their
            // centres agree to within a pixel, and the bar's own content is
            // centred in it to within 1.3 points. What differs is the GLYPHS. A
            // tab item is an icon with a word under it, so its icon rides in the
            // upper half and lands 20.7 points from the bar's top; the disc
            // carries a bare glyph, which centres at 28.8.
            //
            // Both ways of closing that gap cost more than the gap does. Moving
            // the glyph up inside the disc leaves a circle whose contents are
            // off centre, which always reads as broken; moving the whole disc up
            // breaks the one-row line this comment is about. The reference has
            // the same offset for the same reason, and a word under the camera
            // is ruled out twice over (2026-08-24, 2026-08-26: it is an action
            // rather than a place, so it carries no word).
            Button(action: collect) {
                Image(systemName: "camera.fill")
                    .font(.system(size: 21, weight: .semibold))
                    .foregroundStyle(Brand.ink)
                    .frame(width: 58, height: 58)
                    .background {
                        Circle().fill(.regularMaterial)
                        Circle().fill(Brand.ink.opacity(0.06))
                    }
                    .overlay(Circle().strokeBorder(.white.opacity(0.25), lineWidth: 0.5))
                    .shadow(color: .black.opacity(0.10), radius: 10, y: 3)
            }
            .buttonStyle(.plain)
            .accessibilityLabel("Collect a tree")
            .accessibilityIdentifier("tab-collect")
        }
        // 16, not 12: the capsule keeps 4 points inside it, so the first
        // icon landed at x=16 while every page behind it starts its content
        // at 20. The layout gate reported that on six screens, and it is
        // right that a floating bar should line up with what it floats over.
        .padding(.horizontal, 16)
        .padding(.bottom, Self.bottomGap)
    }
}
