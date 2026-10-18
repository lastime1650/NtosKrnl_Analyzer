# CcAsyncReadWorker

- RVA: `0x0045DB10`–`0x0045E15A` (길이 `1,610` bytes)
- VA: `0x000000014045DB10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A969C`
- 디코드: `393`개 명령, `1,610/1,610` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **30**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0045DBA0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0045DBB1` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0045DC3D` → [MmWaitMultipleForCacheManagerPrefetch](../36/MmWaitMultipleForCacheManagerPrefetch_function_0036D470.md) (function, `0x0036D470`)
- `0x0045DC81` → [KeWaitForMultipleObjects](../20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x0045DD2C` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0045DD45` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0045DD7F` → [CcFindNextWorkQueueEntry](../35/CcFindNextWorkQueueEntry_function_00356BFC.md) (function, `0x00356BFC`)
- `0x0045DDBB` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0045DDC3` → [CcAsyncReadPrefetch](CcAsyncReadPrefetch_function_0045E540.md) (function, `0x0045E540`)
- `0x0045DE1A` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0045DE33` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0045DE6F` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0045DEA5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0045DEF0` → [CcCompleteAsyncRead](CcCompleteAsyncRead_function_0045E7DC.md) (function, `0x0045E7DC`)
- `0x0045DEF8` → [CcFreeWorkQueueEntry](../35/CcFreeWorkQueueEntry_function_0035723C.md) (function, `0x0035723C`)
- `0x0045DF65` → [CcCompleteAsyncRead](CcCompleteAsyncRead_function_0045E7DC.md) (function, `0x0045E7DC`)
- `0x0045DF6D` → [CcFreeWorkQueueEntry](../35/CcFreeWorkQueueEntry_function_0035723C.md) (function, `0x0035723C`)
- `0x0045DFA6` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0045DFC0` → [CcShouldSpinAsyncReadWorkerThread](CcShouldSpinAsyncReadWorkerThread_function_0045EB28.md) (function, `0x0045EB28`)
- `0x0045DFCD` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0045DFE6` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0045E024` → [KeAbPostRelease](../2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0045E053` → [ExQueueWorkItemToPartition](../35/ExQueueWorkItemToPartition_function_00356E2C.md) (function, `0x00356E2C`)
- `0x0045E06F` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0045E07C` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0045E086` → [ExfReleasePushLock](../26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0045E0AB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0045E0EA` → [CcPostWorkQueueAsyncRead](CcPostWorkQueueAsyncRead_function_0045D624.md) (function, `0x0045D624`)
- `0x0045E144` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0045E150` → [CcDereferencePartitionAndPrivateVolumeCacheMap](../38/CcDereferencePartitionAndPrivateVolumeCacheMap_function_0038B94C.md) (function, `0x0038B94C`)

### Direct callers
- [CcAsyncReadWorkerThread](../57/CcAsyncReadWorkerThread_function_0057F560.md) at `0x0057F5DD`

### Static image references
- `0x0045DB3F` → RVA `0x00E0A740` (`.data`; read)
- `0x0045DBED` → RVA `0x00E65B88` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0045DEA5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0045E0AB` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x0045E144` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0045E0CD` → [sub_006F2088](../6F/Unknown_function_006F2088.md) (`tail-transfer`)
  - `0x0045E0E0` → [sub_006F2088](../6F/Unknown_function_006F2088.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0045DB10  48 85 C9                        test rcx, rcx
0045DB13  0F 84 7B 03 00 00               je 0x14045de94
0045DB19  48 8B C4                        mov rax, rsp
0045DB1C  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
0045DB20  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
0045DB24  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0045DB28  55                              push rbp
0045DB29  41 54                           push r12
0045DB2B  41 55                           push r13
0045DB2D  41 56                           push r14
0045DB2F  41 57                           push r15
0045DB31  48 8D A8 B8 FB FF FF            lea rbp, [rax - 0x448]
0045DB38  48 81 EC 20 05 00 00            sub rsp, 0x520
0045DB3F  48 8B 05 FA CB 9A 00            mov rax, qword ptr [rip + 0x9acbfa]
0045DB46  48 33 C4                        xor rax, rsp
0045DB49  48 89 85 10 04 00 00            mov qword ptr [rbp + 0x410], rax
0045DB50  8B 59 24                        mov ebx, dword ptr [rcx + 0x24]
0045DB53  33 C0                           xor eax, eax
0045DB55  48 8B 71 38                     mov rsi, qword ptr [rcx + 0x38]
0045DB59  44 8B F0                        mov r14d, eax
0045DB5C  4C 8B 79 48                     mov r15, qword ptr [rcx + 0x48]
0045DB60  0F 57 C0                        xorps xmm0, xmm0
0045DB63  48 8B 79 40                     mov rdi, qword ptr [rcx + 0x40]
0045DB67  41 BC 00 02 00 00               mov r12d, 0x200
0045DB6D  44 8D 68 03                     lea r13d, [rax + 3]
0045DB71  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0045DB76  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0045DB79  45 8B C4                        mov r8d, r12d
0045DB7C  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
0045DB80  33 D2                           xor edx, edx
0045DB82  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0045DB86  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0045DB8A  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
0045DB8E  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
0045DB92  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
0045DB97  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0045DB9C  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
0045DBA0  E8 9B 90 26 00                  call 0x1406c6c40
0045DBA5  45 8B C4                        mov r8d, r12d
0045DBA8  48 8D 8D 10 02 00 00            lea rcx, [rbp + 0x210]
0045DBAF  33 D2                           xor edx, edx
0045DBB1  E8 8A 90 26 00                  call 0x1406c6c40
0045DBB6  49 8B 87 10 01 00 00            mov rax, qword ptr [r15 + 0x110]
0045DBBD  48 8D 0C 5B                     lea rcx, [rbx + rbx*2]
0045DBC1  48 89 4D 98                     mov qword ptr [rbp - 0x68], rcx
0045DBC5  45 33 C0                        xor r8d, r8d
0045DBC8  8B D3                           mov edx, ebx
0045DBCA  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
0045DBCF  4C 8D 24 C8                     lea r12, [rax + rcx*8]
0045DBD3  48 69 CB 94 01 00 00            imul rcx, rbx, 0x194
0045DBDA  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0045DBDF  48 8D 9F 88 04 00 00            lea rbx, [rdi + 0x488]
0045DBE6  49 03 8F 18 01 00 00            add rcx, qword ptr [r15 + 0x118]
0045DBED  44 38 05 94 7F A0 00            cmp byte ptr [rip + 0xa07f94], r8b
0045DBF4  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
0045DBF9  75 07                           jne 0x14045dc02
0045DBFB  48 8D 9E C8 04 00 00            lea rbx, [rsi + 0x4c8]
0045DC02  41 83 7F 04 01                  cmp dword ptr [r15 + 4], 1
0045DC07  48 8D 86 18 05 00 00            lea rax, [rsi + 0x518]
0045DC0E  4C 89 65 88                     mov qword ptr [rbp - 0x78], r12
0045DC12  74 07                           je 0x14045dc1b
0045DC14  48 8D 87 98 04 00 00            lea rax, [rdi + 0x498]
0045DC1B  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0045DC1F  BF 02 00 00 00                  mov edi, 2
0045DC24  41 83 FE 3F                     cmp r14d, 0x3f
0045DC28  0F 82 DC 00 00 00               jb 0x14045dd0a
0045DC2E  45 85 F6                        test r14d, r14d
0045DC31  74 26                           je 0x14045dc59
0045DC33  4D 8B C4                        mov r8, r12
0045DC36  48 8D 4D 10                     lea rcx, [rbp + 0x10]
0045DC3A  41 8B D6                        mov edx, r14d
0045DC3D  E8 2E F8 F0 FF                  call 0x14036d470
0045DC42  44 8B F8                        mov r15d, eax
0045DC45  41 3B C6                        cmp eax, r14d
0045DC48  0F 83 4E 04 00 00               jae 0x14045e09c
0045DC4E  41 BD 01 00 00 00               mov r13d, 1
0045DC54  45 33 C0                        xor r8d, r8d
0045DC57  EB 58                           jmp 0x14045dcb1
0045DC59  48 8D 45 B0                     lea rax, [rbp - 0x50]
0045DC5D  41 B9 08 00 00 00               mov r9d, 8
0045DC63  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0045DC68  48 8D 55 88                     lea rdx, [rbp - 0x78]
0045DC6C  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
0045DC71  8B CF                           mov ecx, edi
0045DC73  44 88 44 24 28                  mov byte ptr [rsp + 0x28], r8b
0045DC78  44 88 44 24 20                  mov byte ptr [rsp + 0x20], r8b
0045DC7D  45 8D 41 F9                     lea r8d, [r9 - 7]
0045DC81  E8 8A F4 DA FF                  call 0x14020d110
0045DC86  45 33 C0                        xor r8d, r8d
0045DC89  44 8B F8                        mov r15d, eax
0045DC8C  85 C0                           test eax, eax
0045DC8E  0F 85 FC 03 00 00               jne 0x14045e090
0045DC94  45 8B E8                        mov r13d, r8d
0045DC97  41 8B CD                        mov ecx, r13d
0045DC9A  45 85 ED                        test r13d, r13d
0045DC9D  0F 84 F3 01 00 00               je 0x14045de96
0045DCA3  83 F9 01                        cmp ecx, 1
0045DCA6  0F 85 A1 01 00 00               jne 0x14045de4d
0045DCAC  41 3B C6                        cmp eax, r14d
0045DCAF  73 36                           jae 0x14045dce7
0045DCB1  0F AE E8                        lfence
0045DCB4  41 8B F7                        mov esi, r15d
0045DCB7  4C 8D A5 10 02 00 00            lea r12, [rbp + 0x210]
0045DCBE  4D 8D 24 F4                     lea r12, [r12 + rsi*8]
0045DCC2  49 8B 3C 24                     mov rdi, qword ptr [r12]
0045DCC6  48 85 FF                        test rdi, rdi
0045DCC9  74 0D                           je 0x14045dcd8
0045DCCB  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
0045DCCF  48 85 C9                        test rcx, rcx
0045DCD2  0F 85 C8 01 00 00               jne 0x14045dea0
0045DCD8  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0045DCDD  BF 02 00 00 00                  mov edi, 2
0045DCE2  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
0045DCE7  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
0045DCEC  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0045DCF1  44 39 44 24 40                  cmp dword ptr [rsp + 0x40], r8d
0045DCF6  0F 84 28 FF FF FF               je 0x14045dc24
0045DCFC  45 85 F6                        test r14d, r14d
0045DCFF  0F 84 60 01 00 00               je 0x14045de65
0045DD05  E9 1A FF FF FF                  jmp 0x14045dc24
0045DD0A  48 8B CA                        mov rcx, rdx
0045DD0D  48 C1 E1 04                     shl rcx, 4
0045DD11  49 03 8F 00 01 00 00            add rcx, qword ptr [r15 + 0x100]
0045DD18  48 39 09                        cmp qword ptr [rcx], rcx
0045DD1B  0F 84 0D FF FF FF               je 0x14045dc2e
0045DD21  45 8B E8                        mov r13d, r8d
0045DD24  45 33 C0                        xor r8d, r8d
0045DD27  33 D2                           xor edx, edx
0045DD29  48 8B CB                        mov rcx, rbx
0045DD2C  E8 FF 24 DB FF                  call 0x140210230
0045DD31  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0045DD37  48 8B F8                        mov rdi, rax
0045DD3A  73 0E                           jae 0x14045dd4a
0045DD3C  4C 8B C3                        mov r8, rbx
0045DD3F  48 8B D0                        mov rdx, rax
0045DD42  48 8B CB                        mov rcx, rbx
0045DD45  E8 46 1F DB FF                  call 0x14020fc90
0045DD4A  48 85 FF                        test rdi, rdi
0045DD4D  74 04                           je 0x14045dd53
0045DD4F  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0045DD53  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
0045DD58  48 C1 E6 04                     shl rsi, 4
0045DD5C  45 33 C9                        xor r9d, r9d
0045DD5F  4D 8B 87 00 01 00 00            mov r8, qword ptr [r15 + 0x100]
0045DD66  4C 03 C6                        add r8, rsi
0045DD69  4D 39 00                        cmp qword ptr [r8], r8
0045DD6C  0F 84 F3 02 00 00               je 0x14045e065
0045DD72  41 83 FE 3F                     cmp r14d, 0x3f
0045DD76  0F 83 FB 01 00 00               jae 0x14045df77
0045DD7C  49 8B D7                        mov rdx, r15
0045DD7F  E8 78 8E EF FF                  call 0x140356bfc
0045DD84  48 8B F8                        mov rdi, rax
0045DD87  0F 0D 0B                        prefetchw byte ptr [rbx]
0045DD8A  48 8B 03                        mov rax, qword ptr [rbx]
0045DD8D  48 8B C8                        mov rcx, rax
0045DD90  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0045DD94  48 83 F9 10                     cmp rcx, 0x10
0045DD98  B9 00 00 00 00                  mov ecx, 0
0045DD9D  48 8D 50 F0                     lea rdx, [rax - 0x10]
0045DDA1  48 0F 46 D1                     cmovbe rdx, rcx
0045DDA5  A8 02                           test al, 2
0045DDA7  0F 85 BF 02 00 00               jne 0x14045e06c
0045DDAD  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0045DDB2  0F 85 B4 02 00 00               jne 0x14045e06c
0045DDB8  48 8B CB                        mov rcx, rbx
0045DDBB  E8 40 38 E8 FF                  call 0x1402e1600
0045DDC0  48 8B CF                        mov rcx, rdi
0045DDC3  E8 78 07 00 00                  call 0x14045e540
0045DDC8  84 C0                           test al, al
0045DDCA  0F 84 92 01 00 00               je 0x14045df62
0045DDD0  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
0045DDD4  48 8B 11                        mov rdx, qword ptr [rcx]
0045DDD7  48 85 D2                        test rdx, rdx
0045DDDA  0F 84 C6 02 00 00               je 0x14045e0a6
0045DDE0  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0045DDE5  41 8B C6                        mov eax, r14d
0045DDE8  41 FF C6                        inc r14d
0045DDEB  48 89 54 C5 10                  mov qword ptr [rbp + rax*8 + 0x10], rdx
0045DDF0  48 89 BC C5 10 02 00 00         mov qword ptr [rbp + rax*8 + 0x210], rdi
0045DDF8  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0045DDFC  F0 FF 04 81                     lock inc dword ptr [rcx + rax*4]
0045DE00  41 83 FE 3F                     cmp r14d, 0x3f
0045DE04  48 1B C0                        sbb rax, rax
0045DE07  49 23 C4                        and rax, r12
0045DE0A  4C 8B E0                        mov r12, rax
0045DE0D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0045DE12  45 33 C0                        xor r8d, r8d
0045DE15  33 D2                           xor edx, edx
0045DE17  48 8B CB                        mov rcx, rbx
0045DE1A  E8 11 24 DB FF                  call 0x140210230
0045DE1F  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0045DE25  48 8B F8                        mov rdi, rax
0045DE28  73 0E                           jae 0x14045de38
0045DE2A  4C 8B C3                        mov r8, rbx
0045DE2D  48 8B D0                        mov rdx, rax
0045DE30  48 8B CB                        mov rcx, rbx
0045DE33  E8 58 1E DB FF                  call 0x14020fc90
0045DE38  45 33 C9                        xor r9d, r9d
0045DE3B  48 85 FF                        test rdi, rdi
0045DE3E  0F 84 1B FF FF FF               je 0x14045dd5f
0045DE44  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0045DE48  E9 12 FF FF FF                  jmp 0x14045dd5f
0045DE4D  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0045DE52  3B CF                           cmp ecx, edi
0045DE54  0F 85 8D FE FF FF               jne 0x14045dce7
0045DE5A  44 39 44 24 40                  cmp dword ptr [rsp + 0x40], r8d
0045DE5F  0F 84 D6 02 00 00               je 0x14045e13b
0045DE65  48 8B 8D 10 04 00 00            mov rcx, qword ptr [rbp + 0x410]
0045DE6C  48 33 CC                        xor rcx, rsp
0045DE6F  E8 CC E7 24 00                  call 0x1406ac640
0045DE74  4C 8D 9C 24 20 05 00 00         lea r11, [rsp + 0x520]
0045DE7C  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
0045DE80  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0045DE84  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
0045DE88  49 8B E3                        mov rsp, r11
0045DE8B  41 5F                           pop r15
0045DE8D  41 5E                           pop r14
0045DE8F  41 5D                           pop r13
0045DE91  41 5C                           pop r12
0045DE93  5D                              pop rbp
0045DE94  C3                              ret
0045DE95  CC                              int3
0045DE96  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
0045DE9B  E9 84 FE FF FF                  jmp 0x14045dd24
0045DEA0  BA 43 63 41 73                  mov edx, 0x73416343
0045DEA5  E8 C6 49 72 00                  call 0x140b82870
0045DEAA  33 C9                           xor ecx, ecx
0045DEAC  C7 87 80 00 00 00 06 00 00 00   mov dword ptr [rdi + 0x80], 6
0045DEB6  48 8D 45 10                     lea rax, [rbp + 0x10]
0045DEBA  49 89 0C 24                     mov qword ptr [r12], rcx
0045DEBE  48 8D 04 F0                     lea rax, [rax + rsi*8]
0045DEC2  48 89 4F 30                     mov qword ptr [rdi + 0x30], rcx
0045DEC6  48 89 08                        mov qword ptr [rax], rcx
0045DEC9  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0045DECD  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0045DED1  8B 88 10 02 00 00               mov ecx, dword ptr [rax + 0x210]
0045DED7  83 F9 01                        cmp ecx, 1
0045DEDA  0F 85 05 02 00 00               jne 0x14045e0e5
0045DEE0  81 7F 28 00 00 02 00            cmp dword ptr [rdi + 0x28], 0x20000
0045DEE7  0F 87 F8 01 00 00               ja 0x14045e0e5
0045DEED  48 8B CF                        mov rcx, rdi
0045DEF0  E8 E7 08 00 00                  call 0x14045e7dc
0045DEF5  48 8B CF                        mov rcx, rdi
0045DEF8  E8 3F 93 EF FF                  call 0x14035723c
0045DEFD  45 8D 46 FF                     lea r8d, [r14 - 1]
0045DF01  45 8B F0                        mov r14d, r8d
0045DF04  45 3B F8                        cmp r15d, r8d
0045DF07  0F 82 E7 01 00 00               jb 0x14045e0f4
0045DF0D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
0045DF12  45 33 C0                        xor r8d, r8d
0045DF15  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
0045DF1A  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0045DF1F  41 8B C7                        mov eax, r15d
0045DF22  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
0045DF27  41 8D 78 02                     lea edi, [r8 + 2]
0045DF2B  4C 89 44 C5 10                  mov qword ptr [rbp + rax*8 + 0x10], r8
0045DF30  4C 89 84 C5 10 02 00 00         mov qword ptr [rbp + rax*8 + 0x210], r8
0045DF38  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
0045DF3C  F0 FF 0C 81                     lock dec dword ptr [rcx + rax*4]
0045DF40  4D 85 E4                        test r12, r12
0045DF43  0F 85 A3 FD FF FF               jne 0x14045dcec
0045DF49  49 8B 87 10 01 00 00            mov rax, qword ptr [r15 + 0x110]
0045DF50  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0045DF54  4C 8D 24 C8                     lea r12, [rax + rcx*8]
0045DF58  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0045DF5D  E9 8A FD FF FF                  jmp 0x14045dcec
0045DF62  48 8B CF                        mov rcx, rdi
0045DF65  E8 72 08 00 00                  call 0x14045e7dc
0045DF6A  48 8B CF                        mov rcx, rdi
0045DF6D  E8 CA 92 EF FF                  call 0x14035723c
0045DF72  E9 9B FE FF FF                  jmp 0x14045de12
0045DF77  0F 0D 0B                        prefetchw byte ptr [rbx]
0045DF7A  48 8B 03                        mov rax, qword ptr [rbx]
0045DF7D  48 8B C8                        mov rcx, rax
0045DF80  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0045DF84  48 83 F9 10                     cmp rcx, 0x10
0045DF88  48 8D 50 F0                     lea rdx, [rax - 0x10]
0045DF8C  49 0F 46 D1                     cmovbe rdx, r9
0045DF90  A8 02                           test al, 2
0045DF92  0F 85 EB 00 00 00               jne 0x14045e083
0045DF98  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0045DF9D  0F 85 E0 00 00 00               jne 0x14045e083
0045DFA3  48 8B CB                        mov rcx, rbx
0045DFA6  E8 55 36 E8 FF                  call 0x1402e1600
0045DFAB  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0045DFB0  4C 8D 44 24 68                  lea r8, [rsp + 0x68]
0045DFB5  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
0045DFBA  48 8B CE                        mov rcx, rsi
0045DFBD  49 8B D7                        mov rdx, r15
0045DFC0  E8 63 0B 00 00                  call 0x14045eb28
0045DFC5  45 33 C0                        xor r8d, r8d
0045DFC8  33 D2                           xor edx, edx
0045DFCA  48 8B CB                        mov rcx, rbx
0045DFCD  E8 5E 22 DB FF                  call 0x140210230
0045DFD2  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0045DFD8  48 8B F8                        mov rdi, rax
0045DFDB  73 0E                           jae 0x14045dfeb
0045DFDD  4C 8B C3                        mov r8, rbx
0045DFE0  48 8B D0                        mov rdx, rax
0045DFE3  48 8B CB                        mov rcx, rbx
0045DFE6  E8 A5 1C DB FF                  call 0x14020fc90
0045DFEB  45 33 C9                        xor r9d, r9d
0045DFEE  48 85 FF                        test rdi, rdi
0045DFF1  74 04                           je 0x14045dff7
0045DFF3  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0045DFF7  0F 0D 0B                        prefetchw byte ptr [rbx]
0045DFFA  48 8B 03                        mov rax, qword ptr [rbx]
0045DFFD  BF 02 00 00 00                  mov edi, 2
0045E002  48 8B C8                        mov rcx, rax
0045E005  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0045E009  48 83 F9 10                     cmp rcx, 0x10
0045E00D  48 8D 50 F0                     lea rdx, [rax - 0x10]
0045E011  49 0F 46 D1                     cmovbe rdx, r9
0045E015  40 84 C7                        test dil, al
0045E018  75 5F                           jne 0x14045e079
0045E01A  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0045E01F  75 58                           jne 0x14045e079
0045E021  48 8B CB                        mov rcx, rbx
0045E024  E8 D7 35 E8 FF                  call 0x1402e1600
0045E029  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0045E02E  45 33 C0                        xor r8d, r8d
0045E031  48 85 C9                        test rcx, rcx
0045E034  0F 84 B2 FC FF FF               je 0x14045dcec
0045E03A  8B 41 28                        mov eax, dword ptr [rcx + 0x28]
0045E03D  48 8B 54 24 70                  mov rdx, qword ptr [rsp + 0x70]
0045E042  44 89 04 82                     mov dword ptr [rdx + rax*4], r8d
0045E046  33 D2                           xor edx, edx
0045E048  4C 89 01                        mov qword ptr [rcx], r8
0045E04B  4C 8B 4E 08                     mov r9, qword ptr [rsi + 8]
0045E04F  45 8B 47 18                     mov r8d, dword ptr [r15 + 0x18]
0045E053  E8 D4 8D EF FF                  call 0x140356e2c
0045E058  45 33 C0                        xor r8d, r8d
0045E05B  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
0045E060  E9 87 FC FF FF                  jmp 0x14045dcec
0045E065  48 8B 74 24 58                  mov rsi, qword ptr [rsp + 0x58]
0045E06A  EB 8B                           jmp 0x14045dff7
0045E06C  48 8B CB                        mov rcx, rbx
0045E06F  E8 5C 58 E0 FF                  call 0x1402638d0
0045E074  E9 3F FD FF FF                  jmp 0x14045ddb8
0045E079  48 8B CB                        mov rcx, rbx
0045E07C  E8 4F 58 E0 FF                  call 0x1402638d0
0045E081  EB 9E                           jmp 0x14045e021
0045E083  48 8B CB                        mov rcx, rbx
0045E086  E8 45 58 E0 FF                  call 0x1402638d0
0045E08B  E9 13 FF FF FF                  jmp 0x14045dfa3
0045E090  83 F8 01                        cmp eax, 1
0045E093  44 0F 44 EF                     cmove r13d, edi
0045E097  E9 FB FB FF FF                  jmp 0x14045dc97
0045E09C  33 F6                           xor esi, esi
0045E09E  44 8B EE                        mov r13d, esi
0045E0A1  E9 F0 FD FF FF                  jmp 0x14045de96
0045E0A6  BA 43 63 41 73                  mov edx, 0x73416343
0045E0AB  E8 C0 47 72 00                  call 0x140b82870
0045E0B0  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0045E0B4  33 C9                           xor ecx, ecx
0045E0B6  C7 87 80 00 00 00 06 00 00 00   mov dword ptr [rdi + 0x80], 6
0045E0C0  48 89 4F 30                     mov qword ptr [rdi + 0x30], rcx
0045E0C4  8B 88 10 02 00 00               mov ecx, dword ptr [rax + 0x210]
0045E0CA  83 F9 01                        cmp ecx, 1
0045E0CD  0F 85 B5 3F 29 00               jne 0x1406f2088
0045E0D3  81 7F 28 00 00 02 00            cmp dword ptr [rdi + 0x28], 0x20000
0045E0DA  0F 86 82 FE FF FF               jbe 0x14045df62
0045E0E0  E9 A3 3F 29 00                  jmp 0x1406f2088
0045E0E5  33 D2                           xor edx, edx
0045E0E7  48 8B CF                        mov rcx, rdi
0045E0EA  E8 35 F5 FF FF                  call 0x14045d624
0045E0EF  E9 09 FE FF FF                  jmp 0x14045defd
0045E0F4  41 8D 47 01                     lea eax, [r15 + 1]
0045E0F8  45 2B C7                        sub r8d, r15d
0045E0FB  48 8D B5 10 02 00 00            lea rsi, [rbp + 0x210]
0045E102  49 8B FC                        mov rdi, r12
0045E105  48 8D 34 C6                     lea rsi, [rsi + rax*8]
0045E109  45 8B FE                        mov r15d, r14d
0045E10C  48 8D 55 10                     lea rdx, [rbp + 0x10]
0045E110  48 8D 14 C2                     lea rdx, [rdx + rax*8]
0045E114  41 8B C0                        mov eax, r8d
0045E117  48 C1 E0 03                     shl rax, 3
0045E11B  48 8B C8                        mov rcx, rax
0045E11E  48 C1 E9 03                     shr rcx, 3
0045E122  F3 48 A5                        rep movsq qword ptr [rdi], qword ptr [rsi]
0045E125  48 8B 7D 80                     mov rdi, qword ptr [rbp - 0x80]
0045E129  48 8B F2                        mov rsi, rdx
0045E12C  48 C1 E8 03                     shr rax, 3
0045E130  48 8B C8                        mov rcx, rax
0045E133  F3 48 A5                        rep movsq qword ptr [rdi], qword ptr [rsi]
0045E136  E9 D2 FD FF FF                  jmp 0x14045df0d
0045E13B  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
0045E13F  BA 43 63 57 71                  mov edx, 0x71576343
0045E144  E8 27 47 72 00                  call 0x140b82870
0045E149  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
0045E14D  48 8B CE                        mov rcx, rsi
0045E150  E8 F7 D7 F2 FF                  call 0x14038b94c
0045E155  E9 0B FD FF FF                  jmp 0x14045de65
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcAsyncReadWorker(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m4B0;
    unsigned __int64 v_stack_m4B8;
    unsigned int v_stack_m4C0;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m4E0;
    unsigned int v_stack_m4E8;
    unsigned __int64 v_stack_m4F0;
    unsigned __int64 v_stack_m4F8;
    unsigned __int64 v_stack_m500;
    unsigned int v_stack_m508;
    unsigned __int64 v_stack_m510;
    unsigned __int64 v_stack_m518;
    unsigned __int8 v_stack_m520;
    unsigned __int8 v_stack_m528;

    if (a1 == 0) goto loc_0045DE94;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (0x520ULL);
    result = (*(unsigned __int64 *)(v_rip + 10144762)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 1096 + 1040) = result;
    result = 0;
    v_stack_m4E0 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 - 96) = a1;
    a2 = 0;
    v_stack_m508 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    *(unsigned __int64 *)(v_rsp - 1096 - 120) = v_xmm0;
    v_stack_m4E8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)));
    v_stack_m4F0 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m500 = *(unsigned __int64 *)(a1 + 72);
    *(unsigned __int64 *)(v_rsp - 1096 - 88) = *(unsigned __int64 *)(a1 + 64);
    result = memset(v_rsp - 1096 + 16, a2, 512, a4);
    a2 = 0;
    result = memset(v_rsp - 1096 + 528, a2, 512, a4);
    *(unsigned __int64 *)(v_rsp - 1096 - 104) = (unsigned int)(*(unsigned int *)(a1 + 36)) + (unsigned int)(*(unsigned int *)(a1 + 36)) * 2;
    a3 = 0;
    v_stack_m4D0 = (unsigned int)(*(unsigned int *)(a1 + 36));
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 36)) + (unsigned int)(*(unsigned int *)(a1 + 36)) * 2) * ((unsigned int)(*(unsigned int *)(a1 + 36)));
    v_stack_m4F8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 272) + (unsigned int)(*(unsigned int *)(a1 + 36)) + (unsigned int)(*(unsigned int *)(a1 + 36)) * 2 * 8;
    a1 = (a1) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 280));
    v_stack_m4D8 = a1;
    v_rbx = *(unsigned __int64 *)(a1 + 64) + 1160;
    if ((*(unsigned __int8 *)(v_rip + 10518420)) == 0) {
        v_rbx = *(unsigned __int64 *)(a1 + 56) + 1224;
    }
    *(unsigned __int64 *)(v_rsp - 1096 - 120) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 272) + (unsigned int)(*(unsigned int *)(a1 + 36)) + (unsigned int)(*(unsigned int *)(a1 + 36)) * 2 * 8;
    result = *(unsigned __int64 *)(a1 + 56) + 1304;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 4)) != 1) {
        result = *(unsigned __int64 *)(a1 + 64) + 1176;
    }
    *(unsigned __int64 *)(v_rsp - 1096 - 112) = result;
