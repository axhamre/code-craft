#!/bin/bash

# CodeCraft setup script
# Copies essential framework files into existing project

set -e

# Default target directory
TARGET_DIR="codecraft"

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -d|--dir)
      TARGET_DIR="$2"
      shift 2
      ;;
    -h|--help)
      echo "Usage: ./setup.sh [-d|--dir TARGET_DIR]"
      echo "  -d, --dir    Target directory name (default: codecraft)"
      echo "  -h, --help   Show this help message"
      exit 0
      ;;
    *)
      echo "Unknown option $1"
      exit 1
      ;;
  esac
done

# Get script directory (where CodeCraft is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Setting up CodeCraft in directory: $TARGET_DIR"

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy essential files and directories
cp -r "$SCRIPT_DIR/framework" "$TARGET_DIR/"
cp -r "$SCRIPT_DIR/templates" "$TARGET_DIR/"
cp -r "$SCRIPT_DIR/guides" "$TARGET_DIR/"
cp "$SCRIPT_DIR/QUICKSTART.md" "$TARGET_DIR/"

# Create working directories
mkdir -p "$TARGET_DIR/01-specification"
mkdir -p "$TARGET_DIR/02-plan"
mkdir -p "$TARGET_DIR/03-implementation"

echo "✅ CodeCraft setup complete!"
echo ""
echo "Next steps:"
echo "1. cd $TARGET_DIR"
echo "2. Follow QUICKSTART.md for workflow instructions"
echo "3. Start with your project requirements" 