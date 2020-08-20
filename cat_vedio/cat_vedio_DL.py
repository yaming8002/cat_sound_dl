# coding=utf-8
import os
import numpy as np
import tensorflow as tf	
import librosa
from keras.models import load_model
from pytube import YouTube
from pydub import AudioSegment
import sys

# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
class cat_vedio_DL():
	MFCC_NUM = 20
	SAMPLING_RATE=22050
	MFCC_MAX_LEN =512
	# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
	self_path = "/".join(os.path.abspath(__file__).split("\\")[:-1])
	model = load_model(self_path+'/model20200627_leakyRelu_1.h5')
	wave_path = ""

	def downMp4toW(self, link_id ="jSz2yWYbkdY" ):
		url = 'https://www.youtube.com/watch?v='+link_id
		#vedio_id = link_id
		yt = YouTube(url)
		down_video = yt.streams.first()
		print( "===============",self.self_path+"/wave" )
		down_video.download(self.self_path+"/wave",filename=link_id)


		mp4_version = AudioSegment.from_file(f"{self.self_path}/wave/{link_id}.mp4", "mp4",shell = False)
		self.wave_path = self.self_path+"/wave/"+ link_id+".wav"
		mp4_version.export(self.wave_path, format="wav")
		os.remove(self.self_path+"/wave/"+link_id+".mp4")


	def wav2mfcc(self,wave, max_len=512):
		wave_mean = abs(np.mean(wave))
		if wave_mean != 0:
			wave = wave / wave_mean
		mfcc = librosa.feature.mfcc(wave, n_mfcc=self.MFCC_NUM, sr=self.SAMPLING_RATE)

		if (max_len > mfcc.shape[1]):
			pad_width = max_len - mfcc.shape[1]
			mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')

		else:
			mfcc = mfcc[:, :max_len]
		
		return mfcc



	def create_test_data(self,path="F:/catsound/excmple", extension = "wav"):

		mfcc_list = []
		audio, sr = librosa.load(path, mono=True, sr=None)
		buffer = 2 * sr
		samples_total = len(audio)
		samples_wrote = 0
		counter = 1
		while samples_wrote < samples_total:
			if buffer > (samples_total - samples_wrote):
				buffer = samples_total - samples_wrote
			block = audio[samples_wrote : (samples_wrote + buffer)]
			mfcc = self.wav2mfcc(block,self.MFCC_MAX_LEN)
			
			mfcc_list.append(mfcc)
			counter += 1
			samples_wrote += buffer
		mfcc_list = np.array(mfcc_list)
		mfcc_list = mfcc_list.reshape(mfcc_list.shape[0], self.MFCC_NUM, self.MFCC_MAX_LEN, 1)
		os.remove(path)
		return mfcc_list


	def test_ans_show_dict(self, extension = "wav" ):
		list_sigle =['none', 'purring', 'cat_talk_cats', 'cat_call_persion', 'caveat']
		if len(self.wave_path) == 0:
			print("we don't finded file")
		else:
			test_one_list = self.create_test_data(self.wave_path)
			Y_testnas = self.model.predict(test_one_list)

			Y_testnas = Y_testnas[~np.all(Y_testnas < 0.1, axis=1)]
			Y_testnas = np.around(Y_testnas, decimals=2) 

			ans = list()
			for two_second in Y_testnas:
				dic = {}
				for i in range(len(list_sigle)):
					dic[list_sigle[i]] = two_second[i]
				ans.append(dic)
			for x in ans:
				print( x )
		return ans

	def test_ans_show_tostr(self, extension = "wav" ):
		if len(self.wave_path) == 0:
			print("we don't finded file")
		else:
			test_one_list = self.create_test_data(self.wave_path)
			Y_testnas = self.model.predict(test_one_list)

			Y_testnas = Y_testnas[~np.all(Y_testnas < 0.1, axis=1)]
			Y_testnas = np.around(Y_testnas, decimals=2) 

			ans = ""
			for i in range(len(Y_testnas)) :
				ans += ",".join([f'{format(x,"0.3f")}' for x in Y_testnas[i] ])
				if i +1 <  len(Y_testnas):
					ans +="__"
		return ans

if __name__ == '__main__':
	# test_path = "/content/drive/My Drive/test_sound/"
	# model =input("請輸入model路徑")
	#test_path =input("請輸入wav路徑")
	test_path=sys.argv

	#print(test_path )
	a = cat_vedio_DL()
	a.downMp4toW( "jSz2yWYbkdY")
	#a.test_ans_show( test_path , a.model)
	a.test_ans_show_tostr( test_path)
	
	
	
	
	
	
	
	