loc_0045DC24:
    if (0 < 63) goto loc_0045DD0A;
loc_0045DC2E:
    if (0 == 0) goto loc_0045DC59;
    result = MmWaitMultipleForCacheManagerPrefetch(v_rsp - 1096 + 16, 0, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 272) + (unsigned int)(*(unsigned int *)(a1 + 36)) + (unsigned int)(*(unsigned int *)(a1 + 36)) * 2 * 8, a4);
    if (((unsigned int)(result)) >= 0) goto loc_0045E09C;
    a3 = 0;
    goto loc_0045DCB1;
loc_0045DC59:
    v_stack_m510 = v_rsp - 1096 - 80;
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    v_stack_m528 = 0;
    result = KeWaitForMultipleObjects(2, v_rsp - 1096 - 120, 8 - 7, 8);
    a3 = 0;
    if ((unsigned int)(result) != 0) goto loc_0045E090;
loc_0045DC97:
    if (0 == 0) goto loc_0045DE96;
    if (0 != 1) goto loc_0045DE4D;
    if (((unsigned int)(result)) >= 0) goto loc_0045DCE7;
loc_0045DCB1:
    if (*(unsigned __int64 *)(v_rsp - 1096 + 528 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8) == 0) goto loc_0045DCD8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsp - 1096 + 528 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))) * 8) + 48) != 0) goto loc_0045DEA0;
