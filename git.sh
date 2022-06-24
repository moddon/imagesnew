#!/bin/bash
git config http.sslCAInfo
git -c credential.helper= ls-remote origin
git add *
git commit -m "Adding Encodings From TC"
git push