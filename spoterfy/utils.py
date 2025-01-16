import click
import sys
from functools import wraps

def handle_keyboard_interrupt(f):
    """Decorator to handle keyboard interrupts consistently across commands"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except KeyboardInterrupt:
            click.echo("\nAborted!", err=True, color=True)
            sys.exit(1)
    return wrapper

def suppress_inquirer_stderr(f):
    """Decorator to suppress inquirer's stderr output during prompts"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        stderr = sys.stderr
        sys.stderr = open('/dev/null', 'w')
        try:
            return f(*args, **kwargs)
        finally:
            sys.stderr = stderr
    return wrapper 