loc_0045DCD8:
loc_0045DCE7:
loc_0045DCEC:
    if (v_stack_m508 == 0) goto loc_0045DC24;
    if (0 == 0) goto loc_0045DE65;
    goto loc_0045DC24;
loc_0045DD0A:
    a1 = (v_stack_m4D0) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_m500 + 256));
    if ((*(unsigned __int64 *)(a1)) == a1) goto loc_0045DC2E;
loc_0045DD24:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, 8);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbx;
        a2 = result;
        a1 = v_rbx;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 8);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsi = (v_stack_m4D0) << (4);
    a4 = 0;
loc_0045DD5F:
    a3 = (*(unsigned __int64 *)(v_stack_m500 + 256)) + (v_rsi);
    if ((*(unsigned __int64 *)(a3)) == a3) goto loc_0045E065;
    if (0 >= 63) goto loc_0045DF77;
    result = CcFindNextWorkQueueEntry(a1, v_stack_m500, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rbx)) & (-16);
    a2 = *(unsigned __int64 *)(v_rbx) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0045E06C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0045E06C;
loc_0045DDB8:
    result = KeAbPostRelease(v_rbx, a2, a3, a4);
    result = CcAsyncReadPrefetch(result, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0045DF62;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 48)) == 0) goto loc_0045E0A6;
    v_r14 = (unsigned int)((0) + 1);
    *(unsigned __int64 *)(v_rsp - 1096 + 0 * 8 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 48));
    *(unsigned __int64 *)(v_rsp - 1096 + 0 * 8 + 528) = result;
    result = ((unsigned int)(v_stack_m508)) & (v_stack_m4F8);
    v_stack_m4F8 = result;
