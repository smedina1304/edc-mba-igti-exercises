/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.pinot.integration.tests;

import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;


/**
 * Hybrid cluster integration test that uses one of the DateTimeFieldSpec as primary time column
 */
public class DateTimeFieldSpecHybridClusterIntegrationTest extends HybridClusterIntegrationTest {
  private static final String SCHEMA_WITH_DATETIME_FIELDSPEC_NAME = "On_Time_On_Time_Performance_2014_100k_subset_nonulls_datetimefieldspecs.schema";

  protected String getSchemaFileName() {
    return SCHEMA_WITH_DATETIME_FIELDSPEC_NAME;
  }

  @BeforeClass
  public void setUp()
      throws Exception {
    super.setUp();
  }


  @AfterClass
  public void tearDown()
      throws Exception {
    super.tearDown();
  }
}
