# PiCMCreateDevice

- RVA: `0x00ACB824`–`0x00ACBFA0` (길이 `1,916` bytes)
- VA: `0x0000000140ACB824`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BE4EC`
- 디코드: `496`개 명령, `1,916/1,916` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00ACB8BC` → [PiCMCaptureCreateDeviceInputData](PiCMCaptureCreateDeviceInputData_function_00ACBFA8.md) (function, `0x00ACBFA8`)
- `0x00ACB8CF` → [PiAuDoesClientHaveAccess](../96/PiAuDoesClientHaveAccess_function_00962940.md) (function, `0x00962940`)
- `0x00ACB944` → [CmIsRootDevice](../93/CmIsRootDevice_function_009325E4.md) (function, `0x009325E4`)
- `0x00ACB95B` → [PiPnpRtlBeginOperation](../8E/PiPnpRtlBeginOperation_function_008E033C.md) (function, `0x008E033C`)
- `0x00ACB976` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ACB9A8` → [PiCMGenerateDeviceInstance](../73/PiCMGenerateDeviceInstance_function_0073B69C.md) (function, `0x0073B69C`)
- `0x00ACB9CF` → [CmValidateDeviceName](../8F/CmValidateDeviceName_function_008F3CF0.md) (function, `0x008F3CF0`)
- `0x00ACBA00` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (function, `0x0041E1C0`)
- `0x00ACBA3D` → [_CmOpenDeviceRegKey](../8E/_CmOpenDeviceRegKey_function_008EE540.md) (function, `0x008EE540`)
- `0x00ACBA96` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00ACBAC6` → [CmCreateDevice](../8F/CmCreateDevice_function_008FFABC.md) (function, `0x008FFABC`)
- `0x00ACBAE5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00ACBB1C` → [PnpCtxRegSetValue](../99/PnpCtxRegSetValue_function_00991B8C.md) (function, `0x00991B8C`)
- `0x00ACBB27` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00ACBB3B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00ACBB40` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00ACBB65` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00ACBB74` → [PpDevNodeLockTree](../A1/PpDevNodeLockTree_function_00A19310.md) (function, `0x00A19310`)
- `0x00ACBB82` → [PnpDeviceObjectFromDeviceInstanceWithTag](../8E/PnpDeviceObjectFromDeviceInstanceWithTag_function_008E7490.md) (function, `0x008E7490`)
- `0x00ACBBA1` → [PpDevNodeUnlockTree](../A2/PpDevNodeUnlockTree_function_00A21290.md) (function, `0x00A21290`)
- `0x00ACBBAE` → [IopIsRootEnumeratedDeviceObjectActive](../AB/IopIsRootEnumeratedDeviceObjectActive_function_00AB1CB4.md) (function, `0x00AB1CB4`)
- `0x00ACBBC8` → [PiPnpRtlEnsureObjectCached](../72/PiPnpRtlEnsureObjectCached_function_0072F928.md) (function, `0x0072F928`)
- `0x00ACBBEC` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00ACBC19` → [CmCreateDevice](../8F/CmCreateDevice_function_008FFABC.md) (function, `0x008FFABC`)
- `0x00ACBC2F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00ACBC34` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00ACBC69` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00ACBCB4` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00ACBCC9` → [PnpGetDeviceInstanceCsConfigFlags](../A7/PnpGetDeviceInstanceCsConfigFlags_function_00A75D5C.md) (function, `0x00A75D5C`)
- `0x00ACBCF0` → [PiInitializeDevice](../73/PiInitializeDevice_function_0073EC5C.md) (function, `0x0073EC5C`)
- `0x00ACBD25` → [PnpCtxRegQueryValue](../99/PnpCtxRegQueryValue_function_009940FC.md) (function, `0x009940FC`)
- `0x00ACBD4E` → [PnpCtxRegDeleteValue](../8F/PnpCtxRegDeleteValue_function_008FE5E0.md) (function, `0x008FE5E0`)
- `0x00ACBD73` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ACBDC6` → [PiCMReturnBufferResultData](../8E/PiCMReturnBufferResultData_function_008ED6D0.md) (function, `0x008ED6D0`)
- `0x00ACBDD6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00ACBDE8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ACBDFA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ACBE07` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00ACBE18` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00ACBE1D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00ACBE3C` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x00ACBE4C` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (function, `0x00448990`)
- `0x00ACBE5A` → [PiPnpRtlEndOperation](../8E/PiPnpRtlEndOperation_function_008E0518.md) (function, `0x008E0518`)
- `0x00ACBEAD` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00ACBECF` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (function, `0x00463960`)
- `0x00ACBEEA` → [PpDeviceRegistration](../A0/PpDeviceRegistration_function_00A079D4.md) (function, `0x00A079D4`)
- `0x00ACBF0D` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (function, `0x00435A70`)

### Direct callers
- [PiCMHandleIoctl](../8E/PiCMHandleIoctl_function_008EB880.md) at `0x008EC271`

