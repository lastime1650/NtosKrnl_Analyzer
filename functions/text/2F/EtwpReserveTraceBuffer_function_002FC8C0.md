# EtwpReserveTraceBuffer

- RVA: `0x002FC8C0`–`0x002FCE66` (길이 `1,446` bytes)
- VA: `0x00000001402FC8C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00072B50`
- 디코드: `348`개 명령, `1,446/1,446` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **20**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x002FC9FA` → [EtwpDequeueFreeBuffer](../3E/EtwpDequeueFreeBuffer_function_003EB1F0.md) (function, `0x003EB1F0`)
- `0x002FCA77` → [EtwpGetLoggerTimeStamp](../37/EtwpGetLoggerTimeStamp_function_0037E690.md) (function, `0x0037E690`)
- `0x002FCAF1` → [EtwpEnqueueAvailableBuffer](EtwpEnqueueAvailableBuffer_function_002FE7DC.md) (function, `0x002FE7DC`)
- `0x002FCB0C` → [EtwpGetLoggerTimeStamp](../37/EtwpGetLoggerTimeStamp_function_0037E690.md) (function, `0x0037E690`)
- `0x002FCB4A` → [EtwpEnqueueOverflowBuffer](EtwpEnqueueOverflowBuffer_function_002FE644.md) (function, `0x002FE644`)
- `0x002FCB73` → [EtwpRequestFlushTimer](EtwpRequestFlushTimer_function_002FE6B0.md) (function, `0x002FE6B0`)
- `0x002FCB95` → [EtwpEnqueueAvailableBuffer](EtwpEnqueueAvailableBuffer_function_002FE7DC.md) (function, `0x002FE7DC`)
- `0x002FCBAC` → [KeGetEffectiveIrql](KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x002FCBC7` → [EtwpAllocateFreeBuffers](../3E/EtwpAllocateFreeBuffers_function_003EAEA4.md) (function, `0x003EAEA4`)
- `0x002FCC50` → [EtwpBuffersFlushRequired](../3E/EtwpBuffersFlushRequired_function_003EB5AC.md) (function, `0x003EB5AC`)
- `0x002FCC6A` → [KeGetEffectiveIrql](KeGetEffectiveIrql_function_002F8030.md) (function, `0x002F8030`)
- `0x002FCC7F` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002FCCB5` → [KeInsertQueueDpc](../20/KeInsertQueueDpc_function_00207C50.md) (function, `0x00207C50`)
- `0x002FCD09` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x002FCD4C` → [EtwpLockBufferList](../3E/EtwpLockBufferList_function_003EB49C.md) (function, `0x003EB49C`)
- `0x002FCD69` → [EtwpUnlockBufferList](../2D/EtwpUnlockBufferList_function_002DFC28.md) (function, `0x002DFC28`)
- `0x002FCDB7` → [EtwpGetTimeStampAndQpcDelta](../4A/EtwpGetTimeStampAndQpcDelta_function_004A1978.md) (function, `0x004A1978`)
- `0x002FCE15` → [EtwpEnqueueAvailableBuffer](EtwpEnqueueAvailableBuffer_function_002FE7DC.md) (function, `0x002FE7DC`)
- `0x002FCE43` → [EtwpReenableCompression](../65/EtwpReenableCompression_function_00653768.md) (function, `0x00653768`)
- `0x002FCE5A` → [EtwpUpdateEventsLostCount](../3F/EtwpUpdateEventsLostCount_function_003F18E0.md) (function, `0x003F18E0`)

### Direct callers
- [EtwpEventWriteFull](../22/EtwpEventWriteFull_function_00225C10.md) at `0x002268E4`
- [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) at `0x0025CD3A`
- [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) at `0x0025D075`
- [EtwpLogKernelEvent](../25/EtwpLogKernelEvent_function_0025CC00.md) at `0x0025D4F0`
- [EtwpTraceMessageVa](EtwpTraceMessageVa_function_002FB2B0.md) at `0x002FB6D2`
- [EtwpLogSystemEventUnsafe](EtwpLogSystemEventUnsafe_function_002FBF10.md) at `0x002FC144`
- [EtwpReserveWithPmcCounters](EtwpReserveWithPmcCounters_function_002FCED0.md) at `0x002FCF59`
- [EtwTraceEvent](EtwTraceEvent_function_002FD290.md) at `0x002FD587`
- [EtwpLogContextSwapEvent](../41/EtwpLogContextSwapEvent_function_004175F0.md) at `0x00417795`
- [EtwpReserveWithPebsIndex](../41/EtwpReserveWithPebsIndex_function_0041809C.md) at `0x004180CF`
- [EtwTraceRaw](../65/EtwTraceRaw_function_006516CC.md) at `0x00651804`
- [EtwpWriteUserEvent](../../page/AF/EtwpWriteUserEvent_function_00AF2FEC.md) at `0x00AF3ADC`

