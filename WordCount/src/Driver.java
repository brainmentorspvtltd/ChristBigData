import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class Driver extends Configured implements Tool {

	@Override
	public int run(String[] args) throws Exception {
		
		JobConf jc = new JobConf(Driver.class);
		FileInputFormat.setInputPaths(jc, new Path(args[0]));
		FileOutputFormat.setOutputPath(jc, new Path(args[1]));
		jc.setMapperClass(MapperCode.class);
		jc.setReducerClass(ReducerCode.class);
		jc.setMapOutputKeyClass(Text.class);
		jc.setMapOutputValueClass(IntWritable.class);
		jc.setOutputKeyClass(Text.class);
		jc.setOutputValueClass(IntWritable.class);
		JobClient.runJob(jc);
		
		return 0;
	}
	
	public static void main(String[] args) throws Exception {
		int exitCode = ToolRunner.run(new Driver(), args);
		System.out.println(exitCode);
	}


}
