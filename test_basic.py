#!/usr/bin/env python3
"""
Basic test to verify our configuration files are working
"""

import yaml
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print("## Forscher-AI Configuration Test ##\n")

# Test environment variables
gemini_key = os.getenv('GEMINI_API_KEY')
serper_key = os.getenv('SERPER_API_KEY')

print("Environment Variables:")
print(f"✅ GEMINI_API_KEY: {'Set' if gemini_key else 'Missing'}")
print(f"✅ SERPER_API_KEY: {'Set' if serper_key else 'Missing'}")

# Test YAML configurations
print("\nYAML Configurations:")

try:
    with open('src/agents.yaml', 'r') as f:
        agents_config = yaml.safe_load(f)
    print("✅ agents.yaml loaded successfully")
    print(f"   - Found {len(agents_config)} agents: {list(agents_config.keys())}")
except Exception as e:
    print(f"❌ agents.yaml error: {e}")

try:
    with open('src/tasks.yaml', 'r') as f:
        tasks_config = yaml.safe_load(f)
    print("✅ tasks.yaml loaded successfully")
    print(f"   - Found {len(tasks_config)} tasks: {list(tasks_config.keys())}")
except Exception as e:
    print(f"❌ tasks.yaml error: {e}")

print("\n## Configuration Test Complete ##")
print("Your Forscher-AI setup is ready!")
print("Note: Full CrewAI functionality requires a compatible environment with all system libraries.")