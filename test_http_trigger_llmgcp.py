#write unit tests for the function

import json
import unittest
from unittest.mock import patch
from function_app import http_trigger_llmgcp
import azure.functions as func
import logging
import google.generativeai as palm


class TestFunctionApp(unittest.TestCase):
    
        def test_http_trigger_llmgcp(self):
            # Create a mock HTTP request object
            req = unittest.mock.Mock()
            req.params = {
                "question": "What is the meaning of life?"
            }
    
            # Call the function
            response = http_trigger_llmgcp(req)
    
            # Check if the response is not None
            self.assertIsNone(response)
    
            # Check the response
            #self.assertEqual(response.status_code, 200)
            self.assertEqual(response.mimetype, "application/json")
    
            # Check the response body
            response_body = json.loads(response.get_body())
            self.assertIn("result", response_body)
            self.assertIsInstance(response_body["result"], str)
            self.assertTrue(len(response_body["result"]) > 0)
            


