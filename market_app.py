from flask import Flask
from market_analysis import MarketAnalyzer, IndexOptionsAnalyzer, OptionsGreeksCalculator, OptionsStrategyGenerator
import logging

def create_app(config=None):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Apply configuration
    if config:
        app.config.update(config)
    
    # Initialize components
    market_analyzer = MarketAnalyzer()
    options_analyzer = IndexOptionsAnalyzer(OptionsGreeksCalculator())
    strategy_generator = OptionsStrategyGenerator()
    
    # Rest of the original routing and configuration code from the previous app.py
    @app.route('/health')
    def health_check():
        return jsonify(APIResponse(
            status='success',
            message='Service is healthy'
        ).to_dict()), 200

    # Include all the other routes like /api/v1/analyze, etc.

    return app