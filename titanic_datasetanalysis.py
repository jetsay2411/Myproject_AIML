{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv(\"titanic.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>male</td>\n",
       "      <td>27.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>female</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0              1         0       3   \n",
       "1              2         1       1   \n",
       "2              3         1       3   \n",
       "3              4         1       1   \n",
       "4              5         0       3   \n",
       "..           ...       ...     ...   \n",
       "886          887         0       2   \n",
       "887          888         1       1   \n",
       "888          889         0       3   \n",
       "889          890         1       1   \n",
       "890          891         0       3   \n",
       "\n",
       "                                                  Name     Sex        Age  \\\n",
       "0                              Braund, Mr. Owen Harris    male  22.000000   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.000000   \n",
       "2                               Heikkinen, Miss. Laina  female  26.000000   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.000000   \n",
       "4                             Allen, Mr. William Henry    male  35.000000   \n",
       "..                                                 ...     ...        ...   \n",
       "886                              Montvila, Rev. Juozas    male  27.000000   \n",
       "887                       Graham, Miss. Margaret Edith  female  19.000000   \n",
       "888           Johnston, Miss. Catherine Helen \"Carrie\"  female  29.699118   \n",
       "889                              Behr, Mr. Karl Howell    male  26.000000   \n",
       "890                                Dooley, Mr. Patrick    male  32.000000   \n",
       "\n",
       "     SibSp  Parch            Ticket     Fare Cabin Embarked  \n",
       "0        1      0         A/5 21171   7.2500   NaN        S  \n",
       "1        1      0          PC 17599  71.2833   C85        C  \n",
       "2        0      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3        1      0            113803  53.1000  C123        S  \n",
       "4        0      0            373450   8.0500   NaN        S  \n",
       "..     ...    ...               ...      ...   ...      ...  \n",
       "886      0      0            211536  13.0000   NaN        S  \n",
       "887      0      0            112053  30.0000   B42        S  \n",
       "888      1      2        W./C. 6607  23.4500   NaN        S  \n",
       "889      0      0            111369  30.0000  C148        C  \n",
       "890      0      0            370376   7.7500   NaN        Q  \n",
       "\n",
       "[891 rows x 12 columns]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "\n",
       "   Parch     Ticket     Fare Cabin Embarked  \n",
       "0      0  A/5 21171   7.2500   NaN        S  \n",
       "1      0   PC 17599  71.2833   C85        C  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)#top two rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.00</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.75</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass                   Name   Sex   Age  SibSp  \\\n",
       "889          890         1       1  Behr, Mr. Karl Howell  male  26.0      0   \n",
       "890          891         0       3    Dooley, Mr. Patrick  male  32.0      0   \n",
       "\n",
       "     Parch  Ticket   Fare Cabin Embarked  \n",
       "889      0  111369  30.00  C148        C  \n",
       "890      0  370376   7.75   NaN        Q  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(2)#bottom two rows"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Drop column by table name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "df.drop([\"Name\",\"Ticket\",\"Cabin\",\"Embarked\"], axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>7.2500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>71.2833</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass     Sex   Age  SibSp  Parch     Fare\n",
       "0            1         0       3    male  22.0      1      0   7.2500\n",
       "1            2         1       1  female  38.0      1      0  71.2833"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Describe function shows only integer data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>714.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.383838</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "      <td>32.204208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>257.353842</td>\n",
       "      <td>0.486592</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>14.526497</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "      <td>49.693429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>223.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>20.125000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.910400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       PassengerId    Survived      Pclass         Age       SibSp  \\\n",
       "count   891.000000  891.000000  891.000000  714.000000  891.000000   \n",
       "mean    446.000000    0.383838    2.308642   29.699118    0.523008   \n",
       "std     257.353842    0.486592    0.836071   14.526497    1.102743   \n",
       "min       1.000000    0.000000    1.000000    0.420000    0.000000   \n",
       "25%     223.500000    0.000000    2.000000   20.125000    0.000000   \n",
       "50%     446.000000    0.000000    3.000000   28.000000    0.000000   \n",
       "75%     668.500000    1.000000    3.000000   38.000000    1.000000   \n",
       "max     891.000000    1.000000    3.000000   80.000000    8.000000   \n",
       "\n",
       "            Parch        Fare  \n",
       "count  891.000000  891.000000  \n",
       "mean     0.381594   32.204208  \n",
       "std      0.806057   49.693429  \n",
       "min      0.000000    0.000000  \n",
       "25%      0.000000    7.910400  \n",
       "50%      0.000000   14.454200  \n",
       "75%      0.000000   31.000000  \n",
       "max      6.000000  512.329200  "
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7128"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.size#Total no. of  element in matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "891"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Pclass.count()#specific column non missing entry"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "714"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.count()#specific column non missing entry"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "891"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Pclass.size#specific column missing and non missing entry"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "891"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.size#specific column missing and non missing entr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891</td>\n",
       "      <td>714.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "      <td>891.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>male</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>577</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.383838</td>\n",
       "      <td>2.308642</td>\n",
       "      <td>NaN</td>\n",
       "      <td>29.699118</td>\n",
       "      <td>0.523008</td>\n",
       "      <td>0.381594</td>\n",
       "      <td>32.204208</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>257.353842</td>\n",
       "      <td>0.486592</td>\n",
       "      <td>0.836071</td>\n",
       "      <td>NaN</td>\n",
       "      <td>14.526497</td>\n",
       "      <td>1.102743</td>\n",
       "      <td>0.806057</td>\n",
       "      <td>49.693429</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.420000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>223.500000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>20.125000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>7.910400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>446.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>28.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>14.454200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>668.500000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>38.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>31.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>891.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>8.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>512.329200</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        PassengerId    Survived      Pclass   Sex         Age       SibSp  \\\n",
       "count    891.000000  891.000000  891.000000   891  714.000000  891.000000   \n",
       "unique          NaN         NaN         NaN     2         NaN         NaN   \n",
       "top             NaN         NaN         NaN  male         NaN         NaN   \n",
       "freq            NaN         NaN         NaN   577         NaN         NaN   \n",
       "mean     446.000000    0.383838    2.308642   NaN   29.699118    0.523008   \n",
       "std      257.353842    0.486592    0.836071   NaN   14.526497    1.102743   \n",
       "min        1.000000    0.000000    1.000000   NaN    0.420000    0.000000   \n",
       "25%      223.500000    0.000000    2.000000   NaN   20.125000    0.000000   \n",
       "50%      446.000000    0.000000    3.000000   NaN   28.000000    0.000000   \n",
       "75%      668.500000    1.000000    3.000000   NaN   38.000000    1.000000   \n",
       "max      891.000000    1.000000    3.000000   NaN   80.000000    8.000000   \n",
       "\n",
       "             Parch        Fare  \n",
       "count   891.000000  891.000000  \n",
       "unique         NaN         NaN  \n",
       "top            NaN         NaN  \n",
       "freq           NaN         NaN  \n",
       "mean      0.381594   32.204208  \n",
       "std       0.806057   49.693429  \n",
       "min       0.000000    0.000000  \n",
       "25%       0.000000    7.910400  \n",
       "50%       0.000000   14.454200  \n",
       "75%       0.000000   31.000000  \n",
       "max       6.000000  512.329200  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe(include=\"all\")#missing and non missing integer,string all type of data entry"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Fare</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass    Sex    Age  SibSp  Parch   Fare\n",
       "0          False     False   False  False  False  False  False  False\n",
       "1          False     False   False  False  False  False  False  False\n",
       "2          False     False   False  False  False  False  False  False\n",
       "3          False     False   False  False  False  False  False  False\n",
       "4          False     False   False  False  False  False  False  False\n",
       "..           ...       ...     ...    ...    ...    ...    ...    ...\n",
       "886        False     False   False  False  False  False  False  False\n",
       "887        False     False   False  False  False  False  False  False\n",
       "888        False     False   False  False   True  False  False  False\n",
       "889        False     False   False  False  False  False  False  False\n",
       "890        False     False   False  False  False  False  False  False\n",
       "\n",
       "[891 rows x 8 columns]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull()#missing and not missing entry False-non missing True-missing entry"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId    False\n",
       "Survived       False\n",
       "Pclass         False\n",
       "Sex            False\n",
       "Age             True\n",
       "SibSp          False\n",
       "Parch          False\n",
       "Fare           False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().any()#one way to list column which has missing value,True means missing value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().any().count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.isnull().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False    714\n",
       "True     177\n",
       "Name: Age, dtype: int64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.isnull().value_counts()#missing(True) and non missing(False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method IndexOpsMixin.value_counts of 0      False\n",
       "1      False\n",
       "2      False\n",
       "3      False\n",
       "4      False\n",
       "       ...  \n",
       "886    False\n",
       "887    False\n",
       "888     True\n",
       "889    False\n",
       "890    False\n",
       "Name: Age, Length: 891, dtype: bool>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.isnull().value_counts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dtype('float64')"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.dtype"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "PassengerId      int64\n",
       "Survived         int64\n",
       "Pclass           int64\n",
       "Sex             object\n",
       "Age            float64\n",
       "SibSp            int64\n",
       "Parch            int64\n",
       "Fare           float64\n",
       "dtype: object"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "177"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.isnull().value_counts()[True] #missing(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "714"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.isnull().value_counts()[False]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Replace missing value in each column and provide reason for chossing one function to replace missing value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21205.17"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "29.69911764705882"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#fillna <value for replacement> fillna so na means not a number\n",
    "#df.Age.mean()\n",
    "df.Age=df.Age.fillna(df.Age.mean())\n",
    "#another way is\n",
    "#df.Age.fillna(df.Age.mean(),inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#To verify replaced or not\n",
    "df.Age.isnull().any()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How to make a loop for data updating for replacing vlaue for 2,3 column at a time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "col = [\"Age\",\"Fare\"]\n",
    "for column in col:\n",
    "    if df[column].isnull().any():\n",
    "        df[column].fillna(df[column].mean(),inplace=True)\n",
    "    else:\n",
    "        pass\n",
    "#df.emarked.fillna(df.embarked.mode()[0], inplace=True)\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age.isnull().any()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How many male and female"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "male      577\n",
       "female    314\n",
       "Name: Sex, dtype: int64"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Sex.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Sex.value_counts().plot(kind=\"bar\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Embarked.value_counts().plot(kind=\"kde\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### save and export"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Sex.value_counts().plot(kind=\"bar\")\n",
    "plt.savefig(\"test.png\")\n",
    "plt.savefig(\"test1.jpg\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    549\n",
       "1    342\n",
       "Name: Survived, dtype: int64"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Survived.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Survived.value_counts().plot(kind=\"bar\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "module 'matplotlib.pyplot' has no attribute 'xtricks'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-23-c9244d943f86>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mSurvived\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvalue_counts\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mplot\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkind\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"bar\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mplt\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mxtricks\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"Not survived\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\"Survived\"\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m: module 'matplotlib.pyplot' has no attribute 'xtricks'"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.Survived.value_counts().plot(kind=\"bar\")\n",
    "plt.xtricks([\"Not survived\",\"Survived\"])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Total number of passengers of various age group(0-30, 31-60, &>60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(df.Age)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(df.Age, bins=30, rwidth=.9)#bins = To create more number of bucket to have mor graular level distribution \n",
    "plt.show()\n",
    "#bins = To create more number of bucket to have mor graular level distribution \n",
    "#rwidth=To control width of bars"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.hist(df.Age, bins=30, rwidth=.9,color=\"c\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       True\n",
       "1      False\n",
       "2       True\n",
       "3      False\n",
       "4      False\n",
       "       ...  \n",
       "886     True\n",
       "887     True\n",
       "888     True\n",
       "889     True\n",
       "890    False\n",
       "Name: Age, Length: 891, dtype: bool"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.Age<=30"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "586\n",
      "308\n",
      "22\n"
     ]
    }
   ],
   "source": [
    "age_grp1 = df.Age.where(df.Age<=30)\n",
    "age_grp2 = df.Age.where((df.Age>=30) & (df.Age<=60))\n",
    "age_grp3 = df.Age.where(df.Age>60)\n",
    "print(age_grp1.count())\n",
    "print(age_grp2.count())\n",
    "print(age_grp3.count())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Find out which age groip is survived"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>886</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>887</th>\n",
       "      <td>888.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>888</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>889</th>\n",
       "      <td>890.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>890</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0            NaN       NaN     NaN   \n",
       "1            2.0       1.0     1.0   \n",
       "2            3.0       1.0     3.0   \n",
       "3            4.0       1.0     1.0   \n",
       "4            NaN       NaN     NaN   \n",
       "..           ...       ...     ...   \n",
       "886          NaN       NaN     NaN   \n",
       "887        888.0       1.0     1.0   \n",
       "888          NaN       NaN     NaN   \n",
       "889        890.0       1.0     1.0   \n",
       "890          NaN       NaN     NaN   \n",
       "\n",
       "                                                  Name     Sex   Age  SibSp  \\\n",
       "0                                                  NaN     NaN   NaN    NaN   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0    1.0   \n",
       "2                               Heikkinen, Miss. Laina  female  26.0    0.0   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0    1.0   \n",
       "4                                                  NaN     NaN   NaN    NaN   \n",
       "..                                                 ...     ...   ...    ...   \n",
       "886                                                NaN     NaN   NaN    NaN   \n",
       "887                       Graham, Miss. Margaret Edith  female  19.0    0.0   \n",
       "888                                                NaN     NaN   NaN    NaN   \n",
       "889                              Behr, Mr. Karl Howell    male  26.0    0.0   \n",
       "890                                                NaN     NaN   NaN    NaN   \n",
       "\n",
       "     Parch            Ticket     Fare Cabin Embarked  \n",
       "0      NaN               NaN      NaN   NaN      NaN  \n",
       "1      0.0          PC 17599  71.2833   C85        C  \n",
       "2      0.0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0.0            113803  53.1000  C123        S  \n",
       "4      NaN               NaN      NaN   NaN      NaN  \n",
       "..     ...               ...      ...   ...      ...  \n",
       "886    NaN               NaN      NaN   NaN      NaN  \n",
       "887    0.0            112053  30.0000   B42        S  \n",
       "888    NaN               NaN      NaN   NaN      NaN  \n",
       "889    0.0            111369  30.0000  C148        C  \n",
       "890    NaN               NaN      NaN   NaN      NaN  \n",
       "\n",
       "[891 rows x 12 columns]"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.where(df.Survived == 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       NaN\n",
       "1      38.0\n",
       "2      26.0\n",
       "3      35.0\n",
       "4       NaN\n",
       "       ... \n",
       "886     NaN\n",
       "887    19.0\n",
       "888     NaN\n",
       "889    26.0\n",
       "890     NaN\n",
       "Name: Age, Length: 891, dtype: float64"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.where(df.Survived == 1).Age"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "342"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.where(df.Survived == 1).Age.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "df.where(df.Survived == 1).Age.plot(kind=\"hist\")\n",
    "plt.show()"
   ]
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
