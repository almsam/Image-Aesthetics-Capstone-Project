# ML/GenerateImage.py snapshot tests

### **INITIALIZE:**
**Begin by running `GenerateImage.py` with this footer & nothing else besides imports & methods:**

```Python
script_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.join(script_dir, "..", "public", "data", "temp")

for i in range(12):
    generateQuality(((i+1)*100), target_dir, n=72)
```

### **Snapshot test 1/3:**
Verify 37 (36+1, or 12*3 + 1) files exist in `public\data\temp\`

### **Snapshot test 2/3:**
Verify 12 files named `generated_image_quality_[1:12]00.png` exist

### **Snapshot test 3/3:**
Verify these 12 files are of 2304x2304 pixels (2304 = order x MLquality = 72x36)
