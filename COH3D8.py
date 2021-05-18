# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(15.0, 15.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Solid', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Solid'].BaseSolidExtrude(depth=2.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(15.0, 15.0))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Cohesive', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Cohesive'].BaseSolidExtrude(depth=1.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='Solid')
mdb.models['Model-1'].materials['Solid'].Elastic(table=((350000.0, 0.3), ))
mdb.models['Model-1'].Material(name='Cohesive')
mdb.models['Model-1'].materials['Cohesive'].QuadsDamageInitiation(table=((25.0, 
    30.0, 30.0), ))
mdb.models['Model-1'].materials['Cohesive'].quadsDamageInitiation.DamageEvolution(
    mixedModeBehavior=BK, power=2.07, table=((0.24, 0.59, 0.59), ), type=
    ENERGY)
mdb.models['Model-1'].materials['Cohesive'].Elastic(table=((1000000.0, 
    1500000.0, 1500000.0), ), type=TRACTION)
mdb.models['Model-1'].CohesiveSection(initialThicknessType=GEOMETRY, material=
    'Cohesive', name='Cohesive', outOfPlaneThickness=None, response=
    TRACTION_SEPARATION)
mdb.models['Model-1'].HomogeneousShellSection(idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, material='Solid', name='Solid', 
    nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
    preIntegrate=OFF, temperature=GRADIENT, thickness=2.0, thicknessField='', 
    thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
mdb.models['Model-1'].parts['Cohesive'].Set(cells=
    mdb.models['Model-1'].parts['Cohesive'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Cohesive'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Cohesive'].sets['Set-1'], sectionName=
    'Cohesive', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Solid'].Set(cells=
    mdb.models['Model-1'].parts['Solid'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), name='Set-1')
mdb.models['Model-1'].parts['Solid'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Solid'].sets['Set-1'], sectionName='Solid', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Solid-1', part=
    mdb.models['Model-1'].parts['Solid'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Solid-2', part=
    mdb.models['Model-1'].parts['Solid'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Cohesive-1', 
    part=mdb.models['Model-1'].parts['Cohesive'])
mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].translateTo(
    clearance=0.0, direction=(0.0, 0.0, -1.0), fixedList=(
    mdb.models['Model-1'].rootAssembly.instances['Solid-1'].faces[5], ), 
    movableList=(
    mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].faces[4], ))
mdb.models['Model-1'].rootAssembly.instances['Solid-2'].translateTo(clearance=
    0.0, direction=(0.0, 0.0, -1.0), fixedList=(
    mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].faces[5], ), 
    movableList=(
    mdb.models['Model-1'].rootAssembly.instances['Solid-2'].faces[4], ))
mdb.models['Model-1'].rootAssembly.Set(name='P1', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].vertices.getSequenceFromMask(
    ('[#10 ]', ), ))
mdb.models['Model-1'].rootAssembly.Set(name='P2', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].vertices.getSequenceFromMask(
    ('[#20 ]', ), ))
mdb.models['Model-1'].rootAssembly.Set(name='P3', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Solid-1'].vertices.getSequenceFromMask(
    ('[#10 ]', ), ))
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Solid-1'].faces.getSequenceFromMask(
    ('[#20 ]', ), ), name='Solid-1_bot')
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].faces.getSequenceFromMask(
    ('[#10 ]', ), ), name='Cohesive_top')
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].faces.getSequenceFromMask(
    ('[#20 ]', ), ), name='Cohesive_bot')
mdb.models['Model-1'].rootAssembly.Set(faces=
    mdb.models['Model-1'].rootAssembly.instances['Solid-2'].faces.getSequenceFromMask(
    ('[#10 ]', ), ), name='Solid-2_top')
mdb.models['Model-1'].Tie(adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE, 
    master=mdb.models['Model-1'].rootAssembly.sets['Solid-1_bot'], name='Top', 
    positionToleranceMethod=COMPUTED, slave=
    mdb.models['Model-1'].rootAssembly.sets['Cohesive_top'], thickness=ON, 
    tieRotations=ON)
