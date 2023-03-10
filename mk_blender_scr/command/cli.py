import click
from ase.io import read,Trajectory,iread
from pathlib import Path

from mk_blender_scr.blender.make_script import create, BallAndStick, Stick, SpaceFilling, Animation
import mk_blender_scr.blender.default as default

@click.group()
def main():
    pass

@main.command('docs')
def document():
    import webbrowser
    print("Showing documents page in browser...")
    url = "https://shimi-lab.github.io/mk-blender-scr_Document/"
    webbrowser.open(url, new=0, autoraise=True)

@main.command('BallAndStick') 
@click.argument('file')
@click.option('-f','--format',default=None)
@click.option('-o','--outfile',default="-")
@click.option('-b','--bicolor',type=bool,default=default.bicolor)
@click.option('-c','--cartoon',type=bool,default=False)
@click.option('-r','--radius',type=float,default=default.radius)
@click.option('-i','--indices',type=int,default=None)
@click.option('-s','--scale',type=float,default=default.scale)
@click.option('-ss','--subdivision_surface',type=bool,default=False)
def ball_and_stick(file,format,outfile,bicolor,cartoon,radius,indices,scale,):
    atoms = read(file,format=format)
    cartoon = {"apply":cartoon}
    subdivision_surface = {"apply":subdivision_surface}
    pyscript = create(
        outfile,
        BallAndStick(
            atoms,
            bicolor=bicolor,
            cartoon=cartoon,
            radius=radius,
            indices=indices,
            scale=scale,
            subdivision_surface=subdivision_surface))
    if outfile == "-":
        print(pyscript)

@main.command('Stick') 
@click.argument('file')
@click.option('-f','--format',default=None)
@click.option('-o','--outfile',default="-")
@click.option('-b','--bicolor',type=bool,default=default.bicolor)
@click.option('-c','--cartoon',type=bool,default=False)
@click.option('-r','--radius',type=float,default=default.radius)
@click.option('-i','--indices',type=int,default=None)
@click.option('-ss','--subdivision_surface',type=bool,default=False)
def stick(file,format,outfile,bicolor,cartoon,radius,indices,subdivision_surface):
    atoms = read(file,format=format)
    cartoon = {"apply":cartoon}
    subdivision_surface = {"apply":subdivision_surface}
    pyscript = create(
        outfile,
        Stick(
            atoms,
            bicolor=bicolor,
            cartoon=cartoon,
            radius=radius,
            subdivision_surface=subdivision_surface,
            indices=indices))
    if outfile == "-":
        print(pyscript)
    
@main.command('SpaceFilling') 
@click.argument('file')
@click.option('-f','--format',default=None)
@click.option('-o','--outfile',default="-")
@click.option('-c','--cartoon',type=bool,default=False)
@click.option('-i','--indices',type=int,default=None)
@click.option('-s','--scale',type=float,default=default.space_filling_scale)
@click.option('-ss','--subdivision_surface',type=bool,default=False)
def spacefilling(file,format,outfile,cartoon,indices,scale,subdivision_surface):
    atoms = read(file,format=format)
    cartoon = {"apply":cartoon}
    subdivision_surface = {"apply":subdivision_surface}
    pyscript = create(
        outfile,
        SpaceFilling(
            atoms,
            cartoon=cartoon,
            indices=indices,
            scale=scale,
            subdivision_surface=subdivision_surface,
            ))
    if outfile == "-":
        print(pyscript)
    
@main.command('Animation') 
@click.argument('file')
@click.option('-f','--format',default=None)
@click.option('-o','--outfile',default="Animations.zip")
@click.option('-c','--cartoon',type=bool,default=False)
@click.option('-i','--indices',type=int,default=None)
@click.option('-s','--scale',type=float,default=default.space_filling_scale)
@click.option('-ss','--subdivision_surface',type=bool,default=False)
@click.option('-step',type=int,default=default.step)
@click.option('-start',type=int,default=default.start)
def animation(file,format,outfile,cartoon,indices,scale,subdivision_surface,step,start):
    if Path(outfile).suffix == ".traj":
        images = Trajectory(file)
    else:
        images = list(iread(file))
    cartoon = {"apply":cartoon}
    subdivision_surface = {"apply":subdivision_surface}
    create(outfile,
           Animation(
               images,
               cartoon=cartoon,
               indices=indices,
               scale=scale,
               subdivision_surface=subdivision_surface,
               step=step,
               start=start
               ))
    
if __name__ == '__main__':
    main()