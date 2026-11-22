// A DROPPED PIN: touch and hold open map, a pin lands, a card names the spot
// (Hidde, 2026-11-22: "1 sounds cool but the interaction is quite specific and
// delicate, can you build it exactly as them?").
//
// Convention, read that day (CONVENTIONS.md "A dropped pin"):
// - Apple Maps (support.apple.com/guide/iphone/iphfa7286b57): "Touch and hold
//   the map until a pin marker appears"; one pin at a time; the card carries
//   Share "at the top of the card" and directions.
// - Google Maps (support.google.com/maps/answer/18539): "touch and hold an area
//   of the map that isn't labeled" drops a red pin; its card is "Dropped pin"
//   with the coordinates.
// Ours, in the same slot and the same header as a tree's card (Apple Maps'
// place row: share, title, cross; TreePlaceSheet.swift): "Dropped pin", the
// coordinates under it, then Add a tree here (the missing-place step of a map
// of trees) and Directions. A tap on open map, the cross or lowering the sheet
// takes the pin away.
import SwiftUI
import CoreLocation

struct DroppedPinHeader: View {
    let spot: CLLocationCoordinate2D
    let onClose: () -> Void

    var body: some View {
        HStack(alignment: .center, spacing: 12) {
            if let url = DroppedPin.shareURL(spot) {
                ShareLink(item: url, subject: Text("Dropped pin"),
                          message: Text(DroppedPin.coordinates(spot))) {
                    PlaceCircle(symbol: "square.and.arrow.up")
                }
                .buttonStyle(.plain)
                .countsShare("dropped_pin")
                .accessibilityLabel("Share this spot")
                .accessibilityIdentifier("dropped-share")
            }
            VStack(spacing: 2) {
                Text("Dropped pin")
                    .font(.brand(20, .bold, relativeTo: .title3))
                    .foregroundStyle(Brand.ink)
                // Google shows the coordinates on the card; a hold copies them
                // (the system's own text selection).
                Text(DroppedPin.coordinates(spot))
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
                    .lineLimit(1)
                    .textSelection(.enabled)
            }
            .multilineTextAlignment(.center)
            .frame(maxWidth: .infinity)
            Button(action: onClose) { PlaceCircle(symbol: "xmark") }
                .buttonStyle(.plain)
                .accessibilityLabel("Close")
                .accessibilityIdentifier("dropped-close")
        }
        .padding(.horizontal, 16)
        .padding(.top, -14)
        .padding(.bottom, 16)
        .accessibilityIdentifier("dropped-header")
    }
}

struct DroppedPinBody: View {
    let spot: CLLocationCoordinate2D
    let onAdd: () -> Void

    var body: some View {
        // Two buttons in one group, 12 apart, the sheet's pills (BrandSheet).
        VStack(spacing: 12) {
            Button(action: onAdd) {
                Label("Add a tree here", systemImage: "plus")
            }
            .buttonStyle(BrandButtonStyle())
            .accessibilityIdentifier("dropped-add")
            Button {
                Directions.walk(lat: spot.latitude, lng: spot.longitude)
            } label: {
                Label("Directions", systemImage: "arrow.triangle.turn.up.right.diamond")
            }
            .buttonStyle(BrandButtonStyle(prominent: false))
            .accessibilityIdentifier("dropped-directions")
        }
        .padding(.horizontal, 16)
    }
}

enum DroppedPin {
    /// Five decimals, about a metre: what Google's card prints.
    static func coordinates(_ c: CLLocationCoordinate2D) -> String {
        String(format: "%.5f, %.5f", c.latitude, c.longitude)
    }

    /// Our own map at the spot, so the person it goes to sees the trees
    /// around it (a dropped pin has no page of its own).
    static func shareURL(_ c: CLLocationCoordinate2D) -> URL? {
        Shared.page(String(format: "/explore#map=17/%.5f/%.5f", c.latitude, c.longitude), from: "dropped_pin")
    }
}