del mdb.models['Model-1'].constraints['Top']
mdb.models['Model-1'].Tie(adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE, 
    master=Region(
    side1Faces=mdb.models['Model-1'].rootAssembly.instances['Solid-1'].faces.getSequenceFromMask(
    mask=('[#20 ]', ), )), name='Constraint-1', positionToleranceMethod=
    COMPUTED, slave=Region(
    side1Faces=mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), thickness=ON, tieRotations=ON)
mdb.models['Model-1'].Tie(adjust=ON, constraintEnforcement=SURFACE_TO_SURFACE, 
    master=Region(
    side1Faces=mdb.models['Model-1'].rootAssembly.instances['Solid-2'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), name='Constraint-2', positionToleranceMethod=
    COMPUTED, slave=Region(
    side1Faces=mdb.models['Model-1'].rootAssembly.instances['Cohesive-1'].faces.getSequenceFromMask(
    mask=('[#20 ]', ), )), thickness=ON, tieRotations=ON)
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-1', toName=
    'Top')
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-2', toName=
    'Bot')
mdb.models['Model-1'].parts['Solid'].seedEdgeByNumber(constraint=FINER, edges=
    mdb.models['Model-1'].parts['Solid'].edges.getSequenceFromMask(('[#fff ]', 
    ), ), number=1)
mdb.models['Model-1'].parts['Solid'].setElementType(elemTypes=(ElemType(
    elemCode=SC8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    hourglassControl=DEFAULT), ElemType(elemCode=SC6R, elemLibrary=STANDARD), 
    ElemType(elemCode=UNKNOWN_TET, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Solid'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), ))
mdb.models['Model-1'].parts['Solid'].generateMesh()
mdb.models['Model-1'].parts['Cohesive'].seedEdgeByNumber(constraint=FINER, 
    edges=mdb.models['Model-1'].parts['Cohesive'].edges.getSequenceFromMask((
    '[#fff ]', ), ), number=1)
mdb.models['Model-1'].parts['Cohesive'].assignStackDirection(cells=
    mdb.models['Model-1'].parts['Cohesive'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), referenceRegion=mdb.models['Model-1'].parts['Cohesive'].faces[4])
mdb.models['Model-1'].parts['Solid'].assignStackDirection(cells=
    mdb.models['Model-1'].parts['Solid'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), referenceRegion=mdb.models['Model-1'].parts['Solid'].faces[4])
mdb.models['Model-1'].parts['Cohesive'].setMeshControls(algorithm=
    ADVANCING_FRONT, regions=
    mdb.models['Model-1'].parts['Cohesive'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Cohesive'].setElementType(elemTypes=(ElemType(
    elemCode=COH3D8, elemLibrary=STANDARD), ElemType(elemCode=COH3D6, 
    elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TET, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Cohesive'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), ))
mdb.models['Model-1'].parts['Cohesive'].generateMesh()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].StaticStep(initialInc=0.1, maxInc=0.1, maxNumInc=1000, 
    minInc=1e-07, name='Step-1', previous='Initial', timePeriod=100.0)
mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
    'S', 'MISES', 'E', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 
    'CDISP', 'SDEG', 'DMICRT', 'CSQUADSCRT', 'STATUS'))
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', name=
    'H-Output-2', rebar=EXCLUDE, region=
    mdb.models['Model-1'].rootAssembly.sets['P3'], sectionPoints=DEFAULT, 
    variables=('U3', 'RF3'))
mdb.models['Model-1'].EncastreBC(createStepName='Step-1', localCsys=None, name=
    'Clamp', region=Region(
    faces=mdb.models['Model-1'].rootAssembly.instances['Solid-2'].faces.getSequenceFromMask(
    mask=('[#20 ]', ), )))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Step-1', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
    'Displ', region=Region(
    faces=mdb.models['Model-1'].rootAssembly.instances['Solid-1'].faces.getSequenceFromMask(
    mask=('[#10 ]', ), )), u1=0.0, u2=0.0, u3=0.1, ur1=UNSET, ur2=UNSET, ur3=
    UNSET)

