import Foundation
import Vision
import AppKit

let dirPath = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/Week 4/chapter_10_screenshots"
let fileManager = FileManager.default

guard let files = try? fileManager.contentsOfDirectory(atPath: dirPath) else {
    print("Failed to read directory")
    exit(1)
}

let pngFiles = files.filter { $0.hasSuffix(".png") }.sorted()
print("Found \(pngFiles.count) PNG files.")

let outputFilePath = "/Users/gerrell/Library/Mobile Documents/com~apple~CloudDocs/Strayer/Capstone/.agents/worker_audit_fix/ocr_results.txt"
fileManager.createFile(atPath: outputFilePath, contents: nil, attributes: nil)

guard let fileHandle = FileHandle(forWritingAtPath: outputFilePath) else {
    print("Cannot open output file handle")
    exit(1)
}

for (idx, fname) in pngFiles.enumerated() {
    let fullPath = "\(dirPath)/\(fname)"
    guard let nsImage = NSImage(contentsOfFile: fullPath),
          let cgImage = nsImage.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        print("Failed to load image \(fname)")
        continue
    }

    let requestHandler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true

    do {
        try requestHandler.perform([request])
        guard let observations = request.results else { continue }
        
        var recognizedText = ""
        for observation in observations {
            let topCandidate = observation.topCandidates(1).first
            if let candidate = topCandidate {
                recognizedText += candidate.string + "\n"
            }
        }
        
        let header = "========================================\nIMAGE \(idx + 1): \(fname)\n========================================\n"
        if let data = (header + recognizedText + "\n\n").data(using: .utf8) {
            fileHandle.write(data)
        }
        print("Processed Image \(idx + 1)/\(pngFiles.count): \(fname)")
    } catch {
        print("Error processing \(fname): \(error)")
    }
}

fileHandle.closeFile()
print("OCR processing complete. Results saved to \(outputFilePath)")
