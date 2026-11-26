// Light, dark, or whatever the phone is set to, and one place that decides.
//
// Added 2026-11-26 from a tester: "The night (dark) mode is very dark, and
// there's no way to turn it off." Until then the app only followed the phone.
// The references keep a row for it under settings: Google Maps ("Dark mode":
// same as device, on, off), and Android's own dark-theme guidance asks every
// app for exactly these three (CONVENTIONS.md "Light, dark or the phone's
// setting"). It follows the account like kilometres or miles do (Units.swift),
// because nothing a person chooses stays on one phone only (Hidde,
// 2026-11-26: "ALTIJD AAN ACCOUNT"); the copy on the phone is the account's,
// read back at launch, and signed out it is simply the default.

import SwiftUI
import UIKit

enum AppTheme: String, CaseIterable, Identifiable {
    case system, light, dark
    var id: String { rawValue }
    var label: String {
        switch self {
        case .system: return "System"
        case .light: return "Light"
        case .dark: return "Dark"
        }
    }
    var style: UIUserInterfaceStyle {
        switch self {
        case .system: return .unspecified
        case .light: return .light
        case .dark: return .dark
        }
    }
}

@MainActor
@Observable
final class Appearance {
    private static let key = "appearance"

    /// Told the account when it changes, set once by the root, so this file
    /// keeps knowing nothing about the network.
    static var sync: ((AppTheme) -> Void)?

    var theme: AppTheme {
        didSet {
            UserDefaults.standard.set(theme.rawValue, forKey: Self.key)
            apply()
            Self.sync?(theme)
        }
    }

    init() {
        theme = UserDefaults.standard.string(forKey: Self.key).flatMap(AppTheme.init(rawValue:)) ?? .system
    }

    /// What the account says, without writing it back to the account.
    func adopt(_ raw: String?) {
        guard let raw, let t = AppTheme(rawValue: raw), t != theme else { return }
        let keep = Self.sync
        Self.sync = nil
        theme = t
        Self.sync = keep
    }

    /// Every window, so sheets, the map and UIKit's own controls change at
    /// once. preferredColorScheme on the root alone leaves a presented sheet
    /// on the old scheme until it is opened again.
    func apply() {
        for scene in UIApplication.shared.connectedScenes {
            for window in (scene as? UIWindowScene)?.windows ?? [] {
                window.overrideUserInterfaceStyle = theme.style
            }
        }
    }
}
