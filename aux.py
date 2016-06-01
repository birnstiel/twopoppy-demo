import scipy.constants as sc

AU           = sc.au*1e2;               # astronomical unit in cm
year         = sc.Julian_year;          # year in s

def better_plots(back='w',front='k',fs=15,cmap='viridis',lw=1,sans=False,\
	usetex=False,brewer=True,rcargs={}):
    """
    set matplotlib parameters to get an improved look
    
    Keywords:
    ---------
    
    back : [*'k'* | color]
        the background color of the axes and the figure
    
    front : [*'w'* | color]
        the foreground color of the axes, lines, font, ...
    
    fs : [*12* | int]
        the default font size 

    lw : float
        line width modifier (1 is already somewhat thicker than default) 

    brewer : bool
        wether to use normal colors or brewer colors 
    
    cmap : [*'spectral'* | colormap]
        the default colormap to be used

    sans : [*False* | True]
		whether to use sans-serif font family or not
    
    usetex : [*False* | True]
        whether tex-fonts are used by default. This also sets the fonts to have
        a consistent look, but makes plotting quite a lot slower
    
    Example:
    
        for usetex in [False,True]:
            for sans in [False,True]:
                better_plots(usetex=usetex,sans=sans)
                figure()
                title('usetex = {:}, sans = {:}'.format(usetex,sans))
                plot(sin(linspace(0,2*pi,100)))
                xlabel(r'$x$ [m]')
                ylabel(r'$\alpha$ [$\mu$m]')
                draw()
                pause(5)
    """
    from matplotlib.pyplot import rcParams, rcParamsDefault, rc, cycler, rc_context, rcdefaults
    import brewer2mpl
    
    context = rc_context()
    #rcdefaults()
    
    dark2_colors = brewer2mpl.get_map('Dark2', 'Qualitative', 8).mpl_colors
    
    rcParams['figure.facecolor']            = back
    rcParams['axes.edgecolor']              = front
    rcParams['axes.facecolor']              = back
    rcParams['axes.linewidth']              = 1.5*lw
    rcParams['axes.labelcolor']             = front
    rcParams['axes.prop_cycle']             = cycler('color',[front, 'g', 'r', 'c', 'm', 'y']*(not brewer)+brewer*dark2_colors)
    rcParams['axes.formatter.limits']       = [-10000,10000]
    rcParams['axes.formatter.use_mathtext'] = True
    rcParams['xtick.color']                 = front
    rcParams['ytick.color']                 = front
    rcParams['xtick.major.size']            = 6*lw
    rcParams['ytick.major.size']            = 6*lw
    rcParams['ytick.major.width']           = 1*lw
    rcParams['xtick.major.width']           = 1*lw
    rcParams['xtick.minor.size']            = 3*lw
    rcParams['ytick.minor.size']            = 3*lw
    rcParams['ytick.minor.width']           = 0.75*lw
    rcParams['xtick.minor.width']           = 0.75*lw
    rcParams['lines.linewidth']             = 1.5*lw
    rcParams['image.cmap']                  = cmap
    rcParams['font.size']                   = fs
    rcParams['text.color']                  = front
    rcParams['savefig.facecolor']            = back
    #
    # avoid tick labels overlapping with the axes for large fonts
    #
    if fs > 16:
        rcParams['xtick.major.pad']='6'
        rcParams['ytick.major.pad']='6'
    #
    # make tex and non-tex text look similar
    #
    if sans > 0:
        if sans==1:
            rcParams['mathtext.fontset']='stixsans'
        elif sans==2:
            rcParams['mathtext.fontset'] = 'custom'
            rcParams['font.family'] = 'sans-serif'
            rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
            rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
            rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
    else:
        rcParams['mathtext.fontset'] = 'stix'
        rcParams['font.family']      = 'STIXGeneral'
        rcParams['mathtext.rm']      = rcParamsDefault['mathtext.rm']
        rcParams['mathtext.it']      = rcParamsDefault['mathtext.it'] 
        rcParams['mathtext.bf']      = rcParamsDefault['mathtext.bf'] 
    #
    # the tex settings
    #
    rcParams['text.usetex']=usetex
    if usetex:
        rcParams['text.latex.preamble']         = [r"\usepackage{amsmath}"]
        if sans:
            rcParams['text.latex.preamble'] += [r"\usepackage{cmbright}"]
            rc('font',**{'family':'sans-serif',\
                         'sans-serif':['Bitstream Vera Sans']})
        else:
            rc('font',**{'family':'serif',\
                         'serif':'Computer Modern Roman',\
                         'sans-serif':'Computer Modern Sans serif',\
                         'monospace':'Computer Modern Typewriter'})
    else:
        rcParams['text.latex.preamble']         = ['']
        
    # process other kwargs
    for k,v in rcargs.iteritems():
        if k in rcParams.keys():
            rcParams[k]=v
    return context
    
    