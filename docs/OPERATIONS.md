# GitHub operation directory

Snapshot 2026-11-15. 1281 published REST operations, 32 GraphQL queries and 285 mutations.

The directory includes deprecated and retired operations. Availability and permissions vary by host, plan, credential and rollout. Retired entries are blocked by the executor.

Use python3 scripts/operations.py search TERM and describe OPERATION for current bundled parameters. For GraphQL add --graphql, then inspect argument types with the type command.

## REST actions

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [actions/get-actions-cache-retention-limit-for-enterprise](https://docs.github.com/rest/actions/cache#get-github-actions-cache-retention-limit-for-an-enterprise) | GET | /enterprises/{enterprise}/actions/cache/retention-limit | indexed |
| [actions/set-actions-cache-retention-limit-for-enterprise](https://docs.github.com/rest/actions/cache#set-github-actions-cache-retention-limit-for-an-enterprise) | PUT | /enterprises/{enterprise}/actions/cache/retention-limit | indexed |
| [actions/get-actions-cache-storage-limit-for-enterprise](https://docs.github.com/rest/actions/cache#get-github-actions-cache-storage-limit-for-an-enterprise) | GET | /enterprises/{enterprise}/actions/cache/storage-limit | indexed |
| [actions/set-actions-cache-storage-limit-for-enterprise](https://docs.github.com/rest/actions/cache#set-github-actions-cache-storage-limit-for-an-enterprise) | PUT | /enterprises/{enterprise}/actions/cache/storage-limit | indexed |
| [actions/get-actions-cache-retention-limit-for-organization](https://docs.github.com/rest/actions/cache#get-github-actions-cache-retention-limit-for-an-organization) | GET | /organizations/{org}/actions/cache/retention-limit | indexed |
| [actions/set-actions-cache-retention-limit-for-organization](https://docs.github.com/rest/actions/cache#set-github-actions-cache-retention-limit-for-an-organization) | PUT | /organizations/{org}/actions/cache/retention-limit | indexed |
| [actions/get-actions-cache-storage-limit-for-organization](https://docs.github.com/rest/actions/cache#get-github-actions-cache-storage-limit-for-an-organization) | GET | /organizations/{org}/actions/cache/storage-limit | indexed |
| [actions/set-actions-cache-storage-limit-for-organization](https://docs.github.com/rest/actions/cache#set-github-actions-cache-storage-limit-for-an-organization) | PUT | /organizations/{org}/actions/cache/storage-limit | indexed |
| [actions/get-actions-cache-usage-for-org](https://docs.github.com/rest/actions/cache#get-github-actions-cache-usage-for-an-organization) | GET | /orgs/{org}/actions/cache/usage | indexed |
| [actions/get-actions-cache-usage-by-repo-for-org](https://docs.github.com/rest/actions/cache#list-repositories-with-github-actions-cache-usage-for-an-organization) | GET | /orgs/{org}/actions/cache/usage-by-repository | indexed |
| [actions/list-hosted-runners-for-org](https://docs.github.com/rest/actions/hosted-runners#list-github-hosted-runners-for-an-organization) | GET | /orgs/{org}/actions/hosted-runners | indexed |
| [actions/create-hosted-runner-for-org](https://docs.github.com/rest/actions/hosted-runners#create-a-github-hosted-runner-for-an-organization) | POST | /orgs/{org}/actions/hosted-runners | indexed |
| [actions/list-custom-images-for-org](https://docs.github.com/rest/actions/hosted-runners#list-custom-images-for-an-organization) | GET | /orgs/{org}/actions/hosted-runners/images/custom | indexed |
| [actions/get-custom-image-for-org](https://docs.github.com/rest/actions/hosted-runners#get-a-custom-image-definition-for-github-actions-hosted-runners) | GET | /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id} | indexed |
| [actions/delete-custom-image-from-org](https://docs.github.com/rest/actions/hosted-runners#delete-a-custom-image-from-the-organization) | DELETE | /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id} | indexed |
| [actions/list-custom-image-versions-for-org](https://docs.github.com/rest/actions/hosted-runners#list-image-versions-of-a-custom-image-for-an-organization) | GET | /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions | indexed |
| [actions/get-custom-image-version-for-org](https://docs.github.com/rest/actions/hosted-runners#get-an-image-version-of-a-custom-image-for-github-actions-hosted-runners) | GET | /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version} | indexed |
| [actions/delete-custom-image-version-from-org](https://docs.github.com/rest/actions/hosted-runners#delete-an-image-version-of-custom-image-from-the-organization) | DELETE | /orgs/{org}/actions/hosted-runners/images/custom/{image_definition_id}/versions/{version} | indexed |
| [actions/get-hosted-runners-github-owned-images-for-org](https://docs.github.com/rest/actions/hosted-runners#get-github-owned-images-for-github-hosted-runners-in-an-organization) | GET | /orgs/{org}/actions/hosted-runners/images/github-owned | indexed |
| [actions/get-hosted-runners-partner-images-for-org](https://docs.github.com/rest/actions/hosted-runners#get-partner-images-for-github-hosted-runners-in-an-organization) | GET | /orgs/{org}/actions/hosted-runners/images/partner | indexed |
| [actions/get-hosted-runners-limits-for-org](https://docs.github.com/rest/actions/hosted-runners#get-limits-on-github-hosted-runners-for-an-organization) | GET | /orgs/{org}/actions/hosted-runners/limits | indexed |
| [actions/get-hosted-runners-machine-specs-for-org](https://docs.github.com/rest/actions/hosted-runners#get-github-hosted-runners-machine-specs-for-an-organization) | GET | /orgs/{org}/actions/hosted-runners/machine-sizes | indexed |
| [actions/get-hosted-runners-platforms-for-org](https://docs.github.com/rest/actions/hosted-runners#get-platforms-for-github-hosted-runners-in-an-organization) | GET | /orgs/{org}/actions/hosted-runners/platforms | indexed |
| [actions/get-hosted-runner-for-org](https://docs.github.com/rest/actions/hosted-runners#get-a-github-hosted-runner-for-an-organization) | GET | /orgs/{org}/actions/hosted-runners/{hosted_runner_id} | indexed |
| [actions/update-hosted-runner-for-org](https://docs.github.com/rest/actions/hosted-runners#update-a-github-hosted-runner-for-an-organization) | PATCH | /orgs/{org}/actions/hosted-runners/{hosted_runner_id} | indexed |
| [actions/delete-hosted-runner-for-org](https://docs.github.com/rest/actions/hosted-runners#delete-a-github-hosted-runner-for-an-organization) | DELETE | /orgs/{org}/actions/hosted-runners/{hosted_runner_id} | indexed |
| [actions/get-github-actions-permissions-organization](https://docs.github.com/rest/actions/permissions#get-github-actions-permissions-for-an-organization) | GET | /orgs/{org}/actions/permissions | indexed |
| [actions/set-github-actions-permissions-organization](https://docs.github.com/rest/actions/permissions#set-github-actions-permissions-for-an-organization) | PUT | /orgs/{org}/actions/permissions | indexed |
| [actions/get-artifact-and-log-retention-settings-organization](https://docs.github.com/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization) | GET | /orgs/{org}/actions/permissions/artifact-and-log-retention | indexed |
| [actions/set-artifact-and-log-retention-settings-organization](https://docs.github.com/rest/actions/permissions#set-artifact-and-log-retention-settings-for-an-organization) | PUT | /orgs/{org}/actions/permissions/artifact-and-log-retention | indexed |
| [actions/get-fork-pr-contributor-approval-permissions-organization](https://docs.github.com/rest/actions/permissions#get-fork-pr-contributor-approval-permissions-for-an-organization) | GET | /orgs/{org}/actions/permissions/fork-pr-contributor-approval | indexed |
| [actions/set-fork-pr-contributor-approval-permissions-organization](https://docs.github.com/rest/actions/permissions#set-fork-pr-contributor-approval-permissions-for-an-organization) | PUT | /orgs/{org}/actions/permissions/fork-pr-contributor-approval | indexed |
| [actions/get-private-repo-fork-pr-workflows-settings-organization](https://docs.github.com/rest/actions/permissions#get-private-repo-fork-pr-workflow-settings-for-an-organization) | GET | /orgs/{org}/actions/permissions/fork-pr-workflows-private-repos | indexed |
| [actions/set-private-repo-fork-pr-workflows-settings-organization](https://docs.github.com/rest/actions/permissions#set-private-repo-fork-pr-workflow-settings-for-an-organization) | PUT | /orgs/{org}/actions/permissions/fork-pr-workflows-private-repos | indexed |
| [actions/list-selected-repositories-enabled-github-actions-organization](https://docs.github.com/rest/actions/permissions#list-selected-repositories-enabled-for-github-actions-in-an-organization) | GET | /orgs/{org}/actions/permissions/repositories | indexed |
| [actions/set-selected-repositories-enabled-github-actions-organization](https://docs.github.com/rest/actions/permissions#set-selected-repositories-enabled-for-github-actions-in-an-organization) | PUT | /orgs/{org}/actions/permissions/repositories | indexed |
| [actions/enable-selected-repository-github-actions-organization](https://docs.github.com/rest/actions/permissions#enable-a-selected-repository-for-github-actions-in-an-organization) | PUT | /orgs/{org}/actions/permissions/repositories/{repository_id} | indexed |
| [actions/disable-selected-repository-github-actions-organization](https://docs.github.com/rest/actions/permissions#disable-a-selected-repository-for-github-actions-in-an-organization) | DELETE | /orgs/{org}/actions/permissions/repositories/{repository_id} | indexed |
| [actions/get-allowed-actions-organization](https://docs.github.com/rest/actions/permissions#get-allowed-actions-and-reusable-workflows-for-an-organization) | GET | /orgs/{org}/actions/permissions/selected-actions | indexed |
| [actions/set-allowed-actions-organization](https://docs.github.com/rest/actions/permissions#set-allowed-actions-and-reusable-workflows-for-an-organization) | PUT | /orgs/{org}/actions/permissions/selected-actions | indexed |
| [actions/get-self-hosted-runners-permissions-organization](https://docs.github.com/rest/actions/permissions#get-self-hosted-runners-settings-for-an-organization) | GET | /orgs/{org}/actions/permissions/self-hosted-runners | indexed |
| [actions/set-self-hosted-runners-permissions-organization](https://docs.github.com/rest/actions/permissions#set-self-hosted-runners-settings-for-an-organization) | PUT | /orgs/{org}/actions/permissions/self-hosted-runners | indexed |
| [actions/list-selected-repositories-self-hosted-runners-organization](https://docs.github.com/rest/actions/permissions#list-repositories-allowed-to-use-self-hosted-runners-in-an-organization) | GET | /orgs/{org}/actions/permissions/self-hosted-runners/repositories | indexed |
| [actions/set-selected-repositories-self-hosted-runners-organization](https://docs.github.com/rest/actions/permissions#set-repositories-allowed-to-use-self-hosted-runners-in-an-organization) | PUT | /orgs/{org}/actions/permissions/self-hosted-runners/repositories | indexed |
| [actions/enable-selected-repository-self-hosted-runners-organization](https://docs.github.com/rest/actions/permissions#add-a-repository-to-the-list-of-repositories-allowed-to-use-self-hosted-runners-in-an-organization) | PUT | /orgs/{org}/actions/permissions/self-hosted-runners/repositories/{repository_id} | indexed |
| [actions/disable-selected-repository-self-hosted-runners-organization](https://docs.github.com/rest/actions/permissions#remove-a-repository-from-the-list-of-repositories-allowed-to-use-self-hosted-runners-in-an-organization) | DELETE | /orgs/{org}/actions/permissions/self-hosted-runners/repositories/{repository_id} | indexed |
| [actions/get-github-actions-default-workflow-permissions-organization](https://docs.github.com/rest/actions/permissions#get-default-workflow-permissions-for-an-organization) | GET | /orgs/{org}/actions/permissions/workflow | indexed |
| [actions/set-github-actions-default-workflow-permissions-organization](https://docs.github.com/rest/actions/permissions#set-default-workflow-permissions-for-an-organization) | PUT | /orgs/{org}/actions/permissions/workflow | indexed |
| [actions/get-org-actions-policies](https://docs.github.com/rest/actions/policies#list-organization-actions-policies) | GET | /orgs/{org}/actions/policies | indexed |
| [actions/create-org-actions-policy](https://docs.github.com/rest/actions/policies#create-an-organization-actions-policy) | POST | /orgs/{org}/actions/policies | indexed |
| [actions/get-org-actions-policy](https://docs.github.com/rest/actions/policies#get-an-organization-actions-policy) | GET | /orgs/{org}/actions/policies/{policy_id} | indexed |
| [actions/update-org-actions-policy](https://docs.github.com/rest/actions/policies#update-an-organization-actions-policy) | PUT | /orgs/{org}/actions/policies/{policy_id} | indexed |
| [actions/delete-org-actions-policy](https://docs.github.com/rest/actions/policies#delete-an-organization-actions-policy) | DELETE | /orgs/{org}/actions/policies/{policy_id} | indexed |
| [actions/list-self-hosted-runner-groups-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#list-self-hosted-runner-groups-for-an-organization) | GET | /orgs/{org}/actions/runner-groups | indexed |
| [actions/create-self-hosted-runner-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#create-a-self-hosted-runner-group-for-an-organization) | POST | /orgs/{org}/actions/runner-groups | indexed |
| [actions/get-self-hosted-runner-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#get-a-self-hosted-runner-group-for-an-organization) | GET | /orgs/{org}/actions/runner-groups/{runner_group_id} | indexed |
| [actions/update-self-hosted-runner-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#update-a-self-hosted-runner-group-for-an-organization) | PATCH | /orgs/{org}/actions/runner-groups/{runner_group_id} | indexed |
| [actions/delete-self-hosted-runner-group-from-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#delete-a-self-hosted-runner-group-from-an-organization) | DELETE | /orgs/{org}/actions/runner-groups/{runner_group_id} | indexed |
| [actions/list-github-hosted-runners-in-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#list-github-hosted-runners-in-a-group-for-an-organization) | GET | /orgs/{org}/actions/runner-groups/{runner_group_id}/hosted-runners | indexed |
| [actions/list-repo-access-to-self-hosted-runner-group-in-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#list-repository-access-to-a-self-hosted-runner-group-in-an-organization) | GET | /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | indexed |
| [actions/set-repo-access-to-self-hosted-runner-group-in-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#set-repository-access-for-a-self-hosted-runner-group-in-an-organization) | PUT | /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories | indexed |
| [actions/add-repo-access-to-self-hosted-runner-group-in-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#add-repository-access-to-a-self-hosted-runner-group-in-an-organization) | PUT | /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | indexed |
| [actions/remove-repo-access-to-self-hosted-runner-group-in-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#remove-repository-access-to-a-self-hosted-runner-group-in-an-organization) | DELETE | /orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id} | indexed |
| [actions/list-self-hosted-runners-in-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#list-self-hosted-runners-in-a-group-for-an-organization) | GET | /orgs/{org}/actions/runner-groups/{runner_group_id}/runners | indexed |
| [actions/set-self-hosted-runners-in-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#set-self-hosted-runners-in-a-group-for-an-organization) | PUT | /orgs/{org}/actions/runner-groups/{runner_group_id}/runners | indexed |
| [actions/add-self-hosted-runner-to-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#add-a-self-hosted-runner-to-a-group-for-an-organization) | PUT | /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | indexed |
| [actions/remove-self-hosted-runner-from-group-for-org](https://docs.github.com/rest/actions/self-hosted-runner-groups#remove-a-self-hosted-runner-from-a-group-for-an-organization) | DELETE | /orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id} | indexed |
| [actions/list-self-hosted-runners-for-org](https://docs.github.com/rest/actions/self-hosted-runners#list-self-hosted-runners-for-an-organization) | GET | /orgs/{org}/actions/runners | indexed |
| [actions/get-runner-version-deprecation-for-org](https://docs.github.com/rest/actions/self-hosted-runners#get-runner-version-end-of-life-schedule-for-an-organization) | GET | /orgs/{org}/actions/runners/deprecations/{version} | indexed |
| [actions/list-runner-applications-for-org](https://docs.github.com/rest/actions/self-hosted-runners#list-runner-applications-for-an-organization) | GET | /orgs/{org}/actions/runners/downloads | indexed |
| [actions/generate-runner-jitconfig-for-org](https://docs.github.com/rest/actions/self-hosted-runners#create-configuration-for-a-just-in-time-runner-for-an-organization) | POST | /orgs/{org}/actions/runners/generate-jitconfig | indexed |
| [actions/create-registration-token-for-org](https://docs.github.com/rest/actions/self-hosted-runners#create-a-registration-token-for-an-organization) | POST | /orgs/{org}/actions/runners/registration-token | indexed |
| [actions/create-remove-token-for-org](https://docs.github.com/rest/actions/self-hosted-runners#create-a-remove-token-for-an-organization) | POST | /orgs/{org}/actions/runners/remove-token | indexed |
| [actions/get-self-hosted-runner-for-org](https://docs.github.com/rest/actions/self-hosted-runners#get-a-self-hosted-runner-for-an-organization) | GET | /orgs/{org}/actions/runners/{runner_id} | indexed |
| [actions/delete-self-hosted-runner-from-org](https://docs.github.com/rest/actions/self-hosted-runners#delete-a-self-hosted-runner-from-an-organization) | DELETE | /orgs/{org}/actions/runners/{runner_id} | indexed |
| [actions/list-labels-for-self-hosted-runner-for-org](https://docs.github.com/rest/actions/self-hosted-runners#list-labels-for-a-self-hosted-runner-for-an-organization) | GET | /orgs/{org}/actions/runners/{runner_id}/labels | indexed |
| [actions/add-custom-labels-to-self-hosted-runner-for-org](https://docs.github.com/rest/actions/self-hosted-runners#add-custom-labels-to-a-self-hosted-runner-for-an-organization) | POST | /orgs/{org}/actions/runners/{runner_id}/labels | indexed |
| [actions/set-custom-labels-for-self-hosted-runner-for-org](https://docs.github.com/rest/actions/self-hosted-runners#set-custom-labels-for-a-self-hosted-runner-for-an-organization) | PUT | /orgs/{org}/actions/runners/{runner_id}/labels | indexed |
| [actions/remove-all-custom-labels-from-self-hosted-runner-for-org](https://docs.github.com/rest/actions/self-hosted-runners#remove-all-custom-labels-from-a-self-hosted-runner-for-an-organization) | DELETE | /orgs/{org}/actions/runners/{runner_id}/labels | indexed |
| [actions/remove-custom-label-from-self-hosted-runner-for-org](https://docs.github.com/rest/actions/self-hosted-runners#remove-a-custom-label-from-a-self-hosted-runner-for-an-organization) | DELETE | /orgs/{org}/actions/runners/{runner_id}/labels/{name} | indexed |
| [actions/list-org-secrets](https://docs.github.com/rest/actions/secrets#list-organization-secrets) | GET | /orgs/{org}/actions/secrets | indexed |
| [actions/get-org-public-key](https://docs.github.com/rest/actions/secrets#get-an-organization-public-key) | GET | /orgs/{org}/actions/secrets/public-key | indexed |
| [actions/get-org-secret](https://docs.github.com/rest/actions/secrets#get-an-organization-secret) | GET | /orgs/{org}/actions/secrets/{secret_name} | indexed |
| [actions/create-or-update-org-secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-organization-secret) | PUT | /orgs/{org}/actions/secrets/{secret_name} | indexed |
| [actions/delete-org-secret](https://docs.github.com/rest/actions/secrets#delete-an-organization-secret) | DELETE | /orgs/{org}/actions/secrets/{secret_name} | indexed |
| [actions/list-selected-repos-for-org-secret](https://docs.github.com/rest/actions/secrets#list-selected-repositories-for-an-organization-secret) | GET | /orgs/{org}/actions/secrets/{secret_name}/repositories | indexed |
| [actions/set-selected-repos-for-org-secret](https://docs.github.com/rest/actions/secrets#set-selected-repositories-for-an-organization-secret) | PUT | /orgs/{org}/actions/secrets/{secret_name}/repositories | indexed |
| [actions/add-selected-repo-to-org-secret](https://docs.github.com/rest/actions/secrets#add-selected-repository-to-an-organization-secret) | PUT | /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [actions/remove-selected-repo-from-org-secret](https://docs.github.com/rest/actions/secrets#remove-selected-repository-from-an-organization-secret) | DELETE | /orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [actions/list-org-variables](https://docs.github.com/rest/actions/variables#list-organization-variables) | GET | /orgs/{org}/actions/variables | indexed |
| [actions/create-org-variable](https://docs.github.com/rest/actions/variables#create-an-organization-variable) | POST | /orgs/{org}/actions/variables | indexed |
| [actions/get-org-variable](https://docs.github.com/rest/actions/variables#get-an-organization-variable) | GET | /orgs/{org}/actions/variables/{name} | indexed |
| [actions/update-org-variable](https://docs.github.com/rest/actions/variables#update-an-organization-variable) | PATCH | /orgs/{org}/actions/variables/{name} | indexed |
| [actions/delete-org-variable](https://docs.github.com/rest/actions/variables#delete-an-organization-variable) | DELETE | /orgs/{org}/actions/variables/{name} | indexed |
| [actions/list-selected-repos-for-org-variable](https://docs.github.com/rest/actions/variables#list-selected-repositories-for-an-organization-variable) | GET | /orgs/{org}/actions/variables/{name}/repositories | indexed |
| [actions/set-selected-repos-for-org-variable](https://docs.github.com/rest/actions/variables#set-selected-repositories-for-an-organization-variable) | PUT | /orgs/{org}/actions/variables/{name}/repositories | indexed |
| [actions/add-selected-repo-to-org-variable](https://docs.github.com/rest/actions/variables#add-selected-repository-to-an-organization-variable) | PUT | /orgs/{org}/actions/variables/{name}/repositories/{repository_id} | indexed |
| [actions/remove-selected-repo-from-org-variable](https://docs.github.com/rest/actions/variables#remove-selected-repository-from-an-organization-variable) | DELETE | /orgs/{org}/actions/variables/{name}/repositories/{repository_id} | indexed |
| [actions/list-artifacts-for-repo](https://docs.github.com/rest/actions/artifacts#list-artifacts-for-a-repository) | GET | /repos/{owner}/{repo}/actions/artifacts | indexed |
| [actions/get-artifact](https://docs.github.com/rest/actions/artifacts#get-an-artifact) | GET | /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | indexed |
| [actions/delete-artifact](https://docs.github.com/rest/actions/artifacts#delete-an-artifact) | DELETE | /repos/{owner}/{repo}/actions/artifacts/{artifact_id} | indexed |
| [actions/download-artifact](https://docs.github.com/rest/actions/artifacts#download-an-artifact) | GET | /repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format} | indexed |
| [actions/get-actions-cache-retention-limit-for-repository](https://docs.github.com/rest/actions/cache#get-github-actions-cache-retention-limit-for-a-repository) | GET | /repos/{owner}/{repo}/actions/cache/retention-limit | indexed |
| [actions/set-actions-cache-retention-limit-for-repository](https://docs.github.com/rest/actions/cache#set-github-actions-cache-retention-limit-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/cache/retention-limit | indexed |
| [actions/get-actions-cache-storage-limit-for-repository](https://docs.github.com/rest/actions/cache#get-github-actions-cache-storage-limit-for-a-repository) | GET | /repos/{owner}/{repo}/actions/cache/storage-limit | indexed |
| [actions/set-actions-cache-storage-limit-for-repository](https://docs.github.com/rest/actions/cache#set-github-actions-cache-storage-limit-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/cache/storage-limit | indexed |
| [actions/get-actions-cache-usage](https://docs.github.com/rest/actions/cache#get-github-actions-cache-usage-for-a-repository) | GET | /repos/{owner}/{repo}/actions/cache/usage | indexed |
| [actions/get-actions-cache-list](https://docs.github.com/rest/actions/cache#list-github-actions-caches-for-a-repository) | GET | /repos/{owner}/{repo}/actions/caches | indexed |
| [actions/delete-actions-cache-by-key](https://docs.github.com/rest/actions/cache#delete-github-actions-caches-for-a-repository-using-a-cache-key) | DELETE | /repos/{owner}/{repo}/actions/caches | indexed |
| [actions/delete-actions-cache-by-id](https://docs.github.com/rest/actions/cache#delete-a-github-actions-cache-for-a-repository-using-a-cache-id) | DELETE | /repos/{owner}/{repo}/actions/caches/{cache_id} | indexed |
| [actions/list-concurrency-groups-for-repository](https://docs.github.com/rest/actions/concurrency-groups#list-concurrency-groups-for-a-repository) | GET | /repos/{owner}/{repo}/actions/concurrency_groups | indexed |
| [actions/get-concurrency-group-for-repository](https://docs.github.com/rest/actions/concurrency-groups#get-a-concurrency-group-for-a-repository) | GET | /repos/{owner}/{repo}/actions/concurrency_groups/{concurrency_group_name} | indexed |
| [actions/get-job-for-workflow-run](https://docs.github.com/rest/actions/workflow-jobs#get-a-job-for-a-workflow-run) | GET | /repos/{owner}/{repo}/actions/jobs/{job_id} | indexed |
| [actions/download-job-logs-for-workflow-run](https://docs.github.com/rest/actions/workflow-jobs#download-job-logs-for-a-workflow-run) | GET | /repos/{owner}/{repo}/actions/jobs/{job_id}/logs | indexed |
| [actions/re-run-job-for-workflow-run](https://docs.github.com/rest/actions/workflow-runs#re-run-a-job-from-a-workflow-run) | POST | /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun | indexed |
| [actions/download-step-logs-for-workflow-run-job](https://docs.github.com/rest/actions/workflow-jobs#download-step-logs-for-a-workflow-run-job) | GET | /repos/{owner}/{repo}/actions/jobs/{job_id}/steps/{step_number}/logs | indexed |
| [actions/get-custom-oidc-sub-claim-for-repo](https://docs.github.com/rest/actions/oidc#get-the-customization-template-for-an-oidc-subject-claim-for-a-repository) | GET | /repos/{owner}/{repo}/actions/oidc/customization/sub | indexed |
| [actions/set-custom-oidc-sub-claim-for-repo](https://docs.github.com/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/oidc/customization/sub | indexed |
| [actions/list-repo-organization-secrets](https://docs.github.com/rest/actions/secrets#list-repository-organization-secrets) | GET | /repos/{owner}/{repo}/actions/organization-secrets | indexed |
| [actions/list-repo-organization-variables](https://docs.github.com/rest/actions/variables#list-repository-organization-variables) | GET | /repos/{owner}/{repo}/actions/organization-variables | indexed |
| [actions/get-github-actions-permissions-repository](https://docs.github.com/rest/actions/permissions#get-github-actions-permissions-for-a-repository) | GET | /repos/{owner}/{repo}/actions/permissions | indexed |
| [actions/set-github-actions-permissions-repository](https://docs.github.com/rest/actions/permissions#set-github-actions-permissions-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/permissions | indexed |
| [actions/get-workflow-access-to-repository](https://docs.github.com/rest/actions/permissions#get-the-level-of-access-for-workflows-outside-of-the-repository) | GET | /repos/{owner}/{repo}/actions/permissions/access | indexed |
| [actions/set-workflow-access-to-repository](https://docs.github.com/rest/actions/permissions#set-the-level-of-access-for-workflows-outside-of-the-repository) | PUT | /repos/{owner}/{repo}/actions/permissions/access | indexed |
| [actions/get-artifact-and-log-retention-settings-repository](https://docs.github.com/rest/actions/permissions#get-artifact-and-log-retention-settings-for-a-repository) | GET | /repos/{owner}/{repo}/actions/permissions/artifact-and-log-retention | indexed |
| [actions/set-artifact-and-log-retention-settings-repository](https://docs.github.com/rest/actions/permissions#set-artifact-and-log-retention-settings-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/permissions/artifact-and-log-retention | indexed |
| [actions/get-fork-pr-contributor-approval-permissions-repository](https://docs.github.com/rest/actions/permissions#get-fork-pr-contributor-approval-permissions-for-a-repository) | GET | /repos/{owner}/{repo}/actions/permissions/fork-pr-contributor-approval | indexed |
| [actions/set-fork-pr-contributor-approval-permissions-repository](https://docs.github.com/rest/actions/permissions#set-fork-pr-contributor-approval-permissions-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/permissions/fork-pr-contributor-approval | indexed |
| [actions/get-private-repo-fork-pr-workflows-settings-repository](https://docs.github.com/rest/actions/permissions#get-private-repo-fork-pr-workflow-settings-for-a-repository) | GET | /repos/{owner}/{repo}/actions/permissions/fork-pr-workflows-private-repos | indexed |
| [actions/set-private-repo-fork-pr-workflows-settings-repository](https://docs.github.com/rest/actions/permissions#set-private-repo-fork-pr-workflow-settings-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/permissions/fork-pr-workflows-private-repos | indexed |
| [actions/get-allowed-actions-repository](https://docs.github.com/rest/actions/permissions#get-allowed-actions-and-reusable-workflows-for-a-repository) | GET | /repos/{owner}/{repo}/actions/permissions/selected-actions | indexed |
| [actions/set-allowed-actions-repository](https://docs.github.com/rest/actions/permissions#set-allowed-actions-and-reusable-workflows-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/permissions/selected-actions | indexed |
| [actions/get-github-actions-default-workflow-permissions-repository](https://docs.github.com/rest/actions/permissions#get-default-workflow-permissions-for-a-repository) | GET | /repos/{owner}/{repo}/actions/permissions/workflow | indexed |
| [actions/set-github-actions-default-workflow-permissions-repository](https://docs.github.com/rest/actions/permissions#set-default-workflow-permissions-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/permissions/workflow | indexed |
| [actions/get-repo-actions-policies](https://docs.github.com/rest/actions/policies#list-repository-actions-policies) | GET | /repos/{owner}/{repo}/actions/policies | indexed |
| [actions/create-repo-actions-policy](https://docs.github.com/rest/actions/policies#create-a-repository-actions-policy) | POST | /repos/{owner}/{repo}/actions/policies | indexed |
| [actions/get-repo-actions-policy](https://docs.github.com/rest/actions/policies#get-a-repository-actions-policy) | GET | /repos/{owner}/{repo}/actions/policies/{policy_id} | indexed |
| [actions/update-repo-actions-policy](https://docs.github.com/rest/actions/policies#update-a-repository-actions-policy) | PUT | /repos/{owner}/{repo}/actions/policies/{policy_id} | indexed |
| [actions/delete-repo-actions-policy](https://docs.github.com/rest/actions/policies#delete-a-repository-actions-policy) | DELETE | /repos/{owner}/{repo}/actions/policies/{policy_id} | indexed |
| [actions/list-self-hosted-runners-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#list-self-hosted-runners-for-a-repository) | GET | /repos/{owner}/{repo}/actions/runners | indexed |
| [actions/get-runner-version-deprecation-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#get-runner-version-end-of-life-schedule-for-a-repository) | GET | /repos/{owner}/{repo}/actions/runners/deprecations/{version} | indexed |
| [actions/list-runner-applications-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#list-runner-applications-for-a-repository) | GET | /repos/{owner}/{repo}/actions/runners/downloads | indexed |
| [actions/generate-runner-jitconfig-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#create-configuration-for-a-just-in-time-runner-for-a-repository) | POST | /repos/{owner}/{repo}/actions/runners/generate-jitconfig | indexed |
| [actions/create-registration-token-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#create-a-registration-token-for-a-repository) | POST | /repos/{owner}/{repo}/actions/runners/registration-token | indexed |
| [actions/create-remove-token-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#create-a-remove-token-for-a-repository) | POST | /repos/{owner}/{repo}/actions/runners/remove-token | indexed |
| [actions/get-self-hosted-runner-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#get-a-self-hosted-runner-for-a-repository) | GET | /repos/{owner}/{repo}/actions/runners/{runner_id} | indexed |
| [actions/delete-self-hosted-runner-from-repo](https://docs.github.com/rest/actions/self-hosted-runners#delete-a-self-hosted-runner-from-a-repository) | DELETE | /repos/{owner}/{repo}/actions/runners/{runner_id} | indexed |
| [actions/list-labels-for-self-hosted-runner-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#list-labels-for-a-self-hosted-runner-for-a-repository) | GET | /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | indexed |
| [actions/add-custom-labels-to-self-hosted-runner-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#add-custom-labels-to-a-self-hosted-runner-for-a-repository) | POST | /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | indexed |
| [actions/set-custom-labels-for-self-hosted-runner-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#set-custom-labels-for-a-self-hosted-runner-for-a-repository) | PUT | /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | indexed |
| [actions/remove-all-custom-labels-from-self-hosted-runner-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#remove-all-custom-labels-from-a-self-hosted-runner-for-a-repository) | DELETE | /repos/{owner}/{repo}/actions/runners/{runner_id}/labels | indexed |
| [actions/remove-custom-label-from-self-hosted-runner-for-repo](https://docs.github.com/rest/actions/self-hosted-runners#remove-a-custom-label-from-a-self-hosted-runner-for-a-repository) | DELETE | /repos/{owner}/{repo}/actions/runners/{runner_id}/labels/{name} | indexed |
| [actions/list-workflow-runs-for-repo](https://docs.github.com/rest/actions/workflow-runs#list-workflow-runs-for-a-repository) | GET | /repos/{owner}/{repo}/actions/runs | indexed |
| [actions/get-workflow-run](https://docs.github.com/rest/actions/workflow-runs#get-a-workflow-run) | GET | /repos/{owner}/{repo}/actions/runs/{run_id} | indexed |
| [actions/delete-workflow-run](https://docs.github.com/rest/actions/workflow-runs#delete-a-workflow-run) | DELETE | /repos/{owner}/{repo}/actions/runs/{run_id} | indexed |
| [actions/get-reviews-for-run](https://docs.github.com/rest/actions/workflow-runs#get-the-review-history-for-a-workflow-run) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/approvals | indexed |
| [actions/approve-workflow-run](https://docs.github.com/rest/actions/workflow-runs#approve-a-workflow-run-for-a-fork-pull-request) | POST | /repos/{owner}/{repo}/actions/runs/{run_id}/approve | indexed |
| [actions/list-workflow-run-artifacts](https://docs.github.com/rest/actions/artifacts#list-workflow-run-artifacts) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/artifacts | indexed |
| [actions/get-workflow-run-attempt](https://docs.github.com/rest/actions/workflow-runs#get-a-workflow-run-attempt) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number} | indexed |
| [actions/list-jobs-for-workflow-run-attempt](https://docs.github.com/rest/actions/workflow-jobs#list-jobs-for-a-workflow-run-attempt) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs | indexed |
| [actions/download-workflow-run-attempt-logs](https://docs.github.com/rest/actions/workflow-runs#download-workflow-run-attempt-logs) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs | indexed |
| [actions/cancel-workflow-run](https://docs.github.com/rest/actions/workflow-runs#cancel-a-workflow-run) | POST | /repos/{owner}/{repo}/actions/runs/{run_id}/cancel | indexed |
| [actions/list-concurrency-groups-for-workflow-run](https://docs.github.com/rest/actions/concurrency-groups#list-concurrency-groups-for-a-workflow-run) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/concurrency_groups | indexed |
| [actions/review-custom-gates-for-run](https://docs.github.com/rest/actions/workflow-runs#review-custom-deployment-protection-rules-for-a-workflow-run) | POST | /repos/{owner}/{repo}/actions/runs/{run_id}/deployment_protection_rule | indexed |
| [actions/force-cancel-workflow-run](https://docs.github.com/rest/actions/workflow-runs#force-cancel-a-workflow-run) | POST | /repos/{owner}/{repo}/actions/runs/{run_id}/force-cancel | indexed |
| [actions/list-jobs-for-workflow-run](https://docs.github.com/rest/actions/workflow-jobs#list-jobs-for-a-workflow-run) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/jobs | indexed |
| [actions/download-workflow-run-logs](https://docs.github.com/rest/actions/workflow-runs#download-workflow-run-logs) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/logs | indexed |
| [actions/delete-workflow-run-logs](https://docs.github.com/rest/actions/workflow-runs#delete-workflow-run-logs) | DELETE | /repos/{owner}/{repo}/actions/runs/{run_id}/logs | indexed |
| [actions/get-pending-deployments-for-run](https://docs.github.com/rest/actions/workflow-runs#get-pending-deployments-for-a-workflow-run) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | indexed |
| [actions/review-pending-deployments-for-run](https://docs.github.com/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run) | POST | /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments | indexed |
| [actions/re-run-workflow](https://docs.github.com/rest/actions/workflow-runs#re-run-a-workflow) | POST | /repos/{owner}/{repo}/actions/runs/{run_id}/rerun | indexed |
| [actions/re-run-workflow-failed-jobs](https://docs.github.com/rest/actions/workflow-runs#re-run-failed-jobs-from-a-workflow-run) | POST | /repos/{owner}/{repo}/actions/runs/{run_id}/rerun-failed-jobs | indexed |
| [actions/get-workflow-run-usage](https://docs.github.com/rest/actions/workflow-runs#get-workflow-run-usage) | GET | /repos/{owner}/{repo}/actions/runs/{run_id}/timing | indexed |
| [actions/list-repo-secrets](https://docs.github.com/rest/actions/secrets#list-repository-secrets) | GET | /repos/{owner}/{repo}/actions/secrets | indexed |
| [actions/get-repo-public-key](https://docs.github.com/rest/actions/secrets#get-a-repository-public-key) | GET | /repos/{owner}/{repo}/actions/secrets/public-key | indexed |
| [actions/get-repo-secret](https://docs.github.com/rest/actions/secrets#get-a-repository-secret) | GET | /repos/{owner}/{repo}/actions/secrets/{secret_name} | indexed |
| [actions/create-or-update-repo-secret](https://docs.github.com/rest/actions/secrets#create-or-update-a-repository-secret) | PUT | /repos/{owner}/{repo}/actions/secrets/{secret_name} | indexed |
| [actions/delete-repo-secret](https://docs.github.com/rest/actions/secrets#delete-a-repository-secret) | DELETE | /repos/{owner}/{repo}/actions/secrets/{secret_name} | indexed |
| [actions/list-repo-variables](https://docs.github.com/rest/actions/variables#list-repository-variables) | GET | /repos/{owner}/{repo}/actions/variables | indexed |
| [actions/create-repo-variable](https://docs.github.com/rest/actions/variables#create-a-repository-variable) | POST | /repos/{owner}/{repo}/actions/variables | indexed |
| [actions/get-repo-variable](https://docs.github.com/rest/actions/variables#get-a-repository-variable) | GET | /repos/{owner}/{repo}/actions/variables/{name} | indexed |
| [actions/update-repo-variable](https://docs.github.com/rest/actions/variables#update-a-repository-variable) | PATCH | /repos/{owner}/{repo}/actions/variables/{name} | indexed |
| [actions/delete-repo-variable](https://docs.github.com/rest/actions/variables#delete-a-repository-variable) | DELETE | /repos/{owner}/{repo}/actions/variables/{name} | indexed |
| [actions/list-repo-workflows](https://docs.github.com/rest/actions/workflows#list-repository-workflows) | GET | /repos/{owner}/{repo}/actions/workflows | indexed |
| [actions/get-workflow](https://docs.github.com/rest/actions/workflows#get-a-workflow) | GET | /repos/{owner}/{repo}/actions/workflows/{workflow_id} | indexed |
| [actions/disable-workflow](https://docs.github.com/rest/actions/workflows#disable-a-workflow) | PUT | /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | indexed |
| [actions/create-workflow-dispatch](https://docs.github.com/rest/actions/workflows#create-a-workflow-dispatch-event) | POST | /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | indexed |
| [actions/enable-workflow](https://docs.github.com/rest/actions/workflows#enable-a-workflow) | PUT | /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | indexed |
| [actions/list-workflow-runs](https://docs.github.com/rest/actions/workflow-runs#list-workflow-runs-for-a-workflow) | GET | /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs | indexed |
| [actions/get-workflow-usage](https://docs.github.com/rest/actions/workflows#get-workflow-usage) | GET | /repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing | indexed |
| [actions/list-environment-secrets](https://docs.github.com/rest/actions/secrets#list-environment-secrets) | GET | /repos/{owner}/{repo}/environments/{environment_name}/secrets | indexed |
| [actions/get-environment-public-key](https://docs.github.com/rest/actions/secrets#get-an-environment-public-key) | GET | /repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key | indexed |
| [actions/get-environment-secret](https://docs.github.com/rest/actions/secrets#get-an-environment-secret) | GET | /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | indexed |
| [actions/create-or-update-environment-secret](https://docs.github.com/rest/actions/secrets#create-or-update-an-environment-secret) | PUT | /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | indexed |
| [actions/delete-environment-secret](https://docs.github.com/rest/actions/secrets#delete-an-environment-secret) | DELETE | /repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name} | indexed |
| [actions/list-environment-variables](https://docs.github.com/rest/actions/variables#list-environment-variables) | GET | /repos/{owner}/{repo}/environments/{environment_name}/variables | indexed |
| [actions/create-environment-variable](https://docs.github.com/rest/actions/variables#create-an-environment-variable) | POST | /repos/{owner}/{repo}/environments/{environment_name}/variables | indexed |
| [actions/get-environment-variable](https://docs.github.com/rest/actions/variables#get-an-environment-variable) | GET | /repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | indexed |
| [actions/update-environment-variable](https://docs.github.com/rest/actions/variables#update-an-environment-variable) | PATCH | /repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | indexed |
| [actions/delete-environment-variable](https://docs.github.com/rest/actions/variables#delete-an-environment-variable) | DELETE | /repos/{owner}/{repo}/environments/{environment_name}/variables/{name} | indexed |

## REST activity

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [activity/list-public-events](https://docs.github.com/rest/activity/events#list-public-events) | GET | /events | indexed |
| [activity/get-feeds](https://docs.github.com/rest/activity/feeds#get-feeds) | GET | /feeds | indexed |
| [activity/list-public-events-for-repo-network](https://docs.github.com/rest/activity/events#list-public-events-for-a-network-of-repositories) | GET | /networks/{owner}/{repo}/events | indexed |
| [activity/list-notifications-for-authenticated-user](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user) | GET | /notifications | indexed |
| [activity/mark-notifications-as-read](https://docs.github.com/rest/activity/notifications#mark-notifications-as-read) | PUT | /notifications | indexed |
| [activity/get-thread](https://docs.github.com/rest/activity/notifications#get-a-thread) | GET | /notifications/threads/{thread_id} | indexed |
| [activity/mark-thread-as-read](https://docs.github.com/rest/activity/notifications#mark-a-thread-as-read) | PATCH | /notifications/threads/{thread_id} | indexed |
| [activity/mark-thread-as-done](https://docs.github.com/rest/activity/notifications#mark-a-thread-as-done) | DELETE | /notifications/threads/{thread_id} | indexed |
| [activity/get-thread-subscription-for-authenticated-user](https://docs.github.com/rest/activity/notifications#get-a-thread-subscription-for-the-authenticated-user) | GET | /notifications/threads/{thread_id}/subscription | indexed |
| [activity/set-thread-subscription](https://docs.github.com/rest/activity/notifications#set-a-thread-subscription) | PUT | /notifications/threads/{thread_id}/subscription | indexed |
| [activity/delete-thread-subscription](https://docs.github.com/rest/activity/notifications#delete-a-thread-subscription) | DELETE | /notifications/threads/{thread_id}/subscription | indexed |
| [activity/list-public-org-events](https://docs.github.com/rest/activity/events#list-public-organization-events) | GET | /orgs/{org}/events | indexed |
| [activity/list-repo-events](https://docs.github.com/rest/activity/events#list-repository-events) | GET | /repos/{owner}/{repo}/events | indexed |
| [activity/list-repo-notifications-for-authenticated-user](https://docs.github.com/rest/activity/notifications#list-repository-notifications-for-the-authenticated-user) | GET | /repos/{owner}/{repo}/notifications | indexed |
| [activity/mark-repo-notifications-as-read](https://docs.github.com/rest/activity/notifications#mark-repository-notifications-as-read) | PUT | /repos/{owner}/{repo}/notifications | indexed |
| [activity/list-stargazers-for-repo](https://docs.github.com/rest/activity/starring#list-stargazers) | GET | /repos/{owner}/{repo}/stargazers | indexed |
| [activity/get-stargazer-count-for-repo](https://docs.github.com/rest/activity/starring#get-stargazer-count) | GET | /repos/{owner}/{repo}/stargazers/count | indexed |
| [activity/get-stargazer-history-for-repo](https://docs.github.com/rest/activity/starring#get-repository-star-history) | GET | /repos/{owner}/{repo}/stargazers/history | indexed |
| [activity/list-watchers-for-repo](https://docs.github.com/rest/activity/watching#list-watchers) | GET | /repos/{owner}/{repo}/subscribers | indexed |
| [activity/get-repo-subscription](https://docs.github.com/rest/activity/watching#get-a-repository-subscription) | GET | /repos/{owner}/{repo}/subscription | indexed |
| [activity/set-repo-subscription](https://docs.github.com/rest/activity/watching#set-a-repository-subscription) | PUT | /repos/{owner}/{repo}/subscription | indexed |
| [activity/delete-repo-subscription](https://docs.github.com/rest/activity/watching#delete-a-repository-subscription) | DELETE | /repos/{owner}/{repo}/subscription | indexed |
| [activity/list-repos-starred-by-authenticated-user](https://docs.github.com/rest/activity/starring#list-repositories-starred-by-the-authenticated-user) | GET | /user/starred | indexed |
| [activity/check-repo-is-starred-by-authenticated-user](https://docs.github.com/rest/activity/starring#check-if-a-repository-is-starred-by-the-authenticated-user) | GET | /user/starred/{owner}/{repo} | indexed |
| [activity/star-repo-for-authenticated-user](https://docs.github.com/rest/activity/starring#star-a-repository-for-the-authenticated-user) | PUT | /user/starred/{owner}/{repo} | indexed |
| [activity/unstar-repo-for-authenticated-user](https://docs.github.com/rest/activity/starring#unstar-a-repository-for-the-authenticated-user) | DELETE | /user/starred/{owner}/{repo} | indexed |
| [activity/list-watched-repos-for-authenticated-user](https://docs.github.com/rest/activity/watching#list-repositories-watched-by-the-authenticated-user) | GET | /user/subscriptions | indexed |
| [activity/list-events-for-authenticated-user](https://docs.github.com/rest/activity/events#list-events-for-the-authenticated-user) | GET | /users/{username}/events | indexed |
| [activity/list-org-events-for-authenticated-user](https://docs.github.com/rest/activity/events#list-organization-events-for-the-authenticated-user) | GET | /users/{username}/events/orgs/{org} | indexed |
| [activity/list-public-events-for-user](https://docs.github.com/rest/activity/events#list-public-events-for-a-user) | GET | /users/{username}/events/public | indexed |
| [activity/list-received-events-for-user](https://docs.github.com/rest/activity/events#list-events-received-by-the-authenticated-user) | GET | /users/{username}/received_events | indexed |
| [activity/list-received-public-events-for-user](https://docs.github.com/rest/activity/events#list-public-events-received-by-a-user) | GET | /users/{username}/received_events/public | indexed |
| [activity/list-repos-starred-by-user](https://docs.github.com/rest/activity/starring#list-repositories-starred-by-a-user) | GET | /users/{username}/starred | indexed |
| [activity/list-repos-watched-by-user](https://docs.github.com/rest/activity/watching#list-repositories-watched-by-a-user) | GET | /users/{username}/subscriptions | indexed |

## REST agent-automations

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [agent-automations/list-automations](https://docs.github.com/rest/agent-automations/agent-automations#list-automations-for-user) | GET | /agents/automations | indexed |
| [agent-automations/list-repo-automations](https://docs.github.com/rest/agent-automations/agent-automations#list-automations-for-a-repository) | GET | /agents/repos/{owner}/{repo}/automations | indexed |
| [agent-automations/create-repo-automation](https://docs.github.com/rest/agent-automations/agent-automations#create-an-automation-for-a-repository) | POST | /agents/repos/{owner}/{repo}/automations | indexed |
| [agent-automations/list-available-repo-automation-tools](https://docs.github.com/rest/agent-automations/agent-automations#list-available-automation-tools-for-a-repository) | GET | /agents/repos/{owner}/{repo}/automations/available-tools | indexed |
| [agent-automations/list-available-repo-automation-triggers](https://docs.github.com/rest/agent-automations/agent-automations#list-available-automation-triggers-for-a-repository) | GET | /agents/repos/{owner}/{repo}/automations/available-triggers | indexed |
| [agent-automations/get-repo-automation](https://docs.github.com/rest/agent-automations/agent-automations#get-an-automation) | GET | /agents/repos/{owner}/{repo}/automations/{automation_id} | indexed |
| [agent-automations/edit-repo-automation](https://docs.github.com/rest/agent-automations/agent-automations#update-an-automation) | PATCH | /agents/repos/{owner}/{repo}/automations/{automation_id} | indexed |
| [agent-automations/delete-repo-automation](https://docs.github.com/rest/agent-automations/agent-automations#delete-an-automation) | DELETE | /agents/repos/{owner}/{repo}/automations/{automation_id} | indexed |
| [agent-automations/list-automation-revisions](https://docs.github.com/rest/agent-automations/agent-automations#list-revisions-for-an-automation) | GET | /agents/repos/{owner}/{repo}/automations/{automation_id}/revisions | indexed |
| [agent-automations/get-automation-revision](https://docs.github.com/rest/agent-automations/agent-automations#get-an-automation-revision) | GET | /agents/repos/{owner}/{repo}/automations/{automation_id}/revisions/{revision_id} | indexed |
| [agent-automations/list-repo-automation-tasks](https://docs.github.com/rest/agent-automations/agent-automations#list-tasks-for-an-automation-in-a-repository) | GET | /agents/repos/{owner}/{repo}/automations/{automation_id}/tasks | indexed |
| [agent-automations/create-repo-automation-task](https://docs.github.com/rest/agent-automations/agent-automations#run-an-automation) | POST | /agents/repos/{owner}/{repo}/automations/{automation_id}/tasks | indexed |

## REST agent-merge

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [agent-merge/get-agent-merge-enrollment](https://docs.github.com/rest/pulls/agent-merge#get-agent-merge-configuration-for-a-pull-request) | GET | /agents/repos/{owner}/{repo}/pulls/{pull_number}/agent-merge | indexed |
| [agent-merge/put-agent-merge-enrollment](https://docs.github.com/rest/pulls/agent-merge#update-agent-merge-configuration-for-a-pull-request) | PUT | /agents/repos/{owner}/{repo}/pulls/{pull_number}/agent-merge | indexed |
| [agent-merge/delete-agent-merge-enrollment](https://docs.github.com/rest/pulls/agent-merge#disable-agent-merge-for-a-pull-request) | DELETE | /agents/repos/{owner}/{repo}/pulls/{pull_number}/agent-merge | indexed |

## REST agent-tasks

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [agent-tasks/list-tasks-for-repo](https://docs.github.com/rest/agent-tasks/agent-tasks#list-tasks-for-repository) | GET | /agents/repos/{owner}/{repo}/tasks | indexed |
| [agent-tasks/create-task-in-repo](https://docs.github.com/rest/agent-tasks/agent-tasks#start-a-task) | POST | /agents/repos/{owner}/{repo}/tasks | indexed |
| [agent-tasks/get-task-by-repo-and-id](https://docs.github.com/rest/agent-tasks/agent-tasks#get-a-task-by-repo) | GET | /agents/repos/{owner}/{repo}/tasks/{task_id} | indexed |
| [agent-tasks/list-tasks](https://docs.github.com/rest/agent-tasks/agent-tasks#list-tasks) | GET | /agents/tasks | indexed |
| [agent-tasks/get-task-by-id](https://docs.github.com/rest/agent-tasks/agent-tasks#get-a-task-by-id) | GET | /agents/tasks/{task_id} | indexed |

## REST agents

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [agents/list-org-secrets](https://docs.github.com/rest/agents/secrets#list-organization-secrets) | GET | /orgs/{org}/agents/secrets | indexed |
| [agents/get-org-public-key](https://docs.github.com/rest/agents/secrets#get-an-organization-public-key) | GET | /orgs/{org}/agents/secrets/public-key | indexed |
| [agents/get-org-secret](https://docs.github.com/rest/agents/secrets#get-an-organization-secret) | GET | /orgs/{org}/agents/secrets/{secret_name} | indexed |
| [agents/create-or-update-org-secret](https://docs.github.com/rest/agents/secrets#create-or-update-an-organization-secret) | PUT | /orgs/{org}/agents/secrets/{secret_name} | indexed |
| [agents/delete-org-secret](https://docs.github.com/rest/agents/secrets#delete-an-organization-secret) | DELETE | /orgs/{org}/agents/secrets/{secret_name} | indexed |
| [agents/list-selected-repos-for-org-secret](https://docs.github.com/rest/agents/secrets#list-selected-repositories-for-an-organization-secret) | GET | /orgs/{org}/agents/secrets/{secret_name}/repositories | indexed |
| [agents/set-selected-repos-for-org-secret](https://docs.github.com/rest/agents/secrets#set-selected-repositories-for-an-organization-secret) | PUT | /orgs/{org}/agents/secrets/{secret_name}/repositories | indexed |
| [agents/add-selected-repo-to-org-secret](https://docs.github.com/rest/agents/secrets#add-selected-repository-to-an-organization-secret) | PUT | /orgs/{org}/agents/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [agents/remove-selected-repo-from-org-secret](https://docs.github.com/rest/agents/secrets#remove-selected-repository-from-an-organization-secret) | DELETE | /orgs/{org}/agents/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [agents/list-org-variables](https://docs.github.com/rest/agents/variables#list-organization-variables) | GET | /orgs/{org}/agents/variables | indexed |
| [agents/create-org-variable](https://docs.github.com/rest/agents/variables#create-an-organization-variable) | POST | /orgs/{org}/agents/variables | indexed |
| [agents/get-org-variable](https://docs.github.com/rest/agents/variables#get-an-organization-variable) | GET | /orgs/{org}/agents/variables/{name} | indexed |
| [agents/update-org-variable](https://docs.github.com/rest/agents/variables#update-an-organization-variable) | PATCH | /orgs/{org}/agents/variables/{name} | indexed |
| [agents/delete-org-variable](https://docs.github.com/rest/agents/variables#delete-an-organization-variable) | DELETE | /orgs/{org}/agents/variables/{name} | indexed |
| [agents/list-selected-repos-for-org-variable](https://docs.github.com/rest/agents/variables#list-selected-repositories-for-an-organization-variable) | GET | /orgs/{org}/agents/variables/{name}/repositories | indexed |
| [agents/set-selected-repos-for-org-variable](https://docs.github.com/rest/agents/variables#set-selected-repositories-for-an-organization-variable) | PUT | /orgs/{org}/agents/variables/{name}/repositories | indexed |
| [agents/add-selected-repo-to-org-variable](https://docs.github.com/rest/agents/variables#add-selected-repository-to-an-organization-variable) | PUT | /orgs/{org}/agents/variables/{name}/repositories/{repository_id} | indexed |
| [agents/remove-selected-repo-from-org-variable](https://docs.github.com/rest/agents/variables#remove-selected-repository-from-an-organization-variable) | DELETE | /orgs/{org}/agents/variables/{name}/repositories/{repository_id} | indexed |
| [agents/list-repo-organization-secrets](https://docs.github.com/rest/agents/secrets#list-repository-organization-secrets) | GET | /repos/{owner}/{repo}/agents/organization-secrets | indexed |
| [agents/list-repo-organization-variables](https://docs.github.com/rest/agents/variables#list-repository-organization-variables) | GET | /repos/{owner}/{repo}/agents/organization-variables | indexed |
| [agents/list-repo-secrets](https://docs.github.com/rest/agents/secrets#list-repository-secrets) | GET | /repos/{owner}/{repo}/agents/secrets | indexed |
| [agents/get-repo-public-key](https://docs.github.com/rest/agents/secrets#get-a-repository-public-key) | GET | /repos/{owner}/{repo}/agents/secrets/public-key | indexed |
| [agents/get-repo-secret](https://docs.github.com/rest/agents/secrets#get-a-repository-secret) | GET | /repos/{owner}/{repo}/agents/secrets/{secret_name} | indexed |
| [agents/create-or-update-repo-secret](https://docs.github.com/rest/agents/secrets#create-or-update-a-repository-secret) | PUT | /repos/{owner}/{repo}/agents/secrets/{secret_name} | indexed |
| [agents/delete-repo-secret](https://docs.github.com/rest/agents/secrets#delete-a-repository-secret) | DELETE | /repos/{owner}/{repo}/agents/secrets/{secret_name} | indexed |
| [agents/list-repo-variables](https://docs.github.com/rest/agents/variables#list-repository-variables) | GET | /repos/{owner}/{repo}/agents/variables | indexed |
| [agents/create-repo-variable](https://docs.github.com/rest/agents/variables#create-a-repository-variable) | POST | /repos/{owner}/{repo}/agents/variables | indexed |
| [agents/get-repo-variable](https://docs.github.com/rest/agents/variables#get-a-repository-variable) | GET | /repos/{owner}/{repo}/agents/variables/{name} | indexed |
| [agents/update-repo-variable](https://docs.github.com/rest/agents/variables#update-a-repository-variable) | PATCH | /repos/{owner}/{repo}/agents/variables/{name} | indexed |
| [agents/delete-repo-variable](https://docs.github.com/rest/agents/variables#delete-a-repository-variable) | DELETE | /repos/{owner}/{repo}/agents/variables/{name} | indexed |

## REST apps

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [apps/get-authenticated](https://docs.github.com/rest/apps/apps#get-the-authenticated-app) | GET | /app | indexed |
| [apps/create-from-manifest](https://docs.github.com/rest/apps/apps#create-a-github-app-from-a-manifest) | POST | /app-manifests/{code}/conversions | indexed |
| [apps/get-webhook-config-for-app](https://docs.github.com/rest/apps/webhooks#get-a-webhook-configuration-for-an-app) | GET | /app/hook/config | indexed |
| [apps/update-webhook-config-for-app](https://docs.github.com/rest/apps/webhooks#update-a-webhook-configuration-for-an-app) | PATCH | /app/hook/config | indexed |
| [apps/list-webhook-deliveries](https://docs.github.com/rest/apps/webhooks#list-deliveries-for-an-app-webhook) | GET | /app/hook/deliveries | indexed |
| [apps/get-webhook-delivery](https://docs.github.com/rest/apps/webhooks#get-a-delivery-for-an-app-webhook) | GET | /app/hook/deliveries/{delivery_id} | indexed |
| [apps/redeliver-webhook-delivery](https://docs.github.com/rest/apps/webhooks#redeliver-a-delivery-for-an-app-webhook) | POST | /app/hook/deliveries/{delivery_id}/attempts | indexed |
| [apps/list-installation-requests-for-authenticated-app](https://docs.github.com/rest/apps/apps#list-installation-requests-for-the-authenticated-app) | GET | /app/installation-requests | indexed |
| [apps/list-installations](https://docs.github.com/rest/apps/apps#list-installations-for-the-authenticated-app) | GET | /app/installations | indexed |
| [apps/get-installation](https://docs.github.com/rest/apps/apps#get-an-installation-for-the-authenticated-app) | GET | /app/installations/{installation_id} | indexed |
| [apps/delete-installation](https://docs.github.com/rest/apps/apps#delete-an-installation-for-the-authenticated-app) | DELETE | /app/installations/{installation_id} | indexed |
| [apps/create-installation-access-token](https://docs.github.com/rest/apps/apps#create-an-installation-access-token-for-an-app) | POST | /app/installations/{installation_id}/access_tokens | indexed |
| [apps/suspend-installation](https://docs.github.com/rest/apps/apps#suspend-an-app-installation) | PUT | /app/installations/{installation_id}/suspended | indexed |
| [apps/unsuspend-installation](https://docs.github.com/rest/apps/apps#unsuspend-an-app-installation) | DELETE | /app/installations/{installation_id}/suspended | indexed |
| [apps/delete-authorization](https://docs.github.com/rest/apps/oauth-applications#delete-an-app-authorization) | DELETE | /applications/{client_id}/grant | indexed |
| [apps/check-token](https://docs.github.com/rest/apps/oauth-applications#check-a-token) | POST | /applications/{client_id}/token | indexed |
| [apps/reset-token](https://docs.github.com/rest/apps/oauth-applications#reset-a-token) | PATCH | /applications/{client_id}/token | indexed |
| [apps/delete-token](https://docs.github.com/rest/apps/oauth-applications#delete-an-app-token) | DELETE | /applications/{client_id}/token | indexed |
| [apps/scope-token](https://docs.github.com/rest/apps/apps#create-a-scoped-access-token) | POST | /applications/{client_id}/token/scoped | indexed |
| [apps/get-by-slug](https://docs.github.com/rest/apps/apps#get-an-app) | GET | /apps/{app_slug} | indexed |
| [apps/list-repos-accessible-to-installation](https://docs.github.com/rest/apps/installations#list-repositories-accessible-to-the-app-installation) | GET | /installation/repositories | indexed |
| [apps/revoke-installation-access-token](https://docs.github.com/rest/apps/installations#revoke-an-installation-access-token) | DELETE | /installation/token | indexed |
| [apps/get-subscription-plan-for-account](https://docs.github.com/rest/apps/marketplace#get-a-subscription-plan-for-an-account) | GET | /marketplace_listing/accounts/{account_id} | indexed |
| [apps/list-plans](https://docs.github.com/rest/apps/marketplace#list-plans) | GET | /marketplace_listing/plans | indexed |
| [apps/list-accounts-for-plan](https://docs.github.com/rest/apps/marketplace#list-accounts-for-a-plan) | GET | /marketplace_listing/plans/{plan_id}/accounts | indexed |
| [apps/get-subscription-plan-for-account-stubbed](https://docs.github.com/rest/apps/marketplace#get-a-subscription-plan-for-an-account-stubbed) | GET | /marketplace_listing/stubbed/accounts/{account_id} | indexed |
| [apps/list-plans-stubbed](https://docs.github.com/rest/apps/marketplace#list-plans-stubbed) | GET | /marketplace_listing/stubbed/plans | indexed |
| [apps/list-accounts-for-plan-stubbed](https://docs.github.com/rest/apps/marketplace#list-accounts-for-a-plan-stubbed) | GET | /marketplace_listing/stubbed/plans/{plan_id}/accounts | indexed |
| [apps/get-org-installation](https://docs.github.com/rest/apps/apps#get-an-organization-installation-for-the-authenticated-app) | GET | /orgs/{org}/installation | indexed |
| [apps/get-repo-installation](https://docs.github.com/rest/apps/apps#get-a-repository-installation-for-the-authenticated-app) | GET | /repos/{owner}/{repo}/installation | indexed |
| [apps/list-installations-for-authenticated-user](https://docs.github.com/rest/apps/installations#list-app-installations-accessible-to-the-user-access-token) | GET | /user/installations | indexed |
| [apps/list-installation-repos-for-authenticated-user](https://docs.github.com/rest/apps/installations#list-repositories-accessible-to-the-user-access-token) | GET | /user/installations/{installation_id}/repositories | indexed |
| [apps/add-repo-to-installation-for-authenticated-user](https://docs.github.com/rest/apps/installations#add-a-repository-to-an-app-installation) | PUT | /user/installations/{installation_id}/repositories/{repository_id} | indexed |
| [apps/remove-repo-from-installation-for-authenticated-user](https://docs.github.com/rest/apps/installations#remove-a-repository-from-an-app-installation) | DELETE | /user/installations/{installation_id}/repositories/{repository_id} | indexed |
| [apps/list-subscriptions-for-authenticated-user](https://docs.github.com/rest/apps/marketplace#list-subscriptions-for-the-authenticated-user) | GET | /user/marketplace_purchases | indexed |
| [apps/list-subscriptions-for-authenticated-user-stubbed](https://docs.github.com/rest/apps/marketplace#list-subscriptions-for-the-authenticated-user-stubbed) | GET | /user/marketplace_purchases/stubbed | indexed |
| [apps/get-user-installation](https://docs.github.com/rest/apps/apps#get-a-user-installation-for-the-authenticated-app) | GET | /users/{username}/installation | indexed |

## REST billing

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [billing/get-github-billing-ai-credit-usage-report-org](https://docs.github.com/rest/billing/usage#get-billing-ai-credit-usage-report-for-an-organization) | GET | /organizations/{org}/settings/billing/ai_credit/usage | indexed |
| [billing/get-all-budgets-org](https://docs.github.com/rest/billing/budgets#get-all-budgets-for-an-organization) | GET | /organizations/{org}/settings/billing/budgets | indexed |
| [billing/create-organization-budget](https://docs.github.com/rest/billing/budgets#create-a-budget-for-an-organization) | POST | /organizations/{org}/settings/billing/budgets | indexed |
| [billing/get-budget-org](https://docs.github.com/rest/billing/budgets#get-a-budget-by-id-for-an-organization) | GET | /organizations/{org}/settings/billing/budgets/{budget_id} | indexed |
| [billing/update-budget-org](https://docs.github.com/rest/billing/budgets#update-a-budget-for-an-organization) | PATCH | /organizations/{org}/settings/billing/budgets/{budget_id} | indexed |
| [billing/delete-budget-org](https://docs.github.com/rest/billing/budgets#delete-a-budget-for-an-organization) | DELETE | /organizations/{org}/settings/billing/budgets/{budget_id} | indexed |
| [billing/get-github-billing-premium-request-usage-report-org](https://docs.github.com/rest/billing/usage#get-billing-premium-request-usage-report-for-an-organization) | GET | /organizations/{org}/settings/billing/premium_request/usage | indexed |
| [billing/get-github-billing-usage-report-org](https://docs.github.com/rest/billing/usage#get-billing-usage-report-for-an-organization) | GET | /organizations/{org}/settings/billing/usage | indexed |
| [billing/get-github-billing-usage-summary-report-org](https://docs.github.com/rest/billing/usage#get-billing-usage-summary-for-an-organization) | GET | /organizations/{org}/settings/billing/usage/summary | indexed |
| [billing/get-github-billing-ai-credit-usage-report-user](https://docs.github.com/rest/billing/usage#get-billing-ai-credit-usage-report-for-a-user) | GET | /users/{username}/settings/billing/ai_credit/usage | indexed |
| [billing/get-github-billing-premium-request-usage-report-user](https://docs.github.com/rest/billing/usage#get-billing-premium-request-usage-report-for-a-user) | GET | /users/{username}/settings/billing/premium_request/usage | indexed |
| [billing/get-github-billing-usage-report-user](https://docs.github.com/rest/billing/usage#get-billing-usage-report-for-a-user) | GET | /users/{username}/settings/billing/usage | indexed |
| [billing/get-github-billing-usage-summary-report-user](https://docs.github.com/rest/billing/usage#get-billing-usage-summary-for-a-user) | GET | /users/{username}/settings/billing/usage/summary | indexed |

## REST campaigns

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [campaigns/list-org-campaigns](https://docs.github.com/rest/campaigns/campaigns#list-campaigns-for-an-organization) | GET | /orgs/{org}/campaigns | indexed |
| [campaigns/create-campaign](https://docs.github.com/rest/campaigns/campaigns#create-a-campaign-for-an-organization) | POST | /orgs/{org}/campaigns | indexed |
| [campaigns/get-campaign-summary](https://docs.github.com/rest/campaigns/campaigns#get-a-campaign-for-an-organization) | GET | /orgs/{org}/campaigns/{campaign_number} | indexed |
| [campaigns/update-campaign](https://docs.github.com/rest/campaigns/campaigns#update-a-campaign) | PATCH | /orgs/{org}/campaigns/{campaign_number} | indexed |
| [campaigns/delete-campaign](https://docs.github.com/rest/campaigns/campaigns#delete-a-campaign-for-an-organization) | DELETE | /orgs/{org}/campaigns/{campaign_number} | indexed |

## REST checks

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [checks/create](https://docs.github.com/rest/checks/runs#create-a-check-run) | POST | /repos/{owner}/{repo}/check-runs | indexed |
| [checks/get](https://docs.github.com/rest/checks/runs#get-a-check-run) | GET | /repos/{owner}/{repo}/check-runs/{check_run_id} | indexed |
| [checks/update](https://docs.github.com/rest/checks/runs#update-a-check-run) | PATCH | /repos/{owner}/{repo}/check-runs/{check_run_id} | indexed |
| [checks/list-annotations](https://docs.github.com/rest/checks/runs#list-check-run-annotations) | GET | /repos/{owner}/{repo}/check-runs/{check_run_id}/annotations | indexed |
| [checks/rerequest-run](https://docs.github.com/rest/checks/runs#rerequest-a-check-run) | POST | /repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest | indexed |
| [checks/create-suite](https://docs.github.com/rest/checks/suites#create-a-check-suite) | POST | /repos/{owner}/{repo}/check-suites | indexed |
| [checks/set-suites-preferences](https://docs.github.com/rest/checks/suites#update-repository-preferences-for-check-suites) | PATCH | /repos/{owner}/{repo}/check-suites/preferences | indexed |
| [checks/get-suite](https://docs.github.com/rest/checks/suites#get-a-check-suite) | GET | /repos/{owner}/{repo}/check-suites/{check_suite_id} | indexed |
| [checks/list-for-suite](https://docs.github.com/rest/checks/runs#list-check-runs-in-a-check-suite) | GET | /repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs | indexed |
| [checks/rerequest-suite](https://docs.github.com/rest/checks/suites#rerequest-a-check-suite) | POST | /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest | indexed |
| [checks/list-for-ref](https://docs.github.com/rest/checks/runs#list-check-runs-for-a-git-reference) | GET | /repos/{owner}/{repo}/commits/{ref}/check-runs | indexed |
| [checks/list-suites-for-ref](https://docs.github.com/rest/checks/suites#list-check-suites-for-a-git-reference) | GET | /repos/{owner}/{repo}/commits/{ref}/check-suites | indexed |

## REST classroom

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [classroom/get-an-assignment](https://docs.github.com/rest/classroom/classroom#closed---get-an-assignment) | GET | /assignments/{assignment_id} | retired |
| [classroom/list-accepted-assignments-for-an-assignment](https://docs.github.com/rest/classroom/classroom#closed---list-accepted-assignments-for-an-assignment) | GET | /assignments/{assignment_id}/accepted_assignments | retired |
| [classroom/get-assignment-grades](https://docs.github.com/rest/classroom/classroom#closed---get-assignment-grades) | GET | /assignments/{assignment_id}/grades | retired |
| [classroom/list-classrooms](https://docs.github.com/rest/classroom/classroom#closed---list-classrooms) | GET | /classrooms | retired |
| [classroom/get-a-classroom](https://docs.github.com/rest/classroom/classroom#closed---get-a-classroom) | GET | /classrooms/{classroom_id} | retired |
| [classroom/list-assignments-for-a-classroom](https://docs.github.com/rest/classroom/classroom#closed---list-assignments-for-a-classroom) | GET | /classrooms/{classroom_id}/assignments | retired |

## REST code-quality

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [code-quality/list-findings-for-repo](https://docs.github.com/rest/code-quality/code-quality#list-code-quality-findings-for-a-repository) | GET | /repos/{owner}/{repo}/code-quality/findings | indexed |
| [code-quality/get-finding](https://docs.github.com/rest/code-quality/code-quality#get-a-code-quality-finding) | GET | /repos/{owner}/{repo}/code-quality/findings/{finding_number} | indexed |
| [code-quality/get-setup](https://docs.github.com/rest/code-quality/code-quality#get-a-code-quality-setup-configuration) | GET | /repos/{owner}/{repo}/code-quality/setup | indexed |
| [code-quality/update-setup](https://docs.github.com/rest/code-quality/code-quality#update-a-code-quality-setup-configuration) | PATCH | /repos/{owner}/{repo}/code-quality/setup | indexed |

## REST code-scanning

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [code-scanning/get-ai-scan-enablement-for-org](https://docs.github.com/rest/code-scanning/code-scanning#get-the-ai-scan-setting-for-an-organization) | GET | /orgs/{org}/code-scanning/ai-scan | indexed |
| [code-scanning/update-ai-scan-enablement-for-org](https://docs.github.com/rest/code-scanning/code-scanning#update-the-ai-scan-setting-for-an-organization) | PATCH | /orgs/{org}/code-scanning/ai-scan | indexed |
| [code-scanning/list-alerts-for-org](https://docs.github.com/rest/code-scanning/code-scanning#list-code-scanning-alerts-for-an-organization) | GET | /orgs/{org}/code-scanning/alerts | indexed |
| [code-scanning/get-ai-scan-enablement](https://docs.github.com/rest/code-scanning/code-scanning#get-ai-scan-enablement-for-a-repository) | GET | /repos/{owner}/{repo}/code-scanning/ai-scan | indexed |
| [code-scanning/update-ai-scan-enablement](https://docs.github.com/rest/code-scanning/code-scanning#update-ai-scan-enablement-for-a-repository) | PATCH | /repos/{owner}/{repo}/code-scanning/ai-scan | indexed |
| [code-scanning/list-alerts-for-repo](https://docs.github.com/rest/code-scanning/code-scanning#list-code-scanning-alerts-for-a-repository) | GET | /repos/{owner}/{repo}/code-scanning/alerts | indexed |
| [code-scanning/get-alert](https://docs.github.com/rest/code-scanning/code-scanning#get-a-code-scanning-alert) | GET | /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | indexed |
| [code-scanning/update-alert](https://docs.github.com/rest/code-scanning/code-scanning#update-a-code-scanning-alert) | PATCH | /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | indexed |
| [code-scanning/get-autofix](https://docs.github.com/rest/code-scanning/code-scanning#get-the-status-of-an-autofix-for-a-code-scanning-alert) | GET | /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | indexed |
| [code-scanning/create-autofix](https://docs.github.com/rest/code-scanning/code-scanning#create-an-autofix-for-a-code-scanning-alert) | POST | /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | indexed |
| [code-scanning/commit-autofix](https://docs.github.com/rest/code-scanning/code-scanning#commit-an-autofix-for-a-code-scanning-alert) | POST | /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix/commits | indexed |
| [code-scanning/list-alert-instances](https://docs.github.com/rest/code-scanning/code-scanning#list-instances-of-a-code-scanning-alert) | GET | /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances | indexed |
| [code-scanning/list-recent-analyses](https://docs.github.com/rest/code-scanning/code-scanning#list-code-scanning-analyses-for-a-repository) | GET | /repos/{owner}/{repo}/code-scanning/analyses | indexed |
| [code-scanning/get-analysis](https://docs.github.com/rest/code-scanning/code-scanning#get-a-code-scanning-analysis-for-a-repository) | GET | /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | indexed |
| [code-scanning/delete-analysis](https://docs.github.com/rest/code-scanning/code-scanning#delete-a-code-scanning-analysis-from-a-repository) | DELETE | /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | indexed |
| [code-scanning/list-codeql-databases](https://docs.github.com/rest/code-scanning/code-scanning#list-codeql-databases-for-a-repository) | GET | /repos/{owner}/{repo}/code-scanning/codeql/databases | indexed |
| [code-scanning/get-codeql-database](https://docs.github.com/rest/code-scanning/code-scanning#get-a-codeql-database-for-a-repository) | GET | /repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | indexed |
| [code-scanning/delete-codeql-database](https://docs.github.com/rest/code-scanning/code-scanning#delete-a-codeql-database) | DELETE | /repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | indexed |
| [code-scanning/create-variant-analysis](https://docs.github.com/rest/code-scanning/code-scanning#create-a-codeql-variant-analysis) | POST | /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses | indexed |
| [code-scanning/get-variant-analysis](https://docs.github.com/rest/code-scanning/code-scanning#get-the-summary-of-a-codeql-variant-analysis) | GET | /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id} | indexed |
| [code-scanning/get-variant-analysis-repo-task](https://docs.github.com/rest/code-scanning/code-scanning#get-the-analysis-status-of-a-repository-in-a-codeql-variant-analysis) | GET | /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}/repos/{repo_owner}/{repo_name} | indexed |
| [code-scanning/get-default-setup](https://docs.github.com/rest/code-scanning/code-scanning#get-a-code-scanning-default-setup-configuration) | GET | /repos/{owner}/{repo}/code-scanning/default-setup | indexed |
| [code-scanning/update-default-setup](https://docs.github.com/rest/code-scanning/code-scanning#update-a-code-scanning-default-setup-configuration) | PATCH | /repos/{owner}/{repo}/code-scanning/default-setup | indexed |
| [code-scanning/upload-sarif](https://docs.github.com/rest/code-scanning/code-scanning#upload-an-analysis-as-sarif-data) | POST | /repos/{owner}/{repo}/code-scanning/sarifs | indexed |
| [code-scanning/get-sarif](https://docs.github.com/rest/code-scanning/code-scanning#get-information-about-a-sarif-upload) | GET | /repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id} | indexed |

## REST code-security

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [code-security/get-configurations-for-enterprise](https://docs.github.com/rest/code-security/configurations#get-code-security-configurations-for-an-enterprise) | GET | /enterprises/{enterprise}/code-security/configurations | indexed |
| [code-security/create-configuration-for-enterprise](https://docs.github.com/rest/code-security/configurations#create-a-code-security-configuration-for-an-enterprise) | POST | /enterprises/{enterprise}/code-security/configurations | indexed |
| [code-security/get-default-configurations-for-enterprise](https://docs.github.com/rest/code-security/configurations#get-default-code-security-configurations-for-an-enterprise) | GET | /enterprises/{enterprise}/code-security/configurations/defaults | indexed |
| [code-security/get-single-configuration-for-enterprise](https://docs.github.com/rest/code-security/configurations#retrieve-a-code-security-configuration-of-an-enterprise) | GET | /enterprises/{enterprise}/code-security/configurations/{configuration_id} | indexed |
| [code-security/update-enterprise-configuration](https://docs.github.com/rest/code-security/configurations#update-a-custom-code-security-configuration-for-an-enterprise) | PATCH | /enterprises/{enterprise}/code-security/configurations/{configuration_id} | indexed |
| [code-security/delete-configuration-for-enterprise](https://docs.github.com/rest/code-security/configurations#delete-a-code-security-configuration-for-an-enterprise) | DELETE | /enterprises/{enterprise}/code-security/configurations/{configuration_id} | indexed |
| [code-security/attach-enterprise-configuration](https://docs.github.com/rest/code-security/configurations#attach-an-enterprise-configuration-to-repositories) | POST | /enterprises/{enterprise}/code-security/configurations/{configuration_id}/attach | indexed |
| [code-security/set-configuration-as-default-for-enterprise](https://docs.github.com/rest/code-security/configurations#set-a-code-security-configuration-as-a-default-for-an-enterprise) | PUT | /enterprises/{enterprise}/code-security/configurations/{configuration_id}/defaults | indexed |
| [code-security/get-repositories-for-enterprise-configuration](https://docs.github.com/rest/code-security/configurations#get-repositories-associated-with-an-enterprise-code-security-configuration) | GET | /enterprises/{enterprise}/code-security/configurations/{configuration_id}/repositories | indexed |
| [code-security/get-configurations-for-org](https://docs.github.com/rest/code-security/configurations#get-code-security-configurations-for-an-organization) | GET | /orgs/{org}/code-security/configurations | indexed |
| [code-security/create-configuration](https://docs.github.com/rest/code-security/configurations#create-a-code-security-configuration) | POST | /orgs/{org}/code-security/configurations | indexed |
| [code-security/get-default-configurations](https://docs.github.com/rest/code-security/configurations#get-default-code-security-configurations) | GET | /orgs/{org}/code-security/configurations/defaults | indexed |
| [code-security/detach-configuration](https://docs.github.com/rest/code-security/configurations#detach-configurations-from-repositories) | DELETE | /orgs/{org}/code-security/configurations/detach | indexed |
| [code-security/get-configuration](https://docs.github.com/rest/code-security/configurations#get-a-code-security-configuration) | GET | /orgs/{org}/code-security/configurations/{configuration_id} | indexed |
| [code-security/update-configuration](https://docs.github.com/rest/code-security/configurations#update-a-code-security-configuration) | PATCH | /orgs/{org}/code-security/configurations/{configuration_id} | indexed |
| [code-security/delete-configuration](https://docs.github.com/rest/code-security/configurations#delete-a-code-security-configuration) | DELETE | /orgs/{org}/code-security/configurations/{configuration_id} | indexed |
| [code-security/attach-configuration](https://docs.github.com/rest/code-security/configurations#attach-a-configuration-to-repositories) | POST | /orgs/{org}/code-security/configurations/{configuration_id}/attach | indexed |
| [code-security/set-configuration-as-default](https://docs.github.com/rest/code-security/configurations#set-a-code-security-configuration-as-a-default-for-an-organization) | PUT | /orgs/{org}/code-security/configurations/{configuration_id}/defaults | indexed |
| [code-security/get-repositories-for-configuration](https://docs.github.com/rest/code-security/configurations#get-repositories-associated-with-a-code-security-configuration) | GET | /orgs/{org}/code-security/configurations/{configuration_id}/repositories | indexed |
| [code-security/get-configuration-for-repository](https://docs.github.com/rest/code-security/configurations#get-the-code-security-configuration-associated-with-a-repository) | GET | /repos/{owner}/{repo}/code-security-configuration | indexed |

## REST codes-of-conduct

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [codes-of-conduct/get-all-codes-of-conduct](https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-all-codes-of-conduct) | GET | /codes_of_conduct | indexed |
| [codes-of-conduct/get-conduct-code](https://docs.github.com/rest/codes-of-conduct/codes-of-conduct#get-a-code-of-conduct) | GET | /codes_of_conduct/{key} | indexed |

## REST codespaces

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [codespaces/list-in-organization](https://docs.github.com/rest/codespaces/organizations#list-codespaces-for-the-organization) | GET | /orgs/{org}/codespaces | indexed |
| [codespaces/set-codespaces-access](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces) | PUT | /orgs/{org}/codespaces/access | deprecated |
| [codespaces/set-codespaces-access-users](https://docs.github.com/rest/codespaces/organizations#add-users-to-codespaces-access-for-an-organization) | POST | /orgs/{org}/codespaces/access/selected_users | deprecated |
| [codespaces/delete-codespaces-access-users](https://docs.github.com/rest/codespaces/organizations#remove-users-from-codespaces-access-for-an-organization) | DELETE | /orgs/{org}/codespaces/access/selected_users | deprecated |
| [codespaces/list-org-secrets](https://docs.github.com/rest/codespaces/organization-secrets#list-organization-secrets) | GET | /orgs/{org}/codespaces/secrets | indexed |
| [codespaces/get-org-public-key](https://docs.github.com/rest/codespaces/organization-secrets#get-an-organization-public-key) | GET | /orgs/{org}/codespaces/secrets/public-key | indexed |
| [codespaces/get-org-secret](https://docs.github.com/rest/codespaces/organization-secrets#get-an-organization-secret) | GET | /orgs/{org}/codespaces/secrets/{secret_name} | indexed |
| [codespaces/create-or-update-org-secret](https://docs.github.com/rest/codespaces/organization-secrets#create-or-update-an-organization-secret) | PUT | /orgs/{org}/codespaces/secrets/{secret_name} | indexed |
| [codespaces/delete-org-secret](https://docs.github.com/rest/codespaces/organization-secrets#delete-an-organization-secret) | DELETE | /orgs/{org}/codespaces/secrets/{secret_name} | indexed |
| [codespaces/list-selected-repos-for-org-secret](https://docs.github.com/rest/codespaces/organization-secrets#list-selected-repositories-for-an-organization-secret) | GET | /orgs/{org}/codespaces/secrets/{secret_name}/repositories | indexed |
| [codespaces/set-selected-repos-for-org-secret](https://docs.github.com/rest/codespaces/organization-secrets#set-selected-repositories-for-an-organization-secret) | PUT | /orgs/{org}/codespaces/secrets/{secret_name}/repositories | indexed |
| [codespaces/add-selected-repo-to-org-secret](https://docs.github.com/rest/codespaces/organization-secrets#add-selected-repository-to-an-organization-secret) | PUT | /orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [codespaces/remove-selected-repo-from-org-secret](https://docs.github.com/rest/codespaces/organization-secrets#remove-selected-repository-from-an-organization-secret) | DELETE | /orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [codespaces/get-codespaces-for-user-in-org](https://docs.github.com/rest/codespaces/organizations#list-codespaces-for-a-user-in-organization) | GET | /orgs/{org}/members/{username}/codespaces | indexed |
| [codespaces/delete-from-organization](https://docs.github.com/rest/codespaces/organizations#delete-a-codespace-from-the-organization) | DELETE | /orgs/{org}/members/{username}/codespaces/{codespace_name} | indexed |
| [codespaces/stop-in-organization](https://docs.github.com/rest/codespaces/organizations#stop-a-codespace-for-an-organization-user) | POST | /orgs/{org}/members/{username}/codespaces/{codespace_name}/stop | indexed |
| [codespaces/list-in-repository-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#list-codespaces-in-a-repository-for-the-authenticated-user) | GET | /repos/{owner}/{repo}/codespaces | indexed |
| [codespaces/create-with-repo-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#create-a-codespace-in-a-repository) | POST | /repos/{owner}/{repo}/codespaces | indexed |
| [codespaces/list-devcontainers-in-repository-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#list-devcontainer-configurations-in-a-repository-for-the-authenticated-user) | GET | /repos/{owner}/{repo}/codespaces/devcontainers | indexed |
| [codespaces/repo-machines-for-authenticated-user](https://docs.github.com/rest/codespaces/machines#list-available-machine-types-for-a-repository) | GET | /repos/{owner}/{repo}/codespaces/machines | indexed |
| [codespaces/pre-flight-with-repo-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#get-default-attributes-for-a-codespace) | GET | /repos/{owner}/{repo}/codespaces/new | indexed |
| [codespaces/check-permissions-for-devcontainer](https://docs.github.com/rest/codespaces/codespaces#check-if-permissions-defined-by-a-devcontainer-have-been-accepted-by-the-authenticated-user) | GET | /repos/{owner}/{repo}/codespaces/permissions_check | indexed |
| [codespaces/list-repo-secrets](https://docs.github.com/rest/codespaces/repository-secrets#list-repository-secrets) | GET | /repos/{owner}/{repo}/codespaces/secrets | indexed |
| [codespaces/get-repo-public-key](https://docs.github.com/rest/codespaces/repository-secrets#get-a-repository-public-key) | GET | /repos/{owner}/{repo}/codespaces/secrets/public-key | indexed |
| [codespaces/get-repo-secret](https://docs.github.com/rest/codespaces/repository-secrets#get-a-repository-secret) | GET | /repos/{owner}/{repo}/codespaces/secrets/{secret_name} | indexed |
| [codespaces/create-or-update-repo-secret](https://docs.github.com/rest/codespaces/repository-secrets#create-or-update-a-repository-secret) | PUT | /repos/{owner}/{repo}/codespaces/secrets/{secret_name} | indexed |
| [codespaces/delete-repo-secret](https://docs.github.com/rest/codespaces/repository-secrets#delete-a-repository-secret) | DELETE | /repos/{owner}/{repo}/codespaces/secrets/{secret_name} | indexed |
| [codespaces/create-with-pr-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#create-a-codespace-from-a-pull-request) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/codespaces | indexed |
| [codespaces/list-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#list-codespaces-for-the-authenticated-user) | GET | /user/codespaces | indexed |
| [codespaces/create-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#create-a-codespace-for-the-authenticated-user) | POST | /user/codespaces | indexed |
| [codespaces/list-secrets-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#list-secrets-for-the-authenticated-user) | GET | /user/codespaces/secrets | indexed |
| [codespaces/get-public-key-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#get-public-key-for-the-authenticated-user) | GET | /user/codespaces/secrets/public-key | indexed |
| [codespaces/get-secret-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#get-a-secret-for-the-authenticated-user) | GET | /user/codespaces/secrets/{secret_name} | indexed |
| [codespaces/create-or-update-secret-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#create-or-update-a-secret-for-the-authenticated-user) | PUT | /user/codespaces/secrets/{secret_name} | indexed |
| [codespaces/delete-secret-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#delete-a-secret-for-the-authenticated-user) | DELETE | /user/codespaces/secrets/{secret_name} | indexed |
| [codespaces/list-repositories-for-secret-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret) | GET | /user/codespaces/secrets/{secret_name}/repositories | indexed |
| [codespaces/set-repositories-for-secret-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#set-selected-repositories-for-a-user-secret) | PUT | /user/codespaces/secrets/{secret_name}/repositories | indexed |
| [codespaces/add-repository-for-secret-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#add-a-selected-repository-to-a-user-secret) | PUT | /user/codespaces/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [codespaces/remove-repository-for-secret-for-authenticated-user](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret) | DELETE | /user/codespaces/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [codespaces/get-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#get-a-codespace-for-the-authenticated-user) | GET | /user/codespaces/{codespace_name} | indexed |
| [codespaces/update-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#update-a-codespace-for-the-authenticated-user) | PATCH | /user/codespaces/{codespace_name} | indexed |
| [codespaces/delete-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#delete-a-codespace-for-the-authenticated-user) | DELETE | /user/codespaces/{codespace_name} | indexed |
| [codespaces/export-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#export-a-codespace-for-the-authenticated-user) | POST | /user/codespaces/{codespace_name}/exports | indexed |
| [codespaces/get-export-details-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#get-details-about-a-codespace-export) | GET | /user/codespaces/{codespace_name}/exports/{export_id} | indexed |
| [codespaces/codespace-machines-for-authenticated-user](https://docs.github.com/rest/codespaces/machines#list-machine-types-for-a-codespace) | GET | /user/codespaces/{codespace_name}/machines | indexed |
| [codespaces/publish-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#create-a-repository-from-an-unpublished-codespace) | POST | /user/codespaces/{codespace_name}/publish | indexed |
| [codespaces/start-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#start-a-codespace-for-the-authenticated-user) | POST | /user/codespaces/{codespace_name}/start | indexed |
| [codespaces/stop-for-authenticated-user](https://docs.github.com/rest/codespaces/codespaces#stop-a-codespace-for-the-authenticated-user) | POST | /user/codespaces/{codespace_name}/stop | indexed |

## REST copilot

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [copilot/copilot-enterprise-one-day-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-enterprise-usage-metrics-for-a-specific-day) | GET | /enterprises/{enterprise}/copilot/metrics/reports/enterprise-1-day | indexed |
| [copilot/copilot-enterprise-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-enterprise-usage-metrics) | GET | /enterprises/{enterprise}/copilot/metrics/reports/enterprise-28-day/latest | indexed |
| [copilot/copilot-enterprise-repos-one-day-report](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-enterprise-repository-report-for-a-specific-day) | GET | /enterprises/{enterprise}/copilot/metrics/reports/repos-1-day | indexed |
| [copilot/copilot-enterprise-user-teams-one-day-report](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-enterprise-user-teams-report-for-a-specific-day) | GET | /enterprises/{enterprise}/copilot/metrics/reports/user-teams-1-day | indexed |
| [copilot/copilot-users-one-day-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-users-usage-metrics-for-a-specific-day) | GET | /enterprises/{enterprise}/copilot/metrics/reports/users-1-day | indexed |
| [copilot/copilot-users-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-users-usage-metrics) | GET | /enterprises/{enterprise}/copilot/metrics/reports/users-28-day/latest | indexed |
| [copilot/get-enterprise-code-review-policy](https://docs.github.com/rest/copilot/copilot-code-review#get-the-copilot-code-review-policy-for-an-enterprise) | GET | /enterprises/{enterprise}/copilot/policies/code-review | indexed |
| [copilot/set-enterprise-code-review-policy](https://docs.github.com/rest/copilot/copilot-code-review#set-the-copilot-code-review-policy-for-an-enterprise) | PUT | /enterprises/{enterprise}/copilot/policies/code-review | indexed |
| [copilot/set-enterprise-coding-agent-policy](https://docs.github.com/rest/copilot/copilot-coding-agent-management#set-the-coding-agent-policy-for-an-enterprise) | PUT | /enterprises/{enterprise}/copilot/policies/coding_agent | indexed |
| [copilot/add-organizations-to-enterprise-coding-agent-policy](https://docs.github.com/rest/copilot/copilot-coding-agent-management#add-organizations-to-the-enterprise-coding-agent-policy) | POST | /enterprises/{enterprise}/copilot/policies/coding_agent/organizations | indexed |
| [copilot/remove-organizations-from-enterprise-coding-agent-policy](https://docs.github.com/rest/copilot/copilot-coding-agent-management#remove-organizations-from-the-enterprise-coding-agent-policy) | DELETE | /enterprises/{enterprise}/copilot/policies/coding_agent/organizations | indexed |
| [copilot/get-copilot-organization-details](https://docs.github.com/rest/copilot/copilot-user-management#get-copilot-seat-information-and-settings-for-an-organization) | GET | /orgs/{org}/copilot/billing | indexed |
| [copilot/list-copilot-seats](https://docs.github.com/rest/copilot/copilot-user-management#list-all-copilot-seat-assignments-for-an-organization) | GET | /orgs/{org}/copilot/billing/seats | indexed |
| [copilot/add-copilot-seats-for-teams](https://docs.github.com/rest/copilot/copilot-user-management#add-teams-to-the-copilot-subscription-for-an-organization) | POST | /orgs/{org}/copilot/billing/selected_teams | indexed |
| [copilot/cancel-copilot-seat-assignment-for-teams](https://docs.github.com/rest/copilot/copilot-user-management#remove-teams-from-the-copilot-subscription-for-an-organization) | DELETE | /orgs/{org}/copilot/billing/selected_teams | indexed |
| [copilot/add-copilot-seats-for-users](https://docs.github.com/rest/copilot/copilot-user-management#add-users-to-the-copilot-subscription-for-an-organization) | POST | /orgs/{org}/copilot/billing/selected_users | indexed |
| [copilot/cancel-copilot-seat-assignment-for-users](https://docs.github.com/rest/copilot/copilot-user-management#remove-users-from-the-copilot-subscription-for-an-organization) | DELETE | /orgs/{org}/copilot/billing/selected_users | indexed |
| [copilot/get-organization-code-review-runner](https://docs.github.com/rest/copilot/copilot-code-review#get-the-copilot-code-review-runner-configuration-for-an-organization) | GET | /orgs/{org}/copilot/code-review/runner | indexed |
| [copilot/set-organization-code-review-runner](https://docs.github.com/rest/copilot/copilot-code-review#set-the-copilot-code-review-runner-configuration-for-an-organization) | PUT | /orgs/{org}/copilot/code-review/runner | indexed |
| [copilot/get-organization-code-review-settings](https://docs.github.com/rest/copilot/copilot-code-review#get-copilot-code-review-settings-for-an-organization) | GET | /orgs/{org}/copilot/code-review/settings | indexed |
| [copilot/update-organization-code-review-settings](https://docs.github.com/rest/copilot/copilot-code-review#update-copilot-code-review-settings-for-an-organization) | PATCH | /orgs/{org}/copilot/code-review/settings | indexed |
| [copilot/get-copilot-coding-agent-permissions-organization](https://docs.github.com/rest/copilot/copilot-coding-agent-management#get-copilot-cloud-agent-permissions-for-an-organization) | GET | /orgs/{org}/copilot/coding-agent/permissions | indexed |
| [copilot/set-copilot-coding-agent-permissions-organization](https://docs.github.com/rest/copilot/copilot-coding-agent-management#set-copilot-cloud-agent-permissions-for-an-organization) | PUT | /orgs/{org}/copilot/coding-agent/permissions | indexed |
| [copilot/list-copilot-coding-agent-selected-repositories-for-organization](https://docs.github.com/rest/copilot/copilot-coding-agent-management#list-repositories-enabled-for-copilot-cloud-agent-in-an-organization) | GET | /orgs/{org}/copilot/coding-agent/permissions/repositories | indexed |
| [copilot/set-copilot-coding-agent-selected-repositories-for-organization](https://docs.github.com/rest/copilot/copilot-coding-agent-management#set-selected-repositories-for-copilot-cloud-agent-in-an-organization) | PUT | /orgs/{org}/copilot/coding-agent/permissions/repositories | indexed |
| [copilot/enable-copilot-coding-agent-for-repository-in-organization](https://docs.github.com/rest/copilot/copilot-coding-agent-management#enable-a-repository-for-copilot-cloud-agent-in-an-organization) | PUT | /orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id} | indexed |
| [copilot/disable-copilot-coding-agent-for-repository-in-organization](https://docs.github.com/rest/copilot/copilot-coding-agent-management#disable-a-repository-for-copilot-cloud-agent-in-an-organization) | DELETE | /orgs/{org}/copilot/coding-agent/permissions/repositories/{repository_id} | indexed |
| [copilot/copilot-content-exclusion-for-organization](https://docs.github.com/rest/copilot/copilot-content-exclusion-management#get-copilot-content-exclusion-rules-for-an-organization) | GET | /orgs/{org}/copilot/content_exclusion | indexed |
| [copilot/set-copilot-content-exclusion-for-organization](https://docs.github.com/rest/copilot/copilot-content-exclusion-management#set-copilot-content-exclusion-rules-for-an-organization) | PUT | /orgs/{org}/copilot/content_exclusion | indexed |
| [copilot/copilot-organization-one-day-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-organization-usage-metrics-for-a-specific-day) | GET | /orgs/{org}/copilot/metrics/reports/organization-1-day | indexed |
| [copilot/copilot-organization-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-organization-usage-metrics) | GET | /orgs/{org}/copilot/metrics/reports/organization-28-day/latest | indexed |
| [copilot/copilot-organization-repos-one-day-report](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-organization-repository-report-for-a-specific-day) | GET | /orgs/{org}/copilot/metrics/reports/repos-1-day | indexed |
| [copilot/copilot-organization-user-teams-one-day-report](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-organization-user-teams-report-for-a-specific-day) | GET | /orgs/{org}/copilot/metrics/reports/user-teams-1-day | indexed |
| [copilot/copilot-organization-users-one-day-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-organization-users-usage-metrics-for-a-specific-day) | GET | /orgs/{org}/copilot/metrics/reports/users-1-day | indexed |
| [copilot/copilot-organization-users-usage-metrics](https://docs.github.com/rest/copilot/copilot-usage-metrics#get-copilot-organization-users-usage-metrics) | GET | /orgs/{org}/copilot/metrics/reports/users-28-day/latest | indexed |
| [copilot/get-organization-code-review-policy](https://docs.github.com/rest/copilot/copilot-code-review#get-the-copilot-code-review-policy-for-an-organization) | GET | /orgs/{org}/copilot/policies/code-review | indexed |
| [copilot/set-organization-code-review-policy](https://docs.github.com/rest/copilot/copilot-code-review#set-the-copilot-code-review-policy-for-an-organization) | PUT | /orgs/{org}/copilot/policies/code-review | indexed |
| [copilot/get-copilot-seat-details-for-user](https://docs.github.com/rest/copilot/copilot-user-management#get-copilot-seat-assignment-details-for-a-user) | GET | /orgs/{org}/members/{username}/copilot | indexed |
| [copilot/get-copilot-team-customizations](https://docs.github.com/rest/copilot/copilot-team-customizations#get-copilot-customizations-for-a-team) | GET | /orgs/{org}/teams/{team_slug}/copilot/customizations | indexed |
| [copilot/set-copilot-team-customizations](https://docs.github.com/rest/copilot/copilot-team-customizations#set-copilot-customizations-for-a-team) | PUT | /orgs/{org}/teams/{team_slug}/copilot/customizations | indexed |
| [copilot/delete-copilot-team-customizations](https://docs.github.com/rest/copilot/copilot-team-customizations#delete-copilot-customizations-for-a-team) | DELETE | /orgs/{org}/teams/{team_slug}/copilot/customizations | indexed |
| [copilot/get-copilot-cloud-agent-configuration](https://docs.github.com/rest/copilot/copilot-cloud-agent-management#get-copilot-cloud-agent-configuration-for-a-repository) | GET | /repos/{owner}/{repo}/copilot/cloud-agent/configuration | indexed |
| [copilot/get-repository-code-review-settings](https://docs.github.com/rest/copilot/copilot-code-review#get-copilot-code-review-settings-for-a-repository) | GET | /repos/{owner}/{repo}/copilot/code-review/settings | indexed |
| [copilot/update-repository-code-review-settings](https://docs.github.com/rest/copilot/copilot-code-review#update-copilot-code-review-settings-for-a-repository) | PATCH | /repos/{owner}/{repo}/copilot/code-review/settings | indexed |

## REST copilot-spaces

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [copilot-spaces/list-for-org](https://docs.github.com/rest/copilot-spaces/copilot-spaces#list-organization-copilot-spaces) | GET | /orgs/{org}/copilot-spaces | indexed |
| [copilot-spaces/create-for-org](https://docs.github.com/rest/copilot-spaces/copilot-spaces#create-an-organization-copilot-space) | POST | /orgs/{org}/copilot-spaces | indexed |
| [copilot-spaces/get-for-org](https://docs.github.com/rest/copilot-spaces/copilot-spaces#get-an-organization-copilot-space) | GET | /orgs/{org}/copilot-spaces/{space_number} | indexed |
| [copilot-spaces/update-for-org](https://docs.github.com/rest/copilot-spaces/copilot-spaces#set-an-organization-copilot-space) | PUT | /orgs/{org}/copilot-spaces/{space_number} | indexed |
| [copilot-spaces/delete-for-org](https://docs.github.com/rest/copilot-spaces/copilot-spaces#delete-an-organization-copilot-space) | DELETE | /orgs/{org}/copilot-spaces/{space_number} | indexed |
| [copilot-spaces/list-collaborators-for-org](https://docs.github.com/rest/copilot-spaces/collaborators#list-collaborators-for-an-organization-copilot-space) | GET | /orgs/{org}/copilot-spaces/{space_number}/collaborators | indexed |
| [copilot-spaces/add-collaborator-for-org](https://docs.github.com/rest/copilot-spaces/collaborators#add-a-collaborator-to-an-organization-copilot-space) | POST | /orgs/{org}/copilot-spaces/{space_number}/collaborators | indexed |
| [copilot-spaces/update-collaborator-for-org](https://docs.github.com/rest/copilot-spaces/collaborators#set-a-collaborator-role-for-an-organization-copilot-space) | PUT | /orgs/{org}/copilot-spaces/{space_number}/collaborators/{actor_type}/{actor_identifier} | indexed |
| [copilot-spaces/remove-collaborator-for-org](https://docs.github.com/rest/copilot-spaces/collaborators#remove-a-collaborator-from-an-organization-copilot-space) | DELETE | /orgs/{org}/copilot-spaces/{space_number}/collaborators/{actor_type}/{actor_identifier} | indexed |
| [copilot-spaces/list-resources-for-org](https://docs.github.com/rest/copilot-spaces/resources#list-resources-for-an-organization-copilot-space) | GET | /orgs/{org}/copilot-spaces/{space_number}/resources | indexed |
| [copilot-spaces/create-resource-for-org](https://docs.github.com/rest/copilot-spaces/resources#create-a-resource-for-an-organization-copilot-space) | POST | /orgs/{org}/copilot-spaces/{space_number}/resources | indexed |
| [copilot-spaces/get-resource-for-org](https://docs.github.com/rest/copilot-spaces/resources#get-a-resource-for-an-organization-copilot-space) | GET | /orgs/{org}/copilot-spaces/{space_number}/resources/{space_resource_id} | indexed |
| [copilot-spaces/update-resource-for-org](https://docs.github.com/rest/copilot-spaces/resources#set-a-resource-for-an-organization-copilot-space) | PUT | /orgs/{org}/copilot-spaces/{space_number}/resources/{space_resource_id} | indexed |
| [copilot-spaces/delete-resource-for-org](https://docs.github.com/rest/copilot-spaces/resources#delete-a-resource-from-an-organization-copilot-space) | DELETE | /orgs/{org}/copilot-spaces/{space_number}/resources/{space_resource_id} | indexed |
| [copilot-spaces/list-for-user](https://docs.github.com/rest/copilot-spaces/copilot-spaces#list-copilot-spaces-for-a-user) | GET | /users/{username}/copilot-spaces | indexed |
| [copilot-spaces/create-for-user](https://docs.github.com/rest/copilot-spaces/copilot-spaces#create-a-copilot-space-for-a-user) | POST | /users/{username}/copilot-spaces | indexed |
| [copilot-spaces/get-for-user](https://docs.github.com/rest/copilot-spaces/copilot-spaces#get-a-copilot-space-for-a-user) | GET | /users/{username}/copilot-spaces/{space_number} | indexed |
| [copilot-spaces/update-for-user](https://docs.github.com/rest/copilot-spaces/copilot-spaces#set-a-copilot-space-for-a-user) | PUT | /users/{username}/copilot-spaces/{space_number} | indexed |
| [copilot-spaces/delete-for-user](https://docs.github.com/rest/copilot-spaces/copilot-spaces#delete-a-copilot-space-for-a-user) | DELETE | /users/{username}/copilot-spaces/{space_number} | indexed |
| [copilot-spaces/list-collaborators-for-user](https://docs.github.com/rest/copilot-spaces/collaborators#list-collaborators-for-a-copilot-space-for-a-user) | GET | /users/{username}/copilot-spaces/{space_number}/collaborators | indexed |
| [copilot-spaces/add-collaborator-for-user](https://docs.github.com/rest/copilot-spaces/collaborators#add-a-collaborator-to-a-copilot-space-for-a-user) | POST | /users/{username}/copilot-spaces/{space_number}/collaborators | indexed |
| [copilot-spaces/update-collaborator-for-user](https://docs.github.com/rest/copilot-spaces/collaborators#set-a-collaborator-role-for-a-copilot-space-for-a-user) | PUT | /users/{username}/copilot-spaces/{space_number}/collaborators/{actor_type}/{actor_identifier} | indexed |
| [copilot-spaces/remove-collaborator-for-user](https://docs.github.com/rest/copilot-spaces/collaborators#remove-a-collaborator-from-a-copilot-space-for-a-user) | DELETE | /users/{username}/copilot-spaces/{space_number}/collaborators/{actor_type}/{actor_identifier} | indexed |
| [copilot-spaces/list-resources-for-user](https://docs.github.com/rest/copilot-spaces/resources#list-resources-for-a-copilot-space-for-a-user) | GET | /users/{username}/copilot-spaces/{space_number}/resources | indexed |
| [copilot-spaces/create-resource-for-user](https://docs.github.com/rest/copilot-spaces/resources#create-a-resource-for-a-copilot-space-for-a-user) | POST | /users/{username}/copilot-spaces/{space_number}/resources | indexed |
| [copilot-spaces/get-resource-for-user](https://docs.github.com/rest/copilot-spaces/resources#get-a-resource-for-a-copilot-space-for-a-user) | GET | /users/{username}/copilot-spaces/{space_number}/resources/{space_resource_id} | indexed |
| [copilot-spaces/update-resource-for-user](https://docs.github.com/rest/copilot-spaces/resources#set-a-resource-for-a-copilot-space-for-a-user) | PUT | /users/{username}/copilot-spaces/{space_number}/resources/{space_resource_id} | indexed |
| [copilot-spaces/delete-resource-for-user](https://docs.github.com/rest/copilot-spaces/resources#delete-a-resource-from-a-copilot-space-for-a-user) | DELETE | /users/{username}/copilot-spaces/{space_number}/resources/{space_resource_id} | indexed |

## REST credentials

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [credentials/revoke](https://docs.github.com/rest/credentials/revoke#revoke-a-list-of-credentials) | POST | /credentials/revoke | indexed |

## REST dependabot

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [dependabot/list-alerts-for-enterprise](https://docs.github.com/rest/dependabot/alerts#list-dependabot-alerts-for-an-enterprise) | GET | /enterprises/{enterprise}/dependabot/alerts | indexed |
| [dependabot/repository-access-for-enterprise](https://docs.github.com/rest/dependabot/repository-access#lists-the-repositories-dependabot-can-access-in-an-enterprise) | GET | /enterprises/{enterprise}/dependabot/repository-access | indexed |
| [dependabot/update-repository-access-for-enterprise](https://docs.github.com/rest/dependabot/repository-access#updates-dependabots-repository-access-list-for-an-enterprise) | PATCH | /enterprises/{enterprise}/dependabot/repository-access | indexed |
| [dependabot/set-repository-access-default-level-for-enterprise](https://docs.github.com/rest/dependabot/repository-access#set-the-default-repository-access-level-for-dependabot-in-an-enterprise) | PUT | /enterprises/{enterprise}/dependabot/repository-access/default-level | indexed |
| [dependabot/list-alerts-for-org](https://docs.github.com/rest/dependabot/alerts#list-dependabot-alerts-for-an-organization) | GET | /orgs/{org}/dependabot/alerts | indexed |
| [dependabot/repository-access-for-org](https://docs.github.com/rest/dependabot/repository-access#lists-the-repositories-dependabot-can-access-in-an-organization) | GET | /orgs/{org}/dependabot/repository-access | indexed |
| [dependabot/update-repository-access-for-org](https://docs.github.com/rest/dependabot/repository-access#updates-dependabots-repository-access-list-for-an-organization) | PATCH | /orgs/{org}/dependabot/repository-access | indexed |
| [dependabot/set-repository-access-default-level](https://docs.github.com/rest/dependabot/repository-access#set-the-default-repository-access-level-for-dependabot) | PUT | /orgs/{org}/dependabot/repository-access/default-level | indexed |
| [dependabot/list-org-secrets](https://docs.github.com/rest/dependabot/secrets#list-organization-secrets) | GET | /orgs/{org}/dependabot/secrets | indexed |
| [dependabot/get-org-public-key](https://docs.github.com/rest/dependabot/secrets#get-an-organization-public-key) | GET | /orgs/{org}/dependabot/secrets/public-key | indexed |
| [dependabot/get-org-secret](https://docs.github.com/rest/dependabot/secrets#get-an-organization-secret) | GET | /orgs/{org}/dependabot/secrets/{secret_name} | indexed |
| [dependabot/create-or-update-org-secret](https://docs.github.com/rest/dependabot/secrets#create-or-update-an-organization-secret) | PUT | /orgs/{org}/dependabot/secrets/{secret_name} | indexed |
| [dependabot/delete-org-secret](https://docs.github.com/rest/dependabot/secrets#delete-an-organization-secret) | DELETE | /orgs/{org}/dependabot/secrets/{secret_name} | indexed |
| [dependabot/list-selected-repos-for-org-secret](https://docs.github.com/rest/dependabot/secrets#list-selected-repositories-for-an-organization-secret) | GET | /orgs/{org}/dependabot/secrets/{secret_name}/repositories | indexed |
| [dependabot/set-selected-repos-for-org-secret](https://docs.github.com/rest/dependabot/secrets#set-selected-repositories-for-an-organization-secret) | PUT | /orgs/{org}/dependabot/secrets/{secret_name}/repositories | indexed |
| [dependabot/add-selected-repo-to-org-secret](https://docs.github.com/rest/dependabot/secrets#add-selected-repository-to-an-organization-secret) | PUT | /orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [dependabot/remove-selected-repo-from-org-secret](https://docs.github.com/rest/dependabot/secrets#remove-selected-repository-from-an-organization-secret) | DELETE | /orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | indexed |
| [dependabot/list-alerts-for-repo](https://docs.github.com/rest/dependabot/alerts#list-dependabot-alerts-for-a-repository) | GET | /repos/{owner}/{repo}/dependabot/alerts | indexed |
| [dependabot/get-alert](https://docs.github.com/rest/dependabot/alerts#get-a-dependabot-alert) | GET | /repos/{owner}/{repo}/dependabot/alerts/{alert_number} | indexed |
| [dependabot/update-alert](https://docs.github.com/rest/dependabot/alerts#update-a-dependabot-alert) | PATCH | /repos/{owner}/{repo}/dependabot/alerts/{alert_number} | indexed |
| [dependabot/get-repository-runner-settings](https://docs.github.com/rest/dependabot/runner-settings#get-repository-dependabot-runner-settings) | GET | /repos/{owner}/{repo}/dependabot/runner-settings | indexed |
| [dependabot/set-repository-runner-settings](https://docs.github.com/rest/dependabot/runner-settings#set-repository-dependabot-runner-settings) | PUT | /repos/{owner}/{repo}/dependabot/runner-settings | indexed |
| [dependabot/list-repo-secrets](https://docs.github.com/rest/dependabot/secrets#list-repository-secrets) | GET | /repos/{owner}/{repo}/dependabot/secrets | indexed |
| [dependabot/get-repo-public-key](https://docs.github.com/rest/dependabot/secrets#get-a-repository-public-key) | GET | /repos/{owner}/{repo}/dependabot/secrets/public-key | indexed |
| [dependabot/get-repo-secret](https://docs.github.com/rest/dependabot/secrets#get-a-repository-secret) | GET | /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | indexed |
| [dependabot/create-or-update-repo-secret](https://docs.github.com/rest/dependabot/secrets#create-or-update-a-repository-secret) | PUT | /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | indexed |
| [dependabot/delete-repo-secret](https://docs.github.com/rest/dependabot/secrets#delete-a-repository-secret) | DELETE | /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | indexed |

## REST dependency-graph

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [dependency-graph/diff-range](https://docs.github.com/rest/dependency-graph/dependency-review#get-a-diff-of-the-dependencies-between-commits) | GET | /repos/{owner}/{repo}/dependency-graph/compare/{basehead} | indexed |
| [dependency-graph/export-sbom](https://docs.github.com/rest/dependency-graph/sboms#export-a-software-bill-of-materials-sbom-for-a-repository) | GET | /repos/{owner}/{repo}/dependency-graph/sbom | retired |
| [dependency-graph/fetch-sbom-report](https://docs.github.com/rest/dependency-graph/sboms#fetch-a-software-bill-of-materials-sbom-for-a-repository) | GET | /repos/{owner}/{repo}/dependency-graph/sbom/fetch-report/{sbom_uuid} | indexed |
| [dependency-graph/generate-sbom-report](https://docs.github.com/rest/dependency-graph/sboms#request-generation-of-a-software-bill-of-materials-sbom-for-a-repository) | GET | /repos/{owner}/{repo}/dependency-graph/sbom/generate-report | indexed |
| [dependency-graph/create-repository-snapshot](https://docs.github.com/rest/dependency-graph/dependency-submission#create-a-snapshot-of-dependencies-for-a-repository) | POST | /repos/{owner}/{repo}/dependency-graph/snapshots | indexed |

## REST emojis

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [emojis/get](https://docs.github.com/rest/emojis/emojis#get-emojis) | GET | /emojis | indexed |

## REST gists

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [gists/list](https://docs.github.com/rest/gists/gists#list-gists-for-the-authenticated-user) | GET | /gists | indexed |
| [gists/create](https://docs.github.com/rest/gists/gists#create-a-gist) | POST | /gists | indexed |
| [gists/list-public](https://docs.github.com/rest/gists/gists#list-public-gists) | GET | /gists/public | indexed |
| [gists/list-starred](https://docs.github.com/rest/gists/gists#list-starred-gists) | GET | /gists/starred | indexed |
| [gists/get](https://docs.github.com/rest/gists/gists#get-a-gist) | GET | /gists/{gist_id} | indexed |
| [gists/update](https://docs.github.com/rest/gists/gists#update-a-gist) | PATCH | /gists/{gist_id} | indexed |
| [gists/delete](https://docs.github.com/rest/gists/gists#delete-a-gist) | DELETE | /gists/{gist_id} | indexed |
| [gists/list-comments](https://docs.github.com/rest/gists/comments#list-gist-comments) | GET | /gists/{gist_id}/comments | indexed |
| [gists/create-comment](https://docs.github.com/rest/gists/comments#create-a-gist-comment) | POST | /gists/{gist_id}/comments | indexed |
| [gists/get-comment](https://docs.github.com/rest/gists/comments#get-a-gist-comment) | GET | /gists/{gist_id}/comments/{comment_id} | indexed |
| [gists/update-comment](https://docs.github.com/rest/gists/comments#update-a-gist-comment) | PATCH | /gists/{gist_id}/comments/{comment_id} | indexed |
| [gists/delete-comment](https://docs.github.com/rest/gists/comments#delete-a-gist-comment) | DELETE | /gists/{gist_id}/comments/{comment_id} | indexed |
| [gists/list-commits](https://docs.github.com/rest/gists/gists#list-gist-commits) | GET | /gists/{gist_id}/commits | indexed |
| [gists/list-forks](https://docs.github.com/rest/gists/gists#list-gist-forks) | GET | /gists/{gist_id}/forks | indexed |
| [gists/fork](https://docs.github.com/rest/gists/gists#fork-a-gist) | POST | /gists/{gist_id}/forks | indexed |
| [gists/check-is-starred](https://docs.github.com/rest/gists/gists#check-if-a-gist-is-starred) | GET | /gists/{gist_id}/star | indexed |
| [gists/star](https://docs.github.com/rest/gists/gists#star-a-gist) | PUT | /gists/{gist_id}/star | indexed |
| [gists/unstar](https://docs.github.com/rest/gists/gists#unstar-a-gist) | DELETE | /gists/{gist_id}/star | indexed |
| [gists/get-revision](https://docs.github.com/rest/gists/gists#get-a-gist-revision) | GET | /gists/{gist_id}/{sha} | indexed |
| [gists/list-for-user](https://docs.github.com/rest/gists/gists#list-gists-for-a-user) | GET | /users/{username}/gists | indexed |

## REST git

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [git/create-blob](https://docs.github.com/rest/git/blobs#create-a-blob) | POST | /repos/{owner}/{repo}/git/blobs | indexed |
| [git/get-blob](https://docs.github.com/rest/git/blobs#get-a-blob) | GET | /repos/{owner}/{repo}/git/blobs/{file_sha} | indexed |
| [git/create-commit](https://docs.github.com/rest/git/commits#create-a-commit) | POST | /repos/{owner}/{repo}/git/commits | indexed |
| [git/get-commit](https://docs.github.com/rest/git/commits#get-a-commit-object) | GET | /repos/{owner}/{repo}/git/commits/{commit_sha} | indexed |
| [git/list-matching-refs](https://docs.github.com/rest/git/refs#list-matching-references) | GET | /repos/{owner}/{repo}/git/matching-refs/{ref} | indexed |
| [git/get-ref](https://docs.github.com/rest/git/refs#get-a-reference) | GET | /repos/{owner}/{repo}/git/ref/{ref} | indexed |
| [git/create-ref](https://docs.github.com/rest/git/refs#create-a-reference) | POST | /repos/{owner}/{repo}/git/refs | indexed |
| [git/update-ref](https://docs.github.com/rest/git/refs#update-a-reference) | PATCH | /repos/{owner}/{repo}/git/refs/{ref} | indexed |
| [git/delete-ref](https://docs.github.com/rest/git/refs#delete-a-reference) | DELETE | /repos/{owner}/{repo}/git/refs/{ref} | indexed |
| [git/create-tag](https://docs.github.com/rest/git/tags#create-a-tag-object) | POST | /repos/{owner}/{repo}/git/tags | indexed |
| [git/get-tag](https://docs.github.com/rest/git/tags#get-a-tag) | GET | /repos/{owner}/{repo}/git/tags/{tag_sha} | indexed |
| [git/create-tree](https://docs.github.com/rest/git/trees#create-a-tree) | POST | /repos/{owner}/{repo}/git/trees | indexed |
| [git/get-tree](https://docs.github.com/rest/git/trees#get-a-tree) | GET | /repos/{owner}/{repo}/git/trees/{tree_sha} | indexed |

## REST gitignore

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [gitignore/get-all-templates](https://docs.github.com/rest/gitignore/gitignore#get-all-gitignore-templates) | GET | /gitignore/templates | indexed |
| [gitignore/get-template](https://docs.github.com/rest/gitignore/gitignore#get-a-gitignore-template) | GET | /gitignore/templates/{name} | indexed |

## REST hosted-compute

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [hosted-compute/list-network-configurations-for-org](https://docs.github.com/rest/orgs/network-configurations#list-hosted-compute-network-configurations-for-an-organization) | GET | /orgs/{org}/settings/network-configurations | indexed |
| [hosted-compute/create-network-configuration-for-org](https://docs.github.com/rest/orgs/network-configurations#create-a-hosted-compute-network-configuration-for-an-organization) | POST | /orgs/{org}/settings/network-configurations | indexed |
| [hosted-compute/get-network-configuration-for-org](https://docs.github.com/rest/orgs/network-configurations#get-a-hosted-compute-network-configuration-for-an-organization) | GET | /orgs/{org}/settings/network-configurations/{network_configuration_id} | indexed |
| [hosted-compute/update-network-configuration-for-org](https://docs.github.com/rest/orgs/network-configurations#update-a-hosted-compute-network-configuration-for-an-organization) | PATCH | /orgs/{org}/settings/network-configurations/{network_configuration_id} | indexed |
| [hosted-compute/delete-network-configuration-from-org](https://docs.github.com/rest/orgs/network-configurations#delete-a-hosted-compute-network-configuration-from-an-organization) | DELETE | /orgs/{org}/settings/network-configurations/{network_configuration_id} | indexed |
| [hosted-compute/get-network-settings-for-org](https://docs.github.com/rest/orgs/network-configurations#get-a-hosted-compute-network-settings-resource-for-an-organization) | GET | /orgs/{org}/settings/network-settings/{network_settings_id} | indexed |

## REST interactions

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [interactions/get-restrictions-for-org](https://docs.github.com/rest/interactions/orgs#get-interaction-restrictions-for-an-organization) | GET | /orgs/{org}/interaction-limits | indexed |
| [interactions/set-restrictions-for-org](https://docs.github.com/rest/interactions/orgs#set-interaction-restrictions-for-an-organization) | PUT | /orgs/{org}/interaction-limits | indexed |
| [interactions/remove-restrictions-for-org](https://docs.github.com/rest/interactions/orgs#remove-interaction-restrictions-for-an-organization) | DELETE | /orgs/{org}/interaction-limits | indexed |
| [interactions/get-pull-request-creation-cap-for-org](https://docs.github.com/rest/interactions/orgs#get-pull-request-creation-cap-for-an-org) | GET | /orgs/{org}/interaction-limits/pulls/creation-cap | indexed |
| [interactions/update-pull-request-creation-cap-for-org](https://docs.github.com/rest/interactions/orgs#update-pull-request-creation-cap-for-an-org) | PATCH | /orgs/{org}/interaction-limits/pulls/creation-cap | indexed |
| [interactions/get-restrictions-for-repo](https://docs.github.com/rest/interactions/repos#get-interaction-restrictions-for-a-repository) | GET | /repos/{owner}/{repo}/interaction-limits | indexed |
| [interactions/set-restrictions-for-repo](https://docs.github.com/rest/interactions/repos#set-interaction-restrictions-for-a-repository) | PUT | /repos/{owner}/{repo}/interaction-limits | indexed |
| [interactions/remove-restrictions-for-repo](https://docs.github.com/rest/interactions/repos#remove-interaction-restrictions-for-a-repository) | DELETE | /repos/{owner}/{repo}/interaction-limits | indexed |
| [interactions/get-pull-request-bypass-list-for-repo](https://docs.github.com/rest/interactions/repos#get-pull-request-creation-cap-bypass-list-for-a-repository) | GET | /repos/{owner}/{repo}/interaction-limits/pulls/bypass-list | indexed |
| [interactions/set-pull-request-bypass-list-for-repo](https://docs.github.com/rest/interactions/repos#add-users-to-the-pull-request-creation-cap-bypass-list-for-a-repository) | PUT | /repos/{owner}/{repo}/interaction-limits/pulls/bypass-list | indexed |
| [interactions/remove-pull-request-bypass-list-for-repo](https://docs.github.com/rest/interactions/repos#remove-users-from-the-pull-request-creation-cap-bypass-list-for-a-repository) | DELETE | /repos/{owner}/{repo}/interaction-limits/pulls/bypass-list | indexed |
| [interactions/get-pull-request-creation-cap-for-repo](https://docs.github.com/rest/interactions/repos#get-pull-request-creation-cap-for-a-repository) | GET | /repos/{owner}/{repo}/interaction-limits/pulls/creation-cap | indexed |
| [interactions/update-pull-request-creation-cap-for-repo](https://docs.github.com/rest/interactions/repos#update-pull-request-creation-cap-for-a-repository) | PATCH | /repos/{owner}/{repo}/interaction-limits/pulls/creation-cap | indexed |
| [interactions/get-restrictions-for-authenticated-user](https://docs.github.com/rest/interactions/user#get-interaction-restrictions-for-your-public-repositories) | GET | /user/interaction-limits | indexed |
| [interactions/set-restrictions-for-authenticated-user](https://docs.github.com/rest/interactions/user#set-interaction-restrictions-for-your-public-repositories) | PUT | /user/interaction-limits | indexed |
| [interactions/remove-restrictions-for-authenticated-user](https://docs.github.com/rest/interactions/user#remove-interaction-restrictions-from-your-public-repositories) | DELETE | /user/interaction-limits | indexed |

## REST issues

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [issues/list](https://docs.github.com/rest/issues/issues#list-issues-assigned-to-the-authenticated-user) | GET | /issues | indexed |
| [issues/list-for-org](https://docs.github.com/rest/issues/issues#list-organization-issues-assigned-to-the-authenticated-user) | GET | /orgs/{org}/issues | indexed |
| [issues/list-assignees](https://docs.github.com/rest/issues/assignees#list-assignees) | GET | /repos/{owner}/{repo}/assignees | indexed |
| [issues/check-user-can-be-assigned](https://docs.github.com/rest/issues/assignees#check-if-a-user-can-be-assigned) | GET | /repos/{owner}/{repo}/assignees/{assignee} | indexed |
| [issues/list-for-repo](https://docs.github.com/rest/issues/issues#list-repository-issues) | GET | /repos/{owner}/{repo}/issues | indexed |
| [issues/create](https://docs.github.com/rest/issues/issues#create-an-issue) | POST | /repos/{owner}/{repo}/issues | indexed |
| [issues/list-comments-for-repo](https://docs.github.com/rest/issues/comments#list-issue-comments-for-a-repository) | GET | /repos/{owner}/{repo}/issues/comments | indexed |
| [issues/get-comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) | GET | /repos/{owner}/{repo}/issues/comments/{comment_id} | indexed |
| [issues/update-comment](https://docs.github.com/rest/issues/comments#update-an-issue-comment) | PATCH | /repos/{owner}/{repo}/issues/comments/{comment_id} | indexed |
| [issues/delete-comment](https://docs.github.com/rest/issues/comments#delete-an-issue-comment) | DELETE | /repos/{owner}/{repo}/issues/comments/{comment_id} | indexed |
| [issues/pin-comment](https://docs.github.com/rest/issues/comments#pin-an-issue-comment) | PUT | /repos/{owner}/{repo}/issues/comments/{comment_id}/pin | indexed |
| [issues/unpin-comment](https://docs.github.com/rest/issues/comments#unpin-an-issue-comment) | DELETE | /repos/{owner}/{repo}/issues/comments/{comment_id}/pin | indexed |
| [issues/list-events-for-repo](https://docs.github.com/rest/issues/events#list-issue-events-for-a-repository) | GET | /repos/{owner}/{repo}/issues/events | indexed |
| [issues/get-event](https://docs.github.com/rest/issues/events#get-an-issue-event) | GET | /repos/{owner}/{repo}/issues/events/{event_id} | indexed |
| [issues/get](https://docs.github.com/rest/issues/issues#get-an-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number} | indexed |
| [issues/update](https://docs.github.com/rest/issues/issues#update-an-issue) | PATCH | /repos/{owner}/{repo}/issues/{issue_number} | indexed |
| [issues/list-issue-artifacts](https://docs.github.com/rest/issues/artifacts#list-issue-artifacts) | GET | /repos/{owner}/{repo}/issues/{issue_number}/artifacts | indexed |
| [issues/create-issue-artifact](https://docs.github.com/rest/issues/artifacts#create-an-issue-artifact) | POST | /repos/{owner}/{repo}/issues/{issue_number}/artifacts | indexed |
| [issues/get-issue-artifact](https://docs.github.com/rest/issues/artifacts#get-an-issue-artifact) | GET | /repos/{owner}/{repo}/issues/{issue_number}/artifacts/{artifact_number} | indexed |
| [issues/update-issue-artifact](https://docs.github.com/rest/issues/artifacts#update-an-issue-artifact) | PATCH | /repos/{owner}/{repo}/issues/{issue_number}/artifacts/{artifact_number} | indexed |
| [issues/delete-issue-artifact](https://docs.github.com/rest/issues/artifacts#delete-an-issue-artifact) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/artifacts/{artifact_number} | indexed |
| [issues/add-assignees](https://docs.github.com/rest/issues/assignees#add-assignees-to-an-issue) | POST | /repos/{owner}/{repo}/issues/{issue_number}/assignees | indexed |
| [issues/remove-assignees](https://docs.github.com/rest/issues/assignees#remove-assignees-from-an-issue) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/assignees | indexed |
| [issues/check-user-can-be-assigned-to-issue](https://docs.github.com/rest/issues/assignees#check-if-a-user-can-be-assigned-to-a-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee} | indexed |
| [issues/list-comments](https://docs.github.com/rest/issues/comments#list-issue-comments) | GET | /repos/{owner}/{repo}/issues/{issue_number}/comments | indexed |
| [issues/create-comment](https://docs.github.com/rest/issues/comments#create-an-issue-comment) | POST | /repos/{owner}/{repo}/issues/{issue_number}/comments | indexed |
| [issues/list-dependencies-blocked-by](https://docs.github.com/rest/issues/issue-dependencies#list-dependencies-an-issue-is-blocked-by) | GET | /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by | indexed |
| [issues/add-blocked-by-dependency](https://docs.github.com/rest/issues/issue-dependencies#add-a-dependency-an-issue-is-blocked-by) | POST | /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by | indexed |
| [issues/remove-dependency-blocked-by](https://docs.github.com/rest/issues/issue-dependencies#remove-dependency-an-issue-is-blocked-by) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocked_by/{issue_id} | indexed |
| [issues/list-dependencies-blocking](https://docs.github.com/rest/issues/issue-dependencies#list-dependencies-an-issue-is-blocking) | GET | /repos/{owner}/{repo}/issues/{issue_number}/dependencies/blocking | indexed |
| [issues/list-events](https://docs.github.com/rest/issues/events#list-issue-events) | GET | /repos/{owner}/{repo}/issues/{issue_number}/events | indexed |
| [issues/list-issue-field-values-for-issue](https://docs.github.com/rest/issues/issue-field-values#list-issue-field-values-for-an-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number}/issue-field-values | indexed |
| [issues/add-issue-field-values](https://docs.github.com/rest/issues/issue-field-values#add-issue-field-values-to-an-issue) | POST | /repos/{owner}/{repo}/issues/{issue_number}/issue-field-values | indexed |
| [issues/set-issue-field-values](https://docs.github.com/rest/issues/issue-field-values#set-issue-field-values-for-an-issue) | PUT | /repos/{owner}/{repo}/issues/{issue_number}/issue-field-values | indexed |
| [issues/delete-issue-field-value](https://docs.github.com/rest/issues/issue-field-values#delete-an-issue-field-value-from-an-issue) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/issue-field-values/{issue_field_id} | indexed |
| [issues/list-labels-on-issue](https://docs.github.com/rest/issues/labels#list-labels-for-an-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number}/labels | indexed |
| [issues/add-labels](https://docs.github.com/rest/issues/labels#add-labels-to-an-issue) | POST | /repos/{owner}/{repo}/issues/{issue_number}/labels | indexed |
| [issues/set-labels](https://docs.github.com/rest/issues/labels#set-labels-for-an-issue) | PUT | /repos/{owner}/{repo}/issues/{issue_number}/labels | indexed |
| [issues/remove-all-labels](https://docs.github.com/rest/issues/labels#remove-all-labels-from-an-issue) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/labels | indexed |
| [issues/remove-label](https://docs.github.com/rest/issues/labels#remove-a-label-from-an-issue) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/labels/{name} | indexed |
| [issues/lock](https://docs.github.com/rest/issues/issues#lock-an-issue) | PUT | /repos/{owner}/{repo}/issues/{issue_number}/lock | indexed |
| [issues/unlock](https://docs.github.com/rest/issues/issues#unlock-an-issue) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/lock | indexed |
| [issues/get-parent](https://docs.github.com/rest/issues/sub-issues#get-parent-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number}/parent | indexed |
| [issues/list-relates-to](https://docs.github.com/rest/issues/issues#list-issues-related-to-an-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number}/relates_to | indexed |
| [issues/add-relates-to](https://docs.github.com/rest/issues/issues#add-a-related-issue) | POST | /repos/{owner}/{repo}/issues/{issue_number}/relates_to | indexed |
| [issues/remove-relates-to](https://docs.github.com/rest/issues/issues#remove-a-related-issue) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/relates_to/{issue_id} | indexed |
| [issues/remove-sub-issue](https://docs.github.com/rest/issues/sub-issues#remove-sub-issue) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/sub_issue | indexed |
| [issues/list-sub-issues](https://docs.github.com/rest/issues/sub-issues#list-sub-issues) | GET | /repos/{owner}/{repo}/issues/{issue_number}/sub_issues | indexed |
| [issues/add-sub-issue](https://docs.github.com/rest/issues/sub-issues#add-sub-issue) | POST | /repos/{owner}/{repo}/issues/{issue_number}/sub_issues | indexed |
| [issues/reprioritize-sub-issue](https://docs.github.com/rest/issues/sub-issues#reprioritize-sub-issue) | PATCH | /repos/{owner}/{repo}/issues/{issue_number}/sub_issues/priority | indexed |
| [issues/list-suggestions](https://docs.github.com/rest/issues/issues#list-issue-suggestions) | GET | /repos/{owner}/{repo}/issues/{issue_number}/suggestions | indexed |
| [issues/approve-suggestion](https://docs.github.com/rest/issues/issues#approve-an-issue-suggestion) | POST | /repos/{owner}/{repo}/issues/{issue_number}/suggestions/{suggestion_id}/approve | indexed |
| [issues/dismiss-suggestion](https://docs.github.com/rest/issues/issues#dismiss-an-issue-suggestion) | POST | /repos/{owner}/{repo}/issues/{issue_number}/suggestions/{suggestion_id}/dismiss | indexed |
| [issues/list-events-for-timeline](https://docs.github.com/rest/issues/timeline#list-timeline-events-for-an-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number}/timeline | indexed |
| [issues/list-labels-for-repo](https://docs.github.com/rest/issues/labels#list-labels-for-a-repository) | GET | /repos/{owner}/{repo}/labels | indexed |
| [issues/create-label](https://docs.github.com/rest/issues/labels#create-a-label) | POST | /repos/{owner}/{repo}/labels | indexed |
| [issues/get-label](https://docs.github.com/rest/issues/labels#get-a-label) | GET | /repos/{owner}/{repo}/labels/{name} | indexed |
| [issues/update-label](https://docs.github.com/rest/issues/labels#update-a-label) | PATCH | /repos/{owner}/{repo}/labels/{name} | indexed |
| [issues/delete-label](https://docs.github.com/rest/issues/labels#delete-a-label) | DELETE | /repos/{owner}/{repo}/labels/{name} | indexed |
| [issues/list-milestones](https://docs.github.com/rest/issues/milestones#list-milestones) | GET | /repos/{owner}/{repo}/milestones | indexed |
| [issues/create-milestone](https://docs.github.com/rest/issues/milestones#create-a-milestone) | POST | /repos/{owner}/{repo}/milestones | indexed |
| [issues/get-milestone](https://docs.github.com/rest/issues/milestones#get-a-milestone) | GET | /repos/{owner}/{repo}/milestones/{milestone_number} | indexed |
| [issues/update-milestone](https://docs.github.com/rest/issues/milestones#update-a-milestone) | PATCH | /repos/{owner}/{repo}/milestones/{milestone_number} | indexed |
| [issues/delete-milestone](https://docs.github.com/rest/issues/milestones#delete-a-milestone) | DELETE | /repos/{owner}/{repo}/milestones/{milestone_number} | indexed |
| [issues/list-labels-for-milestone](https://docs.github.com/rest/issues/labels#list-labels-for-issues-in-a-milestone) | GET | /repos/{owner}/{repo}/milestones/{milestone_number}/labels | indexed |
| [issues/list-for-authenticated-user](https://docs.github.com/rest/issues/issues#list-user-account-issues-assigned-to-the-authenticated-user) | GET | /user/issues | indexed |

## REST licenses

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [licenses/get-all-commonly-used](https://docs.github.com/rest/licenses/licenses#get-all-commonly-used-licenses) | GET | /licenses | indexed |
| [licenses/get](https://docs.github.com/rest/licenses/licenses#get-a-license) | GET | /licenses/{license} | indexed |
| [licenses/get-for-repo](https://docs.github.com/rest/licenses/licenses#get-the-license-for-a-repository) | GET | /repos/{owner}/{repo}/license | indexed |

## REST markdown

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [markdown/render](https://docs.github.com/rest/markdown/markdown#render-a-markdown-document) | POST | /markdown | indexed |
| [markdown/render-raw](https://docs.github.com/rest/markdown/markdown#render-a-markdown-document-in-raw-mode) | POST | /markdown/raw | indexed |

## REST meta

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [meta/root](https://docs.github.com/rest/meta/meta#github-api-root) | GET | / | indexed |
| [meta/get](https://docs.github.com/rest/meta/meta#get-apiname-meta-information) | GET | /meta | indexed |
| [meta/get-octocat](https://docs.github.com/rest/meta/meta#get-octocat) | GET | /octocat | indexed |
| [meta/get-all-versions](https://docs.github.com/rest/meta/meta#get-all-api-versions) | GET | /versions | indexed |
| [meta/get-zen](https://docs.github.com/rest/meta/meta#get-the-zen-of-github) | GET | /zen | indexed |

## REST migrations

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [migrations/list-for-org](https://docs.github.com/rest/migrations/orgs#list-organization-migrations) | GET | /orgs/{org}/migrations | indexed |
| [migrations/start-for-org](https://docs.github.com/rest/migrations/orgs#start-an-organization-migration) | POST | /orgs/{org}/migrations | indexed |
| [migrations/get-status-for-org](https://docs.github.com/rest/migrations/orgs#get-an-organization-migration-status) | GET | /orgs/{org}/migrations/{migration_id} | indexed |
| [migrations/download-archive-for-org](https://docs.github.com/rest/migrations/orgs#download-an-organization-migration-archive) | GET | /orgs/{org}/migrations/{migration_id}/archive | indexed |
| [migrations/delete-archive-for-org](https://docs.github.com/rest/migrations/orgs#delete-an-organization-migration-archive) | DELETE | /orgs/{org}/migrations/{migration_id}/archive | indexed |
| [migrations/unlock-repo-for-org](https://docs.github.com/rest/migrations/orgs#unlock-an-organization-repository) | DELETE | /orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock | indexed |
| [migrations/list-repos-for-org](https://docs.github.com/rest/migrations/orgs#list-repositories-in-an-organization-migration) | GET | /orgs/{org}/migrations/{migration_id}/repositories | indexed |
| [migrations/get-import-status](https://docs.github.com/rest/migrations/source-imports#get-an-import-status) | GET | /repos/{owner}/{repo}/import | retired |
| [migrations/start-import](https://docs.github.com/rest/migrations/source-imports#start-an-import) | PUT | /repos/{owner}/{repo}/import | retired |
| [migrations/update-import](https://docs.github.com/rest/migrations/source-imports#update-an-import) | PATCH | /repos/{owner}/{repo}/import | retired |
| [migrations/cancel-import](https://docs.github.com/rest/migrations/source-imports#cancel-an-import) | DELETE | /repos/{owner}/{repo}/import | retired |
| [migrations/get-commit-authors](https://docs.github.com/rest/migrations/source-imports#get-commit-authors) | GET | /repos/{owner}/{repo}/import/authors | retired |
| [migrations/map-commit-author](https://docs.github.com/rest/migrations/source-imports#map-a-commit-author) | PATCH | /repos/{owner}/{repo}/import/authors/{author_id} | retired |
| [migrations/get-large-files](https://docs.github.com/rest/migrations/source-imports#get-large-files) | GET | /repos/{owner}/{repo}/import/large_files | retired |
| [migrations/set-lfs-preference](https://docs.github.com/rest/migrations/source-imports#update-git-lfs-preference) | PATCH | /repos/{owner}/{repo}/import/lfs | retired |
| [migrations/list-for-authenticated-user](https://docs.github.com/rest/migrations/users#list-user-migrations) | GET | /user/migrations | indexed |
| [migrations/start-for-authenticated-user](https://docs.github.com/rest/migrations/users#start-a-user-migration) | POST | /user/migrations | indexed |
| [migrations/get-status-for-authenticated-user](https://docs.github.com/rest/migrations/users#get-a-user-migration-status) | GET | /user/migrations/{migration_id} | indexed |
| [migrations/get-archive-for-authenticated-user](https://docs.github.com/rest/migrations/users#download-a-user-migration-archive) | GET | /user/migrations/{migration_id}/archive | indexed |
| [migrations/delete-archive-for-authenticated-user](https://docs.github.com/rest/migrations/users#delete-a-user-migration-archive) | DELETE | /user/migrations/{migration_id}/archive | indexed |
| [migrations/unlock-repo-for-authenticated-user](https://docs.github.com/rest/migrations/users#unlock-a-user-repository) | DELETE | /user/migrations/{migration_id}/repos/{repo_name}/lock | indexed |
| [migrations/list-repos-for-authenticated-user](https://docs.github.com/rest/migrations/users#list-repositories-for-a-user-migration) | GET | /user/migrations/{migration_id}/repositories | indexed |

## REST oidc

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [oidc/list-oidc-custom-property-inclusions-for-enterprise](https://docs.github.com/rest/actions/oidc#list-oidc-custom-property-inclusions-for-an-enterprise) | GET | /enterprises/{enterprise}/actions/oidc/customization/properties/repo | indexed |
| [oidc/create-oidc-custom-property-inclusion-for-enterprise](https://docs.github.com/rest/actions/oidc#create-an-oidc-custom-property-inclusion-for-an-enterprise) | POST | /enterprises/{enterprise}/actions/oidc/customization/properties/repo | indexed |
| [oidc/delete-oidc-custom-property-inclusion-for-enterprise](https://docs.github.com/rest/actions/oidc#delete-an-oidc-custom-property-inclusion-for-an-enterprise) | DELETE | /enterprises/{enterprise}/actions/oidc/customization/properties/repo/{custom_property_name} | indexed |
| [oidc/list-oidc-custom-property-inclusions-for-org](https://docs.github.com/rest/actions/oidc#list-oidc-custom-property-inclusions-for-an-organization) | GET | /orgs/{org}/actions/oidc/customization/properties/repo | indexed |
| [oidc/create-oidc-custom-property-inclusion-for-org](https://docs.github.com/rest/actions/oidc#create-an-oidc-custom-property-inclusion-for-an-organization) | POST | /orgs/{org}/actions/oidc/customization/properties/repo | indexed |
| [oidc/delete-oidc-custom-property-inclusion-for-org](https://docs.github.com/rest/actions/oidc#delete-an-oidc-custom-property-inclusion-for-an-organization) | DELETE | /orgs/{org}/actions/oidc/customization/properties/repo/{custom_property_name} | indexed |
| [oidc/get-oidc-custom-sub-template-for-org](https://docs.github.com/rest/actions/oidc#get-the-customization-template-for-an-oidc-subject-claim-for-an-organization) | GET | /orgs/{org}/actions/oidc/customization/sub | indexed |
| [oidc/update-oidc-custom-sub-template-for-org](https://docs.github.com/rest/actions/oidc#set-the-customization-template-for-an-oidc-subject-claim-for-an-organization) | PUT | /orgs/{org}/actions/oidc/customization/sub | indexed |

## REST orgs

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [orgs/list](https://docs.github.com/rest/orgs/orgs#list-organizations) | GET | /organizations | indexed |
| [orgs/get](https://docs.github.com/rest/orgs/orgs#get-an-organization) | GET | /orgs/{org} | indexed |
| [orgs/update](https://docs.github.com/rest/orgs/orgs#update-an-organization) | PATCH | /orgs/{org} | indexed |
| [orgs/delete](https://docs.github.com/rest/orgs/orgs#delete-an-organization) | DELETE | /orgs/{org} | indexed |
| [orgs/create-artifact-deployment-record](https://docs.github.com/rest/orgs/artifact-metadata#create-an-artifact-deployment-record) | POST | /orgs/{org}/artifacts/metadata/deployment-record | indexed |
| [orgs/set-cluster-deployment-records](https://docs.github.com/rest/orgs/artifact-metadata#set-cluster-deployment-records) | POST | /orgs/{org}/artifacts/metadata/deployment-record/cluster/{cluster} | indexed |
| [orgs/create-cluster-deployment-records-job](https://docs.github.com/rest/orgs/artifact-metadata#create-a-cluster-deployment-records-job) | POST | /orgs/{org}/artifacts/metadata/deployment-record/cluster/{cluster}/jobs | indexed |
| [orgs/get-cluster-deployment-records-job](https://docs.github.com/rest/orgs/artifact-metadata#get-cluster-deployment-records-job-status) | GET | /orgs/{org}/artifacts/metadata/deployment-record/cluster/{cluster}/jobs/{job_id} | indexed |
| [orgs/create-artifact-storage-record](https://docs.github.com/rest/orgs/artifact-metadata#create-artifact-metadata-storage-record) | POST | /orgs/{org}/artifacts/metadata/storage-record | indexed |
| [orgs/list-artifact-deployment-records](https://docs.github.com/rest/orgs/artifact-metadata#list-artifact-deployment-records) | GET | /orgs/{org}/artifacts/{subject_digest}/metadata/deployment-records | indexed |
| [orgs/list-artifact-storage-records](https://docs.github.com/rest/orgs/artifact-metadata#list-artifact-storage-records) | GET | /orgs/{org}/artifacts/{subject_digest}/metadata/storage-records | indexed |
| [orgs/list-attestations-bulk](https://docs.github.com/rest/orgs/attestations#list-attestations-by-bulk-subject-digests) | POST | /orgs/{org}/attestations/bulk-list | indexed |
| [orgs/delete-attestations-bulk](https://docs.github.com/rest/orgs/attestations#delete-attestations-in-bulk) | POST | /orgs/{org}/attestations/delete-request | indexed |
| [orgs/delete-attestations-by-subject-digest](https://docs.github.com/rest/orgs/attestations#delete-attestations-by-subject-digest) | DELETE | /orgs/{org}/attestations/digest/{subject_digest} | indexed |
| [orgs/list-attestation-repositories](https://docs.github.com/rest/orgs/attestations#list-attestation-repositories) | GET | /orgs/{org}/attestations/repositories | indexed |
| [orgs/delete-attestations-by-id](https://docs.github.com/rest/orgs/attestations#delete-attestations-by-id) | DELETE | /orgs/{org}/attestations/{attestation_id} | indexed |
| [orgs/list-attestations](https://docs.github.com/rest/orgs/attestations#list-attestations) | GET | /orgs/{org}/attestations/{subject_digest} | indexed |
| [orgs/list-blocked-users](https://docs.github.com/rest/orgs/blocking#list-users-blocked-by-an-organization) | GET | /orgs/{org}/blocks | indexed |
| [orgs/check-blocked-user](https://docs.github.com/rest/orgs/blocking#check-if-a-user-is-blocked-by-an-organization) | GET | /orgs/{org}/blocks/{username} | indexed |
| [orgs/block-user](https://docs.github.com/rest/orgs/blocking#block-a-user-from-an-organization) | PUT | /orgs/{org}/blocks/{username} | indexed |
| [orgs/unblock-user](https://docs.github.com/rest/orgs/blocking#unblock-a-user-from-an-organization) | DELETE | /orgs/{org}/blocks/{username} | indexed |
| [orgs/list-failed-invitations](https://docs.github.com/rest/orgs/members#list-failed-organization-invitations) | GET | /orgs/{org}/failed_invitations | indexed |
| [orgs/list-webhooks](https://docs.github.com/rest/orgs/webhooks#list-organization-webhooks) | GET | /orgs/{org}/hooks | indexed |
| [orgs/create-webhook](https://docs.github.com/rest/orgs/webhooks#create-an-organization-webhook) | POST | /orgs/{org}/hooks | indexed |
| [orgs/get-webhook](https://docs.github.com/rest/orgs/webhooks#get-an-organization-webhook) | GET | /orgs/{org}/hooks/{hook_id} | indexed |
| [orgs/update-webhook](https://docs.github.com/rest/orgs/webhooks#update-an-organization-webhook) | PATCH | /orgs/{org}/hooks/{hook_id} | indexed |
| [orgs/delete-webhook](https://docs.github.com/rest/orgs/webhooks#delete-an-organization-webhook) | DELETE | /orgs/{org}/hooks/{hook_id} | indexed |
| [orgs/get-webhook-config-for-org](https://docs.github.com/rest/orgs/webhooks#get-a-webhook-configuration-for-an-organization) | GET | /orgs/{org}/hooks/{hook_id}/config | indexed |
| [orgs/update-webhook-config-for-org](https://docs.github.com/rest/orgs/webhooks#update-a-webhook-configuration-for-an-organization) | PATCH | /orgs/{org}/hooks/{hook_id}/config | indexed |
| [orgs/list-webhook-deliveries](https://docs.github.com/rest/orgs/webhooks#list-deliveries-for-an-organization-webhook) | GET | /orgs/{org}/hooks/{hook_id}/deliveries | indexed |
| [orgs/get-webhook-delivery](https://docs.github.com/rest/orgs/webhooks#get-a-webhook-delivery-for-an-organization-webhook) | GET | /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id} | indexed |
| [orgs/redeliver-webhook-delivery](https://docs.github.com/rest/orgs/webhooks#redeliver-a-delivery-for-an-organization-webhook) | POST | /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | indexed |
| [orgs/ping-webhook](https://docs.github.com/rest/orgs/webhooks#ping-an-organization-webhook) | POST | /orgs/{org}/hooks/{hook_id}/pings | indexed |
| [api-insights/get-route-stats-by-actor](https://docs.github.com/rest/orgs/api-insights#get-route-stats-by-actor) | GET | /orgs/{org}/insights/api/route-stats/{actor_type}/{actor_id} | indexed |
| [api-insights/get-subject-stats](https://docs.github.com/rest/orgs/api-insights#get-subject-stats) | GET | /orgs/{org}/insights/api/subject-stats | indexed |
| [api-insights/get-summary-stats](https://docs.github.com/rest/orgs/api-insights#get-summary-stats) | GET | /orgs/{org}/insights/api/summary-stats | indexed |
| [api-insights/get-summary-stats-by-user](https://docs.github.com/rest/orgs/api-insights#get-summary-stats-by-user) | GET | /orgs/{org}/insights/api/summary-stats/users/{user_id} | indexed |
| [api-insights/get-summary-stats-by-actor](https://docs.github.com/rest/orgs/api-insights#get-summary-stats-by-actor) | GET | /orgs/{org}/insights/api/summary-stats/{actor_type}/{actor_id} | indexed |
| [api-insights/get-time-stats](https://docs.github.com/rest/orgs/api-insights#get-time-stats) | GET | /orgs/{org}/insights/api/time-stats | indexed |
| [api-insights/get-time-stats-by-user](https://docs.github.com/rest/orgs/api-insights#get-time-stats-by-user) | GET | /orgs/{org}/insights/api/time-stats/users/{user_id} | indexed |
| [api-insights/get-time-stats-by-actor](https://docs.github.com/rest/orgs/api-insights#get-time-stats-by-actor) | GET | /orgs/{org}/insights/api/time-stats/{actor_type}/{actor_id} | indexed |
| [api-insights/get-user-stats](https://docs.github.com/rest/orgs/api-insights#get-user-stats) | GET | /orgs/{org}/insights/api/user-stats/{user_id} | indexed |
| [orgs/list-app-installations](https://docs.github.com/rest/orgs/orgs#list-app-installations-for-an-organization) | GET | /orgs/{org}/installations | indexed |
| [orgs/list-pending-invitations](https://docs.github.com/rest/orgs/members#list-pending-organization-invitations) | GET | /orgs/{org}/invitations | indexed |
| [orgs/create-invitation](https://docs.github.com/rest/orgs/members#create-an-organization-invitation) | POST | /orgs/{org}/invitations | indexed |
| [orgs/cancel-invitation](https://docs.github.com/rest/orgs/members#cancel-an-organization-invitation) | DELETE | /orgs/{org}/invitations/{invitation_id} | indexed |
| [orgs/list-invitation-teams](https://docs.github.com/rest/orgs/members#list-organization-invitation-teams) | GET | /orgs/{org}/invitations/{invitation_id}/teams | indexed |
| [orgs/list-issue-fields](https://docs.github.com/rest/orgs/issue-fields#list-issue-fields-for-an-organization) | GET | /orgs/{org}/issue-fields | indexed |
| [orgs/create-issue-field](https://docs.github.com/rest/orgs/issue-fields#create-issue-field-for-an-organization) | POST | /orgs/{org}/issue-fields | indexed |
| [orgs/update-issue-field](https://docs.github.com/rest/orgs/issue-fields#update-issue-field-for-an-organization) | PATCH | /orgs/{org}/issue-fields/{issue_field_id} | indexed |
| [orgs/delete-issue-field](https://docs.github.com/rest/orgs/issue-fields#delete-issue-field-for-an-organization) | DELETE | /orgs/{org}/issue-fields/{issue_field_id} | indexed |
| [orgs/list-issue-types](https://docs.github.com/rest/orgs/issue-types#list-issue-types-for-an-organization) | GET | /orgs/{org}/issue-types | indexed |
| [orgs/create-issue-type](https://docs.github.com/rest/orgs/issue-types#create-issue-type-for-an-organization) | POST | /orgs/{org}/issue-types | indexed |
| [orgs/update-issue-type](https://docs.github.com/rest/orgs/issue-types#update-issue-type-for-an-organization) | PUT | /orgs/{org}/issue-types/{issue_type_id} | indexed |
| [orgs/delete-issue-type](https://docs.github.com/rest/orgs/issue-types#delete-issue-type-for-an-organization) | DELETE | /orgs/{org}/issue-types/{issue_type_id} | indexed |
| [orgs/list-members](https://docs.github.com/rest/orgs/members#list-organization-members) | GET | /orgs/{org}/members | indexed |
| [orgs/check-membership-for-user](https://docs.github.com/rest/orgs/members#check-organization-membership-for-a-user) | GET | /orgs/{org}/members/{username} | indexed |
| [orgs/remove-member](https://docs.github.com/rest/orgs/members#remove-an-organization-member) | DELETE | /orgs/{org}/members/{username} | indexed |
| [orgs/get-membership-for-user](https://docs.github.com/rest/orgs/members#get-organization-membership-for-a-user) | GET | /orgs/{org}/memberships/{username} | indexed |
| [orgs/set-membership-for-user](https://docs.github.com/rest/orgs/members#set-organization-membership-for-a-user) | PUT | /orgs/{org}/memberships/{username} | indexed |
| [orgs/remove-membership-for-user](https://docs.github.com/rest/orgs/members#remove-organization-membership-for-a-user) | DELETE | /orgs/{org}/memberships/{username} | indexed |
| [orgs/list-org-roles](https://docs.github.com/rest/orgs/organization-roles#get-all-organization-roles-for-an-organization) | GET | /orgs/{org}/organization-roles | indexed |
| [orgs/revoke-all-org-roles-team](https://docs.github.com/rest/orgs/organization-roles#remove-all-organization-roles-for-a-team) | DELETE | /orgs/{org}/organization-roles/teams/{team_slug} | indexed |
| [orgs/assign-team-to-org-role](https://docs.github.com/rest/orgs/organization-roles#assign-an-organization-role-to-a-team) | PUT | /orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | indexed |
| [orgs/revoke-org-role-team](https://docs.github.com/rest/orgs/organization-roles#remove-an-organization-role-from-a-team) | DELETE | /orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | indexed |
| [orgs/revoke-all-org-roles-user](https://docs.github.com/rest/orgs/organization-roles#remove-all-organization-roles-for-a-user) | DELETE | /orgs/{org}/organization-roles/users/{username} | indexed |
| [orgs/assign-user-to-org-role](https://docs.github.com/rest/orgs/organization-roles#assign-an-organization-role-to-a-user) | PUT | /orgs/{org}/organization-roles/users/{username}/{role_id} | indexed |
| [orgs/revoke-org-role-user](https://docs.github.com/rest/orgs/organization-roles#remove-an-organization-role-from-a-user) | DELETE | /orgs/{org}/organization-roles/users/{username}/{role_id} | indexed |
| [orgs/get-org-role](https://docs.github.com/rest/orgs/organization-roles#get-an-organization-role) | GET | /orgs/{org}/organization-roles/{role_id} | indexed |
| [orgs/list-org-role-teams](https://docs.github.com/rest/orgs/organization-roles#list-teams-that-are-assigned-to-an-organization-role) | GET | /orgs/{org}/organization-roles/{role_id}/teams | indexed |
| [orgs/list-org-role-users](https://docs.github.com/rest/orgs/organization-roles#list-users-that-are-assigned-to-an-organization-role) | GET | /orgs/{org}/organization-roles/{role_id}/users | indexed |
| [orgs/list-outside-collaborators](https://docs.github.com/rest/orgs/outside-collaborators#list-outside-collaborators-for-an-organization) | GET | /orgs/{org}/outside_collaborators | indexed |
| [orgs/convert-member-to-outside-collaborator](https://docs.github.com/rest/orgs/outside-collaborators#convert-an-organization-member-to-outside-collaborator) | PUT | /orgs/{org}/outside_collaborators/{username} | indexed |
| [orgs/remove-outside-collaborator](https://docs.github.com/rest/orgs/outside-collaborators#remove-outside-collaborator-from-an-organization) | DELETE | /orgs/{org}/outside_collaborators/{username} | indexed |
| [orgs/list-pat-grant-requests](https://docs.github.com/rest/orgs/personal-access-tokens#list-requests-to-access-organization-resources-with-fine-grained-personal-access-tokens) | GET | /orgs/{org}/personal-access-token-requests | indexed |
| [orgs/review-pat-grant-requests-in-bulk](https://docs.github.com/rest/orgs/personal-access-tokens#review-requests-to-access-organization-resources-with-fine-grained-personal-access-tokens) | POST | /orgs/{org}/personal-access-token-requests | indexed |
| [orgs/review-pat-grant-request](https://docs.github.com/rest/orgs/personal-access-tokens#review-a-request-to-access-organization-resources-with-a-fine-grained-personal-access-token) | POST | /orgs/{org}/personal-access-token-requests/{pat_request_id} | indexed |
| [orgs/list-pat-grant-request-repositories](https://docs.github.com/rest/orgs/personal-access-tokens#list-repositories-requested-to-be-accessed-by-a-fine-grained-personal-access-token) | GET | /orgs/{org}/personal-access-token-requests/{pat_request_id}/repositories | indexed |
| [orgs/list-pat-grants](https://docs.github.com/rest/orgs/personal-access-tokens#list-fine-grained-personal-access-tokens-with-access-to-organization-resources) | GET | /orgs/{org}/personal-access-tokens | indexed |
| [orgs/update-pat-accesses](https://docs.github.com/rest/orgs/personal-access-tokens#update-the-access-to-organization-resources-via-fine-grained-personal-access-tokens) | POST | /orgs/{org}/personal-access-tokens | indexed |
| [orgs/update-pat-access](https://docs.github.com/rest/orgs/personal-access-tokens#update-the-access-a-fine-grained-personal-access-token-has-to-organization-resources) | POST | /orgs/{org}/personal-access-tokens/{pat_id} | indexed |
| [orgs/list-pat-grant-repositories](https://docs.github.com/rest/orgs/personal-access-tokens#list-repositories-a-fine-grained-personal-access-token-has-access-to) | GET | /orgs/{org}/personal-access-tokens/{pat_id}/repositories | indexed |
| [orgs/external-properties-for-repos-get-organization-app-installations](https://docs.github.com/rest/orgs/custom-properties#get-registered-app-installations-for-external-custom-properties) | GET | /orgs/{org}/properties/installations | indexed |
| [orgs/external-properties-for-repos-register-organization-app-installation](https://docs.github.com/rest/orgs/custom-properties#register-an-app-installation-for-external-custom-properties) | POST | /orgs/{org}/properties/installations | indexed |
| [orgs/external-properties-for-repos-get-organization-definitions](https://docs.github.com/rest/orgs/custom-properties#get-all-external-custom-properties-for-a-github-app-installation-in-an-organization) | GET | /orgs/{org}/properties/installations/schema | indexed |
| [orgs/external-properties-for-repos-create-or-update-organization-values](https://docs.github.com/rest/orgs/custom-properties#create-or-update-external-custom-property-values-for-organization-repositories) | PATCH | /orgs/{org}/properties/installations/values | indexed |
| [orgs/external-properties-for-repos-create-or-update-values-for-organization-property](https://docs.github.com/rest/orgs/custom-properties#create-or-update-external-custom-property-values-for-a-property-across-organization-repositories) | PATCH | /orgs/{org}/properties/installations/values/{property_name} | indexed |
| [orgs/external-properties-for-repos-delete-organization-values](https://docs.github.com/rest/orgs/custom-properties#remove-all-external-custom-property-values-for-a-property-across-all-organization-repositories) | DELETE | /orgs/{org}/properties/installations/values/{property_name} | indexed |
| [orgs/custom-properties-for-repos-get-organization-definitions](https://docs.github.com/rest/orgs/custom-properties#get-all-custom-properties-for-an-organization) | GET | /orgs/{org}/properties/schema | indexed |
| [orgs/custom-properties-for-repos-create-or-update-organization-definitions](https://docs.github.com/rest/orgs/custom-properties#create-or-update-custom-properties-for-an-organization) | PATCH | /orgs/{org}/properties/schema | indexed |
| [orgs/custom-properties-for-repos-get-organization-definition](https://docs.github.com/rest/orgs/custom-properties#get-a-custom-property-for-an-organization) | GET | /orgs/{org}/properties/schema/{custom_property_name} | indexed |
| [orgs/custom-properties-for-repos-create-or-update-organization-definition](https://docs.github.com/rest/orgs/custom-properties#create-or-update-a-custom-property-for-an-organization) | PUT | /orgs/{org}/properties/schema/{custom_property_name} | indexed |
| [orgs/custom-properties-for-repos-delete-organization-definition](https://docs.github.com/rest/orgs/custom-properties#remove-a-custom-property-for-an-organization) | DELETE | /orgs/{org}/properties/schema/{custom_property_name} | indexed |
| [orgs/custom-properties-for-repos-get-organization-values](https://docs.github.com/rest/orgs/custom-properties#list-custom-property-values-for-organization-repositories) | GET | /orgs/{org}/properties/values | indexed |
| [orgs/custom-properties-for-repos-create-or-update-organization-values](https://docs.github.com/rest/orgs/custom-properties#create-or-update-custom-property-values-for-organization-repositories) | PATCH | /orgs/{org}/properties/values | indexed |
| [orgs/list-public-members](https://docs.github.com/rest/orgs/members#list-public-organization-members) | GET | /orgs/{org}/public_members | indexed |
| [orgs/check-public-membership-for-user](https://docs.github.com/rest/orgs/members#check-public-organization-membership-for-a-user) | GET | /orgs/{org}/public_members/{username} | indexed |
| [orgs/set-public-membership-for-authenticated-user](https://docs.github.com/rest/orgs/members#set-public-organization-membership-for-the-authenticated-user) | PUT | /orgs/{org}/public_members/{username} | indexed |
| [orgs/remove-public-membership-for-authenticated-user](https://docs.github.com/rest/orgs/members#remove-public-organization-membership-for-the-authenticated-user) | DELETE | /orgs/{org}/public_members/{username} | indexed |
| [orgs/get-org-ruleset-history](https://docs.github.com/rest/orgs/rules#get-organization-ruleset-history) | GET | /orgs/{org}/rulesets/{ruleset_id}/history | indexed |
| [orgs/get-org-ruleset-version](https://docs.github.com/rest/orgs/rules#get-organization-ruleset-version) | GET | /orgs/{org}/rulesets/{ruleset_id}/history/{version_id} | indexed |
| [orgs/list-security-manager-teams](https://docs.github.com/rest/orgs/security-managers#list-security-manager-teams) | GET | /orgs/{org}/security-managers | retired |
| [orgs/add-security-manager-team](https://docs.github.com/rest/orgs/security-managers#add-a-security-manager-team) | PUT | /orgs/{org}/security-managers/teams/{team_slug} | retired |
| [orgs/remove-security-manager-team](https://docs.github.com/rest/orgs/security-managers#remove-a-security-manager-team) | DELETE | /orgs/{org}/security-managers/teams/{team_slug} | retired |
| [orgs/get-immutable-releases-settings](https://docs.github.com/rest/orgs/orgs#get-immutable-releases-settings-for-an-organization) | GET | /orgs/{org}/settings/immutable-releases | indexed |
| [orgs/set-immutable-releases-settings](https://docs.github.com/rest/orgs/orgs#set-immutable-releases-settings-for-an-organization) | PUT | /orgs/{org}/settings/immutable-releases | indexed |
| [orgs/get-immutable-releases-settings-repositories](https://docs.github.com/rest/orgs/orgs#list-selected-repositories-for-immutable-releases-enforcement) | GET | /orgs/{org}/settings/immutable-releases/repositories | indexed |
| [orgs/set-immutable-releases-settings-repositories](https://docs.github.com/rest/orgs/orgs#set-selected-repositories-for-immutable-releases-enforcement) | PUT | /orgs/{org}/settings/immutable-releases/repositories | indexed |
| [orgs/enable-selected-repository-immutable-releases-organization](https://docs.github.com/rest/orgs/orgs#enable-a-selected-repository-for-immutable-releases-in-an-organization) | PUT | /orgs/{org}/settings/immutable-releases/repositories/{repository_id} | indexed |
| [orgs/disable-selected-repository-immutable-releases-organization](https://docs.github.com/rest/orgs/orgs#disable-a-selected-repository-for-immutable-releases-in-an-organization) | DELETE | /orgs/{org}/settings/immutable-releases/repositories/{repository_id} | indexed |
| [orgs/enable-or-disable-security-product-on-all-org-repos](https://docs.github.com/rest/orgs/orgs#enable-or-disable-a-security-feature-for-an-organization) | POST | /orgs/{org}/{security_product}/{enablement} | deprecated |
| [orgs/list-memberships-for-authenticated-user](https://docs.github.com/rest/orgs/members#list-organization-memberships-for-the-authenticated-user) | GET | /user/memberships/orgs | indexed |
| [orgs/get-membership-for-authenticated-user](https://docs.github.com/rest/orgs/members#get-an-organization-membership-for-the-authenticated-user) | GET | /user/memberships/orgs/{org} | indexed |
| [orgs/update-membership-for-authenticated-user](https://docs.github.com/rest/orgs/members#update-an-organization-membership-for-the-authenticated-user) | PATCH | /user/memberships/orgs/{org} | indexed |
| [orgs/list-for-authenticated-user](https://docs.github.com/rest/orgs/orgs#list-organizations-for-the-authenticated-user) | GET | /user/orgs | indexed |
| [orgs/list-for-user](https://docs.github.com/rest/orgs/orgs#list-organizations-for-a-user) | GET | /users/{username}/orgs | indexed |

## REST packages

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [packages/list-docker-migration-conflicting-packages-for-organization](https://docs.github.com/rest/packages/packages#get-list-of-conflicting-packages-during-docker-migration-for-organization) | GET | /orgs/{org}/docker/conflicts | indexed |
| [packages/list-packages-for-organization](https://docs.github.com/rest/packages/packages#list-packages-for-an-organization) | GET | /orgs/{org}/packages | indexed |
| [packages/get-package-for-organization](https://docs.github.com/rest/packages/packages#get-a-package-for-an-organization) | GET | /orgs/{org}/packages/{package_type}/{package_name} | indexed |
| [packages/delete-package-for-org](https://docs.github.com/rest/packages/packages#delete-a-package-for-an-organization) | DELETE | /orgs/{org}/packages/{package_type}/{package_name} | indexed |
| [packages/restore-package-for-org](https://docs.github.com/rest/packages/packages#restore-a-package-for-an-organization) | POST | /orgs/{org}/packages/{package_type}/{package_name}/restore | indexed |
| [packages/get-all-package-versions-for-package-owned-by-org](https://docs.github.com/rest/packages/packages#list-package-versions-for-a-package-owned-by-an-organization) | GET | /orgs/{org}/packages/{package_type}/{package_name}/versions | indexed |
| [packages/get-package-version-for-organization](https://docs.github.com/rest/packages/packages#get-a-package-version-for-an-organization) | GET | /orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id} | indexed |
| [packages/delete-package-version-for-org](https://docs.github.com/rest/packages/packages#delete-package-version-for-an-organization) | DELETE | /orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id} | indexed |
| [packages/restore-package-version-for-org](https://docs.github.com/rest/packages/packages#restore-package-version-for-an-organization) | POST | /orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore | indexed |
| [packages/list-docker-migration-conflicting-packages-for-authenticated-user](https://docs.github.com/rest/packages/packages#get-list-of-conflicting-packages-during-docker-migration-for-authenticated-user) | GET | /user/docker/conflicts | indexed |
| [packages/list-packages-for-authenticated-user](https://docs.github.com/rest/packages/packages#list-packages-for-the-authenticated-users-namespace) | GET | /user/packages | indexed |
| [packages/get-package-for-authenticated-user](https://docs.github.com/rest/packages/packages#get-a-package-for-the-authenticated-user) | GET | /user/packages/{package_type}/{package_name} | indexed |
| [packages/delete-package-for-authenticated-user](https://docs.github.com/rest/packages/packages#delete-a-package-for-the-authenticated-user) | DELETE | /user/packages/{package_type}/{package_name} | indexed |
| [packages/restore-package-for-authenticated-user](https://docs.github.com/rest/packages/packages#restore-a-package-for-the-authenticated-user) | POST | /user/packages/{package_type}/{package_name}/restore | indexed |
| [packages/get-all-package-versions-for-package-owned-by-authenticated-user](https://docs.github.com/rest/packages/packages#list-package-versions-for-a-package-owned-by-the-authenticated-user) | GET | /user/packages/{package_type}/{package_name}/versions | indexed |
| [packages/get-package-version-for-authenticated-user](https://docs.github.com/rest/packages/packages#get-a-package-version-for-the-authenticated-user) | GET | /user/packages/{package_type}/{package_name}/versions/{package_version_id} | indexed |
| [packages/delete-package-version-for-authenticated-user](https://docs.github.com/rest/packages/packages#delete-a-package-version-for-the-authenticated-user) | DELETE | /user/packages/{package_type}/{package_name}/versions/{package_version_id} | indexed |
| [packages/restore-package-version-for-authenticated-user](https://docs.github.com/rest/packages/packages#restore-a-package-version-for-the-authenticated-user) | POST | /user/packages/{package_type}/{package_name}/versions/{package_version_id}/restore | indexed |
| [packages/list-docker-migration-conflicting-packages-for-user](https://docs.github.com/rest/packages/packages#get-list-of-conflicting-packages-during-docker-migration-for-user) | GET | /users/{username}/docker/conflicts | indexed |
| [packages/list-packages-for-user](https://docs.github.com/rest/packages/packages#list-packages-for-a-user) | GET | /users/{username}/packages | indexed |
| [packages/get-package-for-user](https://docs.github.com/rest/packages/packages#get-a-package-for-a-user) | GET | /users/{username}/packages/{package_type}/{package_name} | indexed |
| [packages/delete-package-for-user](https://docs.github.com/rest/packages/packages#delete-a-package-for-a-user) | DELETE | /users/{username}/packages/{package_type}/{package_name} | indexed |
| [packages/restore-package-for-user](https://docs.github.com/rest/packages/packages#restore-a-package-for-a-user) | POST | /users/{username}/packages/{package_type}/{package_name}/restore | indexed |
| [packages/get-all-package-versions-for-package-owned-by-user](https://docs.github.com/rest/packages/packages#list-package-versions-for-a-package-owned-by-a-user) | GET | /users/{username}/packages/{package_type}/{package_name}/versions | indexed |
| [packages/get-package-version-for-user](https://docs.github.com/rest/packages/packages#get-a-package-version-for-a-user) | GET | /users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id} | indexed |
| [packages/delete-package-version-for-user](https://docs.github.com/rest/packages/packages#delete-package-version-for-a-user) | DELETE | /users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id} | indexed |
| [packages/restore-package-version-for-user](https://docs.github.com/rest/packages/packages#restore-package-version-for-a-user) | POST | /users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore | indexed |

## REST private-registries

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [private-registries/list-org-private-registries](https://docs.github.com/rest/private-registries/organization-configurations#list-private-registries-for-an-organization) | GET | /orgs/{org}/private-registries | indexed |
| [private-registries/create-org-private-registry](https://docs.github.com/rest/private-registries/organization-configurations#create-a-private-registry-for-an-organization) | POST | /orgs/{org}/private-registries | indexed |
| [private-registries/get-org-public-key](https://docs.github.com/rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization) | GET | /orgs/{org}/private-registries/public-key | indexed |
| [private-registries/get-org-private-registry](https://docs.github.com/rest/private-registries/organization-configurations#get-a-private-registry-for-an-organization) | GET | /orgs/{org}/private-registries/{secret_name} | indexed |
| [private-registries/update-org-private-registry](https://docs.github.com/rest/private-registries/organization-configurations#update-a-private-registry-for-an-organization) | PATCH | /orgs/{org}/private-registries/{secret_name} | indexed |
| [private-registries/delete-org-private-registry](https://docs.github.com/rest/private-registries/organization-configurations#delete-a-private-registry-for-an-organization) | DELETE | /orgs/{org}/private-registries/{secret_name} | indexed |

## REST projects

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [projects/list-for-org](https://docs.github.com/rest/projects/projects#list-projects-for-organization) | GET | /orgs/{org}/projectsV2 | indexed |
| [projects/get-for-org](https://docs.github.com/rest/projects/projects#get-project-for-organization) | GET | /orgs/{org}/projectsV2/{project_number} | indexed |
| [projects/create-draft-item-for-org](https://docs.github.com/rest/projects/drafts#create-draft-item-for-organization-owned-project) | POST | /orgs/{org}/projectsV2/{project_number}/drafts | indexed |
| [projects/list-fields-for-org](https://docs.github.com/rest/projects/fields#list-project-fields-for-organization) | GET | /orgs/{org}/projectsV2/{project_number}/fields | indexed |
| [projects/add-field-for-org](https://docs.github.com/rest/projects/fields#add-a-field-to-an-organization-owned-project) | POST | /orgs/{org}/projectsV2/{project_number}/fields | indexed |
| [projects/get-field-for-org](https://docs.github.com/rest/projects/fields#get-project-field-for-organization) | GET | /orgs/{org}/projectsV2/{project_number}/fields/{field_id} | indexed |
| [projects/list-items-for-org](https://docs.github.com/rest/projects/items#list-items-for-an-organization-owned-project) | GET | /orgs/{org}/projectsV2/{project_number}/items | indexed |
| [projects/add-item-for-org](https://docs.github.com/rest/projects/items#add-item-to-organization-owned-project) | POST | /orgs/{org}/projectsV2/{project_number}/items | indexed |
| [projects/get-org-item](https://docs.github.com/rest/projects/items#get-an-item-for-an-organization-owned-project) | GET | /orgs/{org}/projectsV2/{project_number}/items/{item_id} | indexed |
| [projects/update-item-for-org](https://docs.github.com/rest/projects/items#update-project-item-for-organization) | PATCH | /orgs/{org}/projectsV2/{project_number}/items/{item_id} | indexed |
| [projects/delete-item-for-org](https://docs.github.com/rest/projects/items#delete-project-item-for-organization) | DELETE | /orgs/{org}/projectsV2/{project_number}/items/{item_id} | indexed |
| [projects/create-view-for-org](https://docs.github.com/rest/projects/views#create-a-view-for-an-organization-owned-project) | POST | /orgs/{org}/projectsV2/{project_number}/views | indexed |
| [projects/list-view-items-for-org](https://docs.github.com/rest/projects/items#list-items-for-an-organization-project-view) | GET | /orgs/{org}/projectsV2/{project_number}/views/{view_number}/items | indexed |
| [projects/create-draft-item-for-authenticated-user](https://docs.github.com/rest/projects/drafts#create-draft-item-for-user-owned-project) | POST | /user/{user_id}/projectsV2/{project_number}/drafts | indexed |
| [projects/create-view-for-user](https://docs.github.com/rest/projects/views#create-a-view-for-a-user-owned-project) | POST | /users/{user_id}/projectsV2/{project_number}/views | indexed |
| [projects/list-for-user](https://docs.github.com/rest/projects/projects#list-projects-for-user) | GET | /users/{username}/projectsV2 | indexed |
| [projects/get-for-user](https://docs.github.com/rest/projects/projects#get-project-for-user) | GET | /users/{username}/projectsV2/{project_number} | indexed |
| [projects/list-fields-for-user](https://docs.github.com/rest/projects/fields#list-project-fields-for-user) | GET | /users/{username}/projectsV2/{project_number}/fields | indexed |
| [projects/add-field-for-user](https://docs.github.com/rest/projects/fields#add-field-to-user-owned-project) | POST | /users/{username}/projectsV2/{project_number}/fields | indexed |
| [projects/get-field-for-user](https://docs.github.com/rest/projects/fields#get-project-field-for-user) | GET | /users/{username}/projectsV2/{project_number}/fields/{field_id} | indexed |
| [projects/list-items-for-user](https://docs.github.com/rest/projects/items#list-items-for-a-user-owned-project) | GET | /users/{username}/projectsV2/{project_number}/items | indexed |
| [projects/add-item-for-user](https://docs.github.com/rest/projects/items#add-item-to-user-owned-project) | POST | /users/{username}/projectsV2/{project_number}/items | indexed |
| [projects/get-user-item](https://docs.github.com/rest/projects/items#get-an-item-for-a-user-owned-project) | GET | /users/{username}/projectsV2/{project_number}/items/{item_id} | indexed |
| [projects/update-item-for-user](https://docs.github.com/rest/projects/items#update-project-item-for-user) | PATCH | /users/{username}/projectsV2/{project_number}/items/{item_id} | indexed |
| [projects/delete-item-for-user](https://docs.github.com/rest/projects/items#delete-project-item-for-user) | DELETE | /users/{username}/projectsV2/{project_number}/items/{item_id} | indexed |
| [projects/list-view-items-for-user](https://docs.github.com/rest/projects/items#list-items-for-a-user-project-view) | GET | /users/{username}/projectsV2/{project_number}/views/{view_number}/items | indexed |

## REST pulls

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [pulls/list](https://docs.github.com/rest/pulls/pulls#list-pull-requests) | GET | /repos/{owner}/{repo}/pulls | indexed |
| [pulls/create](https://docs.github.com/rest/pulls/pulls#create-a-pull-request) | POST | /repos/{owner}/{repo}/pulls | indexed |
| [pulls/list-review-comments-for-repo](https://docs.github.com/rest/pulls/comments#list-review-comments-in-a-repository) | GET | /repos/{owner}/{repo}/pulls/comments | indexed |
| [pulls/get-review-comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request) | GET | /repos/{owner}/{repo}/pulls/comments/{comment_id} | indexed |
| [pulls/update-review-comment](https://docs.github.com/rest/pulls/comments#update-a-review-comment-for-a-pull-request) | PATCH | /repos/{owner}/{repo}/pulls/comments/{comment_id} | indexed |
| [pulls/delete-review-comment](https://docs.github.com/rest/pulls/comments#delete-a-review-comment-for-a-pull-request) | DELETE | /repos/{owner}/{repo}/pulls/comments/{comment_id} | indexed |
| [pulls/get](https://docs.github.com/rest/pulls/pulls#get-a-pull-request) | GET | /repos/{owner}/{repo}/pulls/{pull_number} | indexed |
| [pulls/update](https://docs.github.com/rest/pulls/pulls#update-a-pull-request) | PATCH | /repos/{owner}/{repo}/pulls/{pull_number} | indexed |
| [pulls/list-review-comments](https://docs.github.com/rest/pulls/comments#list-review-comments-on-a-pull-request) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/comments | indexed |
| [pulls/create-review-comment](https://docs.github.com/rest/pulls/comments#create-a-review-comment-for-a-pull-request) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/comments | indexed |
| [pulls/create-reply-for-review-comment](https://docs.github.com/rest/pulls/comments#create-a-reply-for-a-review-comment) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies | indexed |
| [pulls/list-commits](https://docs.github.com/rest/pulls/pulls#list-commits-on-a-pull-request) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/commits | indexed |
| [pulls/request-copilot-code-review](https://docs.github.com/rest/pulls/copilot-code-review#request-a-copilot-code-review-for-a-pull-request) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/copilot-code-review | indexed |
| [pulls/list-files](https://docs.github.com/rest/pulls/pulls#list-pull-requests-files) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/files | indexed |
| [pulls/check-if-merged](https://docs.github.com/rest/pulls/pulls#check-if-a-pull-request-has-been-merged) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/merge | indexed |
| [pulls/merge](https://docs.github.com/rest/pulls/pulls#merge-a-pull-request) | PUT | /repos/{owner}/{repo}/pulls/{pull_number}/merge | indexed |
| [pulls/merge-async](https://docs.github.com/rest/pulls/pulls#merge-a-pull-request-asynchronously) | PUT | /repos/{owner}/{repo}/pulls/{pull_number}/merge-async | indexed |
| [pulls/get-merge-async-result](https://docs.github.com/rest/pulls/pulls#get-the-result-of-an-asynchronous-merge) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/merge-async/{uuid} | indexed |
| [pulls/list-requested-reviewers](https://docs.github.com/rest/pulls/review-requests#get-all-requested-reviewers-for-a-pull-request) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | indexed |
| [pulls/request-reviewers](https://docs.github.com/rest/pulls/review-requests#request-reviewers-for-a-pull-request) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | indexed |
| [pulls/remove-requested-reviewers](https://docs.github.com/rest/pulls/review-requests#remove-requested-reviewers-from-a-pull-request) | DELETE | /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | indexed |
| [pulls/rerequest-reviewers](https://docs.github.com/rest/pulls/review-requests#rerequest-reviewers-for-a-pull-request) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers/rerequest | indexed |
| [pulls/list-reviews](https://docs.github.com/rest/pulls/reviews#list-reviews-for-a-pull-request) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/reviews | indexed |
| [pulls/create-review](https://docs.github.com/rest/pulls/reviews#create-a-review-for-a-pull-request) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/reviews | indexed |
| [pulls/get-review](https://docs.github.com/rest/pulls/reviews#get-a-review-for-a-pull-request) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | indexed |
| [pulls/update-review](https://docs.github.com/rest/pulls/reviews#update-a-review-for-a-pull-request) | PUT | /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | indexed |
| [pulls/delete-pending-review](https://docs.github.com/rest/pulls/reviews#delete-a-pending-review-for-a-pull-request) | DELETE | /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | indexed |
| [pulls/list-comments-for-review](https://docs.github.com/rest/pulls/reviews#list-comments-for-a-pull-request-review) | GET | /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments | indexed |
| [pulls/dismiss-review](https://docs.github.com/rest/pulls/reviews#dismiss-a-review-for-a-pull-request) | PUT | /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals | indexed |
| [pulls/submit-review](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request) | POST | /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events | indexed |
| [pulls/update-branch](https://docs.github.com/rest/pulls/pulls#update-a-pull-request-branch) | PUT | /repos/{owner}/{repo}/pulls/{pull_number}/update-branch | indexed |
| [pull-request-stacks/list](https://docs.github.com/rest/pulls/stacks#list-pull-request-stacks) | GET | /repos/{owner}/{repo}/stacks | indexed |
| [pull-request-stacks/create](https://docs.github.com/rest/pulls/stacks#create-a-pull-request-stack) | POST | /repos/{owner}/{repo}/stacks | indexed |
| [pull-request-stacks/get](https://docs.github.com/rest/pulls/stacks#get-a-pull-request-stack) | GET | /repos/{owner}/{repo}/stacks/{stack_number} | indexed |
| [pull-request-stacks/add](https://docs.github.com/rest/pulls/stacks#add-pull-requests-to-a-pull-request-stack) | POST | /repos/{owner}/{repo}/stacks/{stack_number}/add | indexed |
| [pull-request-stacks/unstack](https://docs.github.com/rest/pulls/stacks#remove-pull-requests-from-a-pull-request-stack) | POST | /repos/{owner}/{repo}/stacks/{stack_number}/unstack | indexed |

## REST rate-limit

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [rate-limit/get](https://docs.github.com/rest/rate-limit/rate-limit#get-rate-limit-status-for-the-authenticated-user) | GET | /rate_limit | indexed |

## REST reactions

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [reactions/list-for-commit-comment](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-commit-comment) | GET | /repos/{owner}/{repo}/comments/{comment_id}/reactions | indexed |
| [reactions/create-for-commit-comment](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-commit-comment) | POST | /repos/{owner}/{repo}/comments/{comment_id}/reactions | indexed |
| [reactions/delete-for-commit-comment](https://docs.github.com/rest/reactions/reactions#delete-a-commit-comment-reaction) | DELETE | /repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id} | indexed |
| [reactions/list-for-issue-comment](https://docs.github.com/rest/reactions/reactions#list-reactions-for-an-issue-comment) | GET | /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | indexed |
| [reactions/create-for-issue-comment](https://docs.github.com/rest/reactions/reactions#create-reaction-for-an-issue-comment) | POST | /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | indexed |
| [reactions/delete-for-issue-comment](https://docs.github.com/rest/reactions/reactions#delete-an-issue-comment-reaction) | DELETE | /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id} | indexed |
| [reactions/list-for-issue](https://docs.github.com/rest/reactions/reactions#list-reactions-for-an-issue) | GET | /repos/{owner}/{repo}/issues/{issue_number}/reactions | indexed |
| [reactions/create-for-issue](https://docs.github.com/rest/reactions/reactions#create-reaction-for-an-issue) | POST | /repos/{owner}/{repo}/issues/{issue_number}/reactions | indexed |
| [reactions/delete-for-issue](https://docs.github.com/rest/reactions/reactions#delete-an-issue-reaction) | DELETE | /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id} | indexed |
| [reactions/list-for-pull-request-review-comment](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-pull-request-review-comment) | GET | /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | indexed |
| [reactions/create-for-pull-request-review-comment](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-pull-request-review-comment) | POST | /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | indexed |
| [reactions/delete-for-pull-request-comment](https://docs.github.com/rest/reactions/reactions#delete-a-pull-request-comment-reaction) | DELETE | /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id} | indexed |
| [reactions/list-for-release](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-release) | GET | /repos/{owner}/{repo}/releases/{release_id}/reactions | indexed |
| [reactions/create-for-release](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-release) | POST | /repos/{owner}/{repo}/releases/{release_id}/reactions | indexed |
| [reactions/delete-for-release](https://docs.github.com/rest/reactions/reactions#delete-a-release-reaction) | DELETE | /repos/{owner}/{repo}/releases/{release_id}/reactions/{reaction_id} | indexed |

## REST repos

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [repos/list-for-org](https://docs.github.com/rest/repos/repos#list-organization-repositories) | GET | /orgs/{org}/repos | indexed |
| [repos/create-in-org](https://docs.github.com/rest/repos/repos#create-an-organization-repository) | POST | /orgs/{org}/repos | indexed |
| [repos/get-org-rulesets](https://docs.github.com/rest/orgs/rules#get-all-organization-repository-rulesets) | GET | /orgs/{org}/rulesets | indexed |
| [repos/create-org-ruleset](https://docs.github.com/rest/orgs/rules#create-an-organization-repository-ruleset) | POST | /orgs/{org}/rulesets | indexed |
| [repos/get-org-rule-suites](https://docs.github.com/rest/orgs/rule-suites#list-organization-rule-suites) | GET | /orgs/{org}/rulesets/rule-suites | indexed |
| [repos/get-org-rule-suite](https://docs.github.com/rest/orgs/rule-suites#get-an-organization-rule-suite) | GET | /orgs/{org}/rulesets/rule-suites/{rule_suite_id} | indexed |
| [repos/get-org-ruleset](https://docs.github.com/rest/orgs/rules#get-an-organization-repository-ruleset) | GET | /orgs/{org}/rulesets/{ruleset_id} | indexed |
| [repos/update-org-ruleset](https://docs.github.com/rest/orgs/rules#update-an-organization-repository-ruleset) | PUT | /orgs/{org}/rulesets/{ruleset_id} | indexed |
| [repos/delete-org-ruleset](https://docs.github.com/rest/orgs/rules#delete-an-organization-repository-ruleset) | DELETE | /orgs/{org}/rulesets/{ruleset_id} | indexed |
| [repos/get](https://docs.github.com/rest/repos/repos#get-a-repository) | GET | /repos/{owner}/{repo} | indexed |
| [repos/update](https://docs.github.com/rest/repos/repos#update-a-repository) | PATCH | /repos/{owner}/{repo} | indexed |
| [repos/delete](https://docs.github.com/rest/repos/repos#delete-a-repository) | DELETE | /repos/{owner}/{repo} | indexed |
| [repos/list-activities](https://docs.github.com/rest/repos/repos#list-repository-activities) | GET | /repos/{owner}/{repo}/activity | indexed |
| [repos/create-attestation](https://docs.github.com/rest/repos/attestations#create-an-attestation) | POST | /repos/{owner}/{repo}/attestations | indexed |
| [repos/list-attestations](https://docs.github.com/rest/repos/attestations#list-attestations) | GET | /repos/{owner}/{repo}/attestations/{subject_digest} | indexed |
| [repos/list-autolinks](https://docs.github.com/rest/repos/autolinks#get-all-autolinks-of-a-repository) | GET | /repos/{owner}/{repo}/autolinks | indexed |
| [repos/create-autolink](https://docs.github.com/rest/repos/autolinks#create-an-autolink-reference-for-a-repository) | POST | /repos/{owner}/{repo}/autolinks | indexed |
| [repos/get-autolink](https://docs.github.com/rest/repos/autolinks#get-an-autolink-reference-of-a-repository) | GET | /repos/{owner}/{repo}/autolinks/{autolink_id} | indexed |
| [repos/delete-autolink](https://docs.github.com/rest/repos/autolinks#delete-an-autolink-reference-from-a-repository) | DELETE | /repos/{owner}/{repo}/autolinks/{autolink_id} | indexed |
| [repos/check-automated-security-fixes](https://docs.github.com/rest/repos/repos#check-if-dependabot-security-updates-are-enabled-for-a-repository) | GET | /repos/{owner}/{repo}/automated-security-fixes | indexed |
| [repos/enable-automated-security-fixes](https://docs.github.com/rest/repos/repos#enable-dependabot-security-updates) | PUT | /repos/{owner}/{repo}/automated-security-fixes | indexed |
| [repos/disable-automated-security-fixes](https://docs.github.com/rest/repos/repos#disable-dependabot-security-updates) | DELETE | /repos/{owner}/{repo}/automated-security-fixes | indexed |
| [repos/list-branches](https://docs.github.com/rest/branches/branches#list-branches) | GET | /repos/{owner}/{repo}/branches | indexed |
| [repos/get-branch](https://docs.github.com/rest/branches/branches#get-a-branch) | GET | /repos/{owner}/{repo}/branches/{branch} | indexed |
| [repos/get-branch-protection](https://docs.github.com/rest/branches/branch-protection#get-branch-protection) | GET | /repos/{owner}/{repo}/branches/{branch}/protection | indexed |
| [repos/update-branch-protection](https://docs.github.com/rest/branches/branch-protection#update-branch-protection) | PUT | /repos/{owner}/{repo}/branches/{branch}/protection | indexed |
| [repos/delete-branch-protection](https://docs.github.com/rest/branches/branch-protection#delete-branch-protection) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection | indexed |
| [repos/get-admin-branch-protection](https://docs.github.com/rest/branches/branch-protection#get-admin-branch-protection) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | indexed |
| [repos/set-admin-branch-protection](https://docs.github.com/rest/branches/branch-protection#set-admin-branch-protection) | POST | /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | indexed |
| [repos/delete-admin-branch-protection](https://docs.github.com/rest/branches/branch-protection#delete-admin-branch-protection) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | indexed |
| [repos/get-pull-request-review-protection](https://docs.github.com/rest/branches/branch-protection#get-pull-request-review-protection) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | indexed |
| [repos/update-pull-request-review-protection](https://docs.github.com/rest/branches/branch-protection#update-pull-request-review-protection) | PATCH | /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | indexed |
| [repos/delete-pull-request-review-protection](https://docs.github.com/rest/branches/branch-protection#delete-pull-request-review-protection) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | indexed |
| [repos/get-commit-signature-protection](https://docs.github.com/rest/branches/branch-protection#get-commit-signature-protection) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | indexed |
| [repos/create-commit-signature-protection](https://docs.github.com/rest/branches/branch-protection#create-commit-signature-protection) | POST | /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | indexed |
| [repos/delete-commit-signature-protection](https://docs.github.com/rest/branches/branch-protection#delete-commit-signature-protection) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | indexed |
| [repos/get-status-checks-protection](https://docs.github.com/rest/branches/branch-protection#get-status-checks-protection) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | indexed |
| [repos/update-status-check-protection](https://docs.github.com/rest/branches/branch-protection#update-status-check-protection) | PATCH | /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | indexed |
| [repos/remove-status-check-protection](https://docs.github.com/rest/branches/branch-protection#remove-status-check-protection) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | indexed |
| [repos/get-all-status-check-contexts](https://docs.github.com/rest/branches/branch-protection#get-all-status-check-contexts) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | indexed |
| [repos/add-status-check-contexts](https://docs.github.com/rest/branches/branch-protection#add-status-check-contexts) | POST | /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | indexed |
| [repos/set-status-check-contexts](https://docs.github.com/rest/branches/branch-protection#set-status-check-contexts) | PUT | /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | indexed |
| [repos/remove-status-check-contexts](https://docs.github.com/rest/branches/branch-protection#remove-status-check-contexts) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | indexed |
| [repos/get-access-restrictions](https://docs.github.com/rest/branches/branch-protection#get-access-restrictions) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions | indexed |
| [repos/delete-access-restrictions](https://docs.github.com/rest/branches/branch-protection#delete-access-restrictions) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions | indexed |
| [repos/get-apps-with-access-to-protected-branch](https://docs.github.com/rest/branches/branch-protection#get-apps-with-access-to-the-protected-branch) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | indexed |
| [repos/add-app-access-restrictions](https://docs.github.com/rest/branches/branch-protection#add-app-access-restrictions) | POST | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | indexed |
| [repos/set-app-access-restrictions](https://docs.github.com/rest/branches/branch-protection#set-app-access-restrictions) | PUT | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | indexed |
| [repos/remove-app-access-restrictions](https://docs.github.com/rest/branches/branch-protection#remove-app-access-restrictions) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | indexed |
| [repos/get-teams-with-access-to-protected-branch](https://docs.github.com/rest/branches/branch-protection#get-teams-with-access-to-the-protected-branch) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | indexed |
| [repos/add-team-access-restrictions](https://docs.github.com/rest/branches/branch-protection#add-team-access-restrictions) | POST | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | indexed |
| [repos/set-team-access-restrictions](https://docs.github.com/rest/branches/branch-protection#set-team-access-restrictions) | PUT | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | indexed |
| [repos/remove-team-access-restrictions](https://docs.github.com/rest/branches/branch-protection#remove-team-access-restrictions) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | indexed |
| [repos/get-users-with-access-to-protected-branch](https://docs.github.com/rest/branches/branch-protection#get-users-with-access-to-the-protected-branch) | GET | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | indexed |
| [repos/add-user-access-restrictions](https://docs.github.com/rest/branches/branch-protection#add-user-access-restrictions) | POST | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | indexed |
| [repos/set-user-access-restrictions](https://docs.github.com/rest/branches/branch-protection#set-user-access-restrictions) | PUT | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | indexed |
| [repos/remove-user-access-restrictions](https://docs.github.com/rest/branches/branch-protection#remove-user-access-restrictions) | DELETE | /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | indexed |
| [repos/rename-branch](https://docs.github.com/rest/branches/branches#rename-a-branch) | POST | /repos/{owner}/{repo}/branches/{branch}/rename | indexed |
| [repos/codeowners-errors](https://docs.github.com/rest/repos/repos#list-codeowners-errors) | GET | /repos/{owner}/{repo}/codeowners/errors | indexed |
| [repos/list-collaborators](https://docs.github.com/rest/collaborators/collaborators#list-repository-collaborators) | GET | /repos/{owner}/{repo}/collaborators | indexed |
| [repos/check-collaborator](https://docs.github.com/rest/collaborators/collaborators#check-if-a-user-is-a-repository-collaborator) | GET | /repos/{owner}/{repo}/collaborators/{username} | indexed |
| [repos/add-collaborator](https://docs.github.com/rest/collaborators/collaborators#add-a-repository-collaborator) | PUT | /repos/{owner}/{repo}/collaborators/{username} | indexed |
| [repos/remove-collaborator](https://docs.github.com/rest/collaborators/collaborators#remove-a-repository-collaborator) | DELETE | /repos/{owner}/{repo}/collaborators/{username} | indexed |
| [repos/get-collaborator-permission-level](https://docs.github.com/rest/collaborators/collaborators#get-repository-permissions-for-a-user) | GET | /repos/{owner}/{repo}/collaborators/{username}/permission | indexed |
| [repos/list-commit-comments-for-repo](https://docs.github.com/rest/commits/comments#list-commit-comments-for-a-repository) | GET | /repos/{owner}/{repo}/comments | indexed |
| [repos/get-commit-comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment) | GET | /repos/{owner}/{repo}/comments/{comment_id} | indexed |
| [repos/update-commit-comment](https://docs.github.com/rest/commits/comments#update-a-commit-comment) | PATCH | /repos/{owner}/{repo}/comments/{comment_id} | indexed |
| [repos/delete-commit-comment](https://docs.github.com/rest/commits/comments#delete-a-commit-comment) | DELETE | /repos/{owner}/{repo}/comments/{comment_id} | indexed |
| [repos/list-commits](https://docs.github.com/rest/commits/commits#list-commits) | GET | /repos/{owner}/{repo}/commits | indexed |
| [repos/list-branches-for-head-commit](https://docs.github.com/rest/commits/commits#list-branches-for-head-commit) | GET | /repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head | indexed |
| [repos/list-comments-for-commit](https://docs.github.com/rest/commits/comments#list-commit-comments) | GET | /repos/{owner}/{repo}/commits/{commit_sha}/comments | indexed |
| [repos/create-commit-comment](https://docs.github.com/rest/commits/comments#create-a-commit-comment) | POST | /repos/{owner}/{repo}/commits/{commit_sha}/comments | indexed |
| [repos/list-pull-requests-associated-with-commit](https://docs.github.com/rest/commits/commits#list-pull-requests-associated-with-a-commit) | GET | /repos/{owner}/{repo}/commits/{commit_sha}/pulls | indexed |
| [repos/get-commit](https://docs.github.com/rest/commits/commits#get-a-commit) | GET | /repos/{owner}/{repo}/commits/{ref} | indexed |
| [repos/get-combined-status-for-ref](https://docs.github.com/rest/commits/statuses#get-the-combined-status-for-a-specific-reference) | GET | /repos/{owner}/{repo}/commits/{ref}/status | indexed |
| [repos/list-commit-statuses-for-ref](https://docs.github.com/rest/commits/statuses#list-commit-statuses-for-a-reference) | GET | /repos/{owner}/{repo}/commits/{ref}/statuses | indexed |
| [repos/get-community-profile-metrics](https://docs.github.com/rest/metrics/community#get-community-profile-metrics) | GET | /repos/{owner}/{repo}/community/profile | indexed |
| [repos/compare-commits](https://docs.github.com/rest/commits/commits#compare-two-commits) | GET | /repos/{owner}/{repo}/compare/{basehead} | indexed |
| [repos/get-content](https://docs.github.com/rest/repos/contents#get-repository-content) | GET | /repos/{owner}/{repo}/contents/{path} | indexed |
| [repos/create-or-update-file-contents](https://docs.github.com/rest/repos/contents#create-or-update-file-contents) | PUT | /repos/{owner}/{repo}/contents/{path} | indexed |
| [repos/delete-file](https://docs.github.com/rest/repos/contents#delete-a-file) | DELETE | /repos/{owner}/{repo}/contents/{path} | indexed |
| [repos/list-contributors](https://docs.github.com/rest/repos/repos#list-repository-contributors) | GET | /repos/{owner}/{repo}/contributors | indexed |
| [repos/list-deployments](https://docs.github.com/rest/deployments/deployments#list-deployments) | GET | /repos/{owner}/{repo}/deployments | indexed |
| [repos/create-deployment](https://docs.github.com/rest/deployments/deployments#create-a-deployment) | POST | /repos/{owner}/{repo}/deployments | indexed |
| [repos/get-deployment](https://docs.github.com/rest/deployments/deployments#get-a-deployment) | GET | /repos/{owner}/{repo}/deployments/{deployment_id} | indexed |
| [repos/delete-deployment](https://docs.github.com/rest/deployments/deployments#delete-a-deployment) | DELETE | /repos/{owner}/{repo}/deployments/{deployment_id} | indexed |
| [repos/list-deployment-statuses](https://docs.github.com/rest/deployments/statuses#list-deployment-statuses) | GET | /repos/{owner}/{repo}/deployments/{deployment_id}/statuses | indexed |
| [repos/create-deployment-status](https://docs.github.com/rest/deployments/statuses#create-a-deployment-status) | POST | /repos/{owner}/{repo}/deployments/{deployment_id}/statuses | indexed |
| [repos/get-deployment-status](https://docs.github.com/rest/deployments/statuses#get-a-deployment-status) | GET | /repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id} | indexed |
| [repos/create-dispatch-event](https://docs.github.com/rest/repos/repos#create-a-repository-dispatch-event) | POST | /repos/{owner}/{repo}/dispatches | indexed |
| [repos/get-all-environments](https://docs.github.com/rest/deployments/environments#list-environments) | GET | /repos/{owner}/{repo}/environments | indexed |
| [repos/get-environment](https://docs.github.com/rest/deployments/environments#get-an-environment) | GET | /repos/{owner}/{repo}/environments/{environment_name} | indexed |
| [repos/create-or-update-environment](https://docs.github.com/rest/deployments/environments#create-or-update-an-environment) | PUT | /repos/{owner}/{repo}/environments/{environment_name} | indexed |
| [repos/delete-an-environment](https://docs.github.com/rest/deployments/environments#delete-an-environment) | DELETE | /repos/{owner}/{repo}/environments/{environment_name} | indexed |
| [repos/list-deployment-branch-policies](https://docs.github.com/rest/deployments/branch-policies#list-deployment-branch-policies) | GET | /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | indexed |
| [repos/create-deployment-branch-policy](https://docs.github.com/rest/deployments/branch-policies#create-a-deployment-branch-policy) | POST | /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies | indexed |
| [repos/get-deployment-branch-policy](https://docs.github.com/rest/deployments/branch-policies#get-a-deployment-branch-policy) | GET | /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | indexed |
| [repos/update-deployment-branch-policy](https://docs.github.com/rest/deployments/branch-policies#update-a-deployment-branch-policy) | PUT | /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | indexed |
| [repos/delete-deployment-branch-policy](https://docs.github.com/rest/deployments/branch-policies#delete-a-deployment-branch-policy) | DELETE | /repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id} | indexed |
| [repos/get-all-deployment-protection-rules](https://docs.github.com/rest/deployments/protection-rules#get-all-deployment-protection-rules-for-an-environment) | GET | /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | indexed |
| [repos/create-deployment-protection-rule](https://docs.github.com/rest/deployments/protection-rules#create-a-custom-deployment-protection-rule-on-an-environment) | POST | /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules | indexed |
| [repos/list-custom-deployment-rule-integrations](https://docs.github.com/rest/deployments/protection-rules#list-custom-deployment-rule-integrations-available-for-an-environment) | GET | /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/apps | indexed |
| [repos/get-custom-deployment-protection-rule](https://docs.github.com/rest/deployments/protection-rules#get-a-custom-deployment-protection-rule) | GET | /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | indexed |
| [repos/disable-deployment-protection-rule](https://docs.github.com/rest/deployments/protection-rules#disable-a-custom-protection-rule-for-an-environment) | DELETE | /repos/{owner}/{repo}/environments/{environment_name}/deployment_protection_rules/{protection_rule_id} | indexed |
| [repos/list-forks](https://docs.github.com/rest/repos/forks#list-forks) | GET | /repos/{owner}/{repo}/forks | indexed |
| [repos/create-fork](https://docs.github.com/rest/repos/forks#create-a-fork) | POST | /repos/{owner}/{repo}/forks | indexed |
| [repos/get-hash-algorithm](https://docs.github.com/rest/repos/repos#get-the-hash-algorithm-for-a-repository) | GET | /repos/{owner}/{repo}/hash-algorithm | indexed |
| [repos/list-webhooks](https://docs.github.com/rest/repos/webhooks#list-repository-webhooks) | GET | /repos/{owner}/{repo}/hooks | indexed |
| [repos/create-webhook](https://docs.github.com/rest/repos/webhooks#create-a-repository-webhook) | POST | /repos/{owner}/{repo}/hooks | indexed |
| [repos/get-webhook](https://docs.github.com/rest/repos/webhooks#get-a-repository-webhook) | GET | /repos/{owner}/{repo}/hooks/{hook_id} | indexed |
| [repos/update-webhook](https://docs.github.com/rest/repos/webhooks#update-a-repository-webhook) | PATCH | /repos/{owner}/{repo}/hooks/{hook_id} | indexed |
| [repos/delete-webhook](https://docs.github.com/rest/repos/webhooks#delete-a-repository-webhook) | DELETE | /repos/{owner}/{repo}/hooks/{hook_id} | indexed |
| [repos/get-webhook-config-for-repo](https://docs.github.com/rest/repos/webhooks#get-a-webhook-configuration-for-a-repository) | GET | /repos/{owner}/{repo}/hooks/{hook_id}/config | indexed |
| [repos/update-webhook-config-for-repo](https://docs.github.com/rest/repos/webhooks#update-a-webhook-configuration-for-a-repository) | PATCH | /repos/{owner}/{repo}/hooks/{hook_id}/config | indexed |
| [repos/list-webhook-deliveries](https://docs.github.com/rest/repos/webhooks#list-deliveries-for-a-repository-webhook) | GET | /repos/{owner}/{repo}/hooks/{hook_id}/deliveries | indexed |
| [repos/get-webhook-delivery](https://docs.github.com/rest/repos/webhooks#get-a-delivery-for-a-repository-webhook) | GET | /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id} | indexed |
| [repos/redeliver-webhook-delivery](https://docs.github.com/rest/repos/webhooks#redeliver-a-delivery-for-a-repository-webhook) | POST | /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | indexed |
| [repos/ping-webhook](https://docs.github.com/rest/repos/webhooks#ping-a-repository-webhook) | POST | /repos/{owner}/{repo}/hooks/{hook_id}/pings | indexed |
| [repos/test-push-webhook](https://docs.github.com/rest/repos/webhooks#test-the-push-repository-webhook) | POST | /repos/{owner}/{repo}/hooks/{hook_id}/tests | indexed |
| [repos/check-immutable-releases](https://docs.github.com/rest/repos/repos#check-if-immutable-releases-are-enabled-for-a-repository) | GET | /repos/{owner}/{repo}/immutable-releases | indexed |
| [repos/enable-immutable-releases](https://docs.github.com/rest/repos/repos#enable-immutable-releases) | PUT | /repos/{owner}/{repo}/immutable-releases | indexed |
| [repos/disable-immutable-releases](https://docs.github.com/rest/repos/repos#disable-immutable-releases) | DELETE | /repos/{owner}/{repo}/immutable-releases | indexed |
| [repos/list-invitations](https://docs.github.com/rest/collaborators/invitations#list-repository-invitations) | GET | /repos/{owner}/{repo}/invitations | indexed |
| [repos/update-invitation](https://docs.github.com/rest/collaborators/invitations#update-a-repository-invitation) | PATCH | /repos/{owner}/{repo}/invitations/{invitation_id} | indexed |
| [repos/delete-invitation](https://docs.github.com/rest/collaborators/invitations#delete-a-repository-invitation) | DELETE | /repos/{owner}/{repo}/invitations/{invitation_id} | indexed |
| [repos/list-issue-types](https://docs.github.com/rest/repos/issue-types#list-issue-types-for-a-repository) | GET | /repos/{owner}/{repo}/issue-types | indexed |
| [repos/list-deploy-keys](https://docs.github.com/rest/deploy-keys/deploy-keys#list-deploy-keys) | GET | /repos/{owner}/{repo}/keys | indexed |
| [repos/create-deploy-key](https://docs.github.com/rest/deploy-keys/deploy-keys#create-a-deploy-key) | POST | /repos/{owner}/{repo}/keys | indexed |
| [repos/get-deploy-key](https://docs.github.com/rest/deploy-keys/deploy-keys#get-a-deploy-key) | GET | /repos/{owner}/{repo}/keys/{key_id} | indexed |
| [repos/delete-deploy-key](https://docs.github.com/rest/deploy-keys/deploy-keys#delete-a-deploy-key) | DELETE | /repos/{owner}/{repo}/keys/{key_id} | indexed |
| [repos/list-languages](https://docs.github.com/rest/repos/repos#list-repository-languages) | GET | /repos/{owner}/{repo}/languages | indexed |
| [repos/merge-upstream](https://docs.github.com/rest/branches/branches#sync-a-fork-branch-with-the-upstream-repository) | POST | /repos/{owner}/{repo}/merge-upstream | indexed |
| [repos/merge](https://docs.github.com/rest/branches/branches#merge-a-branch) | POST | /repos/{owner}/{repo}/merges | indexed |
| [repos/get-pages](https://docs.github.com/rest/pages/pages#get-a-apiname-pages-site) | GET | /repos/{owner}/{repo}/pages | indexed |
| [repos/create-pages-site](https://docs.github.com/rest/pages/pages#create-a-apiname-pages-site) | POST | /repos/{owner}/{repo}/pages | indexed |
| [repos/update-information-about-pages-site](https://docs.github.com/rest/pages/pages#update-information-about-a-apiname-pages-site) | PUT | /repos/{owner}/{repo}/pages | indexed |
| [repos/delete-pages-site](https://docs.github.com/rest/pages/pages#delete-a-apiname-pages-site) | DELETE | /repos/{owner}/{repo}/pages | indexed |
| [repos/list-pages-builds](https://docs.github.com/rest/pages/pages#list-apiname-pages-builds) | GET | /repos/{owner}/{repo}/pages/builds | indexed |
| [repos/request-pages-build](https://docs.github.com/rest/pages/pages#request-a-apiname-pages-build) | POST | /repos/{owner}/{repo}/pages/builds | indexed |
| [repos/get-latest-pages-build](https://docs.github.com/rest/pages/pages#get-latest-pages-build) | GET | /repos/{owner}/{repo}/pages/builds/latest | indexed |
| [repos/get-pages-build](https://docs.github.com/rest/pages/pages#get-apiname-pages-build) | GET | /repos/{owner}/{repo}/pages/builds/{build_id} | indexed |
| [repos/create-pages-deployment](https://docs.github.com/rest/pages/pages#create-a-github-pages-deployment) | POST | /repos/{owner}/{repo}/pages/deployments | indexed |
| [repos/get-pages-deployment](https://docs.github.com/rest/pages/pages#get-the-status-of-a-github-pages-deployment) | GET | /repos/{owner}/{repo}/pages/deployments/{pages_deployment_id} | indexed |
| [repos/cancel-pages-deployment](https://docs.github.com/rest/pages/pages#cancel-a-github-pages-deployment) | POST | /repos/{owner}/{repo}/pages/deployments/{pages_deployment_id}/cancel | indexed |
| [repos/get-pages-health-check](https://docs.github.com/rest/pages/pages#get-a-dns-health-check-for-github-pages) | GET | /repos/{owner}/{repo}/pages/health | indexed |
| [repos/list-planning-statuses](https://docs.github.com/rest/repos/planning-statuses#list-planning-statuses-for-a-repository) | GET | /repos/{owner}/{repo}/planning-statuses | indexed |
| [repos/check-private-vulnerability-reporting](https://docs.github.com/rest/repos/repos#check-if-private-vulnerability-reporting-is-enabled-for-a-repository) | GET | /repos/{owner}/{repo}/private-vulnerability-reporting | indexed |
| [repos/enable-private-vulnerability-reporting](https://docs.github.com/rest/repos/repos#enable-private-vulnerability-reporting-for-a-repository) | PUT | /repos/{owner}/{repo}/private-vulnerability-reporting | indexed |
| [repos/disable-private-vulnerability-reporting](https://docs.github.com/rest/repos/repos#disable-private-vulnerability-reporting-for-a-repository) | DELETE | /repos/{owner}/{repo}/private-vulnerability-reporting | indexed |
| [repos/custom-properties-for-repos-get-repository-values](https://docs.github.com/rest/repos/custom-properties#get-all-custom-property-values-for-a-repository) | GET | /repos/{owner}/{repo}/properties/values | indexed |
| [repos/custom-properties-for-repos-create-or-update-repository-values](https://docs.github.com/rest/repos/custom-properties#create-or-update-custom-property-values-for-a-repository) | PATCH | /repos/{owner}/{repo}/properties/values | indexed |
| [repos/get-readme](https://docs.github.com/rest/repos/contents#get-a-repository-readme) | GET | /repos/{owner}/{repo}/readme | indexed |
| [repos/get-readme-in-directory](https://docs.github.com/rest/repos/contents#get-a-repository-readme-for-a-directory) | GET | /repos/{owner}/{repo}/readme/{dir} | indexed |
| [repos/list-releases](https://docs.github.com/rest/releases/releases#list-releases) | GET | /repos/{owner}/{repo}/releases | indexed |
| [repos/create-release](https://docs.github.com/rest/releases/releases#create-a-release) | POST | /repos/{owner}/{repo}/releases | indexed |
| [repos/get-release-asset](https://docs.github.com/rest/releases/assets#get-a-release-asset) | GET | /repos/{owner}/{repo}/releases/assets/{asset_id} | indexed |
| [repos/update-release-asset](https://docs.github.com/rest/releases/assets#update-a-release-asset) | PATCH | /repos/{owner}/{repo}/releases/assets/{asset_id} | indexed |
| [repos/delete-release-asset](https://docs.github.com/rest/releases/assets#delete-a-release-asset) | DELETE | /repos/{owner}/{repo}/releases/assets/{asset_id} | indexed |
| [repos/generate-release-notes](https://docs.github.com/rest/releases/releases#generate-release-notes-content-for-a-release) | POST | /repos/{owner}/{repo}/releases/generate-notes | indexed |
| [repos/get-latest-release](https://docs.github.com/rest/releases/releases#get-the-latest-release) | GET | /repos/{owner}/{repo}/releases/latest | indexed |
| [repos/get-release-by-tag](https://docs.github.com/rest/releases/releases#get-a-release-by-tag-name) | GET | /repos/{owner}/{repo}/releases/tags/{tag} | indexed |
| [repos/get-release](https://docs.github.com/rest/releases/releases#get-a-release) | GET | /repos/{owner}/{repo}/releases/{release_id} | indexed |
| [repos/update-release](https://docs.github.com/rest/releases/releases#update-a-release) | PATCH | /repos/{owner}/{repo}/releases/{release_id} | indexed |
| [repos/delete-release](https://docs.github.com/rest/releases/releases#delete-a-release) | DELETE | /repos/{owner}/{repo}/releases/{release_id} | indexed |
| [repos/list-release-assets](https://docs.github.com/rest/releases/assets#list-release-assets) | GET | /repos/{owner}/{repo}/releases/{release_id}/assets | indexed |
| [repos/upload-release-asset](https://docs.github.com/rest/releases/assets#upload-a-release-asset) | POST | /repos/{owner}/{repo}/releases/{release_id}/assets | indexed |
| [repos/get-branch-rules](https://docs.github.com/rest/repos/rules#get-rules-for-a-branch) | GET | /repos/{owner}/{repo}/rules/branches/{branch} | indexed |
| [repos/get-repo-rulesets](https://docs.github.com/rest/repos/rules#get-all-repository-rulesets) | GET | /repos/{owner}/{repo}/rulesets | indexed |
| [repos/create-repo-ruleset](https://docs.github.com/rest/repos/rules#create-a-repository-ruleset) | POST | /repos/{owner}/{repo}/rulesets | indexed |
| [repos/get-repo-rule-suites](https://docs.github.com/rest/repos/rule-suites#list-repository-rule-suites) | GET | /repos/{owner}/{repo}/rulesets/rule-suites | indexed |
| [repos/get-repo-rule-suite](https://docs.github.com/rest/repos/rule-suites#get-a-repository-rule-suite) | GET | /repos/{owner}/{repo}/rulesets/rule-suites/{rule_suite_id} | indexed |
| [repos/get-repo-ruleset](https://docs.github.com/rest/repos/rules#get-a-repository-ruleset) | GET | /repos/{owner}/{repo}/rulesets/{ruleset_id} | indexed |
| [repos/update-repo-ruleset](https://docs.github.com/rest/repos/rules#update-a-repository-ruleset) | PUT | /repos/{owner}/{repo}/rulesets/{ruleset_id} | indexed |
| [repos/delete-repo-ruleset](https://docs.github.com/rest/repos/rules#delete-a-repository-ruleset) | DELETE | /repos/{owner}/{repo}/rulesets/{ruleset_id} | indexed |
| [repos/get-repo-ruleset-history](https://docs.github.com/rest/repos/rules#get-repository-ruleset-history) | GET | /repos/{owner}/{repo}/rulesets/{ruleset_id}/history | indexed |
| [repos/get-repo-ruleset-version](https://docs.github.com/rest/repos/rules#get-repository-ruleset-version) | GET | /repos/{owner}/{repo}/rulesets/{ruleset_id}/history/{version_id} | indexed |
| [repos/get-code-frequency-stats](https://docs.github.com/rest/metrics/statistics#get-the-weekly-commit-activity) | GET | /repos/{owner}/{repo}/stats/code_frequency | indexed |
| [repos/get-commit-activity-stats](https://docs.github.com/rest/metrics/statistics#get-the-last-year-of-commit-activity) | GET | /repos/{owner}/{repo}/stats/commit_activity | indexed |
| [repos/get-contributors-stats](https://docs.github.com/rest/metrics/statistics#get-all-contributor-commit-activity) | GET | /repos/{owner}/{repo}/stats/contributors | indexed |
| [repos/get-participation-stats](https://docs.github.com/rest/metrics/statistics#get-the-weekly-commit-count) | GET | /repos/{owner}/{repo}/stats/participation | indexed |
| [repos/get-punch-card-stats](https://docs.github.com/rest/metrics/statistics#get-the-hourly-commit-count-for-each-day) | GET | /repos/{owner}/{repo}/stats/punch_card | indexed |
| [repos/create-commit-status](https://docs.github.com/rest/commits/statuses#create-a-commit-status) | POST | /repos/{owner}/{repo}/statuses/{sha} | indexed |
| [repos/list-tags](https://docs.github.com/rest/repos/repos#list-repository-tags) | GET | /repos/{owner}/{repo}/tags | indexed |
| [repos/download-tarball-archive](https://docs.github.com/rest/repos/contents#download-a-repository-archive-tar) | GET | /repos/{owner}/{repo}/tarball/{ref} | indexed |
| [repos/list-teams](https://docs.github.com/rest/repos/repos#list-repository-teams) | GET | /repos/{owner}/{repo}/teams | indexed |
| [repos/get-all-topics](https://docs.github.com/rest/repos/repos#get-all-repository-topics) | GET | /repos/{owner}/{repo}/topics | indexed |
| [repos/replace-all-topics](https://docs.github.com/rest/repos/repos#replace-all-repository-topics) | PUT | /repos/{owner}/{repo}/topics | indexed |
| [repos/get-clones](https://docs.github.com/rest/metrics/traffic#get-repository-clones) | GET | /repos/{owner}/{repo}/traffic/clones | indexed |
| [repos/get-top-paths](https://docs.github.com/rest/metrics/traffic#get-top-referral-paths) | GET | /repos/{owner}/{repo}/traffic/popular/paths | indexed |
| [repos/get-top-referrers](https://docs.github.com/rest/metrics/traffic#get-top-referral-sources) | GET | /repos/{owner}/{repo}/traffic/popular/referrers | indexed |
| [repos/get-views](https://docs.github.com/rest/metrics/traffic#get-page-views) | GET | /repos/{owner}/{repo}/traffic/views | indexed |
| [repos/transfer](https://docs.github.com/rest/repos/repos#transfer-a-repository) | POST | /repos/{owner}/{repo}/transfer | indexed |
| [repos/check-vulnerability-alerts](https://docs.github.com/rest/repos/repos#check-if-vulnerability-alerts-are-enabled-for-a-repository) | GET | /repos/{owner}/{repo}/vulnerability-alerts | indexed |
| [repos/enable-vulnerability-alerts](https://docs.github.com/rest/repos/repos#enable-vulnerability-alerts) | PUT | /repos/{owner}/{repo}/vulnerability-alerts | indexed |
| [repos/disable-vulnerability-alerts](https://docs.github.com/rest/repos/repos#disable-vulnerability-alerts) | DELETE | /repos/{owner}/{repo}/vulnerability-alerts | indexed |
| [repos/download-zipball-archive](https://docs.github.com/rest/repos/contents#download-a-repository-archive-zip) | GET | /repos/{owner}/{repo}/zipball/{ref} | indexed |
| [repos/create-using-template](https://docs.github.com/rest/repos/repos#create-a-repository-using-a-template) | POST | /repos/{template_owner}/{template_repo}/generate | indexed |
| [repos/list-public](https://docs.github.com/rest/repos/repos#list-public-repositories) | GET | /repositories | indexed |
| [repos/list-for-authenticated-user](https://docs.github.com/rest/repos/repos#list-repositories-for-the-authenticated-user) | GET | /user/repos | indexed |
| [repos/create-for-authenticated-user](https://docs.github.com/rest/repos/repos#create-a-repository-for-the-authenticated-user) | POST | /user/repos | indexed |
| [repos/list-invitations-for-authenticated-user](https://docs.github.com/rest/collaborators/invitations#list-repository-invitations-for-the-authenticated-user) | GET | /user/repository_invitations | indexed |
| [repos/accept-invitation-for-authenticated-user](https://docs.github.com/rest/collaborators/invitations#accept-a-repository-invitation) | PATCH | /user/repository_invitations/{invitation_id} | indexed |
| [repos/decline-invitation-for-authenticated-user](https://docs.github.com/rest/collaborators/invitations#decline-a-repository-invitation) | DELETE | /user/repository_invitations/{invitation_id} | indexed |
| [repos/list-for-user](https://docs.github.com/rest/repos/repos#list-repositories-for-a-user) | GET | /users/{username}/repos | indexed |

## REST search

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [search/code](https://docs.github.com/rest/search/search#search-code) | GET | /search/code | indexed |
| [search/commits](https://docs.github.com/rest/search/search#search-commits) | GET | /search/commits | indexed |
| [search/issues-and-pull-requests](https://docs.github.com/rest/search/search#search-issues-and-pull-requests) | GET | /search/issues | indexed |
| [search/labels](https://docs.github.com/rest/search/search#search-labels) | GET | /search/labels | indexed |
| [search/repos](https://docs.github.com/rest/search/search#search-repositories) | GET | /search/repositories | indexed |
| [search/topics](https://docs.github.com/rest/search/search#search-topics) | GET | /search/topics | indexed |
| [search/users](https://docs.github.com/rest/search/search#search-users) | GET | /search/users | indexed |

## REST secret-scanning

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [secret-scanning/list-alerts-for-org](https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-an-organization) | GET | /orgs/{org}/secret-scanning/alerts | indexed |
| [secret-scanning/list-org-custom-patterns](https://docs.github.com/rest/secret-scanning/custom-patterns#list-organization-custom-patterns) | GET | /orgs/{org}/secret-scanning/custom-patterns | indexed |
| [secret-scanning/bulk-create-org-custom-patterns](https://docs.github.com/rest/secret-scanning/custom-patterns#bulk-create-organization-custom-patterns) | POST | /orgs/{org}/secret-scanning/custom-patterns | indexed |
| [secret-scanning/bulk-delete-org-custom-patterns](https://docs.github.com/rest/secret-scanning/custom-patterns#bulk-delete-organization-custom-patterns) | DELETE | /orgs/{org}/secret-scanning/custom-patterns | indexed |
| [secret-scanning/update-org-custom-pattern](https://docs.github.com/rest/secret-scanning/custom-patterns#update-an-organization-custom-pattern) | PATCH | /orgs/{org}/secret-scanning/custom-patterns/{pattern_id} | indexed |
| [secret-scanning/list-org-pattern-configs](https://docs.github.com/rest/secret-scanning/push-protection#list-organization-pattern-configurations) | GET | /orgs/{org}/secret-scanning/pattern-configurations | indexed |
| [secret-scanning/update-org-pattern-configs](https://docs.github.com/rest/secret-scanning/push-protection#update-organization-pattern-configurations) | PATCH | /orgs/{org}/secret-scanning/pattern-configurations | indexed |
| [secret-scanning/list-alerts-for-repo](https://docs.github.com/rest/secret-scanning/secret-scanning#list-secret-scanning-alerts-for-a-repository) | GET | /repos/{owner}/{repo}/secret-scanning/alerts | indexed |
| [secret-scanning/get-alert](https://docs.github.com/rest/secret-scanning/secret-scanning#get-a-secret-scanning-alert) | GET | /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | indexed |
| [secret-scanning/update-alert](https://docs.github.com/rest/secret-scanning/secret-scanning#update-a-secret-scanning-alert) | PATCH | /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | indexed |
| [secret-scanning/list-locations-for-alert](https://docs.github.com/rest/secret-scanning/secret-scanning#list-locations-for-a-secret-scanning-alert) | GET | /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations | indexed |
| [secret-scanning/list-repo-custom-patterns](https://docs.github.com/rest/secret-scanning/custom-patterns#list-repository-custom-patterns) | GET | /repos/{owner}/{repo}/secret-scanning/custom-patterns | indexed |
| [secret-scanning/bulk-create-repo-custom-patterns](https://docs.github.com/rest/secret-scanning/custom-patterns#bulk-create-repository-custom-patterns) | POST | /repos/{owner}/{repo}/secret-scanning/custom-patterns | indexed |
| [secret-scanning/bulk-delete-repo-custom-patterns](https://docs.github.com/rest/secret-scanning/custom-patterns#bulk-delete-repository-custom-patterns) | DELETE | /repos/{owner}/{repo}/secret-scanning/custom-patterns | indexed |
| [secret-scanning/update-repo-custom-pattern](https://docs.github.com/rest/secret-scanning/custom-patterns#update-a-repository-custom-pattern) | PATCH | /repos/{owner}/{repo}/secret-scanning/custom-patterns/{pattern_id} | indexed |
| [secret-scanning/create-push-protection-bypass](https://docs.github.com/rest/secret-scanning/secret-scanning#create-a-push-protection-bypass) | POST | /repos/{owner}/{repo}/secret-scanning/push-protection-bypasses | indexed |
| [secret-scanning/get-scan-history](https://docs.github.com/rest/secret-scanning/secret-scanning#get-secret-scanning-scan-history-for-a-repository) | GET | /repos/{owner}/{repo}/secret-scanning/scan-history | indexed |

## REST security-advisories

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [security-advisories/list-global-advisories](https://docs.github.com/rest/security-advisories/global-advisories#list-global-security-advisories) | GET | /advisories | indexed |
| [security-advisories/get-global-advisory](https://docs.github.com/rest/security-advisories/global-advisories#get-a-global-security-advisory) | GET | /advisories/{ghsa_id} | indexed |
| [security-advisories/list-org-repository-advisories](https://docs.github.com/rest/security-advisories/repository-advisories#list-repository-security-advisories-for-an-organization) | GET | /orgs/{org}/security-advisories | indexed |
| [security-advisories/list-repository-advisories](https://docs.github.com/rest/security-advisories/repository-advisories#list-repository-security-advisories) | GET | /repos/{owner}/{repo}/security-advisories | indexed |
| [security-advisories/create-repository-advisory](https://docs.github.com/rest/security-advisories/repository-advisories#create-a-repository-security-advisory) | POST | /repos/{owner}/{repo}/security-advisories | indexed |
| [security-advisories/create-private-vulnerability-report](https://docs.github.com/rest/security-advisories/repository-advisories#privately-report-a-security-vulnerability) | POST | /repos/{owner}/{repo}/security-advisories/reports | indexed |
| [security-advisories/get-repository-advisory](https://docs.github.com/rest/security-advisories/repository-advisories#get-a-repository-security-advisory) | GET | /repos/{owner}/{repo}/security-advisories/{ghsa_id} | indexed |
| [security-advisories/update-repository-advisory](https://docs.github.com/rest/security-advisories/repository-advisories#update-a-repository-security-advisory) | PATCH | /repos/{owner}/{repo}/security-advisories/{ghsa_id} | indexed |
| [security-advisories/list-repository-advisory-comments](https://docs.github.com/rest/security-advisories/repository-advisories#list-repository-security-advisory-comments) | GET | /repos/{owner}/{repo}/security-advisories/{ghsa_id}/comments | indexed |
| [security-advisories/create-repository-advisory-comment](https://docs.github.com/rest/security-advisories/repository-advisories#create-a-repository-advisory-comment) | POST | /repos/{owner}/{repo}/security-advisories/{ghsa_id}/comments | indexed |
| [security-advisories/get-repository-advisory-comment](https://docs.github.com/rest/security-advisories/repository-advisories#get-a-repository-advisory-comment) | GET | /repos/{owner}/{repo}/security-advisories/{ghsa_id}/comments/{comment_id} | indexed |
| [security-advisories/update-repository-advisory-comment](https://docs.github.com/rest/security-advisories/repository-advisories#update-a-repository-advisory-comment) | PATCH | /repos/{owner}/{repo}/security-advisories/{ghsa_id}/comments/{comment_id} | indexed |
| [security-advisories/create-repository-advisory-cve-request](https://docs.github.com/rest/security-advisories/repository-advisories#request-a-cve-for-a-repository-security-advisory) | POST | /repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve | indexed |
| [security-advisories/create-fork](https://docs.github.com/rest/security-advisories/repository-advisories#create-a-temporary-private-fork) | POST | /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks | indexed |

## REST teams

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [teams/list](https://docs.github.com/rest/teams/teams#list-teams) | GET | /orgs/{org}/teams | indexed |
| [teams/create](https://docs.github.com/rest/teams/teams#create-a-team) | POST | /orgs/{org}/teams | indexed |
| [teams/get-by-name](https://docs.github.com/rest/teams/teams#get-a-team-by-name) | GET | /orgs/{org}/teams/{team_slug} | indexed |
| [teams/update-in-org](https://docs.github.com/rest/teams/teams#update-a-team) | PATCH | /orgs/{org}/teams/{team_slug} | indexed |
| [teams/delete-in-org](https://docs.github.com/rest/teams/teams#delete-a-team) | DELETE | /orgs/{org}/teams/{team_slug} | indexed |
| [teams/list-pending-invitations-in-org](https://docs.github.com/rest/teams/members#list-pending-team-invitations) | GET | /orgs/{org}/teams/{team_slug}/invitations | indexed |
| [teams/list-members-in-org](https://docs.github.com/rest/teams/members#list-team-members) | GET | /orgs/{org}/teams/{team_slug}/members | indexed |
| [teams/get-membership-for-user-in-org](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user) | GET | /orgs/{org}/teams/{team_slug}/memberships/{username} | indexed |
| [teams/add-or-update-membership-for-user-in-org](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user) | PUT | /orgs/{org}/teams/{team_slug}/memberships/{username} | indexed |
| [teams/remove-membership-for-user-in-org](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user) | DELETE | /orgs/{org}/teams/{team_slug}/memberships/{username} | indexed |
| [teams/list-repos-in-org](https://docs.github.com/rest/teams/teams#list-team-repositories) | GET | /orgs/{org}/teams/{team_slug}/repos | indexed |
| [teams/check-permissions-for-repo-in-org](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository) | GET | /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | indexed |
| [teams/add-or-update-repo-permissions-in-org](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions) | PUT | /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | indexed |
| [teams/remove-repo-in-org](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team) | DELETE | /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | indexed |
| [teams/list-child-in-org](https://docs.github.com/rest/teams/teams#list-child-teams) | GET | /orgs/{org}/teams/{team_slug}/teams | indexed |
| [teams/get-legacy](https://docs.github.com/rest/teams/teams#get-a-team-legacy) | GET | /teams/{team_id} | deprecated |
| [teams/update-legacy](https://docs.github.com/rest/teams/teams#update-a-team-legacy) | PATCH | /teams/{team_id} | deprecated |
| [teams/delete-legacy](https://docs.github.com/rest/teams/teams#delete-a-team-legacy) | DELETE | /teams/{team_id} | deprecated |
| [teams/list-pending-invitations-legacy](https://docs.github.com/rest/teams/members#list-pending-team-invitations-legacy) | GET | /teams/{team_id}/invitations | deprecated |
| [teams/list-members-legacy](https://docs.github.com/rest/teams/members#list-team-members-legacy) | GET | /teams/{team_id}/members | deprecated |
| [teams/get-member-legacy](https://docs.github.com/rest/teams/members#get-team-member-legacy) | GET | /teams/{team_id}/members/{username} | deprecated |
| [teams/add-member-legacy](https://docs.github.com/rest/teams/members#add-team-member-legacy) | PUT | /teams/{team_id}/members/{username} | deprecated |
| [teams/remove-member-legacy](https://docs.github.com/rest/teams/members#remove-team-member-legacy) | DELETE | /teams/{team_id}/members/{username} | deprecated |
| [teams/get-membership-for-user-legacy](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user-legacy) | GET | /teams/{team_id}/memberships/{username} | deprecated |
| [teams/add-or-update-membership-for-user-legacy](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user-legacy) | PUT | /teams/{team_id}/memberships/{username} | deprecated |
| [teams/remove-membership-for-user-legacy](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user-legacy) | DELETE | /teams/{team_id}/memberships/{username} | deprecated |
| [teams/list-repos-legacy](https://docs.github.com/rest/teams/teams#list-team-repositories-legacy) | GET | /teams/{team_id}/repos | deprecated |
| [teams/check-permissions-for-repo-legacy](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository-legacy) | GET | /teams/{team_id}/repos/{owner}/{repo} | deprecated |
| [teams/add-or-update-repo-permissions-legacy](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions-legacy) | PUT | /teams/{team_id}/repos/{owner}/{repo} | deprecated |
| [teams/remove-repo-legacy](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team-legacy) | DELETE | /teams/{team_id}/repos/{owner}/{repo} | deprecated |
| [teams/list-child-legacy](https://docs.github.com/rest/teams/teams#list-child-teams-legacy) | GET | /teams/{team_id}/teams | deprecated |
| [teams/list-for-authenticated-user](https://docs.github.com/rest/teams/teams#list-teams-for-the-authenticated-user) | GET | /user/teams | indexed |

## REST users

| Operation | Method | Route | Availability |
| --- | --- | --- | --- |
| [users/get-authenticated](https://docs.github.com/rest/users/users#get-the-authenticated-user) | GET | /user | indexed |
| [users/update-authenticated](https://docs.github.com/rest/users/users#update-the-authenticated-user) | PATCH | /user | indexed |
| [users/list-blocked-by-authenticated-user](https://docs.github.com/rest/users/blocking#list-users-blocked-by-the-authenticated-user) | GET | /user/blocks | indexed |
| [users/check-blocked](https://docs.github.com/rest/users/blocking#check-if-a-user-is-blocked-by-the-authenticated-user) | GET | /user/blocks/{username} | indexed |
| [users/block](https://docs.github.com/rest/users/blocking#block-a-user) | PUT | /user/blocks/{username} | indexed |
| [users/unblock](https://docs.github.com/rest/users/blocking#unblock-a-user) | DELETE | /user/blocks/{username} | indexed |
| [users/set-primary-email-visibility-for-authenticated-user](https://docs.github.com/rest/users/emails#set-primary-email-visibility-for-the-authenticated-user) | PATCH | /user/email/visibility | indexed |
| [users/list-emails-for-authenticated-user](https://docs.github.com/rest/users/emails#list-email-addresses-for-the-authenticated-user) | GET | /user/emails | indexed |
| [users/add-email-for-authenticated-user](https://docs.github.com/rest/users/emails#add-an-email-address-for-the-authenticated-user) | POST | /user/emails | indexed |
| [users/delete-email-for-authenticated-user](https://docs.github.com/rest/users/emails#delete-an-email-address-for-the-authenticated-user) | DELETE | /user/emails | indexed |
| [users/list-followers-for-authenticated-user](https://docs.github.com/rest/users/followers#list-followers-of-the-authenticated-user) | GET | /user/followers | indexed |
| [users/list-followed-by-authenticated-user](https://docs.github.com/rest/users/followers#list-the-people-the-authenticated-user-follows) | GET | /user/following | indexed |
| [users/check-person-is-followed-by-authenticated](https://docs.github.com/rest/users/followers#check-if-a-person-is-followed-by-the-authenticated-user) | GET | /user/following/{username} | indexed |
| [users/follow](https://docs.github.com/rest/users/followers#follow-a-user) | PUT | /user/following/{username} | indexed |
| [users/unfollow](https://docs.github.com/rest/users/followers#unfollow-a-user) | DELETE | /user/following/{username} | indexed |
| [users/list-gpg-keys-for-authenticated-user](https://docs.github.com/rest/users/gpg-keys#list-gpg-keys-for-the-authenticated-user) | GET | /user/gpg_keys | indexed |
| [users/create-gpg-key-for-authenticated-user](https://docs.github.com/rest/users/gpg-keys#create-a-gpg-key-for-the-authenticated-user) | POST | /user/gpg_keys | indexed |
| [users/get-gpg-key-for-authenticated-user](https://docs.github.com/rest/users/gpg-keys#get-a-gpg-key-for-the-authenticated-user) | GET | /user/gpg_keys/{gpg_key_id} | indexed |
| [users/delete-gpg-key-for-authenticated-user](https://docs.github.com/rest/users/gpg-keys#delete-a-gpg-key-for-the-authenticated-user) | DELETE | /user/gpg_keys/{gpg_key_id} | indexed |
| [users/list-issue-fields-for-authenticated-user](https://docs.github.com/rest/users/issue-fields#list-issue-fields) | GET | /user/issue-fields | indexed |
| [users/create-issue-field-for-authenticated-user](https://docs.github.com/rest/users/issue-fields#create-an-issue-field) | POST | /user/issue-fields | indexed |
| [users/update-issue-field-for-authenticated-user](https://docs.github.com/rest/users/issue-fields#update-an-issue-field) | PATCH | /user/issue-fields/{issue_field_id} | indexed |
| [users/delete-issue-field-for-authenticated-user](https://docs.github.com/rest/users/issue-fields#delete-an-issue-field) | DELETE | /user/issue-fields/{issue_field_id} | indexed |
| [users/list-issue-types-for-authenticated-user](https://docs.github.com/rest/users/issue-types#list-issue-types) | GET | /user/issue-types | indexed |
| [users/create-issue-type-for-authenticated-user](https://docs.github.com/rest/users/issue-types#create-an-issue-type) | POST | /user/issue-types | indexed |
| [users/update-issue-type-for-authenticated-user](https://docs.github.com/rest/users/issue-types#update-an-issue-type) | PUT | /user/issue-types/{issue_type_id} | indexed |
| [users/delete-issue-type-for-authenticated-user](https://docs.github.com/rest/users/issue-types#delete-an-issue-type) | DELETE | /user/issue-types/{issue_type_id} | indexed |
| [users/list-public-ssh-keys-for-authenticated-user](https://docs.github.com/rest/users/keys#list-public-ssh-keys-for-the-authenticated-user) | GET | /user/keys | indexed |
| [users/create-public-ssh-key-for-authenticated-user](https://docs.github.com/rest/users/keys#create-a-public-ssh-key-for-the-authenticated-user) | POST | /user/keys | indexed |
| [users/get-public-ssh-key-for-authenticated-user](https://docs.github.com/rest/users/keys#get-a-public-ssh-key-for-the-authenticated-user) | GET | /user/keys/{key_id} | indexed |
| [users/delete-public-ssh-key-for-authenticated-user](https://docs.github.com/rest/users/keys#delete-a-public-ssh-key-for-the-authenticated-user) | DELETE | /user/keys/{key_id} | indexed |
| [users/list-public-emails-for-authenticated-user](https://docs.github.com/rest/users/emails#list-public-email-addresses-for-the-authenticated-user) | GET | /user/public_emails | indexed |
| [users/list-social-accounts-for-authenticated-user](https://docs.github.com/rest/users/social-accounts#list-social-accounts-for-the-authenticated-user) | GET | /user/social_accounts | indexed |
| [users/add-social-account-for-authenticated-user](https://docs.github.com/rest/users/social-accounts#add-social-accounts-for-the-authenticated-user) | POST | /user/social_accounts | indexed |
| [users/delete-social-account-for-authenticated-user](https://docs.github.com/rest/users/social-accounts#delete-social-accounts-for-the-authenticated-user) | DELETE | /user/social_accounts | indexed |
| [users/list-ssh-signing-keys-for-authenticated-user](https://docs.github.com/rest/users/ssh-signing-keys#list-ssh-signing-keys-for-the-authenticated-user) | GET | /user/ssh_signing_keys | indexed |
| [users/create-ssh-signing-key-for-authenticated-user](https://docs.github.com/rest/users/ssh-signing-keys#create-a-ssh-signing-key-for-the-authenticated-user) | POST | /user/ssh_signing_keys | indexed |
| [users/get-ssh-signing-key-for-authenticated-user](https://docs.github.com/rest/users/ssh-signing-keys#get-an-ssh-signing-key-for-the-authenticated-user) | GET | /user/ssh_signing_keys/{ssh_signing_key_id} | indexed |
| [users/delete-ssh-signing-key-for-authenticated-user](https://docs.github.com/rest/users/ssh-signing-keys#delete-an-ssh-signing-key-for-the-authenticated-user) | DELETE | /user/ssh_signing_keys/{ssh_signing_key_id} | indexed |
| [users/get-by-id](https://docs.github.com/rest/users/users#get-a-user-using-their-id) | GET | /user/{account_id} | indexed |
| [users/list](https://docs.github.com/rest/users/users#list-users) | GET | /users | indexed |
| [users/get-by-username](https://docs.github.com/rest/users/users#get-a-user) | GET | /users/{username} | indexed |
| [users/list-attestations-bulk](https://docs.github.com/rest/users/attestations#list-attestations-by-bulk-subject-digests) | POST | /users/{username}/attestations/bulk-list | indexed |
| [users/delete-attestations-bulk](https://docs.github.com/rest/users/attestations#delete-attestations-in-bulk) | POST | /users/{username}/attestations/delete-request | indexed |
| [users/delete-attestations-by-subject-digest](https://docs.github.com/rest/users/attestations#delete-attestations-by-subject-digest) | DELETE | /users/{username}/attestations/digest/{subject_digest} | indexed |
| [users/delete-attestations-by-id](https://docs.github.com/rest/users/attestations#delete-attestations-by-id) | DELETE | /users/{username}/attestations/{attestation_id} | indexed |
| [users/list-attestations](https://docs.github.com/rest/users/attestations#list-attestations) | GET | /users/{username}/attestations/{subject_digest} | indexed |
| [users/list-followers-for-user](https://docs.github.com/rest/users/followers#list-followers-of-a-user) | GET | /users/{username}/followers | indexed |
| [users/list-following-for-user](https://docs.github.com/rest/users/followers#list-the-people-a-user-follows) | GET | /users/{username}/following | indexed |
| [users/check-following-for-user](https://docs.github.com/rest/users/followers#check-if-a-user-follows-another-user) | GET | /users/{username}/following/{target_user} | indexed |
| [users/list-gpg-keys-for-user](https://docs.github.com/rest/users/gpg-keys#list-gpg-keys-for-a-user) | GET | /users/{username}/gpg_keys | indexed |
| [users/get-context-for-user](https://docs.github.com/rest/users/users#get-contextual-information-for-a-user) | GET | /users/{username}/hovercard | indexed |
| [users/list-public-keys-for-user](https://docs.github.com/rest/users/keys#list-public-keys-for-a-user) | GET | /users/{username}/keys | indexed |
| [users/list-social-accounts-for-user](https://docs.github.com/rest/users/social-accounts#list-social-accounts-for-a-user) | GET | /users/{username}/social_accounts | indexed |
| [users/list-ssh-signing-keys-for-user](https://docs.github.com/rest/users/ssh-signing-keys#list-ssh-signing-keys-for-a-user) | GET | /users/{username}/ssh_signing_keys | indexed |

## GraphQL queries

| Operation | Availability |
| --- | --- |
| _entities | indexed |
| codeOfConduct | indexed |
| codesOfConduct | indexed |
| enterprise | indexed |
| enterpriseAdministratorInvitation | indexed |
| enterpriseAdministratorInvitationByToken | indexed |
| enterpriseMemberInvitation | indexed |
| enterpriseMemberInvitationByToken | indexed |
| id | indexed |
| license | indexed |
| licenses | indexed |
| marketplaceCategories | indexed |
| marketplaceCategory | indexed |
| marketplaceListing | indexed |
| marketplaceListings | indexed |
| meta | indexed |
| node | indexed |
| nodes | indexed |
| organization | indexed |
| rateLimit | indexed |
| relay | indexed |
| repository | indexed |
| repositoryOwner | indexed |
| resource | indexed |
| search | indexed |
| securityAdvisories | indexed |
| securityAdvisory | indexed |
| securityVulnerabilities | indexed |
| sponsorables | indexed |
| topic | indexed |
| user | indexed |
| viewer | indexed |

## GraphQL mutations

| Operation | Availability |
| --- | --- |
| abortQueuedMigrations | indexed |
| abortRepositoryMigration | indexed |
| acceptEnterpriseAdministratorInvitation | indexed |
| acceptEnterpriseMemberInvitation | indexed |
| acceptTopicSuggestion | indexed |
| accessUserNamespaceRepository | indexed |
| addAssigneesToAssignable | indexed |
| addBlockedBy | indexed |
| addCloseIssueReferences | indexed |
| addComment | indexed |
| addDiscussionComment | indexed |
| addDiscussionPollVote | indexed |
| addEnterpriseOrganizationMember | indexed |
| addEnterpriseSupportEntitlement | indexed |
| addLabelsToLabelable | indexed |
| addProjectCard | deprecated |
| addProjectColumn | deprecated |
| addProjectV2DraftIssue | indexed |
| addProjectV2ItemById | indexed |
| addPullRequestCreationCapBypassUsers | indexed |
| addPullRequestReview | indexed |
| addPullRequestReviewComment | indexed |
| addPullRequestReviewThread | indexed |
| addPullRequestReviewThreadReply | indexed |
| addReaction | indexed |
| addRelatesTo | indexed |
| addStar | indexed |
| addSubIssue | indexed |
| addUpvote | indexed |
| addVerifiableDomain | indexed |
| applyPendingIssueSuggestions | indexed |
| approveDeployments | indexed |
| approveVerifiableDomain | indexed |
| archiveProjectV2Item | indexed |
| archivePullRequest | indexed |
| archiveRepository | indexed |
| cancelEnterpriseAdminInvitation | indexed |
| cancelEnterpriseMemberInvitation | indexed |
| cancelSponsorship | indexed |
| changeUserStatus | indexed |
| clearLabelsFromLabelable | indexed |
| clearProjectV2ItemFieldValue | indexed |
| cloneProject | deprecated |
| cloneTemplateRepository | indexed |
| closeDiscussion | indexed |
| closeIssue | indexed |
| closePullRequest | indexed |
| convertProjectCardNoteToIssue | deprecated |
| convertProjectV2DraftIssueItemToIssue | indexed |
| convertPullRequestToDraft | indexed |
| copyProjectV2 | indexed |
| createAttributionInvitation | indexed |
| createBranchProtectionRule | indexed |
| createCheckRun | indexed |
| createCheckSuite | indexed |
| createCommitOnBranch | indexed |
| createDeployment | indexed |
| createDeploymentStatus | indexed |
| createDiscussion | indexed |
| createEnterpriseOrganization | indexed |
| createEnvironment | indexed |
| createIpAllowListEntry | indexed |
| createIssue | indexed |
| createIssueField | indexed |
| createIssueFieldValue | indexed |
| createIssueType | indexed |
| createLabel | indexed |
| createLinkedBranch | indexed |
| createMigrationSource | indexed |
| createProject | deprecated |
| createProjectV2 | indexed |
| createProjectV2Field | indexed |
| createProjectV2IssueField | indexed |
| createProjectV2StatusUpdate | indexed |
| createProjectV2View | indexed |
| createPullRequest | indexed |
| createRef | indexed |
| createRepository | indexed |
| createRepositoryCustomProperty | indexed |
| createRepositoryRuleset | indexed |
| createSponsorsListing | indexed |
| createSponsorsTier | indexed |
| createSponsorship | indexed |
| createSponsorships | indexed |
| createUserList | indexed |
| declineTopicSuggestion | indexed |
| deleteBranchProtectionRule | indexed |
| deleteDeployment | indexed |
| deleteDiscussion | indexed |
| deleteDiscussionComment | indexed |
| deleteEnvironment | indexed |
| deleteIpAllowListEntry | indexed |
| deleteIssue | indexed |
| deleteIssueComment | indexed |
| deleteIssueField | indexed |
| deleteIssueFieldValue | indexed |
| deleteIssueType | indexed |
| deleteLabel | indexed |
| deleteLinkedBranch | indexed |
| deletePackageVersion | indexed |
| deleteProject | deprecated |
| deleteProjectCard | deprecated |
| deleteProjectColumn | deprecated |
| deleteProjectV2 | indexed |
| deleteProjectV2Field | indexed |
| deleteProjectV2Item | indexed |
| deleteProjectV2StatusUpdate | indexed |
| deleteProjectV2View | indexed |
| deleteProjectV2Workflow | indexed |
| deletePullRequestReview | indexed |
| deletePullRequestReviewComment | indexed |
| deleteRef | indexed |
| deleteRepositoryCustomProperty | indexed |
| deleteRepositoryRuleset | indexed |
| deleteUserList | indexed |
| deleteVerifiableDomain | indexed |
| dequeuePullRequest | indexed |
| disablePullRequestAutoMerge | indexed |
| dismissPullRequestReview | indexed |
| dismissRepositoryVulnerabilityAlert | indexed |
| enablePullRequestAutoMerge | indexed |
| enqueuePullRequest | indexed |
| followOrganization | indexed |
| followUser | indexed |
| grantEnterpriseOrganizationsMigratorRole | indexed |
| grantMigratorRole | indexed |
| importProject | deprecated |
| inviteEnterpriseAdmin | indexed |
| inviteEnterpriseMember | indexed |
| linkProjectV2ToRepository | indexed |
| linkProjectV2ToTeam | indexed |
| linkRepositoryToProject | deprecated |
| lockLockable | indexed |
| markDiscussionCommentAsAnswer | indexed |
| markFileAsViewed | indexed |
| markProjectV2AsTemplate | indexed |
| markPullRequestReadyForReview | indexed |
| mergeBranch | indexed |
| mergePullRequest | indexed |
| minimizeComment | indexed |
| moveProjectCard | deprecated |
| moveProjectColumn | deprecated |
| pinEnvironment | indexed |
| pinIssue | indexed |
| pinIssueComment | indexed |
| promoteRepositoryCustomProperty | indexed |
| publishSponsorsTier | indexed |
| regenerateEnterpriseIdentityProviderRecoveryCodes | indexed |
| regenerateVerifiableDomainToken | indexed |
| rejectDeployments | indexed |
| rejectPendingIssueSuggestions | indexed |
| removeAssigneesFromAssignable | indexed |
| removeBlockedBy | indexed |
| removeCloseIssueReferences | indexed |
| removeEnterpriseAdmin | indexed |
| removeEnterpriseIdentityProvider | indexed |
| removeEnterpriseMember | indexed |
| removeEnterpriseOrganization | indexed |
| removeEnterpriseSupportEntitlement | indexed |
| removeLabelsFromLabelable | indexed |
| removeOutsideCollaborator | indexed |
| removePullRequestCreationCapBypassUsers | indexed |
| removeReaction | indexed |
| removeRelatesTo | indexed |
| removeStar | indexed |
| removeSubIssue | indexed |
| removeUpvote | indexed |
| reopenDiscussion | indexed |
| reopenIssue | indexed |
| reopenPullRequest | indexed |
| reorderEnvironment | indexed |
| replaceActorsForAssignable | indexed |
| reprioritizeSubIssue | indexed |
| requestCopilotCodeReview | indexed |
| requestReviews | indexed |
| requestReviewsByLogin | indexed |
| rerequestCheckSuite | indexed |
| rerequestReviews | indexed |
| resolveReviewThread | indexed |
| retireSponsorsTier | indexed |
| revertPullRequest | indexed |
| revokeEnterpriseOrganizationsMigratorRole | indexed |
| revokeMigratorRole | indexed |
| setEnterpriseIdentityProvider | indexed |
| setIssueFieldValue | indexed |
| setIssueStatus | indexed |
| setOrganizationInteractionLimit | indexed |
| setRepositoryCustomPropertyValues | indexed |
| setRepositoryInteractionLimit | indexed |
| setUserInteractionLimit | indexed |
| startOrganizationMigration | indexed |
| startRepositoryMigration | indexed |
| submitPullRequestReview | indexed |
| transferEnterpriseOrganization | indexed |
| transferIssue | indexed |
| unarchiveProjectV2Item | indexed |
| unarchivePullRequest | indexed |
| unarchiveRepository | indexed |
| unfollowOrganization | indexed |
| unfollowUser | indexed |
| unlinkProjectV2FromRepository | indexed |
| unlinkProjectV2FromTeam | indexed |
| unlinkRepositoryFromProject | deprecated |
| unlockLockable | indexed |
| unmarkDiscussionCommentAsAnswer | indexed |
| unmarkFileAsViewed | indexed |
| unmarkIssueAsDuplicate | indexed |
| unmarkProjectV2AsTemplate | indexed |
| unminimizeComment | indexed |
| unpinIssue | indexed |
| unpinIssueComment | indexed |
| unresolveReviewThread | indexed |
| updateBranchProtectionRule | indexed |
| updateCheckRun | indexed |
| updateCheckSuitePreferences | indexed |
| updateDiscussion | indexed |
| updateDiscussionComment | indexed |
| updateEnterpriseAdministratorRole | indexed |
| updateEnterpriseAllowPrivateRepositoryForkingSetting | indexed |
| updateEnterpriseCopilotCodeReviewPolicy | indexed |
| updateEnterpriseDefaultRepositoryPermissionSetting | indexed |
| updateEnterpriseDeployKeySetting | indexed |
| updateEnterpriseMembersCanChangeRepositoryVisibilitySetting | indexed |
| updateEnterpriseMembersCanCreateRepositoriesSetting | indexed |
| updateEnterpriseMembersCanDeleteIssuesSetting | indexed |
| updateEnterpriseMembersCanDeleteRepositoriesSetting | indexed |
| updateEnterpriseMembersCanInviteCollaboratorsSetting | indexed |
| updateEnterpriseMembersCanMakePurchasesSetting | indexed |
| updateEnterpriseMembersCanUpdateProtectedBranchesSetting | indexed |
| updateEnterpriseMembersCanViewDependencyInsightsSetting | indexed |
| updateEnterpriseOrganizationProjectsSetting | indexed |
| updateEnterpriseOwnerOrganizationRole | indexed |
| updateEnterpriseProfile | indexed |
| updateEnterpriseRepositoryProjectsSetting | indexed |
| updateEnterpriseTwoFactorAuthenticationDisallowedMethodsSetting | indexed |
| updateEnterpriseTwoFactorAuthenticationRequiredSetting | indexed |
| updateEnvironment | indexed |
| updateIpAllowListEnabledSetting | indexed |
| updateIpAllowListEntry | indexed |
| updateIpAllowListForInstalledAppsEnabledSetting | indexed |
| updateIpAllowListUserLevelEnforcementEnabledSetting | indexed |
| updateIssue | indexed |
| updateIssueComment | indexed |
| updateIssueField | indexed |
| updateIssueFieldValue | indexed |
| updateIssueIssueType | indexed |
| updateIssueType | indexed |
| updateLabel | indexed |
| updateNotificationRestrictionSetting | indexed |
| updateOrganizationAllowPrivateRepositoryForkingSetting | indexed |
| updateOrganizationCopilotCodeReviewPolicy | indexed |
| updateOrganizationCopilotCodeReviewRunnerConfiguration | indexed |
| updateOrganizationCopilotCodeReviewSettings | indexed |
| updateOrganizationWebCommitSignoffSetting | indexed |
| updatePatreonSponsorability | indexed |
| updateProject | deprecated |
| updateProjectCard | deprecated |
| updateProjectColumn | deprecated |
| updateProjectV2 | indexed |
| updateProjectV2Collaborators | indexed |
| updateProjectV2DraftIssue | indexed |
| updateProjectV2Field | indexed |
| updateProjectV2ItemFieldValue | indexed |
| updateProjectV2ItemPosition | indexed |
| updateProjectV2StatusUpdate | indexed |
| updateProjectV2View | indexed |
| updatePullRequest | indexed |
| updatePullRequestBranch | indexed |
| updatePullRequestReview | indexed |
| updatePullRequestReviewComment | indexed |
| updateRef | indexed |
| updateRefs | indexed |
| updateRepository | indexed |
| updateRepositoryCopilotCodeReviewSettings | indexed |
| updateRepositoryCustomProperty | indexed |
| updateRepositoryRuleset | indexed |
| updateRepositoryWebCommitSignoffSetting | indexed |
| updateSponsorshipPreferences | indexed |
| updateSubscription | indexed |
| updateTeamReviewAssignment | indexed |
| updateTeamsRepository | indexed |
| updateTopics | indexed |
| updateUserList | indexed |
| updateUserListsForItem | indexed |
| verifyVerifiableDomain | indexed |

