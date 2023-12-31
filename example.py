from py3dbp import Packer, Bin, Item
import matplotlib.pyplot as plt
import random

packer = Packer()

packer.add_bin(Bin('small-envelope', 11.5, 6.125, 0.25, 10))
packer.add_bin(Bin('large-envelope', 15.0, 12.0, 0.75, 15))
packer.add_bin(Bin('small-box', 8.625, 5.375, 1.625, 70.0))
packer.add_bin(Bin('medium-box', 11.0, 8.5, 5.5, 70.0))
packer.add_bin(Bin('medium-2-box', 13.625, 11.875, 3.375, 70.0))
packer.add_bin(Bin('large-box', 12.0, 12.0, 5.5, 70.0))
packer.add_bin(Bin('large-2-box', 23.6875, 11.75, 3.0, 70.0))

packer.add_item(Item('50g [powder 1]', 3.9370, 1.9685, 1.9685, 1))
packer.add_item(Item('50g [powder 2]', 3.9370, 1.9685, 1.9685, 2))
packer.add_item(Item('50g [powder 3]', 3.9370, 1.9685, 1.9685, 3))
packer.add_item(Item('250g [powder 4]', 7.8740, 3.9370, 1.9685, 4))
packer.add_item(Item('250g [powder 5]', 7.8740, 3.9370, 1.9685, 5))
packer.add_item(Item('250g [powder 6]', 7.8740, 3.9370, 1.9685, 6))
packer.add_item(Item('250g [powder 7]', 7.8740, 3.9370, 1.9685, 7))
packer.add_item(Item('250g [powder 8]', 7.8740, 3.9370, 1.9685, 8))
packer.add_item(Item('250g [powder 9]', 7.8740, 3.9370, 1.9685, 9))

packer.pack()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.bar3d(0, 0, 0, b.depth, b.width, b.height, shade=True, color='blue', alpha=0.1)
i = 0
for b in packer.bins:
    ax.bar3d(0, 0, 0, b.depth, b.width, b.height, shade=True, color='blue', alpha=0.1)
    print(b.depth, b.width, b.height)
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")
    for item in b.items:
        if i < 4:
            # print(item.position)
            x, y, z = item.position
            print(f"Coords: {x, y, z}")
            print(f"Size: {item.depth, item.width, item.height}")
            ax.bar3d(x, y, z, item.depth, item.width, item.height, shade=True, color=(random.random(), random.random(), random.random()), alpha=0.5)
            # print("====> ", item.string())
            i += 1
    print("UNFITTED ITEMS:")

    for item in b.unfitted_items:
        print(item.name)
        # print("====> ", item.string())
        pass
    print("***************************************************")
    print("***************************************************")

plt.show()