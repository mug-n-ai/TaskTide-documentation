# TaskTide

<img src="contents/tasktide.png" alt="icon" width="300" height="300">

![Version](https://img.shields.io/badge/version-1.2.9-blue)
[![Collect Actions on Issue Events](https://github.com/LorenzoMugnai/journal/actions/workflows/collect_actions.yml/badge.svg)](https://github.com/LorenzoMugnai/journal/actions/workflows/collect_actions.yml)
[![Sync checked Actions](https://github.com/LorenzoMugnai/MyTaskTide/actions/workflows/sync_checked_actions.yml/badge.svg)](https://github.com/LorenzoMugnai/MyTaskTide/actions/workflows/sync_checked_actions.yml)
[![Sync Assigned Issues from Other Repositories](https://github.com/LorenzoMugnai/journal/actions/workflows/sync_issues.yml/badge.svg)](https://github.com/LorenzoMugnai/journal/actions/workflows/sync_issues.yml)
[![Update Changelog](https://github.com/LorenzoMugnai/MyTaskTide/actions/workflows/changelog.yml/badge.svg)](https://github.com/LorenzoMugnai/MyTaskTide/actions/workflows/changelog.yml)
[![Collect Events from Issues](https://github.com/LorenzoMugnai/MyTaskTide/actions/workflows/events_collector.yml/badge.svg)](https://github.com/LorenzoMugnai/MyTaskTide/actions/workflows/events_collector.yml)
<p align="left"> 
    <span style="margin-right: 8px;">Empowered by</span>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Logo" height="20"> 
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Logo" height="20">
    <img src="https://img.shields.io/badge/Google%20Calendar-EAA42B?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Google Calendar Logo" height="20"> 
</p>

## Introduction

The TaskTide repository is designed as a versatile **journal manager** that facilitates the organization and management of various tasks and notes **within GitHub** by leveraging GitHub's projects. Utilizing GitHub's robust issue tracking and project management features, TaskTide allows users to systematically document their progress, manage actionable items, and collaborate effectively across different projects.

TaskTide can be utilized by anyone looking to track and manage diverse projects. TastTide automatically 

- sync assigned issues from other Git repositories, 
- track actions and to-dos, collecting them in a single location 
- Change logs and updates automatically generated and updated in the repository every day
- synchronize events with Google Calendar. 

Additional useful features will be added in future updates.

To tailor the experience, users simply need to create their own project within GitHub, adapting the issue visualization to suit their specific needs and objectives. An example is provided [here](https://github.com/users/mug-n-ai/projects/1/views/1).

TaskTide empowers individuals and teams alike to maintain organized, efficient workflows.

TaskTide is a system based on GitHub Actions and automated through a combination of GitHub workflows and Python scripts


**Table of Contents**

- [TaskTide](#tasktide)
  - [Introduction](#introduction)
  - [Managing Issues with Projects (and Projects with Issues)](#managing-issues-with-projects-and-projects-with-issues)
  - [How to set up your TaskTide](#how-to-set-up-your-tasktide)
    - [Configuration File: settings.yml](#configuration-file-settingsyml)
    - [Set Up Your Repository](#set-up-your-repository)
  - [Supported Functionalities](#supported-functionalities)
    - [All your assigned Issues in one place](#all-your-assigned-issues-in-one-place)
      - [How It Works](#how-it-works)
      - [How to Set Up](#how-to-set-up)
    - [Easy fast access to your open Actions](#easy-fast-access-to-your-open-actions)
      - [How It Works](#how-it-works-1)
      - [How to Set Up](#how-to-set-up-1)
  - [Automated Changelog Generation](#automated-changelog-generation)
    - [How It Works](#how-it-works-2)
    - [How to Set Up](#how-to-set-up-2)
    - [Integration with Google Calendar](#integration-with-google-calendar)
      - [How It Works](#how-it-works-3)
      - [How to Set Up](#how-to-set-up-3)
  - [Contributing](#contributing)


> [!IMPORTANT]
> TaskTide is available only for GitHub Supporters. Find more information about [GitHub Sponsors](https://docs.github.com/en/sponsors).
> To use TaskTide, please consider supporting the project by [becoming a GitHub Sponsor](https://github.com/sponsors/LorenzoMugnai)

## Managing Issues with Projects (and Projects with Issues)

To visualize and manage your issues effectively, it's recommended to create a project within GitHub. This project can be personal and is not restricted by the repository's functions. It serves as a workspace where you can categorize, prioritize, and track progress on your research tasks and notes.

Utilizing GitHub Projects helps to provide a clear overview of the issues in your journal, facilitating better organization and task management. In fact, GitHub projects support different views of the issues simultaneously with options ranging from boards, to timelines, to tables.  

## How to set up your TaskTide

To use TaksTide, just clone this repository in a private one and start a GitHub project there.You can use the TaskTide example project as a starting point for that. Then, start populating your project with issues and... that's all! Have fun surfing on the waves of tasks.  

### Configuration File: settings.yml

TaskTide uses a configuration file named settings.yml located in the root of the repository. This file is essential for setting specific parameters that are used throughout the repository's workflows. Unlike other configuration approaches that rely on GitHub secrets, settings.yml provides an easier and more transparent way to manage certain static configuration values.

An example `settings.yml` file:

```yaml
ACTION_ISSUE_NUMBER: 1
CHANGELOG_ISSUE_NUMBER: 2
USER_NAME: TaskTide
SOURCE_REPOS: owner/repo1,owner/repo2
```

- ACTION_ISSUE_NUMBER: Specifies the issue number where action items will be collected.
- CHANGELOG_ISSUE_NUMBER: Specifies the issue number where changelog updates will be posted.
- USER_NAME: The username of the user whose assigned issues you want to collect.
- SOURCE_REPOS: A comma-separated list of repositories from which you want to collect assigned issues. The format should be `owner/repo1,owner/repo2,...`. For example, `octocat/hello-world,octocat/cool-project`.

### Set Up Your Repository

1. **Create a Private Repository**  
   - Go to GitHub and create a new private repository.  
   - Add a README file.

2. **Clone the Repository**  
   - Clone your newly created repository to your local machine.

3. **Download TaskTide**  
   - Download the content from the TaskTide main branch or one of the releases.

4. **Copy TaskTide Files**  
   - Copy the contents of TaskTide to your private repository and commit the changes.

5. **Create a GitHub Project**  
   - Create a new project within your private repository or connect it later.

6. **Configure the Settings**
    - Update the `settings.yml` file with your desired settings.
    - Add the number of the issues that will be used for collecting actions and changelog updates.
    - Specify the username of the user whose assigned issues you want to collect.
    - Define the source repositories from which you want to collect assigned issues.
  
7. **Add Secrets**
    - Add the necessary secrets to your repository settings. These secrets are used to authenticate the GitHub API and Google Calendar API.

Your repository is now set up to host your TaskTide project!

For detailed steps, refer to the [complete documentation](https://mug-n-ai.github.io/TaskTide-documentation/getting_started.html#getting-started).


## Supported Functionalities

### All your assigned Issues in one place

This repository includes a script designed to synchronize assigned issues across multiple source repositories into a designated target repository.

#### How It Works

- **Fetching Assigned Issues**: The script retrieves all issues assigned to the user from specified source repositories and checks if the user is the assignee.

- **Unique Identification**: Each action item is identified using a unique identifier formatted as `repoName-#issueNumber`, ensuring distinction even with identical issue numbers.

- **Updating or Creating Issues**: For each assigned issue found, the script checks for equivalent issues in the target repository. It updates titles if necessary or creates new issues with references to the original issues.

- **Scheduled Synchronization**: The functionality is integrated into a GitHub Actions workflow, allowing it to run on a schedule (e.g., every Sunday at midnight UTC) or be manually triggered. This ensures the target repository remains updated with new assigned issues from the source repositories.

This mechanism streamlines task management across multiple projects, enhancing organization and visibility of actionable items.

> [!NOTE] 
> Once issues are copied into this project, they must be manually added to different sections of the board.

> [!WARNING] 
> The issues are copied, not synced. If an issue is deleted from the source repository, it will not be deleted from this repository.

> [!WARNING] 
> The Synchronization is by default run every Sunday at midnight UTC. If you want to change this, you can do it in the `.github/workflows/sync_issues.yml` file.


#### How to Set Up

To make the TaskTide repository work, you need to add the following secrets to your repository:

- **`PAT_TOKEN`**: A personal access token allowing the script to access the GitHub API. Create a new token following the instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with access to:
  - `repo`
  - `workflow`
  - `project`

Additionally, make sure to configure the `settings.yml` file with:

- **`USER_NAME`**: The username of the user whose assigned issues you want to collect.
- **`SOURCE_REPOS`**: A comma-separated list of repositories from which you want to collect assigned issues. The format should be `owner/repo1,owner/repo2,...`. For example, `octocat/hello-world,octocat/cool-project`.


### Easy fast access to your open Actions

This repository includes a script designed to automatically collect actionable items marked with the keyword `[action]` from issues and comments across the repository.

#### How It Works

- **Fetching Issues**: The script retrieves all open issues from the specified repository using the GitHub API, checking each issue to gather actionable items.

- **Extracting Actionable Items**: Action items are identified by searching for lines containing the keyword `[action]`, excluding completed items (marked with `[x]`).

- **Synchronising Checked Actions**: The script also synchronises updates. If an action is marked as completed ([x]) in the action issue, the corresponding item in the original issue or comment is updated to reflect this change.

- **Linking to Original Comments**: Each action item includes a clickable link directing users to the specific comment within the original issue, providing context.

- **Updating the Action Issue**: Collected action items are formatted as checkable items in Markdown. The designated action issue is updated with the current list, ensuring completed actions are removed.

- **Event-Driven Synchronization**: Integrated into a GitHub Actions workflow, this functionality triggers on issue creation or edits, and comment creation or edits. When triggered by a comment, it processes only that specific comment. It can also be executed manually or scheduled weekly for comprehensive updates.

This mechanism streamlines task tracking and enhances organization of actionable items across the project.

> [!NOTE]
> Action items are collected and displayed in a central issue for easy access and management. However, completing the task in the collecting issue will not propagate to the original location. Actions needs to be completed in the source issue, and then they will disappear from the collecting thread.  

> [!WARNING] 
> The Synchronization is not real-time. The action running time is average 1 minute, so it can take up to 1 minute to see the changes in the collecting issue.


#### How to Set Up

To enable the action collector, add the following secrets to your repository:

- **`PAT_TOKEN`**: Create a personal access token following the instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with access to:
  - `repo`
  - `workflow`
  - `project`

Additionally, make sure to configure the `settings.yml` file with:

- **`ACTION_ISSUE_NUMBER`**: - **`ACTION_ISSUE_NUMBER`**: The issue number where action items will be collected.

## Automated Changelog Generation

This repository includes a script designed to automatically generate and maintain a changelog based on the assigned issues and comments within the repository.

### How It Works

- **Tracking Changes**: Each change, whether it’s the creation of an issue or updates to comments, is tracked by date. Changes are organized by month and day, providing a clear timeline of activities.

- **Merging Changelog Entries**: The script merges new changelog entries with existing ones, preventing duplication and ensuring that updates are incorporated without losing any historical data.

- **Scheduled Updates**: The functionality is integrated into a GitHub Actions workflow, allowing it to run daily at midnight UTC or be manually triggered. This ensures that the changelog is consistently updated with the latest changes.

This system streamlines the documentation of project progress, enhancing visibility and organization of ongoing work.

> [!WARNING]  
> The changelog generation process is not real-time. Changes may take up to a day to be reflected in the changelog, depending on the scheduled execution.

### How to Set Up

To enable the changelog generation system, you need to add the following secrets to your repository:

- **`PAT_TOKEN`**: A personal access token that grants the script access to the GitHub API. Create a new token following the instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with access to:
  - `repo`
  - `workflow`
  - `project`

Additionally, ensure that you configure the `settings.yml` file with:

- **`CHANGELOG_ISSUE_NUMBER`**: The issue number where the changelog will be maintained.
- **`ACTION_ISSUE_NUMBER`**: The issue number where action items will be collected.

> [!NOTE]
> We need to set the `ACTION_ISSUE_NUMBER` because we don't want to include the action items in the changelog. The changelog is supposed to be a summary of the changes, not a list of tasks to do.

### Integration with Google Calendar

This repository includes a script designed to extract events specified with the keyword `[time]` from issues and comments across the repository and create corresponding events in Google Calendar.

#### How It Works

- **Fetching Issues**: The script retrieves all open issues from the specified repository using the GitHub API, processing each issue to look for events.

- **Extracting Events**: Event are identified by searching for lines containing the keyword `[time]` followed by a date, time, and timezone. Each matched item generates a unique event in Google Calendar.

  - **Date Format**: The date should be in the format `dd/mm/yyyy` (e.g., `15/10/2024` for 15th October 2024).
  - **Time Format**: The time should be in the format `HH:MM` using a 24-hour clock (e.g., `14:30` for 2:30 PM).
  - **Timezone**: The timezone should be specified using a valid identifier (e.g., `Europe/London`). If no timezone is provided, `Europe/London` is used as the default.
  - **Duration**: The event must include a duration in minutes, hours or days (e.g. `duration: 15 m` for 15 minutes).
  - **Reminder**: The event can include a reminder in minutes(e.g. `reminder: 15` for 15 minutes before the event).
  - **Example**: `[time]-15/10/2024 14:30 Europe/London`

- **Linking to Original Comments**: Each event is associated with a clickable link directing users to the specific comment within the original issue, providing context.

- **Creating or Updating Calendar Events**: For each extracted event, the script checks if an event with the same date and time already exists in Google Calendar. If it does, the event is updated with any new details. If not, a new event is created.

- **Triggering the Functionality**: Integrated into a GitHub Actions workflow, this functionality triggers on issue creation, edits, and comment creation or edits. It can also be manually triggered or scheduled to run weekly. When triggered by an issue or comment event, it processes only that specific issue or comment, allowing for quick updates.

This mechanism ensures that events are consistently tracked and organized in your calendar, reducing the likelihood of missing important dates.

> [!NOTE]
> Each occurrence of the `[time]` keyword within an issue or comment will generate a separate event in Google Calendar, preventing duplicates for the same date and time if the same comment is updated.

> [!WARNING]
> The events are created based on the issues at the time of the event trigger; changes made to the original issues after the event creation will not be reflected in Google Calendar until the next trigger occurs.

#### How to Set Up

To enable the `events_collector`, you need to configure the following secrets in your repository:

- **`PAT_TOKEN`**: A personal access token allowing the script to access the GitHub API. Create a new token following the instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) with access to:
  - `repo`
  - `workflow`
  - `project`

- **`GOOGLE_TOKEN`**: This contains the OAuth 2.0 token in JSON format required for the Google Calendar API. Ensure that you have the appropriate permissions to access and modify your Google Calendar. Follow the instructions in this guide to create and download the credentials and generate the `token.json` file: :ref:`generate_credentials`.

  In summary, the process involves:
  
  1. Setting up a new project on Google Cloud Platform,
  2. Enabling the Google Calendar API,
  3. Configuring the OAuth consent screen,
  4. Creating OAuth 2.0 credentials and downloading the `credentials.json` file,
  5. Running the `scripts/update_credentials.py` script to generate the `token.json` file,
  6. Copying the content of `token.json` and storing it as the value for the `GOOGLE_TOKEN` secret in your GitHub repository settings.

  For detailed, step-by-step instructions, refer to TaskTide's documentation on generating Google Calendar credentials.

## Contributing

TaskTide is supposed to be a community project. Please support the development and maintenance. You can contribute with the Fork and Pull method: fork this repository and create a pull request for your updated. Or open an issue or check our public development project and pick a task that you think you can help with. We are happy to have you all on board! 
