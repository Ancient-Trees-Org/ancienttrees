//
//  AncientTreesApp.swift
//  AncientTrees
//
//  Created by Hidde on 19/08/2026.
//

import SwiftUI
import UIKit

@main
struct AncientTreesApp: App {
    /// Somewhere for photographs to live, set before the first request rather
    /// than on the first view. It is two object allocations and cannot hang,
    /// which is the whole reason anything else was moved out of here.
    ///
    /// iOS gives a process 512 KB of image cache by default and this app draws
    /// shelves of photographs, so without this every scroll back down a page
    /// re-downloads what it drew a second ago. See Kit/TreePhoto.swift.
    /// THE FONT IS REGISTERED HERE, before any view exists, and the appearance
    /// work stays where it was moved to.
    ///
    /// Those two used to travel together and the reason they were moved out of
    /// init was sound: anything that hangs before a view exists gives a white
    /// screen with nothing to read. But that risk belongs to the UIKit
    /// appearance proxies, not to this: registering five files that ship inside
    /// the bundle touches no network and no disk we do not control.
    ///
    /// Leaving it out cost the opening cover its typeface (Hidde, 2026-08-29:
    /// "waarom is het lettertype opeens lelijk"). The cover IS the first frame,
    /// so it asked for Gabarito before Gabarito existed, and SwiftUI's
    /// Font.custom falls back to the system face without a word. Every screen
    /// after it looked right, which is why it read as a mystery rather than a
    /// missing font.
    init() {
        // First, so a crash anywhere after this line is caught (Kit/CrashReporter.swift).
        CrashReporter.start()
        // Before anything writes: did the last run end on screen? (Kit/ExitWatch.swift)
        ExitWatch.capture()
        ImageStore.prepareCache()
        BrandFont.register()
    }

    /// Registering the brand font and styling the navigation bar used to happen
    /// in init(), which runs before any view exists. Anything that hangs there
    /// gives a white screen with nothing to read: no view, no console output, no
    /// crash report. It runs on the first view's appearance now, so the worst
    /// case is an unstyled first frame rather than a blank app.
    @MainActor static func configureAppearance() {
// The brand face has to exist before the first view asks for it.
        BrandFont.register()

        // A large navigation title is drawn by UIKit, so SwiftUI cannot set its
        // font. The appearance proxy can, and doing it once here is what stops
        // every screen's own name from being the system face while everything
        // under it is not.
        let glass: Bool
        if #available(iOS 26, *) { glass = true } else { glass = false }
        let bars = navigationBars(glass: glass)
        UINavigationBar.appearance().standardAppearance = bars.scrolled
        UINavigationBar.appearance().scrollEdgeAppearance = bars.edge
        UINavigationBar.appearance().compactAppearance = bars.scrolled
    }

    /// The bar at the scroll edge and once content scrolls under it. Its own
    /// function so NavigationBarTests holds the iOS 18 rule below (escaped bug
    /// of 2026-11-25: the bar was see-through on a scrolled page).
    @MainActor static func navigationBars(glass: Bool)
        -> (edge: UINavigationBarAppearance, scrolled: UINavigationBarAppearance) {
        let bar = UINavigationBarAppearance()
        bar.configureWithTransparentBackground()
        let ink = UIColor { $0.userInterfaceStyle == .dark
            ? UIColor(hex: 0xECEFE4) : UIColor(hex: 0x26301E) }
        if let large = UIFont(name: "Gabarito-Black", size: 34) {
            bar.largeTitleTextAttributes = [.font: large, .foregroundColor: ink]
        }
        if let inline = UIFont(name: "Gabarito-Bold", size: 17) {
            bar.titleTextAttributes = [.font: inline, .foregroundColor: ink]
        }
        // Clear at the scroll edge, Apple's own default. Once content scrolls
        // under the bar, iOS 26 draws its glass edge effect by itself, but
        // iOS 18 and earlier draw nothing behind a transparent bar: the clock
        // and "Back" sat on top of the tree page's facts, Find people's names
        // and Settings (walk before build 42, 2026-11-25). Below 26 the
        // scrolled bar takes the system material, as every UIKit app's does.
        let scrolled: UINavigationBarAppearance
        if glass {
            scrolled = bar
        } else {
            scrolled = UINavigationBarAppearance()
            scrolled.configureWithDefaultBackground()
            scrolled.largeTitleTextAttributes = bar.largeTitleTextAttributes
            scrolled.titleTextAttributes = bar.titleTextAttributes
        }
        return (bar, scrolled)
    }

    var body: some Scene {
        WindowGroup {
            ContentView()
                // The whole app presses in moss, not in system blue. Without
                // this, iOS tints the selected tab, the map's locate button and
                // every text field's caret and placeholder link with its own
                // accent, so four screens out of fourteen had a blue element on
                // them and the app read as half-finished. Found by the first
                // screenshot sweep on 2026-08-20, on the first screenshot.
                .tint(Brand.moss)
                .task { AncientTreesApp.configureAppearance() }
        }
    }
}