loc_0045DE12:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbx;
        a2 = result;
        a1 = v_rbx;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    a4 = 0;
    if (result == 0) goto loc_0045DD5F;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_0045DD5F;
loc_0045DE4D:
    v_stack_m4F8 = result;
    if (((unsigned int)(a1)) != ((unsigned int)(result))) goto loc_0045DCE7;
    if (v_stack_m508 == ((unsigned int)(a3))) goto loc_0045E13B;
loc_0045DE65:
    a1 = (*(unsigned __int64 *)(v_rsp - 1096 + 1040)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
loc_0045DE94:
    return result;
loc_0045DE96:
    goto loc_0045DD24;
loc_0045DEA0:
    result = ExFreePoolWithTag(a1, (unsigned int)(0x73416343ULL), a3, a4);
    a1 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 128) = 6;
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 48) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + 16 + *(unsigned __int64 *)(v_stack_m28 + 64) * 8) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 - 128) = v_rsp - 1096 + 16 + *(unsigned __int64 *)(v_stack_m28 + 64) * 8;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 16) + 528)))) != 1) goto loc_0045E0E5;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 40)) > 0x20000ULL) goto loc_0045E0E5;
    result = CcCompleteAsyncRead(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(0x73416343ULL), a3, a4);
    result = CcFreeWorkQueueEntry(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(0x73416343ULL), a3, a4);
