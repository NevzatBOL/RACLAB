import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("data/MNIST_data/", one_hot=True)
import cv2
import numpy as np

x=tf.placeholder(tf.float32,[None, 784])

W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))

y=tf.nn.softmax(tf.matmul(x,W)+b)

y_=tf.placeholder(tf.float32, [None, 10])
cross_entropy=tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess=tf.InteractiveSession()
tf.global_variables_initializer().run()

for _ in range(1000):
	batch_xs, batch_ys = mnist.train.next_batch(100)
	sess.run(train_step, feed_dict={x: batch_xs, y_:batch_ys})

correct_prediction=tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print sess.run(accuracy, feed_dict={x: mnist.test.images, y_:mnist.test.labels})

frame=cv2.imread("data/3.png")
img=cv2.resize(frame,(28,28))
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print img.shape
cizim=np.vectorize(lambda x:255 -x)(np.ndarray.flatten(img))
sonuc=sess.run(tf.argmax(y,1),feed_dict={x : [cizim]})
print sonuc
