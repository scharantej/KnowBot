
@app.route('/cloud_orchestration/kubernetes_engine')
def kubernetes_engine():
    """Kubernetes Engine overview page."""
    return render_template('cloud_orchestration/kubernetes_engine/index.html')