loc_0045DEFD:
    if (((unsigned int)(v_stack_m4D8)) < ((unsigned int)(v_r14 - 1))) goto loc_0045E0F4;
loc_0045DF0D:
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + (unsigned int)((unsigned int)(v_stack_m4D8)) * 8 + 16) = 0;
    *(unsigned __int64 *)(v_rsp - 1096 + (unsigned int)((unsigned int)(v_stack_m4D8)) * 8 + 528) = 0;
    if (v_stack_m4D0 != 0) goto loc_0045DCEC;
    v_stack_m4D0 = *(unsigned __int64 *)(v_stack_m4D8 + 272) + *(unsigned __int64 *)(v_rsp - 1096 - 104) * 8;
    goto loc_0045DCEC;
loc_0045DF62:
    result = CcCompleteAsyncRead(a3 + 2, (unsigned int)(0x73416343ULL), a3, a4);
    result = CcFreeWorkQueueEntry(a3 + 2, (unsigned int)(0x73416343ULL), a3, a4);
    goto loc_0045DE12;
loc_0045DF77:
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56))) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)))) & (2)) != 0) goto loc_0045E083;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)))) & (2)) != 0) goto loc_0045E083;
loc_0045DFA3:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, a4);
    result = CcShouldSpinAsyncReadWorkerThread(v_stack_m4C8, v_stack_m4D8, v_stack_m4B8, (unsigned int)(v_stack_m4C0));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, (unsigned int)(v_stack_m4C0));
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(v_stack_m28 + 56);
        a2 = result;
        a1 = *(unsigned __int64 *)(v_stack_m28 + 56);
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)(v_stack_m4C0));
    }
    a4 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56))) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56)) - 16;
    if (a1 <= 16) { a2 = 0; }
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56))))) != 0) goto loc_0045E079;
    if (((2) & ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 56))))) != 0) goto loc_0045E079;
