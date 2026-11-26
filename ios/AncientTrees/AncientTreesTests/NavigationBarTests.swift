// The navigation bar once content scrolls under it (escaped bug, 2026-11-25:
// on iOS 18 the bar stayed transparent, so the clock and "Back" sat on top of
// the tree page's facts, Find people's names and Settings). iOS 26 draws its
// own glass edge behind a clear bar; iOS 18 and earlier draw nothing, so below
// 26 the scrolled bar must carry the system material.

import Testing
import UIKit
@testable import AncientTrees

@MainActor
struct NavigationBarTests {
    @Test func belowIOS26TheScrolledBarHasABackground() {
        // The system's own default bar, whatever runtime runs the test, not
        // the clear one: what every UIKit app shows once content scrolls under.
        let bars = AncientTreesApp.navigationBars(glass: false)
        let system = UINavigationBarAppearance()
        system.configureWithDefaultBackground()
        system.largeTitleTextAttributes = bars.scrolled.largeTitleTextAttributes
        system.titleTextAttributes = bars.scrolled.titleTextAttributes
        let clear = UINavigationBarAppearance()
        clear.configureWithTransparentBackground()
        clear.largeTitleTextAttributes = bars.scrolled.largeTitleTextAttributes
        clear.titleTextAttributes = bars.scrolled.titleTextAttributes
        #expect(bars.scrolled.isEqual(system))
        // On an iOS 26 runtime Apple's default bar is itself hidden (it draws
        // glass), so the two cannot differ there; the floor job runs this on
        // iOS 18, where the 2026-11-25 fault lived.
        if #unavailable(iOS 26) {
            #expect(!bars.scrolled.isEqual(clear))
        }
    }

    @Test func onIOS26TheScrolledBarIsTheClearOne() {
        // iOS 26 draws its own glass edge behind a clear bar.
        let bars = AncientTreesApp.navigationBars(glass: true)
        #expect(bars.scrolled === bars.edge)
    }

    @Test func atTheScrollEdgeTheBarStaysClear() {
        for glass in [false, true] {
            let bars = AncientTreesApp.navigationBars(glass: glass)
            #expect(bars.edge.backgroundEffect == nil)
            #expect(bars.edge.backgroundColor == nil || bars.edge.backgroundColor == .clear)
        }
    }

    @Test func theScrolledBarKeepsTheBrandTitles() {
        let bars = AncientTreesApp.navigationBars(glass: false)
        #expect(bars.scrolled.titleTextAttributes.keys.contains(.font)
                == bars.edge.titleTextAttributes.keys.contains(.font))
    }
}