### Static image references
- `0x00ACBA2B` → RVA `0x00E66398` (`.data`; read)
- `0x00ACBA85` → RVA `0x00F8C600` (`.data`; read)
- `0x00ACBB10` → RVA `0x00AFF700` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x00ACB976` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ACBA00` → [RtlStringCchCopyExW](../../text/41/RtlStringCchCopyExW_function_0041E1C0.md) (`PAGE` → `.text`)
  - `0x00ACBA96` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00ACBAE5` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00ACBB27` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00ACBB3B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00ACBB40` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00ACBB65` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00ACBBEC` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00ACBC2F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00ACBC34` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00ACBC69` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00ACBD73` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ACBDD6` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00ACBDE8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ACBDFA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ACBE07` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00ACBE18` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00ACBE1D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00ACBE3C` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x00ACBE4C` → [PiControlFreeUserModeCallersBuffer](../../text/44/PiControlFreeUserModeCallersBuffer_function_00448990.md) (`PAGE` → `.text`)
  - `0x00ACBECF` → [RtlInitUnicodeStringEx](../../text/46/RtlInitUnicodeStringEx_function_00463960.md) (`PAGE` → `.text`)
  - `0x00ACBF0D` → [RtlStringCchLengthW](../../text/43/RtlStringCchLengthW_function_00435A70.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACB824  48 8B C4                        mov rax, rsp
00ACB827  48 89 58 08                     mov qword ptr [rax + 8], rbx
00ACB82B  44 89 48 20                     mov dword ptr [rax + 0x20], r9d
00ACB82F  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
00ACB833  55                              push rbp
00ACB834  56                              push rsi
00ACB835  57                              push rdi
00ACB836  41 54                           push r12
00ACB838  41 55                           push r13
00ACB83A  41 56                           push r14
00ACB83C  41 57                           push r15
00ACB83E  48 8D 68 B1                     lea rbp, [rax - 0x4f]
00ACB842  48 81 EC F0 00 00 00            sub rsp, 0xf0
00ACB849  45 33 C0                        xor r8d, r8d
00ACB84C  33 C0                           xor eax, eax
00ACB84E  0F 57 C0                        xorps xmm0, xmm0
00ACB851  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00ACB855  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00ACB859  0F 57 C9                        xorps xmm1, xmm1
00ACB85C  41 8B D9                        mov ebx, r9d
00ACB85F  44 89 44 24 54                  mov dword ptr [rsp + 0x54], r8d
00ACB864  44 89 45 87                     mov dword ptr [rbp - 0x79], r8d
00ACB868  4C 8D 4D DF                     lea r9, [rbp - 0x21]
00ACB86C  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
00ACB870  45 8B E0                        mov r12d, r8d
00ACB873  44 89 00                        mov dword ptr [rax], r8d
00ACB876  41 8B F8                        mov edi, r8d
00ACB879  44 89 45 BF                     mov dword ptr [rbp - 0x41], r8d
00ACB87D  45 8A E8                        mov r13b, r8b
00ACB880  44 89 45 B7                     mov dword ptr [rbp - 0x49], r8d
00ACB884  45 8B F0                        mov r14d, r8d
00ACB887  44 89 45 9F                     mov dword ptr [rbp - 0x61], r8d
00ACB88B  45 8B F8                        mov r15d, r8d
00ACB88E  44 89 45 BB                     mov dword ptr [rbp - 0x45], r8d
00ACB892  4C 89 45 97                     mov qword ptr [rbp - 0x69], r8
00ACB896  4C 89 45 C7                     mov qword ptr [rbp - 0x39], r8
00ACB89A  44 88 44 24 50                  mov byte ptr [rsp + 0x50], r8b
00ACB89F  4C 89 45 AF                     mov qword ptr [rbp - 0x51], r8
00ACB8A3  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
00ACB8A8  44 8B 45 77                     mov r8d, dword ptr [rbp + 0x77]
00ACB8AC  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00ACB8B0  0F 11 4D DF                     movups xmmword ptr [rbp - 0x21], xmm1
00ACB8B4  0F 11 4D EF                     movups xmmword ptr [rbp - 0x11], xmm1
00ACB8B8  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
00ACB8BC  E8 E7 06 00 00                  call 0x140acbfa8
00ACB8C1  8B F0                           mov esi, eax
00ACB8C3  85 C0                           test eax, eax
00ACB8C5  0F 88 57 05 00 00               js 0x140acbe22
00ACB8CB  41 8D 4F 02                     lea ecx, [r15 + 2]
00ACB8CF  E8 6C 70 E9 FF                  call 0x140962940
00ACB8D4  84 C0                           test al, al
00ACB8D6  75 0A                           jne 0x140acb8e2
00ACB8D8  BB 22 00 00 C0                  mov ebx, 0xc0000022
00ACB8DD  E9 AE 04 00 00                  jmp 0x140acbd90
00ACB8E2  48 8B 75 E7                     mov rsi, qword ptr [rbp - 0x19]
00ACB8E6  48 85 F6                        test rsi, rsi
00ACB8E9  0F 84 99 06 00 00               je 0x140acbf88
00ACB8EF  83 7D EF 02                     cmp dword ptr [rbp - 0x11], 2
00ACB8F3  0F 82 8F 06 00 00               jb 0x140acbf88
00ACB8F9  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00ACB8FD  48 85 C9                        test rcx, rcx
00ACB900  0F 84 82 06 00 00               je 0x140acbf88
00ACB906  83 7D FF 02                     cmp dword ptr [rbp - 1], 2
00ACB90A  0F 82 78 06 00 00               jb 0x140acbf88
00ACB910  48 39 7D 67                     cmp qword ptr [rbp + 0x67], rdi
00ACB914  0F 84 6E 06 00 00               je 0x140acbf88
00ACB91A  83 FB 14                        cmp ebx, 0x14
00ACB91D  0F 82 65 06 00 00               jb 0x140acbf88
00ACB923  44 8B 6D E3                     mov r13d, dword ptr [rbp - 0x1d]
00ACB927  41 F7 C5 F0 FF FF FF            test r13d, 0xfffffff0
00ACB92E  74 0D                           je 0x140acb93d
00ACB930  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ACB935  44 8A EF                        mov r13b, dil
00ACB938  E9 53 04 00 00                  jmp 0x140acbd90
00ACB93D  45 8B FD                        mov r15d, r13d
00ACB940  41 83 E7 02                     and r15d, 2
00ACB944  E8 9B 6C E6 FF                  call 0x1409325e4
00ACB949  84 C0                           test al, al
00ACB94B  75 0A                           jne 0x140acb957
00ACB94D  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ACB952  4C 8B FF                        mov r15, rdi
00ACB955  EB DE                           jmp 0x140acb935
00ACB957  48 8D 4D C7                     lea rcx, [rbp - 0x39]
00ACB95B  E8 DC 49 E1 FF                  call 0x1408e033c
00ACB960  8B D8                           mov ebx, eax
00ACB962  85 C0                           test eax, eax
00ACB964  78 EC                           js 0x140acb952
00ACB966  BA 90 01 00 00                  mov edx, 0x190
00ACB96B  B9 00 01 00 00                  mov ecx, 0x100
00ACB970  41 B8 50 6E 70 34               mov r8d, 0x34706e50
00ACB976  E8 75 67 0B 00                  call 0x140b820f0
00ACB97B  48 8B F8                        mov rdi, rax
00ACB97E  48 85 C0                        test rax, rax
00ACB981  75 10                           jne 0x140acb993
00ACB983  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00ACB988  4D 8B FC                        mov r15, r12
00ACB98B  45 8A EC                        mov r13b, r12b
00ACB98E  E9 FD 03 00 00                  jmp 0x140acbd90
00ACB993  45 8B E5                        mov r12d, r13d
00ACB996  41 83 E4 04                     and r12d, 4
00ACB99A  74 30                           je 0x140acb9cc
00ACB99C  45 85 FF                        test r15d, r15d
00ACB99F  4C 8B C7                        mov r8, rdi
00ACB9A2  48 8B CE                        mov rcx, rsi
00ACB9A5  0F 95 C2                        setne dl
00ACB9A8  E8 EF FC C6 FF                  call 0x14073b69c
00ACB9AD  33 C9                           xor ecx, ecx
00ACB9AF  8B D8                           mov ebx, eax
00ACB9B1  45 85 FF                        test r15d, r15d
00ACB9B4  74 22                           je 0x140acb9d8
00ACB9B6  44 8B E1                        mov r12d, ecx
00ACB9B9  44 8A E9                        mov r13b, cl
00ACB9BC  44 8B F9                        mov r15d, ecx
00ACB9BF  85 C0                           test eax, eax
00ACB9C1  0F 89 87 01 00 00               jns 0x140acbb4e
00ACB9C7  E9 C4 03 00 00                  jmp 0x140acbd90
00ACB9CC  48 8B D6                        mov rdx, rsi
00ACB9CF  E8 1C 83 E2 FF                  call 0x1408f3cf0
00ACB9D4  8B D8                           mov ebx, eax
00ACB9D6  33 C9                           xor ecx, ecx
00ACB9D8  85 DB                           test ebx, ebx
00ACB9DA  0F 88 8E 00 00 00               js 0x140acba6e
00ACB9E0  45 85 E4                        test r12d, r12d
00ACB9E3  75 2C                           jne 0x140acba11
00ACB9E5  C7 44 24 28 00 08 00 00         mov dword ptr [rsp + 0x28], 0x800
00ACB9ED  45 33 C9                        xor r9d, r9d
00ACB9F0  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00ACB9F5  4C 8B C6                        mov r8, rsi
00ACB9F8  48 8B CF                        mov rcx, rdi
00ACB9FB  BA C8 00 00 00                  mov edx, 0xc8
00ACBA00  E8 BB 27 95 FF                  call 0x14041e1c0
00ACBA05  33 C9                           xor ecx, ecx
00ACBA07  8B D8                           mov ebx, eax
00ACBA09  85 C0                           test eax, eax
00ACBA0B  0F 88 81 05 00 00               js 0x140acbf92
00ACBA11  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
00ACBA16  48 8D 45 97                     lea rax, [rbp - 0x69]
00ACBA1A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ACBA1F  45 33 C9                        xor r9d, r9d
00ACBA22  88 4C 24 28                     mov byte ptr [rsp + 0x28], cl
00ACBA26  BE 1F 00 02 00                  mov esi, 0x2001f
00ACBA2B  48 8B 0D 66 A9 39 00            mov rcx, qword ptr [rip + 0x39a966]
00ACBA32  48 8B D7                        mov rdx, rdi
00ACBA35  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00ACBA39  45 8D 41 10                     lea r8d, [r9 + 0x10]
00ACBA3D  E8 FE 2A E2 FF                  call 0x1408ee540
00ACBA42  B9 00 00 00 80                  mov ecx, 0x80000000
00ACBA47  8B D8                           mov ebx, eax
00ACBA49  03 C1                           add eax, ecx
00ACBA4B  85 C1                           test ecx, eax
00ACBA4D  75 08                           jne 0x140acba57
00ACBA4F  81 FB 0E 00 00 C0               cmp ebx, 0xc000000e
00ACBA55  75 17                           jne 0x140acba6e
00ACBA57  45 85 FF                        test r15d, r15d
00ACBA5A  0F 84 F5 00 00 00               je 0x140acbb55
00ACBA60  45 33 FF                        xor r15d, r15d
00ACBA63  4C 39 7D 97                     cmp qword ptr [rbp - 0x69], r15
00ACBA67  74 13                           je 0x140acba7c
00ACBA69  BB 35 00 00 C0                  mov ebx, 0xc0000035
00ACBA6E  4D 8B E6                        mov r12, r14
00ACBA71  4D 8B FE                        mov r15, r14
00ACBA74  45 8A EE                        mov r13b, r14b
00ACBA77  E9 14 03 00 00                  jmp 0x140acbd90
00ACBA7C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00ACBA85  48 8D 0D 74 0B 4C 00            lea rcx, [rip + 0x4c0b74]
00ACBA8C  B2 01                           mov dl, 1
00ACBA8E  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00ACBA95  90                              nop
00ACBA96  E8 85 93 74 FF                  call 0x140214e20
00ACBA9B  48 8B 0D F6 A8 39 00            mov rcx, qword ptr [rip + 0x39a8f6]
00ACBAA2  48 8D 44 24 51                  lea rax, [rsp + 0x51]
00ACBAA7  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00ACBAAC  4C 8D 4D A7                     lea r9, [rbp - 0x59]
00ACBAB0  41 B8 06 00 02 00               mov r8d, 0x20006
00ACBAB6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ACBABB  48 8B D7                        mov rdx, rdi
00ACBABE  44 88 7C 24 51                  mov byte ptr [rsp + 0x51], r15b
00ACBAC3  41 B5 01                        mov r13b, 1
00ACBAC6  E8 F1 3F E3 FF                  call 0x1408ffabc
00ACBACB  8B D8                           mov ebx, eax
00ACBACD  85 C0                           test eax, eax
00ACBACF  0F 88 A9 04 00 00               js 0x140acbf7e
00ACBAD5  44 38 7C 24 51                  cmp byte ptr [rsp + 0x51], r15b
00ACBADA  75 1A                           jne 0x140acbaf6
00ACBADC  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00ACBAE0  BB 35 00 00 C0                  mov ebx, 0xc0000035
00ACBAE5  E8 C6 17 BE FF                  call 0x1406ad2b0
00ACBAEA  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00ACBAEE  4D 8B E7                        mov r12, r15
00ACBAF1  E9 9A 02 00 00                  jmp 0x140acbd90
00ACBAF6  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00ACBAFA  48 8D 45 B7                     lea rax, [rbp - 0x49]
00ACBAFE  41 B9 04 00 00 00               mov r9d, 4
00ACBB04  C7 45 B7 01 00 00 00            mov dword ptr [rbp - 0x49], 1
00ACBB0B  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00ACBB10  4C 8D 05 E9 3B 03 00            lea r8, [rip + 0x33be9]
00ACBB17  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ACBB1C  E8 6B 60 EC FF                  call 0x140991b8c
00ACBB21  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00ACBB25  8B D8                           mov ebx, eax
00ACBB27  E8 84 17 BE FF                  call 0x1406ad2b0
00ACBB2C  85 DB                           test ebx, ebx
00ACBB2E  0F 88 4A 04 00 00               js 0x140acbf7e
00ACBB34  48 8D 0D C5 0A 4C 00            lea rcx, [rip + 0x4c0ac5]
00ACBB3B  E8 D0 3E 79 FF                  call 0x14025fa10
00ACBB40  E8 6B 1D 79 FF                  call 0x14025d8b0
00ACBB45  45 8A EF                        mov r13b, r15b
00ACBB48  4D 8B E6                        mov r12, r14
00ACBB4B  4D 8B FE                        mov r15, r14
00ACBB4E  33 F6                           xor esi, esi
00ACBB50  E9 AC 03 00 00                  jmp 0x140acbf01
00ACBB55  45 33 FF                        xor r15d, r15d
00ACBB58  4C 39 7D 97                     cmp qword ptr [rbp - 0x69], r15
00ACBB5C  74 74                           je 0x140acbbd2
00ACBB5E  48 8B D7                        mov rdx, rdi
00ACBB61  48 8D 4D 07                     lea rcx, [rbp + 7]
00ACBB65  E8 F6 7D 99 FF                  call 0x140463960
00ACBB6A  85 C0                           test eax, eax
00ACBB6C  0F 88 ED 00 00 00               js 0x140acbc5f
00ACBB72  33 C9                           xor ecx, ecx
00ACBB74  E8 97 D7 F4 FF                  call 0x140a19310
00ACBB79  BA 44 66 6C 74                  mov edx, 0x746c6644
00ACBB7E  48 8D 4D 07                     lea rcx, [rbp + 7]
00ACBB82  E8 09 B9 E1 FF                  call 0x1408e7490
00ACBB87  4C 8B E0                        mov r12, rax
00ACBB8A  48 85 C0                        test rax, rax
00ACBB8D  74 0D                           je 0x140acbb9c
00ACBB8F  48 8B 88 38 01 00 00            mov rcx, qword ptr [rax + 0x138]
00ACBB96  48 8B 59 28                     mov rbx, qword ptr [rcx + 0x28]
00ACBB9A  EB 03                           jmp 0x140acbb9f
00ACBB9C  49 8B DF                        mov rbx, r15
00ACBB9F  33 C9                           xor ecx, ecx
00ACBBA1  E8 EA 56 F5 FF                  call 0x140a21290
00ACBBA6  48 85 DB                        test rbx, rbx
00ACBBA9  74 1A                           je 0x140acbbc5
00ACBBAB  49 8B CC                        mov rcx, r12
00ACBBAE  E8 01 61 FE FF                  call 0x140ab1cb4
00ACBBB3  84 C0                           test al, al
00ACBBB5  0F 84 A7 00 00 00               je 0x140acbc62
00ACBBBB  BB 35 00 00 C0                  mov ebx, 0xc0000035
00ACBBC0  E9 AC FE FF FF                  jmp 0x140acba71
00ACBBC5  48 8B D7                        mov rdx, rdi
00ACBBC8  E8 5B 3D C6 FF                  call 0x14072f928
00ACBBCD  E9 90 00 00 00                  jmp 0x140acbc62
00ACBBD2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00ACBBDB  48 8D 0D 1E 0A 4C 00            lea rcx, [rip + 0x4c0a1e]
00ACBBE2  B2 01                           mov dl, 1
00ACBBE4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00ACBBEB  90                              nop
00ACBBEC  E8 2F 92 74 FF                  call 0x140214e20
00ACBBF1  48 8B 0D A0 A7 39 00            mov rcx, qword ptr [rip + 0x39a7a0]
00ACBBF8  48 8D 44 24 51                  lea rax, [rsp + 0x51]
00ACBBFD  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00ACBC02  4C 8D 4D 97                     lea r9, [rbp - 0x69]
00ACBC06  44 8B C6                        mov r8d, esi
00ACBC09  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ACBC0E  48 8B D7                        mov rdx, rdi
00ACBC11  44 88 7C 24 51                  mov byte ptr [rsp + 0x51], r15b
00ACBC16  41 B5 01                        mov r13b, 1
00ACBC19  E8 9E 3E E3 FF                  call 0x1408ffabc
00ACBC1E  8B D8                           mov ebx, eax
00ACBC20  85 C0                           test eax, eax
00ACBC22  0F 88 56 03 00 00               js 0x140acbf7e
00ACBC28  48 8D 0D D1 09 4C 00            lea rcx, [rip + 0x4c09d1]
00ACBC2F  E8 DC 3D 79 FF                  call 0x14025fa10
00ACBC34  E8 77 1C 79 FF                  call 0x14025d8b0
00ACBC39  45 8A EF                        mov r13b, r15b
00ACBC3C  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00ACBC40  4D 8B E7                        mov r12, r15
00ACBC43  44 88 7C 24 50                  mov byte ptr [rsp + 0x50], r15b
00ACBC48  44 38 7C 24 51                  cmp byte ptr [rsp + 0x51], r15b
00ACBC4D  75 0A                           jne 0x140acbc59
00ACBC4F  BB 35 00 00 C0                  mov ebx, 0xc0000035
00ACBC54  E9 37 01 00 00                  jmp 0x140acbd90
00ACBC59  44 8B 6D E3                     mov r13d, dword ptr [rbp - 0x1d]
00ACBC5D  EB 03                           jmp 0x140acbc62
00ACBC5F  4D 8B E6                        mov r12, r14
00ACBC62  48 8B D7                        mov rdx, rdi
00ACBC65  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ACBC69  E8 F2 7C 99 FF                  call 0x140463960
00ACBC6E  8B D8                           mov ebx, eax
00ACBC70  85 C0                           test eax, eax
00ACBC72  0F 88 13 01 00 00               js 0x140acbd8b
00ACBC78  4C 8B 45 97                     mov r8, qword ptr [rbp - 0x69]
00ACBC7C  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00ACBC81  48 8B 0D 10 A7 39 00            mov rcx, qword ptr [rip + 0x39a710]
00ACBC88  BE 04 00 00 00                  mov esi, 4
00ACBC8D  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
00ACBC92  48 8B D7                        mov rdx, rdi
00ACBC95  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ACBC9A  48 8D 45 9F                     lea rax, [rbp - 0x61]
00ACBC9E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ACBCA3  48 8D 45 87                     lea rax, [rbp - 0x79]
00ACBCA7  44 8D 4E 07                     lea r9d, [rsi + 7]
00ACBCAB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ACBCB0  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
00ACBCB4  E8 B7 1B E2 FF                  call 0x1408ed870
00ACBCB9  85 C0                           test eax, eax
00ACBCBB  79 04                           jns 0x140acbcc1
00ACBCBD  44 89 7D 9F                     mov dword ptr [rbp - 0x61], r15d
00ACBCC1  4C 8D 45 BB                     lea r8, [rbp - 0x45]
00ACBCC5  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ACBCC9  E8 8E A0 FA FF                  call 0x140a75d5c
00ACBCCE  8B 55 BB                        mov edx, dword ptr [rbp - 0x45]
00ACBCD1  85 C0                           test eax, eax
00ACBCD3  41 0F 48 D7                     cmovs edx, r15d
00ACBCD7  F6 45 9F 12                     test byte ptr [rbp - 0x61], 0x12
00ACBCDB  0F 94 C1                        sete cl
00ACBCDE  F6 C2 02                        test dl, 2
00ACBCE1  0F 94 C0                        sete al
00ACBCE4  84 C8                           test al, cl
00ACBCE6  0F 84 88 02 00 00               je 0x140acbf74
00ACBCEC  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ACBCF0  E8 67 2F C7 FF                  call 0x14073ec5c
00ACBCF5  8B D8                           mov ebx, eax
00ACBCF7  85 C0                           test eax, eax
00ACBCF9  0F 88 8C 00 00 00               js 0x140acbd8b
00ACBCFF  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
00ACBD03  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00ACBD08  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ACBD0D  4C 8D 4D 87                     lea r9, [rbp - 0x79]
00ACBD11  48 8D 45 BF                     lea rax, [rbp - 0x41]
00ACBD15  89 74 24 54                     mov dword ptr [rsp + 0x54], esi
00ACBD19  4C 8D 05 E0 39 03 00            lea r8, [rip + 0x339e0]
00ACBD20  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ACBD25  E8 D2 83 EC FF                  call 0x1409940fc
00ACBD2A  85 C0                           test eax, eax
00ACBD2C  78 0E                           js 0x140acbd3c
00ACBD2E  39 75 87                        cmp dword ptr [rbp - 0x79], esi
00ACBD31  75 09                           jne 0x140acbd3c
00ACBD33  8B 45 BF                        mov eax, dword ptr [rbp - 0x41]
00ACBD36  39 74 24 54                     cmp dword ptr [rsp + 0x54], esi
00ACBD3A  74 03                           je 0x140acbd3f
00ACBD3C  41 8B C7                        mov eax, r15d
00ACBD3F  85 C0                           test eax, eax
00ACBD41  74 10                           je 0x140acbd53
00ACBD43  48 8B 55 97                     mov rdx, qword ptr [rbp - 0x69]
00ACBD47  4C 8D 05 B2 39 03 00            lea r8, [rip + 0x339b2]
00ACBD4E  E8 8D 28 E3 FF                  call 0x1408fe5e0
00ACBD53  41 F6 C5 08                     test r13b, 8
00ACBD57  0F 84 9D 01 00 00               je 0x140acbefa
00ACBD5D  BB 00 02 00 00                  mov ebx, 0x200
00ACBD62  41 B8 50 6E 70 34               mov r8d, 0x34706e50
00ACBD68  8B D3                           mov edx, ebx
00ACBD6A  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
00ACBD6E  B9 00 01 00 00                  mov ecx, 0x100
00ACBD73  E8 78 63 0B 00                  call 0x140b820f0
00ACBD78  33 F6                           xor esi, esi
00ACBD7A  4C 8B F8                        mov r15, rax
00ACBD7D  48 85 C0                        test rax, rax
00ACBD80  0F 85 F7 00 00 00               jne 0x140acbe7d
00ACBD86  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00ACBD8B  44 8A 6C 24 50                  mov r13b, byte ptr [rsp + 0x50]
00ACBD90  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
00ACBD94  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00ACBD98  43 8D 14 36                     lea edx, [r14 + r14]
00ACBD9C  48 8B 4D 67                     mov rcx, qword ptr [rbp + 0x67]
00ACBDA0  45 33 F6                        xor r14d, r14d
00ACBDA3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ACBDA8  45 33 C9                        xor r9d, r9d
00ACBDAB  8B 45 03                        mov eax, dword ptr [rbp + 3]
00ACBDAE  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00ACBDB3  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00ACBDB8  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00ACBDBC  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00ACBDC1  45 33 C0                        xor r8d, r8d
00ACBDC4  8B CB                           mov ecx, ebx
00ACBDC6  E8 05 19 E2 FF                  call 0x1408ed6d0
00ACBDCB  48 8B 4D 97                     mov rcx, qword ptr [rbp - 0x69]
00ACBDCF  8B F0                           mov esi, eax
00ACBDD1  48 85 C9                        test rcx, rcx
00ACBDD4  74 05                           je 0x140acbddb
00ACBDD6  E8 D5 14 BE FF                  call 0x1406ad2b0
00ACBDDB  48 85 FF                        test rdi, rdi
00ACBDDE  74 0D                           je 0x140acbded
00ACBDE0  BA 50 6E 70 34                  mov edx, 0x34706e50
00ACBDE5  48 8B CF                        mov rcx, rdi
00ACBDE8  E8 83 6A 0B 00                  call 0x140b82870
00ACBDED  4D 85 FF                        test r15, r15
00ACBDF0  74 0D                           je 0x140acbdff
00ACBDF2  BA 50 6E 70 34                  mov edx, 0x34706e50
00ACBDF7  49 8B CF                        mov rcx, r15
00ACBDFA  E8 71 6A 0B 00                  call 0x140b82870
00ACBDFF  4D 85 E4                        test r12, r12
00ACBE02  74 08                           je 0x140acbe0c
00ACBE04  49 8B CC                        mov rcx, r12
00ACBE07  E8 44 D5 82 FF                  call 0x1402f9350
00ACBE0C  45 84 ED                        test r13b, r13b
00ACBE0F  74 11                           je 0x140acbe22
00ACBE11  48 8D 0D E8 07 4C 00            lea rcx, [rip + 0x4c07e8]
00ACBE18  E8 F3 3B 79 FF                  call 0x14025fa10
00ACBE1D  E8 8E 1A 79 FF                  call 0x14025d8b0
00ACBE22  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00ACBE2B  48 8B 55 E7                     mov rdx, qword ptr [rbp - 0x19]
00ACBE2F  8A 98 32 02 00 00               mov bl, byte ptr [rax + 0x232]
00ACBE35  48 85 D2                        test rdx, rdx
00ACBE38  74 07                           je 0x140acbe41
00ACBE3A  8A CB                           mov cl, bl
00ACBE3C  E8 4F CB 97 FF                  call 0x140448990
00ACBE41  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
00ACBE45  48 85 D2                        test rdx, rdx
00ACBE48  74 07                           je 0x140acbe51
00ACBE4A  8A CB                           mov cl, bl
00ACBE4C  E8 3F CB 97 FF                  call 0x140448990
00ACBE51  48 8B 4D C7                     mov rcx, qword ptr [rbp - 0x39]
00ACBE55  48 85 C9                        test rcx, rcx
00ACBE58  74 05                           je 0x140acbe5f
00ACBE5A  E8 B9 46 E1 FF                  call 0x1408e0518
00ACBE5F  48 8B 9C 24 30 01 00 00         mov rbx, qword ptr [rsp + 0x130]
00ACBE67  8B C6                           mov eax, esi
00ACBE69  48 81 C4 F0 00 00 00            add rsp, 0xf0
00ACBE70  41 5F                           pop r15
00ACBE72  41 5E                           pop r14
00ACBE74  41 5D                           pop r13
00ACBE76  41 5C                           pop r12
00ACBE78  5F                              pop rdi
00ACBE79  5E                              pop rsi
00ACBE7A  5D                              pop rbp
00ACBE7B  C3                              ret
00ACBE7C  CC                              int3
00ACBE7D  4C 8B 45 97                     mov r8, qword ptr [rbp - 0x69]
00ACBE81  48 8D 44 24 54                  lea rax, [rsp + 0x54]
00ACBE86  48 8B 0D 0B A5 39 00            mov rcx, qword ptr [rip + 0x39a50b]
00ACBE8D  41 B9 05 00 00 00               mov r9d, 5
00ACBE93  89 74 24 38                     mov dword ptr [rsp + 0x38], esi
00ACBE97  48 8B D7                        mov rdx, rdi
00ACBE9A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ACBE9F  48 8D 45 87                     lea rax, [rbp - 0x79]
00ACBEA3  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00ACBEA8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ACBEAD  E8 BE 19 E2 FF                  call 0x1408ed870
00ACBEB2  85 C0                           test eax, eax
00ACBEB4  78 46                           js 0x140acbefc
00ACBEB6  83 7D 87 01                     cmp dword ptr [rbp - 0x79], 1
00ACBEBA  75 40                           jne 0x140acbefc
00ACBEBC  39 5C 24 54                     cmp dword ptr [rsp + 0x54], ebx
00ACBEC0  77 3A                           ja 0x140acbefc
00ACBEC2  66 41 39 37                     cmp word ptr [r15], si
00ACBEC6  74 34                           je 0x140acbefc
00ACBEC8  48 8B D7                        mov rdx, rdi
00ACBECB  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ACBECF  E8 8C 7A 99 FF                  call 0x140463960
00ACBED4  8B D8                           mov ebx, eax
00ACBED6  85 C0                           test eax, eax
00ACBED8  0F 88 AD FE FF FF               js 0x140acbd8b
00ACBEDE  45 33 C9                        xor r9d, r9d
00ACBEE1  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00ACBEE5  45 33 C0                        xor r8d, r8d
00ACBEE8  B2 01                           mov dl, 1
00ACBEEA  E8 E5 BA F3 FF                  call 0x140a079d4
00ACBEEF  8B D8                           mov ebx, eax
00ACBEF1  85 C0                           test eax, eax
00ACBEF3  79 07                           jns 0x140acbefc
00ACBEF5  E9 91 FE FF FF                  jmp 0x140acbd8b
00ACBEFA  33 F6                           xor esi, esi
00ACBEFC  44 8A 6C 24 50                  mov r13b, byte ptr [rsp + 0x50]
00ACBF01  4C 8D 45 AF                     lea r8, [rbp - 0x51]
00ACBF05  BA C8 00 00 00                  mov edx, 0xc8
00ACBF0A  48 8B CF                        mov rcx, rdi
00ACBF0D  E8 5E 9B 96 FF                  call 0x140435a70
00ACBF12  8B D8                           mov ebx, eax
00ACBF14  85 C0                           test eax, eax
00ACBF16  78 54                           js 0x140acbf6c
00ACBF18  4C 8B 75 AF                     mov r14, qword ptr [rbp - 0x51]
00ACBF1C  BA 23 00 00 C0                  mov edx, 0xc0000023
00ACBF21  44 8B 45 6F                     mov r8d, dword ptr [rbp + 0x6f]
00ACBF25  49 FF C6                        inc r14
00ACBF28  4B 8D 04 36                     lea rax, [r14 + r14]
00ACBF2C  49 8D 48 EC                     lea rcx, [r8 - 0x14]
00ACBF30  48 3B C8                        cmp rcx, rax
00ACBF33  0F 42 DA                        cmovb ebx, edx
00ACBF36  85 DB                           test ebx, ebx
00ACBF38  0F 88 56 FE FF FF               js 0x140acbd94
00ACBF3E  48 8B 45 7F                     mov rax, qword ptr [rbp + 0x7f]
00ACBF42  43 8D 14 36                     lea edx, [r14 + r14]
00ACBF46  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ACBF4B  4C 8B CF                        mov r9, rdi
00ACBF4E  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00ACBF52  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00ACBF57  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ACBF5C  8B 45 03                        mov eax, dword ptr [rbp + 3]
00ACBF5F  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00ACBF63  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
00ACBF67  E9 55 FE FF FF                  jmp 0x140acbdc1
00ACBF6C  4C 8B F6                        mov r14, rsi
00ACBF6F  E9 1C FE FF FF                  jmp 0x140acbd90
00ACBF74  BB 10 00 00 C0                  mov ebx, 0xc0000010
00ACBF79  E9 0D FE FF FF                  jmp 0x140acbd8b
00ACBF7E  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
00ACBF83  E9 62 FB FF FF                  jmp 0x140acbaea
00ACBF88  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00ACBF8D  E9 FE FD FF FF                  jmp 0x140acbd90
00ACBF92  4C 8B F9                        mov r15, rcx
00ACBF95  4C 8B E1                        mov r12, rcx
00ACBF98  44 8A E9                        mov r13b, cl
00ACBF9B  E9 F0 FD FF FF                  jmp 0x140acbd90
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCMCreateDevice(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int64 v_stack_mD7;
    unsigned __int8 v_stack_mD8;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p50;
    unsigned __int64 v_stack_p54;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned int *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    v_rsp = (v_rsp) - (240);
    a3 = 0;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 1) = 0;
    v_stack_mD4 = 0;
    *(unsigned int *)(v_rsp - 79 - 121) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 89) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_rsp - 79 + 127)) = 0;
    *(unsigned int *)(v_rsp - 79 - 65) = 0;
    *(unsigned int *)(v_rsp - 79 - 73) = 0;
    *(unsigned int *)(v_rsp - 79 - 97) = 0;
    *(unsigned int *)(v_rsp - 79 - 69) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 105) = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 57) = 0;
    v_stack_mD8 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 81) = 0;
    v_stack_mD0 = 0;
    *(unsigned __int64 *)(v_rsp - 79 - 49) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 79 - 33) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 79 - 17) = v_xmm1;
    *(unsigned __int64 *)(v_rsp - 79 + 7) = v_xmm0;
    result = PiCMCaptureCreateDeviceInputData(a1, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), v_rsp - 79 - 33);
    if (sign_flag) goto loc_00ACBE22;
    result = PiAuDoesClientHaveAccess(0 + 2, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), v_rsp - 79 - 33);
    if ((unsigned __int8)(result) != 0) goto loc_00ACB8E2;
    goto loc_00ACBD90;
loc_00ACB8E2:
    if (*(unsigned __int64 *)(v_rsp - 79 - 25) == 0) goto loc_00ACBF88;
    if ((*(unsigned int *)(v_rsp - 79 - 17)) < 2) goto loc_00ACBF88;
    if (*(unsigned __int64 *)(v_rsp - 79 - 9) == 0) goto loc_00ACBF88;
    if ((*(unsigned int *)(v_rsp - 79 - 1)) < 2) goto loc_00ACBF88;
    if ((*(unsigned __int64 *)(v_rsp - 79 + 103)) == 0) goto loc_00ACBF88;
    if (((unsigned int)((unsigned int)(0xC0000022ULL))) < 20) goto loc_00ACBF88;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 29)))) & (0xFFFFFFF0ULL)) == 0) goto loc_00ACB93D;
loc_00ACB935:
    goto loc_00ACBD90;
loc_00ACB93D:
    v_r15 = (unsigned int)((0) & (2));
    result = CmIsRootDevice(*(unsigned __int64 *)(v_rsp - 79 - 9), a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), v_rsp - 79 - 33);
    if ((unsigned __int8)(result) != 0) goto loc_00ACB957;
loc_00ACB952:
    goto loc_00ACB935;
loc_00ACB957:
    result = PiPnpRtlBeginOperation(v_rsp - 79 - 57, a2, (unsigned int)(*(unsigned int *)(v_rsp - 79 + 119)), v_rsp - 79 - 33);
    if (sign_flag) goto loc_00ACB952;
    result = ExAllocatePool2(256, 400, (unsigned int)(0x34706E50ULL), v_rsp - 79 - 33);
    if (result != 0) goto loc_00ACB993;
    goto loc_00ACBD90;
loc_00ACB993:
    v_r12 = (unsigned int)((0) & (4));
    if (condition_is_equal) goto loc_00ACB9CC;
    a2 = (0 != 0) ? 1 : 0;
    result = PiCMGenerateDeviceInstance(*(unsigned __int64 *)(v_rsp - 79 - 25), a2, result, v_rsp - 79 - 33);
    a1 = 0;
    if (0 == 0) goto loc_00ACB9D8;
    if (!sign_flag) goto loc_00ACBB4E;
    goto loc_00ACBD90;
loc_00ACB9CC:
    result = CmValidateDeviceName(a1, *(unsigned __int64 *)(v_rsp - 79 - 25), result, v_rsp - 79 - 33);
    a1 = 0;
loc_00ACB9D8:
    if (sign_flag) goto loc_00ACBA6E;
    if (0 != 0) goto loc_00ACBA11;
    v_stack_m100 = 0x800ULL;
    a4 = 0;
    v_stack_m108 = 0;
    result = RtlStringCchCopyExW(result, 200, *(unsigned __int64 *)(v_rsp - 79 - 25), a4);
    a1 = 0;
    if (sign_flag) goto loc_00ACBF92;
loc_00ACBA11:
    v_stack_mF0 = 0;
    v_stack_mF8 = v_rsp - 79 - 105;
    a4 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = (unsigned int)((unsigned int)(0x2001FULL));
    result = _CmOpenDeviceRegKey(*(unsigned __int64 *)(v_rip + 3778918), result, a4 + 16, a4);
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_00ACBA57;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC000000EULL) goto loc_00ACBA6E;
loc_00ACBA57:
    if (0 == 0) goto loc_00ACBB55;
    v_r15 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 79 - 105)) == 0) goto loc_00ACBA7C;
loc_00ACBA6E:
loc_00ACBA71:
    goto loc_00ACBD90;
loc_00ACBA7C:
    result = ExAcquireResourceExclusiveLite(v_rip + 4983668, 1, a4 + 16, a4);
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mD7;
    v_stack_mD7 = 0;
    result = CmCreateDevice(*(unsigned __int64 *)(v_rip + 3778806), result, (unsigned int)(0x20006ULL), v_rsp - 79 - 89);
    if (sign_flag) goto loc_00ACBF7E;
    if (v_stack_mD7 != 0) goto loc_00ACBAF6;
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 79 - 89), result, (unsigned int)(0x20006ULL), v_rsp - 79 - 89);
loc_00ACBAEA:
    goto loc_00ACBD90;
loc_00ACBAF6:
    *(unsigned int *)(v_rsp - 79 - 73) = 1;
    v_stack_m100 = 4;
    v_stack_m108 = v_rsp - 79 - 73;
    result = PnpCtxRegSetValue(*(unsigned __int64 *)(v_rsp - 79 - 89), *(unsigned __int64 *)(v_rsp - 79 - 89), v_rip + 211945, 4);
    result = ZwClose(*(unsigned __int64 *)(v_rsp - 79 - 89), *(unsigned __int64 *)(v_rsp - 79 - 89), v_rip + 211945, 4);
    if (sign_flag) goto loc_00ACBF7E;
    result = ExReleaseResourceLite(v_rip + 4983493, *(unsigned __int64 *)(v_rsp - 79 - 89), v_rip + 211945, 4);
    result = KeLeaveCriticalRegion(v_rip + 4983493, *(unsigned __int64 *)(v_rsp - 79 - 89), v_rip + 211945, 4);
loc_00ACBB4E:
    v_rsi = 0;
    goto loc_00ACBF01;
loc_00ACBB55:
    v_r15 = 0;
    if ((*(unsigned __int64 *)(v_rsp - 79 - 105)) == 0) goto loc_00ACBBD2;
    result = RtlInitUnicodeStringEx(v_rsp - 79 + 7, result, v_rip + 211945, 4);
    if (sign_flag) goto loc_00ACBC5F;
    a1 = 0;
    result = PpDevNodeLockTree(a1, result, v_rip + 211945, 4);
    result = PnpDeviceObjectFromDeviceInstanceWithTag(v_rsp - 79 + 7, (unsigned int)(0x746C6644ULL), v_rip + 211945, 4);
    if (result == 0) goto loc_00ACBB9C;
    goto loc_00ACBB9F;
loc_00ACBB9C:
loc_00ACBB9F:
    a1 = 0;
    result = PpDevNodeUnlockTree(a1, (unsigned int)(0x746C6644ULL), v_rip + 211945, 4);
    if (0 == 0) goto loc_00ACBBC5;
    result = IopIsRootEnumeratedDeviceObjectActive(result, (unsigned int)(0x746C6644ULL), v_rip + 211945, 4);
    if ((unsigned __int8)(result) == 0) goto loc_00ACBC62;
    goto loc_00ACBA71;
loc_00ACBBC5:
    result = PiPnpRtlEnsureObjectCached(result, result, v_rip + 211945, 4);
    goto loc_00ACBC62;
loc_00ACBBD2:
    result = ExAcquireResourceExclusiveLite(v_rip + 4983326, 1, v_rip + 211945, 4);
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mD7;
    v_stack_mD7 = 0;
    result = CmCreateDevice(*(unsigned __int64 *)(v_rip + 3778464), result, 0, v_rsp - 79 - 105);
    if (sign_flag) goto loc_00ACBF7E;
    result = ExReleaseResourceLite(v_rip + 4983249, result, 0, v_rsp - 79 - 105);
    result = KeLeaveCriticalRegion(v_rip + 4983249, result, 0, v_rsp - 79 - 105);
    v_stack_mD8 = 0;
    if (v_stack_mD7 != 0) goto loc_00ACBC59;
    goto loc_00ACBD90;
loc_00ACBC59:
    goto loc_00ACBC62;
loc_00ACBC5F:
loc_00ACBC62:
    result = RtlInitUnicodeStringEx(v_rsp - 79 - 49, result, 0, v_rsp - 79 - 105);
    if (sign_flag) goto loc_00ACBD8B;
    v_stack_mF0 = 0;
    v_stack_mF8 = v_stack_mD4;
    v_stack_m100 = v_rsp - 79 - 97;
    v_stack_m108 = v_rsp - 79 - 121;
    v_stack_mD4 = 4;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 3778320), result, *(unsigned __int64 *)(v_rsp - 79 - 105), 4 + 7);
    if (sign_flag) {
        *(unsigned int *)(v_rsp - 79 - 97) = 0;
    }
    result = PnpGetDeviceInstanceCsConfigFlags(v_rsp - 79 - 49, result, v_rsp - 79 - 69, 4 + 7);
    a2 = (unsigned int)(*(unsigned int *)(v_rsp - 79 - 69));
    if (sign_flag) { a2 = 0; }
    a1 = (((*(unsigned __int8 *)(v_rsp - 79 - 97)) & (18)) == 0) ? 1 : 0;
    result = ((((unsigned __int8)(a2)) & (2)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00ACBF74;
    result = PiInitializeDevice(v_rsp - 79 - 49, a2, v_rsp - 79 - 69, 4 + 7);
    if (sign_flag) goto loc_00ACBD8B;
    v_stack_m100 = v_stack_mD4;
    v_stack_mD4 = 4;
    v_stack_m108 = v_rsp - 79 - 65;
    result = PnpCtxRegQueryValue(v_rsp - 79 - 49, *(unsigned __int64 *)(v_rsp - 79 - 105), v_rip + 211424, v_rsp - 79 - 121);
    if (sign_flag) goto loc_00ACBD3C;
    if ((*(unsigned int *)(v_rsp - 79 - 121)) != 4) goto loc_00ACBD3C;
    result = (unsigned int)(*(unsigned int *)(v_rsp - 79 - 65));
    if (v_stack_mD4 != 4) {
        result = 0;
    }
    if ((unsigned int)(result) != 0) {
        a2 = *(unsigned __int64 *)(v_rsp - 79 - 105);
        a3 = v_rip + 211378;
        result = PnpCtxRegDeleteValue(v_rsp - 79 - 49, a2, a3, v_rsp - 79 - 121);
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rsp - 79 - 29)))) & (8)) == 0) goto loc_00ACBEFA;
    v_stack_mD4 = 512;
    result = ExAllocatePool2(256, 512, (unsigned int)(0x34706E50ULL), v_rsp - 79 - 121);
    v_rsi = 0;
    if (result != 0) goto loc_00ACBE7D;
loc_00ACBD8B:
loc_00ACBD90:
loc_00ACBD94:
    v_r14 = 0;
    v_stack_mE8 = *(unsigned __int64 *)(v_rsp - 79 + 127);
    a4 = 0;
    v_stack_mF0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 111)));
    v_stack_mF8 = *(unsigned __int64 *)(v_rsp - 79 + 103);
    v_stack_m100 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 3)));
    v_stack_m108 = 0;
loc_00ACBDC1:
    a3 = 0;
    result = PiCMReturnBufferResultData((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))), *(unsigned __int64 *)(v_rsp - 79 - 81) + *(unsigned __int64 *)(v_rsp - 79 - 81) * 1, a3, a4);
    if (*(unsigned __int64 *)(v_rsp - 79 - 105) != 0) {
        result = ZwClose(*(unsigned __int64 *)(v_rsp - 79 - 105), *(unsigned __int64 *)(v_rsp - 79 - 81) + *(unsigned __int64 *)(v_rsp - 79 - 81) * 1, a3, a4);
    }
    if (result != 0) {
        a2 = 0x34706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (result != 0) {
        a2 = 0x34706E50ULL;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 79 - 81) != 0) {
        a1 = *(unsigned __int64 *)(v_rsp - 79 - 81);
        result = ObfDereferenceObject(a1, a2, a3, a4);
    }
    if ((unsigned __int8)(v_stack_mD8) != 0) {
        a1 = v_rip + 4982760;
        result = ExReleaseResourceLite(a1, a2, a3, a4);
        result = KeLeaveCriticalRegion(a1, a2, a3, a4);
    }
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(v_rsp - 79 - 25) != 0) {
        a1 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = PiControlFreeUserModeCallersBuffer(a1, *(unsigned __int64 *)(v_rsp - 79 - 25), a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 79 - 9) != 0) {
        a1 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = PiControlFreeUserModeCallersBuffer(a1, *(unsigned __int64 *)(v_rsp - 79 - 9), a3, a4);
    }
    if (*(unsigned __int64 *)(v_rsp - 79 - 57) != 0) {
        result = PiPnpRtlEndOperation(*(unsigned __int64 *)(v_rsp - 79 - 57), *(unsigned __int64 *)(v_rsp - 79 - 9), a3, a4);
    }
    v_rsp = (v_rsp) + (240);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00ACBE7D:
    v_stack_p38 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_p30 = v_stack_p54;
    v_stack_p28 = result;
    v_stack_p20 = v_rsp - 79 - 121;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 3777803), result, *(unsigned __int64 *)(v_rsp - 79 - 105), 5);
    if (sign_flag) goto loc_00ACBEFC;
    if ((*(unsigned int *)(v_rsp - 79 - 121)) != 1) goto loc_00ACBEFC;
    if (v_stack_p54 > ((unsigned int)(v_stack_p8))) goto loc_00ACBEFC;
    if ((*(unsigned __int16 *)(result)) == ((unsigned __int16)((unsigned int)((unsigned int)(result))))) goto loc_00ACBEFC;
    result = RtlInitUnicodeStringEx(v_rsp - 79 - 49, result, *(unsigned __int64 *)(v_rsp - 79 - 105), 5);
    if (sign_flag) goto loc_00ACBD8B;
    a4 = 0;
    a3 = 0;
    result = PpDeviceRegistration(v_rsp - 79 - 49, 1, a3, a4);
    if (!sign_flag) goto loc_00ACBEFC;
    goto loc_00ACBD8B;
loc_00ACBEFA:
    v_rsi = 0;
loc_00ACBEFC:
loc_00ACBF01:
    result = RtlStringCchLengthW(result, 200, v_rsp - 79 - 81, a4);
    if (sign_flag) goto loc_00ACBF6C;
    v_r14 = (*(unsigned __int64 *)(v_rsp - 79 - 81)) + 1;
    v_rbx = (unsigned int)((unsigned int)(result));
    if (((unsigned int)(*(unsigned int *)(v_rsp - 79 + 111)) - 20) < (v_r14 + v_r14 * 1)) { v_rbx = (unsigned int)((unsigned int)(0xC0000023ULL)); }
    if (sign_flag) goto loc_00ACBD94;
    v_stack_p40 = *(unsigned __int64 *)(v_rsp - 79 + 127);
    v_stack_p38 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 111)));
    v_stack_p30 = *(unsigned __int64 *)(v_rsp - 79 + 103);
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 79 + 3)));
    v_stack_p20 = (unsigned int)(v_r14 + v_r14 * 1);
    goto loc_00ACBDC1;
loc_00ACBF6C:
    goto loc_00ACBD90;
loc_00ACBF74:
    goto loc_00ACBD8B;
loc_00ACBF7E:
    goto loc_00ACBAEA;
loc_00ACBF88:
    goto loc_00ACBD90;
loc_00ACBF92:
    goto loc_00ACBD90;
}
```

