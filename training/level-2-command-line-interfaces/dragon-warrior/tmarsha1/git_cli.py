"""
This module provides a CLI that copies files using the 
Click third-party library.
"""

import click

import git_ops

    
@click.group()
def git_cli():
    pass
        
        
@git_cli.command()
@click.argument('remote')
def fetch(remote):
    git_ops.git_fetch(remote)
    
    
@git_cli.command()
@click.argument('remote_branch')
def merge(remote_branch):
    git_ops.git_merge(remote_branch)

    
if __name__ == '__main__':
    git_cli()
    
