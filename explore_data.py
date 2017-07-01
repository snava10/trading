from data import *


if __name__ == "__main__":
	df, stats_df = create_training_set("data/fb.csv")
	'''
	for i in range(len(df.columns)-1):
		for j in range(i+1,len(df.columns)-1):
			x = df.columns[i]
			y = df.columns[j]
			plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
			plot_logistic_regression_data(df, xcol=x, ycol=y, feature="Label", plotModel=plotModel)
	#print(df.head(5))

	#print(stats_df.head(30))
	jdf = pd.concat([df, stats_df], axis=1, join='inner')
	print(jdf.columns)
	x ="Adj Close"
	y = "Low10"
	plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
	plot_logistic_regression_data(jdf, xcol=x, ycol=y, feature="Label", plotModel=plotModel)
	
	x ="High10"
	y = "Low10"
	plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
	plot_logistic_regression_data(jdf, xcol=x, ycol=y, feature="Label", plotModel=plotModel)

	x = "Low"
	y = "Adj_Close_Mean10"
	plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
	plot_logistic_regression_data(jdf, xcol=x, ycol=y, feature="Label", plotModel=plotModel)
	

	x = "Low"
	y = "Adj_Close_Std10"
	plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
	plot_logistic_regression_data(jdf, xcol=x, ycol=y, feature="Label", plotModel=plotModel)


	x ="Adj_Close_Mean10"
	y = "Adj_Close_Std10"
	plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
	plot_logistic_regression_data(jdf, xcol=x, ycol=y, feature="Label", plotModel=plotModel)
	
	x ="High"
	y = "Low"
	plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
	plot_logistic_regression_data(jdf, xcol=x, ycol=y, feature="Label", plotModel=plotModel)
	'''
	plot_data(df,col="Adj Close")
	jdf = pd.concat([df, stats_df], axis=1, join='inner')
	x ="Adj Close"
	y = "Adj_Close_Mean10"
	plotModel = PlotModel(title="Log Reg", xlabel=x, ylabel=y)
	plot_ternary_log_reg_data(jdf, xcol=x, ycol=y, feature="Label5", plotModel=plotModel)

#	print(df["Label5"].head(10))
	
