#!/usr/bin/env python3
import sys
import os

def main():
    print("🚀 Starting AI Legal Assistant - Split Screen Chatbot...")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('src/main.py'):
        print("❌ Error: src/main.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check if BNS data exists
    if os.path.exists('src/bns_data.json'):
        print("✅ BNS data found - Advanced legal analysis enabled")
    else:
        print("⚠️  BNS data not found - Using fallback legal analysis")
    
    print("🔧 Starting Flask application...")
    print("📱 Once started, open your browser and go to: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Change to src directory and run the app
    sys.path.insert(0, 'src')
    
    try:
        from main import app
        app.run(host='0.0.0.0', port=5000, debug=False)
    except ImportError as e:
        print(f"❌ Error importing Flask app: {e}")
        print("💡 Make sure you've installed the requirements: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting the application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

