// A map you drag under a fixed pin, to say where something is.
//
// Convention: Google Maps ("Move map to adjust") and Airbnb's location step.
// Both move the MAP under a pin that never moves, and for the same reason:
// dragging a marker puts your thumb over the thing you are aiming at, while a
// fixed crosshair leaves the target visible the whole time. CONVENTIONS.md
// carries the entry.
//
// Lifted out of PlacePin on 2026-08-28 rather than copied. That screen asks
// where a tree we publish really is; the collect flow now has to ask where a
// photograph was taken when the photograph does not say. Two screens, one
// question, and a second hand-built crosshair would have drifted from this one
// within a month.
//
// AND A FIELD TO TYPE AN ADDRESS (2026-11-26, a tester adding a library photo
// with no location: he knew the address and could only drag). Airbnb's
// location step and Google Maps' "Add a missing place" both open with an
// address field over the map, suggestions as you type, and the pin to fine-tune
// after a pick. Apple's own MKLocalSearchCompleter gives the suggestions, biased
// to what the map shows; a pick flies the map there and the crosshair does the
// rest, so the coordinate still comes from the pin and never from the words.

import SwiftUI
import MapKit

struct PinPicker: View {
    /// Where the map opens. For a correction that is our own pin; for a
    /// photograph with no location of its own it is wherever the person is,
    /// or the last place they looked.
    let start: CLLocationCoordinate2D
    /// Drawn for context and never selectable: knowing which trees we already
    /// map is most of what tells somebody they are in the right place.
    var trees: [Tree] = []
    /// The street, not the district. Somebody is telling us which trunk, and
    /// at four kilometres a trunk is a dot.
    var spanMeters: Double = 300
    @Binding var coordinate: CLLocationCoordinate2D

    @State private var region: MKCoordinateRegion?
    @State private var moveTo: (token: UUID, region: MKCoordinateRegion)?
    @State private var search = AddressSearch()
    @FocusState private var typing: Bool

    var body: some View {
        ZStack(alignment: .top) {
            TreeMap(trees: trees,
                    focus: start,
                    spanMeters: spanMeters,
                    declutter: false,
                    region: $region,
                    moveTo: moveTo,
                    selected: .constant(nil))
                .ignoresSafeArea(edges: .bottom)
            crosshair
                .frame(maxWidth: .infinity, maxHeight: .infinity)
            addressBox
        }
        .onChange(of: region?.center.latitude) { _, _ in read() }
        .onChange(of: region?.center.longitude) { _, _ in read() }
        .onChange(of: search.query) { _, _ in
            if let r = region { search.completer.region = r }
            search.update()
        }
    }

    private func read() {
        guard let c = region?.center else { return }
        coordinate = c
    }

    // MARK: - Typing an address

    /// The field and, while somebody types, Apple's suggestions under it in
    /// the same card. Spacing is the collect flow's search field (44 tall,
    /// radius 14, 12 inside) and MapSearch's rows (EmptyPlaceRow, 56 tall).
    private var addressBox: some View {
        VStack(spacing: 0) {
            HStack(spacing: 8) {
                Image(systemName: "magnifyingglass").foregroundStyle(Brand.inkSoft)
                TextField("Search an address", text: $search.query)
                    .font(.system(size: 16))
                    .foregroundStyle(Brand.ink)
                    .autocorrectionDisabled()
                    .textContentType(.fullStreetAddress)
                    .submitLabel(.search)
                    .focused($typing)
                    .onSubmit { if let first = search.results.first { pick(first) } }
                    .accessibilityIdentifier("pin-address")
                if !search.query.isEmpty {
                    Button { search.query = ""; search.results = [] } label: {
                        Image(systemName: "xmark.circle.fill").foregroundStyle(Brand.inkSoft)
                    }
                    .buttonStyle(.plain)
                    .accessibilityLabel("Clear")
                }
            }
            .padding(.horizontal, 12)
            .frame(minHeight: 44)

            if typing && !search.results.isEmpty {
                Divider().overlay(Brand.hairline)
                ForEach(Array(search.results.prefix(5).enumerated()), id: \.offset) { i, r in
                    Button { pick(r) } label: {
                        EmptyPlaceRow(name: r.title, sub: r.subtitle,
                                      icon: "mappin.and.ellipse", inset: 12)
                    }
                    .buttonStyle(.plain)
                    .accessibilityIdentifier("pin-address-\(i)")
                }
            }
        }
        .background(Brand.surfaceMuted, in: .rect(cornerRadius: 14))
        // An edge, because in the dark the field and the map are one tone
        // apart and a shadow does not show there (Apple's dark-mode note).
        .overlay(RoundedRectangle(cornerRadius: 14).stroke(Brand.hairline))
        .shadow(color: .black.opacity(0.12), radius: 6, y: 2)
        .padding(.horizontal, 16)
        .padding(.top, 12)
    }

    /// Fly the map to the picked address at the picker's own street span, so
    /// the crosshair lands on it and the person drags the last metres.
    private func pick(_ r: MKLocalSearchCompletion) {
        typing = false
        search.query = [r.title, r.subtitle].filter { !$0.isEmpty }.joined(separator: ", ")
        search.results = []
        Task {
            guard let item = try? await MKLocalSearch(request: .init(completion: r)).start()
                .mapItems.first else { return }
            let c = item.placemark.coordinate
            moveTo = (UUID(), MKCoordinateRegion(center: c, latitudinalMeters: spanMeters,
                                                 longitudinalMeters: spanMeters))
            coordinate = c
        }
    }

    /// Dead centre, hanging from its point like a map pin rather than sitting
    /// on it, so the tip marks the spot and not the middle of a circle.
    private var crosshair: some View {
        VStack(spacing: 0) {
            Image(systemName: "mappin")
                .font(.system(size: 34, weight: .semibold))
                .foregroundStyle(Brand.moss)
                .shadow(color: .black.opacity(0.25), radius: 3, y: 1)
            Circle()
                .fill(Brand.moss)
                .frame(width: 6, height: 6)
                .shadow(color: .black.opacity(0.3), radius: 2)
        }
        .offset(y: -20)
        .allowsHitTesting(false)
        .accessibilityHidden(true)
    }
}

/// Apple's address suggestions as somebody types (MKLocalSearchCompleter, the
/// type Apple Maps' own search field runs on). Nothing is stored.
@Observable
final class AddressSearch: NSObject, MKLocalSearchCompleterDelegate {
    nonisolated deinit {}
    var query = ""
    var results: [MKLocalSearchCompletion] = []
    @ObservationIgnored let completer = MKLocalSearchCompleter()

    override init() {
        super.init()
        completer.resultTypes = [.address, .pointOfInterest]
        completer.delegate = self
    }

    func update() {
        let q = query.trimmingCharacters(in: .whitespaces)
        guard q.count >= 3 else { results = []; return }
        completer.queryFragment = q
    }

    func completerDidUpdateResults(_ completer: MKLocalSearchCompleter) {
        results = completer.results
    }

    func completer(_ completer: MKLocalSearchCompleter, didFailWithError error: Error) {
        results = []
    }
}
