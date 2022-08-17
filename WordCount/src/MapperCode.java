import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Reporter;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Mapper;

public class MapperCode extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable>{
	IntWritable one = new IntWritable(1);
	Text word = new Text();
	@Override
	public void map(LongWritable key, Text value, OutputCollector<Text, IntWritable> output, Reporter rep)
			throws IOException {
		String line = value.toString().toLowerCase(); // type casting to String from Text Type
		StringTokenizer tokenizer = new StringTokenizer(line);
		while(tokenizer.hasMoreElements()) {
			word.set(tokenizer.nextToken());
			output.collect(word, one);
		}
	}
	
}