loc_0045E021:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, a4);
    a3 = 0;
    if (v_stack_m4B8 == 0) goto loc_0045DCEC;
    *(unsigned int *)(v_stack_m4B0 + (unsigned int)(*(unsigned int *)(v_stack_m4B8 + 40)) * 4) = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_stack_m4B8) = 0;
    result = ExQueueWorkItemToPartition(v_stack_m4B8, a2, (unsigned int)(*(unsigned int *)(v_stack_m4D8 + 24)), *(unsigned __int64 *)(v_stack_m4C8 + 8));
    a3 = 0;
    v_stack_m4B8 = 0;
    goto loc_0045DCEC;
loc_0045E065:
    goto loc_0045DFF7;
loc_0045E06C:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, *(unsigned __int64 *)(v_stack_m4C8 + 8));
    goto loc_0045DDB8;
loc_0045E079:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, *(unsigned __int64 *)(v_stack_m4C8 + 8));
    goto loc_0045E021;
loc_0045E083:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_stack_m28 + 56), a2, a3, *(unsigned __int64 *)(v_stack_m4C8 + 8));
    goto loc_0045DFA3;
loc_0045E090:
    v_r13 = 0;
    if (((unsigned int)(result)) == 1) { v_r13 = 2; }
    goto loc_0045DC97;
loc_0045E09C:
    v_rsi = 0;
    goto loc_0045DE96;
loc_0045E0A6:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m28 + 56), (unsigned int)(0x73416343ULL), a3, *(unsigned __int64 *)(v_stack_m4C8 + 8));
    a1 = 0;
    *(unsigned int *)(2 + 128) = 6;
    *(unsigned __int64 *)(2 + 48) = 0;
    if ((*(unsigned int *)(2 + 40)) <= 0x20000ULL) goto loc_0045DF62;
loc_0045E0E5:
    a2 = 0;
    result = CcPostWorkQueueAsyncRead(2, a2, a3, *(unsigned __int64 *)(v_stack_m4C8 + 8));
    goto loc_0045DEFD;
loc_0045E0F4:
    a3 = (unsigned int)((a3) - ((unsigned int)(v_stack_m4D8)));
    result = ((unsigned int)((unsigned int)(a3))) << (3);
    a1 = (result) >> (3);
    result = (result) >> (3);
    goto loc_0045DF0D;
