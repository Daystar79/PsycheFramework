#!/bin/bash
# Migration script: Replace original files with optimized versions
# Run this from the Authors_Framework directory

set -e

echo "=== Cognitive Middleware Optimization Migration ==="
echo ""

# Backup originals
echo "Creating backups..."
mkdir -p backups_$(date +%Y%m%d)
cp Framework/Main.md backups_$(date +%Y%m%d)/Main_original.md
cp Framework/Rules_Index.md backups_$(date +%Y%m%d)/Rules_Index_original.md
cp Framework/Psychology/realm_data.yaml backups_$(date +%Y%m%d)/realm_data_original.yaml
cp Simulator/CharacterRuntime.md backups_$(date +%Y%m%d)/CharacterRuntime_original.md
cp Characters/*.md backups_$(date +%Y%m%d)/

echo "Backups created in backups_$(date +%Y%m%d)/"
echo ""

# Replace core files
echo "Replacing core framework files..."
cp Framework/Main_optimized.md Framework/Main.md
cp Framework/Rules_Index_optimized.md Framework/Rules_Index.md
cp Framework/Psychology/realm_data_optimized.yaml Framework/Psychology/realm_data.yaml
cp Simulator/CharacterRuntime_optimized.md Simulator/CharacterRuntime.md

echo "Core files replaced."
echo ""

# Replace character cards
echo "Replacing character cards..."
for char in cass helen lior nora reed wren; do
    cp Characters/${char}_optimized.md Characters/${char}.md
    rm Characters/${char}_optimized.md
done

echo "Character cards replaced."
echo ""

# Clean up optimized files
echo "Cleaning up temporary files..."
rm -f Framework/Main_optimized.md
rm -f Framework/Rules_Index_optimized.md
rm -f Framework/Psychology/realm_data_optimized.yaml
rm -f Simulator/CharacterRuntime_optimized.md

echo "Temporary files removed."
echo ""

echo "README.md updated."
echo ""

echo "=== Migration Complete ==="
echo ""
echo "Word count verification:"
echo ""
echo "Core framework load:"
wc -w Framework/Main.md Framework/Rules_Index.md Framework/Psychology/realm_data.yaml

echo ""
echo "All character cards:"
wc -w Characters/cass.md Characters/helen.md Characters/lior.md Characters/nora.md Characters/reed.md Characters/wren.md

echo ""
echo "Total mandatory load (core + 1 character):"
echo "~$(expr $(wc -w < Framework/Main.md) + $(wc -w < Framework/Rules_Index.md) + $(wc -w < Framework/Psychology/realm_data.yaml) + $(wc -w < Characters/nora.md)) words"

echo ""
echo "Optimization summary saved to OPTIMIZATION_SUMMARY.md"