### Static image references
- `0x002FC91D` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x002FC931` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x002FC93E` → RVA `0x00FC6A80` (`ALMOSTRO`; read)
- `0x002FC9DE` → RVA `0x00F4754C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **5**
  - `0x002FCDE2` → [sub_006DFB24](../6D/Unknown_function_006DFB24.md) (`tail-transfer`)
  - `0x002FCDEB` → [sub_006DFB24](../6D/Unknown_function_006DFB24.md) (`tail-transfer`)
  - `0x002FCE23` → [sub_006DFB24 + 0x8B](../6D/Unknown_function_006DFB24.md) (`tail-transfer`)
  - `0x002FCE3A` → [sub_006DFB24 + 0x8B](../6D/Unknown_function_006DFB24.md) (`tail-transfer`)
  - `0x002FCE49` → [sub_006DFB24 + 0x8B](../6D/Unknown_function_006DFB24.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002FC8C0  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002FC8C5  48 89 6C 24 18                  mov qword ptr [rsp + 0x18], rbp
002FC8CA  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
002FC8CF  57                              push rdi
002FC8D0  41 54                           push r12
002FC8D2  41 55                           push r13
002FC8D4  41 56                           push r14
002FC8D6  41 57                           push r15
002FC8D8  48 83 EC 50                     sub rsp, 0x50
002FC8DC  83 79 10 00                     cmp dword ptr [rcx + 0x10], 0
002FC8E0  4D 8B E9                        mov r13, r9
002FC8E3  4D 8B E0                        mov r12, r8
002FC8E6  4C 8B F9                        mov r15, rcx
002FC8E9  0F 8C 68 05 00 00               jl 0x1402fce57
002FC8EF  3B 51 08                        cmp edx, dword ptr [rcx + 8]
002FC8F2  0F 87 5F 05 00 00               ja 0x1402fce57
002FC8F8  44 8B 01                        mov r8d, dword ptr [rcx]
002FC8FB  44 8D 4A 07                     lea r9d, [rdx + 7]
002FC8FF  8B 51 04                        mov edx, dword ptr [rcx + 4]
002FC902  41 83 E1 F8                     and r9d, 0xfffffff8
002FC906  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
002FC90B  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
002FC90F  44 89 44 24 24                  mov dword ptr [rsp + 0x24], r8d
002FC914  65 48 8B 04 25 20 00 00 00      mov rax, qword ptr gs:[0x20]
002FC91D  48 8D 0D 1C C3 CC 00            lea rcx, [rip + 0xccc31c]
002FC924  45 33 C9                        xor r9d, r9d
002FC927  8B 68 24                        mov ebp, dword ptr [rax + 0x24]
002FC92A  49 8B 87 50 05 00 00            mov rax, qword ptr [r15 + 0x550]
002FC931  48 3B 05 70 A1 CC 00            cmp rax, qword ptr [rip + 0xcca170]
002FC938  0F 85 5C 04 00 00               jne 0x1402fcd9a
002FC93E  8B 05 3C A1 CC 00               mov eax, dword ptr [rip + 0xcca13c]
002FC944  3B E8                           cmp ebp, eax
002FC946  0F 83 B3 03 00 00               jae 0x1402fccff
002FC94C  48 8B 0C E9                     mov rcx, qword ptr [rcx + rbp*8]
002FC950  4C 8B B1 A8 8B 00 00            mov r14, qword ptr [rcx + 0x8ba8]
002FC957  49 81 C6 40 01 00 00            add r14, 0x140
002FC95E  41 F7 47 0C 00 00 00 10         test dword ptr [r15 + 0xc], 0x10000000
002FC966  0F 84 54 01 00 00               je 0x1402fcac0
002FC96C  49 8D B7 80 00 00 00            lea rsi, [r15 + 0x80]
002FC973  C6 84 24 80 00 00 00 00         mov byte ptr [rsp + 0x80], 0
002FC97B  0F 0D 0E                        prefetchw byte ptr [rsi]
002FC97E  48 8B 3E                        mov rdi, qword ptr [rsi]
002FC981  40 F6 C7 0F                     test dil, 0xf
002FC985  74 15                           je 0x1402fc99c
002FC987  48 8D 4F FF                     lea rcx, [rdi - 1]
002FC98B  48 8B C7                        mov rax, rdi
002FC98E  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
002FC993  74 07                           je 0x1402fc99c
002FC995  48 8B F8                        mov rdi, rax
002FC998  A8 0F                           test al, 0xf
002FC99A  75 EB                           jne 0x1402fc987
002FC99C  48 85 FF                        test rdi, rdi
002FC99F  0F 84 D8 01 00 00               je 0x1402fcb7d
002FC9A5  8B C7                           mov eax, edi
002FC9A7  83 E0 0F                        and eax, 0xf
002FC9AA  83 F8 01                        cmp eax, 1
002FC9AD  0F 82 8E 03 00 00               jb 0x1402fcd41
002FC9B3  48 83 E7 F0                     and rdi, 0xfffffffffffffff0
002FC9B7  83 F8 01                        cmp eax, 1
002FC9BA  0F 84 FF 02 00 00               je 0x1402fccbf
002FC9C0  48 85 FF                        test rdi, rdi
002FC9C3  74 19                           je 0x1402fc9de
002FC9C5  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
002FC9CA  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
002FC9CF  0F 0D 4F 08                     prefetchw byte ptr [rdi + 8]
002FC9D3  8B 5F 08                        mov ebx, dword ptr [rdi + 8]
002FC9D6  3B DA                           cmp ebx, edx
002FC9D8  0F 86 1A 01 00 00               jbe 0x1402fcaf8
002FC9DE  8B 05 68 AB C4 00               mov eax, dword ptr [rip + 0xc4ab68]
002FC9E4  A8 03                           test al, 3
002FC9E6  0F 85 62 04 00 00               jne 0x1402fce4e
002FC9EC  45 8B 77 0C                     mov r14d, dword ptr [r15 + 0xc]
002FC9F0  41 81 E6 00 04 00 00            and r14d, 0x400
002FC9F7  49 8B CF                        mov rcx, r15
002FC9FA  E8 F1 E7 0E 00                  call 0x1403eb1f0
002FC9FF  48 8B D0                        mov rdx, rax
002FCA02  48 85 C0                        test rax, rax
002FCA05  0F 84 94 01 00 00               je 0x1402fcb9f
002FCA0B  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
002FCA0F  0F BA E0 1C                     bt eax, 0x1c
002FCA13  72 04                           jb 0x1402fca19
002FCA15  66 89 6A 28                     mov word ptr [rdx + 0x28], bp
002FCA19  F0 83 42 0C 0F                  lock add dword ptr [rdx + 0xc], 0xf
002FCA1E  45 85 F6                        test r14d, r14d
002FCA21  75 04                           jne 0x1402fca27
002FCA23  48 89 7A 20                     mov qword ptr [rdx + 0x20], rdi
002FCA27  0F 0D 0E                        prefetchw byte ptr [rsi]
002FCA2A  48 8B 1E                        mov rbx, qword ptr [rsi]
002FCA2D  48 8B C3                        mov rax, rbx
002FCA30  48 33 C7                        xor rax, rdi
002FCA33  48 83 F8 0F                     cmp rax, 0xf
002FCA37  77 11                           ja 0x1402fca4a
002FCA39  48 8B CA                        mov rcx, rdx
002FCA3C  48 8B C3                        mov rax, rbx
002FCA3F  48 83 C9 0F                     or rcx, 0xf
002FCA43  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
002FCA48  75 6E                           jne 0x1402fcab8
002FCA4A  48 8B EB                        mov rbp, rbx
002FCA4D  48 83 E5 F0                     and rbp, 0xfffffffffffffff0
002FCA51  48 3B EF                        cmp rbp, rdi
002FCA54  75 79                           jne 0x1402fcacf
002FCA56  48 85 ED                        test rbp, rbp
002FCA59  0F 84 F5 00 00 00               je 0x1402fcb54
002FCA5F  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
002FCA63  49 8B CF                        mov rcx, r15
002FCA66  0F BA E0 0A                     bt eax, 0xa
002FCA6A  0F 82 15 01 00 00               jb 0x1402fcb85
002FCA70  C7 45 2C 03 00 00 00            mov dword ptr [rbp + 0x2c], 3
002FCA77  E8 14 1C 08 00                  call 0x14037e690
002FCA7C  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
002FCA80  83 E3 0F                        and ebx, 0xf
002FCA83  F7 D3                           not ebx
002FCA85  F0 01 5D 0C                     lock add dword ptr [rbp + 0xc], ebx
002FCA89  45 85 F6                        test r14d, r14d
002FCA8C  0F 84 BB 01 00 00               je 0x1402fcc4d
002FCA92  33 DB                           xor ebx, ebx
002FCA94  41 F7 47 0C 00 00 00 04         test dword ptr [r15 + 0xc], 0x4000000
002FCA9C  0F 85 65 02 00 00               jne 0x1402fcd07
002FCAA2  85 DB                           test ebx, ebx
002FCAA4  0F 88 AD 03 00 00               js 0x1402fce57
002FCAAA  44 8B 44 24 24                  mov r8d, dword ptr [rsp + 0x24]
002FCAAF  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
002FCAB3  E9 5C FE FF FF                  jmp 0x1402fc914
002FCAB8  48 8B D8                        mov rbx, rax
002FCABB  E9 6D FF FF FF                  jmp 0x1402fca2d
002FCAC0  49 8B 06                        mov rax, qword ptr [r14]
002FCAC3  41 8B C8                        mov ecx, r8d
002FCAC6  48 8D 34 C8                     lea rsi, [rax + rcx*8]
002FCACA  E9 A4 FE FF FF                  jmp 0x1402fc973
002FCACF  48 85 ED                        test rbp, rbp
002FCAD2  0F 84 B1 01 00 00               je 0x1402fcc89
002FCAD8  48 85 FF                        test rdi, rdi
002FCADB  74 04                           je 0x1402fcae1
002FCADD  F0 FF 4F 0C                     lock dec dword ptr [rdi + 0xc]
002FCAE1  F0 83 42 0C F1                  lock add dword ptr [rdx + 0xc], -0xf
002FCAE6  49 8B CF                        mov rcx, r15
002FCAE9  45 85 F6                        test r14d, r14d
002FCAEC  75 5C                           jne 0x1402fcb4a
002FCAEE  45 33 C0                        xor r8d, r8d
002FCAF1  E8 E6 1C 00 00                  call 0x1402fe7dc
002FCAF6  EB 9A                           jmp 0x1402fca92
002FCAF8  41 F7 87 30 03 00 00 00 00 00 08  test dword ptr [r15 + 0x330], 0x8000000
002FCB03  49 8B CF                        mov rcx, r15
002FCB06  0F 85 A1 02 00 00               jne 0x1402fcdad
002FCB0C  E8 7F 1B 08 00                  call 0x14037e690
002FCB11  44 8B 44 24 24                  mov r8d, dword ptr [rsp + 0x24]
002FCB16  44 8B 4C 24 28                  mov r9d, dword ptr [rsp + 0x28]
002FCB1B  49 89 45 00                     mov qword ptr [r13], rax
002FCB1F  8B C3                           mov eax, ebx
002FCB21  42 8D 0C 0B                     lea ecx, [rbx + r9]
002FCB25  F0 0F B1 4F 08                  lock cmpxchg dword ptr [rdi + 8], ecx
002FCB2A  8B D0                           mov edx, eax
002FCB2C  3B D8                           cmp ebx, eax
002FCB2E  0F 85 C7 02 00 00               jne 0x1402fcdfb
002FCB34  42 8D 04 0A                     lea eax, [rdx + r9]
002FCB38  3B 44 24 20                     cmp eax, dword ptr [rsp + 0x20]
002FCB3C  0F 86 A6 00 00 00               jbe 0x1402fcbe8
002FCB42  89 57 04                        mov dword ptr [rdi + 4], edx
002FCB45  E9 94 FE FF FF                  jmp 0x1402fc9de
002FCB4A  E8 F5 1A 00 00                  call 0x1402fe644
002FCB4F  E9 3E FF FF FF                  jmp 0x1402fca92
002FCB54  41 83 BF D0 00 00 00 00         cmp dword ptr [r15 + 0xd0], 0
002FCB5C  0F 86 30 FF FF FF               jbe 0x1402fca92
002FCB62  F7 84 24 A0 00 00 00 00 06 00 00  test dword ptr [rsp + 0xa0], 0x600
002FCB6D  49 8B CF                        mov rcx, r15
002FCB70  0F 95 C2                        setne dl
002FCB73  E8 38 1B 00 00                  call 0x1402fe6b0
002FCB78  E9 15 FF FF FF                  jmp 0x1402fca92
002FCB7D  49 8B F9                        mov rdi, r9
002FCB80  E9 59 FE FF FF                  jmp 0x1402fc9de
002FCB85  48 8B D5                        mov rdx, rbp
002FCB88  0F BA E0 1A                     bt eax, 0x1a
002FCB8C  0F 82 7D 02 00 00               jb 0x1402fce0f
002FCB92  45 33 C0                        xor r8d, r8d
002FCB95  E8 42 1C 00 00                  call 0x1402fe7dc
002FCB9A  E9 E1 FE FF FF                  jmp 0x1402fca80
002FCB9F  F7 84 24 A0 00 00 00 00 02 00 00  test dword ptr [rsp + 0xa0], 0x200
002FCBAA  75 29                           jne 0x1402fcbd5
002FCBAC  E8 7F B4 FF FF                  call 0x1402f8030
002FCBB1  3C 02                           cmp al, 2
002FCBB3  77 20                           ja 0x1402fcbd5
002FCBB5  41 F7 47 0C 00 00 04 00         test dword ptr [r15 + 0xc], 0x40000
002FCBBD  75 16                           jne 0x1402fcbd5
002FCBBF  BA 01 00 00 00                  mov edx, 1
002FCBC4  49 8B CF                        mov rcx, r15
002FCBC7  E8 D8 E2 0E 00                  call 0x1403eaea4
002FCBCC  83 F8 01                        cmp eax, 1
002FCBCF  0F 84 22 FE FF FF               je 0x1402fc9f7
002FCBD5  48 85 FF                        test rdi, rdi
002FCBD8  74 04                           je 0x1402fcbde
002FCBDA  F0 FF 4F 0C                     lock dec dword ptr [rdi + 0xc]
002FCBDE  BB 17 00 00 C0                  mov ebx, 0xc0000017
002FCBE3  E9 AC FE FF FF                  jmp 0x1402fca94
002FCBE8  41 F7 47 0C 00 04 00 00         test dword ptr [r15 + 0xc], 0x400
002FCBF0  74 1F                           je 0x1402fcc11
002FCBF2  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
002FCBF6  49 8B 4D 00                     mov rcx, qword ptr [r13]
002FCBFA  48 3B C8                        cmp rcx, rax
002FCBFD  7E 12                           jle 0x1402fcc11
002FCBFF  90                              nop
002FCC00  F0 48 0F B1 4F 10               lock cmpxchg qword ptr [rdi + 0x10], rcx
002FCC06  74 09                           je 0x1402fcc11
002FCC08  49 8B 4D 00                     mov rcx, qword ptr [r13]
002FCC0C  48 3B C8                        cmp rcx, rax
002FCC0F  7F EF                           jg 0x1402fcc00
002FCC11  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
002FCC15  41 8B C8                        mov ecx, r8d
002FCC18  48 FF 04 C8                     inc qword ptr [rax + rcx*8]
002FCC1C  48 8D 04 17                     lea rax, [rdi + rdx]
002FCC20  49 89 3C 24                     mov qword ptr [r12], rdi
002FCC24  49 89 74 24 08                  mov qword ptr [r12 + 8], rsi
002FCC29  41 89 54 24 10                  mov dword ptr [r12 + 0x10], edx
002FCC2E  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
002FCC33  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
002FCC37  49 8B 6B 40                     mov rbp, qword ptr [r11 + 0x40]
002FCC3B  49 8B 73 48                     mov rsi, qword ptr [r11 + 0x48]
002FCC3F  49 8B E3                        mov rsp, r11
002FCC42  41 5F                           pop r15
002FCC44  41 5E                           pop r14
002FCC46  41 5D                           pop r13
002FCC48  41 5C                           pop r12
002FCC4A  5F                              pop rdi
002FCC4B  C3                              ret
002FCC4C  CC                              int3
002FCC4D  49 8B CF                        mov rcx, r15
002FCC50  E8 57 E9 0E 00                  call 0x1403eb5ac
002FCC55  84 C0                           test al, al
002FCC57  0F 84 35 FE FF FF               je 0x1402fca92
002FCC5D  F7 84 24 A0 00 00 00 00 06 00 00  test dword ptr [rsp + 0xa0], 0x600
002FCC68  75 2F                           jne 0x1402fcc99
002FCC6A  E8 C1 B3 FF FF                  call 0x1402f8030
002FCC6F  3C 02                           cmp al, 2
002FCC71  77 26                           ja 0x1402fcc99
002FCC73  49 8D 8F E0 01 00 00            lea rcx, [r15 + 0x1e0]
002FCC7A  45 33 C0                        xor r8d, r8d
002FCC7D  33 D2                           xor edx, edx
002FCC7F  E8 8C 26 04 00                  call 0x14033f310
002FCC84  E9 09 FE FF FF                  jmp 0x1402fca92
002FCC89  48 85 FF                        test rdi, rdi
002FCC8C  0F 85 74 01 00 00               jne 0x1402fce06
002FCC92  33 FF                           xor edi, edi
002FCC94  E9 85 FD FF FF                  jmp 0x1402fca1e
002FCC99  F0 41 0F BA AF 38 03 00 00 08   lock bts dword ptr [r15 + 0x338], 8
002FCCA3  0F 82 E9 FD FF FF               jb 0x1402fca92
002FCCA9  49 8D 8F 38 02 00 00            lea rcx, [r15 + 0x238]
002FCCB0  45 33 C0                        xor r8d, r8d
002FCCB3  33 D2                           xor edx, edx
002FCCB5  E8 96 AF F0 FF                  call 0x140207c50
002FCCBA  E9 D3 FD FF FF                  jmp 0x1402fca92
002FCCBF  F0 83 47 0C 0F                  lock add dword ptr [rdi + 0xc], 0xf
002FCCC4  0F 0D 0E                        prefetchw byte ptr [rsi]
002FCCC7  48 8B 06                        mov rax, qword ptr [rsi]
002FCCCA  48 8B C8                        mov rcx, rax
002FCCCD  83 E1 0F                        and ecx, 0xf
002FCCD0  48 83 C1 0F                     add rcx, 0xf
002FCCD4  48 83 F9 0F                     cmp rcx, 0xf
002FCCD8  0F 87 B2 00 00 00               ja 0x1402fcd90
002FCCDE  48 8B C8                        mov rcx, rax
002FCCE1  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
002FCCE5  48 3B F9                        cmp rdi, rcx
002FCCE8  0F 85 A2 00 00 00               jne 0x1402fcd90
002FCCEE  48 8D 48 0F                     lea rcx, [rax + 0xf]
002FCCF2  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
002FCCF7  0F 84 C3 FC FF FF               je 0x1402fc9c0
002FCCFD  EB CB                           jmp 0x1402fccca
002FCCFF  49 8B C9                        mov rcx, r9
002FCD02  E9 49 FC FF FF                  jmp 0x1402fc950
002FCD07  33 C9                           xor ecx, ecx
002FCD09  E8 D2 1A 08 00                  call 0x14037e7e0
002FCD0E  48 8B C8                        mov rcx, rax
002FCD11  4C 8B C8                        mov r9, rax
002FCD14  49 87 8F 00 06 00 00            xchg qword ptr [r15 + 0x600], rcx
002FCD1B  4C 2B C9                        sub r9, rcx
002FCD1E  4D 8B 87 08 06 00 00            mov r8, qword ptr [r15 + 0x608]
002FCD25  4D 85 C0                        test r8, r8
002FCD28  75 50                           jne 0x1402fcd7a
002FCD2A  49 8B C9                        mov rcx, r9
002FCD2D  49 8B C0                        mov rax, r8
002FCD30  F0 49 0F B1 8F 08 06 00 00      lock cmpxchg qword ptr [r15 + 0x608], rcx
002FCD39  0F 84 63 FD FF FF               je 0x1402fcaa2
002FCD3F  EB DD                           jmp 0x1402fcd1e
002FCD41  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
002FCD49  49 8B CF                        mov rcx, r15
002FCD4C  E8 4B E7 0E 00                  call 0x1403eb49c
002FCD51  48 8B 3E                        mov rdi, qword ptr [rsi]
002FCD54  48 83 E7 F0                     and rdi, 0xfffffffffffffff0
002FCD58  74 04                           je 0x1402fcd5e
002FCD5A  F0 FF 47 0C                     lock inc dword ptr [rdi + 0xc]
002FCD5E  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
002FCD66  49 8B CF                        mov rcx, r15
002FCD69  E8 BA 2E FE FF                  call 0x1402dfc28
002FCD6E  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
002FCD72  45 33 C9                        xor r9d, r9d
002FCD75  E9 46 FC FF FF                  jmp 0x1402fc9c0
002FCD7A  4B 8D 04 41                     lea rax, [r9 + r8*2]
002FCD7E  49 03 C0                        add rax, r8
002FCD81  48 99                           cqo
002FCD83  83 E2 03                        and edx, 3
002FCD86  48 8D 0C 02                     lea rcx, [rdx + rax]
002FCD8A  48 C1 F9 02                     sar rcx, 2
002FCD8E  EB 9D                           jmp 0x1402fcd2d
002FCD90  F0 83 47 0C F1                  lock add dword ptr [rdi + 0xc], -0xf
002FCD95  E9 26 FC FF FF                  jmp 0x1402fc9c0
002FCD9A  4C 8B F5                        mov r14, rbp
002FCD9D  49 C1 E6 06                     shl r14, 6
002FCDA1  4C 03 B0 40 11 00 00            add r14, qword ptr [rax + 0x1140]
002FCDA8  E9 B1 FB FF FF                  jmp 0x1402fc95e
002FCDAD  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
002FCDB2  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
002FCDB7  E8 BC 4B 1A 00                  call 0x1404a1978
002FCDBC  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
002FCDC0  85 C0                           test eax, eax
002FCDC2  0F 85 0E FC FF FF               jne 0x1402fc9d6
002FCDC8  44 8B 44 24 24                  mov r8d, dword ptr [rsp + 0x24]
002FCDCD  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
002FCDD1  4E 8D 1C C5 00 00 00 00         lea r11, [r8*8]
002FCDD9  4D 8B 14 03                     mov r10, qword ptr [r11 + rax]
002FCDDD  4C 39 54 24 30                  cmp qword ptr [rsp + 0x30], r10
002FCDE2  0F 85 3C 2D 3E 00               jne 0x1406dfb24
002FCDE8  83 FB 48                        cmp ebx, 0x48
002FCDEB  0F 84 33 2D 3E 00               je 0x1406dfb24
002FCDF1  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
002FCDF6  E9 1B FD FF FF                  jmp 0x1402fcb16
002FCDFB  8B DA                           mov ebx, edx
002FCDFD  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
002FCE01  E9 D0 FB FF FF                  jmp 0x1402fc9d6
002FCE06  F0 FF 4F 0C                     lock dec dword ptr [rdi + 0xc]
002FCE0A  E9 83 FE FF FF                  jmp 0x1402fcc92
002FCE0F  41 B8 04 00 00 00               mov r8d, 4
002FCE15  E8 C2 19 00 00                  call 0x1402fe7dc
002FCE1A  41 8B 87 98 05 00 00            mov eax, dword ptr [r15 + 0x598]
002FCE21  85 C0                           test eax, eax
002FCE23  0F 85 86 2D 3E 00               jne 0x1406dfbaf
002FCE29  49 8B 87 10 06 00 00            mov rax, qword ptr [r15 + 0x610]
002FCE30  48 03 C0                        add rax, rax
002FCE33  49 39 87 08 06 00 00            cmp qword ptr [r15 + 0x608], rax
002FCE3A  0F 8C 6F 2D 3E 00               jl 0x1406dfbaf
002FCE40  49 8B CF                        mov rcx, r15
002FCE43  E8 20 69 35 00                  call 0x140653768
002FCE48  90                              nop
002FCE49  E9 61 2D 3E 00                  jmp 0x1406dfbaf
002FCE4E  48 85 FF                        test rdi, rdi
002FCE51  74 04                           je 0x1402fce57
002FCE53  F0 FF 4F 0C                     lock dec dword ptr [rdi + 0xc]
002FCE57  49 8B CF                        mov rcx, r15
002FCE5A  E8 81 4A 0F 00                  call 0x1403f18e0
002FCE5F  33 C0                           xor eax, eax
002FCE61  E9 C8 FD FF FF                  jmp 0x1402fcc2e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpReserveTraceBuffer(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rbp;
    v_stack_p20 = v_rsi;
    v_rsp = (v_rsp) - (80);
    if ((*(unsigned int *)(a1 + 16)) < 0) goto loc_002FCE57;
    if (((unsigned int)(a2)) > (*(unsigned int *)(a1 + 8))) goto loc_002FCE57;
    a4 = (unsigned int)((a2 + 7) & (0xFFFFFFF8ULL));
    v_stack_m50 = (unsigned int)(a4);
    v_stack_m58 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    v_stack_m54 = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
loc_002FC914:
    a4 = 0;
    if ((*(unsigned __int64 *)(a1 + 1360)) != (*(unsigned __int64 *)(v_rip + 13410672))) goto loc_002FCD9A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 13410620))))) goto loc_002FCCFF;
loc_002FC950:
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 13419292 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)) * 8) + 35752)) + (320);
loc_002FC95E:
    if (((*(unsigned int *)(a1 + 12)) & (0x10000000ULL)) == 0) goto loc_002FCAC0;
loc_002FC973:
    v_stack_p8 = 0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 128))) & (15)) == 0) goto loc_002FC99C;
loc_002FC987:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 128))) & (15)) == 0) goto loc_002FC99C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a1 + 128))) & (15)) != 0) goto loc_002FC987;
loc_002FC99C:
    if (*(unsigned __int64 *)(a1 + 128) == 0) goto loc_002FCB7D;
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(a1 + 128)))) & (15));
    if (((unsigned int)(result)) < 1) goto loc_002FCD41;
    v_rdi = (*(unsigned __int64 *)(a1 + 128)) & (-16);
    if (((unsigned int)(result)) == 1) goto loc_002FCCBF;
loc_002FC9C0:
    if (v_rdi == 0) goto loc_002FC9DE;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
loc_002FC9D6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) goto loc_002FCAF8;
loc_002FC9DE:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12888936)))) & (3)) != 0) goto loc_002FCE4E;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 12))) & (0x400ULL));
loc_002FC9F7:
    result = EtwpDequeueFreeBuffer(a1, (unsigned int)(*(unsigned int *)(a1 + 4)), (unsigned int)(*(unsigned int *)(a1)), a4);
    if (result == 0) goto loc_002FCB9F;
    if (!(condition_is_below)) {
        *(unsigned __int16 *)(result + 40) = (unsigned __int16)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 32)) + 36)));
    }
loc_002FCA1E:
    if ((unsigned int)(v_r14) == 0) {
        *(unsigned __int64 *)(result + 32) = v_rdi;
    }
loc_002FCA2D:
    result = (*(unsigned __int64 *)(a1 + 128)) ^ (v_rdi);
    if (result > 15) goto loc_002FCA4A;
    a1 = (result) | (15);
    if (condition_is_not_equal) goto loc_002FCAB8;
loc_002FCA4A:
    v_rbp = (*(unsigned __int64 *)(a1 + 128)) & (-16);
    if (v_rbp != v_rdi) goto loc_002FCACF;
    if (v_rbp == 0) goto loc_002FCB54;
    if (condition_is_below) goto loc_002FCB85;
    *(unsigned int *)(v_rbp + 44) = 3;
    result = EtwpGetLoggerTimeStamp(a1, result, (unsigned int)(*(unsigned int *)(a1)), a4);
    *(unsigned __int64 *)(v_rbp + 16) = result;
loc_002FCA80:
    v_rbx = (unsigned int)((*(unsigned __int64 *)(a1 + 128)) & (15));
    v_rbx = (unsigned int)(~(v_rbx));
    if ((unsigned int)(v_r14) == 0) goto loc_002FCC4D;
loc_002FCA92:
    v_rbx = 0;
loc_002FCA94:
    if (((*(unsigned int *)(a1 + 12)) & (0x4000000ULL)) != 0) goto loc_002FCD07;
loc_002FCAA2:
    if (sign_flag) goto loc_002FCE57;
    goto loc_002FC914;
loc_002FCAB8:
    goto loc_002FCA2D;
loc_002FCAC0:
    goto loc_002FC973;
loc_002FCACF:
    if (v_rbp == 0) goto loc_002FCC89;
    if (v_rdi != 0) {
    }
    if ((unsigned int)(v_r14) != 0) goto loc_002FCB4A;
    a3 = 0;
    result = EtwpEnqueueAvailableBuffer(a1, (unsigned int)(v_stack_m58), a3, a4);
    goto loc_002FCA92;
loc_002FCAF8:
    if (((*(unsigned int *)(a1 + 816)) & (0x8000000ULL)) != 0) goto loc_002FCDAD;
    result = EtwpGetLoggerTimeStamp(a1, (unsigned int)(v_stack_m58), a3, a4);
loc_002FCB16:
    *(unsigned __int64 *)(a4) = result;
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_002FCDFB;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) + (unsigned int)(v_stack_m50) * 1)) <= v_stack_m58) goto loc_002FCBE8;
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    goto loc_002FC9DE;
loc_002FCB4A:
    result = EtwpEnqueueOverflowBuffer(result + (unsigned int)(v_stack_m50) * 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_m54), (unsigned int)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCB54:
    if ((*(unsigned int *)(a1 + 208)) <= 0) goto loc_002FCA92;
    a2 = (((a5) & (0x600ULL)) != 0) ? 1 : 0;
    result = EtwpRequestFlushTimer(a1, a2, (unsigned int)(v_stack_m54), (unsigned int)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCB7D:
    goto loc_002FC9DE;
loc_002FCB85:
    if (condition_is_below) goto loc_002FCE0F;
    a3 = 0;
    result = EtwpEnqueueAvailableBuffer(a1, v_rbp, a3, (unsigned int)(v_stack_m50));
    goto loc_002FCA80;
loc_002FCB9F:
    if (((a5) & (512)) != 0) goto loc_002FCBD5;
    result = KeGetEffectiveIrql(a1, v_rbp, a3, (unsigned int)(v_stack_m50));
    if (((unsigned __int8)(result)) > 2) goto loc_002FCBD5;
    if (((*(unsigned int *)(a1 + 12)) & (0x40000ULL)) != 0) goto loc_002FCBD5;
    result = EtwpAllocateFreeBuffers(a1, 1, a3, (unsigned int)(v_stack_m50));
    if (((unsigned int)(result)) == 1) goto loc_002FC9F7;
loc_002FCBD5:
    if ((unsigned int)(v_stack_m50) != 0) {
    }
    goto loc_002FCA94;
loc_002FCBE8:
    if (((*(unsigned int *)(a1 + 12)) & (0x400ULL)) == 0) goto loc_002FCC11;
    if ((*(unsigned __int64 *)(a4)) <= (*(unsigned __int64 *)((unsigned int)(v_stack_m50) + 16))) goto loc_002FCC11;
loc_002FCC00:
    if ((*(unsigned __int64 *)(a4)) == (*(unsigned __int64 *)((unsigned int)(v_stack_m50) + 16))) goto loc_002FCC11;
    if ((*(unsigned __int64 *)(a4)) > (*(unsigned __int64 *)((unsigned int)(v_stack_m50) + 16))) goto loc_002FCC00;
loc_002FCC11:
    *(unsigned __int64 *)(a3) = (unsigned int)(v_stack_m50);
    *(unsigned __int64 *)(a3 + 8) = *(unsigned __int64 *)(v_r14) + (unsigned int)((unsigned int)((unsigned int)(v_stack_m54))) * 8;
    *(unsigned int *)(a3 + 16) = 1;
loc_002FCC2E:
    return (unsigned int)(v_stack_m50) + 1 * 1;
loc_002FCC4D:
    result = EtwpBuffersFlushRequired(a1, 1, a3, (unsigned int)(v_stack_m50));
    if ((unsigned __int8)(result) == 0) goto loc_002FCA92;
    if (((a5) & (0x600ULL)) != 0) goto loc_002FCC99;
    result = KeGetEffectiveIrql(a1, 1, a3, (unsigned int)(v_stack_m50));
    if (((unsigned __int8)(result)) > 2) goto loc_002FCC99;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(a1 + 480, a2, a3, (unsigned int)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCC89:
    if ((unsigned int)(v_stack_m50) != 0) goto loc_002FCE06;
loc_002FCC92:
    v_rdi = 0;
    goto loc_002FCA1E;
loc_002FCC99:
    if (condition_is_below) goto loc_002FCA92;
    a3 = 0;
    a2 = 0;
    result = KeInsertQueueDpc(a1 + 568, a2, a3, (unsigned int)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCCBF:
loc_002FCCCA:
    a1 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72))) & (15));
    a1 = (a1) + (15);
    if (a1 > 15) goto loc_002FCD90;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72))) & (-16);
    if (0 != a1) goto loc_002FCD90;
    if (0 == a1) goto loc_002FC9C0;
    goto loc_002FCCCA;
loc_002FCCFF:
    goto loc_002FC950;
loc_002FCD07:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, (unsigned int)(v_stack_m50));
    a4 = (result) - (result);
loc_002FCD1E:
    if (*(unsigned __int64 *)(a1 + 1544) != 0) goto loc_002FCD7A;
loc_002FCD2D:
    if (*(unsigned __int64 *)(a1 + 1544) == 0) goto loc_002FCAA2;
    goto loc_002FCD1E;
loc_002FCD41:
    result = EtwpLockBufferList(0, v_stack_p30, *(unsigned __int64 *)(a1 + 1544), a4);
    v_rdi = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72))) & (-16);
    if (!(condition_is_equal)) {
    }
    result = EtwpUnlockBufferList(0, v_stack_p30, *(unsigned __int64 *)(a1 + 1544), a4);
    a4 = 0;
    goto loc_002FC9C0;
loc_002FCD7A:
    result = (a4 + *(unsigned __int64 *)(a1 + 1544) * 2) + (*(unsigned __int64 *)(a1 + 1544));
    a2 = (unsigned int)(((unsigned int)(v_stack_m30)) & (3));
    a1 = (a2 + result * 1) >> (2);
    goto loc_002FCD2D;
loc_002FCD90:
    goto loc_002FC9C0;
loc_002FCD9A:
    v_r14 = (*(unsigned __int64 *)(v_stack_m28 + 64)) << (6);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(result + 4416));
    goto loc_002FC95E;
loc_002FCDAD:
    result = EtwpGetTimeStampAndQpcDelta(a1, v_stack_m18, v_stack_m20, a4);
    if ((unsigned int)(result) != 0) goto loc_002FC9D6;
    goto loc_002FCB16;
loc_002FCDFB:
    goto loc_002FC9D6;
loc_002FCE06:
    goto loc_002FCC92;
loc_002FCE0F:
    result = EtwpEnqueueAvailableBuffer(a1, (unsigned int)(v_stack_m30), 4, a4);
    result = (*(unsigned __int64 *)(a1 + 1552)) + (*(unsigned __int64 *)(a1 + 1552));
    result = EtwpReenableCompression(a1, (unsigned int)(v_stack_m30), 4, a4);
loc_002FCE4E:
    if (v_rdi != 0) {
    }
    result = EtwpUpdateEventsLostCount(a1, (unsigned int)(v_stack_m30), 4, a4);
    result = 0;
    goto loc_002FCC2E;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpReserveTraceBuffer(void *Arg1, int64_t Arg2, void *Arg3, void *Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p30;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rbp;
    v_stack_p20 = local_rsi;
    local_rsp = (local_rsp) - (80);
    if ((*(uint32_t *)(arg1 + 0x10)) < 0) goto loc_002FCE57;
    if (((uint32_t)(Arg2)) > (*(uint32_t *)(arg1 + 0x8))) goto loc_002FCE57;
    Arg4 = (uint32_t)((Arg2 + 7) & (0xFFFFFFF8ULL));
    v_stack_m50 = (uint32_t)(Arg4);
    v_stack_m58 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    v_stack_m54 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1)));
loc_002FC914:
    Arg4 = 0;
    if ((*(uint64_t *)(arg1 + 0x550)) != (*(uint64_t *)(v_rip + 0xCCA170))) goto loc_002FCD9A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xCCA13C))))) goto loc_002FCCFF;
loc_002FC950:
    local_r14 = (*(uint64_t *)(*(uint64_t *)(v_rip + 0xCCC31C + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)) * 8) + 0x8BA8)) + (320);
loc_002FC95E:
    if (((*(uint32_t *)(arg1 + 0xC)) & (0x10000000ULL)) == 0) goto loc_002FCAC0;
loc_002FC973:
    v_stack_p8 = 0;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x80))) & (15)) == 0) goto loc_002FC99C;
loc_002FC987:
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x80))) & (15)) == 0) goto loc_002FC99C;
    if ((((uint8_t)(*(uint64_t *)(arg1 + 0x80))) & (15)) != 0) goto loc_002FC987;
loc_002FC99C:
    if (*(uint64_t *)(arg1 + 0x80) == 0) goto loc_002FCB7D;
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(arg1 + 0x80)))) & (15));
    if (((uint32_t)(result)) < 1) goto loc_002FCD41;
    local_rdi = (*(uint64_t *)(arg1 + 0x80)) & (-16);
    if (((uint32_t)(result)) == 1) goto loc_002FCCBF;
loc_002FC9C0:
    if (local_rdi == 0) goto loc_002FC9DE;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
loc_002FC9D6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) goto loc_002FCAF8;
loc_002FC9DE:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC4AB68)))) & (3)) != 0) goto loc_002FCE4E;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC))) & (0x400ULL));
loc_002FC9F7:
    result = EtwpDequeueFreeBuffer(Arg1, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), (uint32_t)(*(uint32_t *)(arg1)), Arg4);
    if (result == 0) goto loc_002FCB9F;
    if (!(condition_is_below)) {
        *(uint16_t *)(result + 0x28) = (uint16_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x20)) + 0x24)));
    }
loc_002FCA1E:
    if ((uint32_t)(local_r14) == 0) {
        *(uint64_t *)(result + 0x20) = local_rdi;
    }
loc_002FCA2D:
    result = (*(uint64_t *)(arg1 + 0x80)) ^ (local_rdi);
    if (result > 15) goto loc_002FCA4A;
    Arg1 = (result) | (15);
    if (condition_is_not_equal) goto loc_002FCAB8;
loc_002FCA4A:
    local_rbp = (*(uint64_t *)(arg1 + 0x80)) & (-16);
    if (local_rbp != local_rdi) goto loc_002FCACF;
    if (local_rbp == 0) goto loc_002FCB54;
    if (condition_is_below) goto loc_002FCB85;
    *(uint32_t *)(local_rbp + 0x2C) = 3;
    result = EtwpGetLoggerTimeStamp(Arg1, result, (uint32_t)(*(uint32_t *)(arg1)), Arg4);
    *(uint64_t *)(local_rbp + 0x10) = result;
loc_002FCA80:
    local_rbx = (uint32_t)((*(uint64_t *)(arg1 + 0x80)) & (15));
    local_rbx = (uint32_t)(~(local_rbx));
    if ((uint32_t)(local_r14) == 0) goto loc_002FCC4D;
loc_002FCA92:
    local_rbx = 0;
loc_002FCA94:
    if (((*(uint32_t *)(arg1 + 0xC)) & (0x4000000ULL)) != 0) goto loc_002FCD07;
loc_002FCAA2:
    if (sign_flag) goto loc_002FCE57;
    goto loc_002FC914;
loc_002FCAB8:
    goto loc_002FCA2D;
loc_002FCAC0:
    goto loc_002FC973;
loc_002FCACF:
    if (local_rbp == 0) goto loc_002FCC89;
    if (local_rdi != 0) {
    }
    if ((uint32_t)(local_r14) != 0) goto loc_002FCB4A;
    Arg3 = 0;
    result = EtwpEnqueueAvailableBuffer(Arg1, (uint32_t)(v_stack_m58), Arg3, Arg4);
    goto loc_002FCA92;
loc_002FCAF8:
    if (((*(uint32_t *)(arg1 + 0x330)) & (0x8000000ULL)) != 0) goto loc_002FCDAD;
    result = EtwpGetLoggerTimeStamp(Arg1, (uint32_t)(v_stack_m58), Arg3, Arg4);
loc_002FCB16:
    *(uint64_t *)(arg4) = result;
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_002FCDFB;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) + (uint32_t)(v_stack_m50) * 1)) <= v_stack_m58) goto loc_002FCBE8;
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    goto loc_002FC9DE;
loc_002FCB4A:
    result = EtwpEnqueueOverflowBuffer(result + (uint32_t)(v_stack_m50) * 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_m54), (uint32_t)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCB54:
    if ((*(uint32_t *)(arg1 + 0xD0)) <= 0) goto loc_002FCA92;
    Arg2 = (((Arg5) & (0x600ULL)) != 0) ? 1 : 0;
    result = EtwpRequestFlushTimer(Arg1, Arg2, (uint32_t)(v_stack_m54), (uint32_t)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCB7D:
    goto loc_002FC9DE;
loc_002FCB85:
    if (condition_is_below) goto loc_002FCE0F;
    Arg3 = 0;
    result = EtwpEnqueueAvailableBuffer(Arg1, local_rbp, Arg3, (uint32_t)(v_stack_m50));
    goto loc_002FCA80;
loc_002FCB9F:
    if (((Arg5) & (512)) != 0) goto loc_002FCBD5;
    result = KeGetEffectiveIrql(Arg1, local_rbp, Arg3, (uint32_t)(v_stack_m50));
    if (((uint8_t)(result)) > 2) goto loc_002FCBD5;
    if (((*(uint32_t *)(arg1 + 0xC)) & (0x40000ULL)) != 0) goto loc_002FCBD5;
    result = EtwpAllocateFreeBuffers(Arg1, 1, Arg3, (uint32_t)(v_stack_m50));
    if (((uint32_t)(result)) == 1) goto loc_002FC9F7;
loc_002FCBD5:
    if ((uint32_t)(v_stack_m50) != 0) {
    }
    goto loc_002FCA94;
loc_002FCBE8:
    if (((*(uint32_t *)(arg1 + 0xC)) & (0x400ULL)) == 0) goto loc_002FCC11;
    if ((*(uint64_t *)(arg4)) <= (*(uint64_t *)((uint32_t)(v_stack_m50) + 0x10))) goto loc_002FCC11;
loc_002FCC00:
    if ((*(uint64_t *)(arg4)) == (*(uint64_t *)((uint32_t)(v_stack_m50) + 0x10))) goto loc_002FCC11;
    if ((*(uint64_t *)(arg4)) > (*(uint64_t *)((uint32_t)(v_stack_m50) + 0x10))) goto loc_002FCC00;
loc_002FCC11:
    *(uint64_t *)(arg3) = (uint32_t)(v_stack_m50);
    *(uint64_t *)(arg3 + 0x8) = *(uint64_t *)(local_r14) + (uint32_t)((uint32_t)((uint32_t)(v_stack_m54))) * 8;
    *(uint32_t *)(arg3 + 0x10) = 1;
loc_002FCC2E:
    return (uint32_t)(v_stack_m50) + 1 * 1;
loc_002FCC4D:
    result = EtwpBuffersFlushRequired(Arg1, 1, Arg3, (uint32_t)(v_stack_m50));
    if ((uint8_t)(result) == 0) goto loc_002FCA92;
    if (((Arg5) & (0x600ULL)) != 0) goto loc_002FCC99;
    result = KeGetEffectiveIrql(Arg1, 1, Arg3, (uint32_t)(v_stack_m50));
    if (((uint8_t)(result)) > 2) goto loc_002FCC99;
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(Arg1 + 480, Arg2, Arg3, (uint32_t)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCC89:
    if ((uint32_t)(v_stack_m50) != 0) goto loc_002FCE06;
loc_002FCC92:
    local_rdi = 0;
    goto loc_002FCA1E;
loc_002FCC99:
    if (condition_is_below) goto loc_002FCA92;
    Arg3 = 0;
    Arg2 = 0;
    result = KeInsertQueueDpc(Arg1 + 568, Arg2, Arg3, (uint32_t)(v_stack_m50));
    goto loc_002FCA92;
loc_002FCCBF:
loc_002FCCCA:
    Arg1 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48))) & (15));
    Arg1 = (Arg1) + (15);
    if (Arg1 > 15) goto loc_002FCD90;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48))) & (-16);
    if (0 != Arg1) goto loc_002FCD90;
    if (0 == Arg1) goto loc_002FC9C0;
    goto loc_002FCCCA;
loc_002FCCFF:
    goto loc_002FC950;
loc_002FCD07:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, (uint32_t)(v_stack_m50));
    Arg4 = (result) - (result);
loc_002FCD1E:
    if (*(uint64_t *)(arg1 + 0x608) != 0) goto loc_002FCD7A;
loc_002FCD2D:
    if (*(uint64_t *)(arg1 + 0x608) == 0) goto loc_002FCAA2;
    goto loc_002FCD1E;
loc_002FCD41:
    result = EtwpLockBufferList(0, v_stack_p30, *(uint64_t *)(arg1 + 0x608), Arg4);
    local_rdi = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48))) & (-16);
    if (!(condition_is_equal)) {
    }
    result = EtwpUnlockBufferList(0, v_stack_p30, *(uint64_t *)(arg1 + 0x608), Arg4);
    Arg4 = 0;
    goto loc_002FC9C0;
loc_002FCD7A:
    result = (Arg4 + *(uint64_t *)(arg1 + 0x608) * 2) + (*(uint64_t *)(arg1 + 0x608));
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m30)) & (3));
    Arg1 = (Arg2 + result * 1) >> (2);
    goto loc_002FCD2D;
loc_002FCD90:
    goto loc_002FC9C0;
loc_002FCD9A:
    local_r14 = (*(uint64_t *)(v_stack_m28 + 0x40)) << (6);
    local_r14 = (local_r14) + (*(uint64_t *)(result + 0x1140));
    goto loc_002FC95E;
loc_002FCDAD:
    result = EtwpGetTimeStampAndQpcDelta(Arg1, v_stack_m18, v_stack_m20, Arg4);
    if ((uint32_t)(result) != 0) goto loc_002FC9D6;
    goto loc_002FCB16;
loc_002FCDFB:
    goto loc_002FC9D6;
loc_002FCE06:
    goto loc_002FCC92;
loc_002FCE0F:
    result = EtwpEnqueueAvailableBuffer(Arg1, (uint32_t)(v_stack_m30), 4, Arg4);
    result = (*(uint64_t *)(arg1 + 0x610)) + (*(uint64_t *)(arg1 + 0x610));
    result = EtwpReenableCompression(Arg1, (uint32_t)(v_stack_m30), 4, Arg4);
loc_002FCE4E:
    if (local_rdi != 0) {
    }
    result = EtwpUpdateEventsLostCount(Arg1, (uint32_t)(v_stack_m30), 4, Arg4);
    result = 0;
    goto loc_002FCC2E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |
| `Arg1` | `+ 0xD0` | `32` | `R` |
| `Arg1` | `+ 0x1E0` | `64` | `R` |
| `Arg1` | `+ 0x238` | `64` | `R` |
| `Arg1` | `+ 0x330` | `32` | `R` |
| `Arg1` | `+ 0x338` | `32` | `R/W` |
| `Arg1` | `+ 0x550` | `64` | `R` |
| `Arg1` | `+ 0x598` | `32` | `R` |
| `Arg1` | `+ 0x600` | `64` | `R/W` |
| `Arg1` | `+ 0x608` | `64` | `R` |
| `Arg1` | `+ 0x610` | `64` | `R` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |
| `Arg3` | `+ 0x10` | `32` | `W` |
| `Arg4` | `+ 0x0` | `64` | `R` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FC8C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