loc_0045E13B:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 1096 - 96), (unsigned int)(0x71576343ULL), a3, *(unsigned __int64 *)(v_stack_m4C8 + 8));
    result = CcDereferencePartitionAndPrivateVolumeCacheMap(v_rsp - 1096 + 16 + v_stack_m4D8 + 1 * 8, *(unsigned __int64 *)(v_rsp - 1096 - 88), a3, *(unsigned __int64 *)(v_stack_m4C8 + 8));
    goto loc_0045DE65;
}
```

## 5. (Beta) C Style

```c
int64_t CcAsyncReadWorker(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m4B0;
    uint64_t v_stack_m4B8;
    uint32_t v_stack_m4C0;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m4E0;
    uint32_t v_stack_m4E8;
    uint64_t v_stack_m4F0;
    uint64_t v_stack_m4F8;
    uint64_t v_stack_m500;
    uint32_t v_stack_m508;
    uint64_t v_stack_m510;
    uint64_t v_stack_m518;
    uint8_t v_stack_m520;
    uint8_t v_stack_m528;

    if (Arg1 == 0) goto loc_0045DE94;
    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (0x520ULL);
    result = (*(uint64_t *)(v_rip + 0x9ACBFA)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x448 + 0x410) = result;
    result = 0;
    v_stack_m4E0 = 0;
    *(uint64_t *)(local_rsp - 0x448 - 0x60) = Arg1;
    Arg2 = 0;
    v_stack_m508 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x28)));
    *(uint64_t *)(local_rsp - 0x448 - 0x78) = v_xmm0;
    v_stack_m4E8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x24)));
    v_stack_m4F0 = *(uint64_t *)(Arg1 + 0x38);
    v_stack_m500 = *(uint64_t *)(Arg1 + 0x48);
    *(uint64_t *)(local_rsp - 0x448 - 0x58) = *(uint64_t *)(Arg1 + 0x40);
    result = memset(local_rsp - 1096 + 16, Arg2, 512, a4);
    Arg2 = 0;
    result = memset(local_rsp - 1096 + 528, Arg2, 512, a4);
    *(uint64_t *)(local_rsp - 0x448 - 0x68) = (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) * 2;
    a3 = 0;
    v_stack_m4D0 = (uint32_t)(*(uint32_t *)(Arg1 + 0x24));
    Arg1 = ((uint32_t)(*(uint32_t *)(Arg1 + 0x24)) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) * 2) * ((uint32_t)(*(uint32_t *)(Arg1 + 0x24)));
    v_stack_m4F8 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x48) + 0x110) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) * 2 * 8;
    Arg1 = (Arg1) + (*(uint64_t *)(*(uint64_t *)(Arg1 + 0x48) + 0x118));
    v_stack_m4D8 = Arg1;
    local_rbx = *(uint64_t *)(Arg1 + 0x40) + 1160;
    if ((*(uint8_t *)(v_rip + 0xA07F94)) == 0) {
        local_rbx = *(uint64_t *)(Arg1 + 0x38) + 1224;
    }
    *(uint64_t *)(local_rsp - 0x448 - 0x78) = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x48) + 0x110) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) * 2 * 8;
    result = *(uint64_t *)(Arg1 + 0x38) + 1304;
    if ((*(uint32_t *)(*(uint64_t *)(Arg1 + 0x48) + 0x4)) != 1) {
        result = *(uint64_t *)(Arg1 + 0x40) + 1176;
    }
    *(uint64_t *)(local_rsp - 0x448 - 0x70) = result;
loc_0045DC24:
    if (0 < 63) goto loc_0045DD0A;
loc_0045DC2E:
    if (0 == 0) goto loc_0045DC59;
    result = MmWaitMultipleForCacheManagerPrefetch(local_rsp - 1096 + 16, 0, *(uint64_t *)(*(uint64_t *)(Arg1 + 0x48) + 0x110) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) + (uint32_t)(*(uint32_t *)(Arg1 + 0x24)) * 2 * 8, a4);
    if (((uint32_t)(result)) >= 0) goto loc_0045E09C;
    a3 = 0;
    goto loc_0045DCB1;
loc_0045DC59:
    v_stack_m510 = local_rsp - 1096 - 80;
    v_stack_m518 = 0;
    v_stack_m520 = 0;
    v_stack_m528 = 0;
    result = KeWaitForMultipleObjects(2, local_rsp - 1096 - 120, 8 - 7, 8);
    a3 = 0;
    if ((uint32_t)(result) != 0) goto loc_0045E090;
loc_0045DC97:
    if (0 == 0) goto loc_0045DE96;
    if (0 != 1) goto loc_0045DE4D;
    if (((uint32_t)(result)) >= 0) goto loc_0045DCE7;
loc_0045DCB1:
    if (*(uint64_t *)(local_rsp - 0x448 + 0x210 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8) == 0) goto loc_0045DCD8;
    if (*(uint64_t *)(*(uint64_t *)(local_rsp - 0x448 + 0x210 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))) * 8) + 0x30) != 0) goto loc_0045DEA0;
loc_0045DCD8:
loc_0045DCE7:
loc_0045DCEC:
    if (v_stack_m508 == 0) goto loc_0045DC24;
    if (0 == 0) goto loc_0045DE65;
    goto loc_0045DC24;
loc_0045DD0A:
    Arg1 = (v_stack_m4D0) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_m500 + 0x100));
    if ((*(uint64_t *)(Arg1)) == Arg1) goto loc_0045DC2E;
loc_0045DD24:
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, a3, 8);
    if (!(condition_is_above_or_equal)) {
        a3 = local_rbx;
        Arg2 = result;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, 8);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsi = (v_stack_m4D0) << (4);
    a4 = 0;
loc_0045DD5F:
    a3 = (*(uint64_t *)(v_stack_m500 + 0x100)) + (local_rsi);
    if ((*(uint64_t *)(a3)) == a3) goto loc_0045E065;
    if (0 >= 63) goto loc_0045DF77;
    result = CcFindNextWorkQueueEntry(Arg1, v_stack_m500, a3, a4);
    Arg1 = (*(uint64_t *)(local_rbx)) & (-16);
    Arg2 = *(uint64_t *)(local_rbx) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0045E06C;
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0045E06C;
loc_0045DDB8:
    result = KeAbPostRelease(local_rbx, Arg2, a3, a4);
    result = CcAsyncReadPrefetch(result, Arg2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0045DF62;
    if (*(uint64_t *)(*(uint64_t *)(result + 0x30)) == 0) goto loc_0045E0A6;
    local_r14 = (uint32_t)((0) + 1);
    *(uint64_t *)(local_rsp - 0x448 + 0x0 * 8 + 0x10) = *(uint64_t *)(*(uint64_t *)(result + 0x30));
    *(uint64_t *)(local_rsp - 0x448 + 0x0 * 8 + 0x210) = result;
    result = ((uint32_t)(v_stack_m508)) & (v_stack_m4F8);
    v_stack_m4F8 = result;
loc_0045DE12:
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = local_rbx;
        Arg2 = result;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, a4);
    }
    a4 = 0;
    if (result == 0) goto loc_0045DD5F;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_0045DD5F;
