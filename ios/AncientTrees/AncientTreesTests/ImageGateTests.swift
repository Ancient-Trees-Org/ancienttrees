import XCTest
@testable import AncientTrees

/// A fast scroll down the Feed (Hidde, 2026-11-26: photographs loading
/// "forever", other pages loading nothing): the gate serves the NEWEST request
/// first, so what is on screen does not wait behind what was scrolled past.
final class ImageGateTests: XCTestCase {
    func testTheLastOneAskedGoesFirst() async {
        let gate = ImageGate(limit: 1)
        await gate.acquire()                       // the one slot is taken
        let order = Order()
        let a = Task { await gate.acquire(); await order.add("old") }
        try? await Task.sleep(for: .milliseconds(50))
        let b = Task { await gate.acquire(); await order.add("new") }
        try? await Task.sleep(for: .milliseconds(50))
        await gate.release()                       // one slot frees up
        try? await Task.sleep(for: .milliseconds(50))
        let first = await order.list.first
        XCTAssertEqual(first, "new", "the request scrolled past was served before the one on screen")
        await gate.release()
        _ = await (a.value, b.value)
    }
}

private actor Order {
    var list: [String] = []
    func add(_ s: String) { list.append(s) }
}
