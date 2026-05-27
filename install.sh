#!/bin/bash
# opc-starter-kit Installer
# Copies the skill to your project's skills directory.
#
# Usage:
#   ./install.sh                    install to current directory
#   ./install.sh /path/to/project   install to specific project
#   ./install.sh --global           install globally (~/.comate/skills/)

set -e

SKILL_NAME="opc-starter-kit"
SKILL_SRC="$(cd "$(dirname "$0")" && pwd)/skills/${SKILL_NAME}"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}╔══════════════════════════════════════╗${NC}"
echo -e "${BLUE}║   opc-starter-kit Installer          ║${NC}"
echo -e "${BLUE}║   AI Startup Discipline Checkpoint   ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════╝${NC}"
echo ""

# Parse arguments
TARGET_DIR=""
GLOBAL=false

for arg in "$@"; do
    case $arg in
        --global|-g) GLOBAL=true ;;
        --help|-h)
            echo "Usage: ./install.sh [OPTIONS] [TARGET_DIR]"
            echo ""
            echo "Options:"
            echo "  --global, -g   Install globally (~/.comate/skills/)"
            echo "  --help, -h     Show this help"
            echo ""
            echo "Examples:"
            echo "  ./install.sh                   current directory"
            echo "  ./install.sh ~/my-startup      specific project"
            echo "  ./install.sh --global          global install"
            echo ""
            echo "For other platforms (Cursor, Windsurf, etc.),"
            echo "see tool-adaptations.md in the references/ directory."
            exit 0
            ;;
        *) TARGET_DIR="$arg" ;;
    esac
done

# Check source
if [ ! -f "$SKILL_SRC/skill.md" ]; then
    echo -e "${RED}Error: skill source not found.${NC}"
    echo "Run this script from the opc-starter-kit repository root."
    exit 1
fi

# Global install
if [ "$GLOBAL" = true ]; then
    DEST="${HOME}/.comate/skills/${SKILL_NAME}"
    echo -e "${YELLOW}Installing globally → ${DEST}${NC}"
    mkdir -p "$(dirname "$DEST")"
    rm -rf "$DEST"
    cp -r "$SKILL_SRC" "$DEST"
    echo -e "${GREEN}✅ Done. Type 'opc' in any Comate project.${NC}"
    exit 0
fi

# Project install
[ -z "$TARGET_DIR" ] && TARGET_DIR="$(pwd)"

if [ ! -d "$TARGET_DIR" ]; then
    echo -e "${RED}Error: '$TARGET_DIR' does not exist.${NC}"
    exit 1
fi

DEST="${TARGET_DIR}/.codebuddy/skills/${SKILL_NAME}"
mkdir -p "$(dirname "$DEST")"
rm -rf "$DEST"
cp -r "$SKILL_SRC" "$DEST"
echo -e "${GREEN}✅ Installed → ${DEST}${NC}"

echo ""
echo -e "${GREEN}Done! Open your AI tool in '${TARGET_DIR}' and type:${NC} ${BLUE}opc${NC}"
echo ""
echo -e "Tip: For Cursor, Windsurf, Copilot, or other tools,"
echo -e "see ${BLUE}skills/opc-starter-kit/references/tool-adaptations.md${NC}"
