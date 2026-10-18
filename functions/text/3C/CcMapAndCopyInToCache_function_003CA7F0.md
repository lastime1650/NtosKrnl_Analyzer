# CcMapAndCopyInToCache

- RVA: `0x003CA7F0`–`0x003CB3BD` (길이 `3,021` bytes)
- VA: `0x00000001403CA7F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008F6DC`
- 디코드: `664`개 명령, `3,021/3,021` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **42**; 고유 호출 대상: **23**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003CA921` → [CcForceWriteThrough](../38/CcForceWriteThrough_function_00389E50.md) (function, `0x00389E50`)
- `0x003CA9A1` → [IoReferenceIoAttributionFromThread](IoReferenceIoAttributionFromThread_function_003CB490.md) (function, `0x003CB490`)
- `0x003CAA17` → [CcGetVirtualAddress](../34/CcGetVirtualAddress_function_00340C9C.md) (function, `0x00340C9C`)
- `0x003CAB42` → [CcWrapperMmCopyToCachedPage](../34/CcWrapperMmCopyToCachedPage_function_00347AB0.md) (function, `0x00347AB0`)
- `0x003CABCC` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003CABFB` → [CcSetDirtyInMask](CcSetDirtyInMask_function_003CB688.md) (function, `0x003CB688`)
- `0x003CACEC` → [MmCheckCachedPageStates](../2F/MmCheckCachedPageStates_function_002F6C60.md) (function, `0x002F6C60`)
- `0x003CADB1` → [CcCopyToCacheHelper](CcCopyToCacheHelper_function_003CC290.md) (function, `0x003CC290`)
- `0x003CADFB` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CAE04` → [FsRtlIsNtstatusExpected](../26/FsRtlIsNtstatusExpected_function_0026D390.md) (function, `0x0026D390`)
- `0x003CAE16` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CAEB8` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x003CAEF8` → [CcFlushCachePriv](../35/CcFlushCachePriv_function_0035B040.md) (function, `0x0035B040`)
- `0x003CAF11` → [FsRtlIsNtstatusExpected](../26/FsRtlIsNtstatusExpected_function_0026D390.md) (function, `0x0026D390`)
- `0x003CAF20` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CAFB7` → [MmCheckCachedPageStates](../2F/MmCheckCachedPageStates_function_002F6C60.md) (function, `0x002F6C60`)
- `0x003CAFD0` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x003CB04C` → [FsRtlIsNtstatusExpected](../26/FsRtlIsNtstatusExpected_function_0026D390.md) (function, `0x0026D390`)
- `0x003CB05B` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CB063` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CB097` → [CcLockSystemCacheBuffer](CcLockSystemCacheBuffer_function_003CC5B8.md) (function, `0x003CC5B8`)
- `0x003CB0B6` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CB0C7` → [MmUnlockPages](../29/MmUnlockPages_function_0029EEE0.md) (function, `0x0029EEE0`)
- `0x003CB0CF` → [IoFreeMdl](../29/IoFreeMdl_function_0029EA80.md) (function, `0x0029EA80`)
- `0x003CB1DB` → [CcFlushCachePriv](../35/CcFlushCachePriv_function_0035B040.md) (function, `0x0035B040`)
- `0x003CB208` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CB21C` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CB232` → [FsRtlIsNtstatusExpected](../26/FsRtlIsNtstatusExpected_function_0026D390.md) (function, `0x0026D390`)
- `0x003CB241` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CB254` → [MmUpdateSectionIoAttribution](MmUpdateSectionIoAttribution_function_003C9FA4.md) (function, `0x003C9FA4`)
- `0x003CB261` → [IoDiskIoAttributionDereference](../34/IoDiskIoAttributionDereference_function_00349978.md) (function, `0x00349978`)
- `0x003CB292` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x003CB2BC` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CB2EA` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x003CB30E` → [KeQueryPerformanceCounter](../37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x003CB33E` → [KeAcquireInStackQueuedSpinLockAtDpcLevel](../27/KeAcquireInStackQueuedSpinLockAtDpcLevel_function_00275740.md) (function, `0x00275740`)
- `0x003CB35D` → [KeReleaseInStackQueuedSpinLockFromDpcLevel](../21/KeReleaseInStackQueuedSpinLockFromDpcLevel_function_002171B0.md) (function, `0x002171B0`)
- `0x003CB36A` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)
- `0x003CB37A` → [KeDelayExecutionThread](../20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x003CB384` → [RtlRaiseStatus](../2F/RtlRaiseStatus_function_002F6A50.md) (function, `0x002F6A50`)
- `0x003CB38D` → [CcFreeWorkQueueEntry](../35/CcFreeWorkQueueEntry_function_0035723C.md) (function, `0x0035723C`)
- `0x003CB3B0` → [CcSetDirtyInMask](CcSetDirtyInMask_function_003CB688.md) (function, `0x003CB688`)

### Direct callers
- [CcCopyWriteEx](CcCopyWriteEx_function_003CA4F0.md) at `0x003CA630`

### Static image references
- `0x003CB139` → RVA `0x00E0A86C` (`.data`; read)
- `0x003CB36F` → RVA `0x00E0A858` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003CB34F` → [sub_006E855E](../6E/Unknown_function_006E855E.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003CA7F0  4C 8B DC                        mov r11, rsp
003CA7F3  45 89 4B 20                     mov dword ptr [r11 + 0x20], r9d
003CA7F7  4D 89 43 18                     mov qword ptr [r11 + 0x18], r8
003CA7FB  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
003CA7FF  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
003CA803  53                              push rbx
003CA804  56                              push rsi
003CA805  57                              push rdi
003CA806  41 54                           push r12
003CA808  41 55                           push r13
003CA80A  41 56                           push r14
003CA80C  41 57                           push r15
003CA80E  48 81 EC 40 01 00 00            sub rsp, 0x140
003CA815  41 8B C1                        mov eax, r9d
003CA818  89 84 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], eax
003CA81F  48 8B F9                        mov rdi, rcx
003CA822  44 8A BC 24 B8 01 00 00         mov r15b, byte ptr [rsp + 0x1b8]
003CA82A  33 D2                           xor edx, edx
003CA82C  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
003CA830  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
003CA834  0F 57 C0                        xorps xmm0, xmm0
003CA837  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
003CA83F  4C 8B A4 24 A8 01 00 00         mov r12, qword ptr [rsp + 0x1a8]
003CA847  41 8A 74 24 50                  mov sil, byte ptr [r12 + 0x50]
003CA84C  40 C0 EE 04                     shr sil, 4
003CA850  44 8D 4A 01                     lea r9d, [rdx + 1]
003CA854  41 22 F1                        and sil, r9b
003CA857  40 88 74 24 40                  mov byte ptr [rsp + 0x40], sil
003CA85C  89 84 24 C0 00 00 00            mov dword ptr [rsp + 0xc0], eax
003CA863  41 8B 00                        mov eax, dword ptr [r8]
003CA866  25 FF 0F 00 00                  and eax, 0xfff
003CA86B  89 84 24 80 00 00 00            mov dword ptr [rsp + 0x80], eax
003CA872  49 89 93 20 FF FF FF            mov qword ptr [r11 - 0xe0], rdx
003CA879  65 4C 8B 2C 25 88 01 00 00      mov r13, qword ptr gs:[0x188]
003CA882  4C 89 AC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r13
003CA88A  44 8B F2                        mov r14d, edx
003CA88D  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
003CA891  88 54 24 49                     mov byte ptr [rsp + 0x49], dl
003CA895  88 54 24 44                     mov byte ptr [rsp + 0x44], dl
003CA899  8B DA                           mov ebx, edx
003CA89B  49 89 93 50 FF FF FF            mov qword ptr [r11 - 0xb0], rdx
003CA8A2  44 88 4C 24 47                  mov byte ptr [rsp + 0x47], r9b
003CA8A7  88 54 24 41                     mov byte ptr [rsp + 0x41], dl
003CA8AB  88 54 24 45                     mov byte ptr [rsp + 0x45], dl
003CA8AF  33 C0                           xor eax, eax
003CA8B1  0F 11 84 24 E0 00 00 00         movups xmmword ptr [rsp + 0xe0], xmm0
003CA8B9  49 89 83 78 FF FF FF            mov qword ptr [r11 - 0x88], rax
003CA8C0  0F 57 C9                        xorps xmm1, xmm1
003CA8C3  41 0F 11 4B A0                  movups xmmword ptr [r11 - 0x60], xmm1
003CA8C8  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
003CA8CC  8B 81 98 00 00 00               mov eax, dword ptr [rcx + 0x98]
003CA8D2  B9 00 10 00 00                  mov ecx, 0x1000
003CA8D7  23 C1                           and eax, ecx
003CA8D9  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
003CA8DD  0F 95 44 24 51                  setne byte ptr [rsp + 0x51]
003CA8E2  49 8B 00                        mov rax, qword ptr [r8]
003CA8E5  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
003CA8EA  41 8B 8D 98 05 00 00            mov ecx, dword ptr [r13 + 0x598]
003CA8F1  41 0F B6 85 AC 05 00 00         movzx eax, byte ptr [r13 + 0x5ac]
003CA8F9  8D 04 48                        lea eax, [rax + rcx*2]
003CA8FC  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
003CA903  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
003CA90A  44 8A EE                        mov r13b, sil
003CA90D  40 88 74 24 48                  mov byte ptr [rsp + 0x48], sil
003CA912  40 84 F6                        test sil, sil
003CA915  75 16                           jne 0x1403ca92d
003CA917  4C 8B C7                        mov r8, rdi
003CA91A  41 8B 53 20                     mov edx, dword ptr [r11 + 0x20]
003CA91E  49 8B CC                        mov rcx, r12
003CA921  E8 2A F5 FB FF                  call 0x140389e50
003CA926  44 8A E8                        mov r13b, al
003CA929  88 44 24 48                     mov byte ptr [rsp + 0x48], al
003CA92D  45 84 ED                        test r13b, r13b
003CA930  0F 85 ED 09 00 00               jne 0x1403cb323
003CA936  41 8A C7                        mov al, r15b
003CA939  F6 D8                           neg al
003CA93B  1B C0                           sbb eax, eax
003CA93D  83 E0 FE                        and eax, 0xfffffffe
003CA940  83 C0 06                        add eax, 6
003CA943  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
003CA94A  4C 8B BF 18 02 00 00            mov r15, qword ptr [rdi + 0x218]
003CA951  4C 89 BC 24 08 01 00 00         mov qword ptr [rsp + 0x108], r15
003CA959  4C 89 BC 24 10 01 00 00         mov qword ptr [rsp + 0x110], r15
003CA961  40 84 F6                        test sil, sil
003CA964  0F 85 19 09 00 00               jne 0x1403cb283
003CA96A  48 85 DB                        test rbx, rbx
003CA96D  0F 85 17 0A 00 00               jne 0x1403cb38a
003CA973  4C 8B BC 24 C0 01 00 00         mov r15, qword ptr [rsp + 0x1c0]
003CA97B  4D 85 FF                        test r15, r15
003CA97E  75 16                           jne 0x1403ca996
003CA980  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
003CA989  4C 89 BC 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], r15
003CA991  44 8B 74 24 54                  mov r14d, dword ptr [rsp + 0x54]
003CA996  48 8D 94 24 C8 00 00 00         lea rdx, [rsp + 0xc8]
003CA99E  49 8B CF                        mov rcx, r15
003CA9A1  E8 EA 0A 00 00                  call 0x1403cb490
003CA9A6  45 33 DB                        xor r11d, r11d
003CA9A9  85 C0                           test eax, eax
003CA9AB  0F 89 96 08 00 00               jns 0x1403cb247
003CA9B1  4C 8B AC 24 A8 01 00 00         mov r13, qword ptr [rsp + 0x1a8]
003CA9B9  8B 9C 24 98 01 00 00            mov ebx, dword ptr [rsp + 0x198]
003CA9C0  85 DB                           test ebx, ebx
003CA9C2  75 13                           jne 0x1403ca9d7
003CA9C4  BB 01 00 00 00                  mov ebx, 1
003CA9C9  88 5C 24 4A                     mov byte ptr [rsp + 0x4a], bl
003CA9CD  44 88 5C 24 41                  mov byte ptr [rsp + 0x41], r11b
003CA9D2  E9 21 07 00 00                  jmp 0x1403cb0f8
003CA9D7  44 88 5C 24 43                  mov byte ptr [rsp + 0x43], r11b
003CA9DC  44 39 5C 24 70                  cmp dword ptr [rsp + 0x70], r11d
003CA9E1  8B 84 24 A0 01 00 00            mov eax, dword ptr [rsp + 0x1a0]
003CA9E8  41 0F 45 C3                     cmovne eax, r11d
003CA9EC  89 84 24 A0 01 00 00            mov dword ptr [rsp + 0x1a0], eax
003CA9F3  44 89 5C 24 58                  mov dword ptr [rsp + 0x58], r11d
003CA9F8  44 89 5C 24 28                  mov dword ptr [rsp + 0x28], r11d
003CA9FD  44 89 5C 24 20                  mov dword ptr [rsp + 0x20], r11d
003CAA02  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
003CAA07  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
003CAA0F  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
003CAA14  48 8B CF                        mov rcx, rdi
003CAA17  E8 80 62 F7 FF                  call 0x140340c9c
003CAA1C  4C 8B D0                        mov r10, rax
003CAA1F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
003CAA24  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
003CAA28  3B D3                           cmp edx, ebx
003CAA2A  0F 47 D3                        cmova edx, ebx
003CAA2D  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
003CAA31  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
003CAA35  29 94 24 98 01 00 00            sub dword ptr [rsp + 0x198], edx
003CAA3C  44 8B AC 24 80 00 00 00         mov r13d, dword ptr [rsp + 0x80]
003CAA44  4D 2B D5                        sub r10, r13
003CAA47  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
003CAA4C  46 8D 24 2A                     lea r12d, [rdx + r13]
003CAA50  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
003CAA55  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
003CAA5A  41 B8 01 00 00 00               mov r8d, 1
003CAA60  41 8B C0                        mov eax, r8d
003CAA63  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
003CAA6A  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
003CAA6F  48 89 9C 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rbx
003CAA77  41 2B DD                        sub ebx, r13d
003CAA7A  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
003CAA81  45 33 DB                        xor r11d, r11d
003CAA84  44 88 5C 24 41                  mov byte ptr [rsp + 0x41], r11b
003CAA89  41 8A F3                        mov sil, r11b
003CAA8C  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
003CAA90  44 88 5C 24 43                  mov byte ptr [rsp + 0x43], r11b
003CAA95  41 8B CC                        mov ecx, r12d
003CAA98  41 B9 00 10 00 00               mov r9d, 0x1000
003CAA9E  44 88 5C 24 42                  mov byte ptr [rsp + 0x42], r11b
003CAAA3  45 8B FB                        mov r15d, r11d
003CAAA6  44 89 9C 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r11d
003CAAAE  44 88 44 24 47                  mov byte ptr [rsp + 0x47], r8b
003CAAB3  41 8B D3                        mov edx, r11d
003CAAB6  41 3B C9                        cmp ecx, r9d
003CAAB9  0F 97 C2                        seta dl
003CAABC  89 54 24 5C                     mov dword ptr [rsp + 0x5c], edx
003CAAC0  89 94 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], edx
003CAAC7  44 89 5C 24 64                  mov dword ptr [rsp + 0x64], r11d
003CAACC  8B 8C 24 A0 01 00 00            mov ecx, dword ptr [rsp + 0x1a0]
003CAAD3  85 C1                           test ecx, eax
003CAAD5  0F 84 CA 01 00 00               je 0x1403caca5
003CAADB  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
003CAAE3  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
003CAAEB  48 3B 01                        cmp rax, qword ptr [rcx]
003CAAEE  7C 08                           jl 0x1403caaf8
003CAAF0  45 0B F0                        or r14d, r8d
003CAAF3  44 89 74 24 54                  mov dword ptr [rsp + 0x54], r14d
003CAAF8  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
003CAAFE  A8 40                           test al, 0x40
003CAB00  0F 85 E7 04 00 00               jne 0x1403cafed
003CAB06  0F BA E0 1E                     bt eax, 0x1e
003CAB0A  0F 82 EB 04 00 00               jb 0x1403caffb
003CAB10  44 88 5C 24 42                  mov byte ptr [rsp + 0x42], r11b
003CAB15  85 D2                           test edx, edx
003CAB17  41 8B C1                        mov eax, r9d
003CAB1A  75 03                           jne 0x1403cab1f
003CAB1C  41 8B C4                        mov eax, r12d
003CAB1F  41 2B C5                        sub eax, r13d
003CAB22  44 8B C8                        mov r9d, eax
003CAB25  48 8D 44 24 42                  lea rax, [rsp + 0x42]
003CAB2A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003CAB2F  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
003CAB34  45 8B C5                        mov r8d, r13d
003CAB37  48 8B 94 24 88 01 00 00         mov rdx, qword ptr [rsp + 0x188]
003CAB3F  49 8B CA                        mov rcx, r10
003CAB42  E8 69 CF F7 FF                  call 0x140347ab0
003CAB47  8B F0                           mov esi, eax
003CAB49  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
003CAB4D  45 33 DB                        xor r11d, r11d
003CAB50  85 C0                           test eax, eax
003CAB52  0F 88 F2 04 00 00               js 0x1403cb04a
003CAB58  45 8D 43 01                     lea r8d, [r11 + 1]
003CAB5C  44 88 44 24 41                  mov byte ptr [rsp + 0x41], r8b
003CAB61  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
003CAB65  40 84 F6                        test sil, sil
003CAB68  0F 84 1A 04 00 00               je 0x1403caf88
003CAB6E  44 8B 7C 24 5C                  mov r15d, dword ptr [rsp + 0x5c]
003CAB73  41 B9 00 10 00 00               mov r9d, 0x1000
003CAB79  41 8B C1                        mov eax, r9d
003CAB7C  41 2B C5                        sub eax, r13d
003CAB7F  48 01 84 24 88 01 00 00         add qword ptr [rsp + 0x188], rax
003CAB87  45 8B EB                        mov r13d, r11d
003CAB8A  44 89 9C 24 80 00 00 00         mov dword ptr [rsp + 0x80], r11d
003CAB92  45 85 FF                        test r15d, r15d
003CAB95  0F 85 C0 00 00 00               jne 0x1403cac5b
003CAB9B  44 88 5C 24 41                  mov byte ptr [rsp + 0x41], r11b
003CABA0  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
003CABA8  48 8B 58 08                     mov rbx, qword ptr [rax + 8]
003CABAC  83 C9 FF                        or ecx, 0xffffffff
003CABAF  F0 0F C1 48 10                  lock xadd dword ptr [rax + 0x10], ecx
003CABB4  FF C9                           dec ecx
003CABB6  66 85 C9                        test cx, cx
003CABB9  75 20                           jne 0x1403cabdb
003CABBB  48 8B 8B C0 00 00 00            mov rcx, qword ptr [rbx + 0xc0]
003CABC2  48 85 C9                        test rcx, rcx
003CABC5  74 0D                           je 0x1403cabd4
003CABC7  45 33 C0                        xor r8d, r8d
003CABCA  33 D2                           xor edx, edx
003CABCC  E8 3F 47 F7 FF                  call 0x14033f310
003CABD1  45 33 DB                        xor r11d, r11d
003CABD4  F0 FF 8B 28 02 00 00            lock dec dword ptr [rbx + 0x228]
003CABDB  4C 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], r11
003CABE3  4C 8B BC 24 C0 01 00 00         mov r15, qword ptr [rsp + 0x1c0]
003CABEB  4D 8B CF                        mov r9, r15
003CABEE  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
003CABF3  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
003CABF8  48 8B CF                        mov rcx, rdi
003CABFB  E8 88 0A 00 00                  call 0x1403cb688
003CAC00  8B 8F 98 00 00 00               mov ecx, dword ptr [rdi + 0x98]
003CAC06  81 E1 00 00 00 40               and ecx, 0x40000000
003CAC0C  0F 84 7B 02 00 00               je 0x1403cae8d
003CAC12  45 33 DB                        xor r11d, r11d
003CAC15  85 C9                           test ecx, ecx
003CAC17  0F 85 CB 04 00 00               jne 0x1403cb0e8
003CAC1D  4C 8B AC 24 A8 01 00 00         mov r13, qword ptr [rsp + 0x1a8]
003CAC25  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
003CAC2A  B8 00 10 00 00                  mov eax, 0x1000
003CAC2F  39 84 24 98 01 00 00            cmp dword ptr [rsp + 0x198], eax
003CAC36  0F 82 1E 02 00 00               jb 0x1403cae5a
003CAC3C  B8 01 00 00 00                  mov eax, 1
003CAC41  09 84 24 A0 01 00 00            or dword ptr [rsp + 0x1a0], eax
003CAC48  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
003CAC4C  48 01 44 24 68                  add qword ptr [rsp + 0x68], rax
003CAC51  44 8B 74 24 54                  mov r14d, dword ptr [rsp + 0x54]
003CAC56  E9 5E FD FF FF                  jmp 0x1403ca9b9
003CAC5B  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
003CAC60  4D 03 D1                        add r10, r9
003CAC63  4C 89 54 24 78                  mov qword ptr [rsp + 0x78], r10
003CAC68  41 81 C4 00 F0 FF FF            add r12d, 0xfffff000
003CAC6F  44 89 64 24 74                  mov dword ptr [rsp + 0x74], r12d
003CAC74  41 8B CC                        mov ecx, r12d
003CAC77  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
003CAC7C  41 03 D9                        add ebx, r9d
003CAC7F  89 9C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ebx
003CAC86  44 39 9C 24 98 01 00 00         cmp dword ptr [rsp + 0x198], r11d
003CAC8E  0F 84 E6 01 00 00               je 0x1403cae7a
003CAC94  B8 02 00 00 00                  mov eax, 2
003CAC99  89 84 24 84 00 00 00            mov dword ptr [rsp + 0x84], eax
003CACA0  E9 F9 FD FF FF                  jmp 0x1403caa9e
003CACA5  41 8A C0                        mov al, r8b
003CACA8  88 44 24 46                     mov byte ptr [rsp + 0x46], al
003CACAC  45 8A E3                        mov r12b, r11b
003CACAF  44 88 5C 24 50                  mov byte ptr [rsp + 0x50], r11b
003CACB4  85 D2                           test edx, edx
003CACB6  0F 85 69 02 00 00               jne 0x1403caf25
003CACBC  44 38 9C 24 B8 01 00 00         cmp byte ptr [rsp + 0x1b8], r11b
003CACC4  74 55                           je 0x1403cad1b
003CACC6  48 8B B4 24 C8 01 00 00         mov rsi, qword ptr [rsp + 0x1c8]
003CACCE  4C 39 1E                        cmp qword ptr [rsi], r11
003CACD1  75 44                           jne 0x1403cad17
003CACD3  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
003CACDB  41 83 C8 02                     or r8d, 2
003CACDF  4C 8D 4C 24 46                  lea r9, [rsp + 0x46]
003CACE4  BA 01 00 00 00                  mov edx, 1
003CACE9  49 8B CA                        mov rcx, r10
003CACEC  E8 6F BF F2 FF                  call 0x1402f6c60
003CACF1  B9 01 00 00 00                  mov ecx, 1
003CACF6  44 8A E1                        mov r12b, cl
003CACF9  88 4C 24 50                     mov byte ptr [rsp + 0x50], cl
003CACFD  8A 44 24 46                     mov al, byte ptr [rsp + 0x46]
003CAD01  45 33 DB                        xor r11d, r11d
003CAD04  84 C0                           test al, al
003CAD06  0F 84 C2 02 00 00               je 0x1403cafce
003CAD0C  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
003CAD10  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
003CAD15  EB 09                           jmp 0x1403cad20
003CAD17  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
003CAD1B  B9 01 00 00 00                  mov ecx, 1
003CAD20  45 84 E4                        test r12b, r12b
003CAD23  0F 84 7B 02 00 00               je 0x1403cafa4
003CAD29  84 C0                           test al, al
003CAD2B  0F 84 73 02 00 00               je 0x1403cafa4
003CAD31  44 38 5C 24 47                  cmp byte ptr [rsp + 0x47], r11b
003CAD36  0F 84 1A 02 00 00               je 0x1403caf56
003CAD3C  4C 89 9C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r11
003CAD44  49 8B D3                        mov rdx, r11
003CAD47  48 89 94 24 00 01 00 00         mov qword ptr [rsp + 0x100], rdx
003CAD4F  44 89 9C 24 94 00 00 00         mov dword ptr [rsp + 0x94], r11d
003CAD57  45 85 FF                        test r15d, r15d
003CAD5A  0F 88 00 03 00 00               js 0x1403cb060
003CAD60  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
003CAD64  44 8B 64 24 74                  mov r12d, dword ptr [rsp + 0x74]
003CAD69  44 8B 7C 24 5C                  mov r15d, dword ptr [rsp + 0x5c]
003CAD6E  85 C0                           test eax, eax
003CAD70  0F 85 F2 02 00 00               jne 0x1403cb068
003CAD76  85 C0                           test eax, eax
003CAD78  48 0F 44 54 24 78               cmove rdx, qword ptr [rsp + 0x78]
003CAD7E  41 8B C5                        mov eax, r13d
003CAD81  48 03 D0                        add rdx, rax
003CAD84  45 85 FF                        test r15d, r15d
003CAD87  75 58                           jne 0x1403cade1
003CAD89  45 8B CC                        mov r9d, r12d
003CAD8C  45 2B CD                        sub r9d, r13d
003CAD8F  44 88 5C 24 42                  mov byte ptr [rsp + 0x42], r11b
003CAD94  48 8D 44 24 42                  lea rax, [rsp + 0x42]
003CAD99  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003CAD9E  8A 44 24 51                     mov al, byte ptr [rsp + 0x51]
003CADA2  88 44 24 20                     mov byte ptr [rsp + 0x20], al
003CADA6  4C 8B 84 24 88 01 00 00         mov r8, qword ptr [rsp + 0x188]
003CADAE  48 8B CF                        mov rcx, rdi
003CADB1  E8 DA 14 00 00                  call 0x1403cc290
003CADB6  41 B8 01 00 00 00               mov r8d, 1
003CADBC  44 88 44 24 41                  mov byte ptr [rsp + 0x41], r8b
003CADC1  45 33 DB                        xor r11d, r11d
003CADC4  40 84 F6                        test sil, sil
003CADC7  75 20                           jne 0x1403cade9
003CADC9  40 0F B6 F6                     movzx esi, sil
003CADCD  44 38 5C 24 42                  cmp byte ptr [rsp + 0x42], r11b
003CADD2  41 0F 45 F0                     cmovne esi, r8d
003CADD6  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
003CADDA  40 88 74 24 43                  mov byte ptr [rsp + 0x43], sil
003CADDF  EB 08                           jmp 0x1403cade9
003CADE1  41 B9 00 10 00 00               mov r9d, 0x1000
003CADE7  EB A3                           jmp 0x1403cad8c
003CADE9  EB 31                           jmp 0x1403cae1c
003CADEB  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
003CADEF  3D 05 00 00 C0                  cmp eax, 0xc0000005
003CADF4  75 0A                           jne 0x1403cae00
003CADF6  B9 E8 00 00 C0                  mov ecx, 0xc00000e8
003CADFB  E8 50 BC F2 FF                  call 0x1402f6a50
003CAE00  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
003CAE04  E8 87 25 EA FF                  call 0x14026d390
003CAE09  84 C0                           test al, al
003CAE0B  8B 4C 24 64                     mov ecx, dword ptr [rsp + 0x64]
003CAE0F  75 05                           jne 0x1403cae16
003CAE11  B9 E9 00 00 C0                  mov ecx, 0xc00000e9
003CAE16  E8 35 BC F2 FF                  call 0x1402f6a50
003CAE1B  90                              nop
003CAE1C  48 8B B4 24 D0 00 00 00         mov rsi, qword ptr [rsp + 0xd0]
003CAE24  48 85 F6                        test rsi, rsi
003CAE27  0F 85 97 02 00 00               jne 0x1403cb0c4
003CAE2D  8B 94 24 88 00 00 00            mov edx, dword ptr [rsp + 0x88]
003CAE34  8A C2                           mov al, dl
003CAE36  41 22 C0                        and al, r8b
003CAE39  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
003CAE41  88 81 AC 05 00 00               mov byte ptr [rcx + 0x5ac], al
003CAE47  8B C2                           mov eax, edx
003CAE49  D1 E8                           shr eax, 1
003CAE4B  89 81 98 05 00 00               mov dword ptr [rcx + 0x598], eax
003CAE51  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
003CAE55  E9 19 FD FF FF                  jmp 0x1403cab73
003CAE5A  8A 84 24 A0 01 00 00            mov al, byte ptr [rsp + 0x1a0]
003CAE61  24 04                           and al, 4
003CAE63  F6 D8                           neg al
003CAE65  1B C0                           sbb eax, eax
003CAE67  23 84 24 A0 01 00 00            and eax, dword ptr [rsp + 0x1a0]
003CAE6E  89 84 24 A0 01 00 00            mov dword ptr [rsp + 0x1a0], eax
003CAE75  E9 CE FD FF FF                  jmp 0x1403cac48
003CAE7A  B8 04 00 00 00                  mov eax, 4
003CAE7F  41 3B C9                        cmp ecx, r9d
003CAE82  8D 50 FE                        lea edx, [rax - 2]
003CAE85  0F 47 C2                        cmova eax, edx
003CAE88  E9 0C FE FF FF                  jmp 0x1403cac99
003CAE8D  8B 84 24 8C 00 00 00            mov eax, dword ptr [rsp + 0x8c]
003CAE94  2B 84 24 98 01 00 00            sub eax, dword ptr [rsp + 0x198]
003CAE9B  3D 00 00 00 01                  cmp eax, 0x1000000
003CAEA0  0F 86 6C FD FF FF               jbe 0x1403cac12
003CAEA6  45 33 DB                        xor r11d, r11d
003CAEA9  48 8B B4 24 C8 01 00 00         mov rsi, qword ptr [rsp + 0x1c8]
003CAEB1  4C 39 1E                        cmp qword ptr [rsi], r11
003CAEB4  75 0D                           jne 0x1403caec3
003CAEB6  33 C9                           xor ecx, ecx
003CAEB8  E8 23 39 FB FF                  call 0x14037e7e0
003CAEBD  48 89 06                        mov qword ptr [rsi], rax
003CAEC0  45 33 DB                        xor r11d, r11d
003CAEC3  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
003CAEC8  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
003CAED0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003CAED5  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
003CAEDA  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
003CAEDF  45 33 C9                        xor r9d, r9d
003CAEE2  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
003CAEE7  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
003CAEEC  4C 8B AC 24 A8 01 00 00         mov r13, qword ptr [rsp + 0x1a8]
003CAEF4  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003CAEF8  E8 43 01 F9 FF                  call 0x14035b040
003CAEFD  8B 9C 24 A0 00 00 00            mov ebx, dword ptr [rsp + 0xa0]
003CAF04  45 33 DB                        xor r11d, r11d
003CAF07  85 DB                           test ebx, ebx
003CAF09  0F 89 1B FD FF FF               jns 0x1403cac2a
003CAF0F  8B CB                           mov ecx, ebx
003CAF11  E8 7A 24 EA FF                  call 0x14026d390
003CAF16  B9 E9 00 00 C0                  mov ecx, 0xc00000e9
003CAF1B  84 C0                           test al, al
003CAF1D  0F 45 CB                        cmovne ecx, ebx
003CAF20  E8 2B BB F2 FF                  call 0x1402f6a50
003CAF25  F6 C1 04                        test cl, 4
003CAF28  0F 84 8E FD FF FF               je 0x1403cacbc
003CAF2E  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
003CAF36  44 88 81 AC 05 00 00            mov byte ptr [rcx + 0x5ac], r8b
003CAF3D  44 39 81 98 05 00 00            cmp dword ptr [rcx + 0x598], r8d
003CAF44  0F 83 72 FD FF FF               jae 0x1403cacbc
003CAF4A  44 89 81 98 05 00 00            mov dword ptr [rcx + 0x598], r8d
003CAF51  E9 66 FD FF FF                  jmp 0x1403cacbc
003CAF56  44 38 9C 24 B8 01 00 00         cmp byte ptr [rsp + 0x1b8], r11b
003CAF5E  0F 85 D8 FD FF FF               jne 0x1403cad3c
003CAF64  44 88 5C 24 4A                  mov byte ptr [rsp + 0x4a], r11b
003CAF69  40 8A 74 24 40                  mov sil, byte ptr [rsp + 0x40]
003CAF6E  4C 8B BC 24 C0 01 00 00         mov r15, qword ptr [rsp + 0x1c0]
003CAF76  4C 8B AC 24 A8 01 00 00         mov r13, qword ptr [rsp + 0x1a8]
003CAF7E  BB 01 00 00 00                  mov ebx, 1
003CAF83  E9 70 01 00 00                  jmp 0x1403cb0f8
003CAF88  44 38 5C 24 42                  cmp byte ptr [rsp + 0x42], r11b
003CAF8D  0F 84 DB FB FF FF               je 0x1403cab6e
003CAF93  41 8A F0                        mov sil, r8b
003CAF96  89 74 24 4C                     mov dword ptr [rsp + 0x4c], esi
003CAF9A  44 88 44 24 43                  mov byte ptr [rsp + 0x43], r8b
003CAF9F  E9 CA FB FF FF                  jmp 0x1403cab6e
003CAFA4  4C 8D 4C 24 47                  lea r9, [rsp + 0x47]
003CAFA9  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
003CAFB1  48 8B D1                        mov rdx, rcx
003CAFB4  49 8B CA                        mov rcx, r10
003CAFB7  E8 A4 BC F2 FF                  call 0x1402f6c60
003CAFBC  44 8B F8                        mov r15d, eax
003CAFBF  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
003CAFC6  45 33 DB                        xor r11d, r11d
003CAFC9  E9 63 FD FF FF                  jmp 0x1403cad31
003CAFCE  33 C9                           xor ecx, ecx
003CAFD0  E8 0B 38 FB FF                  call 0x14037e7e0
003CAFD5  48 89 06                        mov qword ptr [rsi], rax
003CAFD8  8A 44 24 46                     mov al, byte ptr [rsp + 0x46]
003CAFDC  8B 74 24 4C                     mov esi, dword ptr [rsp + 0x4c]
003CAFE0  4C 8B 54 24 78                  mov r10, qword ptr [rsp + 0x78]
003CAFE5  45 33 DB                        xor r11d, r11d
003CAFE8  E9 2E FD FF FF                  jmp 0x1403cad1b
003CAFED  41 83 CE 02                     or r14d, 2
003CAFF1  44 89 74 24 54                  mov dword ptr [rsp + 0x54], r14d
003CAFF6  E9 0B FB FF FF                  jmp 0x1403cab06
003CAFFB  85 D2                           test edx, edx
003CAFFD  41 8B C1                        mov eax, r9d
003CB000  75 03                           jne 0x1403cb005
003CB002  41 8B C4                        mov eax, r12d
003CB005  41 2B C5                        sub eax, r13d
003CB008  41 0B C5                        or eax, r13d
003CB00B  A8 3F                           test al, 0x3f
003CB00D  75 22                           jne 0x1403cb031
003CB00F  41 83 CE 04                     or r14d, 4
003CB013  44 89 74 24 54                  mov dword ptr [rsp + 0x54], r14d
003CB018  44 38 5C 24 40                  cmp byte ptr [rsp + 0x40], r11b
003CB01D  0F 84 ED FA FF FF               je 0x1403cab10
003CB023  41 83 CE 08                     or r14d, 8
003CB027  44 89 74 24 54                  mov dword ptr [rsp + 0x54], r14d
003CB02C  E9 DF FA FF FF                  jmp 0x1403cab10
003CB031  41 83 E6 F3                     and r14d, 0xfffffff3
003CB035  44 89 74 24 54                  mov dword ptr [rsp + 0x54], r14d
003CB03A  41 8A C0                        mov al, r8b
003CB03D  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
003CB041  88 44 24 43                     mov byte ptr [rsp + 0x43], al
003CB045  E9 C6 FA FF FF                  jmp 0x1403cab10
003CB04A  8B CE                           mov ecx, esi
003CB04C  E8 3F 23 EA FF                  call 0x14026d390
003CB051  B9 E8 00 00 C0                  mov ecx, 0xc00000e8
003CB056  84 C0                           test al, al
003CB058  0F 45 CE                        cmovne ecx, esi
003CB05B  E8 F0 B9 F2 FF                  call 0x1402f6a50
003CB060  41 8B CF                        mov ecx, r15d
003CB063  E8 E8 B9 F2 FF                  call 0x1402f6a50
003CB068  45 8B C4                        mov r8d, r12d
003CB06B  45 85 FF                        test r15d, r15d
003CB06E  B8 00 10 00 00                  mov eax, 0x1000
003CB073  44 0F 45 C0                     cmovne r8d, eax
003CB077  48 8D 84 24 94 00 00 00         lea rax, [rsp + 0x94]
003CB07F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003CB084  41 B9 01 00 00 00               mov r9d, 1
003CB08A  48 8D 94 24 D0 00 00 00         lea rdx, [rsp + 0xd0]
003CB092  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
003CB097  E8 1C 15 00 00                  call 0x1403cc5b8
003CB09C  48 8B D0                        mov rdx, rax
003CB09F  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
003CB0A7  45 33 DB                        xor r11d, r11d
003CB0AA  48 85 C0                        test rax, rax
003CB0AD  75 0C                           jne 0x1403cb0bb
003CB0AF  8B 8C 24 94 00 00 00            mov ecx, dword ptr [rsp + 0x94]
003CB0B6  E8 95 B9 F2 FF                  call 0x1402f6a50
003CB0BB  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
003CB0BF  E9 B2 FC FF FF                  jmp 0x1403cad76
003CB0C4  48 8B CE                        mov rcx, rsi
003CB0C7  E8 14 3E ED FF                  call 0x14029eee0
003CB0CC  48 8B CE                        mov rcx, rsi
003CB0CF  E8 AC 39 ED FF                  call 0x14029ea80
003CB0D4  45 33 DB                        xor r11d, r11d
003CB0D7  4C 89 9C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r11
003CB0DF  45 8D 43 01                     lea r8d, [r11 + 1]
003CB0E3  E9 45 FD FF FF                  jmp 0x1403cae2d
003CB0E8  44 38 5C 24 43                  cmp byte ptr [rsp + 0x43], r11b
003CB0ED  0F 84 2A FB FF FF               je 0x1403cac1d
003CB0F3  E9 B1 FD FF FF                  jmp 0x1403caea9
003CB0F8  44 8B A4 24 88 00 00 00         mov r12d, dword ptr [rsp + 0x88]
003CB100  41 8A C4                        mov al, r12b
003CB103  22 C3                           and al, bl
003CB105  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
003CB10D  88 81 AC 05 00 00               mov byte ptr [rcx + 0x5ac], al
003CB113  41 D1 EC                        shr r12d, 1
003CB116  44 89 A1 98 05 00 00            mov dword ptr [rcx + 0x598], r12d
003CB11D  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
003CB125  48 85 C9                        test rcx, rcx
003CB128  0F 85 98 01 00 00               jne 0x1403cb2c6
003CB12E  44 38 5C 24 41                  cmp byte ptr [rsp + 0x41], r11b
003CB133  0F 85 5E 02 00 00               jne 0x1403cb397
003CB139  8B 0D 2D F7 A3 00               mov ecx, dword ptr [rip + 0xa3f72d]
003CB13F  41 83 CE FF                     or r14d, 0xffffffff
003CB143  41 3B CE                        cmp ecx, r14d
003CB146  75 26                           jne 0x1403cb16e
003CB148  44 38 5C 24 48                  cmp byte ptr [rsp + 0x48], r11b
003CB14D  75 3D                           jne 0x1403cb18c
003CB14F  44 38 5C 24 45                  cmp byte ptr [rsp + 0x45], r11b
003CB154  75 36                           jne 0x1403cb18c
003CB156  8A 44 24 4A                     mov al, byte ptr [rsp + 0x4a]
003CB15A  48 81 C4 40 01 00 00            add rsp, 0x140
003CB161  41 5F                           pop r15
003CB163  41 5E                           pop r14
003CB165  41 5D                           pop r13
003CB167  41 5C                           pop r12
003CB169  5F                              pop rdi
003CB16A  5E                              pop rsi
003CB16B  5B                              pop rbx
003CB16C  C3                              ret
003CB16D  CC                              int3
003CB16E  41 F7 45 50 00 00 00 01         test dword ptr [r13 + 0x50], 0x1000000
003CB176  74 D0                           je 0x1403cb148
003CB178  40 84 F6                        test sil, sil
003CB17B  75 CB                           jne 0x1403cb148
003CB17D  39 4F 70                        cmp dword ptr [rdi + 0x70], ecx
003CB180  72 C6                           jb 0x1403cb148
003CB182  88 5C 24 44                     mov byte ptr [rsp + 0x44], bl
003CB186  88 5C 24 45                     mov byte ptr [rsp + 0x45], bl
003CB18A  EB BC                           jmp 0x1403cb148
003CB18C  41 8B DB                        mov ebx, r11d
003CB18F  89 9C 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], ebx
003CB196  40 84 F6                        test sil, sil
003CB199  0F 85 CF 00 00 00               jne 0x1403cb26e
003CB19F  45 8B C3                        mov r8d, r11d
003CB1A2  8A 44 24 44                     mov al, byte ptr [rsp + 0x44]
003CB1A6  84 C0                           test al, al
003CB1A8  44 0F 44 84 24 8C 00 00 00      cmove r8d, dword ptr [rsp + 0x8c]
003CB1B1  49 8B D3                        mov rdx, r11
003CB1B4  48 0F 44 94 24 90 01 00 00      cmove rdx, qword ptr [rsp + 0x190]
003CB1BD  4C 89 5C 24 30                  mov qword ptr [rsp + 0x30], r11
003CB1C2  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
003CB1CA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
003CB1CF  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
003CB1D4  45 33 C9                        xor r9d, r9d
003CB1D7  49 8B 4D 28                     mov rcx, qword ptr [r13 + 0x28]
003CB1DB  E8 60 FE F8 FF                  call 0x14035b040
003CB1E0  8B 9C 24 A0 00 00 00            mov ebx, dword ptr [rsp + 0xa0]
003CB1E7  45 33 DB                        xor r11d, r11d
003CB1EA  44 38 5C 24 49                  cmp byte ptr [rsp + 0x49], r11b
003CB1EF  74 37                           je 0x1403cb228
003CB1F1  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
003CB1F9  48 81 C1 00 03 00 00            add rcx, 0x300
003CB200  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
003CB208  E8 93 A5 EA FF                  call 0x1402757a0
003CB20D  44 01 B7 0C 02 00 00            add dword ptr [rdi + 0x20c], r14d
003CB214  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
003CB21C  E8 BF 7A F7 FF                  call 0x140342ce0
003CB221  8B 9C 24 A0 00 00 00            mov ebx, dword ptr [rsp + 0xa0]
003CB228  85 DB                           test ebx, ebx
003CB22A  0F 89 26 FF FF FF               jns 0x1403cb156
003CB230  8B CB                           mov ecx, ebx
003CB232  E8 59 21 EA FF                  call 0x14026d390
003CB237  B9 E9 00 00 C0                  mov ecx, 0xc00000e9
003CB23C  84 C0                           test al, al
003CB23E  0F 45 CB                        cmovne ecx, ebx
003CB241  E8 0A B8 F2 FF                  call 0x1402f6a50
003CB246  CC                              int3
003CB247  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
003CB24F  49 8B 4C 24 28                  mov rcx, qword ptr [r12 + 0x28]
003CB254  E8 4B ED FF FF                  call 0x1403c9fa4
003CB259  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
003CB261  E8 12 E7 F7 FF                  call 0x140349978
003CB266  45 33 DB                        xor r11d, r11d
003CB269  E9 43 F7 FF FF                  jmp 0x1403ca9b1
003CB26E  F7 87 98 00 00 00 00 00 00 40   test dword ptr [rdi + 0x98], 0x40000000
003CB278  0F 84 21 FF FF FF               je 0x1403cb19f
003CB27E  E9 67 FF FF FF                  jmp 0x1403cb1ea
003CB283  49 8D 8F 00 03 00 00            lea rcx, [r15 + 0x300]
003CB28A  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
003CB292  E8 09 A5 EA FF                  call 0x1402757a0
003CB297  8B 87 98 00 00 00               mov eax, dword ptr [rdi + 0x98]
003CB29D  A8 20                           test al, 0x20
003CB29F  0F 85 8A 00 00 00               jne 0x1403cb32f
003CB2A5  B8 01 00 00 00                  mov eax, 1
003CB2AA  01 87 0C 02 00 00               add dword ptr [rdi + 0x20c], eax
003CB2B0  88 44 24 49                     mov byte ptr [rsp + 0x49], al
003CB2B4  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
003CB2BC  E8 1F 7A F7 FF                  call 0x140342ce0
003CB2C1  E9 A4 F6 FF FF                  jmp 0x1403ca96a
003CB2C6  48 8B 59 08                     mov rbx, qword ptr [rcx + 8]
003CB2CA  83 C8 FF                        or eax, 0xffffffff
003CB2CD  F0 0F C1 41 10                  lock xadd dword ptr [rcx + 0x10], eax
003CB2D2  FF C8                           dec eax
003CB2D4  66 85 C0                        test ax, ax
003CB2D7  75 20                           jne 0x1403cb2f9
003CB2D9  48 8B 8B C0 00 00 00            mov rcx, qword ptr [rbx + 0xc0]
003CB2E0  48 85 C9                        test rcx, rcx
003CB2E3  74 0D                           je 0x1403cb2f2
003CB2E5  45 33 C0                        xor r8d, r8d
003CB2E8  33 D2                           xor edx, edx
003CB2EA  E8 21 40 F7 FF                  call 0x14033f310
003CB2EF  45 33 DB                        xor r11d, r11d
003CB2F2  F0 FF 8B 28 02 00 00            lock dec dword ptr [rbx + 0x228]
003CB2F9  BB 01 00 00 00                  mov ebx, 1
003CB2FE  E9 2B FE FF FF                  jmp 0x1403cb12e
003CB303  45 84 ED                        test r13b, r13b
003CB306  0F 84 2A F6 FF FF               je 0x1403ca936
003CB30C  33 C9                           xor ecx, ecx
003CB30E  E8 CD 34 FB FF                  call 0x14037e7e0
003CB313  48 8B 8C 24 C8 01 00 00         mov rcx, qword ptr [rsp + 0x1c8]
003CB31B  48 89 01                        mov qword ptr [rcx], rax
003CB31E  E9 13 F6 FF FF                  jmp 0x1403ca936
003CB323  45 84 FF                        test r15b, r15b
003CB326  75 DB                           jne 0x1403cb303
003CB328  32 C0                           xor al, al
003CB32A  E9 2B FE FF FF                  jmp 0x1403cb15a
003CB32F  49 8D 8F 40 03 00 00            lea rcx, [r15 + 0x340]
003CB336  48 8D 94 24 18 01 00 00         lea rdx, [rsp + 0x118]
003CB33E  E8 FD A3 EA FF                  call 0x140275740
003CB343  48 8B 9F F8 01 00 00            mov rbx, qword ptr [rdi + 0x1f8]
003CB34A  33 D2                           xor edx, edx
003CB34C  48 85 DB                        test rbx, rbx
003CB34F  0F 85 09 D2 31 00               jne 0x1406e855e
003CB355  48 8D 8C 24 18 01 00 00         lea rcx, [rsp + 0x118]
003CB35D  E8 4E BE E4 FF                  call 0x1402171b0
003CB362  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
003CB36A  E8 71 79 F7 FF                  call 0x140342ce0
003CB36F  4C 8D 05 E2 F4 A3 00            lea r8, [rip + 0xa3f4e2]
003CB376  33 D2                           xor edx, edx
003CB378  33 C9                           xor ecx, ecx
003CB37A  E8 D1 E1 E3 FF                  call 0x140209550
003CB37F  B9 D8 00 00 C0                  mov ecx, 0xc00000d8
003CB384  E8 C7 B6 F2 FF                  call 0x1402f6a50
003CB389  CC                              int3
003CB38A  48 8B CB                        mov rcx, rbx
003CB38D  E8 AA BE F8 FF                  call 0x14035723c
003CB392  E9 DC F5 FF FF                  jmp 0x1403ca973
003CB397  44 8B 44 24 58                  mov r8d, dword ptr [rsp + 0x58]
003CB39C  45 85 C0                        test r8d, r8d
003CB39F  0F 84 94 FD FF FF               je 0x1403cb139
003CB3A5  4D 8B CF                        mov r9, r15
003CB3A8  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
003CB3AD  48 8B CF                        mov rcx, rdi
003CB3B0  E8 D3 02 00 00                  call 0x1403cb688
003CB3B5  45 33 DB                        xor r11d, r11d
003CB3B8  E9 7C FD FF FF                  jmp 0x1403cb139
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcMapAndCopyInToCache(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned __int8 a5, __int64 a6, __int64 a7, unsigned __int8 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m104;
    unsigned int v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned int v_stack_m114;
    unsigned int v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned int v_stack_m124;
    unsigned __int8 v_stack_m127;
    unsigned __int8 v_stack_m128;
    unsigned int v_stack_m12C;
    unsigned __int8 v_stack_m12E;
    unsigned __int8 v_stack_m12F;
    unsigned __int8 v_stack_m130;
    unsigned __int8 v_stack_m131;
    unsigned __int8 v_stack_m132;
    unsigned __int8 v_stack_m133;
    unsigned __int8 v_stack_m134;
    unsigned __int8 v_stack_m135;
    unsigned __int8 v_stack_m136;
    unsigned __int8 v_stack_m137;
    unsigned __int8 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned int v_stack_mE8;
    unsigned int v_stack_mEC;
    unsigned int v_stack_mF0;
    unsigned int v_stack_mF4;
    unsigned int v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p190;
    unsigned int v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int8 v_stack_p44;
    unsigned __int8 v_stack_p45;
    unsigned __int64 v_stack_p48;
    unsigned __int8 v_stack_p49;
    unsigned int v_stack_p58;
    unsigned __int64 v_stack_p68;
    unsigned int v_stack_p8C;
    unsigned int v_stack_pA0;
    unsigned __int64 v_stack_pC8;
    unsigned __int64 v_stack_pE0;

    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (320);
    v_stack_mEC = (unsigned int)((unsigned int)(a4));
    a2 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_mD8 = v_xmm0;
    v_rsi = (unsigned __int8)((*(unsigned __int8 *)(a6 + 80)) >> (4));
    v_rsi = (unsigned __int8)((v_rsi) & ((unsigned __int8)(a2 + 1)));
    v_stack_m138 = (unsigned __int8)(v_rsi);
    v_stack_mB8 = (unsigned int)((unsigned int)(a4));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) & (0xFFFULL));
    v_stack_mF8 = (unsigned int)(result);
    *(unsigned __int64 *)(v_rsp - 224) = 0;
    v_stack_mC8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m124 = 0;
    v_stack_m12F = 0;
    v_stack_m134 = 0;
    *(unsigned __int64 *)(v_rsp - 176) = 0;
    v_stack_m131 = (unsigned __int8)(a2 + 1);
    v_stack_m137 = 0;
    v_stack_m133 = 0;
    result = 0;
    v_stack_m98 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 136) = 0;
    *(unsigned __int64 *)(v_rsp - 96) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 80) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 152))) & ((unsigned int)((unsigned int)(0x1000ULL))));
    v_stack_m108 = (unsigned int)(result);
    v_stack_m110 = *(unsigned __int64 *)(a3);
    v_stack_mF0 = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432)) * 2);
    v_stack_mBC = (unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432)) * 2);
    v_stack_m130 = (unsigned __int8)(v_rsi);
    result = *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1452) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1432)) * 2;
    v_r13 = (unsigned __int8)(v_rsi);
    if ((unsigned __int8)(v_rsi) == 0) {
        a3 = a1;
        a2 = *(unsigned int *)(v_rsp + 32);
        a1 = a6;
        result = CcForceWriteThrough(a1, a2, a3, a2 + 1);
        v_r13 = (unsigned __int8)(result);
        v_stack_m130 = (unsigned __int8)(result);
    }
    if ((unsigned __int8)(v_r13) != 0) goto loc_003CB323;
loc_003CA936:
    result = (unsigned __int8)(-(a8));
    result = (unsigned int)((result) & (0xFFFFFFFEULL));
    result = (unsigned int)((result) + (6));
    v_stack_mE8 = (unsigned int)(result);
    v_stack_m70 = *(unsigned __int64 *)(a1 + 536);
    v_stack_m68 = *(unsigned __int64 *)(a1 + 536);
    if ((unsigned __int8)(v_rsi) != 0) goto loc_003CB283;
loc_003CA96A:
    if (0 != 0) goto loc_003CB38A;
loc_003CA973:
    v_r14 = 0;
    v_r15 = a9;
    if (a9 == 0) {
        v_r15 = *(unsigned __int64 *)(gs_base + (0 + 392));
        v_stack_p48 = v_r15;
        v_r14 = v_stack_m124;
    }
    result = IoReferenceIoAttributionFromThread(v_r15, v_stack_mB0, a3, a2 + 1);
    v_r11 = 0;
    if (!sign_flag) goto loc_003CB247;
loc_003CA9B1:
loc_003CA9B9:
    if ((unsigned int)((unsigned int)(v_stack_p20)) != 0) goto loc_003CA9D7;
    v_stack_m12E = 1;
    v_stack_m137 = 0;
    goto loc_003CB0F8;
loc_003CA9D7:
    v_stack_m135 = 0;
    result = (unsigned int)(a5);
    if (v_stack_m108 != 0) { result = 0; }
    v_stack_p28 = (unsigned int)(result);
    v_stack_m120 = 0;
    v_stack_m150 = 0;
    v_stack_m158 = 0;
    result = CcGetVirtualAddress(a1, v_stack_m110, v_stack_mE0, v_stack_m118);
    v_stack_m100 = result;
    a2 = (unsigned int)(v_stack_m118);
    if (((unsigned int)((unsigned int)(v_stack_m118))) > 1) { a2 = 1; }
    v_stack_m118 = (unsigned int)(a2);
    v_stack_m120 = (unsigned int)(a2);
    v_r10 = (result) - ((unsigned int)(v_stack_mF8));
    v_stack_m100 = v_r10;
    v_stack_m104 = (unsigned int)(a2 + (unsigned int)(v_stack_mF8) * 1);
    v_stack_m118 = (unsigned int)(a2 + (unsigned int)(v_stack_mF8) * 1);
    v_stack_mF4 = 1;
    v_stack_mA0 = v_stack_m110;
    v_rbx = (unsigned int)((v_stack_m110) - ((unsigned int)((unsigned int)(v_stack_mF8))));
    v_stack_mA0 = (unsigned int)(v_rbx);
    v_r11 = 0;
    v_stack_m137 = 0;
    v_stack_m12C = 0;
    v_stack_m135 = 0;
loc_003CAA9E:
    v_stack_m136 = 0;
    v_stack_mC0 = 0;
    v_stack_m131 = 1;
    a2 = (((unsigned int)((unsigned int)((unsigned int)(a2 + (unsigned int)(v_stack_mF8) * 1)))) > ((unsigned int)((unsigned int)(0x1000ULL)))) ? 1 : 0;
    v_stack_m11C = (unsigned int)(a2);
    v_stack_m80 = (unsigned int)(a2);
    v_stack_m114 = 0;
    if ((((unsigned int)((unsigned int)(a5))) & (1)) == 0) goto loc_003CACA5;
    if (v_stack_mA0 >= (*(unsigned __int64 *)(a7))) {
        v_r14 = (unsigned int)((v_r14) | (1));
        v_stack_m124 = (unsigned int)(v_r14);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 152)))) & (64)) != 0) goto loc_003CAFED;
loc_003CAB06:
    if (condition_is_below) goto loc_003CAFFB;
loc_003CAB10:
    v_stack_m136 = 0;
    result = (unsigned int)((unsigned int)((unsigned int)(0x1000ULL)));
    if ((unsigned int)(a2) == 0) {
        result = (unsigned int)(a2 + (unsigned int)(v_stack_mF8) * 1);
    }
    result = (unsigned int)((result) - ((unsigned int)((unsigned int)(v_stack_mF8))));
    v_stack_m150 = v_stack_m136;
    v_stack_m158 = (unsigned int)(v_r14);
    result = CcWrapperMmCopyToCachedPage(v_r10, v_stack_p10, (unsigned int)((unsigned int)((unsigned int)(v_stack_mF8))), (unsigned int)((unsigned int)(result)));
    v_stack_m114 = (unsigned int)(result);
    v_r11 = 0;
    if (sign_flag) goto loc_003CB04A;
    v_stack_m137 = (unsigned __int8)(v_r11 + 1);
    if ((unsigned __int8)((unsigned int)(v_stack_m12C)) == 0) goto loc_003CAF88;
loc_003CAB6E:
loc_003CAB73:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x1000ULL)))) - ((unsigned int)((unsigned int)(v_stack_mF8))));
    v_stack_mF8 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m11C)) != 0) goto loc_003CAC5B;
    v_stack_m137 = 0;
    a1 = (unsigned int)((v_r10) | (0xFFFFFFFFULL));
    a1 = (unsigned int)((a1) - 1);
    if ((unsigned __int16)(a1) != 0) goto loc_003CABDB;
    result = v_stack_mE0;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE0 + 8) + 192) != 0) {
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mE0 + 8) + 192), a2, a3, (unsigned int)(0x1000ULL));
        v_r11 = 0;
    }
loc_003CABDB:
    v_stack_mE0 = 0;
    result = CcSetDirtyInMask(a1, v_stack_m110, (unsigned int)(v_stack_m120), a9);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 152))) & (0x40000000ULL));
    if (condition_is_equal) goto loc_003CAE8D;
loc_003CAC12:
    v_r11 = 0;
    if ((unsigned int)(a1) != 0) goto loc_003CB0E8;
loc_003CAC1D:
loc_003CAC2A:
    if (v_stack_p20 < ((unsigned int)((unsigned int)(0x1000ULL)))) goto loc_003CAE5A;
loc_003CAC48:
    goto loc_003CA9B9;
loc_003CAC5B:
    v_r10 = (v_stack_m100) + (a9);
    v_stack_m100 = v_r10;
    v_r12 = (unsigned int)((a2 + (unsigned int)(v_stack_mF8) * 1) + (0xFFFFF000ULL));
    v_stack_m104 = (unsigned int)(v_r12);
    v_stack_m118 = (unsigned int)(v_r12);
    v_rbx = (unsigned int)((*(unsigned __int64 *)(v_stack_mE0 + 8)) + ((unsigned int)(a9)));
    v_stack_mA0 = (unsigned int)(v_rbx);
    if (v_stack_p20 == 0) goto loc_003CAE7A;
loc_003CAC99:
    v_stack_mF4 = 2;
    goto loc_003CAA9E;
loc_003CACA5:
    v_stack_m132 = (unsigned __int8)((unsigned __int8)((unsigned int)(v_stack_m120)));
    v_stack_m128 = 0;
    if ((unsigned int)(v_stack_m110) != 0) goto loc_003CAF25;
loc_003CACBC:
    if (a8 == 0) goto loc_003CAD1B;
    if ((*(unsigned __int64 *)(a10)) != 0) goto loc_003CAD17;
    a3 = (unsigned int)(((unsigned int)(v_stack_mE8)) | (2));
    result = MmCheckCachedPageStates(v_r10, 1, a3, v_stack_m132);
    v_stack_m128 = 1;
    v_r11 = 0;
    if ((unsigned __int8)(v_stack_m132) == 0) goto loc_003CAFCE;
    goto loc_003CAD20;
loc_003CAD17:
loc_003CAD1B:
loc_003CAD20:
    if (1 == 0) goto loc_003CAFA4;
    if ((unsigned __int8)(v_stack_m132) == 0) goto loc_003CAFA4;
loc_003CAD31:
    if (v_stack_m131 == 0) goto loc_003CAF56;
loc_003CAD3C:
    v_stack_mA8 = 0;
    v_stack_m78 = 0;
    v_stack_mE4 = 0;
    if (sign_flag) goto loc_003CB060;
    if ((unsigned int)((unsigned int)(v_stack_m108)) != 0) goto loc_003CB068;
loc_003CAD76:
    a2 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m108)) == 0) { a2 = v_stack_m100; }
    a2 = (a2) + ((unsigned int)((unsigned int)(a6)));
    if ((unsigned int)((unsigned int)(v_stack_m11C)) != 0) goto loc_003CADE1;
loc_003CAD8C:
    a4 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m104)))) - ((unsigned int)(a6)));
    v_stack_m136 = 0;
    v_stack_m150 = v_stack_m136;
    v_stack_m158 = (unsigned __int8)(v_stack_m127);
    result = CcCopyToCacheHelper(a1, a2, v_stack_p10, a4);
    v_stack_m137 = 1;
    v_r11 = 0;
    if ((unsigned __int8)((unsigned int)(v_stack_m12C)) != 0) goto loc_003CADE9;
    v_rsi = (unsigned __int8)((unsigned int)(v_stack_m12C));
    if (v_stack_m136 != 0) { v_rsi = 1; }
    v_stack_m12C = (unsigned int)(v_rsi);
    v_stack_m135 = (unsigned __int8)(v_rsi);
    goto loc_003CADE9;
loc_003CADE1:
    goto loc_003CAD8C;
loc_003CADE9:
    goto loc_003CAE1C;
loc_003CAE1C:
    if (v_stack_mA8 != 0) goto loc_003CB0C4;
loc_003CAE2D:
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_mF0))) & (1));
    *(unsigned __int8 *)(v_stack_mC8 + 1452) = (unsigned __int8)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mF0)))) >> (1));
    *(unsigned int *)(v_stack_mC8 + 1432) = (unsigned int)(result);
    goto loc_003CAB73;
loc_003CAE5A:
    result = (unsigned __int8)((a5) & (4));
    result = (unsigned __int8)(-(result));
    result = (unsigned int)((result) & (a5));
    v_stack_p28 = (unsigned int)(result);
    goto loc_003CAC48;
loc_003CAE7A:
    result = 4;
    if (((unsigned int)(v_stack_mC8)) > ((unsigned int)((unsigned int)(0x1000ULL)))) { result = (unsigned int)(4 - 2); }
    goto loc_003CAC99;
loc_003CAE8D:
    result = (unsigned int)(((unsigned int)(v_stack_mEC)) - (v_stack_p20));
    if (((unsigned int)(result)) <= 0x1000000ULL) goto loc_003CAC12;
    v_r11 = 0;
loc_003CAEA9:
    if ((*(unsigned __int64 *)(a10)) == 0) {
        a1 = 0;
        result = KeQueryPerformanceCounter(a1, 4 - 2, 1, (unsigned int)(0x1000ULL));
        *(unsigned __int64 *)(a10) = result;
        v_r11 = 0;
    }
    v_stack_m148 = 0;
    v_stack_m150 = v_stack_mD8;
    v_stack_m158 = (unsigned __int8)(v_stack_m138);
    a4 = 0;
    result = CcFlushCachePriv(*(unsigned __int64 *)(a6 + 40), v_stack_m110, (unsigned int)(v_stack_m120), a4);
    v_r11 = 0;
    if (!sign_flag) goto loc_003CAC2A;
    result = FsRtlIsNtstatusExpected((unsigned int)((unsigned int)((unsigned int)(v_stack_mD8))), v_stack_m110, (unsigned int)(v_stack_m120), a4);
    a1 = (unsigned int)(0xC00000E9ULL);
    if ((unsigned __int8)(result) != 0) { a1 = (unsigned int)((unsigned int)(v_stack_mD8)); }
    result = RtlRaiseStatus(a1, v_stack_m110, (unsigned int)(v_stack_m120), a4);
loc_003CAF25:
    if ((((unsigned __int8)(a1)) & (4)) == 0) goto loc_003CACBC;
    *(unsigned __int8 *)(v_stack_mC8 + 1452) = (unsigned __int8)((unsigned int)(v_stack_m120));
    if ((*(unsigned int *)(v_stack_mC8 + 1432)) >= ((unsigned int)((unsigned int)(v_stack_m120)))) goto loc_003CACBC;
    *(unsigned int *)(v_stack_mC8 + 1432) = (unsigned int)((unsigned int)(v_stack_m120));
    goto loc_003CACBC;
loc_003CAF56:
    if (a8 != 0) goto loc_003CAD3C;
    v_stack_m12E = 0;
    goto loc_003CB0F8;
loc_003CAF88:
    if (v_stack_m136 == 0) goto loc_003CAB6E;
    v_stack_m12C = (unsigned int)((unsigned __int8)((unsigned int)(v_stack_m120)));
    v_stack_m135 = (unsigned __int8)((unsigned int)(v_stack_m120));
    goto loc_003CAB6E;
loc_003CAFA4:
    result = MmCheckCachedPageStates(v_stack_m100, v_stack_mC8, (unsigned int)(v_stack_mE8), v_stack_m131);
    v_stack_mC0 = (unsigned int)(result);
    v_r11 = 0;
    goto loc_003CAD31;
loc_003CAFCE:
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, v_stack_mC8, (unsigned int)(v_stack_mE8), v_stack_m131);
    *(unsigned __int64 *)((unsigned __int8)((unsigned int)(v_stack_m120))) = result;
    v_r11 = 0;
    goto loc_003CAD1B;
loc_003CAFED:
    v_r14 = (unsigned int)(((unsigned int)(v_stack_m124)) | (2));
    v_stack_m124 = (unsigned int)(v_r14);
    goto loc_003CAB06;
loc_003CAFFB:
    result = (unsigned int)((unsigned int)(v_stack_m131));
    if ((unsigned int)(v_stack_mC8) == 0) {
        result = (unsigned int)((unsigned int)(v_stack_m104));
    }
    result = (unsigned int)((result) - ((unsigned int)(a6)));
    result = (unsigned int)((result) | ((unsigned int)(a6)));
    if ((((unsigned __int8)(result)) & (63)) != 0) goto loc_003CB031;
    v_r14 = (unsigned int)((v_r14) | (4));
    v_stack_m124 = (unsigned int)(v_r14);
    if (v_stack_m138 == 0) goto loc_003CAB10;
    v_r14 = (unsigned int)((v_r14) | (8));
    v_stack_m124 = (unsigned int)(v_r14);
    goto loc_003CAB10;
loc_003CB031:
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFF3ULL));
    v_stack_m124 = (unsigned int)(v_r14);
    v_stack_m12C = (unsigned int)((unsigned __int8)((unsigned int)(v_stack_mE8)));
    v_stack_m135 = (unsigned __int8)((unsigned __int8)((unsigned int)(v_stack_mE8)));
    goto loc_003CAB10;
loc_003CB04A:
    result = FsRtlIsNtstatusExpected((unsigned int)((unsigned int)((unsigned int)(v_stack_m12C))), v_stack_mC8, (unsigned int)(v_stack_mE8), v_stack_m131);
    a1 = (unsigned int)(0xC00000E8ULL);
    if ((unsigned __int8)(result) != 0) { a1 = (unsigned int)((unsigned int)(v_stack_m12C)); }
    result = RtlRaiseStatus(a1, v_stack_mC8, (unsigned int)(v_stack_mE8), v_stack_m131);
loc_003CB060:
    result = RtlRaiseStatus((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_mC8, (unsigned int)(v_stack_mE8), v_stack_m131);
loc_003CB068:
    a3 = (unsigned int)((unsigned int)((unsigned int)(v_stack_m104)));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) { a3 = (unsigned int)((unsigned int)(0x1000ULL)); }
    v_stack_m158 = v_stack_mE4;
    result = CcLockSystemCacheBuffer(v_stack_m100, v_stack_mA8, a3, 1);
    v_stack_m78 = result;
    v_r11 = 0;
    if (result == 0) {
        a1 = v_stack_mE4;
        result = RtlRaiseStatus(a1, result, a3, 1);
    }
    goto loc_003CAD76;
loc_003CB0C4:
    result = MmUnlockPages((unsigned int)(v_stack_m12C), result, a3, 1);
    result = IoFreeMdl((unsigned int)(v_stack_m12C), result, a3, 1);
    v_r11 = 0;
    v_stack_mA8 = 0;
    goto loc_003CAE2D;
loc_003CB0E8:
    if (v_stack_m135 == 0) goto loc_003CAC1D;
    goto loc_003CAEA9;
loc_003CB0F8:
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_mF0))) & (1));
    *(unsigned __int8 *)(v_stack_mC8 + 1452) = (unsigned __int8)(result);
    v_r12 = (unsigned int)(((unsigned int)(v_stack_mF0)) >> (1));
    *(unsigned int *)(v_stack_mC8 + 1432) = (unsigned int)(v_r12);
    if (v_stack_mE0 != 0) goto loc_003CB2C6;
loc_003CB12E:
    if (v_stack_m137 != 0) goto loc_003CB397;
loc_003CB139:
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10745645)))) != ((unsigned int)(v_r14))) goto loc_003CB16E;
loc_003CB148:
    if (v_stack_m130 != 0) goto loc_003CB18C;
    if (v_stack_m133 != 0) goto loc_003CB18C;
loc_003CB156:
loc_003CB15A:
    v_rsp = (v_rsp) + (320);
    return v_stack_m12E;
loc_003CB16E:
    if (((*(unsigned int *)(a6 + 80)) & (0x1000000ULL)) == 0) goto loc_003CB148;
    if ((unsigned __int8)((unsigned int)(v_stack_m12C)) != 0) goto loc_003CB148;
    if ((*(unsigned int *)(a1 + 112)) < ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10745645))))) goto loc_003CB148;
    v_stack_p44 = 1;
    v_stack_p45 = 1;
    goto loc_003CB148;
loc_003CB18C:
    v_stack_pA0 = 0;
    if ((unsigned __int8)((unsigned int)(v_stack_m12C)) != 0) goto loc_003CB26E;
loc_003CB19F:
    a3 = 0;
    if ((unsigned __int8)(v_stack_p44) == 0) { a3 = v_stack_p8C; }
    a2 = 0;
    if ((unsigned __int8)(v_stack_p44) == 0) { a2 = v_stack_p190; }
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_pA0;
    v_stack_p20 = (unsigned __int8)((unsigned int)(v_stack_m12C));
    a4 = 0;
    result = CcFlushCachePriv(*(unsigned __int64 *)(a6 + 40), a2, a3, a4);
    v_r11 = 0;
loc_003CB1EA:
    v_rbx = (unsigned int)(v_stack_pA0);
    if (v_stack_p49 != 0) {
        a1 = v_stack_p108;
        a1 = (a1) + (768);
        a2 = v_stack_pE0;
        result = KeAcquireInStackQueuedSpinLock(a1, a2, a3, a4);
        a1 = v_stack_pE0;
        result = KeReleaseInStackQueuedSpinLock(a1, a2, a3, a4);
        v_rbx = v_stack_pA0;
    }
    if (!sign_flag) goto loc_003CB156;
    result = FsRtlIsNtstatusExpected((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    a1 = (unsigned int)(0xC00000E9ULL);
    if ((unsigned __int8)(result) != 0) { a1 = (unsigned int)(v_rbx); }
    result = RtlRaiseStatus(a1, a2, a3, a4);
loc_003CB247:
    result = MmUpdateSectionIoAttribution(*(unsigned __int64 *)(v_r12 + 40), v_stack_pC8, a3, a4);
    result = IoDiskIoAttributionDereference(v_stack_pC8, v_stack_pC8, a3, a4);
    v_r11 = 0;
    goto loc_003CA9B1;
loc_003CB26E:
    if (((*(unsigned int *)(a1 + 152)) & (0x40000000ULL)) == 0) goto loc_003CB19F;
    goto loc_003CB1EA;
loc_003CB283:
    result = KeAcquireInStackQueuedSpinLock((unsigned int)((unsigned int)(result)) + 768, v_stack_pE0, a3, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 152)))) & (32)) != 0) goto loc_003CB32F;
    v_stack_p49 = 1;
    result = KeReleaseInStackQueuedSpinLock(v_stack_pE0, v_stack_pE0, a3, a4);
    goto loc_003CA96A;
loc_003CB2C6:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = (unsigned int)((result) - 1);
    if ((unsigned __int16)(result) != 0) goto loc_003CB2F9;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pE0 + 8) + 192) != 0) {
        a3 = 0;
        a2 = 0;
        result = KeSetEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pE0 + 8) + 192), a2, a3, a4);
        v_r11 = 0;
    }
loc_003CB2F9:
    goto loc_003CB12E;
loc_003CB303:
    if ((unsigned __int8)(a6) == 0) goto loc_003CA936;
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, a3, a4);
    *(unsigned __int64 *)(a10) = result;
    goto loc_003CA936;
loc_003CB323:
    if ((unsigned __int8)((unsigned int)((unsigned int)(result))) != 0) goto loc_003CB303;
    result = 0;
    goto loc_003CB15A;
loc_003CB32F:
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel((unsigned int)((unsigned int)(result)) + 832, v_stack_p118, a3, a4);
    a2 = 0;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_p118, a2, a3, a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_pE0, a2, a3, a4);
    a2 = 0;
    a1 = 0;
    result = KeDelayExecutionThread(a1, a2, v_rip + 10745058, a4);
    result = RtlRaiseStatus((unsigned int)(0xC00000D8ULL), a2, v_rip + 10745058, a4);
loc_003CB38A:
    result = CcFreeWorkQueueEntry(*(unsigned __int64 *)(a1 + 504), a2, v_rip + 10745058, a4);
    goto loc_003CA973;
loc_003CB397:
    if ((unsigned int)((unsigned int)(v_stack_p58)) == 0) goto loc_003CB139;
    result = CcSetDirtyInMask(0, v_stack_p68, (unsigned int)(v_stack_p58), (unsigned int)((unsigned int)(result)));
    v_r11 = 0;
    goto loc_003CB139;
}
```

## 5. (Beta) C Style

```c
int64_t CcMapAndCopyInToCache(void *Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, uint8_t Arg5, void *Arg6, void *Arg7, uint8_t Arg8, int64_t Arg9, void *Arg10)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m104;
    uint32_t v_stack_m108;
    uint64_t v_stack_m110;
    uint32_t v_stack_m114;
    uint32_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint32_t v_stack_m124;
    uint8_t v_stack_m127;
    uint8_t v_stack_m128;
    uint32_t v_stack_m12C;
    uint8_t v_stack_m12E;
    uint8_t v_stack_m12F;
    uint8_t v_stack_m130;
    uint8_t v_stack_m131;
    uint8_t v_stack_m132;
    uint8_t v_stack_m133;
    uint8_t v_stack_m134;
    uint8_t v_stack_m135;
    uint8_t v_stack_m136;
    uint8_t v_stack_m137;
    uint8_t v_stack_m138;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint32_t v_stack_m158;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint32_t v_stack_mE8;
    uint32_t v_stack_mEC;
    uint32_t v_stack_mF0;
    uint32_t v_stack_mF4;
    uint32_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p108;
    uint64_t v_stack_p118;
    uint64_t v_stack_p190;
    uint32_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint8_t v_stack_p44;
    uint8_t v_stack_p45;
    uint64_t v_stack_p48;
    uint8_t v_stack_p49;
    uint32_t v_stack_p58;
    uint64_t v_stack_p68;
    uint32_t v_stack_p8C;
    uint32_t v_stack_pA0;
    uint64_t v_stack_pC8;
    uint64_t v_stack_pE0;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(void **)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (320);
    v_stack_mEC = (uint32_t)((uint32_t)(Arg4));
    Arg2 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_mD8 = v_xmm0;
    local_rsi = (uint8_t)((*(uint8_t *)(arg6 + 0x50)) >> (4));
    local_rsi = (uint8_t)((local_rsi) & ((uint8_t)(Arg2 + 1)));
    v_stack_m138 = (uint8_t)(local_rsi);
    v_stack_mB8 = (uint32_t)((uint32_t)(Arg4));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3))) & (0xFFFULL));
    v_stack_mF8 = (uint32_t)(result);
    *(uint64_t *)(local_rsp - 0xE0) = 0;
    v_stack_mC8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m124 = 0;
    v_stack_m12F = 0;
    v_stack_m134 = 0;
    *(uint64_t *)(local_rsp - 0xB0) = 0;
    v_stack_m131 = (uint8_t)(Arg2 + 1);
    v_stack_m137 = 0;
    v_stack_m133 = 0;
    result = 0;
    v_stack_m98 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x88) = 0;
    *(uint64_t *)(local_rsp - 0x60) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x50) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x98))) & ((uint32_t)((uint32_t)(0x1000ULL))));
    v_stack_m108 = (uint32_t)(result);
    v_stack_m110 = *(uint64_t *)(arg3);
    v_stack_mF0 = (uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598)) * 2);
    v_stack_mBC = (uint32_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598)) * 2);
    v_stack_m130 = (uint8_t)(local_rsi);
    result = *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5AC) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x598)) * 2;
    local_r13 = (uint8_t)(local_rsi);
    if ((uint8_t)(local_rsi) == 0) {
        Arg3 = Arg1;
        Arg2 = *(uint32_t *)(local_rsp + 0x20);
        Arg1 = Arg6;
        result = CcForceWriteThrough(Arg1, Arg2, Arg3, Arg2 + 1);
        local_r13 = (uint8_t)(result);
        v_stack_m130 = (uint8_t)(result);
    }
    if ((uint8_t)(local_r13) != 0) goto loc_003CB323;
loc_003CA936:
    result = (uint8_t)(-(Arg8));
    result = (uint32_t)((result) & (0xFFFFFFFEULL));
    result = (uint32_t)((result) + (6));
    v_stack_mE8 = (uint32_t)(result);
    v_stack_m70 = *(uint64_t *)(arg1 + 0x218);
    v_stack_m68 = *(uint64_t *)(arg1 + 0x218);
    if ((uint8_t)(local_rsi) != 0) goto loc_003CB283;
loc_003CA96A:
    if (0 != 0) goto loc_003CB38A;
loc_003CA973:
    local_r14 = 0;
    local_r15 = Arg9;
    if (Arg9 == 0) {
        local_r15 = *(uint64_t *)(gs_base + (0 + 0x188));
        v_stack_p48 = local_r15;
        local_r14 = v_stack_m124;
    }
    result = IoReferenceIoAttributionFromThread(local_r15, v_stack_mB0, Arg3, Arg2 + 1);
    local_r11 = 0;
    if (!sign_flag) goto loc_003CB247;
loc_003CA9B1:
loc_003CA9B9:
    if ((uint32_t)((uint32_t)(v_stack_p20)) != 0) goto loc_003CA9D7;
    v_stack_m12E = 1;
    v_stack_m137 = 0;
    goto loc_003CB0F8;
loc_003CA9D7:
    v_stack_m135 = 0;
    result = (uint32_t)(Arg5);
    if (v_stack_m108 != 0) { result = 0; }
    v_stack_p28 = (uint32_t)(result);
    v_stack_m120 = 0;
    v_stack_m150 = 0;
    v_stack_m158 = 0;
    result = CcGetVirtualAddress(Arg1, v_stack_m110, v_stack_mE0, v_stack_m118);
    v_stack_m100 = result;
    Arg2 = (uint32_t)(v_stack_m118);
    if (((uint32_t)((uint32_t)(v_stack_m118))) > 1) { Arg2 = 1; }
    v_stack_m118 = (uint32_t)(Arg2);
    v_stack_m120 = (uint32_t)(Arg2);
    local_r10 = (result) - ((uint32_t)(v_stack_mF8));
    v_stack_m100 = local_r10;
    v_stack_m104 = (uint32_t)(Arg2 + (uint32_t)(v_stack_mF8) * 1);
    v_stack_m118 = (uint32_t)(Arg2 + (uint32_t)(v_stack_mF8) * 1);
    v_stack_mF4 = 1;
    v_stack_mA0 = v_stack_m110;
    local_rbx = (uint32_t)((v_stack_m110) - ((uint32_t)((uint32_t)(v_stack_mF8))));
    v_stack_mA0 = (uint32_t)(local_rbx);
    local_r11 = 0;
    v_stack_m137 = 0;
    v_stack_m12C = 0;
    v_stack_m135 = 0;
loc_003CAA9E:
    v_stack_m136 = 0;
    v_stack_mC0 = 0;
    v_stack_m131 = 1;
    Arg2 = (((uint32_t)((uint32_t)((uint32_t)(Arg2 + (uint32_t)(v_stack_mF8) * 1)))) > ((uint32_t)((uint32_t)(0x1000ULL)))) ? 1 : 0;
    v_stack_m11C = (uint32_t)(Arg2);
    v_stack_m80 = (uint32_t)(Arg2);
    v_stack_m114 = 0;
    if ((((uint32_t)((uint32_t)(Arg5))) & (1)) == 0) goto loc_003CACA5;
    if (v_stack_mA0 >= (*(uint64_t *)(arg7))) {
        local_r14 = (uint32_t)((local_r14) | (1));
        v_stack_m124 = (uint32_t)(local_r14);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x98)))) & (64)) != 0) goto loc_003CAFED;
loc_003CAB06:
    if (condition_is_below) goto loc_003CAFFB;
loc_003CAB10:
    v_stack_m136 = 0;
    result = (uint32_t)((uint32_t)((uint32_t)(0x1000ULL)));
    if ((uint32_t)(Arg2) == 0) {
        result = (uint32_t)(Arg2 + (uint32_t)(v_stack_mF8) * 1);
    }
    result = (uint32_t)((result) - ((uint32_t)((uint32_t)(v_stack_mF8))));
    v_stack_m150 = v_stack_m136;
    v_stack_m158 = (uint32_t)(local_r14);
    result = CcWrapperMmCopyToCachedPage(local_r10, v_stack_p10, (uint32_t)((uint32_t)((uint32_t)(v_stack_mF8))), (uint32_t)((uint32_t)(result)));
    v_stack_m114 = (uint32_t)(result);
    local_r11 = 0;
    if (sign_flag) goto loc_003CB04A;
    v_stack_m137 = (uint8_t)(local_r11 + 1);
    if ((uint8_t)((uint32_t)(v_stack_m12C)) == 0) goto loc_003CAF88;
loc_003CAB6E:
loc_003CAB73:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x1000ULL)))) - ((uint32_t)((uint32_t)(v_stack_mF8))));
    v_stack_mF8 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m11C)) != 0) goto loc_003CAC5B;
    v_stack_m137 = 0;
    Arg1 = (uint32_t)((local_r10) | (0xFFFFFFFFULL));
    Arg1 = (uint32_t)((Arg1) - 1);
    if ((uint16_t)(Arg1) != 0) goto loc_003CABDB;
    result = v_stack_mE0;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mE0 + 0x8) + 0xC0) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(v_stack_mE0 + 0x8) + 0xC0), Arg2, Arg3, (uint32_t)(0x1000ULL));
        local_r11 = 0;
    }
loc_003CABDB:
    v_stack_mE0 = 0;
    result = CcSetDirtyInMask(Arg1, v_stack_m110, (uint32_t)(v_stack_m120), Arg9);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x98))) & (0x40000000ULL));
    if (condition_is_equal) goto loc_003CAE8D;
loc_003CAC12:
    local_r11 = 0;
    if ((uint32_t)(Arg1) != 0) goto loc_003CB0E8;
loc_003CAC1D:
loc_003CAC2A:
    if (v_stack_p20 < ((uint32_t)((uint32_t)(0x1000ULL)))) goto loc_003CAE5A;
loc_003CAC48:
    goto loc_003CA9B9;
loc_003CAC5B:
    local_r10 = (v_stack_m100) + (Arg9);
    v_stack_m100 = local_r10;
    local_r12 = (uint32_t)((Arg2 + (uint32_t)(v_stack_mF8) * 1) + (0xFFFFF000ULL));
    v_stack_m104 = (uint32_t)(local_r12);
    v_stack_m118 = (uint32_t)(local_r12);
    local_rbx = (uint32_t)((*(uint64_t *)(v_stack_mE0 + 0x8)) + ((uint32_t)(Arg9)));
    v_stack_mA0 = (uint32_t)(local_rbx);
    if (v_stack_p20 == 0) goto loc_003CAE7A;
loc_003CAC99:
    v_stack_mF4 = 2;
    goto loc_003CAA9E;
loc_003CACA5:
    v_stack_m132 = (uint8_t)((uint8_t)((uint32_t)(v_stack_m120)));
    v_stack_m128 = 0;
    if ((uint32_t)(v_stack_m110) != 0) goto loc_003CAF25;
loc_003CACBC:
    if (Arg8 == 0) goto loc_003CAD1B;
    if ((*(uint64_t *)(arg10)) != 0) goto loc_003CAD17;
    Arg3 = (uint32_t)(((uint32_t)(v_stack_mE8)) | (2));
    result = MmCheckCachedPageStates(local_r10, 1, Arg3, v_stack_m132);
    v_stack_m128 = 1;
    local_r11 = 0;
    if ((uint8_t)(v_stack_m132) == 0) goto loc_003CAFCE;
    goto loc_003CAD20;
loc_003CAD17:
loc_003CAD1B:
loc_003CAD20:
    if (1 == 0) goto loc_003CAFA4;
    if ((uint8_t)(v_stack_m132) == 0) goto loc_003CAFA4;
loc_003CAD31:
    if (v_stack_m131 == 0) goto loc_003CAF56;
loc_003CAD3C:
    v_stack_mA8 = 0;
    v_stack_m78 = 0;
    v_stack_mE4 = 0;
    if (sign_flag) goto loc_003CB060;
    if ((uint32_t)((uint32_t)(v_stack_m108)) != 0) goto loc_003CB068;
loc_003CAD76:
    Arg2 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m108)) == 0) { Arg2 = v_stack_m100; }
    Arg2 = (Arg2) + ((uint32_t)((uint32_t)(Arg6)));
    if ((uint32_t)((uint32_t)(v_stack_m11C)) != 0) goto loc_003CADE1;
loc_003CAD8C:
    Arg4 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m104)))) - ((uint32_t)(Arg6)));
    v_stack_m136 = 0;
    v_stack_m150 = v_stack_m136;
    v_stack_m158 = (uint8_t)(v_stack_m127);
    result = CcCopyToCacheHelper(Arg1, Arg2, v_stack_p10, Arg4);
    v_stack_m137 = 1;
    local_r11 = 0;
    if ((uint8_t)((uint32_t)(v_stack_m12C)) != 0) goto loc_003CADE9;
    local_rsi = (uint8_t)((uint32_t)(v_stack_m12C));
    if (v_stack_m136 != 0) { local_rsi = 1; }
    v_stack_m12C = (uint32_t)(local_rsi);
    v_stack_m135 = (uint8_t)(local_rsi);
    goto loc_003CADE9;
loc_003CADE1:
    goto loc_003CAD8C;
loc_003CADE9:
    goto loc_003CAE1C;
loc_003CAE1C:
    if (v_stack_mA8 != 0) goto loc_003CB0C4;
loc_003CAE2D:
    result = (uint8_t)(((uint8_t)((uint32_t)(v_stack_mF0))) & (1));
    *(uint8_t *)(v_stack_mC8 + 0x5AC) = (uint8_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mF0)))) >> (1));
    *(uint32_t *)(v_stack_mC8 + 0x598) = (uint32_t)(result);
    goto loc_003CAB73;
loc_003CAE5A:
    result = (uint8_t)((Arg5) & (4));
    result = (uint8_t)(-(result));
    result = (uint32_t)((result) & (Arg5));
    v_stack_p28 = (uint32_t)(result);
    goto loc_003CAC48;
loc_003CAE7A:
    result = 4;
    if (((uint32_t)(v_stack_mC8)) > ((uint32_t)((uint32_t)(0x1000ULL)))) { result = (uint32_t)(4 - 2); }
    goto loc_003CAC99;
loc_003CAE8D:
    result = (uint32_t)(((uint32_t)(v_stack_mEC)) - (v_stack_p20));
    if (((uint32_t)(result)) <= 0x1000000ULL) goto loc_003CAC12;
    local_r11 = 0;
loc_003CAEA9:
    if ((*(uint64_t *)(arg10)) == 0) {
        Arg1 = 0;
        result = KeQueryPerformanceCounter(Arg1, 4 - 2, 1, (uint32_t)(0x1000ULL));
        *(uint64_t *)(arg10) = result;
        local_r11 = 0;
    }
    v_stack_m148 = 0;
    v_stack_m150 = v_stack_mD8;
    v_stack_m158 = (uint8_t)(v_stack_m138);
    Arg4 = 0;
    result = CcFlushCachePriv(*(uint64_t *)(arg6 + 0x28), v_stack_m110, (uint32_t)(v_stack_m120), Arg4);
    local_r11 = 0;
    if (!sign_flag) goto loc_003CAC2A;
    result = FsRtlIsNtstatusExpected((uint32_t)((uint32_t)((uint32_t)(v_stack_mD8))), v_stack_m110, (uint32_t)(v_stack_m120), Arg4);
    Arg1 = (uint32_t)(0xC00000E9ULL);
    if ((uint8_t)(result) != 0) { Arg1 = (uint32_t)((uint32_t)(v_stack_mD8)); }
    result = RtlRaiseStatus(Arg1, v_stack_m110, (uint32_t)(v_stack_m120), Arg4);
loc_003CAF25:
    if ((((uint8_t)(Arg1)) & (4)) == 0) goto loc_003CACBC;
    *(uint8_t *)(v_stack_mC8 + 0x5AC) = (uint8_t)((uint32_t)(v_stack_m120));
    if ((*(uint32_t *)(v_stack_mC8 + 0x598)) >= ((uint32_t)((uint32_t)(v_stack_m120)))) goto loc_003CACBC;
    *(uint32_t *)(v_stack_mC8 + 0x598) = (uint32_t)((uint32_t)(v_stack_m120));
    goto loc_003CACBC;
loc_003CAF56:
    if (Arg8 != 0) goto loc_003CAD3C;
    v_stack_m12E = 0;
    goto loc_003CB0F8;
loc_003CAF88:
    if (v_stack_m136 == 0) goto loc_003CAB6E;
    v_stack_m12C = (uint32_t)((uint8_t)((uint32_t)(v_stack_m120)));
    v_stack_m135 = (uint8_t)((uint32_t)(v_stack_m120));
    goto loc_003CAB6E;
loc_003CAFA4:
    result = MmCheckCachedPageStates(v_stack_m100, v_stack_mC8, (uint32_t)(v_stack_mE8), v_stack_m131);
    v_stack_mC0 = (uint32_t)(result);
    local_r11 = 0;
    goto loc_003CAD31;
loc_003CAFCE:
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, v_stack_mC8, (uint32_t)(v_stack_mE8), v_stack_m131);
    *(uint64_t *)((uint8_t)((uint32_t)(v_stack_m120))) = result;
    local_r11 = 0;
    goto loc_003CAD1B;
loc_003CAFED:
    local_r14 = (uint32_t)(((uint32_t)(v_stack_m124)) | (2));
    v_stack_m124 = (uint32_t)(local_r14);
    goto loc_003CAB06;
loc_003CAFFB:
    result = (uint32_t)((uint32_t)(v_stack_m131));
    if ((uint32_t)(v_stack_mC8) == 0) {
        result = (uint32_t)((uint32_t)(v_stack_m104));
    }
    result = (uint32_t)((result) - ((uint32_t)(Arg6)));
    result = (uint32_t)((result) | ((uint32_t)(Arg6)));
    if ((((uint8_t)(result)) & (63)) != 0) goto loc_003CB031;
    local_r14 = (uint32_t)((local_r14) | (4));
    v_stack_m124 = (uint32_t)(local_r14);
    if (v_stack_m138 == 0) goto loc_003CAB10;
    local_r14 = (uint32_t)((local_r14) | (8));
    v_stack_m124 = (uint32_t)(local_r14);
    goto loc_003CAB10;
loc_003CB031:
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFF3ULL));
    v_stack_m124 = (uint32_t)(local_r14);
    v_stack_m12C = (uint32_t)((uint8_t)((uint32_t)(v_stack_mE8)));
    v_stack_m135 = (uint8_t)((uint8_t)((uint32_t)(v_stack_mE8)));
    goto loc_003CAB10;
loc_003CB04A:
    result = FsRtlIsNtstatusExpected((uint32_t)((uint32_t)((uint32_t)(v_stack_m12C))), v_stack_mC8, (uint32_t)(v_stack_mE8), v_stack_m131);
    Arg1 = (uint32_t)(0xC00000E8ULL);
    if ((uint8_t)(result) != 0) { Arg1 = (uint32_t)((uint32_t)(v_stack_m12C)); }
    result = RtlRaiseStatus(Arg1, v_stack_mC8, (uint32_t)(v_stack_mE8), v_stack_m131);
loc_003CB060:
    result = RtlRaiseStatus((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_mC8, (uint32_t)(v_stack_mE8), v_stack_m131);
loc_003CB068:
    Arg3 = (uint32_t)((uint32_t)((uint32_t)(v_stack_m104)));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) { Arg3 = (uint32_t)((uint32_t)(0x1000ULL)); }
    v_stack_m158 = v_stack_mE4;
    result = CcLockSystemCacheBuffer(v_stack_m100, v_stack_mA8, Arg3, 1);
    v_stack_m78 = result;
    local_r11 = 0;
    if (result == 0) {
        Arg1 = v_stack_mE4;
        result = RtlRaiseStatus(Arg1, result, Arg3, 1);
    }
    goto loc_003CAD76;
loc_003CB0C4:
    result = MmUnlockPages((uint32_t)(v_stack_m12C), result, Arg3, 1);
    result = IoFreeMdl((uint32_t)(v_stack_m12C), result, Arg3, 1);
    local_r11 = 0;
    v_stack_mA8 = 0;
    goto loc_003CAE2D;
loc_003CB0E8:
    if (v_stack_m135 == 0) goto loc_003CAC1D;
    goto loc_003CAEA9;
loc_003CB0F8:
    result = (uint8_t)(((uint8_t)((uint32_t)(v_stack_mF0))) & (1));
    *(uint8_t *)(v_stack_mC8 + 0x5AC) = (uint8_t)(result);
    local_r12 = (uint32_t)(((uint32_t)(v_stack_mF0)) >> (1));
    *(uint32_t *)(v_stack_mC8 + 0x598) = (uint32_t)(local_r12);
    if (v_stack_mE0 != 0) goto loc_003CB2C6;
loc_003CB12E:
    if (v_stack_m137 != 0) goto loc_003CB397;
loc_003CB139:
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA3F72D)))) != ((uint32_t)(local_r14))) goto loc_003CB16E;
loc_003CB148:
    if (v_stack_m130 != 0) goto loc_003CB18C;
    if (v_stack_m133 != 0) goto loc_003CB18C;
loc_003CB156:
loc_003CB15A:
    local_rsp = (local_rsp) + (320);
    return v_stack_m12E;
loc_003CB16E:
    if (((*(uint32_t *)(arg6 + 0x50)) & (0x1000000ULL)) == 0) goto loc_003CB148;
    if ((uint8_t)((uint32_t)(v_stack_m12C)) != 0) goto loc_003CB148;
    if ((*(uint32_t *)(arg1 + 0x70)) < ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA3F72D))))) goto loc_003CB148;
    v_stack_p44 = 1;
    v_stack_p45 = 1;
    goto loc_003CB148;
loc_003CB18C:
    v_stack_pA0 = 0;
    if ((uint8_t)((uint32_t)(v_stack_m12C)) != 0) goto loc_003CB26E;
loc_003CB19F:
    Arg3 = 0;
    if ((uint8_t)(v_stack_p44) == 0) { Arg3 = v_stack_p8C; }
    Arg2 = 0;
    if ((uint8_t)(v_stack_p44) == 0) { Arg2 = v_stack_p190; }
    v_stack_p30 = 0;
    v_stack_p28 = v_stack_pA0;
    v_stack_p20 = (uint8_t)((uint32_t)(v_stack_m12C));
    Arg4 = 0;
    result = CcFlushCachePriv(*(uint64_t *)(arg6 + 0x28), Arg2, Arg3, Arg4);
    local_r11 = 0;
loc_003CB1EA:
    local_rbx = (uint32_t)(v_stack_pA0);
    if (v_stack_p49 != 0) {
        Arg1 = v_stack_p108;
        Arg1 = (Arg1) + (768);
        Arg2 = v_stack_pE0;
        result = KeAcquireInStackQueuedSpinLock(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_pE0;
        result = KeReleaseInStackQueuedSpinLock(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_pA0;
    }
    if (!sign_flag) goto loc_003CB156;
    result = FsRtlIsNtstatusExpected((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, Arg4);
    Arg1 = (uint32_t)(0xC00000E9ULL);
    if ((uint8_t)(result) != 0) { Arg1 = (uint32_t)(local_rbx); }
    result = RtlRaiseStatus(Arg1, Arg2, Arg3, Arg4);
loc_003CB247:
    result = MmUpdateSectionIoAttribution(*(uint64_t *)(local_r12 + 0x28), v_stack_pC8, Arg3, Arg4);
    result = IoDiskIoAttributionDereference(v_stack_pC8, v_stack_pC8, Arg3, Arg4);
    local_r11 = 0;
    goto loc_003CA9B1;
loc_003CB26E:
    if (((*(uint32_t *)(arg1 + 0x98)) & (0x40000000ULL)) == 0) goto loc_003CB19F;
    goto loc_003CB1EA;
loc_003CB283:
    result = KeAcquireInStackQueuedSpinLock((uint32_t)((uint32_t)(result)) + 768, v_stack_pE0, Arg3, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x98)))) & (32)) != 0) goto loc_003CB32F;
    v_stack_p49 = 1;
    result = KeReleaseInStackQueuedSpinLock(v_stack_pE0, v_stack_pE0, Arg3, Arg4);
    goto loc_003CA96A;
loc_003CB2C6:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = (uint32_t)((result) - 1);
    if ((uint16_t)(result) != 0) goto loc_003CB2F9;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_pE0 + 0x8) + 0xC0) != 0) {
        Arg3 = 0;
        Arg2 = 0;
        result = KeSetEvent(*(uint64_t *)(*(uint64_t *)(v_stack_pE0 + 0x8) + 0xC0), Arg2, Arg3, Arg4);
        local_r11 = 0;
    }
loc_003CB2F9:
    goto loc_003CB12E;
loc_003CB303:
    if ((uint8_t)(Arg6) == 0) goto loc_003CA936;
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, Arg3, Arg4);
    *(uint64_t *)(arg10) = result;
    goto loc_003CA936;
loc_003CB323:
    if ((uint8_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_003CB303;
    result = 0;
    goto loc_003CB15A;
loc_003CB32F:
    result = KeAcquireInStackQueuedSpinLockAtDpcLevel((uint32_t)((uint32_t)(result)) + 832, v_stack_p118, Arg3, Arg4);
    Arg2 = 0;
    result = KeReleaseInStackQueuedSpinLockFromDpcLevel(v_stack_p118, Arg2, Arg3, Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_pE0, Arg2, Arg3, Arg4);
    Arg2 = 0;
    Arg1 = 0;
    result = KeDelayExecutionThread(Arg1, Arg2, v_rip + 10745058, Arg4);
    result = RtlRaiseStatus((uint32_t)(0xC00000D8ULL), Arg2, v_rip + 10745058, Arg4);
loc_003CB38A:
    result = CcFreeWorkQueueEntry(*(uint64_t *)(arg1 + 0x1F8), Arg2, v_rip + 10745058, Arg4);
    goto loc_003CA973;
loc_003CB397:
    if ((uint32_t)((uint32_t)(v_stack_p58)) == 0) goto loc_003CB139;
    result = CcSetDirtyInMask(0, v_stack_p68, (uint32_t)(v_stack_p58), (uint32_t)((uint32_t)(result)));
    local_r11 = 0;
    goto loc_003CB139;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x70` | `32` | `R` |
| `Arg1` | `+ 0x98` | `32` | `R` |
| `Arg1` | `+ 0x1F8` | `64` | `R` |
| `Arg1` | `+ 0x20C` | `32` | `R/W` |
| `Arg1` | `+ 0x218` | `64` | `R` |
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg6` | `+ 0x28` | `64` | `R` |
| `Arg6` | `+ 0x50` | `8` | `R` |
| `Arg6` | `+ 0x50` | `32` | `R` |
| `Arg7` | `+ 0x0` | `64` | `R` |
| `Arg10` | `+ 0x0` | `64` | `R` |
| `Arg10` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003CA7F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
