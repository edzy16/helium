# Immersive Mode Testing

## How to Test Your Immersive Mode Feature

### Option 1: GitHub Actions Build (Recommended)

1. **Push your changes** to this repository
2. **Go to Actions tab** in GitHub
3. **Wait for build to complete** (~2-3 hours)
4. **Download the artifact** from the latest successful run
5. **Run with immersive mode**:
   ```bash
   helium.exe --enable-immersive-mode
   ```

### Option 2: Manual Testing

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

### Option 3: Local Build (if you have space)

```bash
# Clone the Windows platform repo
git clone https://github.com/imputnet/helium-windows.git
cd helium-windows

# Point to your local core repo
git submodule set-url core /path/to/your/helium/repo

# Build
python scripts/fetch.py
python scripts/configure.py --release
python scripts/build.py --release
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

## Troubleshooting

- **Build fails**: Check Actions logs for specific errors
- **Feature doesn't work**: Verify flag is enabled and browser restarted
- **Animation issues**: Check if hardware acceleration is enabled
