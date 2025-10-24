# Vitalis Spitbank - Investment Teaser

Professional one-page investment teaser for Vitalis Spitbank, an ultra-luxury wellness fortress project.

## Project Overview

This Streamlit app presents a one-page investment opportunity for:
- **Operating Partners**: Experienced wellness/luxury hotel operators
- **Capital Partners**: Institutional equity investors, family offices

**The Opportunity**: Acquire and reposition Spitbank Fort as "Vitalis Spitbank" – a 9-suite wellness and longevity destination with world-leading spa partnership.

## Files Structure

```
vitalis-teaser/
├── vitalis_teaser_app.py   # Main Streamlit application
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Local Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run vitalis_teaser_app.py
```

4. **View in browser**
   - App will open automatically at `http://localhost:8501`
   - Or open the URL shown in your terminal

## Export as PDF

**To save the teaser as PDF:**

1. Open the app in your browser
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
3. Select **"Save as PDF"** as destination
4. Click **Save**

**Print Settings (for best results):**
- Layout: Portrait
- Paper size: Letter (8.5" x 11")
- Margins: Default
- Background graphics: Enabled

## Deployment to Streamlit Cloud

### Step 1: Push to GitHub

1. Create a new repository on GitHub (e.g., `vitalis-teaser`)
2. Upload these files:
   - `vitalis_teaser_app.py`
   - `requirements.txt`
   - `README.md`

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **"New app"**
4. Select your repository: `your-username/vitalis-teaser`
5. Main file path: `vitalis_teaser_app.py`
6. Click **"Deploy"**

### Step 3: Get Your URL

You'll receive a URL like:
```
https://your-username-vitalis-teaser.streamlit.app
```

Share this URL to let partners view the teaser online.

## Customization

### Update Contact Information

Find this section at the bottom of `vitalis_teaser_app.py`:

```python
Contact: [YOUR NAME] | [YOUR EMAIL] | [YOUR PHONE]
```

Replace with your actual details.

### Modify Financial Projections

Search for these sections in the code to update numbers:
- Executive Summary
- The Asset stats
- Financial Snapshot

### Change Branding Colors

Main colors used:
- Primary: `#92400e` (brown)
- Accent: `#fbbf24` (gold)
- Dark: `#1e293b` (slate)

Find and replace these hex codes to rebrand.

## Usage Tips

### For Operating Partners
Emphasize:
- Unique asset (no comparable property globally)
- Wellness opportunity with strategic spa partner
- UK market gap for ultra-luxury wellness

### For Capital Partners
Emphasize:
- Financial returns (296% 10-year ROI, 15% stabilized yield)
- Strategic partnership de-risking
- Multiple exit paths
- Institutional quality asset

### Combined Pitch
Present both aspects:
1. Start with the vision and asset uniqueness
2. Show financial snapshot
3. Position as needing both operator + capital

## Converting to Static PDF

If you need a static PDF without running the app:

**Option 1: Using Browser**
1. Run the app locally
2. Print to PDF as described above

**Option 2: Using HTML**
The teaser can also be saved as a standalone HTML file for offline viewing. Contact for HTML version.

## Troubleshooting

### App won't start
```bash
# Check Python version (should be 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Streamlit Cloud deployment fails
- Verify `requirements.txt` exists in repository root
- Check that `vitalis_teaser_app.py` is the correct filename
- Ensure repository is public (or Streamlit has access)

### PDF export looks wrong
- Enable background graphics in print settings
- Use portrait orientation
- Try different browsers (Chrome works best)

## Next Steps

1. **Customize** contact information and any specific details
2. **Export PDF** for email distribution
3. **Deploy online** for link sharing
4. **Track engagement** (Streamlit Cloud provides analytics)

## Support

For questions or customization requests:
- Review Streamlit docs: [docs.streamlit.io](https://docs.streamlit.io)
- Check this README for common issues

---

**Confidential & Proprietary | October 2025**
