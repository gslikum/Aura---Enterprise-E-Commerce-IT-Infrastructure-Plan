import Foundation
import Vision
import AppKit

let arguments = CommandLine.arguments
if arguments.count < 2 {
    print("Usage: ocr <image_path>")
    exit(1)
}

let imagePath = arguments[1]
let url = URL(fileURLWithPath: imagePath)

guard let image = NSImage(contentsOf: url),
      let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    print("Failed to load image: \(imagePath)")
    exit(1)
}

let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
let request = VNRecognizeTextRequest { request, error in
    guard let observations = request.results as? [VNRecognizedTextObservation] else { return }
    for observation in observations {
        if let topCandidate = observation.topCandidates(1).first {
            print(topCandidate.string)
        }
    }
}
request.recognitionLevel = .accurate
request.usesLanguageCorrection = true

do {
    try requestHandler.perform([request])
} catch {
    print("Error performing OCR: \(error)")
}
