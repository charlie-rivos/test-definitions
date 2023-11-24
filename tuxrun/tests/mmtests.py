# vim: set ts=4
#
# Copyright 2023-present Linaro Limited
#
# SPDX-License-Identifier: MIT

from tuxrun.tests import Test


class MMTests(Test):
    devices = ["qemu-arm64", "qemu-x86_64"]
    configfile: str = ""
    iterations: int = 0
    need_test_definition = True

    def render(self, **kwargs):
        kwargs["name"] = self.name
        kwargs["configfile"] = self.configfile
        kwargs["iterations"] = self.iterations
        kwargs["timeout"] = self.timeout
        return self._render("mmtests.yaml.jinja2", **kwargs)


class MMTestsDbSqliteInsertSmall(MMTests):
    configfile = "configs/config-db-sqlite-insert-small"
    name = "mmtests-db-sqlite-insert-small"
    iterations = 10
    timeout = 90


class MMTestsHpcScimarkcSmall(MMTests):
    configfile = "configs/config-hpc-scimarkc-small"
    name = "mmtests-hpc-scimarkc-small"
    iterations = 20
    timeout = 90


class MMTestsBlogbench(MMTests):
    configfile = "configs/config-io-blogbench"
    name = "mmtests-io-blogbench"
    iterations = 30
    timeout = 90


class MMTestsFioRandreadAsyncRandwrite(MMTests):
    configfile = "configs/config-io-fio-randread-async-randwrite"
    name = "mmtests-io-fio-randread-async-randwrite"
    iterations = 10
    timeout = 90


class MMTestsFioRandreadAsyncSeqwrite(MMTests):
    configfile = "configs/config-io-fio-randread-async-seqwrite"
    name = "mmtests-io-fio-randread-async-seqwrite"
    iterations = 10
    timeout = 90


class MMTestsFioRandreadSyncHeavywrite(MMTests):
    configfile = "configs/config-io-fio-randread-sync-heavywrite"
    name = "mmtests-io-fio-randread-sync-heavywrite"
    iterations = 10
    timeout = 90


class MMTestsFioRandreadSyncRandwrite(MMTests):
    configfile = "configs/config-io-fio-randread-sync-randwrite"
    name = "mmtests-io-fio-randread-sync-randwrite"
    iterations = 10
    timeout = 90


class MMTestsFsmarkSmallFileStream(MMTests):
    configfile = "configs/config-io-fsmark-small-file-stream"
    name = "mmtests-io-fsmark-small-file-stream"
    iterations = 10
    timeout = 90


class MMTestsRedisBenchmarkSmall(MMTests):
    configfile = "configs/config-memdb-redis-benchmark-small"
    name = "mmtests-memdb-redis-benchmark-small"
    iterations = 20
    timeout = 90


class MMTestsRedisMemtierSmall(MMTests):
    configfile = "configs/config-memdb-redis-memtier-small"
    name = "mmtests-memdb-redis-memtier-small"
    iterations = 20
    timeout = 90


class MMTestsSchbench(MMTests):
    configfile = "configs/config-scheduler-schbench"
    name = "mmtests-scheduler-schbench"
    iterations = 10
    timeout = 90


class MMTestsSysbenchCpu(MMTests):
    configfile = "configs/config-scheduler-sysbench-cpu"
    name = "mmtests-scheduler-sysbench-cpu"
    iterations = 10
    timeout = 90


class MMTestsSysbenchThread(MMTests):
    configfile = "configs/config-scheduler-sysbench-thread"
    name = "mmtests-scheduler-sysbench-thread"
    iterations = 10
    timeout = 90


class MMTestsAim9Disk(MMTests):
    configfile = "configs/config-workload-aim9-disk"
    name = "mmtests-workload-aim9-disk"
    iterations = 10
    timeout = 90


class MMTestsCoremark(MMTests):
    configfile = "configs/config-workload-coremark"
    name = "mmtests-workload-coremark"
    iterations = 20
    timeout = 90


class MMTestsCyclictestFineHackbench(MMTests):
    configfile = "configs/config-workload-cyclictest-fine-hackbench"
    name = "mmtests-workload-cyclictest-fine-hackbench"
    iterations = 15
    timeout = 90


