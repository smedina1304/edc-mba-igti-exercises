resource "aws_s3_bucket_object" "job_spark" {
  bucket = aws_s3_bucket.dl.id
  key    = "sources/scripts-glue/mod01-desaf-item2-aws-glue-job_spark.py"
  acl    = "private"
  source = "../sources/mod01-desaf-item2-aws-glue-job_spark.py"
  etag   = filemd5("../sources/mod01-desaf-item2-aws-glue-job_spark.py")
}