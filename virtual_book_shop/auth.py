"""Routes for user authentication."""
from flask import Blueprint
from flask import Blueprint, render_template, request
from .forms import SignupForm

# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # Login route logic goes here
    return


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    def signup():
        """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = SignupForm()
    if form.validate_on_submit():
        # User sign-up logic will go here.
        ...
    return render_template(
        'signup.jinja2',
        title='Create an Account.',
        form=form,
        template='signup-page',
        body="Sign up for a user account."
    )