loc_0045DE4D:
    v_stack_m4F8 = result;
    if (((uint32_t)(Arg1)) != ((uint32_t)(result))) goto loc_0045DCE7;
    if (v_stack_m508 == ((uint32_t)(a3))) goto loc_0045E13B;
loc_0045DE65:
    Arg1 = (*(uint64_t *)(local_rsp - 0x448 + 0x410)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, a3, a4);
loc_0045DE94:
    return result;
loc_0045DE96:
    goto loc_0045DD24;
loc_0045DEA0:
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x73416343ULL), a3, a4);
    Arg1 = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x80) = 6;
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x448 + 0x10 + *(uint64_t *)(v_stack_m28 + 0x40) * 8) = 0;
    *(uint64_t *)(local_rsp - 0x448 - 0x80) = local_rsp - 1096 + 16 + *(uint64_t *)(v_stack_m28 + 0x40) * 8;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x10) + 0x210)))) != 1) goto loc_0045E0E5;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x28)) > 0x20000ULL) goto loc_0045E0E5;
    result = CcCompleteAsyncRead(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(0x73416343ULL), a3, a4);
    result = CcFreeWorkQueueEntry(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(0x73416343ULL), a3, a4);
loc_0045DEFD:
    if (((uint32_t)(v_stack_m4D8)) < ((uint32_t)(local_r14 - 1))) goto loc_0045E0F4;
loc_0045DF0D:
    a3 = 0;
    *(uint64_t *)(local_rsp - 0x448 + (uint32_t)((uint32_t)(v_stack_m4D8)) * 8 + 0x10) = 0;
    *(uint64_t *)(local_rsp - 0x448 + (uint32_t)((uint32_t)(v_stack_m4D8)) * 8 + 0x210) = 0;
    if (v_stack_m4D0 != 0) goto loc_0045DCEC;
    v_stack_m4D0 = *(uint64_t *)(v_stack_m4D8 + 0x110) + *(uint64_t *)(local_rsp - 0x448 - 0x68) * 8;
    goto loc_0045DCEC;
loc_0045DF62:
    result = CcCompleteAsyncRead(a3 + 2, (uint32_t)(0x73416343ULL), a3, a4);
    result = CcFreeWorkQueueEntry(a3 + 2, (uint32_t)(0x73416343ULL), a3, a4);
    goto loc_0045DE12;
loc_0045DF77:
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)))) & (2)) != 0) goto loc_0045E083;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)))) & (2)) != 0) goto loc_0045E083;
loc_0045DFA3:
    result = KeAbPostRelease(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, a3, a4);
    result = CcShouldSpinAsyncReadWorkerThread(v_stack_m4C8, v_stack_m4D8, v_stack_m4B8, (uint32_t)(v_stack_m4C0));
    a3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, a3, (uint32_t)(v_stack_m4C0));
    if (!(condition_is_above_or_equal)) {
        a3 = *(uint64_t *)(v_stack_m28 + 0x38);
        Arg2 = result;
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x38);
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, a3, (uint32_t)(v_stack_m4C0));
    }
    a4 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38))) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38)) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if (((2) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38))))) != 0) goto loc_0045E079;
    if (((2) & ((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m28 + 0x38))))) != 0) goto loc_0045E079;
loc_0045E021:
    result = KeAbPostRelease(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, a3, a4);
    a3 = 0;
    if (v_stack_m4B8 == 0) goto loc_0045DCEC;
    *(uint32_t *)(v_stack_m4B0 + (uint32_t)(*(uint32_t *)(v_stack_m4B8 + 0x28)) * 4) = 0;
    Arg2 = 0;
    *(uint64_t *)(v_stack_m4B8) = 0;
    result = ExQueueWorkItemToPartition(v_stack_m4B8, Arg2, (uint32_t)(*(uint32_t *)(v_stack_m4D8 + 0x18)), *(uint64_t *)(v_stack_m4C8 + 0x8));
    a3 = 0;
    v_stack_m4B8 = 0;
    goto loc_0045DCEC;
loc_0045E065:
    goto loc_0045DFF7;
loc_0045E06C:
    result = ExfReleasePushLock(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, a3, *(uint64_t *)(v_stack_m4C8 + 0x8));
    goto loc_0045DDB8;
loc_0045E079:
    result = ExfReleasePushLock(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, a3, *(uint64_t *)(v_stack_m4C8 + 0x8));
    goto loc_0045E021;
loc_0045E083:
    result = ExfReleasePushLock(*(uint64_t *)(v_stack_m28 + 0x38), Arg2, a3, *(uint64_t *)(v_stack_m4C8 + 0x8));
    goto loc_0045DFA3;
loc_0045E090:
    local_r13 = 0;
    if (((uint32_t)(result)) == 1) { local_r13 = 2; }
    goto loc_0045DC97;
loc_0045E09C:
    local_rsi = 0;
    goto loc_0045DE96;
loc_0045E0A6:
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m28 + 0x38), (uint32_t)(0x73416343ULL), a3, *(uint64_t *)(v_stack_m4C8 + 0x8));
    Arg1 = 0;
    *(uint32_t *)(2 + 0x80) = 6;
    *(uint64_t *)(2 + 0x30) = 0;
    if ((*(uint32_t *)(2 + 0x28)) <= 0x20000ULL) goto loc_0045DF62;
loc_0045E0E5:
    Arg2 = 0;
    result = CcPostWorkQueueAsyncRead(2, Arg2, a3, *(uint64_t *)(v_stack_m4C8 + 0x8));
    goto loc_0045DEFD;
loc_0045E0F4:
    a3 = (uint32_t)((a3) - ((uint32_t)(v_stack_m4D8)));
    result = ((uint32_t)((uint32_t)(a3))) << (3);
    Arg1 = (result) >> (3);
    result = (result) >> (3);
    goto loc_0045DF0D;
loc_0045E13B:
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x448 - 0x60), (uint32_t)(0x71576343ULL), a3, *(uint64_t *)(v_stack_m4C8 + 0x8));
    result = CcDereferencePartitionAndPrivateVolumeCacheMap(local_rsp - 1096 + 16 + v_stack_m4D8 + 1 * 8, *(uint64_t *)(local_rsp - 0x448 - 0x58), a3, *(uint64_t *)(v_stack_m4C8 + 0x8));
    goto loc_0045DE65;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0045DB10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
