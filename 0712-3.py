from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlock(x,y-1,z+1,206)
mc.setBlock(x+1,y-1,z+1,206)
mc.setBlock(x+2,y-1,z+1,206)
mc.setBlock(x,y-1,z,206)
mc.setBlock(x+2,y-1,z,206)
mc.setBlock(x,y-1,z-1,206)
mc.setBlock(x+1,y-1,z-1,206)
mc.setBlock(x+2,y-1,z-1,206)

mc.setBlock(x+1,y-1,z,11)