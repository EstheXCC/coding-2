# Load the os library
import os
files = os.listdir('cat_data')
import matplotlib.pyplot as plt
import numpy as np

print(os.path.join('cat_data', files[0]))
plt.imread(os.path.join('cat_data', files[0]))

files = [os.path.join('cat_data', file_i)
 for file_i in os.listdir('cat_data')
 if '.jpg' in file_i]


img = plt.imread(files[4])

print(img)

plt.imshow(img)
plt.show()
print(img.shape)

plt.imshow(img[:, :, 0], cmap='gray') # Red Channel
plt.imshow(img[:, :, 1], cmap='gray') # Green Channel
plt.imshow(img[:, :, 2], cmap='gray') # Green Channel
plt.show()

imgs = [plt.imread(files[file_i])
        for file_i in range(10)]
plt.imshow(imgs[4])
plt.show()

print(imgs[4].shape)

data = np.array(imgs) # make 'data' = our numpy array
data.shape
print(data.shape)
print("The shape of our new 'data' object is a 'batch' of 100 images, with a height of 218, width of 178, and 3 colour channels")
print("If your images aren't all the same size to begin with, then this won't work!")

mean_img = np.mean(data, axis=0) # This is the mean of the 'batch' channel
plt.imshow(mean_img.astype(np.uint8))
print("look at this average person")
plt.show()
std_img = np.std(data, axis=0)
plt.imshow(std_img.astype(np.uint8))
print("This is the standard deviation - the variance of the mean")
plt.show()

plt.imshow(np.mean(std_img, axis=2).astype(np.uint8)) # Mean of all colour channels
print("Mean of all colour channels")
plt.show()

flattened = data.ravel()
print(data[:1])
print(flattened[:10])


print(plt.hist(flattened.ravel(), 255))
plt.show()

print(plt.hist(mean_img.ravel(), 255))
plt.show()
bins = 20
fig, axs = plt.subplots(1, 3, figsize=(12, 6), sharey=True, sharex=True)
axs[0].hist((data[0]).ravel(), bins)
axs[0].set_title('img distribution')
axs[1].hist((mean_img).ravel(), bins)
axs[1].set_title('mean distribution')
axs[2].hist((data[0] - mean_img).ravel(), bins)
axs[2].set_title('(img - mean) distribution')
plt.show()

fig, axs = plt.subplots(1, 3, figsize=(12, 6), sharey=True, sharex=True)
axs[0].hist((data[0] - mean_img).ravel(), bins)
axs[0].set_title('(img - mean) distribution')
axs[1].hist((std_img).ravel(), bins)
axs[1].set_title('std deviation distribution')
axs[2].hist(((data[0] - mean_img) / std_img).ravel(), bins)
axs[2].set_title('((img - mean) / std_dev) distribution')
plt.show()

axs[2].set_xlim([-150, 150])
axs[2].set_xlim([-100, 100])
axs[2].set_xlim([-50, 50])
axs[2].set_xlim([-10, 10])
axs[2].set_xlim([-5, 5])


import tensorflow._api.v2.compat.v1 as tf
tf.disable_v2_behavior()
x = np.linspace(-3.0, 3.0, 100)

x = np.linspace(-3.0, 3.0, 100)

# Immediately, the result is given to us.  An array of 100 numbers equally spaced from -3.0 to 3.0.
print(x)

# We know from numpy arrays that they have a `shape`, in this case a 1-dimensional array of 100 values
print(x.shape)

# and a `dtype`, in this case float64, or 64 bit floating point values.
print(x.dtype)

x = tf.linspace(-3.0, 3.0, 100)
print(x)

g = tf.get_default_graph()
print([op.name for op in g.get_operations()])
g.get_tensor_by_name('linspace/Slice' + ':0')
# We're first going to create a session:
sess = tf.Session()

# Now we tell our session to compute anything we've created in the tensorflow graph.
computed_x = sess.run(x)
print(computed_x)

# Alternatively, we could tell the previous Tensor to evaluate itself using this session:
computed_x = x.eval(session=sess)
print(computed_x)

# We can close the session after we're done like so:
sess.close()
sess = tf.Session(graph=g)
sess.close()
g2 = tf.Graph()
sess = tf.InteractiveSession()
x.eval()

# We can find out the shape of a tensor like so:
print(x.get_shape())

# %% Or in a more friendly format
print(x.get_shape().as_list())

mean = 0.0
sigma = 1.0

# Don't worry about trying to learn or remember this formula.  I always have to refer to textbooks or check online for the exact formula.
z = (tf.exp(tf.negative(tf.pow(x - mean, 2.0) /
                   (2.0 * tf.pow(sigma, 2.0)))) *
     (1.0 / (sigma * tf.sqrt(2.0 * 3.1415))))
res = z.eval()
plt.plot(res)
plt.show()

# Let's store the number of values in our Gaussian curve.
ksize = z.get_shape().as_list()[0]

# Let's multiply the two to get a 2d gaussian
z_2d = tf.matmul(tf.reshape(z, [ksize, 1]), tf.reshape(z, [1, ksize]))

# Execute the graph
plt.imshow(z_2d.eval())
plt.show()