class MMTestsCyclictestHackbench(MMTests):
    configfile = "configs/config-workload-cyclictest-hackbench"
    name = "mmtests-workload-cyclictest-hackbench"
    iterations = 20
    timeout = 90


class MMTestsEbizzy(MMTests):
    configfile = "configs/config-workload-ebizzy"
    name = "mmtests-workload-ebizzy"
    iterations = 10
    timeout = 90


class MMTestsPmqtestHackbench(MMTests):
    configfile = "configs/config-workload-pmqtest-hackbench"
    name = "mmtests-workload-pmqtest-hackbench"
    iterations = 10
    timeout = 90


class MMTestsStressngAfAlg(MMTests):
    configfile = "configs/config-workload-stressng-af-alg"
    name = "mmtests-workload-stressng-af-alg"
    iterations = 10
    timeout = 90


class MMTestsStressngBadAltstack(MMTests):
    configfile = "configs/config-workload-stressng-bad-altstack"
    name = "mmtests-workload-stressng-bad-altstack"
    iterations = 10
    timeout = 90


class MMTestsStressngClassIoParallel(MMTests):
    configfile = "configs/config-workload-stressng-class-io-parallel"
    name = "mmtests-workload-stressng-class-io-parallel"
    iterations = 10
    timeout = 90


class MMTestsStressngContext(MMTests):
    configfile = "configs/config-workload-stressng-context"
    name = "mmtests-workload-stressng-context"
    iterations = 10
    timeout = 90


class MMTestsStressngFork(MMTests):
    configfile = "configs/config-workload-stressng-fork"
    name = "mmtests-workload-stressng-fork"
    iterations = 10
    timeout = 90


class MMTestsStressngGet(MMTests):
    configfile = "configs/config-workload-stressng-get"
    name = "mmtests-workload-stressng-get"
    iterations = 10
    timeout = 90


class MMTestsStressngGetdent(MMTests):
    configfile = "configs/config-workload-stressng-getdent"
    name = "mmtests-workload-stressng-getdent"
    iterations = 10
    timeout = 90


class MMTestsStressngMadvise(MMTests):
    configfile = "configs/config-workload-stressng-madvise"
    name = "mmtests-workload-stressng-madvise"
    iterations = 10
    timeout = 90


class MMTestsStressngMmap(MMTests):
    configfile = "configs/config-workload-stressng-mmap"
    name = "mmtests-workload-stressng-mmap"
    iterations = 10
    timeout = 90


class MMTestsStressngVmSplice(MMTests):
    configfile = "configs/config-workload-stressng-vm-splice"
    name = "mmtests-workload-stressng-vm-splice"
    iterations = 10
    timeout = 90


class MMTestsStressngZombie(MMTests):
    configfile = "configs/config-workload-stressng-zombie"
    name = "mmtests-workload-stressng-zombie"
    iterations = 10
    timeout = 90


class MMTestsUsemem(MMTests):
    configfile = "configs/config-workload-usemem"
    name = "mmtests-workload-usemem"
    iterations = 10
    timeout = 90


class MMTestsScaleIoProcesses(MMTests):
    configfile = "configs/config-workload-will-it-scale-io-processes"
    name = "mmtests-workload-will-it-scale-io-processes"
    iterations = 10
    timeout = 90


class MMTestsScaleIoThreads(MMTests):
    configfile = "configs/config-workload-will-it-scale-io-threads"
    name = "mmtests-workload-will-it-scale-io-threads"
    iterations = 10
    timeout = 90


class MMTestsScalePfProcesses(MMTests):
    configfile = "configs/config-workload-will-it-scale-pf-processes"
    name = "mmtests-workload-will-it-scale-pf-processes"
    iterations = 10
    timeout = 90


class MMTestsScalePfThreads(MMTests):
    configfile = "configs/config-workload-will-it-scale-pf-threads"
    name = "mmtests-workload-will-it-scale-pf-threads"
    iterations = 10
    timeout = 90


class MMTestsScaleSysProcesses(MMTests):
    configfile = "configs/config-workload-will-it-scale-sys-processes"
    name = "mmtests-workload-will-it-scale-sys-processes"
    iterations = 10
    timeout = 90


class MMTestsScaleSysThreads(MMTests):
    configfile = "configs/config-workload-will-it-scale-sys-threads"
    name = "mmtests-workload-will-it-scale-sys-threads"
    iterations = 10
    timeout = 90
