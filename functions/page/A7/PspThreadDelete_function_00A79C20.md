# PspThreadDelete

- RVA: `0x00A79C20`–`0x00A7A149` (길이 `1,321` bytes)
- VA: `0x0000000140A79C20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B62E4`
- 디코드: `310`개 명령, `1,321/1,321` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **21**

### Outgoing calls
- `0x00A79C37` → [KeCleanupThreadState](../../text/44/KeCleanupThreadState_function_0044B518.md) (function, `0x0044B518`)
- `0x00A79D5C` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (function, `0x00460164`)
- `0x00A79D70` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00A79D89` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00A79D9B` → [KeFoldProcessStatisticsThread](../../text/41/KeFoldProcessStatisticsThread_function_004171AC.md) (function, `0x004171AC`)
- `0x00A79DCF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00A79DED` → [ExMapHandleToPointer](../86/ExMapHandleToPointer_function_00868B60.md) (function, `0x00868B60`)
- `0x00A79E08` → [ExDestroyHandle](../88/ExDestroyHandle_function_00889430.md) (function, `0x00889430`)
- `0x00A79E10` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00A79E1F` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (function, `0x004FD640`)
- `0x00A79FAB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00A79FB6` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00A79FF5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A79FFF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x00A7A01B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00A7A034` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00A7A050` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00A7A06C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00A7A07F` → [KeEnumerateKernelStackSegments](../../text/2A/KeEnumerateKernelStackSegments_function_002A13B8.md) (function, `0x002A13B8`)
- `0x00A7A094` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A7A0A9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A7A0BF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A7A12A` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (function, `0x0045BBD0`)
- `0x00A7A13F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A79CFE` → RVA `0x00E62590` (`.data`; read)
- `0x00A79DE6` → RVA `0x00FC6CA8` (`ALMOSTRO`; read)
- `0x00A79E25` → RVA `0x00E62580` (`.data`; read)
- `0x00A79E35` → RVA `0x00E62598` (`.data`; read)
- `0x00A79E47` → RVA `0x00F0F680` (`.data`; read)
- `0x00A79E51` → RVA `0x00E625A0` (`.data`; read)
- `0x00A79E88` → RVA `0x00E625C0` (`.data`; read)
- `0x00A79EB3` → RVA `0x00E62588` (`.data`; read)
- `0x00A79EEE` → RVA `0x00E625C8` (`.data`; read)
- `0x00A79EF7` → RVA `0x00E62550` (`.data`; read)
- `0x00A79F18` → RVA `0x00E62568` (`.data`; write)
- `0x00A79F22` → RVA `0x00E62550` (`.data`; write)
- `0x00A79F29` → RVA `0x00E62558` (`.data`; read)
- `0x00A79F30` → RVA `0x00E62570` (`.data`; write)
- `0x00A79F88` → RVA `0x00E62590` (`.data`; write)
- `0x00A79FCB` → RVA `0x00FC6B70` (`ALMOSTRO`; read)
- `0x00A7A075` → RVA `0x002A1550` (`PspDeleteKernelStack`; read)
- `0x00A7A109` → RVA `0x0069BE90` (`KiScanQueues`; read)
- `0x00A7A110` → RVA `0x00E62528` (`.data`; read)
- `0x00A7A117` → RVA `0x00E62510` (`.data`; read)
- `0x00A7A135` → RVA `0x00F06530` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **22**
  - `0x00A79C37` → [KeCleanupThreadState](../../text/44/KeCleanupThreadState_function_0044B518.md) (`PAGE` → `.text`)
  - `0x00A79D5C` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (`PAGE` → `.text`)
  - `0x00A79D70` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00A79D89` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00A79D9B` → [KeFoldProcessStatisticsThread](../../text/41/KeFoldProcessStatisticsThread_function_004171AC.md) (`PAGE` → `.text`)
  - `0x00A79DCF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00A79E10` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00A79E1F` → [KeBugCheck](../../text/4F/KeBugCheck_function_004FD640.md) (`PAGE` → `.text`)
  - `0x00A79FAB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00A79FB6` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00A79FF5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A79FFF` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x00A7A01B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00A7A034` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00A7A050` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00A7A06C` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00A7A07F` → [KeEnumerateKernelStackSegments](../../text/2A/KeEnumerateKernelStackSegments_function_002A13B8.md) (`PAGE` → `.text`)
  - `0x00A7A094` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A7A0A9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A7A0BF` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A7A12A` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (`PAGE` → `.text`)
  - `0x00A7A13F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00A7A0A3` → [sub_00B41FE2](../B4/Unknown_function_00B41FE2.md) (`tail-transfer`)
  - `0x00A7A0B5` → [sub_00B41FE2](../B4/Unknown_function_00B41FE2.md) (`tail-transfer`)
  - `0x00A7A11E` → [sub_00B41FE2 + 0xD](../B4/Unknown_function_00B41FE2.md) (`tail-transfer`)
  - `0x00A7A130` → [sub_00B41FE2 + 0xD](../B4/Unknown_function_00B41FE2.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A79C20  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A79C25  55                              push rbp
00A79C26  56                              push rsi
00A79C27  57                              push rdi
00A79C28  41 54                           push r12
00A79C2A  41 55                           push r13
00A79C2C  41 56                           push r14
00A79C2E  41 57                           push r15
00A79C30  48 83 EC 30                     sub rsp, 0x30
00A79C34  48 8B F9                        mov rdi, rcx
00A79C37  E8 DC 18 9D FF                  call 0x14044b518
00A79C3C  8B 87 EC 05 00 00               mov eax, dword ptr [rdi + 0x5ec]
00A79C42  45 33 ED                        xor r13d, r13d
00A79C45  85 C0                           test eax, eax
00A79C47  0F 85 B9 03 00 00               jne 0x140a7a006
00A79C4D  8B 87 E0 05 00 00               mov eax, dword ptr [rdi + 0x5e0]
00A79C53  85 C0                           test eax, eax
00A79C55  0F 85 C6 03 00 00               jne 0x140a7a021
00A79C5B  8B 87 E4 05 00 00               mov eax, dword ptr [rdi + 0x5e4]
00A79C61  85 C0                           test eax, eax
00A79C63  0F 85 D1 03 00 00               jne 0x140a7a03a
00A79C69  8B 87 E8 05 00 00               mov eax, dword ptr [rdi + 0x5e8]
00A79C6F  85 C0                           test eax, eax
00A79C71  0F 85 DF 03 00 00               jne 0x140a7a056
00A79C77  48 8D 87 D0 06 00 00            lea rax, [rdi + 0x6d0]
00A79C7E  4C 8B 08                        mov r9, qword ptr [rax]
00A79C81  4C 3B C8                        cmp r9, rax
00A79C84  0F 85 33 01 00 00               jne 0x140a79dbd
00A79C8A  4C 39 6F 28                     cmp qword ptr [rdi + 0x28], r13
00A79C8E  0F 85 DE 03 00 00               jne 0x140a7a072
00A79C94  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
00A79C9D  48 83 CB FF                     or rbx, 0xffffffffffffffff
00A79CA1  4C 39 AF 10 05 00 00            cmp qword ptr [rdi + 0x510], r13
00A79CA8  0F 85 27 01 00 00               jne 0x140a79dd5
00A79CAE  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
00A79CB4  BE 08 00 00 00                  mov esi, 8
00A79CB9  40 84 C6                        test sil, al
00A79CBC  0F 85 C7 03 00 00               jne 0x140a7a089
00A79CC2  48 8B 8F A0 06 00 00            mov rcx, qword ptr [rdi + 0x6a0]
00A79CC9  4C 89 AF 38 05 00 00            mov qword ptr [rdi + 0x538], r13
00A79CD0  48 85 C9                        test rcx, rcx
00A79CD3  0F 85 E1 03 00 00               jne 0x140a7a0ba
00A79CD9  49 BE B0 03 00 00 80 F7 FF FF   movabs r14, 0xfffff780000003b0
00A79CE3  49 BF 08 00 00 00 80 F7 FF FF   movabs r15, 0xfffff78000000008
00A79CED  49 8B 16                        mov rdx, qword ptr [r14]
00A79CF0  49 8B 0F                        mov rcx, qword ptr [r15]
00A79CF3  49 8B 06                        mov rax, qword ptr [r14]
00A79CF6  48 3B D0                        cmp rdx, rax
00A79CF9  75 F2                           jne 0x140a79ced
00A79CFB  48 2B CA                        sub rcx, rdx
00A79CFE  48 3B 0D 8B 88 3E 00            cmp rcx, qword ptr [rip + 0x3e888b]
00A79D05  0F 83 1A 01 00 00               jae 0x140a79e25
00A79D0B  4C 39 AF 90 07 00 00            cmp qword ptr [rdi + 0x790], r13
00A79D12  74 22                           je 0x140a79d36
00A79D14  49 8B C5                        mov rax, r13
00A79D17  48 87 87 90 07 00 00            xchg qword ptr [rdi + 0x790], rax
00A79D1E  48 8B D0                        mov rdx, rax
00A79D21  48 83 E2 F0                     and rdx, 0xfffffffffffffff0
00A79D25  74 0F                           je 0x140a79d36
00A79D27  83 E0 0F                        and eax, 0xf
00A79D2A  76 0A                           jbe 0x140a79d36
00A79D2C  F7 D8                           neg eax
00A79D2E  48 63 C8                        movsxd rcx, eax
00A79D31  F0 48 01 4A D0                  lock add qword ptr [rdx - 0x30], rcx
00A79D36  48 8B AF 20 02 00 00            mov rbp, qword ptr [rdi + 0x220]
00A79D3D  48 85 ED                        test rbp, rbp
00A79D40  0F 84 8E 02 00 00               je 0x140a79fd4
00A79D46  4C 8D B7 78 05 00 00            lea r14, [rdi + 0x578]
00A79D4D  4D 39 2E                        cmp qword ptr [r14], r13
00A79D50  0F 84 65 02 00 00               je 0x140a79fbb
00A79D56  49 8B D4                        mov rdx, r12
00A79D59  48 8B CD                        mov rcx, rbp
00A79D5C  E8 03 64 9E FF                  call 0x140460164
00A79D61  48 8D B5 E0 05 00 00            lea rsi, [rbp + 0x5e0]
00A79D68  45 33 C0                        xor r8d, r8d
00A79D6B  48 8B CE                        mov rcx, rsi
00A79D6E  33 D2                           xor edx, edx
00A79D70  E8 BB 64 79 FF                  call 0x140210230
00A79D75  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
00A79D7B  4C 8B F8                        mov r15, rax
00A79D7E  73 0E                           jae 0x140a79d8e
00A79D80  4C 8B C6                        mov r8, rsi
00A79D83  48 8B D0                        mov rdx, rax
00A79D86  48 8B CE                        mov rcx, rsi
00A79D89  E8 02 5F 79 FF                  call 0x14020fc90
00A79D8E  4D 85 FF                        test r15, r15
00A79D91  74 05                           je 0x140a79d98
00A79D93  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00A79D98  48 8B CF                        mov rcx, rdi
00A79D9B  E8 0C D4 99 FF                  call 0x1404171ac
00A79DA0  49 8B 0E                        mov rcx, qword ptr [r14]
00A79DA3  4C 39 71 08                     cmp qword ptr [rcx + 8], r14
00A79DA7  75 0D                           jne 0x140a79db6
00A79DA9  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
00A79DAD  4C 39 30                        cmp qword ptr [rax], r14
00A79DB0  0F 84 DE 01 00 00               je 0x140a79f94
00A79DB6  B9 03 00 00 00                  mov ecx, 3
00A79DBB  CD 29                           int 0x29
00A79DBD  4C 8B C7                        mov r8, rdi
00A79DC0  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A79DC5  BA 15 00 00 00                  mov edx, 0x15
00A79DCA  B9 C6 01 00 00                  mov ecx, 0x1c6
00A79DCF  E8 8C 38 A8 FF                  call 0x1404fd660
00A79DD4  CC                              int3
00A79DD5  66 41 01 9C 24 E4 01 00 00      add word ptr [r12 + 0x1e4], bx
00A79DDE  90                              nop
00A79DDF  48 8B 97 10 05 00 00            mov rdx, qword ptr [rdi + 0x510]
00A79DE6  48 8B 0D BB CE 54 00            mov rcx, qword ptr [rip + 0x54cebb]
00A79DED  E8 6E ED DE FF                  call 0x140868b60
00A79DF2  48 85 C0                        test rax, rax
00A79DF5  74 23                           je 0x140a79e1a
00A79DF7  48 8B 97 10 05 00 00            mov rdx, qword ptr [rdi + 0x510]
00A79DFE  4C 8B C0                        mov r8, rax
00A79E01  48 8B 0D A0 CE 54 00            mov rcx, qword ptr [rip + 0x54cea0]
00A79E08  E8 23 F6 E0 FF                  call 0x140889430
00A79E0D  49 8B CC                        mov rcx, r12
00A79E10  E8 FB 51 7E FF                  call 0x14025f010
00A79E15  E9 94 FE FF FF                  jmp 0x140a79cae
00A79E1A  B9 17 00 00 00                  mov ecx, 0x17
00A79E1F  E8 1C 38 A8 FF                  call 0x1404fd640
00A79E24  CC                              int3
00A79E25  48 8B 15 54 87 3E 00            mov rdx, qword ptr [rip + 0x3e8754]
00A79E2C  48 85 D2                        test rdx, rdx
00A79E2F  0F 84 02 01 00 00               je 0x140a79f37
00A79E35  8B 05 5D 87 3E 00               mov eax, dword ptr [rip + 0x3e875d]
00A79E3B  BD 0C 01 00 00                  mov ebp, 0x10c
00A79E40  85 C0                           test eax, eax
00A79E42  74 44                           je 0x140a79e88
00A79E44  4D 8B C5                        mov r8, r13
00A79E47  48 8D 15 32 58 49 00            lea rdx, [rip + 0x495832]
00A79E4E  44 8B C8                        mov r9d, eax
00A79E51  4C 0F A3 05 47 87 3E 00         bt qword ptr [rip + 0x3e8747], r8
00A79E59  4C 8B 12                        mov r10, qword ptr [rdx]
00A79E5C  0F 92 C0                        setb al
00A79E5F  0F B6 C8                        movzx ecx, al
00A79E62  41 0F B6 42 42                  movzx eax, byte ptr [r10 + 0x42]
00A79E67  C1 E8 06                        shr eax, 6
00A79E6A  83 E0 01                        and eax, 1
00A79E6D  3B C1                           cmp eax, ecx
00A79E6F  0F 85 54 02 00 00               jne 0x140a7a0c9
00A79E75  49 FF C0                        inc r8
00A79E78  48 03 D6                        add rdx, rsi
00A79E7B  49 83 E9 01                     sub r9, 1
00A79E7F  75 D0                           jne 0x140a79e51
00A79E81  48 8B 15 F8 86 3E 00            mov rdx, qword ptr [rip + 0x3e86f8]
00A79E88  4C 8B 15 31 87 3E 00            mov r10, qword ptr [rip + 0x3e8731]
00A79E8F  41 B9 40 00 00 00               mov r9d, 0x40
00A79E95  4D 8D 42 70                     lea r8, [r10 + 0x70]
00A79E99  49 8D 8A B0 00 00 00            lea rcx, [r10 + 0xb0]
00A79EA0  49 8B C0                        mov rax, r8
00A79EA3  4C 3B C1                        cmp r8, rcx
00A79EA6  73 0B                           jae 0x140a79eb3
00A79EA8  0F 18 00                        prefetchnta byte ptr [rax]
00A79EAB  49 03 C1                        add rax, r9
00A79EAE  48 3B C1                        cmp rax, rcx
00A79EB1  72 F5                           jb 0x140a79ea8
00A79EB3  4C 8B 1D CE 86 3E 00            mov r11, qword ptr [rip + 0x3e86ce]
00A79EBA  48 8B C6                        mov rax, rsi
00A79EBD  49 2B 10                        sub rdx, qword ptr [r8]
00A79EC0  41 8B CB                        mov ecx, r11d
00A79EC3  48 D3 CA                        ror rdx, cl
00A79EC6  4C 03 C6                        add r8, rsi
00A79EC9  41 83 C1 F8                     add r9d, -8
00A79ECD  48 83 E8 01                     sub rax, 1
00A79ED1  75 EA                           jne 0x140a79ebd
00A79ED3  45 85 C9                        test r9d, r9d
00A79ED6  74 16                           je 0x140a79eee
00A79ED8  41 0F B6 00                     movzx eax, byte ptr [r8]
00A79EDC  41 8B CB                        mov ecx, r11d
00A79EDF  48 2B D0                        sub rdx, rax
00A79EE2  49 FF C0                        inc r8
00A79EE5  48 D3 CA                        ror rdx, cl
00A79EE8  41 83 C1 FF                     add r9d, -1
00A79EEC  75 EA                           jne 0x140a79ed8
00A79EEE  48 39 15 D3 86 3E 00            cmp qword ptr [rip + 0x3e86d3], rdx
00A79EF5  74 40                           je 0x140a79f37
00A79EF7  4C 39 2D 52 86 3E 00            cmp qword ptr [rip + 0x3e8652], r13
00A79EFE  0F 85 05 02 00 00               jne 0x140a7a109
00A79F04  C7 44 24 78 78 43 42 00         mov dword ptr [rsp + 0x78], 0x424378
00A79F0C  0F 57 C0                        xorps xmm0, xmm0
00A79F0F  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00A79F13  35 78 03 00 00                  xor eax, 0x378
00A79F18  48 89 2D 49 86 3E 00            mov qword ptr [rip + 0x3e8649], rbp
00A79F1F  C1 C8 6E                        ror eax, 0x6e
00A79F22  48 89 05 27 86 3E 00            mov qword ptr [rip + 0x3e8627], rax
00A79F29  0F 11 05 28 86 3E 00            movups xmmword ptr [rip + 0x3e8628], xmm0
00A79F30  4C 89 15 39 86 3E 00            mov qword ptr [rip + 0x3e8639], r10
00A79F37  4C 39 2D 12 86 3E 00            cmp qword ptr [rip + 0x3e8612], r13
00A79F3E  0F 85 C5 01 00 00               jne 0x140a7a109
00A79F44  49 8B 0E                        mov rcx, qword ptr [r14]
00A79F47  4D 8B 07                        mov r8, qword ptr [r15]
00A79F4A  49 8B 06                        mov rax, qword ptr [r14]
00A79F4D  48 3B C8                        cmp rcx, rax
00A79F50  75 F2                           jne 0x140a79f44
00A79F52  0F 31                           rdtsc
00A79F54  48 C1 E2 20                     shl rdx, 0x20
00A79F58  49 B9 00 20 5F A0 12 00 00 00   movabs r9, 0x12a05f2000
00A79F62  48 0B C2                        or rax, rdx
00A79F65  33 D2                           xor edx, edx
00A79F67  48 C1 E8 04                     shr rax, 4
00A79F6B  48 69 C0 BF CB 7F 02            imul rax, rax, 0x27fcbbf
00A79F72  49 F7 F1                        div r9
00A79F75  48 2B D1                        sub rdx, rcx
00A79F78  48 B9 00 40 23 0E 43 00 00 00   movabs rcx, 0x430e234000
00A79F82  48 03 CA                        add rcx, rdx
00A79F85  49 03 C8                        add rcx, r8
00A79F88  48 89 0D 01 86 3E 00            mov qword ptr [rip + 0x3e8601], rcx
00A79F8F  E9 77 FD FF FF                  jmp 0x140a79d0b
00A79F94  48 89 08                        mov qword ptr [rax], rcx
00A79F97  48 89 41 08                     mov qword ptr [rcx + 8], rax
00A79F9B  F0 48 0F C1 1E                  lock xadd qword ptr [rsi], rbx
00A79FA0  80 E3 06                        and bl, 6
00A79FA3  80 FB 02                        cmp bl, 2
00A79FA6  74 54                           je 0x140a79ffc
00A79FA8  48 8B CE                        mov rcx, rsi
00A79FAB  E8 50 76 86 FF                  call 0x1402e1600
00A79FB0  49 8B D4                        mov rdx, r12
00A79FB3  48 8B CD                        mov rcx, rbp
00A79FB6  E8 05 62 9E FF                  call 0x1404601c0
00A79FBB  F7 87 A0 05 00 00 00 00 10 00   test dword ptr [rdi + 0x5a0], 0x100000
00A79FC5  0F 85 6A 01 00 00               jne 0x140a7a135
00A79FCB  48 3B 2D 9E CB 54 00            cmp rbp, qword ptr [rip + 0x54cb9e]
00A79FD2  75 19                           jne 0x140a79fed
00A79FD4  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
00A79FDC  48 83 C4 30                     add rsp, 0x30
00A79FE0  41 5F                           pop r15
00A79FE2  41 5E                           pop r14
00A79FE4  41 5D                           pop r13
00A79FE6  41 5C                           pop r12
00A79FE8  5F                              pop rdi
00A79FE9  5E                              pop rsi
00A79FEA  5D                              pop rbp
00A79FEB  C3                              ret
00A79FEC  CC                              int3
00A79FED  BA 50 73 43 72                  mov edx, 0x72437350
00A79FF2  48 8B CD                        mov rcx, rbp
00A79FF5  E8 E6 D8 87 FF                  call 0x1402f78e0
00A79FFA  EB D8                           jmp 0x140a79fd4
00A79FFC  48 8B CE                        mov rcx, rsi
00A79FFF  E8 CC BD 7E FF                  call 0x140265dd0
00A7A004  EB A2                           jmp 0x140a79fa8
00A7A006  4C 8B C8                        mov r9, rax
00A7A009  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A7A00E  4C 8B C7                        mov r8, rdi
00A7A011  BA 01 00 00 00                  mov edx, 1
00A7A016  B9 94 00 00 00                  mov ecx, 0x94
00A7A01B  E8 40 36 A8 FF                  call 0x1404fd660
00A7A020  CC                              int3
00A7A021  4C 8B C0                        mov r8, rax
00A7A024  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A7A029  45 33 C9                        xor r9d, r9d
00A7A02C  48 8B D7                        mov rdx, rdi
00A7A02F  B9 3C 01 00 00                  mov ecx, 0x13c
00A7A034  E8 27 36 A8 FF                  call 0x1404fd660
00A7A039  CC                              int3
00A7A03A  4C 8B C0                        mov r8, rax
00A7A03D  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A7A042  41 B9 01 00 00 00               mov r9d, 1
00A7A048  48 8B D7                        mov rdx, rdi
00A7A04B  B9 3C 01 00 00                  mov ecx, 0x13c
00A7A050  E8 0B 36 A8 FF                  call 0x1404fd660
00A7A055  CC                              int3
00A7A056  4C 8B C0                        mov r8, rax
00A7A059  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00A7A05E  41 B9 02 00 00 00               mov r9d, 2
00A7A064  48 8B D7                        mov rdx, rdi
00A7A067  B9 3C 01 00 00                  mov ecx, 0x13c
00A7A06C  E8 EF 35 A8 FF                  call 0x1404fd660
00A7A071  CC                              int3
00A7A072  45 33 C0                        xor r8d, r8d
00A7A075  48 8D 15 D4 74 82 FF            lea rdx, [rip - 0x7d8b2c]
00A7A07C  48 8B CF                        mov rcx, rdi
00A7A07F  E8 34 73 82 FF                  call 0x1402a13b8
00A7A084  E9 0B FC FF FF                  jmp 0x140a79c94
00A7A089  48 8B 8F 38 05 00 00            mov rcx, qword ptr [rdi + 0x538]
00A7A090  48 83 E1 F8                     and rcx, 0xfffffffffffffff8
00A7A094  E8 B7 F2 87 FF                  call 0x1402f9350
00A7A099  48 8B 8F 48 06 00 00            mov rcx, qword ptr [rdi + 0x648]
00A7A0A0  48 85 C9                        test rcx, rcx
00A7A0A3  0F 84 39 7F 0C 00               je 0x140b41fe2
00A7A0A9  E8 A2 F2 87 FF                  call 0x1402f9350
00A7A0AE  4C 89 AF 48 06 00 00            mov qword ptr [rdi + 0x648], r13
00A7A0B5  E9 28 7F 0C 00                  jmp 0x140b41fe2
00A7A0BA  BA 54 68 4E 6D                  mov edx, 0x6d4e6854
00A7A0BF  E8 AC 87 10 00                  call 0x140b82870
00A7A0C4  E9 10 FC FF FF                  jmp 0x140a79cd9
00A7A0C9  4C 39 2D 80 84 3E 00            cmp qword ptr [rip + 0x3e8480], r13
00A7A0D0  0F 85 9F FD FF FF               jne 0x140a79e75
00A7A0D6  C7 44 24 70 20 21 00 00         mov dword ptr [rsp + 0x70], 0x2120
00A7A0DE  0F 57 C0                        xorps xmm0, xmm0
00A7A0E1  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00A7A0E5  C1 C8 65                        ror eax, 0x65
00A7A0E8  48 89 05 61 84 3E 00            mov qword ptr [rip + 0x3e8461], rax
00A7A0EF  0F 11 05 62 84 3E 00            movups xmmword ptr [rip + 0x3e8462], xmm0
00A7A0F6  48 89 2D 6B 84 3E 00            mov qword ptr [rip + 0x3e846b], rbp
00A7A0FD  4C 89 15 6C 84 3E 00            mov qword ptr [rip + 0x3e846c], r10
00A7A104  E9 6C FD FF FF                  jmp 0x140a79e75
00A7A109  48 8D 15 80 1D C2 FF            lea rdx, [rip - 0x3de280]
00A7A110  48 39 15 11 84 3E 00            cmp qword ptr [rip + 0x3e8411], rdx
00A7A117  48 8D 35 F2 83 3E 00            lea rsi, [rip + 0x3e83f2]
00A7A11E  0F 84 CB 7E 0C 00               je 0x140b41fef
00A7A124  4C 8B C6                        mov r8, rsi
00A7A127  48 8B CE                        mov rcx, rsi
00A7A12A  E8 A1 1A 9E FF                  call 0x14045bbd0
00A7A12F  90                              nop
00A7A130  E9 BA 7E 0C 00                  jmp 0x140b41fef
00A7A135  48 8B 05 F4 C3 48 00            mov rax, qword ptr [rip + 0x48c3f4]
00A7A13C  48 8B CF                        mov rcx, rdi
00A7A13F  E8 8C 09 C4 FF                  call 0x1406baad0
00A7A144  E9 82 FE FF FF                  jmp 0x140a79fcb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspThreadDelete(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p70;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (48);
    result = KeCleanupThreadState(a1, a2, a3, a4);
    v_r13 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1516))) != 0) goto loc_00A7A006;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1504))) != 0) goto loc_00A7A021;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1508))) != 0) goto loc_00A7A03A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1512))) != 0) goto loc_00A7A056;
    if ((*(unsigned __int64 *)(a1 + 1744)) != (a1 + 1744)) goto loc_00A79DBD;
    if ((*(unsigned __int64 *)(a1 + 40)) != 0) goto loc_00A7A072;
loc_00A79C94:
    v_rbx = (v_rbx) | (-1);
    if ((*(unsigned __int64 *)(a1 + 1296)) != 0) goto loc_00A79DD5;
loc_00A79CAE:
    if (((8) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 1440))))) != 0) goto loc_00A7A089;
    *(unsigned __int64 *)(a1 + 1336) = 0;
    if (*(unsigned __int64 *)(a1 + 1696) != 0) goto loc_00A7A0BA;
loc_00A79CD9:
loc_00A79CED:
    if ((*(unsigned __int64 *)(v_r14)) != (*(unsigned __int64 *)(v_r14))) goto loc_00A79CED;
    a1 = (*(unsigned __int64 *)(v_r15)) - (*(unsigned __int64 *)(v_r14));
    if (a1 >= (*(unsigned __int64 *)(v_rip + 4098187))) goto loc_00A79E25;
loc_00A79D0B:
    if ((*(unsigned __int64 *)(a1 + 1936)) == 0) goto loc_00A79D36;
    a2 = (0) & (-16);
    if (condition_is_equal) goto loc_00A79D36;
    result = (unsigned int)((0) & (15));
    if (!(condition_is_below_or_equal)) {
        result = (unsigned int)(-(result));
        a1 = (int)((unsigned int)(result));
    }
    if (*(unsigned __int64 *)(a1 + 544) == 0) goto loc_00A79FD4;
    if ((*(unsigned __int64 *)(a1 + 1400)) == 0) goto loc_00A79FBB;
    result = PspLockProcessExclusive(*(unsigned __int64 *)(a1 + 544), *(unsigned __int64 *)(gs_base + (0 + 392)), a3, *(unsigned __int64 *)(a1 + 1744));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(a1 + 544) + 1504, a2, a3, *(unsigned __int64 *)(a1 + 1744));
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(a1 + 544) + 1504;
        a2 = result;
        a1 = *(unsigned __int64 *)(a1 + 544) + 1504;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int64 *)(a1 + 1744));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = KeFoldProcessStatisticsThread(a1, a2, a3, *(unsigned __int64 *)(a1 + 1744));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1400) + 8)) != (a1 + 1400)) goto loc_00A79DB6;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1400 + 8))) == (a1 + 1400)) goto loc_00A79F94;
loc_00A79DB6:
loc_00A79DBD:
    v_stack_m48 = 0;
    result = KeBugCheckEx(454, 21, a1, *(unsigned __int64 *)(a1 + 1744));
loc_00A79DD5:
    result = ExMapHandleToPointer(*(unsigned __int64 *)(v_rip + 5557947), *(unsigned __int64 *)(a1 + 1296), a1, *(unsigned __int64 *)(a1 + 1744));
    if (result == 0) goto loc_00A79E1A;
    result = ExDestroyHandle(*(unsigned __int64 *)(v_rip + 5557920), *(unsigned __int64 *)(a1 + 1296), result, *(unsigned __int64 *)(a1 + 1744));
    result = KiLeaveCriticalRegionUnsafe(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(a1 + 1296), result, *(unsigned __int64 *)(a1 + 1744));
    goto loc_00A79CAE;
loc_00A79E1A:
    result = KeBugCheck(23, *(unsigned __int64 *)(a1 + 1296), result, *(unsigned __int64 *)(a1 + 1744));
loc_00A79E25:
    if (*(unsigned __int64 *)(v_rip + 4097876) == 0) goto loc_00A79F37;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4097885))) == 0) goto loc_00A79E88;
loc_00A79E51:
    result = (condition_is_below) ? 1 : 0;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 4806706) + 66)) >> (6));
    result = (unsigned int)((result) & (1));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned __int8)(result)))) goto loc_00A7A0C9;
loc_00A79E75:
    a3 = (0) + 1;
    a2 = (v_rip + 4806706) + (*(unsigned __int64 *)(a1 + 544) + 1504);
    a4 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4097885))))) - (1);
    if (condition_is_not_equal) goto loc_00A79E51;
loc_00A79E88:
    if ((*(unsigned __int64 *)(v_rip + 4097841) + 112) >= (*(unsigned __int64 *)(v_rip + 4097841) + 176)) goto loc_00A79EB3;
loc_00A79EA8:
    result = (*(unsigned __int64 *)(v_rip + 4097841) + 112) + (64);
    if (result < (*(unsigned __int64 *)(v_rip + 4097841) + 176)) goto loc_00A79EA8;
loc_00A79EB3:
loc_00A79EBD:
    a2 = (*(unsigned __int64 *)(v_rip + 4097784)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4097841) + 112));
    a3 = (*(unsigned __int64 *)(v_rip + 4097841) + 112) + (*(unsigned __int64 *)(a1 + 544) + 1504);
    a4 = (unsigned int)((64) + (-8));
    result = (*(unsigned __int64 *)(a1 + 544) + 1504) - (1);
    if (condition_is_not_equal) goto loc_00A79EBD;
    if ((unsigned int)(a4) == 0) goto loc_00A79EEE;
loc_00A79ED8:
    a2 = (a2) - (*(unsigned __int8 *)(a3));
    a3 = (a3) + 1;
    a4 = (unsigned int)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00A79ED8;
loc_00A79EEE:
    if ((*(unsigned __int64 *)(v_rip + 4097747)) == a2) goto loc_00A79F37;
    if ((*(unsigned __int64 *)(v_rip + 4097618)) != 0) goto loc_00A7A109;
    v_stack_p10 = 0x424378ULL;
    result = (unsigned int)(((unsigned int)(v_stack_p10)) ^ (888));
    *(unsigned __int64 *)(v_rip + 4097609) = 268;
    *(unsigned __int64 *)(v_rip + 4097575) = result;
    *(unsigned __int64 *)(v_rip + 4097576) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 4097593) = *(unsigned __int64 *)(v_rip + 4097841);
loc_00A79F37:
    if ((*(unsigned __int64 *)(v_rip + 4097554)) != 0) goto loc_00A7A109;
loc_00A79F44:
    if ((*(unsigned __int64 *)(a1 + 1400)) != (*(unsigned __int64 *)(a1 + 1400))) goto loc_00A79F44;
    a2 = (a2) << (32);
    result = (*(unsigned __int64 *)(a1 + 1400)) | (a2);
    a2 = 0;
    result = (result) >> (4);
    result = (result) * (result);
    a2 = (a2) - (*(unsigned __int64 *)(a1 + 1400));
    a1 = (*(unsigned __int64 *)(a1 + 1400)) + (a2);
    a1 = (a1) + (*(unsigned __int64 *)(result));
    *(unsigned __int64 *)(v_rip + 4097537) = a1;
    goto loc_00A79D0B;
loc_00A79F94:
    *(unsigned __int64 *)(result) = a1;
    *(unsigned __int64 *)(a1 + 8) = result;
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_00A79FFC;
loc_00A79FA8:
    result = KeAbPostRelease(*(unsigned __int64 *)(a1 + 544) + 1504, a2, *(unsigned __int64 *)(result), a4);
    result = PspUnlockProcessExclusive(268, *(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(result), a4);
loc_00A79FBB:
    if (((*(unsigned int *)(a1 + 1440)) & (0x100000ULL)) != 0) goto loc_00A7A135;
loc_00A79FCB:
    if (268 != (*(unsigned __int64 *)(v_rip + 5557150))) goto loc_00A79FED;
loc_00A79FD4:
    v_rsp = (v_rsp) + (48);
    return result;
loc_00A79FED:
    result = ObfDereferenceObjectWithTag(268, (unsigned int)(0x72437350ULL), *(unsigned __int64 *)(result), a4);
    goto loc_00A79FD4;
loc_00A79FFC:
    result = ExfTryToWakePushLock(*(unsigned __int64 *)(a1 + 544) + 1504, (unsigned int)(0x72437350ULL), *(unsigned __int64 *)(result), a4);
    goto loc_00A79FA8;
loc_00A7A006:
    v_stack_p20 = 0;
    result = KeBugCheckEx(148, 1, a1, result);
loc_00A7A021:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(316, a1, result, a4);
loc_00A7A03A:
    v_stack_p20 = 0;
    result = KeBugCheckEx(316, a1, result, 1);
loc_00A7A056:
    v_stack_p20 = 0;
    result = KeBugCheckEx(316, a1, result, 2);
loc_00A7A072:
    a3 = 0;
    result = KeEnumerateKernelStackSegments(a1, v_rip - 8227628, a3, 2);
    goto loc_00A79C94;
loc_00A7A089:
    a1 = (*(unsigned __int64 *)(a1 + 1336)) & (-8);
    result = ObfDereferenceObject(a1, v_rip - 8227628, a3, 2);
    result = ObfDereferenceObject(*(unsigned __int64 *)(a1 + 1608), v_rip - 8227628, a3, 2);
    *(unsigned __int64 *)(a1 + 1608) = 0;
loc_00A7A0BA:
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 1608), (unsigned int)(0x6D4E6854ULL), a3, 2);
    goto loc_00A79CD9;
loc_00A7A0C9:
    if ((*(unsigned __int64 *)(v_rip + 4097152)) != 0) goto loc_00A79E75;
    v_stack_p70 = 0x2120ULL;
    *(unsigned __int64 *)(v_rip + 4097121) = (unsigned int)(v_stack_p70);
    *(unsigned __int64 *)(v_rip + 4097122) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 4097131) = 268;
    *(unsigned __int64 *)(v_rip + 4097132) = *(unsigned __int64 *)(v_rip + 4097841);
    goto loc_00A79E75;
loc_00A7A109:
    result = KeInitializeDpc(v_rip + 4097010, v_rip - 4055680, v_rip + 4097010, 2);
loc_00A7A135:
    result = guard_dispatch_icall(a1, v_rip - 4055680, v_rip + 4097010, 2);
    goto loc_00A79FCB;
}
```

