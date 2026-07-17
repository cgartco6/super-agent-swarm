#!/bin/bash
# Super Agent Swarm - Full Setup Script for Ubuntu 24.04 LTS
# Run with: bash setup_ubuntu.sh

set -e

echo "🚀 Starting Super Agent Swarm Setup on Ubuntu 24.04..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3 python3-pip python3-venv git curl

# Create project directory
PROJECT_DIR="$HOME/super-agent-swarm"
mkdir -p $PROJECT_DIR/ui
cd $PROJECT_DIR

echo "📥 Cloning / Creating project files..."
# (If you copied files manually, skip git clone)
# git clone https://github.com/yourusername/super-agent-swarm.git .  # or paste files

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file template
cat > .env << EOF
OPENAI_API_KEY=sk-your-key-here
EOF

echo "✅ Setup complete!"

# Make launch script
cat > launch.sh << 'EOL'
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
streamlit run ui/command_center.py --server.port 8501
EOL

chmod +x launch.sh

echo "🎉 Ready! Run ./launch.sh to start the Command Center"
echo "Access UI at: http://localhost:8501"
