# Immersive Mode Testing

## How to Test Your Immersive Mode Feature

### ✅ **GitHub Actions Validation (Recommended)**

**What it does:**
- Validates patch syntax and structure
- Checks flag registration
- Ensures patches are properly included in series file
- Runs lint checks for code quality

**How to use:**
1. **Push your changes** to this repository
2. **Go to Actions tab** in GitHub
3. **Watch the "Validate Immersive Mode Patch" workflow** (completes in ~30 seconds)
4. **Check for green checkmarks** - if all pass, your patch is ready!

**What it validates:**
- ✅ Patch file exists and has correct syntax
- ✅ Flag constant `kEnableImmersiveModeCommandLine` is defined
- ✅ Flag description "Enable Immersive Mode" is present
- ✅ BrowserView modifications are included
- ✅ Patch is listed in `patches/series` file
- ✅ No trailing whitespace or formatting issues

### ⚠️ **GitHub Actions Build (Experimental)**

**Important:** The build workflow is **manual-only** and **experimental**.

**Why manual-only:**
- Requires 200+ GB disk space
- Takes 6+ hours to complete
- Will likely fail on GitHub Actions free tier
- For testing purposes only

**How to trigger (if you really want to):**
1. Go to Actions → "Build Helium (Manual Only - Experimental)"
2. Click "Run workflow"
3. Type exactly: `I understand this takes 6+ hours and 200GB`
4. Wait 6+ hours (if it doesn't fail first)

**Better alternative:** Submit a PR to [helium-windows](https://github.com/imputnet/helium-windows) for real builds.

### 🏠 **Local Testing (If you have space)**

```bash
# Clone the Windows platform repo
git clone https://github.com/imputnet/helium-windows.git
cd helium-windows

# Point to your local core repo
git submodule set-url core /path/to/your/helium/repo

# Build (requires 200GB+ disk space)
python scripts/fetch.py
python scripts/configure.py --release
python scripts/build.py --release
```

### 🧪 **Manual Testing with Existing Build**

If you want to test the concept without building:

1. **Download official Helium** from [releases](https://github.com/imputnet/helium-windows/releases)
2. **Use browser dev tools** to simulate the feature:
   ```javascript
   // Hide toolbar (simulate immersive mode)
   document.querySelector('[role="toolbar"]').style.transform = 'translateY(-100%)';
   document.querySelector('[role="tablist"]').style.transform = 'translateY(-100%)';
   
   // Show toolbar
   document.querySelector('[role="toolbar"]').style.transform = 'translateY(0)';
   document.querySelector('[role="tablist"]').style.transform = 'translateY(0)';
   ```

## Testing the Feature

Once you have a build with your patch:

1. **Enable the flag**:
   - Go to `chrome://flags`
   - Search "Immersive Mode"
   - Enable it
   - Relaunch browser

2. **Test behavior**:
   - Move mouse to top of window → bars should slide down
   - Move mouse away → bars should slide up after 1 second
   - Test in different window states (maximized, windowed, etc.)

3. **Verify edge cases**:
   - Fullscreen mode (should be disabled)
   - PWA windows (should be disabled)
   - DevTools open (should work normally)

## Production Builds

**For production-ready builds:**
1. Submit a PR to [helium-windows](https://github.com/imputnet/helium-windows)
2. Include your core patches in the PR
3. Let their CI handle the heavy lifting
4. Download the official build when ready

## Troubleshooting

- **Validation fails**: Check the Actions logs for specific errors
- **Feature doesn't work**: Verify flag is enabled and browser restarted
- **Animation issues**: Check if hardware acceleration is enabled
- **Build fails**: Use the official helium-windows repo instead

## Summary

- ✅ **Use GitHub Actions validation** for patch development
- ⚠️ **Avoid GitHub Actions builds** (too resource-intensive)
- 🏠 **Build locally** if you have 200GB+ disk space
- 🚀 **Submit to helium-windows** for production builds
