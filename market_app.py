from flask import Flask, jsonify
import os
from market_analysis import (
    MarketAnalyzer, 
    IndexOptionsAnalyzer, 
    OptionsGreeksCalculator, 
    OptionsStrategyGenerator,
    APIResponse  # Include any other necessary classes
)

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
    
    # Copy all the route definitions from the original app.py
    @app.route('/health')
    def health_check():
        return jsonify(APIResponse(
            status='success',
            message='Service is healthy'
        ).to_dict()), 200

    # Add other routes from the original app.py

    return app