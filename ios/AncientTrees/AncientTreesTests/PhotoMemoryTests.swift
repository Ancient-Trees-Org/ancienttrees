import XCTest
import UIKit
@testable import AncientTrees

/// A photograph is never held in memory bigger than a screen can show
/// (Kit/TreePhoto.swift, ImageStore.downsampled; 2026-11-16). 1,172 photos in
/// the feed were Wikimedia originals of 20 to 50 megapixels, each about
/// 100 MB once decoded the old way.
final class PhotoMemoryTests: XCTestCase {

    private func jpeg(width: Int, height: Int) -> Data {
        let format = UIGraphicsImageRendererFormat()
        format.scale = 1
        let image = UIGraphicsImageRenderer(size: CGSize(width: width, height: height), format: format).image { ctx in
            UIColor.green.setFill()
            ctx.fill(CGRect(x: 0, y: 0, width: width, height: height))
        }
        return image.jpegData(compressionQuality: 0.5)!
    }

    private func pixels(_ image: UIImage) -> (Int, Int) {
        (Int(image.size.width * image.scale), Int(image.size.height * image.scale))
    }

    func testAnOriginalIsReadAtScreenSize() async {
        let big = await ImageStore.downsampled(jpeg(width: 6000, height: 4000))
        XCTAssertNotNil(big)
        let (w, h) = pixels(big!)
        XCTAssertEqual(max(w, h), ImageStore.maxPixels)
        XCTAssertEqual(Double(w) / Double(h), 1.5, accuracy: 0.01, "keeps its shape")
    }

    func testOurOwnCopyPassesThroughUnchanged() async {
        let ours = await ImageStore.downsampled(jpeg(width: 1600, height: 1200))
        XCTAssertNotNil(ours)
        let (w, h) = pixels(ours!)
        XCTAssertEqual(w, 1600)
        XCTAssertEqual(h, 1200)
    }

    func testNotAPictureGivesNothing() async {
        let none = await ImageStore.downsampled(Data("not a jpeg".utf8))
        XCTAssertNil(none)
    }
}
