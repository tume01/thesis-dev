# -*- coding: utf-8 -*-

import sys,getopt,got,datetime,codecs

def main(argv):

	keywords = [#"democracia", 
				#"corrupcion", 
				#"sobornos politica", 
				#"plan de gobierno",
				#"sistema erectoral",
				#"onpe",
				#"propuesta salud",
				#"propuesta delincuencia",
				#"hugo chavez",
				#"nicolas maduro",
				#"delincuencia",
				#"politica ambiental",
				#"politica",
				#"politica economica",
				#"acuerdos entre paises",
				#"politica monetaria",
				#"dictadura",
				#"congreso politico",
				#"oficialismo",
				#"nacionalismo",
				#"comunismo",
				"conflictos sociales",
				"partido social"
				]

	for i in range(len(keywords)):
		tweetCriteria = got.manager.TweetCriteria()
		
		tweetCriteria.querySearch = keywords[i]

		outputFile = codecs.open("output_got" + keywords[i] + ".out", "w+", "utf-8")

		def receiveBuffer(tweets):
			for t in tweets:
				outputFile.write(('%s\n' % (t.text)))
			outputFile.flush();
			#print 'More %d saved on file...\n' % len(tweets)

		got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

		outputFile.close()
		print 'Done. Output file generated for' + keywords[i]


if __name__ == '__main__':
	main(sys.argv[1:])