## 5. (Beta) C Style

```c
int64_t PiCMCreateDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint64_t v_stack_mD7;
    uint8_t v_stack_mD8;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint8_t v_stack_p50;
    uint64_t v_stack_p54;
    uint64_t v_stack_p58;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    local_rsp = (local_rsp) - (240);
    Arg3 = 0;
    result = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x1) = 0;
    v_stack_mD4 = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x79) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x59) = 0;
    *(uint32_t *)(*(uint64_t *)(local_rsp - 0x4F + 0x7F)) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x41) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x49) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x61) = 0;
    *(uint32_t *)(local_rsp - 0x4F - 0x45) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x69) = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x39) = 0;
    v_stack_mD8 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x51) = 0;
    v_stack_mD0 = 0;
    *(uint64_t *)(local_rsp - 0x4F - 0x31) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x4F - 0x21) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x4F - 0x11) = v_xmm1;
    *(uint64_t *)(local_rsp - 0x4F + 0x7) = v_xmm0;
    result = PiCMCaptureCreateDeviceInputData(Arg1, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), local_rsp - 79 - 33);
    if (sign_flag) goto loc_00ACBE22;
    result = PiAuDoesClientHaveAccess(0 + 2, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), local_rsp - 79 - 33);
    if ((uint8_t)(result) != 0) goto loc_00ACB8E2;
    goto loc_00ACBD90;
loc_00ACB8E2:
    if (*(uint64_t *)(local_rsp - 0x4F - 0x19) == 0) goto loc_00ACBF88;
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x11)) < 2) goto loc_00ACBF88;
    if (*(uint64_t *)(local_rsp - 0x4F - 0x9) == 0) goto loc_00ACBF88;
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x1)) < 2) goto loc_00ACBF88;
    if ((*(uint64_t *)(local_rsp - 0x4F + 0x67)) == 0) goto loc_00ACBF88;
    if (((uint32_t)((uint32_t)(0xC0000022ULL))) < 20) goto loc_00ACBF88;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x1D)))) & (0xFFFFFFF0ULL)) == 0) goto loc_00ACB93D;
loc_00ACB935:
    goto loc_00ACBD90;
loc_00ACB93D:
    local_r15 = (uint32_t)((0) & (2));
    result = CmIsRootDevice(*(uint64_t *)(local_rsp - 0x4F - 0x9), Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), local_rsp - 79 - 33);
    if ((uint8_t)(result) != 0) goto loc_00ACB957;
loc_00ACB952:
    goto loc_00ACB935;
loc_00ACB957:
    result = PiPnpRtlBeginOperation(local_rsp - 79 - 57, Arg2, (uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x77)), local_rsp - 79 - 33);
    if (sign_flag) goto loc_00ACB952;
    result = ExAllocatePool2(256, 400, (uint32_t)(0x34706E50ULL), local_rsp - 79 - 33);
    if (result != 0) goto loc_00ACB993;
    goto loc_00ACBD90;
loc_00ACB993:
    local_r12 = (uint32_t)((0) & (4));
    if (condition_is_equal) goto loc_00ACB9CC;
    Arg2 = (0 != 0) ? 1 : 0;
    result = PiCMGenerateDeviceInstance(*(uint64_t *)(local_rsp - 0x4F - 0x19), Arg2, result, local_rsp - 79 - 33);
    Arg1 = 0;
    if (0 == 0) goto loc_00ACB9D8;
    if (!sign_flag) goto loc_00ACBB4E;
    goto loc_00ACBD90;
loc_00ACB9CC:
    result = CmValidateDeviceName(Arg1, *(uint64_t *)(local_rsp - 0x4F - 0x19), result, local_rsp - 79 - 33);
    Arg1 = 0;
loc_00ACB9D8:
    if (sign_flag) goto loc_00ACBA6E;
    if (0 != 0) goto loc_00ACBA11;
    v_stack_m100 = 0x800ULL;
    Arg4 = 0;
    v_stack_m108 = 0;
    result = RtlStringCchCopyExW(result, 200, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg4);
    Arg1 = 0;
    if (sign_flag) goto loc_00ACBF92;
loc_00ACBA11:
    v_stack_mF0 = 0;
    v_stack_mF8 = local_rsp - 79 - 105;
    Arg4 = 0;
    v_stack_m100 = 0;
    v_stack_m108 = (uint32_t)((uint32_t)(0x2001FULL));
    result = _CmOpenDeviceRegKey(*(uint64_t *)(v_rip + 0x39A966), result, Arg4 + 16, Arg4);
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_00ACBA57;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC000000EULL) goto loc_00ACBA6E;
loc_00ACBA57:
    if (0 == 0) goto loc_00ACBB55;
    local_r15 = 0;
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x69)) == 0) goto loc_00ACBA7C;
loc_00ACBA6E:
loc_00ACBA71:
    goto loc_00ACBD90;
loc_00ACBA7C:
    result = ExAcquireResourceExclusiveLite(v_rip + 4983668, 1, Arg4 + 16, Arg4);
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mD7;
    v_stack_mD7 = 0;
    result = CmCreateDevice(*(uint64_t *)(v_rip + 0x39A8F6), result, (uint32_t)(0x20006ULL), local_rsp - 79 - 89);
    if (sign_flag) goto loc_00ACBF7E;
    if (v_stack_mD7 != 0) goto loc_00ACBAF6;
    result = ZwClose(*(uint64_t *)(local_rsp - 0x4F - 0x59), result, (uint32_t)(0x20006ULL), local_rsp - 79 - 89);
loc_00ACBAEA:
    goto loc_00ACBD90;
loc_00ACBAF6:
    *(uint32_t *)(local_rsp - 0x4F - 0x49) = 1;
    v_stack_m100 = 4;
    v_stack_m108 = local_rsp - 79 - 73;
    result = PnpCtxRegSetValue(*(uint64_t *)(local_rsp - 0x4F - 0x59), *(uint64_t *)(local_rsp - 0x4F - 0x59), v_rip + 211945, 4);
    result = ZwClose(*(uint64_t *)(local_rsp - 0x4F - 0x59), *(uint64_t *)(local_rsp - 0x4F - 0x59), v_rip + 211945, 4);
    if (sign_flag) goto loc_00ACBF7E;
    result = ExReleaseResourceLite(v_rip + 4983493, *(uint64_t *)(local_rsp - 0x4F - 0x59), v_rip + 211945, 4);
    result = KeLeaveCriticalRegion(v_rip + 4983493, *(uint64_t *)(local_rsp - 0x4F - 0x59), v_rip + 211945, 4);
loc_00ACBB4E:
    local_rsi = 0;
    goto loc_00ACBF01;
loc_00ACBB55:
    local_r15 = 0;
    if ((*(uint64_t *)(local_rsp - 0x4F - 0x69)) == 0) goto loc_00ACBBD2;
    result = RtlInitUnicodeStringEx(local_rsp - 79 + 7, result, v_rip + 211945, 4);
    if (sign_flag) goto loc_00ACBC5F;
    Arg1 = 0;
    result = PpDevNodeLockTree(Arg1, result, v_rip + 211945, 4);
    result = PnpDeviceObjectFromDeviceInstanceWithTag(local_rsp - 79 + 7, (uint32_t)(0x746C6644ULL), v_rip + 211945, 4);
    if (result == 0) goto loc_00ACBB9C;
    goto loc_00ACBB9F;
loc_00ACBB9C:
loc_00ACBB9F:
    Arg1 = 0;
    result = PpDevNodeUnlockTree(Arg1, (uint32_t)(0x746C6644ULL), v_rip + 211945, 4);
    if (0 == 0) goto loc_00ACBBC5;
    result = IopIsRootEnumeratedDeviceObjectActive(result, (uint32_t)(0x746C6644ULL), v_rip + 211945, 4);
    if ((uint8_t)(result) == 0) goto loc_00ACBC62;
    goto loc_00ACBA71;
loc_00ACBBC5:
    result = PiPnpRtlEnsureObjectCached(result, result, v_rip + 211945, 4);
    goto loc_00ACBC62;
loc_00ACBBD2:
    result = ExAcquireResourceExclusiveLite(v_rip + 4983326, 1, v_rip + 211945, 4);
    v_stack_m100 = 0;
    v_stack_m108 = v_stack_mD7;
    v_stack_mD7 = 0;
    result = CmCreateDevice(*(uint64_t *)(v_rip + 0x39A7A0), result, 0, local_rsp - 79 - 105);
    if (sign_flag) goto loc_00ACBF7E;
    result = ExReleaseResourceLite(v_rip + 4983249, result, 0, local_rsp - 79 - 105);
    result = KeLeaveCriticalRegion(v_rip + 4983249, result, 0, local_rsp - 79 - 105);
    v_stack_mD8 = 0;
    if (v_stack_mD7 != 0) goto loc_00ACBC59;
    goto loc_00ACBD90;
loc_00ACBC59:
    goto loc_00ACBC62;
loc_00ACBC5F:
loc_00ACBC62:
    result = RtlInitUnicodeStringEx(local_rsp - 79 - 49, result, 0, local_rsp - 79 - 105);
    if (sign_flag) goto loc_00ACBD8B;
    v_stack_mF0 = 0;
    v_stack_mF8 = v_stack_mD4;
    v_stack_m100 = local_rsp - 79 - 97;
    v_stack_m108 = local_rsp - 79 - 121;
    v_stack_mD4 = 4;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x39A710), result, *(uint64_t *)(local_rsp - 0x4F - 0x69), 4 + 7);
    if (sign_flag) {
        *(uint32_t *)(local_rsp - 0x4F - 0x61) = 0;
    }
    result = PnpGetDeviceInstanceCsConfigFlags(local_rsp - 79 - 49, result, local_rsp - 79 - 69, 4 + 7);
    Arg2 = (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x45));
    if (sign_flag) { Arg2 = 0; }
    Arg1 = (((*(uint8_t *)(local_rsp - 0x4F - 0x61)) & (18)) == 0) ? 1 : 0;
    result = ((((uint8_t)(Arg2)) & (2)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00ACBF74;
    result = PiInitializeDevice(local_rsp - 79 - 49, Arg2, local_rsp - 79 - 69, 4 + 7);
    if (sign_flag) goto loc_00ACBD8B;
    v_stack_m100 = v_stack_mD4;
    v_stack_mD4 = 4;
    v_stack_m108 = local_rsp - 79 - 65;
    result = PnpCtxRegQueryValue(local_rsp - 79 - 49, *(uint64_t *)(local_rsp - 0x4F - 0x69), v_rip + 211424, local_rsp - 79 - 121);
    if (sign_flag) goto loc_00ACBD3C;
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x79)) != 4) goto loc_00ACBD3C;
    result = (uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x41));
    if (v_stack_mD4 != 4) {
        result = 0;
    }
    if ((uint32_t)(result) != 0) {
        Arg2 = *(uint64_t *)(local_rsp - 0x4F - 0x69);
        Arg3 = v_rip + 211378;
        result = PnpCtxRegDeleteValue(local_rsp - 79 - 49, Arg2, Arg3, local_rsp - 79 - 121);
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F - 0x1D)))) & (8)) == 0) goto loc_00ACBEFA;
    v_stack_mD4 = 512;
    result = ExAllocatePool2(256, 512, (uint32_t)(0x34706E50ULL), local_rsp - 79 - 121);
    local_rsi = 0;
    if (result != 0) goto loc_00ACBE7D;
loc_00ACBD8B:
loc_00ACBD90:
loc_00ACBD94:
    local_r14 = 0;
    v_stack_mE8 = *(uint64_t *)(local_rsp - 0x4F + 0x7F);
    Arg4 = 0;
    v_stack_mF0 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x6F)));
    v_stack_mF8 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
    v_stack_m100 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x3)));
    v_stack_m108 = 0;
loc_00ACBDC1:
    Arg3 = 0;
    result = PiCMReturnBufferResultData((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))), *(uint64_t *)(local_rsp - 0x4F - 0x51) + *(uint64_t *)(local_rsp - 0x4F - 0x51) * 1, Arg3, Arg4);
    if (*(uint64_t *)(local_rsp - 0x4F - 0x69) != 0) {
        result = ZwClose(*(uint64_t *)(local_rsp - 0x4F - 0x69), *(uint64_t *)(local_rsp - 0x4F - 0x51) + *(uint64_t *)(local_rsp - 0x4F - 0x51) * 1, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0x34706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        Arg2 = 0x34706E50ULL;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x4F - 0x51) != 0) {
        Arg1 = *(uint64_t *)(local_rsp - 0x4F - 0x51);
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, Arg4);
    }
    if ((uint8_t)(v_stack_mD8) != 0) {
        Arg1 = v_rip + 4982760;
        result = ExReleaseResourceLite(Arg1, Arg2, Arg3, Arg4);
        result = KeLeaveCriticalRegion(Arg1, Arg2, Arg3, Arg4);
    }
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(local_rsp - 0x4F - 0x19) != 0) {
        Arg1 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = PiControlFreeUserModeCallersBuffer(Arg1, *(uint64_t *)(local_rsp - 0x4F - 0x19), Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x4F - 0x9) != 0) {
        Arg1 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = PiControlFreeUserModeCallersBuffer(Arg1, *(uint64_t *)(local_rsp - 0x4F - 0x9), Arg3, Arg4);
    }
    if (*(uint64_t *)(local_rsp - 0x4F - 0x39) != 0) {
        result = PiPnpRtlEndOperation(*(uint64_t *)(local_rsp - 0x4F - 0x39), *(uint64_t *)(local_rsp - 0x4F - 0x9), Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (240);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00ACBE7D:
    v_stack_p38 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_p30 = v_stack_p54;
    v_stack_p28 = result;
    v_stack_p20 = local_rsp - 79 - 121;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x39A50B), result, *(uint64_t *)(local_rsp - 0x4F - 0x69), 5);
    if (sign_flag) goto loc_00ACBEFC;
    if ((*(uint32_t *)(local_rsp - 0x4F - 0x79)) != 1) goto loc_00ACBEFC;
    if (v_stack_p54 > ((uint32_t)(v_stack_p8))) goto loc_00ACBEFC;
    if ((*(uint16_t *)(result)) == ((uint16_t)((uint32_t)((uint32_t)(result))))) goto loc_00ACBEFC;
    result = RtlInitUnicodeStringEx(local_rsp - 79 - 49, result, *(uint64_t *)(local_rsp - 0x4F - 0x69), 5);
    if (sign_flag) goto loc_00ACBD8B;
    Arg4 = 0;
    Arg3 = 0;
    result = PpDeviceRegistration(local_rsp - 79 - 49, 1, Arg3, Arg4);
    if (!sign_flag) goto loc_00ACBEFC;
    goto loc_00ACBD8B;
loc_00ACBEFA:
    local_rsi = 0;
loc_00ACBEFC:
loc_00ACBF01:
    result = RtlStringCchLengthW(result, 200, local_rsp - 79 - 81, Arg4);
    if (sign_flag) goto loc_00ACBF6C;
    local_r14 = (*(uint64_t *)(local_rsp - 0x4F - 0x51)) + 1;
    local_rbx = (uint32_t)((uint32_t)(result));
    if (((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x6F)) - 20) < (local_r14 + local_r14 * 1)) { local_rbx = (uint32_t)((uint32_t)(0xC0000023ULL)); }
    if (sign_flag) goto loc_00ACBD94;
    v_stack_p40 = *(uint64_t *)(local_rsp - 0x4F + 0x7F);
    v_stack_p38 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x6F)));
    v_stack_p30 = *(uint64_t *)(local_rsp - 0x4F + 0x67);
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x4F + 0x3)));
    v_stack_p20 = (uint32_t)(local_r14 + local_r14 * 1);
    goto loc_00ACBDC1;
loc_00ACBF6C:
    goto loc_00ACBD90;
loc_00ACBF74:
    goto loc_00ACBD8B;
loc_00ACBF7E:
    goto loc_00ACBAEA;
loc_00ACBF88:
    goto loc_00ACBD90;
loc_00ACBF92:
    goto loc_00ACBD90;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACB824&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