## 5. (Beta) C Style

```c
int64_t PspThreadDelete(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint32_t v_stack_p70;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (48);
    result = KeCleanupThreadState(Arg1, Arg2, Arg3, a4);
    local_r13 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5EC))) != 0) goto loc_00A7A006;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5E0))) != 0) goto loc_00A7A021;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5E4))) != 0) goto loc_00A7A03A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5E8))) != 0) goto loc_00A7A056;
    if ((*(uint64_t *)(arg1 + 0x6D0)) != (Arg1 + 1744)) goto loc_00A79DBD;
    if ((*(uint64_t *)(arg1 + 0x28)) != 0) goto loc_00A7A072;
loc_00A79C94:
    local_rbx = (local_rbx) | (-1);
    if ((*(uint64_t *)(arg1 + 0x510)) != 0) goto loc_00A79DD5;
loc_00A79CAE:
    if (((8) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5A0))))) != 0) goto loc_00A7A089;
    *(uint64_t *)(arg1 + 0x538) = 0;
    if (*(uint64_t *)(arg1 + 0x6A0) != 0) goto loc_00A7A0BA;
loc_00A79CD9:
loc_00A79CED:
    if ((*(uint64_t *)(local_r14)) != (*(uint64_t *)(local_r14))) goto loc_00A79CED;
    Arg1 = (*(uint64_t *)(local_r15)) - (*(uint64_t *)(local_r14));
    if (Arg1 >= (*(uint64_t *)(v_rip + 0x3E888B))) goto loc_00A79E25;
loc_00A79D0B:
    if ((*(uint64_t *)(arg1 + 0x790)) == 0) goto loc_00A79D36;
    Arg2 = (0) & (-16);
    if (condition_is_equal) goto loc_00A79D36;
    result = (uint32_t)((0) & (15));
    if (!(condition_is_below_or_equal)) {
        result = (uint32_t)(-(result));
        Arg1 = (int32_t)((uint32_t)(result));
    }
    if (*(uint64_t *)(arg1 + 0x220) == 0) goto loc_00A79FD4;
    if ((*(uint64_t *)(arg1 + 0x578)) == 0) goto loc_00A79FBB;
    result = PspLockProcessExclusive(*(uint64_t *)(arg1 + 0x220), *(uint64_t *)(gs_base + (0 + 0x188)), Arg3, *(uint64_t *)(arg1 + 0x6D0));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(arg1 + 0x220) + 1504, Arg2, Arg3, *(uint64_t *)(arg1 + 0x6D0));
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(arg1 + 0x220) + 1504;
        Arg2 = result;
        Arg1 = *(uint64_t *)(arg1 + 0x220) + 1504;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint64_t *)(arg1 + 0x6D0));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = KeFoldProcessStatisticsThread(Arg1, Arg2, Arg3, *(uint64_t *)(arg1 + 0x6D0));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x578) + 0x8)) != (Arg1 + 1400)) goto loc_00A79DB6;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x578 + 0x8))) == (Arg1 + 1400)) goto loc_00A79F94;
loc_00A79DB6:
loc_00A79DBD:
    v_stack_m48 = 0;
    result = KeBugCheckEx(454, 21, Arg1, *(uint64_t *)(arg1 + 0x6D0));
loc_00A79DD5:
    result = ExMapHandleToPointer(*(uint64_t *)(v_rip + 0x54CEBB), *(uint64_t *)(arg1 + 0x510), Arg1, *(uint64_t *)(arg1 + 0x6D0));
    if (result == 0) goto loc_00A79E1A;
    result = ExDestroyHandle(*(uint64_t *)(v_rip + 0x54CEA0), *(uint64_t *)(arg1 + 0x510), result, *(uint64_t *)(arg1 + 0x6D0));
    result = KiLeaveCriticalRegionUnsafe(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(arg1 + 0x510), result, *(uint64_t *)(arg1 + 0x6D0));
    goto loc_00A79CAE;
loc_00A79E1A:
    result = KeBugCheck(23, *(uint64_t *)(arg1 + 0x510), result, *(uint64_t *)(arg1 + 0x6D0));
loc_00A79E25:
    if (*(uint64_t *)(v_rip + 0x3E8754) == 0) goto loc_00A79F37;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3E875D))) == 0) goto loc_00A79E88;
loc_00A79E51:
    result = (condition_is_below) ? 1 : 0;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_rip + 0x495832) + 0x42)) >> (6));
    result = (uint32_t)((result) & (1));
    if (((uint32_t)(result)) != ((uint32_t)((uint8_t)(result)))) goto loc_00A7A0C9;
loc_00A79E75:
    Arg3 = (0) + 1;
    Arg2 = (v_rip + 4806706) + (*(uint64_t *)(arg1 + 0x220) + 1504);
    a4 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3E875D))))) - (1);
    if (condition_is_not_equal) goto loc_00A79E51;
loc_00A79E88:
    if ((*(uint64_t *)(v_rip + 0x3E8731) + 112) >= (*(uint64_t *)(v_rip + 0x3E8731) + 176)) goto loc_00A79EB3;
loc_00A79EA8:
    result = (*(uint64_t *)(v_rip + 0x3E8731) + 112) + (64);
    if (result < (*(uint64_t *)(v_rip + 0x3E8731) + 176)) goto loc_00A79EA8;
loc_00A79EB3:
loc_00A79EBD:
    Arg2 = (*(uint64_t *)(v_rip + 0x3E86F8)) - (*(uint64_t *)(*(uint64_t *)(v_rip + 0x3E8731) + 0x70));
    Arg3 = (*(uint64_t *)(v_rip + 0x3E8731) + 112) + (*(uint64_t *)(arg1 + 0x220) + 1504);
    a4 = (uint32_t)((64) + (-8));
    result = (*(uint64_t *)(arg1 + 0x220) + 1504) - (1);
    if (condition_is_not_equal) goto loc_00A79EBD;
    if ((uint32_t)(a4) == 0) goto loc_00A79EEE;
loc_00A79ED8:
    Arg2 = (Arg2) - (*(uint8_t *)(Arg3));
    Arg3 = (Arg3) + 1;
    a4 = (uint32_t)((a4) + (-1));
    if (condition_is_not_equal) goto loc_00A79ED8;
loc_00A79EEE:
    if ((*(uint64_t *)(v_rip + 0x3E86D3)) == Arg2) goto loc_00A79F37;
    if ((*(uint64_t *)(v_rip + 0x3E8652)) != 0) goto loc_00A7A109;
    v_stack_p10 = 0x424378ULL;
    result = (uint32_t)(((uint32_t)(v_stack_p10)) ^ (888));
    *(uint64_t *)(v_rip + 0x3E8649) = 268;
    *(uint64_t *)(v_rip + 0x3E8627) = result;
    *(uint64_t *)(v_rip + 0x3E8628) = v_xmm0;
    *(uint64_t *)(v_rip + 0x3E8639) = *(uint64_t *)(v_rip + 0x3E8731);
loc_00A79F37:
    if ((*(uint64_t *)(v_rip + 0x3E8612)) != 0) goto loc_00A7A109;
loc_00A79F44:
    if ((*(uint64_t *)(arg1 + 0x578)) != (*(uint64_t *)(arg1 + 0x578))) goto loc_00A79F44;
    Arg2 = (Arg2) << (32);
    result = (*(uint64_t *)(arg1 + 0x578)) | (Arg2);
    Arg2 = 0;
    result = (result) >> (4);
    result = (result) * (result);
    Arg2 = (Arg2) - (*(uint64_t *)(arg1 + 0x578));
    Arg1 = (*(uint64_t *)(arg1 + 0x578)) + (Arg2);
    Arg1 = (Arg1) + (*(uint64_t *)(result));
    *(void **)(v_rip + 0x3E8601) = Arg1;
    goto loc_00A79D0B;
loc_00A79F94:
    *(void **)(result) = Arg1;
    *(uint64_t *)(arg1 + 0x8) = result;
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_00A79FFC;
loc_00A79FA8:
    result = KeAbPostRelease(*(uint64_t *)(arg1 + 0x220) + 1504, Arg2, *(uint64_t *)(result), a4);
    result = PspUnlockProcessExclusive(268, *(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(result), a4);
loc_00A79FBB:
    if (((*(uint32_t *)(arg1 + 0x5A0)) & (0x100000ULL)) != 0) goto loc_00A7A135;
loc_00A79FCB:
    if (268 != (*(uint64_t *)(v_rip + 0x54CB9E))) goto loc_00A79FED;
loc_00A79FD4:
    local_rsp = (local_rsp) + (48);
    return result;
loc_00A79FED:
    result = ObfDereferenceObjectWithTag(268, (uint32_t)(0x72437350ULL), *(uint64_t *)(result), a4);
    goto loc_00A79FD4;
loc_00A79FFC:
    result = ExfTryToWakePushLock(*(uint64_t *)(arg1 + 0x220) + 1504, (uint32_t)(0x72437350ULL), *(uint64_t *)(result), a4);
    goto loc_00A79FA8;
loc_00A7A006:
    v_stack_p20 = 0;
    result = KeBugCheckEx(148, 1, Arg1, result);
loc_00A7A021:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(316, Arg1, result, a4);
loc_00A7A03A:
    v_stack_p20 = 0;
    result = KeBugCheckEx(316, Arg1, result, 1);
loc_00A7A056:
    v_stack_p20 = 0;
    result = KeBugCheckEx(316, Arg1, result, 2);
loc_00A7A072:
    Arg3 = 0;
    result = KeEnumerateKernelStackSegments(Arg1, v_rip - 8227628, Arg3, 2);
    goto loc_00A79C94;
loc_00A7A089:
    Arg1 = (*(uint64_t *)(arg1 + 0x538)) & (-8);
    result = ObfDereferenceObject(Arg1, v_rip - 8227628, Arg3, 2);
    result = ObfDereferenceObject(*(uint64_t *)(arg1 + 0x648), v_rip - 8227628, Arg3, 2);
    *(uint64_t *)(arg1 + 0x648) = 0;
loc_00A7A0BA:
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x648), (uint32_t)(0x6D4E6854ULL), Arg3, 2);
    goto loc_00A79CD9;
loc_00A7A0C9:
    if ((*(uint64_t *)(v_rip + 0x3E8480)) != 0) goto loc_00A79E75;
    v_stack_p70 = 0x2120ULL;
    *(uint64_t *)(v_rip + 0x3E8461) = (uint32_t)(v_stack_p70);
    *(uint64_t *)(v_rip + 0x3E8462) = v_xmm0;
    *(uint64_t *)(v_rip + 0x3E846B) = 268;
    *(uint64_t *)(v_rip + 0x3E846C) = *(uint64_t *)(v_rip + 0x3E8731);
    goto loc_00A79E75;
loc_00A7A109:
    result = KeInitializeDpc(v_rip + 4097010, v_rip - 4055680, v_rip + 4097010, 2);
loc_00A7A135:
    result = guard_dispatch_icall(Arg1, v_rip - 4055680, v_rip + 4097010, 2);
    goto loc_00A79FCB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x510` | `64` | `R` |
| `Arg1` | `+ 0x538` | `64` | `R` |
| `Arg1` | `+ 0x538` | `64` | `W` |
| `Arg1` | `+ 0x578` | `64` | `R` |
| `Arg1` | `+ 0x5A0` | `32` | `R` |
| `Arg1` | `+ 0x5E0` | `32` | `R` |
| `Arg1` | `+ 0x5E4` | `32` | `R` |
| `Arg1` | `+ 0x5E8` | `32` | `R` |
| `Arg1` | `+ 0x5EC` | `32` | `R` |
| `Arg1` | `+ 0x648` | `64` | `R` |
| `Arg1` | `+ 0x648` | `64` | `W` |
| `Arg1` | `+ 0x6A0` | `64` | `R` |
| `Arg1` | `+ 0x6D0` | `64` | `R` |
| `Arg1` | `+ 0x790` | `64` | `R` |
| `Arg1` | `+ 0x790` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A79C20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
