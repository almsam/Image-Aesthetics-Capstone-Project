## Sunday (06/10/2024)

### Current Tasks

* #150: fix eda - the experiment had a bug, the fix was as follows

```diff
-    df['BestColorMatch'] = df['SelectedImageId'].isin(comparison_df['bestColor']).astype(int); df['BestContrastMatch'] = df['SelectedImageId'].isin(comparison_df['bestContrast']).astype(int)
-    df['BestShapeMatch'] = df['SelectedImageId'].isin(comparison_df['bestShape']).astype(int); df['BestOverallMatch'] = df['SelectedImageId'].isin(comparison_df['Bestoverall']).astype(int)
+    df['BestColorMatch'] = (df['SelectedImageId'] == (comparison_df['bestColor'])).astype(int); df['BestContrastMatch'] = (df['SelectedImageId'] == (comparison_df['bestContrast'])).astype(int)
+    df['BestShapeMatch'] = (df['SelectedImageId'] == (comparison_df['bestShape'])).astype(int); df['BestOverallMatch'] = (df['SelectedImageId'] == (comparison_df['Bestoverall'])).astype(int)
```


* #164: new images from PDF - Imported the VAST images from VAST PDF
* #165: retsurcture - file repo needed cleanup after CIFAR went away
* #149: image quality - implement VAST images

### Progress Update (Sunday 18/1/2025)

<table>
    <tr>
        <td><strong>TASK/ISSUE #</strong>
        </td>
        <td><strong>STATUS</strong>
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task 1
        </td>
        <!-- Status -->
        <td>Complete
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task 2
        </td>
        <!-- Status -->
        <td>Complete
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task 3
        </td>
        <!-- Status -->
        <td>Complete
        </td>
    </tr>
    <tr>
        <!-- Task/Issue # -->
        <td>Task 4
        </td>
        <!-- Status -->
        <td>In Progress
        </td>

I did 3 tasks with the inent of migratimng from CIFAR 10 dataset to the VAST image set - I am satisfied with progress thusfar & looking fwd to see how the ML portion will go

Team plays nice still - only improovement would be a replacement after Zoe dropping out. But player 5 or not we should smoothly sail to the end of the term

### Goals For Next Iteration

3 issues:

* #149: image quality - Implement the VAST image set to increase image quality
* #168: make ML model adopt VAST - Cascade above change into the ML model
* #169: pixelate images for CNN - VAST needs to be stepped down for the CNN
