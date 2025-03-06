from flask import Blueprint, render_template

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin')
def admin_dashboard():
    return render_template('admin/dashboard.html')