# src/website/routes/main_routes.py
from flask import Blueprint, jsonify, request
from website.models.database import SessionLocal
from website.models.hotel import Hotel
from ai_agent.crew import AiAgent


main_routes = Blueprint('main_routes', __name__)
