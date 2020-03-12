{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Let's create, process a dataframe with 100M claims records\n",
    "# Do some data processing on it \n",
    "\n",
    "# Idea: My New $300 Data Science PC only have 16GB of RAM.\n",
    "# How to do Data Engineering on any budget?\n",
    "# Answer: To process them pieces at a time :)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import random\n",
    "import math\n",
    "import h5py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_size = 1000000000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1000000000\n"
     ]
    }
   ],
   "source": [
    "# number of records to process\n",
    "print(sample_size)\n",
    "\n",
    "# at each iteration i shall process only 1M rows\n",
    "# so I don't crash my Linux machine and server\n",
    "loop_size = 10000000\n",
    "loop_count = math.ceil(sample_size/loop_size)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "def method_01_for_loop(loop_size, loop_count):\n",
    "    for i in range(loop_count):\n",
    "        # write feedback to user on the same line\n",
    "        print('\\r>> processing: {0:.2f}%'.format(i/loop_count*100), sep='', end='')\n",
    "\n",
    "        with open('DW_Claim.txt', 'a') as f:\n",
    "            # this does not work if your range is smaller than sample size\n",
    "            # member_numbers = random.sample(range(99999), loop_size)\n",
    "\n",
    "            member_numbers = [str(int(9999 * random.random())) for _ in range(loop_size)]\n",
    "\n",
    "            for number in member_numbers:\n",
    "                f.write(number)\n",
    "                f.write('\\n')\n",
    "\n",
    "            member_numbers = None\n",
    "        \n",
    "# But this is really really slow, how can I do better?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# https://stackoverflow.com/a/27384379\n",
    "# writing a block of code at once\n",
    "\n",
    "def method_02_write_block(loop_size, loop_count):\n",
    "    for i in range(loop_count):\n",
    "        # write feedback to user on the same line\n",
    "        print('\\r>> processing: {0:.2f}%'.format(i/loop_count*100), sep='', end='')\n",
    "\n",
    "        with open('DW_Claim_2.txt', 'a') as f:\n",
    "            f.write('\\n'.join([str(int(9999 * random.random())) for _ in range(loop_size)]))\n",
    "        \n",
    "# What is the effect on how much to \"tune\" your program?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reference link\n",
    "# https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.randint.html#numpy.random.randint\n",
    "\n",
    "def method_03_hdf5(loop_size, loop_count):\n",
    "    s = pd.Series(np.random.randint(1000, 9999, size=loop_size, dtype='int16'))\n",
    "    f = h5py.File('myfile.hdf5','w')\n",
    "    group = f.create_group('a_group')\n",
    "    group.create_dataset(name='matrix', data=s, chunks=True, compression='gzip')\n",
    "    f.close()\n",
    "    s = None\n",
    "\n",
    "# How to print percentage to 2 decimal points?\n",
    "# https://stackoverflow.com/a/455634\n",
    "\n",
    "# How to print on the same line\n",
    "# https://stackoverflow.com/q/7715594"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">> processing: 90.00%CPU times: user 1min 6s, sys: 2.44 s, total: 1min 9s\n",
      "Wall time: 1min 9s\n"
     ]
    }
   ],
   "source": [
    "%time method_01_for_loop(10000000, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">> processing: 90.00%CPU times: user 42.7 s, sys: 2.32 s, total: 45 s\n",
      "Wall time: 45.1 s\n"
     ]
    }
   ],
   "source": [
    "%time method_02_write_block(10000000, 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CPU times: user 6.33 s, sys: 196 ms, total: 6.52 s\n",
      "Wall time: 9.95 s\n"
     ]
    }
   ],
   "source": [
    "%time method_03_hdf5(100000000, 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7f09cadd5f10>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlAAAAJNCAYAAAD+qksAAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAepElEQVR4nO3dfbRld13f8c83mcAEEg0JQ1ZkjBNoeNJAIpNIAspDJKAgRHkubYNCU7sEAaXtVK3iQzVqK49amsVTdIEEkZQIVgghAU0iYUJCeBhoBCOMCWQYQB6DBn794+wJl+HOzP3O3Jt7JvN6rZV1zt5n73N+J+ucO++797571xgjAAAs3UGrPQAAgP2NgAIAaBJQAABNAgoAoElAAQA0CSgAgKY1t+WL3fWudx0bNmy4LV8SAGCvXHXVVZ8dY6xb7LHbNKA2bNiQzZs335YvCQCwV6rqH3b1mF14AABNAgoAoElAAQA03abHQAEA8+9f/uVfsnXr1tx8882rPZTbxNq1a7N+/foccsghS15HQAEA32br1q05/PDDs2HDhlTVag9nRY0xsn379mzdujXHHXfcktezCw8A+DY333xzjjrqqNt9PCVJVeWoo45qb20TUADAdzgQ4mmHvXmvduEBAHNl+/btOf3005Mkn/70p3PwwQdn3brZ+SzvdKc75fLLL1/N4SURUADAHmzY9LZlfb7rz3nMbh8/6qijcs011yRJXvjCF+awww7LC17wgmUdw76yCw8A2G8cdthhSZJLL700D33oQ/PkJz8597rXvbJp06a87nWvyymnnJITTjghH//4x5Mk27ZtyxOe8IScfPLJOfnkk3PZZZctyzhsgQIA9ksf+MAHsmXLlhx55JG5xz3ukWc961m58sor85KXvCQve9nL8uIXvzjPfe5z8/znPz8PechD8slPfjKPetSjsmXLln1+bQEFAOyXTj755BxzzDFJknve854544wzkiQnnHBCLrnkkiTJO9/5znzkIx+5dZ0vfvGL+dKXvpTDDz98n15bQAEA+6U73vGOt94/6KCDbp0+6KCDcssttyRJvvnNb+aKK67IoYceuqyvvcdjoKrq3lV1zYL/vlhVz6uqI6vqoqq6brq9y7KODABgH51xxhl5+ctffuv0joPT99UeA2qM8bExxoljjBOTPDDJV5Nc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\n",
      "text/plain": [
       "<Figure size 720x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Execution Time Analysis for 100M rows generate\n",
    "df = pd.DataFrame([['For Loop Write', 69],\n",
    "                  ['For Loop Block Write', 45],\n",
    "                  ['HDF5 Write', 9.95]], columns=['Method', 'Time'])\n",
    "\n",
    "df.plot.bar(x='Method', y='Time', figsize=(10, 10), rot=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
