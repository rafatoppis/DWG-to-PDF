# The following code sample demonstrates how to specify the specific layout of a DWG file to export as a PDF document in Python.
import aspose.cad as cad
import os


path = os.path.dirname(os.path.realpath(__file__))
inputpath = os.path.join(path, "native")
exportpath = os.path.join(path, "exported_pdf")

# Listing all Natives and producing pdf's
for _, _, files in os.walk(inputpath):
    for file in files:
        inputfile = os.path.join(inputpath, file)
        print("Loading File -> %s" % (file)) 
        image = cad.Image.load(inputfile)

        # Specify PDF Options
        rasterizationOptions = cad.imageoptions.CadRasterizationOptions()
        rasterizationOptions.draw_type = cad.fileformats.cad.CadDrawTypeMode.USE_OBJECT_COLOR
        pdfOptions = cad.imageoptions.PdfOptions()
        pdfOptions.vector_rasterization_options = rasterizationOptions



        # Save as PDF
        filename = file.replace(".DWG", ".PDF")
        output = os.path.join(exportpath, filename)
        print("Converting to PDF -> '%s' to '%s'" % (file, filename))
        image.save(output, pdfOptions)
        print("File %s converted to PDF!" % (file))
