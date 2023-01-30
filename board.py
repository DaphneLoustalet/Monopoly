# build the game board
from graphics import *
win = GraphWin()
win.setBackground('paleturquoise')
pt = Point(100, 100)
# draw the specified point
outlowDiag = Point(0, 0)
# draw upper diagonal point
outhighDiag = Point(200, 200)
# draw the outer rectangle
outerRect = Rectangle(outlowDiag, outhighDiag)
# draw lower diagonal point
inlowDiag = Point(18, 18)
# draw upper diagonal point
inhighDiag = Point(182, 182)
# draw the inner rectangle
innerRect = Rectangle(inlowDiag, inhighDiag)
innerRect.draw(win)

# BOTTOM
# Go Square
golowDiag = Point(182, 182)
gohighDiag = Point(200, 200)
goRect = Rectangle(golowDiag, gohighDiag)
goRect.draw(win)
goLabel = Text(Point(191,191), 'GO')
goLabel.setTextColor('red')
goLabel.setStyle('bold')
goLabel.setSize(10)
goLabel.draw(win)

# Mediterranean Ave (Purple)
MedilowDiag = Point(164, 182)
MedihighDiag = Point(182, 200)
MediRect = Rectangle(MedilowDiag, MedihighDiag)
MediRect.draw(win)
MediLabel = Text(Point(173, 191), '1')
MediLabel.setTextColor('purple')
MediLabel.setStyle('bold')
MediLabel.setSize(10)
MediLabel.draw(win)
# if this is drawn 
# print('Mediterranean Ave')

# Community Chest
CC1lowDiag = Point(146, 182)
CC1highDiag = Point(164, 200)
CC1Rect = Rectangle(CC1lowDiag, CC1highDiag)
CC1Rect.draw(win)
CC1Label = Text(Point(155, 191), 'CC')
CC1Label.setTextColor('dodgerblue')
CC1Label.setStyle('bold')
CC1Label.setSize(10)
CC1Label.draw(win)
# if this is drawn
# print('Community Chest')

# Baltic Ave (Purple)
BallowDiag = Point(128, 182)
BalhighDiag = Point(146, 200)
BalRect = Rectangle(BallowDiag, BalhighDiag)
BalRect.draw(win)
BalLabel = Text(Point(137, 191), '2')
BalLabel.setTextColor('purple')
BalLabel.setStyle('bold')
BalLabel.setSize(10)
BalLabel.draw(win)

# Income Tax
TaxlowDiag = Point(110, 182)
TaxhighDiag = Point(128, 200)
TaxRect = Rectangle(TaxlowDiag, TaxhighDiag)
TaxRect.draw(win)
TaxLabel = Text(Point(119, 191), 'T')
TaxLabel.setTextColor('gray')
TaxLabel.setStyle('bold')
TaxLabel.setSize(10)
TaxLabel.draw(win)

# Reading Railroad (Black)
RRlowDiag = Point(92, 182)
RRhighDiag = Point(110, 200)
RRRect = Rectangle(RRlowDiag, RRhighDiag)
RRRect.draw(win)
RRLabel = Text(Point(101, 191), 'RR')
RRLabel.setTextColor('black')
RRLabel.setStyle('bold')
RRLabel.setSize(10)
RRLabel.draw(win)

# Oriental Ave (Light Blue)
OrilowDiag = Point(74, 182)
OrihighDiag = Point(92, 200)
OriRect = Rectangle(OrilowDiag, OrihighDiag)
OriRect.draw(win)
OriLabel = Text(Point(83, 191), '3')
OriLabel.setTextColor('blue')
OriLabel.setStyle('bold')
OriLabel.setSize(10)
OriLabel.draw(win)

# Chance
C1lowDiag = Point(56, 182)
C1highDiag = Point(74, 200)
C1Rect = Rectangle(C1lowDiag, C1highDiag)
C1Rect.draw(win)
C1Label = Text(Point(65, 191), '?')
C1Label.setTextColor('magenta')
C1Label.setStyle('bold')
C1Label.setSize(10)
C1Label.draw(win)

# Vermont Ave (Light Blue)
VerlowDiag = Point(38, 182)
VerhighDiag = Point(56, 200)
VerRect = Rectangle(VerlowDiag, VerhighDiag)
VerRect.draw(win)
VerLabel = Text(Point(47, 191), '4')
VerLabel.setTextColor('blue')
VerLabel.setStyle('bold')
VerLabel.setSize(10)
VerLabel.draw(win)

# Connecticut Ave (Light Blue)
ConlowDiag = Point(18, 182)
ConhighDiag = Point(38, 200)
ConRect = Rectangle(ConlowDiag, ConhighDiag)
ConRect.draw(win)
ConLabel = Text(Point(29, 191), '5')
ConLabel.setTextColor('blue')
ConLabel.setStyle('bold')
ConLabel.setSize(10)
ConLabel.draw(win)

# Jail
JaillowDiag = Point(0, 182)
JailhighDiag = Point(18, 200)
JailRect = Rectangle(JaillowDiag, JailhighDiag)
JailRect.draw(win)
JailLabel = Text(Point(9, 191), 'J')
JailLabel.setTextColor('silver')
JailLabel.setStyle('bold')
JailLabel.setSize(10)
JailLabel.draw(win)

# LEFT SIDE
# St. Charles Place (Pink)
SClowDiag = Point(0, 164)
SChighDiag = Point(18, 182)
SCRect = Rectangle(SClowDiag, SChighDiag)
SCRect.draw(win)
SCLabel = Text(Point(9, 173), '6')
SCLabel.setTextColor('pink')
SCLabel.setStyle('bold')
SCLabel.setSize(10)
SCLabel.draw(win)

# Electric Company
EllowDiag = Point(0, 146)
ElhighDiag = Point(18, 164)
ElRect = Rectangle(EllowDiag, ElhighDiag)
ElRect.draw(win)
ElLabel = Text(Point(9, 155), 'EC')
ElLabel.setTextColor('white')
ElLabel.setStyle('bold')
ElLabel.setSize(10)
ElLabel.draw(win)

# States Ave (Pink)
StlowDiag = Point(120, 180)
SthighDiag = Point(140, 200)
StRect = Rectangle(BallowDiag, BalhighDiag)
StRect.draw(win)
StLabel = Text(Point(130, 190), '2')
StLabel.setTextColor('purple')
StLabel.setStyle('bold')
StLabel.setSize(10)
StLabel.draw(win)

## Virginia Ave (Pink)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Pennsylvania Railroad (Black)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## St. James Place (Orange)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Community Chest
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Tennessee Ave (Orange)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## New York Ave (Orange)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Free Parking
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## TOP
## Kentucky Ave (Red)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Chance
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Indiana Ave (Red)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Illinois Ave (Red)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## B&O Railroad
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Atlantic Ave (Yellow)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Ventnor Ave (Yellow)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Water Works
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Marvin Gardens (Yellow)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Go To Jail
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## RIGHT
## Pacific Ave (Green)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## North Carolina Ave (Green)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Community Chest
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Pennsylvania Ave (Green)
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Short Line
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Chance
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Park Place
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Luxury Tax
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
##
## Boardwalk
##BallowDiag = Point(120, 180)
##BalhighDiag = Point(140, 200)
##BalRect = Rectangle(BallowDiag, BalhighDiag)
##BalRect.draw(win)
##BalLabel = Text(Point(130, 190), '2')
##BalLabel.setTextColor('purple')
##BalLabel.setStyle('bold')
##BalLabel.setSize(10)
##BalLabel.draw(win)
