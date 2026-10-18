# sub_008C28B0

- RVA: `0x008C28B0`–`0x008C2DB8` (길이 `1,288` bytes)
- VA: `0x00000001408C28B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008372C`
- 디코드: `304`개 명령, `1,288/1,288` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **16**; 고유 호출 대상: **14**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x008C28B9` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x008C28F3` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (function, `0x006BA5B0`)
- `0x008C290B` → [EtwpAddGuidEntry](../8B/EtwpAddGuidEntry_function_008BFC80.md) (function, `0x008BFC80`)
- `0x008C2978` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008C29CD` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x008C29FB` → [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) (function, `0x008B97A0`)
- `0x008C2A13` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008C2A63` → [EtwpApplyScopeFilters](EtwpApplyScopeFilters_function_008C3470.md) (function, `0x008C3470`)
- `0x008C2AF8` → [EtwpComputeRegEntryEnableInfo](EtwpComputeRegEntryEnableInfo_function_008C0FE0.md) (function, `0x008C0FE0`)
- `0x008C2BCC` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (function, `0x00411F50`)
- `0x008C2C30` → [EtwpCheckLoggerControlAccess](EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)
- `0x008C2C54` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x008C2C9B` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (function, `0x0025F050`)
- `0x008C2D50` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008C2D95` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x008C2DA5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x008C28B0` → RVA `0x00FD9BD0` (`PAGEDATA`; read)
- `0x008C2982` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x008C29BE` → RVA `0x00FC6D30` (`ALMOSTRO`; read)
- `0x008C2D39` → RVA `0x00B82850` (`ExFreePool`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **10**
  - `0x008C28F3` → [ExpInterlockedPushEntrySList](../../text/6B/ExpInterlockedPushEntrySList_function_006BA5B0.md) (`PAGE` → `.text`)
  - `0x008C2978` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008C29CD` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x008C2A13` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008C2BCC` → [ExAcquireRundownProtectionCacheAwareEx](../../text/41/ExAcquireRundownProtectionCacheAwareEx_function_00411F50.md) (`PAGE` → `.text`)
  - `0x008C2C54` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x008C2C9B` → [ExReleaseRundownProtectionCacheAwareEx](../../text/25/ExReleaseRundownProtectionCacheAwareEx_function_0025F050.md) (`PAGE` → `.text`)
  - `0x008C2D50` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008C2D95` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x008C2DA5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **22**
  - `0x008C28C0` → [sub_008C2328 + 0x318](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C28CB` → [sub_008C2328 + 0x357](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C28FB` → [sub_008C2328 + 0x4D1](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2916` → [sub_008C2328 + 0x108](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2921` → [sub_008C2328 + 0x54B](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C294B` → [sub_008C2328 + 0x21C](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2970` → [sub_008C2328 + 0x4D1](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C297D` → [sub_008C2328 + 0x50B](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C298D` → [sub_008C2DC2 + 0x85](Unknown_function_008C2DC2.md) (`tail-transfer`)
  - `0x008C299A` → [sub_008C2328 + 0x3B6](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2A0A` → [sub_008C2328 + 0x4D1](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2A72` → [sub_008C2DC2 + 0xB9](Unknown_function_008C2DC2.md) (`tail-transfer`)
  - `0x008C2AEC` → [sub_008C2328 + 0x46B](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2C08` → [sub_008C2DC2 + 0xAA](Unknown_function_008C2DC2.md) (`tail-transfer`)
  - `0x008C2CC9` → [sub_008C2328 + 0x427](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2D30` → [sub_008C2328 + 0x3A0](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2D4A` → [sub_008C2DC2 + 0x78](Unknown_function_008C2DC2.md) (`tail-transfer`)
  - `0x008C2D55` → [sub_008C2328 + 0x3A8](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2D8F` → [sub_008C2DC2 + 0x61](Unknown_function_008C2DC2.md) (`tail-transfer`)
  - `0x008C2D9D` → [sub_008C2328 + 0x4D1](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2DAA` → [sub_008C2328 + 0xE9](Unknown_function_008C2328.md) (`tail-transfer`)
  - `0x008C2DB3` → [sub_008C2328 + 0x3D3](Unknown_function_008C2328.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C28B0  48 8B 0D 19 73 71 00            mov rcx, qword ptr [rip + 0x717319]
008C28B7  33 D2                           xor edx, edx
008C28B9  E8 62 F5 FA FF                  call 0x140871e20
008C28BE  84 C0                           test al, al
008C28C0  0F 85 7A FD FF FF               jne 0x1408c2640
008C28C6  BB 61 00 00 C0                  mov ebx, 0xc0000061
008C28CB  E9 AF FD FF FF                  jmp 0x1408c267f
008C28D0  65 48 8B 14 25 20 00 00 00      mov rdx, qword ptr gs:[0x20]
008C28D9  48 8B 8A 40 08 00 00            mov rcx, qword ptr [rdx + 0x840]
008C28E0  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008C28E3  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008C28E7  66 39 01                        cmp word ptr [rcx], ax
008C28EA  0F 83 71 04 00 00               jae 0x1408c2d61
008C28F0  48 8B D6                        mov rdx, rsi
008C28F3  E8 B8 7C DF FF                  call 0x1406ba5b0
008C28F8  45 33 F6                        xor r14d, r14d
008C28FB  E9 F9 FE FF FF                  jmp 0x1408c27f9
008C2900  44 8B 44 24 78                  mov r8d, dword ptr [rsp + 0x78]
008C2905  48 8B D7                        mov rdx, rdi
008C2908  49 8B CC                        mov rcx, r12
008C290B  E8 70 D3 FF FF                  call 0x1408bfc80
008C2910  4C 8B F8                        mov r15, rax
008C2913  48 85 C0                        test rax, rax
008C2916  0F 85 14 FB FF FF               jne 0x1408c2430
008C291C  BB 17 00 00 C0                  mov ebx, 0xc0000017
008C2921  E9 4D FF FF FF                  jmp 0x1408c2873
008C2926  41 8B D6                        mov edx, r14d
008C2929  49 8D 8F 80 00 00 00            lea rcx, [r15 + 0x80]
008C2930  49 83 C1 58                     add r9, 0x58
008C2934  44 39 29                        cmp dword ptr [rcx], r13d
008C2937  75 17                           jne 0x1408c2950
008C2939  FF C2                           inc edx
008C293B  48 83 C1 20                     add rcx, 0x20
008C293F  49 83 C1 68                     add r9, 0x68
008C2943  83 FA 10                        cmp edx, 0x10
008C2946  72 EC                           jb 0x1408c2934
008C2948  41 8B 02                        mov eax, dword ptr [r10]
008C294B  E9 F4 FB FF FF                  jmp 0x1408c2544
008C2950  49 8B 01                        mov rax, qword ptr [r9]
008C2953  48 85 C0                        test rax, rax
008C2956  74 E1                           je 0x1408c2939
008C2958  80 FA 0F                        cmp dl, 0xf
008C295B  77 DC                           ja 0x1408c2939
008C295D  8B 40 10                        mov eax, dword ptr [rax + 0x10]
008C2960  83 C0 07                        add eax, 7
008C2963  83 E0 F8                        and eax, 0xfffffff8
008C2966  44 03 C0                        add r8d, eax
008C2969  EB CE                           jmp 0x1408c2939
008C296B  BB 23 00 00 C0                  mov ebx, 0xc0000023
008C2970  E9 84 FE FF FF                  jmp 0x1408c27f9
008C2975  48 8B CF                        mov rcx, rdi
008C2978  E8 53 0F 9A FF                  call 0x1402638d0
008C297D  E9 B1 FE FF FF                  jmp 0x1408c2833
008C2982  44 39 2D 87 26 70 00            cmp dword ptr [rip + 0x702687], r13d
008C2989  48 8B 75 90                     mov rsi, qword ptr [rbp - 0x70]
008C298D  0F 85 B4 04 00 00               jne 0x1408c2e47
008C2993  48 83 C6 30                     add rsi, 0x30
008C2997  4C 8B F6                        mov r14, rsi
008C299A  E9 3F FD FF FF                  jmp 0x1408c26de
008C299F  48 89 46 08                     mov qword ptr [rsi + 8], rax
008C29A3  48 89 0E                        mov qword ptr [rsi], rcx
008C29A6  48 89 71 08                     mov qword ptr [rcx + 8], rsi
008C29AA  48 89 30                        mov qword ptr [rax], rsi
008C29AD  48 8D 46 10                     lea rax, [rsi + 0x10]
008C29B1  48 89 40 08                     mov qword ptr [rax + 8], rax
008C29B5  48 89 00                        mov qword ptr [rax], rax
008C29B8  66 F0 41 83 0E 40               lock or word ptr [r14], 0x40
008C29BE  4C 8B 05 6B 43 70 00            mov r8, qword ptr [rip + 0x70436b]
008C29C5  45 33 C9                        xor r9d, r9d
008C29C8  33 D2                           xor edx, edx
008C29CA  48 8B CE                        mov rcx, rsi
008C29CD  E8 2E 63 B7 FF                  call 0x140438d00
008C29D2  48 8D 45 98                     lea rax, [rbp - 0x68]
008C29D6  45 33 F6                        xor r14d, r14d
008C29D9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008C29DE  33 D2                           xor edx, edx
008C29E0  48 8D 45 B8                     lea rax, [rbp - 0x48]
008C29E4  41 B8 04 08 00 00               mov r8d, 0x804
008C29EA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008C29EF  48 8B CE                        mov rcx, rsi
008C29F2  45 8D 4E 01                     lea r9d, [r14 + 1]
008C29F6  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
008C29FB  E8 A0 6D FF FF                  call 0x1408b97a0
008C2A00  8B D8                           mov ebx, eax
008C2A02  4C 8B EE                        mov r13, rsi
008C2A05  4C 8B E6                        mov r12, rsi
008C2A08  85 C0                           test eax, eax
008C2A0A  0F 88 E9 FD FF FF               js 0x1408c27f9
008C2A10  48 8B CE                        mov rcx, rsi
008C2A13  E8 38 69 A3 FF                  call 0x1402f9350
008C2A18  44 38 74 24 50                  cmp byte ptr [rsp + 0x50], r14b
008C2A1D  74 0A                           je 0x1408c2a29
008C2A1F  B8 80 00 00 00                  mov eax, 0x80
008C2A24  66 F0 09 46 62                  lock or word ptr [rsi + 0x62], ax
008C2A29  48 8B 45 98                     mov rax, qword ptr [rbp - 0x68]
008C2A2D  48 89 47 18                     mov qword ptr [rdi + 0x18], rax
008C2A31  45 39 77 60                     cmp dword ptr [r15 + 0x60], r14d
008C2A35  0F 85 F7 00 00 00               jne 0x1408c2b32
008C2A3B  41 0F B7 45 64                  movzx eax, word ptr [r13 + 0x64]
008C2A40  45 33 C9                        xor r9d, r9d
008C2A43  41 0F B6 55 62                  movzx edx, byte ptr [r13 + 0x62]
008C2A48  45 33 C0                        xor r8d, r8d
008C2A4B  66 89 44 24 50                  mov word ptr [rsp + 0x50], ax
008C2A50  49 8B CD                        mov rcx, r13
008C2A53  C0 EA 03                        shr dl, 3
008C2A56  48 8D 44 24 50                  lea rax, [rsp + 0x50]
008C2A5B  80 E2 01                        and dl, 1
008C2A5E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008C2A63  E8 08 0A 00 00                  call 0x1408c3470
008C2A68  49 8B 8F 90 02 00 00            mov rcx, qword ptr [r15 + 0x290]
008C2A6F  48 85 C9                        test rcx, rcx
008C2A72  0F 85 03 04 00 00               jne 0x1408c2e7b
008C2A78  41 F6 45 62 08                  test byte ptr [r13 + 0x62], 8
008C2A7D  0F B7 74 24 50                  movzx esi, word ptr [rsp + 0x50]
008C2A82  0F B7 44 24 54                  movzx eax, word ptr [rsp + 0x54]
008C2A87  0F 85 F0 01 00 00               jne 0x1408c2c7d
008C2A8D  66 41 23 75 64                  and si, word ptr [r13 + 0x64]
008C2A92  66 41 21 45 68                  and word ptr [r13 + 0x68], ax
008C2A97  41 0F B7 45 68                  movzx eax, word ptr [r13 + 0x68]
008C2A9C  66 41 89 75 64                  mov word ptr [r13 + 0x64], si
008C2AA1  66 89 74 24 50                  mov word ptr [rsp + 0x50], si
008C2AA6  66 85 F6                        test si, si
008C2AA9  75 46                           jne 0x1408c2af1
008C2AAB  66 85 C0                        test ax, ax
008C2AAE  75 41                           jne 0x1408c2af1
008C2AB0  0F 57 C0                        xorps xmm0, xmm0
008C2AB3  33 C0                           xor eax, eax
008C2AB5  0F 11 47 70                     movups xmmword ptr [rdi + 0x70], xmm0
008C2AB9  0F 11 87 80 00 00 00            movups xmmword ptr [rdi + 0x80], xmm0
008C2AC0  44 89 B7 98 00 00 00            mov dword ptr [rdi + 0x98], r14d
008C2AC7  4C 8B 75 A0                     mov r14, qword ptr [rbp - 0x60]
008C2ACB  48 89 87 90 00 00 00            mov qword ptr [rdi + 0x90], rax
008C2AD2  33 C0                           xor eax, eax
008C2AD4  8B D0                           mov edx, eax
008C2AD6  41 C7 06 A0 00 00 00            mov dword ptr [r14], 0xa0
008C2ADD  49 39 87 80 02 00 00            cmp qword ptr [r15 + 0x280], rax
008C2AE4  0F 85 BB 01 00 00               jne 0x1408c2ca5
008C2AEA  8B C8                           mov ecx, eax
008C2AEC  E9 A2 FC FF FF                  jmp 0x1408c2793
008C2AF1  48 8D 57 70                     lea rdx, [rdi + 0x70]
008C2AF5  49 8B CD                        mov rcx, r13
008C2AF8  E8 E3 E4 FF FF                  call 0x1408c0fe0
008C2AFD  41 0F B6 47 5B                  movzx eax, byte ptr [r15 + 0x5b]
008C2B02  83 E0 01                        and eax, 1
008C2B05  C6 44 24 63 00                  mov byte ptr [rsp + 0x63], 0
008C2B0A  89 87 98 00 00 00               mov dword ptr [rdi + 0x98], eax
008C2B10  41 0F B7 47 58                  movzx eax, word ptr [r15 + 0x58]
008C2B15  66 89 44 24 60                  mov word ptr [rsp + 0x60], ax
008C2B1A  41 0F B6 47 5A                  movzx eax, byte ptr [r15 + 0x5a]
008C2B1F  88 44 24 62                     mov byte ptr [rsp + 0x62], al
008C2B23  41 8B 47 50                     mov eax, dword ptr [r15 + 0x50]
008C2B27  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
008C2B2B  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008C2B30  EB 95                           jmp 0x1408c2ac7
008C2B32  0F B7 7E 62                     movzx edi, word ptr [rsi + 0x62]
008C2B36  49 8D B7 86 00 00 00            lea rsi, [r15 + 0x86]
008C2B3D  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
008C2B41  66 83 E7 08                     and di, 8
008C2B45  BB 22 00 00 C0                  mov ebx, 0xc0000022
008C2B4A  66 0F 1F 44 00 00               nop word ptr [rax + rax]
008C2B50  83 7E FA 00                     cmp dword ptr [rsi - 6], 0
008C2B54  75 20                           jne 0x1408c2b76
008C2B56  41 FF C6                        inc r14d
008C2B59  48 83 C6 20                     add rsi, 0x20
008C2B5D  41 83 FE 10                     cmp r14d, 0x10
008C2B61  72 ED                           jb 0x1408c2b50
008C2B63  48 8B 7D C0                     mov rdi, qword ptr [rbp - 0x40]
008C2B67  4D 8B EC                        mov r13, r12
008C2B6A  8B 5C 24 68                     mov ebx, dword ptr [rsp + 0x68]
008C2B6E  45 33 F6                        xor r14d, r14d
008C2B71  E9 C5 FE FF FF                  jmp 0x1408c2a3b
008C2B76  44 0F B7 06                     movzx r8d, word ptr [rsi]
008C2B7A  33 C0                           xor eax, eax
008C2B7C  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008C2B80  44 89 44 24 6C                  mov dword ptr [rsp + 0x6c], r8d
008C2B85  66 85 FF                        test di, di
008C2B88  0F 85 7B 01 00 00               jne 0x1408c2d09
008C2B8E  4D 8B AF 88 02 00 00            mov r13, qword ptr [r15 + 0x288]
008C2B95  4C 89 6D 88                     mov qword ptr [rbp - 0x78], r13
008C2B99  45 3B 45 10                     cmp r8d, dword ptr [r13 + 0x10]
008C2B9D  73 B7                           jae 0x1408c2b56
008C2B9F  49 8B 85 C8 02 00 00            mov rax, qword ptr [r13 + 0x2c8]
008C2BA6  4A 8B 14 C0                     mov rdx, qword ptr [rax + r8*8]
008C2BAA  F6 C2 01                        test dl, 1
008C2BAD  75 A7                           jne 0x1408c2b56
008C2BAF  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
008C2BB6  4A 8D 04 C5 00 00 00 00         lea rax, [r8*8]
008C2BBE  BA 01 00 00 00                  mov edx, 1
008C2BC3  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008C2BC8  48 8B 0C 08                     mov rcx, qword ptr [rax + rcx]
008C2BCC  E8 7F F3 B4 FF                  call 0x140411f50
008C2BD1  84 C0                           test al, al
008C2BD3  74 81                           je 0x1408c2b56
008C2BD5  8B 44 24 6C                     mov eax, dword ptr [rsp + 0x6c]
008C2BD9  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
008C2BDE  41 3B 45 10                     cmp eax, dword ptr [r13 + 0x10]
008C2BE2  0F 83 A3 00 00 00               jae 0x1408c2c8b
008C2BE8  0F AE E8                        lfence
008C2BEB  49 8B 85 C8 02 00 00            mov rax, qword ptr [r13 + 0x2c8]
008C2BF2  4D 8B 2C 00                     mov r13, qword ptr [r8 + rax]
008C2BF6  41 F6 C5 01                     test r13b, 1
008C2BFA  0F 85 87 00 00 00               jne 0x1408c2c87
008C2C00  41 83 BD 40 01 00 00 00         cmp dword ptr [r13 + 0x140], 0
008C2C08  0F 84 5E 02 00 00               je 0x1408c2e6c
008C2C0E  4D 85 ED                        test r13, r13
008C2C11  0F 84 3F FF FF FF               je 0x1408c2b56
008C2C17  41 8B 45 0C                     mov eax, dword ptr [r13 + 0xc]
008C2C1B  66 85 FF                        test di, di
008C2C1E  0F 85 D5 00 00 00               jne 0x1408c2cf9
008C2C24  84 C0                           test al, al
008C2C26  79 11                           jns 0x1408c2c39
008C2C28  49 8B D5                        mov rdx, r13
008C2C2B  B9 00 02 00 00                  mov ecx, 0x200
008C2C30  E8 AB DE FF FF                  call 0x1408c0ae0
008C2C35  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008C2C39  49 8B 85 50 05 00 00            mov rax, qword ptr [r13 + 0x550]
008C2C40  BA 01 00 00 00                  mov edx, 1
008C2C45  45 8B 45 00                     mov r8d, dword ptr [r13]
008C2C49  48 8B 88 C0 02 00 00            mov rcx, qword ptr [rax + 0x2c0]
008C2C50  4A 8B 0C C1                     mov rcx, qword ptr [rcx + r8*8]
008C2C54  E8 F7 C3 99 FF                  call 0x14025f050
008C2C59  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
008C2C5E  0F 85 F2 FE FF FF               jne 0x1408c2b56
008C2C64  41 0F B7 4C 24 64               movzx ecx, word ptr [r12 + 0x64]
008C2C6A  41 0F B6 C6                     movzx eax, r14b
008C2C6E  66 0F AB C1                     bts cx, ax
008C2C72  66 41 89 4C 24 64               mov word ptr [r12 + 0x64], cx
008C2C78  E9 D9 FE FF FF                  jmp 0x1408c2b56
008C2C7D  66 41 89 45 68                  mov word ptr [r13 + 0x68], ax
008C2C82  E9 15 FE FF FF                  jmp 0x1408c2a9c
008C2C87  4C 8B 6D 88                     mov r13, qword ptr [rbp - 0x78]
008C2C8B  49 8B 8D C0 02 00 00            mov rcx, qword ptr [r13 + 0x2c0]
008C2C92  BA 01 00 00 00                  mov edx, 1
008C2C97  49 8B 0C 08                     mov rcx, qword ptr [r8 + rcx]
008C2C9B  E8 B0 C3 99 FF                  call 0x14025f050
008C2CA0  E9 B1 FE FF FF                  jmp 0x1408c2b56
008C2CA5  44 8B C8                        mov r9d, eax
008C2CA8  4D 8D 87 80 00 00 00            lea r8, [r15 + 0x80]
008C2CAF  4C 8B D0                        mov r10, rax
008C2CB2  41 83 38 00                     cmp dword ptr [r8], 0
008C2CB6  75 16                           jne 0x1408c2cce
008C2CB8  41 FF C1                        inc r9d
008C2CBB  49 83 C0 20                     add r8, 0x20
008C2CBF  49 83 C2 68                     add r10, 0x68
008C2CC3  41 83 F9 10                     cmp r9d, 0x10
008C2CC7  72 E9                           jb 0x1408c2cb2
008C2CC9  E9 81 FA FF FF                  jmp 0x1408c274f
008C2CCE  49 8B 87 80 02 00 00            mov rax, qword ptr [r15 + 0x280]
008C2CD5  4D 8B 5C 02 58                  mov r11, qword ptr [r10 + rax + 0x58]
008C2CDA  4D 85 DB                        test r11, r11
008C2CDD  74 D9                           je 0x1408c2cb8
008C2CDF  41 0F B6 C9                     movzx ecx, r9b
008C2CE3  0F B7 C6                        movzx eax, si
008C2CE6  0F A3 C8                        bt eax, ecx
008C2CE9  73 CD                           jae 0x1408c2cb8
008C2CEB  41 8B 43 10                     mov eax, dword ptr [r11 + 0x10]
008C2CEF  83 C0 07                        add eax, 7
008C2CF2  83 E0 F8                        and eax, 0xfffffff8
008C2CF5  03 D0                           add edx, eax
008C2CF7  EB BF                           jmp 0x1408c2cb8
008C2CF9  0F BA E0 18                     bt eax, 0x18
008C2CFD  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
008C2D01  0F 42 C3                        cmovb eax, ebx
008C2D04  E9 2C FF FF FF                  jmp 0x1408c2c35
008C2D09  41 0F B7 47 58                  movzx eax, word ptr [r15 + 0x58]
008C2D0E  44 3B C0                        cmp r8d, eax
008C2D11  0F 84 77 FE FF FF               je 0x1408c2b8e
008C2D17  E9 3A FE FF FF                  jmp 0x1408c2b56
008C2D1C  FF 41 20                        inc dword ptr [rcx + 0x20]
008C2D1F  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
008C2D26  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008C2D29  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008C2D2D  66 39 01                        cmp word ptr [rcx], ax
008C2D30  0F 82 92 F9 FF FF               jb 0x1408c26c8
008C2D36  FF 41 20                        inc dword ptr [rcx + 0x20]
008C2D39  48 8D 05 10 FB 2B 00            lea rax, [rip + 0x2bfb10]
008C2D40  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008C2D44  48 8B CE                        mov rcx, rsi
008C2D47  48 3B D0                        cmp rdx, rax
008C2D4A  0F 85 EA 00 00 00               jne 0x1408c2e3a
008C2D50  E8 FB FA 2B 00                  call 0x140b82850
008C2D55  E9 76 F9 FF FF                  jmp 0x1408c26d0
008C2D5A  33 C0                           xor eax, eax
008C2D5C  E9 89 FD FF FF                  jmp 0x1408c2aea
008C2D61  FF 41 20                        inc dword ptr [rcx + 0x20]
008C2D64  48 8B 8A 48 08 00 00            mov rcx, qword ptr [rdx + 0x848]
008C2D6B  FF 41 1C                        inc dword ptr [rcx + 0x1c]
008C2D6E  0F B7 41 10                     movzx eax, word ptr [rcx + 0x10]
008C2D72  66 39 01                        cmp word ptr [rcx], ax
008C2D75  0F 82 75 FB FF FF               jb 0x1408c28f0
008C2D7B  FF 41 20                        inc dword ptr [rcx + 0x20]
008C2D7E  48 8D 05 CB FA 2B 00            lea rax, [rip + 0x2bfacb]
008C2D85  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
008C2D89  48 8B CE                        mov rcx, rsi
008C2D8C  48 3B D0                        cmp rdx, rax
008C2D8F  0F 85 8E 00 00 00               jne 0x1408c2e23
008C2D95  E8 B6 FA 2B 00                  call 0x140b82850
008C2D9A  45 33 F6                        xor r14d, r14d
008C2D9D  E9 57 FA FF FF                  jmp 0x1408c27f9
008C2DA2  49 8B CE                        mov rcx, r14
008C2DA5  E8 96 06 9A FF                  call 0x140263440
008C2DAA  E9 62 F6 FF FF                  jmp 0x1408c2411
008C2DAF  49 83 C6 62                     add r14, 0x62
008C2DB3  E9 43 F9 FF FF                  jmp 0x1408c26fb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008C28B0(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p50;
    unsigned __int16 v_stack_p54;
    unsigned int v_stack_p58;
    unsigned __int16 v_stack_p60;
    unsigned __int8 v_stack_p62;
    unsigned __int8 v_stack_p63;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p78;

    a2 = 0;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 7435033), a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_008C28B0(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p50;
    uint16_t v_stack_p54;
    uint32_t v_stack_p58;
    uint16_t v_stack_p60;
    uint8_t v_stack_p62;
    uint8_t v_stack_p63;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p78;

    Arg2 = 0;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x717319), Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C28B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
