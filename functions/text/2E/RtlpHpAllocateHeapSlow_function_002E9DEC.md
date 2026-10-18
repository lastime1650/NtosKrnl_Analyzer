# RtlpHpAllocateHeapSlow

- RVA: `0x002E9DEC`–`0x002EA61C` (길이 `2,096` bytes)
- VA: `0x00000001402E9DEC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071578`
- 디코드: `554`개 명령, `2,096/2,096` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **25**; 고유 호출 대상: **22**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x002E9E48` → [RtlpCallInterceptRoutine](../47/RtlpCallInterceptRoutine_function_00479594.md) (function, `0x00479594`)
- `0x002E9E7C` → [RtlpHpCalculateAllocSize](../41/RtlpHpCalculateAllocSize_function_00410350.md) (function, `0x00410350`)
- `0x002E9EC1` → [RtlpHpEnvTlsGetValue](RtlpHpEnvTlsGetValue_function_002E9850.md) (function, `0x002E9850`)
- `0x002E9ECE` → [RtlpHpLfhThreadDataInitializeSet](../4F/RtlpHpLfhThreadDataInitializeSet_function_004F6334.md) (function, `0x004F6334`)
- `0x002E9EF6` → [RtlpHpLfhBucketCheckAndUpdate](../4F/RtlpHpLfhBucketCheckAndUpdate_function_004FC894.md) (function, `0x004FC894`)
- `0x002EA063` → [RtlHeapZero](../6B/RtlHeapZero_function_006BBC10.md) (function, `0x006BBC10`)
- `0x002EA254` → [RtlpHpLfhSubsegmentCommitBlock](RtlpHpLfhSubsegmentCommitBlock_function_002EA630.md) (function, `0x002EA630`)
- `0x002EA293` → [RtlpHpLfhSubsegmentPrefetch](RtlpHpLfhSubsegmentPrefetch_function_002EBB18.md) (function, `0x002EBB18`)
- `0x002EA2B4` → [RtlHeapZero](../6B/RtlHeapZero_function_006BBC10.md) (function, `0x006BBC10`)
- `0x002EA32F` → [RtlpHpEnvCompactionIsScheduled](../48/RtlpHpEnvCompactionIsScheduled_function_0048E7E0.md) (function, `0x0048E7E0`)
- `0x002EA33C` → [RtlpHpEnvCompactionSchedule](../32/RtlpHpEnvCompactionSchedule_function_003264A0.md) (function, `0x003264A0`)
- `0x002EA3D8` → [RtlpHpLfhBucketUpdateAffinityMapping](../4D/RtlpHpLfhBucketUpdateAffinityMapping_function_004D0008.md) (function, `0x004D0008`)
- `0x002EA402` → [RtlpHpLfhSlotAllocateSlow](RtlpHpLfhSlotAllocateSlow_function_002E8FBC.md) (function, `0x002E8FBC`)
- `0x002EA42A` → [RtlpHpVsContextAllocate](RtlpHpVsContextAllocate_function_002EA944.md) (function, `0x002EA944`)
- `0x002EA445` → [RtlpHpAllocateHeapBackend](../32/RtlpHpAllocateHeapBackend_function_00326580.md) (function, `0x00326580`)
- `0x002EA44C` → [RtlpHpLargeAlloc](RtlpHpLargeAlloc_function_002EBD5C.md) (function, `0x002EBD5C`)
- `0x002EA48F` → [RtlpHpExtrasAppend](../4D/RtlpHpExtrasAppend_function_004DB1B8.md) (function, `0x004DB1B8`)
- `0x002EA4C7` → [RtlpCallInterceptRoutine](../47/RtlpCallInterceptRoutine_function_00479594.md) (function, `0x00479594`)
- `0x002EA4E6` → [RtlpCallInterceptRoutine](../47/RtlpCallInterceptRoutine_function_00479594.md) (function, `0x00479594`)
- `0x002EA508` → [RtlCSparseBitmapBitmaskRead](../36/RtlCSparseBitmapBitmaskRead_function_0036190C.md) (function, `0x0036190C`)
- `0x002EA537` → [RtlpHpLargeFree](RtlpHpLargeFree_function_002EC89C.md) (function, `0x002EC89C`)
- `0x002EA5AC` → [RtlpHpLfhContextFree](../35/RtlpHpLfhContextFree_function_0035B2A0.md) (function, `0x0035B2A0`)
- `0x002EA5BF` → [RtlpHpSegFreeInternal](../36/RtlpHpSegFreeInternal_function_0036198C.md) (function, `0x0036198C`)
- `0x002EA5DE` → [RtlpLogHeapFailure](../35/RtlpLogHeapFailure_function_0035B7BC.md) (function, `0x0035B7BC`)
- `0x002EA5FB` → [RtlpLogHeapAllocateEvent](../5F/RtlpLogHeapAllocateEvent_function_005F1638.md) (function, `0x005F1638`)

### Direct callers
- [sub_002E9BEB](Unknown_function_002E9BEB.md) at `0x002E9BEF`

### Static image references
- `0x002E9EA6` → RVA `0x00010B80` (`.rdata`; read)
- `0x002E9F81` → RVA `0x00E28308` (`.data`; read)
- `0x002EA150` → RVA `0x00E28328` (`.data`; read)
- `0x002EA4F3` → RVA `0x00E68610` (`.data`; read)
- `0x002EA4FA` → RVA `0x00E68608` (`.data`; read)
- `0x002EA555` → RVA `0x00E28300` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E9DEC  4C 8B DC                        mov r11, rsp
002E9DEF  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
002E9DF3  45 89 43 18                     mov dword ptr [r11 + 0x18], r8d
002E9DF7  55                              push rbp
002E9DF8  56                              push rsi
002E9DF9  57                              push rdi
002E9DFA  41 54                           push r12
002E9DFC  41 55                           push r13
002E9DFE  41 56                           push r14
002E9E00  41 57                           push r15
002E9E02  48 83 EC 60                     sub rsp, 0x60
002E9E06  33 DB                           xor ebx, ebx
002E9E08  4C 8B E2                        mov r12, rdx
002E9E0B  49 89 5B B8                     mov qword ptr [r11 - 0x48], rbx
002E9E0F  45 8B C8                        mov r9d, r8d
002E9E12  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
002E9E16  48 8B F1                        mov rsi, rcx
002E9E19  8B C3                           mov eax, ebx
002E9E1B  8D 53 01                        lea edx, [rbx + 1]
002E9E1E  41 F6 C0 20                     test r8b, 0x20
002E9E22  74 3E                           je 0x1402e9e62
002E9E24  8B 49 18                        mov ecx, dword ptr [rcx + 0x18]
002E9E27  89 4C 24 3C                     mov dword ptr [rsp + 0x3c], ecx
002E9E2B  85 C9                           test ecx, ecx
002E9E2D  74 33                           je 0x1402e9e62
002E9E2F  41 83 C9 08                     or r9d, 8
002E9E33  49 8D 43 B8                     lea rax, [r11 - 0x48]
002E9E37  45 89 4B 18                     mov dword ptr [r11 + 0x18], r9d
002E9E3B  45 33 C0                        xor r8d, r8d
002E9E3E  44 8B CA                        mov r9d, edx
002E9E41  49 89 43 88                     mov qword ptr [r11 - 0x78], rax
002E9E45  48 8B D6                        mov rdx, rsi
002E9E48  E8 47 F7 18 00                  call 0x140479594
002E9E4D  85 C0                           test eax, eax
002E9E4F  0F 88 AB 07 00 00               js 0x1402ea600
002E9E55  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002E9E5A  44 8B 8C 24 B0 00 00 00         mov r9d, dword ptr [rsp + 0xb0]
002E9E62  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
002E9E6C  4C 3B E1                        cmp r12, rcx
002E9E6F  0F 87 8B 07 00 00               ja 0x1402ea600
002E9E75  4A 8D 0C 20                     lea rcx, [rax + r12]
002E9E79  41 8B D1                        mov edx, r9d
002E9E7C  E8 CF 64 12 00                  call 0x140410350
002E9E81  0F B7 8E 84 03 00 00            movzx ecx, word ptr [rsi + 0x384]
002E9E88  45 8B F9                        mov r15d, r9d
002E9E8B  41 81 E7 02 20 00 10            and r15d, 0x10002002
002E9E92  4C 8B E8                        mov r13, rax
002E9E95  44 89 7C 24 34                  mov dword ptr [rsp + 0x34], r15d
002E9E9A  48 3B C1                        cmp rax, rcx
002E9E9D  0F 83 69 05 00 00               jae 0x1402ea40c
002E9EA3  83 C0 0F                        add eax, 0xf
002E9EA6  48 8D 0D D3 6C D2 FF            lea rcx, [rip - 0x2d932d]
002E9EAD  C1 E8 04                        shr eax, 4
002E9EB0  4C 8D B6 40 03 00 00            lea r14, [rsi + 0x340]
002E9EB7  0F B6 2C 08                     movzx ebp, byte ptr [rax + rcx]
002E9EBB  41 8B 4E 4C                     mov ecx, dword ptr [r14 + 0x4c]
002E9EBF  FF CD                           dec ebp
002E9EC1  E8 8A F9 FF FF                  call 0x1402e9850
002E9EC6  48 85 C0                        test rax, rax
002E9EC9  75 08                           jne 0x1402e9ed3
002E9ECB  49 8B CE                        mov rcx, r14
002E9ECE  E8 61 C4 20 00                  call 0x1404f6334
002E9ED3  0F B7 D8                        movzx ebx, ax
002E9ED6  33 D2                           xor edx, edx
002E9ED8  C1 E3 06                        shl ebx, 6
002E9EDB  49 03 DE                        add rbx, r14
002E9EDE  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
002E9EE6  0F B7 04 6B                     movzx eax, word ptr [rbx + rbp*2]
002E9EEA  44 8B C0                        mov r8d, eax
002E9EED  85 C0                           test eax, eax
002E9EEF  75 3B                           jne 0x1402e9f2c
002E9EF1  8B D5                           mov edx, ebp
002E9EF3  49 8B CE                        mov rcx, r14
002E9EF6  E8 99 29 21 00                  call 0x1404fc894
002E9EFB  33 D2                           xor edx, edx
002E9EFD  48 85 C0                        test rax, rax
002E9F00  0F 84 06 05 00 00               je 0x1402ea40c
002E9F06  0F B6 8C 24 BC 00 00 00         movzx ecx, byte ptr [rsp + 0xbc]
002E9F0E  48 C1 E1 08                     shl rcx, 8
002E9F12  48 81 C1 C0 05 00 00            add rcx, 0x5c0
002E9F19  49 03 CE                        add rcx, r14
002E9F1C  0F B7 04 69                     movzx eax, word ptr [rcx + rbp*2]
002E9F20  44 8B C0                        mov r8d, eax
002E9F23  48 3B D9                        cmp rbx, rcx
002E9F26  74 04                           je 0x1402e9f2c
002E9F28  66 89 04 6B                     mov word ptr [rbx + rbp*2], ax
002E9F2C  41 C1 E0 06                     shl r8d, 6
002E9F30  41 8B E8                        mov ebp, r8d
002E9F33  49 03 EE                        add rbp, r14
002E9F36  66 39 55 04                     cmp word ptr [rbp + 4], dx
002E9F3A  0F 84 2D 01 00 00               je 0x1402ea06d
002E9F40  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
002E9F44  41 BB FF 0F 00 00               mov r11d, 0xfff
002E9F4A  49 85 C3                        test r11, rax
002E9F4D  0F 84 A3 04 00 00               je 0x1402ea3f6
002E9F53  4C 8B D8                        mov r11, rax
002E9F56  49 81 E3 00 F0 FF FF            and r11, 0xfffffffffffff000
002E9F5D  48 FF C8                        dec rax
002E9F60  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
002E9F64  49 8B C3                        mov rax, r11
002E9F67  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
002E9F70  45 0F B6 53 18                  movzx r10d, byte ptr [r11 + 0x18]
002E9F75  48 C1 E8 0C                     shr rax, 0xc
002E9F79  41 83 C2 F8                     add r10d, -8
002E9F7D  41 33 43 28                     xor eax, dword ptr [r11 + 0x28]
002E9F81  33 05 81 E3 B3 00               xor eax, dword ptr [rip + 0xb3e381]
002E9F87  49 8B 89 60 07 00 00            mov rcx, qword ptr [r9 + 0x760]
002E9F8E  49 8B 91 68 07 00 00            mov rdx, qword ptr [r9 + 0x768]
002E9F95  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
002E9F9C  0F B7 D8                        movzx ebx, ax
002E9F9F  4C 8D 04 0A                     lea r8, [rdx + rcx]
002E9FA3  48 33 D1                        xor rdx, rcx
002E9FA6  48 8B C2                        mov rax, rdx
002E9FA9  48 C1 C1 18                     rol rcx, 0x18
002E9FAD  48 C1 E0 10                     shl rax, 0x10
002E9FB1  48 33 C8                        xor rcx, rax
002E9FB4  49 C1 E8 20                     shr r8, 0x20
002E9FB8  48 33 CA                        xor rcx, rdx
002E9FBB  41 0F B6 F8                     movzx edi, r8b
002E9FBF  48 C1 C2 25                     rol rdx, 0x25
002E9FC3  49 89 91 68 07 00 00            mov qword ptr [r9 + 0x768], rdx
002E9FCA  49 FF CA                        dec r10
002E9FCD  49 89 89 60 07 00 00            mov qword ptr [r9 + 0x760], rcx
002E9FD4  4D 8D 4B 40                     lea r9, [r11 + 0x40]
002E9FD8  41 0F B6 43 24                  movzx eax, byte ptr [r11 + 0x24]
002E9FDD  4F 8D 14 D1                     lea r10, [r9 + r10*8]
002E9FE1  49 8D 14 C1                     lea rdx, [r9 + rax*8]
002E9FE5  4C 8B 02                        mov r8, qword ptr [rdx]
002E9FE8  49 8B C8                        mov rcx, r8
002E9FEB  48 F7 D1                        not rcx
002E9FEE  48 85 C9                        test rcx, rcx
002E9FF1  75 10                           jne 0x1402ea003
002E9FF3  49 3B D2                        cmp rdx, r10
002E9FF6  74 06                           je 0x1402e9ffe
002E9FF8  48 83 C2 08                     add rdx, 8
002E9FFC  EB E7                           jmp 0x1402e9fe5
002E9FFE  49 8B D1                        mov rdx, r9
002EA001  EB E2                           jmp 0x1402e9fe5
002EA003  F3 48 0F B8 C1                  popcnt rax, rcx
002EA008  0F AF C7                        imul eax, edi
002EA00B  41 BA 01 00 00 00               mov r10d, 1
002EA011  C1 E8 08                        shr eax, 8
002EA014  C4 C2 F9 F7 C2                  shlx rax, r10, rax
002EA019  C4 E2 FB F5 C9                  pdep rcx, rax, rcx
002EA01E  4C 0B C1                        or r8, rcx
002EA021  F3 48 0F BC C1                  tzcnt rax, rcx
002EA026  4C 89 02                        mov qword ptr [rdx], r8
002EA029  41 2B D1                        sub edx, r9d
002EA02C  45 8D 4A 01                     lea r9d, [r10 + 1]
002EA030  8D 0C D0                        lea ecx, [rax + rdx*8]
002EA033  0F AF D9                        imul ebx, ecx
002EA036  8B C1                           mov eax, ecx
002EA038  C1 E8 06                        shr eax, 6
002EA03B  41 88 43 24                     mov byte ptr [r11 + 0x24], al
002EA03F  0F B7 84 24 BA 00 00 00         movzx eax, word ptr [rsp + 0xba]
002EA047  03 D8                           add ebx, eax
002EA049  49 03 DB                        add rbx, r11
002EA04C  45 84 F9                        test r9b, r15b
002EA04F  0F 84 8D 03 00 00               je 0x1402ea3e2
002EA055  41 8B D4                        mov edx, r12d
002EA058  48 8B CB                        mov rcx, rbx
002EA05B  48 83 C2 0F                     add rdx, 0xf
002EA05F  48 83 E2 F0                     and rdx, 0xfffffffffffffff0
002EA063  E8 A8 1B 3D 00                  call 0x1406bbc10
002EA068  E9 75 03 00 00                  jmp 0x1402ea3e2
002EA06D  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
002EA071  0F 0D 4D 38                     prefetchw byte ptr [rbp + 0x38]
002EA075  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
002EA079  41 BA 01 00 00 00               mov r10d, 1
002EA07F  48 F7 C7 FF 0F 00 00            test rdi, 0xfff
002EA086  74 22                           je 0x1402ea0aa
002EA088  48 8D 4F FF                     lea rcx, [rdi - 1]
002EA08C  48 8B C7                        mov rax, rdi
002EA08F  F0 48 0F B1 4D 38               lock cmpxchg qword ptr [rbp + 0x38], rcx
002EA095  74 0A                           je 0x1402ea0a1
002EA097  44 89 54 24 38                  mov dword ptr [rsp + 0x38], r10d
002EA09C  48 8B F8                        mov rdi, rax
002EA09F  EB DE                           jmp 0x1402ea07f
002EA0A1  48 81 E7 00 F0 FF FF            and rdi, 0xfffffffffffff000
002EA0A8  EB 03                           jmp 0x1402ea0ad
002EA0AA  48 8B FA                        mov rdi, rdx
002EA0AD  48 85 FF                        test rdi, rdi
002EA0B0  0F 84 40 03 00 00               je 0x1402ea3f6
002EA0B6  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
002EA0BF  4C 8D 7F 40                     lea r15, [rdi + 0x40]
002EA0C3  0F B6 5F 18                     movzx ebx, byte ptr [rdi + 0x18]
002EA0C7  48 8B C7                        mov rax, rdi
002EA0CA  48 C1 E8 0C                     shr rax, 0xc
002EA0CE  83 C3 F8                        add ebx, -8
002EA0D1  33 47 28                        xor eax, dword ptr [rdi + 0x28]
002EA0D4  33 05 2E E2 B3 00               xor eax, dword ptr [rip + 0xb3e22e]
002EA0DA  49 8B 89 60 07 00 00            mov rcx, qword ptr [r9 + 0x760]
002EA0E1  49 8B 91 68 07 00 00            mov rdx, qword ptr [r9 + 0x768]
002EA0E8  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
002EA0EC  0F B7 C0                        movzx eax, ax
002EA0EF  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
002EA0F3  4C 8D 04 0A                     lea r8, [rdx + rcx]
002EA0F7  48 33 D1                        xor rdx, rcx
002EA0FA  48 8B C2                        mov rax, rdx
002EA0FD  48 C1 C1 18                     rol rcx, 0x18
002EA101  48 C1 E0 10                     shl rax, 0x10
002EA105  48 33 C8                        xor rcx, rax
002EA108  49 C1 E8 20                     shr r8, 0x20
002EA10C  48 33 CA                        xor rcx, rdx
002EA10F  45 0F B6 D8                     movzx r11d, r8b
002EA113  48 C1 C2 25                     rol rdx, 0x25
002EA117  49 89 91 68 07 00 00            mov qword ptr [r9 + 0x768], rdx
002EA11E  48 FF CB                        dec rbx
002EA121  49 89 89 60 07 00 00            mov qword ptr [r9 + 0x760], rcx
002EA128  8A 47 27                        mov al, byte ptr [rdi + 0x27]
002EA12B  44 0F B6 4F 32                  movzx r9d, byte ptr [rdi + 0x32]
002EA130  88 84 24 B8 00 00 00            mov byte ptr [rsp + 0xb8], al
002EA137  49 8D 1C DF                     lea rbx, [r15 + rbx*8]
002EA13B  0F B6 47 24                     movzx eax, byte ptr [rdi + 0x24]
002EA13F  44 89 4C 24 30                  mov dword ptr [rsp + 0x30], r9d
002EA144  49 8D 14 C7                     lea rdx, [r15 + rax*8]
002EA148  4C 8B 02                        mov r8, qword ptr [rdx]
002EA14B  E9 A8 00 00 00                  jmp 0x1402ea1f8
002EA150  8B 05 D2 E1 B3 00               mov eax, dword ptr [rip + 0xb3e1d2]
002EA156  A8 04                           test al, 4
002EA158  75 5E                           jne 0x1402ea1b8
002EA15A  48 3B D3                        cmp rdx, rbx
002EA15D  74 1A                           je 0x1402ea179
002EA15F  41 83 F9 40                     cmp r9d, 0x40
002EA163  75 14                           jne 0x1402ea179
002EA165  41 8B CB                        mov ecx, r11d
002EA168  49 D3 C8                        ror r8, cl
002EA16B  F3 4D 0F BC C8                  tzcnt r9, r8
002EA170  45 03 CB                        add r9d, r11d
002EA173  41 83 E1 3F                     and r9d, 0x3f
002EA177  EB 31                           jmp 0x1402ea1aa
002EA179  F3 49 0F BC C8                  tzcnt rcx, r8
002EA17E  49 0F BD C0                     bsr rax, r8
002EA182  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
002EA186  2B C1                           sub eax, ecx
002EA188  FF C0                           inc eax
002EA18A  44 3B C8                        cmp r9d, eax
002EA18D  41 0F 42 C1                     cmovb eax, r9d
002EA191  44 0F AF D8                     imul r11d, eax
002EA195  41 C1 EB 08                     shr r11d, 8
002EA199  44 03 D9                        add r11d, ecx
002EA19C  41 8B CB                        mov ecx, r11d
002EA19F  49 D3 C8                        ror r8, cl
002EA1A2  F3 4D 0F BC C8                  tzcnt r9, r8
002EA1A7  45 03 CB                        add r9d, r11d
002EA1AA  41 8B C9                        mov ecx, r9d
002EA1AD  41 BA 01 00 00 00               mov r10d, 1
002EA1B3  49 D3 E2                        shl r10, cl
002EA1B6  EB 20                           jmp 0x1402ea1d8
002EA1B8  F3 49 0F B8 C0                  popcnt rax, r8
002EA1BD  41 0F AF C3                     imul eax, r11d
002EA1C1  B9 01 00 00 00                  mov ecx, 1
002EA1C6  C1 E8 08                        shr eax, 8
002EA1C9  C4 E2 F9 F7 C1                  shlx rax, rcx, rax
002EA1CE  C4 42 FB F5 D0                  pdep r10, rax, r8
002EA1D3  F3 4D 0F BC CA                  tzcnt r9, r10
002EA1D8  0F 0D 0A                        prefetchw byte ptr [rdx]
002EA1DB  48 8B 02                        mov rax, qword ptr [rdx]
002EA1DE  48 8B C8                        mov rcx, rax
002EA1E1  49 0B CA                        or rcx, r10
002EA1E4  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
002EA1E9  75 F3                           jne 0x1402ea1de
002EA1EB  4C 8B C0                        mov r8, rax
002EA1EE  4C 85 D0                        test rax, r10
002EA1F1  74 27                           je 0x1402ea21a
002EA1F3  44 8B 4C 24 30                  mov r9d, dword ptr [rsp + 0x30]
002EA1F8  49 F7 D0                        not r8
002EA1FB  4D 85 C0                        test r8, r8
002EA1FE  0F 85 4C FF FF FF               jne 0x1402ea150
002EA204  48 3B D3                        cmp rdx, rbx
002EA207  74 09                           je 0x1402ea212
002EA209  48 83 C2 08                     add rdx, 8
002EA20D  E9 36 FF FF FF                  jmp 0x1402ea148
002EA212  49 8B D7                        mov rdx, r15
002EA215  E9 2E FF FF FF                  jmp 0x1402ea148
002EA21A  41 2B D7                        sub edx, r15d
002EA21D  45 8D 3C D1                     lea r15d, [r9 + rdx*8]
002EA221  44 8B 4C 24 4C                  mov r9d, dword ptr [rsp + 0x4c]
002EA226  41 8B C7                        mov eax, r15d
002EA229  41 8B D9                        mov ebx, r9d
002EA22C  C1 E8 06                        shr eax, 6
002EA22F  41 0F AF DF                     imul ebx, r15d
002EA233  88 47 24                        mov byte ptr [rdi + 0x24], al
002EA236  0F B7 44 24 42                  movzx eax, word ptr [rsp + 0x42]
002EA23B  03 D8                           add ebx, eax
002EA23D  B8 01 00 00 00                  mov eax, 1
002EA242  38 84 24 B8 00 00 00            cmp byte ptr [rsp + 0xb8], al
002EA249  76 36                           jbe 0x1402ea281
002EA24B  44 8B C3                        mov r8d, ebx
002EA24E  48 8B D7                        mov rdx, rdi
002EA251  49 8B CE                        mov rcx, r14
002EA254  E8 D7 03 00 00                  call 0x1402ea630
002EA259  85 C0                           test eax, eax
002EA25B  79 3B                           jns 0x1402ea298
002EA25D  33 DB                           xor ebx, ebx
002EA25F  41 83 FF FF                     cmp r15d, -1
002EA263  74 54                           je 0x1402ea2b9
002EA265  41 8B C7                        mov eax, r15d
002EA268  48 8D 53 FE                     lea rdx, [rbx - 2]
002EA26C  41 83 E7 3F                     and r15d, 0x3f
002EA270  C1 E8 06                        shr eax, 6
002EA273  41 8B CF                        mov ecx, r15d
002EA276  48 D3 C2                        rol rdx, cl
002EA279  F0 48 21 54 C7 40               lock and qword ptr [rdi + rax*8 + 0x40], rdx
002EA27F  EB 41                           jmp 0x1402ea2c2
002EA281  0F B7 47 30                     movzx eax, word ptr [rdi + 0x30]
002EA285  44 3B F8                        cmp r15d, eax
002EA288  76 0E                           jbe 0x1402ea298
002EA28A  44 8B C3                        mov r8d, ebx
002EA28D  48 8B D7                        mov rdx, rdi
002EA290  49 8B CE                        mov rcx, r14
002EA293  E8 80 18 00 00                  call 0x1402ebb18
002EA298  48 03 DF                        add rbx, rdi
002EA29B  B8 02 00 00 00                  mov eax, 2
002EA2A0  84 44 24 34                     test byte ptr [rsp + 0x34], al
002EA2A4  74 13                           je 0x1402ea2b9
002EA2A6  41 8B D4                        mov edx, r12d
002EA2A9  48 8B CB                        mov rcx, rbx
002EA2AC  48 83 C2 0F                     add rdx, 0xf
002EA2B0  48 83 E2 F0                     and rdx, 0xfffffffffffffff0
002EA2B4  E8 57 19 3D 00                  call 0x1406bbc10
002EA2B9  48 85 DB                        test rbx, rbx
002EA2BC  0F 85 01 01 00 00               jne 0x1402ea3c3
002EA2C2  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
002EA2C6  41 B8 01 00 00 00               mov r8d, 1
002EA2CC  45 8D 48 01                     lea r9d, [r8 + 1]
002EA2D0  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
002EA2D8  48 8B C8                        mov rcx, rax
002EA2DB  0F B6 94 24 BE 00 00 00         movzx edx, byte ptr [rsp + 0xbe]
002EA2E3  48 C1 E9 30                     shr rcx, 0x30
002EA2E7  41 3A C8                        cmp cl, r8b
002EA2EA  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
002EA2EF  41 0F 44 D1                     cmove edx, r9d
002EA2F3  66 44 01 84 24 BA 00 00 00      add word ptr [rsp + 0xba], r8w
002EA2FC  88 94 24 BE 00 00 00            mov byte ptr [rsp + 0xbe], dl
002EA303  0F B7 57 2C                     movzx edx, word ptr [rdi + 0x2c]
002EA307  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
002EA30F  48 C1 E2 06                     shl rdx, 6
002EA313  F0 48 0F B1 4F 10               lock cmpxchg qword ptr [rdi + 0x10], rcx
002EA319  75 B5                           jne 0x1402ea2d0
002EA31B  42 80 7C 32 5C 00               cmp byte ptr [rdx + r14 + 0x5c], 0
002EA321  75 24                           jne 0x1402ea347
002EA323  46 88 44 32 5C                  mov byte ptr [rdx + r14 + 0x5c], r8b
002EA328  4D 8B 3E                        mov r15, qword ptr [r14]
002EA32B  49 8B 4F 38                     mov rcx, qword ptr [r15 + 0x38]
002EA32F  E8 AC 44 1A 00                  call 0x14048e7e0
002EA334  85 C0                           test eax, eax
002EA336  75 09                           jne 0x1402ea341
002EA338  49 8B 4F 38                     mov rcx, qword ptr [r15 + 0x38]
002EA33C  E8 5F C1 03 00                  call 0x1403264a0
002EA341  41 B8 01 00 00 00               mov r8d, 1
002EA347  44 38 44 24 46                  cmp byte ptr [rsp + 0x46], r8b
002EA34C  75 75                           jne 0x1402ea3c3
002EA34E  44 0F B7 4C 24 44               movzx r9d, word ptr [rsp + 0x44]
002EA354  41 C1 E1 06                     shl r9d, 6
002EA358  4D 03 CE                        add r9, r14
002EA35B  41 0F 0D 49 08                  prefetchw byte ptr [r9 + 8]
002EA360  4C 8B 57 18                     mov r10, qword ptr [rdi + 0x18]
002EA364  49 C7 C7 00 F0 FF FF            mov r15, 0xfffffffffffff000
002EA36B  49 8B 41 08                     mov rax, qword ptr [r9 + 8]
002EA36F  49 8B CA                        mov rcx, r10
002EA372  48 33 C8                        xor rcx, rax
002EA375  48 8B D0                        mov rdx, rax
002EA378  49 23 CF                        and rcx, r15
002EA37B  41 BB FF 0F 00 00               mov r11d, 0xfff
002EA381  49 33 CA                        xor rcx, r10
002EA384  49 23 D3                        and rdx, r11
002EA387  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
002EA38B  48 8B CF                        mov rcx, rdi
002EA38E  48 0B CA                        or rcx, rdx
002EA391  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
002EA397  74 2A                           je 0x1402ea3c3
002EA399  49 8B CA                        mov rcx, r10
002EA39C  48 8B D0                        mov rdx, rax
002EA39F  48 33 C8                        xor rcx, rax
002EA3A2  49 23 D3                        and rdx, r11
002EA3A5  49 23 CF                        and rcx, r15
002EA3A8  4C 8B C0                        mov r8, rax
002EA3AB  49 33 CA                        xor rcx, r10
002EA3AE  48 89 4F 18                     mov qword ptr [rdi + 0x18], rcx
002EA3B2  48 8B CF                        mov rcx, rdi
002EA3B5  48 0B CA                        or rcx, rdx
002EA3B8  F0 49 0F B1 49 08               lock cmpxchg qword ptr [r9 + 8], rcx
002EA3BE  49 3B C0                        cmp rax, r8
002EA3C1  75 D6                           jne 0x1402ea399
002EA3C3  83 7C 24 38 00                  cmp dword ptr [rsp + 0x38], 0
002EA3C8  74 13                           je 0x1402ea3dd
002EA3CA  0F B7 55 02                     movzx edx, word ptr [rbp + 2]
002EA3CE  49 8B CE                        mov rcx, r14
002EA3D1  48 C1 E2 06                     shl rdx, 6
002EA3D5  49 03 D6                        add rdx, r14
002EA3D8  E8 2B 5C 1E 00                  call 0x1404d0008
002EA3DD  44 8B 7C 24 34                  mov r15d, dword ptr [rsp + 0x34]
002EA3E2  45 8B C5                        mov r8d, r13d
002EA3E5  48 83 FB FF                     cmp rbx, -1
002EA3E9  74 24                           je 0x1402ea40f
002EA3EB  41 BD 02 00 00 00               mov r13d, 2
002EA3F1  41 8B FD                        mov edi, r13d
002EA3F4  EB 64                           jmp 0x1402ea45a
002EA3F6  45 8B CF                        mov r9d, r15d
002EA3F9  45 8B C4                        mov r8d, r12d
002EA3FC  48 8B D5                        mov rdx, rbp
002EA3FF  49 8B CE                        mov rcx, r14
002EA402  E8 B5 EB FF FF                  call 0x1402e8fbc
002EA407  48 8B D8                        mov rbx, rax
002EA40A  EB D6                           jmp 0x1402ea3e2
002EA40C  45 8B C5                        mov r8d, r13d
002EA40F  BF 03 00 00 00                  mov edi, 3
002EA414  45 8B CF                        mov r9d, r15d
002EA417  49 81 FD 00 00 02 00            cmp r13, 0x20000
002EA41E  77 11                           ja 0x1402ea431
002EA420  48 8D 8E C0 02 00 00            lea rcx, [rsi + 0x2c0]
002EA427  41 8B D4                        mov edx, r12d
002EA42A  E8 15 05 00 00                  call 0x1402ea944
002EA42F  EB 20                           jmp 0x1402ea451
002EA431  8B 86 10 02 00 00               mov eax, dword ptr [rsi + 0x210]
002EA437  4D 8B C5                        mov r8, r13
002EA43A  49 8B D4                        mov rdx, r12
002EA43D  48 8B CE                        mov rcx, rsi
002EA440  4C 3B E8                        cmp r13, rax
002EA443  77 07                           ja 0x1402ea44c
002EA445  E8 36 C1 03 00                  call 0x140326580
002EA44A  EB 05                           jmp 0x1402ea451
002EA44C  E8 0B 19 00 00                  call 0x1402ebd5c
002EA451  48 8B D8                        mov rbx, rax
002EA454  41 BD 02 00 00 00               mov r13d, 2
002EA45A  45 33 FF                        xor r15d, r15d
002EA45D  48 85 DB                        test rbx, rbx
002EA460  0F 84 9A 01 00 00               je 0x1402ea600
002EA466  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
002EA46D  A9 08 2F 00 20                  test eax, 0x20002f08
002EA472  0F 84 70 01 00 00               je 0x1402ea5e8
002EA478  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
002EA47C  4D 8B C4                        mov r8, r12
002EA47F  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
002EA484  48 8B D3                        mov rdx, rbx
002EA487  48 8B CE                        mov rcx, rsi
002EA48A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
002EA48F  E8 24 0D 1F 00                  call 0x1404db1b8
002EA494  44 8B 74 24 3C                  mov r14d, dword ptr [rsp + 0x3c]
002EA499  45 85 F6                        test r14d, r14d
002EA49C  0F 84 46 01 00 00               je 0x1402ea5e8
002EA4A2  8A 48 02                        mov cl, byte ptr [rax + 2]
002EA4A5  48 8D 68 10                     lea rbp, [rax + 0x10]
002EA4A9  8A D1                           mov dl, cl
002EA4AB  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
002EA4B0  41 32 D6                        xor dl, r14b
002EA4B3  45 8B CD                        mov r9d, r13d
002EA4B6  80 E2 0F                        and dl, 0xf
002EA4B9  4C 8B C3                        mov r8, rbx
002EA4BC  32 D1                           xor dl, cl
002EA4BE  41 8B CE                        mov ecx, r14d
002EA4C1  88 50 02                        mov byte ptr [rax + 2], dl
002EA4C4  48 8B D6                        mov rdx, rsi
002EA4C7  E8 C8 F0 18 00                  call 0x140479594
002EA4CC  85 C0                           test eax, eax
002EA4CE  0F 89 14 01 00 00               jns 0x1402ea5e8
002EA4D4  45 8D 4F 03                     lea r9d, [r15 + 3]
002EA4D8  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
002EA4DD  4C 8B C3                        mov r8, rbx
002EA4E0  48 8B D6                        mov rdx, rsi
002EA4E3  41 8B CE                        mov ecx, r14d
002EA4E6  E8 A9 F0 18 00                  call 0x140479594
002EA4EB  66 85 DB                        test bx, bx
002EA4EE  75 51                           jne 0x1402ea541
002EA4F0  48 8B D3                        mov rdx, rbx
002EA4F3  48 8D 0D 16 E1 B7 00            lea rcx, [rip + 0xb7e116]
002EA4FA  48 2B 15 07 E1 B7 00            sub rdx, qword ptr [rip + 0xb7e107]
002EA501  48 C1 EA 14                     shr rdx, 0x14
002EA505  48 03 D2                        add rdx, rdx
002EA508  E8 FF 73 07 00                  call 0x14036190c
002EA50D  48 85 C0                        test rax, rax
002EA510  74 1F                           je 0x1402ea531
002EA512  FF C8                           dec eax
002EA514  41 3B C5                        cmp eax, r13d
002EA517  74 18                           je 0x1402ea531
002EA519  41 8D 4F 01                     lea ecx, [r15 + 1]
002EA51D  4C 8D 96 40 01 00 00            lea r10, [rsi + 0x140]
002EA524  3B C1                           cmp eax, ecx
002EA526  75 20                           jne 0x1402ea548
002EA528  49 81 C2 C0 00 00 00            add r10, 0xc0
002EA52F  EB 17                           jmp 0x1402ea548
002EA531  48 8B D3                        mov rdx, rbx
002EA534  48 8B CE                        mov rcx, rsi
002EA537  E8 60 23 00 00                  call 0x1402ec89c
002EA53C  E9 A2 00 00 00                  jmp 0x1402ea5e3
002EA541  4C 8D 96 40 01 00 00            lea r10, [rsi + 0x140]
002EA548  4C 8B C3                        mov r8, rbx
002EA54B  4D 23 02                        and r8, qword ptr [r10]
002EA54E  49 8B C0                        mov rax, r8
002EA551  49 33 40 10                     xor rax, qword ptr [r8 + 0x10]
002EA555  48 33 05 A4 DD B3 00            xor rax, qword ptr [rip + 0xb3dda4]
002EA55C  49 3B C2                        cmp rax, r10
002EA55F  75 65                           jne 0x1402ea5c6
002EA561  41 8A 4A 08                     mov cl, byte ptr [r10 + 8]
002EA565  4C 8B DB                        mov r11, rbx
002EA568  4D 2B D8                        sub r11, r8
002EA56B  45 8B DB                        mov r11d, r11d
002EA56E  49 D3 EB                        shr r11, cl
002EA571  49 C1 E3 05                     shl r11, 5
002EA575  4D 03 D8                        add r11, r8
002EA578  41 0F B6 43 1A                  movzx eax, byte ptr [r11 + 0x1a]
002EA57D  48 F7 D8                        neg rax
002EA580  48 C1 E0 05                     shl rax, 5
002EA584  4C 03 D8                        add r11, rax
002EA587  49 8B D3                        mov rdx, r11
002EA58A  49 2B D0                        sub rdx, r8
002EA58D  48 C1 FA 05                     sar rdx, 5
002EA591  48 D3 E2                        shl rdx, cl
002EA594  49 03 D0                        add rdx, r8
002EA597  48 3B D3                        cmp rdx, rbx
002EA59A  0F 94 C0                        sete al
002EA59D  41 02 43 18                     add al, byte ptr [r11 + 0x18]
002EA5A1  3C 0B                           cmp al, 0xb
002EA5A3  75 0E                           jne 0x1402ea5b3
002EA5A5  49 8B 4A 18                     mov rcx, qword ptr [r10 + 0x18]
002EA5A9  4C 8B C3                        mov r8, rbx
002EA5AC  E8 EF 0C 07 00                  call 0x14035b2a0
002EA5B1  EB 30                           jmp 0x1402ea5e3
002EA5B3  45 33 C9                        xor r9d, r9d
002EA5B6  4D 8B C3                        mov r8, r11
002EA5B9  48 8B D3                        mov rdx, rbx
002EA5BC  49 8B CA                        mov rcx, r10
002EA5BF  E8 C8 73 07 00                  call 0x14036198c
002EA5C4  EB 1D                           jmp 0x1402ea5e3
002EA5C6  49 8B 52 38                     mov rdx, qword ptr [r10 + 0x38]
002EA5CA  45 33 C9                        xor r9d, r9d
002EA5CD  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
002EA5D2  4C 8B C3                        mov r8, rbx
002EA5D5  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
002EA5DA  41 8D 49 09                     lea ecx, [r9 + 9]
002EA5DE  E8 D9 11 07 00                  call 0x14035b7bc
002EA5E3  49 8B DF                        mov rbx, r15
002EA5E6  EB 18                           jmp 0x1402ea600
002EA5E8  8B 4E 14                        mov ecx, dword ptr [rsi + 0x14]
002EA5EB  84 C9                           test cl, cl
002EA5ED  79 11                           jns 0x1402ea600
002EA5EF  44 8B CF                        mov r9d, edi
002EA5F2  4D 8B C4                        mov r8, r12
002EA5F5  48 8B D3                        mov rdx, rbx
002EA5F8  48 8B CE                        mov rcx, rsi
002EA5FB  E8 38 70 30 00                  call 0x1405f1638
002EA600  48 8B C3                        mov rax, rbx
002EA603  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
002EA60B  48 83 C4 60                     add rsp, 0x60
002EA60F  41 5F                           pop r15
002EA611  41 5E                           pop r14
002EA613  41 5D                           pop r13
002EA615  41 5C                           pop r12
002EA617  5F                              pop rdi
002EA618  5E                              pop rsi
002EA619  5D                              pop rbp
002EA61A  C3                              ret
002EA61B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpAllocateHeapSlow(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int8 v_stack_m52;
    unsigned __int16 v_stack_m54;
    unsigned __int16 v_stack_m56;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int16 v_stack_p22;
    unsigned __int8 v_stack_p24;
    unsigned __int8 v_stack_p26;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (96);
    v_rbx = 0;
    *(unsigned __int64 *)(v_rsp - 72) = 0;
    v_stack_m5C = 0;
    if ((((unsigned __int8)(a3)) & (32)) == 0) goto loc_002E9E62;
    v_stack_m5C = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))) == 0) goto loc_002E9E62;
    a4 = (unsigned int)(((unsigned int)(a3)) | (8));
    *(unsigned int *)(v_rsp + 24) = (unsigned int)(a4);
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 120) = v_rsp - 72;
    result = RtlpCallInterceptRoutine((unsigned int)(*(unsigned int *)(a1 + 24)), a1, a3, (unsigned int)((unsigned int)(v_rbx + 1)));
    if (sign_flag) goto loc_002EA600;
loc_002E9E62:
    if (a2 > ((unsigned int)(*(unsigned int *)(a1 + 24)))) goto loc_002EA600;
    result = RtlpHpCalculateAllocSize(v_stack_m48 + a2 * 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), a3, (unsigned int)(v_stack_p18));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_p18)))) & (0x10002002ULL));
    v_stack_m64 = (unsigned int)(v_r15);
    if (result >= (*(unsigned __int16 *)(a1 + 900))) goto loc_002EA40C;
    result = (unsigned int)((result) + (15));
    result = (unsigned int)((result) >> (4));
    v_rbp = (unsigned int)((*(unsigned __int8 *)(result + v_rip - 2986797 * 1)) - 1);
    result = RtlpHpEnvTlsGetValue((unsigned int)(*(unsigned int *)(a1 + 832 + 76)), (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), a3, (unsigned int)(v_stack_p18));
    if (result == 0) {
        a1 = a1 + 832;
        result = RtlpHpLfhThreadDataInitializeSet(a1, (unsigned int)((unsigned int)((unsigned int)(v_stack_p18))), a3, (unsigned int)(v_stack_p18));
    }
    a2 = 0;
    v_rbx = (unsigned int)(((unsigned __int16)(result)) << (6));
    v_rbx = (v_rbx) + (a1 + 832);
    v_stack_p20 = result;
    if ((unsigned int)(*(unsigned __int16 *)(v_rbx + v_rbp * 2)) != 0) goto loc_002E9F2C;
    result = RtlpHpLfhBucketCheckAndUpdate(a1 + 832, (unsigned int)((unsigned int)(v_rbp)), (unsigned int)((unsigned int)(*(unsigned __int16 *)(v_rbx + v_rbp * 2))), (unsigned int)(v_stack_p18));
    a2 = 0;
    if (result == 0) goto loc_002EA40C;
    a1 = (v_stack_p24) << (8);
    a1 = (a1) + (0x5C0ULL);
    a1 = (a1) + (a1 + 832);
    if (v_rbx != a1) {
        *(unsigned __int16 *)(v_rbx + v_rbp * 2) = (unsigned __int16)(*(unsigned __int16 *)(a1 + v_rbp * 2));
    }
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(a1 + v_rbp * 2)))) << (6));
    v_rbp = ((unsigned int)(a3)) + (a1 + 832);
    if ((*(unsigned __int16 *)(v_rbp + 4)) == 0) goto loc_002EA06D;
    if ((((unsigned int)(0xFFFULL)) & (*(unsigned __int64 *)(v_rbp + 56))) == 0) goto loc_002EA3F6;
    v_r11 = (*(unsigned __int64 *)(v_rbp + 56)) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(unsigned __int64 *)(v_rbp + 56)) - 1;
    *(unsigned __int64 *)(v_rbp + 56) = result;
    result = (v_r11) >> (12);
    v_r10 = (unsigned int)((*(unsigned __int8 *)(v_r11 + 24)) + (-8));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_r11 + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11789185)));
    v_stack_p20 = (unsigned int)(result);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888));
    result = (a2) << (16);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888)) ^ (result);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) * 1) >> (32);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) = a2;
    v_r10 = (v_r10) - 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) = a1;
loc_002E9FE5:
    a1 = ~(*(unsigned __int64 *)(v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8));
    if (a1 != 0) goto loc_002EA003;
    if ((v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8) == (v_r11 + 64 + v_r10 * 8)) goto loc_002E9FFE;
    a2 = (v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8) + (8);
    goto loc_002E9FE5;
loc_002E9FFE:
    goto loc_002E9FE5;
loc_002EA003:
    result = (unsigned int)((*(unsigned __int8 *)(v_r11 + 36)) * ((unsigned int)((unsigned __int8)(a3))));
    result = (unsigned int)((result) >> (8));
    a3 = (*(unsigned __int64 *)(v_r11 + 64 + *(unsigned __int8 *)(v_r11 + 36) * 8)) | (a1);
    *(unsigned __int64 *)(v_r11 + 64) = a3;
    a2 = (unsigned int)((v_r11 + 64) - ((unsigned int)(v_r11 + 64)));
    v_rbx = (unsigned int)(((unsigned __int16)(result)) * ((unsigned int)(result + a2 * 8)));
    result = (unsigned int)(((unsigned int)((unsigned int)(result + a2 * 8))) >> (6));
    *(unsigned __int8 *)(v_r11 + 36) = (unsigned __int8)(result);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_stack_p22)));
    v_rbx = (v_rbx) + (v_r11);
    if ((((unsigned __int8)(1 + 1)) & ((unsigned __int8)(v_r15))) == 0) goto loc_002EA3E2;
    a2 = ((unsigned int)((unsigned int)(a2))) + (15);
    a2 = (a2) & (-16);
    result = RtlHeapZero(v_rbx, a2, a3, 1 + 1);
    goto loc_002EA3E2;
loc_002EA06D:
    v_stack_m60 = (unsigned int)(a2);
loc_002EA07F:
    if (((*(unsigned __int64 *)(v_rbp + 56)) & (0xFFFULL)) == 0) goto loc_002EA0AA;
    if (((*(unsigned __int64 *)(v_rbp + 56)) & (0xFFFULL)) == 0) goto loc_002EA0A1;
    v_stack_m60 = 1;
    goto loc_002EA07F;
loc_002EA0A1:
    v_rdi = (*(unsigned __int64 *)(v_rbp + 56)) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_002EA0AD;
loc_002EA0AA:
loc_002EA0AD:
    if (a2 == 0) goto loc_002EA3F6;
    result = (a2) >> (12);
    v_rbx = (unsigned int)((*(unsigned __int8 *)(a2 + 24)) + (-8));
    result = (unsigned int)((result) ^ (*(unsigned int *)(a2 + 40)));
    result = (unsigned int)((result) ^ (*(unsigned int *)(v_rip + 11788846)));
    v_stack_m58 = (unsigned int)(result);
    v_stack_m4C = (unsigned int)((unsigned __int16)(result));
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896)) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888));
    result = (a2) << (16);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888)) ^ (result);
    a3 = (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) + *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) * 1) >> (32);
    a1 = (a1) ^ (a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1896) = a2;
    v_rbx = (v_rbx) - 1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1888) = a1;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(a2 + 39));
    v_stack_m68 = (unsigned int)(*(unsigned __int8 *)(a2 + 50));
loc_002EA148:
    goto loc_002EA1F8;
loc_002EA150:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11788754)))) & (4)) != 0) goto loc_002EA1B8;
    if ((a2 + 64 + *(unsigned __int8 *)(a2 + 36) * 8) == (a2 + 64 + v_rbx * 8)) goto loc_002EA179;
    if (((unsigned int)(*(unsigned __int8 *)(a2 + 50))) != 64) goto loc_002EA179;
    a4 = (unsigned int)((*(unsigned __int8 *)(a2 + 50)) + ((unsigned int)((unsigned __int8)(a3))));
    a4 = (unsigned int)((a4) & (63));
    goto loc_002EA1AA;
loc_002EA179:
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11788754)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11788754))) - ((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(a3))))));
    result = (unsigned int)((result) + 1);
    if (((unsigned int)(a4)) < ((unsigned int)(result))) { result = (unsigned int)(a4); }
    v_r11 = (unsigned int)(((unsigned __int8)(a3)) * ((unsigned int)(result)));
    v_r11 = (unsigned int)((v_r11) >> (8));
    v_r11 = (unsigned int)((v_r11) + ((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(a3))))));
    a4 = (unsigned int)((a4) + ((unsigned int)(v_r11)));
loc_002EA1AA:
    v_r10 = (1) << ((unsigned __int8)((unsigned int)((unsigned int)(a4))));
    goto loc_002EA1D8;
loc_002EA1B8:
    result = (unsigned int)((result) * ((unsigned int)(v_r11)));
    result = (unsigned int)((result) >> (8));
loc_002EA1D8:
loc_002EA1DE:
    a1 = (*(unsigned __int64 *)(a2 + 64 + *(unsigned __int8 *)(a2 + 36) * 8)) | (v_r10);
    if (condition_is_not_equal) goto loc_002EA1DE;
    if (((*(unsigned __int64 *)(a2 + 64 + *(unsigned __int8 *)(a2 + 36) * 8)) & (v_r10)) == 0) goto loc_002EA21A;
loc_002EA1F8:
    a3 = ~(*(unsigned __int64 *)(a2 + 64 + *(unsigned __int8 *)(a2 + 36) * 8));
    if (a3 != 0) goto loc_002EA150;
    if ((a2 + 64 + *(unsigned __int8 *)(a2 + 36) * 8) == (a2 + 64 + v_rbx * 8)) goto loc_002EA212;
    a2 = (a2 + 64 + *(unsigned __int8 *)(a2 + 36) * 8) + (8);
    goto loc_002EA148;
loc_002EA212:
    goto loc_002EA148;
loc_002EA21A:
    a2 = (unsigned int)((a2 + 64) - ((unsigned int)(a2 + 64)));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m68) + a2 * 8))) >> (6));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m4C)))) * ((unsigned int)((unsigned int)(v_stack_m68) + a2 * 8)));
    *(unsigned __int8 *)(a2 + 36) = (unsigned __int8)(result);
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_stack_m56)));
    if (v_stack_p20 <= 1) goto loc_002EA281;
    result = RtlpHpLfhSubsegmentCommitBlock(a1 + 832, a2, (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(v_stack_m4C));
    if (!sign_flag) goto loc_002EA298;
    v_rbx = 0;
    if (((unsigned int)((unsigned int)(v_stack_m68) + a2 * 8)) == -1) goto loc_002EA2B9;
    v_r15 = (unsigned int)(((unsigned int)(v_stack_m68) + a2 * 8) & (63));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m68) + a2 * 8))) >> (6));
    goto loc_002EA2C2;
loc_002EA281:
    result = *(unsigned __int16 *)(a2 + 48);
    if (((unsigned int)(v_r15)) >= = ((unsigned int)(*(unsigned __int16 *)(a2 + 48)))) {
        a3 = 0;
        a2 = a2;
        a1 = a1 + 832;
        result = RtlpHpLfhSubsegmentPrefetch(a1, a2, a3, (unsigned int)(v_stack_m4C));
    }
    v_rbx = (v_rbx) + (a2);
    result = 2;
    if (((v_stack_m64) & (2)) != 0) {
        a2 = (unsigned int)(a2);
        a1 = v_rbx;
        a2 = (a2) + (15);
        a2 = (a2) & (-16);
        result = RtlHeapZero(a1, a2, a3, (unsigned int)(v_stack_m4C));
    }
    if (v_rbx != 0) goto loc_002EA3C3;
loc_002EA2C2:
loc_002EA2D0:
    v_stack_p20 = *(unsigned __int64 *)(a2 + 16);
    a1 = (*(unsigned __int64 *)(a2 + 16)) >> (48);
    v_stack_m58 = *(unsigned __int64 *)(a2 + 16);
    a2 = v_stack_p26;
    if (((unsigned __int8)(a1)) == 1) { a2 = (unsigned int)(1 + 1); }
    v_stack_p26 = (unsigned __int8)(a2);
    a2 = (*(unsigned __int16 *)(a2 + 44)) << (6);
    if (condition_is_not_equal) goto loc_002EA2D0;
    if ((*(unsigned __int8 *)(a2 + a1 + 832 * 1 + 92)) != 0) goto loc_002EA347;
    *(unsigned __int8 *)(a2 + a1 + 832 * 1 + 92) = 1;
    result = RtlpHpEnvCompactionIsScheduled(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 832) + 56), a2, 1, 1 + 1);
    if ((unsigned int)(result) == 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 832) + 56);
        result = RtlpHpEnvCompactionSchedule(a1, a2, 1, 1 + 1);
    }
loc_002EA347:
    if (v_stack_m52 != 1) goto loc_002EA3C3;
    a4 = (unsigned int)((v_stack_m54) << (6));
    a4 = (a4) + (a1 + 832);
    a1 = (*(unsigned __int64 *)(a2 + 24)) ^ (*(unsigned __int64 *)(a4 + 8));
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(a2 + 24));
    a2 = (*(unsigned __int64 *)(a4 + 8)) & ((unsigned int)(0xFFFULL));
    *(unsigned __int64 *)(a2 + 24) = a1;
    a1 = (a2) | (a2);
    if (condition_is_equal) goto loc_002EA3C3;
loc_002EA399:
    a1 = (*(unsigned __int64 *)(a2 + 24)) ^ (*(unsigned __int64 *)(a4 + 8));
    a2 = (*(unsigned __int64 *)(a4 + 8)) & ((unsigned int)(0xFFFULL));
    a1 = (a1) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (a1) ^ (*(unsigned __int64 *)(a2 + 24));
    *(unsigned __int64 *)(a2 + 24) = a1;
    a1 = (a2) | (a2);
    if ((*(unsigned __int64 *)(a4 + 8)) != (*(unsigned __int64 *)(a4 + 8))) goto loc_002EA399;
loc_002EA3C3:
    result = *(unsigned __int64 *)(a4 + 8);
    if (v_stack_m60 != 0) {
        a2 = *(unsigned __int16 *)(v_rbp + 2);
        a1 = a1 + 832;
        a2 = (a2) << (6);
        a2 = (a2) + (a1 + 832);
        result = RtlpHpLfhBucketUpdateAffinityMapping(a1, a2, *(unsigned __int64 *)(a4 + 8), a4);
    }
loc_002EA3E2:
    if (v_rbx == -1) goto loc_002EA40F;
    goto loc_002EA45A;
loc_002EA3F6:
    result = RtlpHpLfhSlotAllocateSlow(a1 + 832, v_rbp, (unsigned int)((unsigned int)(a2)), (unsigned int)((unsigned int)((unsigned int)(v_stack_m64))));
    goto loc_002EA3E2;
loc_002EA40C:
loc_002EA40F:
    if (2 > 0x20000ULL) goto loc_002EA431;
    result = RtlpHpVsContextAllocate(a1 + 704, (unsigned int)((unsigned int)(a2)), 2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m64))));
    goto loc_002EA451;
loc_002EA431:
    if (2 > ((unsigned int)(*(unsigned int *)(a1 + 528)))) goto loc_002EA44C;
    result = RtlpHpAllocateHeapBackend(a1, a2, 2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m64))));
    goto loc_002EA451;
loc_002EA44C:
    result = RtlpHpLargeAlloc(a1, a2, 2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m64))));
loc_002EA451:
loc_002EA45A:
    v_r15 = 0;
    if (result == 0) goto loc_002EA600;
    if ((((unsigned int)((unsigned int)(v_stack_p18))) & (0x20002F08ULL)) == 0) goto loc_002EA5E8;
    v_stack_m70 = (unsigned int)((unsigned int)(v_stack_p18));
    v_stack_m78 = v_stack_m48;
    result = RtlpHpExtrasAppend(a1, result, a2, (unsigned int)((unsigned int)((unsigned int)(v_stack_m64))));
    if ((unsigned int)((unsigned int)(v_stack_m5C)) == 0) goto loc_002EA5E8;
    v_stack_m78 = result + 16;
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(result + 2))) ^ ((unsigned __int8)((unsigned int)(v_stack_m5C))));
    a2 = (unsigned __int8)((a2) & (15));
    a2 = (unsigned __int8)((a2) ^ ((unsigned __int8)(*(unsigned __int8 *)(result + 2))));
    *(unsigned __int8 *)(result + 2) = (unsigned __int8)(a2);
    result = RtlpCallInterceptRoutine((unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))), a1, result, 2);
    if (!sign_flag) goto loc_002EA5E8;
    v_stack_m78 = result + 16;
    result = RtlpCallInterceptRoutine((unsigned int)((unsigned int)((unsigned int)(v_stack_m5C))), a1, result, v_r15 + 3);
    if ((unsigned __int16)(result) != 0) goto loc_002EA541;
    a2 = (result) - (*(unsigned __int64 *)(v_rip + 12050695));
    a2 = (a2) >> (20);
    a2 = (a2) + (a2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 12050710, a2, result, v_r15 + 3);
    if (result == 0) goto loc_002EA531;
    result = (unsigned int)((result) - 1);
    if (((unsigned int)(result)) == 2) goto loc_002EA531;
    if (((unsigned int)(result)) != ((unsigned int)(v_r15 + 1))) goto loc_002EA548;
    v_r10 = (a1 + 320) + (192);
    goto loc_002EA548;
loc_002EA531:
    result = RtlpHpLargeFree(a1, result, result, v_r15 + 3);
    goto loc_002EA5E3;
loc_002EA541:
loc_002EA548:
    a3 = (result) & (*(unsigned __int64 *)(a1 + 320));
    result = (a3) ^ (*(unsigned __int64 *)(a3 + 16));
    result = (result) ^ (*(unsigned __int64 *)(v_rip + 11787684));
    if (result != (a1 + 320)) goto loc_002EA5C6;
    v_r11 = (result) - (a3);
    v_r11 = ((unsigned int)((unsigned int)(v_r11))) >> ((unsigned __int8)(*(unsigned __int8 *)(a1 + 320 + 8)));
    v_r11 = (v_r11) << (5);
    v_r11 = (v_r11) + (a3);
    result = -(*(unsigned __int8 *)(v_r11 + 26));
    result = (result) << (5);
    v_r11 = (v_r11) + (result);
    a2 = (v_r11) - (a3);
    a2 = (a2) >> (5);
    a2 = (a2) << ((unsigned __int8)(*(unsigned __int8 *)(a1 + 320 + 8)));
    a2 = (a2) + (a3);
    result = (a2 == result) ? 1 : 0;
    result = (unsigned __int8)((result) + (*(unsigned __int8 *)(v_r11 + 24)));
    if (((unsigned __int8)(result)) != 11) goto loc_002EA5B3;
    result = RtlpHpLfhContextFree(*(unsigned __int64 *)(a1 + 320 + 24), a2, result, v_r15 + 3);
    goto loc_002EA5E3;
loc_002EA5B3:
    a4 = 0;
    result = RtlpHpSegFreeInternal(a1 + 320, result, v_r11, a4);
    goto loc_002EA5E3;
loc_002EA5C6:
    a4 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = RtlpLogHeapFailure(a4 + 9, *(unsigned __int64 *)(a1 + 320 + 56), result, a4);
loc_002EA5E3:
    goto loc_002EA600;
loc_002EA5E8:
    if (sign_flag) {
        a4 = 3;
        a3 = a2;
        a2 = 0;
        a1 = a1;
        result = RtlpLogHeapAllocateEvent(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (96);
    return 0;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpAllocateHeapSlow(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint8_t v_stack_m52;
    uint16_t v_stack_m54;
    uint16_t v_stack_m56;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint16_t v_stack_p22;
    uint8_t v_stack_p24;
    uint8_t v_stack_p26;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (96);
    local_rbx = 0;
    *(uint64_t *)(local_rsp - 0x48) = 0;
    v_stack_m5C = 0;
    if ((((uint8_t)(Arg3)) & (32)) == 0) goto loc_002E9E62;
    v_stack_m5C = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))) == 0) goto loc_002E9E62;
    a4 = (uint32_t)(((uint32_t)(Arg3)) | (8));
    *(uint32_t *)(local_rsp + 0x18) = (uint32_t)(a4);
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x78) = local_rsp - 72;
    result = RtlpCallInterceptRoutine((uint32_t)(*(uint32_t *)(arg1 + 0x18)), Arg1, Arg3, (uint32_t)((uint32_t)(local_rbx + 1)));
    if (sign_flag) goto loc_002EA600;
loc_002E9E62:
    if (Arg2 > ((uint32_t)(*(uint32_t *)(arg1 + 0x18)))) goto loc_002EA600;
    result = RtlpHpCalculateAllocSize(v_stack_m48 + Arg2 * 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), Arg3, (uint32_t)(v_stack_p18));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_p18)))) & (0x10002002ULL));
    v_stack_m64 = (uint32_t)(local_r15);
    if (result >= (*(uint16_t *)(arg1 + 0x384))) goto loc_002EA40C;
    result = (uint32_t)((result) + (15));
    result = (uint32_t)((result) >> (4));
    local_rbp = (uint32_t)((*(uint8_t *)(result + v_rip - 0x2D932D * 1)) - 1);
    result = RtlpHpEnvTlsGetValue((uint32_t)(*(uint32_t *)(arg1 + 0x340 + 0x4C)), (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), Arg3, (uint32_t)(v_stack_p18));
    if (result == 0) {
        Arg1 = Arg1 + 832;
        result = RtlpHpLfhThreadDataInitializeSet(Arg1, (uint32_t)((uint32_t)((uint32_t)(v_stack_p18))), Arg3, (uint32_t)(v_stack_p18));
    }
    Arg2 = 0;
    local_rbx = (uint32_t)(((uint16_t)(result)) << (6));
    local_rbx = (local_rbx) + (Arg1 + 832);
    v_stack_p20 = result;
    if ((uint32_t)(*(uint16_t *)(local_rbx + local_rbp * 2)) != 0) goto loc_002E9F2C;
    result = RtlpHpLfhBucketCheckAndUpdate(Arg1 + 832, (uint32_t)((uint32_t)(local_rbp)), (uint32_t)((uint32_t)(*(uint16_t *)(local_rbx + local_rbp * 2))), (uint32_t)(v_stack_p18));
    Arg2 = 0;
    if (result == 0) goto loc_002EA40C;
    Arg1 = (v_stack_p24) << (8);
    Arg1 = (Arg1) + (0x5C0ULL);
    Arg1 = (Arg1) + (Arg1 + 832);
    if (local_rbx != Arg1) {
        *(uint16_t *)(local_rbx + local_rbp * 2) = (uint16_t)(*(uint16_t *)(arg1 + local_rbp * 2));
    }
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(arg1 + local_rbp * 2)))) << (6));
    local_rbp = ((uint32_t)(Arg3)) + (Arg1 + 832);
    if ((*(uint16_t *)(local_rbp + 0x4)) == 0) goto loc_002EA06D;
    if ((((uint32_t)(0xFFFULL)) & (*(uint64_t *)(local_rbp + 0x38))) == 0) goto loc_002EA3F6;
    local_r11 = (*(uint64_t *)(local_rbp + 0x38)) & (0xFFFFFFFFFFFFF000ULL);
    result = (*(uint64_t *)(local_rbp + 0x38)) - 1;
    *(uint64_t *)(local_rbp + 0x38) = result;
    result = (local_r11) >> (12);
    local_r10 = (uint32_t)((*(uint8_t *)(local_r11 + 0x18)) + (-8));
    result = (uint32_t)((result) ^ (*(uint32_t *)(local_r11 + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xB3E381)));
    v_stack_p20 = (uint32_t)(result);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768)) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760));
    result = (Arg2) << (16);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760)) ^ (result);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) * 1) >> (32);
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) = Arg2;
    local_r10 = (local_r10) - 1;
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) = Arg1;
loc_002E9FE5:
    Arg1 = ~(*(uint64_t *)(local_r11 + 0x40 + *(uint8_t *)(local_r11 + 0x24) * 8));
    if (Arg1 != NULL) goto loc_002EA003;
    if ((local_r11 + 64 + *(uint8_t *)(local_r11 + 0x24) * 8) == (local_r11 + 64 + local_r10 * 8)) goto loc_002E9FFE;
    Arg2 = (local_r11 + 64 + *(uint8_t *)(local_r11 + 0x24) * 8) + (8);
    goto loc_002E9FE5;
loc_002E9FFE:
    goto loc_002E9FE5;
loc_002EA003:
    result = (uint32_t)((*(uint8_t *)(local_r11 + 0x24)) * ((uint32_t)((uint8_t)(Arg3))));
    result = (uint32_t)((result) >> (8));
    Arg3 = (*(uint64_t *)(local_r11 + 0x40 + *(uint8_t *)(local_r11 + 0x24) * 8)) | (Arg1);
    *(uint64_t *)(local_r11 + 0x40) = Arg3;
    Arg2 = (uint32_t)((local_r11 + 64) - ((uint32_t)(local_r11 + 64)));
    local_rbx = (uint32_t)(((uint16_t)(result)) * ((uint32_t)(result + Arg2 * 8)));
    result = (uint32_t)(((uint32_t)((uint32_t)(result + Arg2 * 8))) >> (6));
    *(uint8_t *)(local_r11 + 0x24) = (uint8_t)(result);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(v_stack_p22)));
    local_rbx = (local_rbx) + (local_r11);
    if ((((uint8_t)(1 + 1)) & ((uint8_t)(local_r15))) == 0) goto loc_002EA3E2;
    Arg2 = ((uint32_t)((uint32_t)(Arg2))) + (15);
    Arg2 = (Arg2) & (-16);
    result = RtlHeapZero(local_rbx, Arg2, Arg3, 1 + 1);
    goto loc_002EA3E2;
loc_002EA06D:
    v_stack_m60 = (uint32_t)(Arg2);
loc_002EA07F:
    if (((*(uint64_t *)(local_rbp + 0x38)) & (0xFFFULL)) == 0) goto loc_002EA0AA;
    if (((*(uint64_t *)(local_rbp + 0x38)) & (0xFFFULL)) == 0) goto loc_002EA0A1;
    v_stack_m60 = 1;
    goto loc_002EA07F;
loc_002EA0A1:
    local_rdi = (*(uint64_t *)(local_rbp + 0x38)) & (0xFFFFFFFFFFFFF000ULL);
    goto loc_002EA0AD;
loc_002EA0AA:
loc_002EA0AD:
    if (Arg2 == 0) goto loc_002EA3F6;
    result = (Arg2) >> (12);
    local_rbx = (uint32_t)((*(uint8_t *)(Arg2 + 0x18)) + (-8));
    result = (uint32_t)((result) ^ (*(uint32_t *)(Arg2 + 0x28)));
    result = (uint32_t)((result) ^ (*(uint32_t *)(v_rip + 0xB3E22E)));
    v_stack_m58 = (uint32_t)(result);
    v_stack_m4C = (uint32_t)((uint16_t)(result));
    Arg2 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768)) ^ (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760));
    result = (Arg2) << (16);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760)) ^ (result);
    Arg3 = (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) + *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) * 1) >> (32);
    Arg1 = (Arg1) ^ (Arg2);
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x768) = Arg2;
    local_rbx = (local_rbx) - 1;
    *(void **)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x760) = Arg1;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(Arg2 + 0x27));
    v_stack_m68 = (uint32_t)(*(uint8_t *)(Arg2 + 0x32));
loc_002EA148:
    goto loc_002EA1F8;
loc_002EA150:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3E1D2)))) & (4)) != 0) goto loc_002EA1B8;
    if ((Arg2 + 64 + *(uint8_t *)(Arg2 + 0x24) * 8) == (Arg2 + 64 + local_rbx * 8)) goto loc_002EA179;
    if (((uint32_t)(*(uint8_t *)(Arg2 + 0x32))) != 64) goto loc_002EA179;
    a4 = (uint32_t)((*(uint8_t *)(Arg2 + 0x32)) + ((uint32_t)((uint8_t)(Arg3))));
    a4 = (uint32_t)((a4) & (63));
    goto loc_002EA1AA;
loc_002EA179:
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3E1D2)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB3E1D2))) - ((uint32_t)((uint32_t)((uint32_t)((uint8_t)(Arg3))))));
    result = (uint32_t)((result) + 1);
    if (((uint32_t)(a4)) < ((uint32_t)(result))) { result = (uint32_t)(a4); }
    local_r11 = (uint32_t)(((uint8_t)(Arg3)) * ((uint32_t)(result)));
    local_r11 = (uint32_t)((local_r11) >> (8));
    local_r11 = (uint32_t)((local_r11) + ((uint32_t)((uint32_t)((uint32_t)((uint8_t)(Arg3))))));
    a4 = (uint32_t)((a4) + ((uint32_t)(local_r11)));
loc_002EA1AA:
    local_r10 = (1) << ((uint8_t)((uint32_t)((uint32_t)(a4))));
    goto loc_002EA1D8;
loc_002EA1B8:
    result = (uint32_t)((result) * ((uint32_t)(local_r11)));
    result = (uint32_t)((result) >> (8));
loc_002EA1D8:
loc_002EA1DE:
    Arg1 = (*(uint64_t *)(Arg2 + 0x40 + *(uint8_t *)(Arg2 + 0x24) * 8)) | (local_r10);
    if (condition_is_not_equal) goto loc_002EA1DE;
    if (((*(uint64_t *)(Arg2 + 0x40 + *(uint8_t *)(Arg2 + 0x24) * 8)) & (local_r10)) == 0) goto loc_002EA21A;
loc_002EA1F8:
    Arg3 = ~(*(uint64_t *)(Arg2 + 0x40 + *(uint8_t *)(Arg2 + 0x24) * 8));
    if (Arg3 != 0) goto loc_002EA150;
    if ((Arg2 + 64 + *(uint8_t *)(Arg2 + 0x24) * 8) == (Arg2 + 64 + local_rbx * 8)) goto loc_002EA212;
    Arg2 = (Arg2 + 64 + *(uint8_t *)(Arg2 + 0x24) * 8) + (8);
    goto loc_002EA148;
loc_002EA212:
    goto loc_002EA148;
loc_002EA21A:
    Arg2 = (uint32_t)((Arg2 + 64) - ((uint32_t)(Arg2 + 64)));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m68) + Arg2 * 8))) >> (6));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m4C)))) * ((uint32_t)((uint32_t)(v_stack_m68) + Arg2 * 8)));
    *(uint8_t *)(Arg2 + 0x24) = (uint8_t)(result);
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(v_stack_m56)));
    if (v_stack_p20 <= 1) goto loc_002EA281;
    result = RtlpHpLfhSubsegmentCommitBlock(Arg1 + 832, Arg2, (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(v_stack_m4C));
    if (!sign_flag) goto loc_002EA298;
    local_rbx = 0;
    if (((uint32_t)((uint32_t)(v_stack_m68) + Arg2 * 8)) == -1) goto loc_002EA2B9;
    local_r15 = (uint32_t)(((uint32_t)(v_stack_m68) + Arg2 * 8) & (63));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m68) + Arg2 * 8))) >> (6));
    goto loc_002EA2C2;
loc_002EA281:
    result = *(uint16_t *)(Arg2 + 0x30);
    if (((uint32_t)(local_r15)) >= = ((uint32_t)(*(uint16_t *)(Arg2 + 0x30)))) {
        Arg3 = 0;
        Arg2 = Arg2;
        Arg1 = Arg1 + 832;
        result = RtlpHpLfhSubsegmentPrefetch(Arg1, Arg2, Arg3, (uint32_t)(v_stack_m4C));
    }
    local_rbx = (local_rbx) + (Arg2);
    result = 2;
    if (((v_stack_m64) & (2)) != 0) {
        Arg2 = (uint32_t)(Arg2);
        Arg1 = local_rbx;
        Arg2 = (Arg2) + (15);
        Arg2 = (Arg2) & (-16);
        result = RtlHeapZero(Arg1, Arg2, Arg3, (uint32_t)(v_stack_m4C));
    }
    if (local_rbx != 0) goto loc_002EA3C3;
loc_002EA2C2:
loc_002EA2D0:
    v_stack_p20 = *(uint64_t *)(Arg2 + 0x10);
    Arg1 = (*(uint64_t *)(Arg2 + 0x10)) >> (48);
    v_stack_m58 = *(uint64_t *)(Arg2 + 0x10);
    Arg2 = v_stack_p26;
    if (((uint8_t)(Arg1)) == 1) { Arg2 = (uint32_t)(1 + 1); }
    v_stack_p26 = (uint8_t)(Arg2);
    Arg2 = (*(uint16_t *)(Arg2 + 0x2C)) << (6);
    if (condition_is_not_equal) goto loc_002EA2D0;
    if ((*(uint8_t *)(Arg2 + arg1 + 0x340 * 1 + 0x5C)) != 0) goto loc_002EA347;
    *(uint8_t *)(Arg2 + arg1 + 0x340 * 1 + 0x5C) = 1;
    result = RtlpHpEnvCompactionIsScheduled(*(uint64_t *)(*(uint64_t *)(arg1 + 0x340) + 0x38), Arg2, 1, 1 + 1);
    if ((uint32_t)(result) == 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x340) + 0x38);
        result = RtlpHpEnvCompactionSchedule(Arg1, Arg2, 1, 1 + 1);
    }
loc_002EA347:
    if (v_stack_m52 != 1) goto loc_002EA3C3;
    a4 = (uint32_t)((v_stack_m54) << (6));
    a4 = (a4) + (Arg1 + 832);
    Arg1 = (*(uint64_t *)(Arg2 + 0x18)) ^ (*(uint64_t *)(a4 + 0x8));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(Arg2 + 0x18));
    Arg2 = (*(uint64_t *)(a4 + 0x8)) & ((uint32_t)(0xFFFULL));
    *(void **)(Arg2 + 0x18) = Arg1;
    Arg1 = (Arg2) | (Arg2);
    if (condition_is_equal) goto loc_002EA3C3;
loc_002EA399:
    Arg1 = (*(uint64_t *)(Arg2 + 0x18)) ^ (*(uint64_t *)(a4 + 0x8));
    Arg2 = (*(uint64_t *)(a4 + 0x8)) & ((uint32_t)(0xFFFULL));
    Arg1 = (Arg1) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (Arg1) ^ (*(uint64_t *)(Arg2 + 0x18));
    *(void **)(Arg2 + 0x18) = Arg1;
    Arg1 = (Arg2) | (Arg2);
    if ((*(uint64_t *)(a4 + 0x8)) != (*(uint64_t *)(a4 + 0x8))) goto loc_002EA399;
loc_002EA3C3:
    result = *(uint64_t *)(a4 + 0x8);
    if (v_stack_m60 != 0) {
        Arg2 = *(uint16_t *)(local_rbp + 0x2);
        Arg1 = Arg1 + 832;
        Arg2 = (Arg2) << (6);
        Arg2 = (Arg2) + (Arg1 + 832);
        result = RtlpHpLfhBucketUpdateAffinityMapping(Arg1, Arg2, *(uint64_t *)(a4 + 0x8), a4);
    }
loc_002EA3E2:
    if (local_rbx == -1) goto loc_002EA40F;
    goto loc_002EA45A;
loc_002EA3F6:
    result = RtlpHpLfhSlotAllocateSlow(Arg1 + 832, local_rbp, (uint32_t)((uint32_t)(Arg2)), (uint32_t)((uint32_t)((uint32_t)(v_stack_m64))));
    goto loc_002EA3E2;
loc_002EA40C:
loc_002EA40F:
    if (2 > 0x20000ULL) goto loc_002EA431;
    result = RtlpHpVsContextAllocate(Arg1 + 704, (uint32_t)((uint32_t)(Arg2)), 2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m64))));
    goto loc_002EA451;
loc_002EA431:
    if (2 > ((uint32_t)(*(uint32_t *)(arg1 + 0x210)))) goto loc_002EA44C;
    result = RtlpHpAllocateHeapBackend(Arg1, Arg2, 2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m64))));
    goto loc_002EA451;
loc_002EA44C:
    result = RtlpHpLargeAlloc(Arg1, Arg2, 2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m64))));
loc_002EA451:
loc_002EA45A:
    local_r15 = 0;
    if (result == 0) goto loc_002EA600;
    if ((((uint32_t)((uint32_t)(v_stack_p18))) & (0x20002F08ULL)) == 0) goto loc_002EA5E8;
    v_stack_m70 = (uint32_t)((uint32_t)(v_stack_p18));
    v_stack_m78 = v_stack_m48;
    result = RtlpHpExtrasAppend(Arg1, result, Arg2, (uint32_t)((uint32_t)((uint32_t)(v_stack_m64))));
    if ((uint32_t)((uint32_t)(v_stack_m5C)) == 0) goto loc_002EA5E8;
    v_stack_m78 = result + 16;
    Arg2 = (uint8_t)(((uint8_t)(*(uint8_t *)(result + 0x2))) ^ ((uint8_t)((uint32_t)(v_stack_m5C))));
    Arg2 = (uint8_t)((Arg2) & (15));
    Arg2 = (uint8_t)((Arg2) ^ ((uint8_t)(*(uint8_t *)(result + 0x2))));
    *(uint8_t *)(result + 0x2) = (uint8_t)(Arg2);
    result = RtlpCallInterceptRoutine((uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))), Arg1, result, 2);
    if (!sign_flag) goto loc_002EA5E8;
    v_stack_m78 = result + 16;
    result = RtlpCallInterceptRoutine((uint32_t)((uint32_t)((uint32_t)(v_stack_m5C))), Arg1, result, local_r15 + 3);
    if ((uint16_t)(result) != 0) goto loc_002EA541;
    Arg2 = (result) - (*(uint64_t *)(v_rip + 0xB7E107));
    Arg2 = (Arg2) >> (20);
    Arg2 = (Arg2) + (Arg2);
    result = RtlCSparseBitmapBitmaskRead(v_rip + 12050710, Arg2, result, local_r15 + 3);
    if (result == 0) goto loc_002EA531;
    result = (uint32_t)((result) - 1);
    if (((uint32_t)(result)) == 2) goto loc_002EA531;
    if (((uint32_t)(result)) != ((uint32_t)(local_r15 + 1))) goto loc_002EA548;
    local_r10 = (Arg1 + 320) + (192);
    goto loc_002EA548;
loc_002EA531:
    result = RtlpHpLargeFree(Arg1, result, result, local_r15 + 3);
    goto loc_002EA5E3;
loc_002EA541:
loc_002EA548:
    Arg3 = (result) & (*(uint64_t *)(arg1 + 0x140));
    result = (Arg3) ^ (*(uint64_t *)(Arg3 + 0x10));
    result = (result) ^ (*(uint64_t *)(v_rip + 0xB3DDA4));
    if (result != (Arg1 + 320)) goto loc_002EA5C6;
    local_r11 = (result) - (Arg3);
    local_r11 = ((uint32_t)((uint32_t)(local_r11))) >> ((uint8_t)(*(uint8_t *)(arg1 + 0x140 + 0x8)));
    local_r11 = (local_r11) << (5);
    local_r11 = (local_r11) + (Arg3);
    result = -(*(uint8_t *)(local_r11 + 0x1A));
    result = (result) << (5);
    local_r11 = (local_r11) + (result);
    Arg2 = (local_r11) - (Arg3);
    Arg2 = (Arg2) >> (5);
    Arg2 = (Arg2) << ((uint8_t)(*(uint8_t *)(arg1 + 0x140 + 0x8)));
    Arg2 = (Arg2) + (Arg3);
    result = (Arg2 == result) ? 1 : 0;
    result = (uint8_t)((result) + (*(uint8_t *)(local_r11 + 0x18)));
    if (((uint8_t)(result)) != 11) goto loc_002EA5B3;
    result = RtlpHpLfhContextFree(*(uint64_t *)(arg1 + 0x140 + 0x18), Arg2, result, local_r15 + 3);
    goto loc_002EA5E3;
loc_002EA5B3:
    a4 = 0;
    result = RtlpHpSegFreeInternal(Arg1 + 320, result, local_r11, a4);
    goto loc_002EA5E3;
loc_002EA5C6:
    a4 = 0;
    v_stack_m70 = 0;
    v_stack_m78 = 0;
    result = RtlpLogHeapFailure(a4 + 9, *(uint64_t *)(arg1 + 0x140 + 0x38), result, a4);
loc_002EA5E3:
    goto loc_002EA600;
loc_002EA5E8:
    if (sign_flag) {
        a4 = 3;
        Arg3 = Arg2;
        Arg2 = 0;
        Arg1 = Arg1;
        result = RtlpLogHeapAllocateEvent(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (96);
    return 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x4C` | `32` | `R` |
| `Arg1` | `+ 0x140` | `64` | `R` |
| `Arg1` | `+ 0x210` | `32` | `R` |
| `Arg1` | `+ 0x2C0` | `64` | `R` |
| `Arg1` | `+ 0x340` | `64` | `R` |
| `Arg1` | `+ 0x384` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E9DEC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
