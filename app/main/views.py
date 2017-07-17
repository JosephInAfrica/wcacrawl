from . import main
from .. import db
from ..models import Company, Contact


@main.route('/',methods=['GET','POST'])
def index():
	return 'Hello world.'