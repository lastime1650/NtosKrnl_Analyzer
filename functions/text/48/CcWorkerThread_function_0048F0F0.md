# CcWorkerThread

- RVA: `0x0048F0F0`–`0x0048F732` (길이 `1,602` bytes)
- VA: `0x000000014048F0F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B2A64`
- 디코드: `349`개 명령, `1,602/1,602` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **24**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0048F1AA` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0048F20B` → [CcShouldWorkOnThisQueue](../35/CcShouldWorkOnThisQueue_function_003587E8.md) (function, `0x003587E8`)
- `0x0048F21B` → [CcFindNextWorkQueueEntry](../35/CcFindNextWorkQueueEntry_function_00356BFC.md) (function, `0x00356BFC`)
- `0x0048F25B` → [CcIsWriteBehindThreadpoolAtLowPriority](../35/CcIsWriteBehindThreadpoolAtLowPriority_function_003570DC.md) (function, `0x003570DC`)
- `0x0048F28E` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0048F2E5` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x0048F329` → [CcWriteBehind](../35/CcWriteBehind_function_00356EAC.md) (function, `0x00356EAC`)
- `0x0048F370` → [CcLazyWriteScanVolume](../38/CcLazyWriteScanVolume_function_00388DC0.md) (function, `0x00388DC0`)
- `0x0048F391` → [CcPerformReadAhead](CcPerformReadAhead_function_0048F738.md) (function, `0x0048F738`)
- `0x0048F39B` → [CcLazyWriteScan](../3C/CcLazyWriteScan_function_003C9394.md) (function, `0x003C9394`)
- `0x0048F42F` → [CcPerfLogWorkItemEnqueue](../35/CcPerfLogWorkItemEnqueue_function_00357340.md) (function, `0x00357340`)
- `0x0048F4A7` → [CcFreeWorkQueueEntry](../35/CcFreeWorkQueueEntry_function_0035723C.md) (function, `0x0035723C`)
- `0x0048F4E1` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0048F534` → [CcDereferencePartitionAndPrivateVolumeCacheMap](../38/CcDereferencePartitionAndPrivateVolumeCacheMap_function_0038B94C.md) (function, `0x0038B94C`)
- `0x0048F56E` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0048F57B` → [CcNotifyWriteBehindVolume](../3C/CcNotifyWriteBehindVolume_function_003CC134.md) (function, `0x003CC134`)
- `0x0048F588` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x0048F5A7` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0048F5CD` → [CcReEngageWorkerThreads](../57/CcReEngageWorkerThreads_function_0057BEB0.md) (function, `0x0057BEB0`)
- `0x0048F65C` → [CcLogExtraWBThreadAction](../4D/CcLogExtraWBThreadAction_function_004D737C.md) (function, `0x004D737C`)
- `0x0048F669` → [CcPerfLogWorkItemDequeue](../35/CcPerfLogWorkItemDequeue_function_0035877C.md) (function, `0x0035877C`)
- `0x0048F68F` → [CcPerfLogWorkItemComplete](../35/CcPerfLogWorkItemComplete_function_00358710.md) (function, `0x00358710`)
- `0x0048F709` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0048F728` → [CcLogExtraWBThreadAction](../4D/CcLogExtraWBThreadAction_function_004D737C.md) (function, `0x004D737C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0048F293` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x0048F439` → RVA `0x00E65B64` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x0048F245` → [sub_006F6D7E + 0x25](../6F/Unknown_function_006F6D7E.md) (`tail-transfer`)
  - `0x0048F44F` → [sub_006F6D7E + 0xFA](../6F/Unknown_function_006F6D7E.md) (`tail-transfer`)
  - `0x0048F5DF` → [sub_006F6D7E](../6F/Unknown_function_006F6D7E.md) (`tail-transfer`)
  - `0x0048F5F0` → [sub_006F6D7E](../6F/Unknown_function_006F6D7E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0048F0F0  4C 8B DC                        mov r11, rsp
0048F0F3  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
0048F0F7  53                              push rbx
0048F0F8  56                              push rsi
0048F0F9  57                              push rdi
0048F0FA  41 54                           push r12
0048F0FC  41 55                           push r13
0048F0FE  41 56                           push r14
0048F100  41 57                           push r15
0048F102  48 81 EC D0 00 00 00            sub rsp, 0xd0
0048F109  33 F6                           xor esi, esi
0048F10B  44 8B FE                        mov r15d, esi
0048F10E  44 8B F6                        mov r14d, esi
0048F111  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
0048F116  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0048F11B  48 89 4C 24 60                  mov qword ptr [rsp + 0x60], rcx
0048F120  0F 57 C0                        xorps xmm0, xmm0
0048F123  33 C0                           xor eax, eax
0048F125  41 0F 11 43 80                  movups xmmword ptr [r11 - 0x80], xmm0
0048F12A  49 89 43 90                     mov qword ptr [r11 - 0x70], rax
0048F12E  0F 57 C9                        xorps xmm1, xmm1
0048F131  41 0F 11 4B 98                  movups xmmword ptr [r11 - 0x68], xmm1
0048F136  49 89 43 A8                     mov qword ptr [r11 - 0x58], rax
0048F13A  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
0048F13F  44 8B 61 20                     mov r12d, dword ptr [rcx + 0x20]
0048F143  44 89 A4 24 28 01 00 00         mov dword ptr [rsp + 0x128], r12d
0048F14B  44 89 64 24 50                  mov dword ptr [rsp + 0x50], r12d
0048F150  41 8D 44 24 FF                  lea eax, [r12 - 1]
0048F155  83 F8 01                        cmp eax, 1
0048F158  0F 87 31 04 00 00               ja 0x14048f58f
0048F15E  41 83 FC 02                     cmp r12d, 2
0048F162  0F 94 84 24 20 01 00 00         sete byte ptr [rsp + 0x120]
0048F16A  4C 8B 69 38                     mov r13, qword ptr [rcx + 0x38]
0048F16E  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
0048F173  48 8B 79 48                     mov rdi, qword ptr [rcx + 0x48]
0048F177  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
0048F17C  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
0048F180  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0048F185  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0048F18D  8B DE                           mov ebx, esi
0048F18F  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
0048F193  40 88 B4 24 18 01 00 00         mov byte ptr [rsp + 0x118], sil
0048F19B  49 8D 8D 40 03 00 00            lea rcx, [r13 + 0x340]
0048F1A2  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
0048F1AA  E8 F1 65 DE FF                  call 0x1402757a0
0048F1AF  40 38 74 24 30                  cmp byte ptr [rsp + 0x30], sil
0048F1B4  0F 85 F3 03 00 00               jne 0x14048f5ad
0048F1BA  48 81 7C 24 48 5E 8A 00 00      cmp qword ptr [rsp + 0x48], 0x8a5e
0048F1C3  0F 84 0E 04 00 00               je 0x14048f5d7
0048F1C9  41 83 FC 02                     cmp r12d, 2
0048F1CD  0F 84 22 04 00 00               je 0x14048f5f5
0048F1D3  F6 C3 01                        test bl, 1
0048F1D6  0F 84 A9 02 00 00               je 0x14048f485
0048F1DC  F6 C3 02                        test bl, 2
0048F1DF  0F 85 79 02 00 00               jne 0x14048f45e
0048F1E5  83 CB 02                        or ebx, 2
0048F1E8  4C 8D 7F 58                     lea r15, [rdi + 0x58]
0048F1EC  4D 39 3F                        cmp qword ptr [r15], r15
0048F1EF  0F 84 69 02 00 00               je 0x14048f45e
0048F1F5  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
0048F1FA  44 8A 8C 24 20 01 00 00         mov r9b, byte ptr [rsp + 0x120]
0048F202  4D 8B C7                        mov r8, r15
0048F205  48 8B D7                        mov rdx, rdi
0048F208  49 8B CD                        mov rcx, r13
0048F20B  E8 D8 95 EC FF                  call 0x1403587e8
0048F210  84 C0                           test al, al
0048F212  0F 84 3C 02 00 00               je 0x14048f454
0048F218  4D 8B C7                        mov r8, r15
0048F21B  E8 DC 79 EC FF                  call 0x140356bfc
0048F220  4C 8B F0                        mov r14, rax
0048F223  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0048F228  48 85 C0                        test rax, rax
0048F22B  0F 84 23 02 00 00               je 0x14048f454
0048F231  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
0048F23B  48 8B 18                        mov rbx, qword ptr [rax]
0048F23E  40 38 B7 E0 00 00 00            cmp byte ptr [rdi + 0xe0], sil
0048F245  0F 85 58 7B 26 00               jne 0x1406f6da3
0048F24B  48 8D 47 68                     lea rax, [rdi + 0x68]
0048F24F  4C 3B F8                        cmp r15, rax
0048F252  0F 84 CB 03 00 00               je 0x14048f623
0048F258  49 8B CD                        mov rcx, r13
0048F25B  E8 7C 7E EC FF                  call 0x1403570dc
0048F260  84 C0                           test al, al
0048F262  0F 84 D1 01 00 00               je 0x14048f439
0048F268  8A 9C 24 18 01 00 00            mov bl, byte ptr [rsp + 0x118]
0048F26F  48 8D 47 68                     lea rax, [rdi + 0x68]
0048F273  4C 3B F8                        cmp r15, rax
0048F276  0F 85 B3 03 00 00               jne 0x14048f62f
0048F27C  48 8D 87 BC 00 00 00            lea rax, [rdi + 0xbc]
0048F283  F0 FF 00                        lock inc dword ptr [rax]
0048F286  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
0048F28E  E8 4D 3A EB FF                  call 0x140342ce0
0048F293  48 8B 05 76 78 B3 00            mov rax, qword ptr [rip + 0xb37876]
0048F29A  0F BA E0 11                     bt eax, 0x11
0048F29E  0F 82 A4 03 00 00               jb 0x14048f648
0048F2A4  48 8B 05 65 78 B3 00            mov rax, qword ptr [rip + 0xb37865]
0048F2AB  0F BA E0 11                     bt eax, 0x11
0048F2AF  0F 82 B1 03 00 00               jb 0x14048f666
0048F2B5  41 8B 8E 80 00 00 00            mov ecx, dword ptr [r14 + 0x80]
0048F2BC  83 E9 01                        sub ecx, 1
0048F2BF  0F 84 C5 00 00 00               je 0x14048f38a
0048F2C5  83 E9 01                        sub ecx, 1
0048F2C8  74 2A                           je 0x14048f2f4
0048F2CA  83 E9 01                        sub ecx, 1
0048F2CD  0F 84 82 00 00 00               je 0x14048f355
0048F2D3  83 F9 01                        cmp ecx, 1
0048F2D6  0F 85 C4 00 00 00               jne 0x14048f3a0
0048F2DC  45 33 C0                        xor r8d, r8d
0048F2DF  33 D2                           xor edx, edx
0048F2E1  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0048F2E5  E8 26 00 EB FF                  call 0x14033f310
0048F2EA  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0048F2EF  E9 AC 00 00 00                  jmp 0x14048f3a0
0048F2F4  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0048F2FD  48 89 8C 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rcx
0048F305  8B 81 A4 05 00 00               mov eax, dword ptr [rcx + 0x5a4]
0048F30B  83 C8 02                        or eax, 2
0048F30E  89 81 A4 05 00 00               mov dword ptr [rcx + 0x5a4], eax
0048F314  8B 5C 24 34                     mov ebx, dword ptr [rsp + 0x34]
0048F318  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
0048F31D  4C 8B C7                        mov r8, rdi
0048F320  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
0048F325  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0048F329  E8 7E 7B EC FF                  call 0x140356eac
0048F32E  83 FB 0A                        cmp ebx, 0xa
0048F331  72 44                           jb 0x14048f377
0048F333  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0048F33C  48 89 8C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rcx
0048F344  8B 81 A4 05 00 00               mov eax, dword ptr [rcx + 0x5a4]
0048F34A  83 E0 FD                        and eax, 0xfffffffd
0048F34D  89 81 A4 05 00 00               mov dword ptr [rcx + 0x5a4], eax
0048F353  EB 4B                           jmp 0x14048f3a0
0048F355  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
0048F35D  48 8B 48 40                     mov rcx, qword ptr [rax + 0x40]
0048F361  45 8B 4E 10                     mov r9d, dword ptr [r14 + 0x10]
0048F365  4D 8B C6                        mov r8, r14
0048F368  48 8B D7                        mov rdx, rdi
0048F36B  48 85 C9                        test rcx, rcx
0048F36E  74 28                           je 0x14048f398
0048F370  E8 4B 9A EF FF                  call 0x140388dc0
0048F375  EB 29                           jmp 0x14048f3a0
0048F377  FF C3                           inc ebx
0048F379  89 5C 24 34                     mov dword ptr [rsp + 0x34], ebx
0048F37D  48 81 7C 24 48 5E 8A 00 00      cmp qword ptr [rsp + 0x48], 0x8a5e
0048F386  75 AB                           jne 0x14048f333
0048F388  EB 8E                           jmp 0x14048f318
0048F38A  49 8B 56 10                     mov rdx, qword ptr [r14 + 0x10]
0048F38E  49 8B CE                        mov rcx, r14
0048F391  E8 A2 03 00 00                  call 0x14048f738
0048F396  EB 08                           jmp 0x14048f3a0
0048F398  49 8B CD                        mov rcx, r13
0048F39B  E8 F4 9F F3 FF                  call 0x1403c9394
0048F3A0  EB 4A                           jmp 0x14048f3ec
0048F3A2  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
0048F3A7  41 83 BE 80 00 00 00 02         cmp dword ptr [r14 + 0x80], 2
0048F3AF  75 10                           jne 0x14048f3c1
0048F3B1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0048F3BA  83 A0 A4 05 00 00 FD            and dword ptr [rax + 0x5a4], 0xfffffffd
0048F3C1  33 F6                           xor esi, esi
0048F3C3  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
0048F3C8  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
0048F3CD  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
0048F3D2  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
0048F3DA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0048F3DF  44 8B 64 24 50                  mov r12d, dword ptr [rsp + 0x50]
0048F3E4  44 89 A4 24 28 01 00 00         mov dword ptr [rsp + 0x128], r12d
0048F3EC  48 8D 47 68                     lea rax, [rdi + 0x68]
0048F3F0  4C 3B F8                        cmp r15, rax
0048F3F3  0F 85 7A 02 00 00               jne 0x14048f673
0048F3F9  48 8D 87 BC 00 00 00            lea rax, [rdi + 0xbc]
0048F400  F0 FF 08                        lock dec dword ptr [rax]
0048F403  48 8B 05 06 77 B3 00            mov rax, qword ptr [rip + 0xb37706]
0048F40A  48 81 7C 24 48 5E 8A 00 00      cmp qword ptr [rsp + 0x48], 0x8a5e
0048F413  0F 85 81 00 00 00               jne 0x14048f49a
0048F419  0F BA E0 11                     bt eax, 0x11
0048F41D  0F 83 6A FD FF FF               jae 0x14048f18d
0048F423  45 33 C9                        xor r9d, r9d
0048F426  41 B0 01                        mov r8b, 1
0048F429  49 8B D6                        mov rdx, r14
0048F42C  49 8B CF                        mov rcx, r15
0048F42F  E8 0C 7F EC FF                  call 0x140357340
0048F434  E9 54 FD FF FF                  jmp 0x14048f18d
0048F439  8B 0D 25 67 9D 00               mov ecx, dword ptr [rip + 0x9d6725]
0048F43F  48 03 8F D0 00 00 00            add rcx, qword ptr [rdi + 0xd0]
0048F446  48 3B D9                        cmp rbx, rcx
0048F449  0F 8C 19 FE FF FF               jl 0x14048f268
0048F44F  E9 24 7A 26 00                  jmp 0x1406f6e78
0048F454  41 83 FC 02                     cmp r12d, 2
0048F458  0F 85 75 FD FF FF               jne 0x14048f1d3
0048F45E  F6 C3 04                        test bl, 4
0048F461  0F 84 A7 01 00 00               je 0x14048f60e
0048F467  41 83 FC 02                     cmp r12d, 2
0048F46B  0F 84 28 02 00 00               je 0x14048f699
0048F471  48 8D 47 38                     lea rax, [rdi + 0x38]
0048F475  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
0048F479  48 39 02                        cmp qword ptr [rdx], rax
0048F47C  74 33                           je 0x14048f4b1
0048F47E  B9 03 00 00 00                  mov ecx, 3
0048F483  CD 29                           int 0x29
0048F485  83 CB 01                        or ebx, 1
0048F488  4C 8D 7F 48                     lea r15, [rdi + 0x48]
0048F48C  4D 39 3F                        cmp qword ptr [r15], r15
0048F48F  0F 85 60 FD FF FF               jne 0x14048f1f5
0048F495  E9 42 FD FF FF                  jmp 0x14048f1dc
0048F49A  0F BA E0 11                     bt eax, 0x11
0048F49E  0F 82 E8 01 00 00               jb 0x14048f68c
0048F4A4  49 8B CE                        mov rcx, r14
0048F4A7  E8 90 7D EC FF                  call 0x14035723c
0048F4AC  E9 DC FC FF FF                  jmp 0x14048f18d
0048F4B1  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
0048F4B6  49 89 00                        mov qword ptr [r8], rax
0048F4B9  49 89 50 08                     mov qword ptr [r8 + 8], rdx
0048F4BD  4C 89 02                        mov qword ptr [rdx], r8
0048F4C0  4C 89 40 08                     mov qword ptr [rax + 8], r8
0048F4C4  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
0048F4C7  FF C8                           dec eax
0048F4C9  89 47 30                        mov dword ptr [rdi + 0x30], eax
0048F4CC  40 38 B7 E0 00 00 00            cmp byte ptr [rdi + 0xe0], sil
0048F4D3  0F 85 FC 01 00 00               jne 0x14048f6d5
0048F4D9  48 8D 8C 24 88 00 00 00         lea rcx, [rsp + 0x88]
0048F4E1  E8 FA 37 EB FF                  call 0x140342ce0
0048F4E6  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
0048F4F0  4C 8B 00                        mov r8, qword ptr [rax]
0048F4F3  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
0048F4F8  48 85 DB                        test rbx, rbx
0048F4FB  74 20                           je 0x14048f51d
0048F4FD  41 83 FC 02                     cmp r12d, 2
0048F501  74 1A                           je 0x14048f51d
0048F503  8B 47 30                        mov eax, dword ptr [rdi + 0x30]
0048F506  83 F8 01                        cmp eax, 1
0048F509  77 12                           ja 0x14048f51d
0048F50B  48 8B 93 E0 03 00 00            mov rdx, qword ptr [rbx + 0x3e0]
0048F512  8B 83 10 04 00 00               mov eax, dword ptr [rbx + 0x410]
0048F518  48 3B D0                        cmp rdx, rax
0048F51B  73 30                           jae 0x14048f54d
0048F51D  48 8B 05 EC 75 B3 00            mov rax, qword ptr [rip + 0xb375ec]
0048F524  0F BA E0 11                     bt eax, 0x11
0048F528  0F 82 E5 01 00 00               jb 0x14048f713
0048F52E  48 8B D3                        mov rdx, rbx
0048F531  49 8B CD                        mov rcx, r13
0048F534  E8 13 C4 EF FF                  call 0x14038b94c
0048F539  48 81 C4 D0 00 00 00            add rsp, 0xd0
0048F540  41 5F                           pop r15
0048F542  41 5E                           pop r14
0048F544  41 5D                           pop r13
0048F546  41 5C                           pop r12
0048F548  5F                              pop rdi
0048F549  5E                              pop rsi
0048F54A  5B                              pop rbx
0048F54B  C3                              ret
0048F54C  CC                              int3
0048F54D  48 8B 83 40 06 00 00            mov rax, qword ptr [rbx + 0x640]
0048F554  48 05 40 4B 4C 00               add rax, 0x4c4b40
0048F55A  4C 3B C0                        cmp r8, rax
0048F55D  7C BE                           jl 0x14048f51d
0048F55F  49 8D 8D 00 03 00 00            lea rcx, [r13 + 0x300]
0048F566  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
0048F56E  E8 2D 62 DE FF                  call 0x1402757a0
0048F573  BA 20 00 00 00                  mov edx, 0x20
0048F578  48 8B CB                        mov rcx, rbx
0048F57B  E8 B4 CB F3 FF                  call 0x1403cc134
0048F580  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
0048F588  E8 53 37 EB FF                  call 0x140342ce0
0048F58D  EB 8E                           jmp 0x14048f51d
0048F58F  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0048F594  45 33 C9                        xor r9d, r9d
0048F597  BA E9 19 00 00                  mov edx, 0x19e9
0048F59C  41 8D 49 34                     lea ecx, [r9 + 0x34]
0048F5A0  49 C7 C0 20 04 00 C0            mov r8, 0xffffffffc0000420
0048F5A7  E8 B4 E0 06 00                  call 0x1404fd660
0048F5AC  CC                              int3
0048F5AD  40 88 B7 C4 00 00 00            mov byte ptr [rdi + 0xc4], sil
0048F5B4  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
0048F5B9  44 8B 8F B8 00 00 00            mov r9d, dword ptr [rdi + 0xb8]
0048F5C0  44 8B 87 B4 00 00 00            mov r8d, dword ptr [rdi + 0xb4]
0048F5C7  48 8B D7                        mov rdx, rdi
0048F5CA  49 8B CD                        mov rcx, r13
0048F5CD  E8 DE C8 0E 00                  call 0x14057beb0
0048F5D2  E9 E3 FB FF FF                  jmp 0x14048f1ba
0048F5D7  41 83 BE 80 00 00 00 02         cmp dword ptr [r14 + 0x80], 2
0048F5DF  0F 85 99 77 26 00               jne 0x1406f6d7e
0048F5E5  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
0048F5E9  4C 89 B0 F8 01 00 00            mov qword ptr [rax + 0x1f8], r14
0048F5F0  E9 89 77 26 00                  jmp 0x1406f6d7e
0048F5F5  40 38 B7 E1 00 00 00            cmp byte ptr [rdi + 0xe1], sil
0048F5FC  0F 84 52 FE FF FF               je 0x14048f454
0048F602  40 88 B7 E1 00 00 00            mov byte ptr [rdi + 0xe1], sil
0048F609  E9 59 FE FF FF                  jmp 0x14048f467
0048F60E  83 CB 04                        or ebx, 4
0048F611  4C 8D 7F 68                     lea r15, [rdi + 0x68]
0048F615  4D 39 3F                        cmp qword ptr [r15], r15
0048F618  0F 84 49 FE FF FF               je 0x14048f467
0048F61E  E9 D2 FB FF FF                  jmp 0x14048f1f5
0048F623  48 89 9F D0 00 00 00            mov qword ptr [rdi + 0xd0], rbx
0048F62A  E9 29 FC FF FF                  jmp 0x14048f258
0048F62F  48 8D 47 78                     lea rax, [rdi + 0x78]
0048F633  4C 3B F8                        cmp r15, rax
0048F636  48 8D 87 C0 00 00 00            lea rax, [rdi + 0xc0]
0048F63D  0F 85 40 FC FF FF               jne 0x14048f283
0048F643  E9 34 FC FF FF                  jmp 0x14048f27c
0048F648  84 DB                           test bl, bl
0048F64A  0F 84 54 FC FF FF               je 0x14048f2a4
0048F650  41 B8 02 00 00 00               mov r8d, 2
0048F656  48 8B D7                        mov rdx, rdi
0048F659  49 8B CD                        mov rcx, r13
0048F65C  E8 1B 7D 04 00                  call 0x1404d737c
0048F661  E9 3E FC FF FF                  jmp 0x14048f2a4
0048F666  49 8B CE                        mov rcx, r14
0048F669  E8 0E 91 EC FF                  call 0x14035877c
0048F66E  E9 42 FC FF FF                  jmp 0x14048f2b5
0048F673  48 8D 47 78                     lea rax, [rdi + 0x78]
0048F677  4C 3B F8                        cmp r15, rax
0048F67A  48 8D 87 C0 00 00 00            lea rax, [rdi + 0xc0]
0048F681  0F 85 79 FD FF FF               jne 0x14048f400
0048F687  E9 6D FD FF FF                  jmp 0x14048f3f9
0048F68C  49 8B CE                        mov rcx, r14
0048F68F  E8 7C 90 EC FF                  call 0x140358710
0048F694  E9 0B FE FF FF                  jmp 0x14048f4a4
0048F699  48 8D 87 88 00 00 00            lea rax, [rdi + 0x88]
0048F6A0  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
0048F6A4  48 39 01                        cmp qword ptr [rcx], rax
0048F6A7  0F 85 D1 FD FF FF               jne 0x14048f47e
0048F6AD  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
0048F6B2  49 89 04 24                     mov qword ptr [r12], rax
0048F6B6  49 89 4C 24 08                  mov qword ptr [r12 + 8], rcx
0048F6BB  4C 89 21                        mov qword ptr [rcx], r12
0048F6BE  4C 89 60 08                     mov qword ptr [rax + 8], r12
0048F6C2  FF 8F 98 00 00 00               dec dword ptr [rdi + 0x98]
0048F6C8  44 8B A4 24 28 01 00 00         mov r12d, dword ptr [rsp + 0x128]
0048F6D0  E9 F7 FD FF FF                  jmp 0x14048f4cc
0048F6D5  39 B7 98 00 00 00               cmp dword ptr [rdi + 0x98], esi
0048F6DB  0F 85 F8 FD FF FF               jne 0x14048f4d9
0048F6E1  83 7F 30 01                     cmp dword ptr [rdi + 0x30], 1
0048F6E5  0F 87 EE FD FF FF               ja 0x14048f4d9
0048F6EB  40 88 B7 E0 00 00 00            mov byte ptr [rdi + 0xe0], sil
0048F6F2  45 8B 85 60 03 00 00            mov r8d, dword ptr [r13 + 0x360]
0048F6F9  41 FF C0                        inc r8d
0048F6FC  49 C1 E0 03                     shl r8, 3
0048F700  33 D2                           xor edx, edx
0048F702  49 8B 8D 70 04 00 00            mov rcx, qword ptr [r13 + 0x470]
0048F709  E8 32 75 23 00                  call 0x1406c6c40
0048F70E  E9 C6 FD FF FF                  jmp 0x14048f4d9
0048F713  41 83 FC 02                     cmp r12d, 2
0048F717  0F 85 11 FE FF FF               jne 0x14048f52e
0048F71D  45 8D 44 24 01                  lea r8d, [r12 + 1]
0048F722  48 8B D7                        mov rdx, rdi
0048F725  49 8B CD                        mov rcx, r13
0048F728  E8 4F 7C 04 00                  call 0x1404d737c
0048F72D  E9 FC FD FF FF                  jmp 0x14048f52e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcWorkerThread(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int8 v_stack_mD8;
    unsigned __int8 v_stack_p10;
    unsigned int v_stack_p128;
    unsigned __int8 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pA0;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (208);
    v_rsi = 0;
    v_stack_mD8 = 0;
    v_stack_mC8 = 0;
    v_stack_mA8 = a1;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 128) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 112) = 0;
    *(unsigned __int64 *)(v_rsp - 104) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 88) = 0;
    v_stack_mC0 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)) - 1)) > 1) goto loc_0048F58F;
    v_stack_m98 = *(unsigned __int64 *)(a1 + 56);
    v_stack_m90 = *(unsigned __int64 *)(a1 + 72);
    v_stack_mD0 = *(unsigned __int64 *)(a1 + 64);
    v_stack_m88 = *(unsigned __int64 *)(a1 + 64);
loc_0048F18D:
    v_stack_mD4 = 0;
    v_stack_p10 = 0;
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(a1 + 56) + 832, v_stack_m80, a3, a4);
    if (v_stack_mD8 != 0) goto loc_0048F5AD;
loc_0048F1BA:
    if (v_stack_mC0 == 0x8A5EULL) goto loc_0048F5D7;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) == 2) goto loc_0048F5F5;
loc_0048F1D3:
    if (((0) & (1)) == 0) goto loc_0048F485;
loc_0048F1DC:
    if (((0) & (2)) != 0) goto loc_0048F45E;
    v_rbx = (unsigned int)((0) | (2));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 88)) == (*(unsigned __int64 *)(a1 + 72) + 88)) goto loc_0048F45E;
loc_0048F1F5:
    v_stack_mB0 = *(unsigned __int64 *)(a1 + 72) + 88;
    result = CcShouldWorkOnThisQueue(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 72), *(unsigned __int64 *)(a1 + 72) + 88, v_stack_p18);
    if ((unsigned __int8)(result) == 0) goto loc_0048F454;
    result = CcFindNextWorkQueueEntry(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 72), *(unsigned __int64 *)(a1 + 72) + 88, v_stack_p18);
    v_stack_mA0 = result;
    if (result == 0) goto loc_0048F454;
    if ((*(unsigned __int64 *)(a1 + 72) + 88) == (*(unsigned __int64 *)(a1 + 72) + 104)) goto loc_0048F623;
loc_0048F258:
    result = CcIsWriteBehindThreadpoolAtLowPriority(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 72), *(unsigned __int64 *)(a1 + 72) + 88, v_stack_p18);
    if ((unsigned __int8)(result) == 0) goto loc_0048F439;
loc_0048F268:
    if ((*(unsigned __int64 *)(a1 + 72) + 88) != (*(unsigned __int64 *)(a1 + 72) + 104)) goto loc_0048F62F;
loc_0048F27C:
loc_0048F283:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, *(unsigned __int64 *)(a1 + 72), *(unsigned __int64 *)(a1 + 72) + 88, v_stack_p18);
    if ((*(unsigned __int64 *)(a1 + 72) + 88) < (*(unsigned __int64 *)(a1 + 72) + 104)) goto loc_0048F648;
loc_0048F2A4:
    if ((*(unsigned __int64 *)(a1 + 72) + 88) < (*(unsigned __int64 *)(a1 + 72) + 104)) goto loc_0048F666;
loc_0048F2B5:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 128))) - (1));
    if (condition_is_equal) goto loc_0048F38A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0048F2F4;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_0048F355;
    if (((unsigned int)(a1)) != 1) goto loc_0048F3A0;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(unsigned __int64 *)(result + 16), a2, a3, v_stack_p18);
    v_stack_mD8 = 1;
    goto loc_0048F3A0;
loc_0048F2F4:
    v_stack_m50 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444))) | (2));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444) = (unsigned int)(result);
loc_0048F318:
    v_stack_mC0 = result;
    result = CcWriteBehind(*(unsigned __int64 *)(result + 16), v_stack_mC8, *(unsigned __int64 *)(a1 + 72), v_stack_p18);
    if (((unsigned int)((unsigned int)(v_stack_mD4))) < 10) goto loc_0048F377;
loc_0048F333:
    v_stack_m48 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444))) & (0xFFFFFFFDULL));
    *(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1444) = (unsigned int)(result);
    goto loc_0048F3A0;
loc_0048F355:
    if (*(unsigned __int64 *)(v_stack_p8 + 64) == 0) goto loc_0048F398;
    result = CcLazyWriteScanVolume(*(unsigned __int64 *)(v_stack_p8 + 64), *(unsigned __int64 *)(a1 + 72), result, (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_0048F3A0;
loc_0048F377:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_mD4)) + 1);
    v_stack_mD4 = (unsigned int)(v_rbx);
    if (v_stack_mC0 != 0x8A5EULL) goto loc_0048F333;
    goto loc_0048F318;
loc_0048F38A:
    result = CcPerformReadAhead(result, *(unsigned __int64 *)(result + 16), result, (unsigned int)(*(unsigned int *)(result + 16)));
    goto loc_0048F3A0;
loc_0048F398:
    result = CcLazyWriteScan(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(result + 16), result, (unsigned int)(*(unsigned int *)(result + 16)));
loc_0048F3A0:
    goto loc_0048F3EC;
loc_0048F3EC:
    if ((*(unsigned __int64 *)(a1 + 72) + 88) != (*(unsigned __int64 *)(a1 + 72) + 104)) goto loc_0048F673;
loc_0048F3F9:
loc_0048F400:
    if (v_stack_mC0 != 0x8A5EULL) goto loc_0048F49A;
    if (v_stack_mC0 >= 0x8A5EULL) goto loc_0048F18D;
    a4 = 0;
    result = CcPerfLogWorkItemEnqueue(*(unsigned __int64 *)(a1 + 72) + 88, result, 1, a4);
    goto loc_0048F18D;
loc_0048F439:
    a1 = ((unsigned int)(*(unsigned int *)(v_rip + 10315557))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 208));
    if (v_rbx < a1) goto loc_0048F268;
loc_0048F454:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) != 2) goto loc_0048F1D3;
loc_0048F45E:
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_0048F60E;
loc_0048F467:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) == 2) goto loc_0048F699;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 56 + 8))) == (*(unsigned __int64 *)(a1 + 72) + 56)) goto loc_0048F4B1;
loc_0048F47E:
loc_0048F485:
    v_rbx = (unsigned int)((v_rbx) | (1));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 72)) != (*(unsigned __int64 *)(a1 + 72) + 72)) goto loc_0048F1F5;
    goto loc_0048F1DC;
loc_0048F49A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 72)) < (*(unsigned __int64 *)(a1 + 72) + 72)) goto loc_0048F68C;
loc_0048F4A4:
    result = CcFreeWorkQueueEntry(result, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 56 + 8), 1, a4);
    goto loc_0048F18D;
loc_0048F4B1:
    *(unsigned __int64 *)(v_stack_mA8) = result;
    *(unsigned __int64 *)(v_stack_mA8 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 56 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 56 + 8)) = v_stack_mA8;
    *(unsigned __int64 *)(result + 8) = v_stack_mA8;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48))) - 1);
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48) = (unsigned int)(result);
loc_0048F4CC:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 224)) != 0) goto loc_0048F6D5;
loc_0048F4D9:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 56 + 8), v_stack_mA8, a4);
    if (v_stack_mD0 == 0) goto loc_0048F51D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)))) == 2) goto loc_0048F51D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48)))) > 1) goto loc_0048F51D;
    if ((*(unsigned __int64 *)(v_stack_mD0 + 992)) >= ((unsigned int)(*(unsigned int *)(v_stack_mD0 + 1040)))) goto loc_0048F54D;
loc_0048F51D:
    if ((*(unsigned __int64 *)(v_stack_mD0 + 992)) < ((unsigned int)(*(unsigned int *)(v_stack_mD0 + 1040)))) goto loc_0048F713;
loc_0048F52E:
    result = CcDereferencePartitionAndPrivateVolumeCacheMap(*(unsigned __int64 *)(a1 + 56), v_stack_mD0, *(unsigned __int64 *)(result), a4);
    v_rsp = (v_rsp) + (208);
    return result;
loc_0048F54D:
    result = (*(unsigned __int64 *)(v_stack_mD0 + 1600)) + (0x4C4B40ULL);
    if ((*(unsigned __int64 *)(result)) < result) goto loc_0048F51D;
    result = KeAcquireInStackQueuedSpinLock(*(unsigned __int64 *)(a1 + 56) + 768, v_stack_pA0, *(unsigned __int64 *)(result), a4);
    result = CcNotifyWriteBehindVolume(v_stack_mD0, 32, *(unsigned __int64 *)(result), a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_pA0, 32, *(unsigned __int64 *)(result), a4);
    goto loc_0048F51D;
loc_0048F58F:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, (unsigned int)(0x19E9ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_0048F5AD:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 196) = 0;
    v_stack_p30 = 0;
    result = CcReEngageWorkerThreads(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 72), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 180)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 184)));
    goto loc_0048F1BA;
loc_0048F5D7:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 504) = result;
loc_0048F5F5:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 225)) == 0) goto loc_0048F454;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 225) = 0;
    goto loc_0048F467;
loc_0048F60E:
    v_rbx = (unsigned int)((v_stack_mD0) | (4));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 104)) == (*(unsigned __int64 *)(a1 + 72) + 104)) goto loc_0048F467;
    goto loc_0048F1F5;
loc_0048F623:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 208) = v_rbx;
    goto loc_0048F258;
loc_0048F62F:
    if ((*(unsigned __int64 *)(a1 + 72) + 104) != (*(unsigned __int64 *)(a1 + 72) + 120)) goto loc_0048F283;
    goto loc_0048F27C;
loc_0048F648:
    if ((unsigned __int8)(v_rbx) == 0) goto loc_0048F2A4;
    result = CcLogExtraWBThreadAction(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 72), 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 184)));
    goto loc_0048F2A4;
loc_0048F666:
    result = CcPerfLogWorkItemDequeue(result, *(unsigned __int64 *)(a1 + 72), 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 184)));
    goto loc_0048F2B5;
loc_0048F673:
    if ((*(unsigned __int64 *)(a1 + 72) + 104) != (*(unsigned __int64 *)(a1 + 72) + 120)) goto loc_0048F400;
    goto loc_0048F3F9;
loc_0048F68C:
    result = CcPerfLogWorkItemComplete(result, *(unsigned __int64 *)(a1 + 72), 2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 184)));
    goto loc_0048F4A4;
loc_0048F699:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 136 + 8))) != (*(unsigned __int64 *)(a1 + 72) + 136)) goto loc_0048F47E;
    *(unsigned __int64 *)(v_stack_p60) = *(unsigned __int64 *)(a1 + 72) + 136;
    *(unsigned __int64 *)(v_stack_p60 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 136 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 136 + 8)) = v_stack_p60;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 72) + 136 + 8) = v_stack_p60;
    goto loc_0048F4CC;
loc_0048F6D5:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 152)) != 0) goto loc_0048F4D9;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 48)) > 1) goto loc_0048F4D9;
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 72) + 224) = 0;
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 56) + 864))) + 1);
    a3 = (a3) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 56) + 1136), a2, a3, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 184)));
    goto loc_0048F4D9;
loc_0048F713:
    if (((unsigned int)((unsigned int)(v_stack_p128))) != 2) goto loc_0048F52E;
    result = CcLogExtraWBThreadAction(*(unsigned __int64 *)(a1 + 56), *(unsigned __int64 *)(a1 + 72), (unsigned int)(v_stack_p128) + 1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72) + 184)));
    goto loc_0048F52E;
}
```

## 5. (Beta) C Style

```c
int64_t CcWorkerThread(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint8_t v_stack_mD8;
    uint8_t v_stack_p10;
    uint32_t v_stack_p128;
    uint8_t v_stack_p18;
    uint32_t v_stack_p20;
    uint8_t v_stack_p30;
    uint64_t v_stack_p60;
    uint64_t v_stack_p8;
    uint64_t v_stack_pA0;

    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (208);
    local_rsi = 0;
    v_stack_mD8 = 0;
    v_stack_mC8 = 0;
    v_stack_mA8 = Arg1;
    result = 0;
    *(uint64_t *)(local_rsp - 0x80) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x70) = 0;
    *(uint64_t *)(local_rsp - 0x68) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x58) = 0;
    v_stack_mC0 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)) - 1)) > 1) goto loc_0048F58F;
    v_stack_m98 = *(uint64_t *)(arg1 + 0x38);
    v_stack_m90 = *(uint64_t *)(arg1 + 0x48);
    v_stack_mD0 = *(uint64_t *)(arg1 + 0x40);
    v_stack_m88 = *(uint64_t *)(arg1 + 0x40);
loc_0048F18D:
    v_stack_mD4 = 0;
    v_stack_p10 = 0;
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(arg1 + 0x38) + 832, v_stack_m80, a3, a4);
    if (v_stack_mD8 != 0) goto loc_0048F5AD;
loc_0048F1BA:
    if (v_stack_mC0 == 0x8A5EULL) goto loc_0048F5D7;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) == 2) goto loc_0048F5F5;
loc_0048F1D3:
    if (((0) & (1)) == 0) goto loc_0048F485;
loc_0048F1DC:
    if (((0) & (2)) != 0) goto loc_0048F45E;
    local_rbx = (uint32_t)((0) | (2));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x58)) == (*(uint64_t *)(arg1 + 0x48) + 88)) goto loc_0048F45E;
loc_0048F1F5:
    v_stack_mB0 = *(uint64_t *)(arg1 + 0x48) + 88;
    result = CcShouldWorkOnThisQueue(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x48), *(uint64_t *)(arg1 + 0x48) + 88, v_stack_p18);
    if ((uint8_t)(result) == 0) goto loc_0048F454;
    result = CcFindNextWorkQueueEntry(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x48), *(uint64_t *)(arg1 + 0x48) + 88, v_stack_p18);
    v_stack_mA0 = result;
    if (result == 0) goto loc_0048F454;
    if ((*(uint64_t *)(arg1 + 0x48) + 88) == (*(uint64_t *)(arg1 + 0x48) + 104)) goto loc_0048F623;
loc_0048F258:
    result = CcIsWriteBehindThreadpoolAtLowPriority(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x48), *(uint64_t *)(arg1 + 0x48) + 88, v_stack_p18);
    if ((uint8_t)(result) == 0) goto loc_0048F439;
loc_0048F268:
    if ((*(uint64_t *)(arg1 + 0x48) + 88) != (*(uint64_t *)(arg1 + 0x48) + 104)) goto loc_0048F62F;
loc_0048F27C:
loc_0048F283:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, *(uint64_t *)(arg1 + 0x48), *(uint64_t *)(arg1 + 0x48) + 88, v_stack_p18);
    if ((*(uint64_t *)(arg1 + 0x48) + 88) < (*(uint64_t *)(arg1 + 0x48) + 104)) goto loc_0048F648;
loc_0048F2A4:
    if ((*(uint64_t *)(arg1 + 0x48) + 88) < (*(uint64_t *)(arg1 + 0x48) + 104)) goto loc_0048F666;
loc_0048F2B5:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x80))) - (1));
    if (condition_is_equal) goto loc_0048F38A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0048F2F4;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_0048F355;
    if (((uint32_t)(Arg1)) != 1) goto loc_0048F3A0;
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(*(uint64_t *)(result + 0x10), a2, a3, v_stack_p18);
    v_stack_mD8 = 1;
    goto loc_0048F3A0;
loc_0048F2F4:
    v_stack_m50 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4))) | (2));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4) = (uint32_t)(result);
loc_0048F318:
    v_stack_mC0 = result;
    result = CcWriteBehind(*(uint64_t *)(result + 0x10), v_stack_mC8, *(uint64_t *)(arg1 + 0x48), v_stack_p18);
    if (((uint32_t)((uint32_t)(v_stack_mD4))) < 10) goto loc_0048F377;
loc_0048F333:
    v_stack_m48 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4))) & (0xFFFFFFFDULL));
    *(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A4) = (uint32_t)(result);
    goto loc_0048F3A0;
loc_0048F355:
    if (*(uint64_t *)(v_stack_p8 + 0x40) == 0) goto loc_0048F398;
    result = CcLazyWriteScanVolume(*(uint64_t *)(v_stack_p8 + 0x40), *(uint64_t *)(arg1 + 0x48), result, (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_0048F3A0;
loc_0048F377:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_mD4)) + 1);
    v_stack_mD4 = (uint32_t)(local_rbx);
    if (v_stack_mC0 != 0x8A5EULL) goto loc_0048F333;
    goto loc_0048F318;
loc_0048F38A:
    result = CcPerformReadAhead(result, *(uint64_t *)(result + 0x10), result, (uint32_t)(*(uint32_t *)(result + 0x10)));
    goto loc_0048F3A0;
loc_0048F398:
    result = CcLazyWriteScan(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(result + 0x10), result, (uint32_t)(*(uint32_t *)(result + 0x10)));
loc_0048F3A0:
    goto loc_0048F3EC;
loc_0048F3EC:
    if ((*(uint64_t *)(arg1 + 0x48) + 88) != (*(uint64_t *)(arg1 + 0x48) + 104)) goto loc_0048F673;
loc_0048F3F9:
loc_0048F400:
    if (v_stack_mC0 != 0x8A5EULL) goto loc_0048F49A;
    if (v_stack_mC0 >= 0x8A5EULL) goto loc_0048F18D;
    a4 = 0;
    result = CcPerfLogWorkItemEnqueue(*(uint64_t *)(arg1 + 0x48) + 88, result, 1, a4);
    goto loc_0048F18D;
loc_0048F439:
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip + 0x9D6725))) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0xD0));
    if (local_rbx < Arg1) goto loc_0048F268;
loc_0048F454:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) != 2) goto loc_0048F1D3;
loc_0048F45E:
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_0048F60E;
loc_0048F467:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) == 2) goto loc_0048F699;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x38 + 0x8))) == (*(uint64_t *)(arg1 + 0x48) + 56)) goto loc_0048F4B1;
loc_0048F47E:
loc_0048F485:
    local_rbx = (uint32_t)((local_rbx) | (1));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x48)) != (*(uint64_t *)(arg1 + 0x48) + 72)) goto loc_0048F1F5;
    goto loc_0048F1DC;
loc_0048F49A:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x48)) < (*(uint64_t *)(arg1 + 0x48) + 72)) goto loc_0048F68C;
loc_0048F4A4:
    result = CcFreeWorkQueueEntry(result, *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x38 + 0x8), 1, a4);
    goto loc_0048F18D;
loc_0048F4B1:
    *(uint64_t *)(v_stack_mA8) = result;
    *(uint64_t *)(v_stack_mA8 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x38 + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x38 + 0x8)) = v_stack_mA8;
    *(uint64_t *)(result + 0x8) = v_stack_mA8;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30))) - 1);
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30) = (uint32_t)(result);
loc_0048F4CC:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0xE0)) != 0) goto loc_0048F6D5;
loc_0048F4D9:
    result = KeReleaseInStackQueuedSpinLock(v_stack_m80, *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x38 + 0x8), v_stack_mA8, a4);
    if (v_stack_mD0 == 0) goto loc_0048F51D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)))) == 2) goto loc_0048F51D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30)))) > 1) goto loc_0048F51D;
    if ((*(uint64_t *)(v_stack_mD0 + 0x3E0)) >= ((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x410)))) goto loc_0048F54D;
loc_0048F51D:
    if ((*(uint64_t *)(v_stack_mD0 + 0x3E0)) < ((uint32_t)(*(uint32_t *)(v_stack_mD0 + 0x410)))) goto loc_0048F713;
loc_0048F52E:
    result = CcDereferencePartitionAndPrivateVolumeCacheMap(*(uint64_t *)(arg1 + 0x38), v_stack_mD0, *(uint64_t *)(result), a4);
    local_rsp = (local_rsp) + (208);
    return result;
loc_0048F54D:
    result = (*(uint64_t *)(v_stack_mD0 + 0x640)) + (0x4C4B40ULL);
    if ((*(uint64_t *)(result)) < result) goto loc_0048F51D;
    result = KeAcquireInStackQueuedSpinLock(*(uint64_t *)(arg1 + 0x38) + 768, v_stack_pA0, *(uint64_t *)(result), a4);
    result = CcNotifyWriteBehindVolume(v_stack_mD0, 32, *(uint64_t *)(result), a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_pA0, 32, *(uint64_t *)(result), a4);
    goto loc_0048F51D;
loc_0048F58F:
    v_stack_p20 = 0;
    a4 = 0;
    result = KeBugCheckEx(a4 + 52, (uint32_t)(0x19E9ULL), 0xFFFFFFFFC0000420ULL, a4);
loc_0048F5AD:
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0xC4) = 0;
    v_stack_p30 = 0;
    result = CcReEngageWorkerThreads(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x48), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0xB4)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0xB8)));
    goto loc_0048F1BA;
loc_0048F5D7:
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x1F8) = result;
loc_0048F5F5:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0xE1)) == 0) goto loc_0048F454;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0xE1) = 0;
    goto loc_0048F467;
loc_0048F60E:
    local_rbx = (uint32_t)((v_stack_mD0) | (4));
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x68)) == (*(uint64_t *)(arg1 + 0x48) + 104)) goto loc_0048F467;
    goto loc_0048F1F5;
loc_0048F623:
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0xD0) = local_rbx;
    goto loc_0048F258;
loc_0048F62F:
    if ((*(uint64_t *)(arg1 + 0x48) + 104) != (*(uint64_t *)(arg1 + 0x48) + 120)) goto loc_0048F283;
    goto loc_0048F27C;
loc_0048F648:
    if ((uint8_t)(local_rbx) == 0) goto loc_0048F2A4;
    result = CcLogExtraWBThreadAction(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x48), 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0xB8)));
    goto loc_0048F2A4;
loc_0048F666:
    result = CcPerfLogWorkItemDequeue(result, *(uint64_t *)(arg1 + 0x48), 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0xB8)));
    goto loc_0048F2B5;
loc_0048F673:
    if ((*(uint64_t *)(arg1 + 0x48) + 104) != (*(uint64_t *)(arg1 + 0x48) + 120)) goto loc_0048F400;
    goto loc_0048F3F9;
loc_0048F68C:
    result = CcPerfLogWorkItemComplete(result, *(uint64_t *)(arg1 + 0x48), 2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0xB8)));
    goto loc_0048F4A4;
loc_0048F699:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x88 + 0x8))) != (*(uint64_t *)(arg1 + 0x48) + 136)) goto loc_0048F47E;
    *(uint64_t *)(v_stack_p60) = *(uint64_t *)(arg1 + 0x48) + 136;
    *(uint64_t *)(v_stack_p60 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x88 + 0x8);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x88 + 0x8)) = v_stack_p60;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x48) + 0x88 + 0x8) = v_stack_p60;
    goto loc_0048F4CC;
loc_0048F6D5:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x98)) != 0) goto loc_0048F4D9;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0x30)) > 1) goto loc_0048F4D9;
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x48) + 0xE0) = 0;
    a3 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x38) + 0x360))) + 1);
    a3 = (a3) << (3);
    a2 = 0;
    result = memset(*(uint64_t *)(*(uint64_t *)(arg1 + 0x38) + 0x470), a2, a3, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0xB8)));
    goto loc_0048F4D9;
loc_0048F713:
    if (((uint32_t)((uint32_t)(v_stack_p128))) != 2) goto loc_0048F52E;
    result = CcLogExtraWBThreadAction(*(uint64_t *)(arg1 + 0x38), *(uint64_t *)(arg1 + 0x48), (uint32_t)(v_stack_p128) + 1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48) + 0xB8)));
    goto loc_0048F52E;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048F0F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
