# PiCreateDriverSwDeviceCallback

- RVA: `0x00ABB420`–`0x00ABBEB7` (길이 `2,711` bytes)
- VA: `0x0000000140ABB420`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BD414`
- 디코드: `695`개 명령, `2,711/2,711` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **52**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x00ABB50C` → [_RegRtlOpenKeyTransacted](../8E/_RegRtlOpenKeyTransacted_function_008EF810.md) (function, `0x008EF810`)
- `0x00ABB52A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00ABB63D` → [RtlpQueryRegistryValues](../8C/RtlpQueryRegistryValues_function_008C9050.md) (function, `0x008C9050`)
- `0x00ABB661` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ABB67B` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ABB697` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ABB6AF` → [RtlGUIDFromString](../8F/RtlGUIDFromString_function_008F1EF0.md) (function, `0x008F1EF0`)
- `0x00ABB6D9` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ABB6F3` → [RtlFreeAnsiString](../9C/RtlFreeAnsiString_function_009C0800.md) (function, `0x009C0800`)
- `0x00ABB768` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABB778` → [RtlPrefixUnicodeString](../8F/RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x00ABB79A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABB7AA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABB7BA` → [RtlPrefixUnicodeString](../8F/RtlPrefixUnicodeString_function_008F4F70.md) (function, `0x008F4F70`)
- `0x00ABB7F3` → [PnpGenerateDeviceIdsHash](../A2/PnpGenerateDeviceIdsHash_function_00A2B120.md) (function, `0x00A2B120`)
- `0x00ABB813` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABB825` → [RtlHashUnicodeString](../97/RtlHashUnicodeString_function_0097A780.md) (function, `0x0097A780`)
- `0x00ABB84A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00ABB85C` → [RtlHashUnicodeString](../97/RtlHashUnicodeString_function_0097A780.md) (function, `0x0097A780`)
- `0x00ABB89F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABB8F6` → [CmGetDeviceRegProp](../8E/CmGetDeviceRegProp_function_008ED870.md) (function, `0x008ED870`)
- `0x00ABB92F` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00ABB944` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00ABB97C` → [PnpCompareMultiSz](../73/PnpCompareMultiSz_function_0073D27C.md) (function, `0x0073D27C`)
- `0x00ABB9DD` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00ABB9EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABB9FA` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00ABBA0F` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00ABBA24` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00ABBA39` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00ABBA4E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (function, `0x00B82850`)
- `0x00ABBA64` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABBA73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABBA81` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00ABBAAF` → [McTemplateK0zzd_EtwWriteTransfer](../../text/42/McTemplateK0zzd_EtwWriteTransfer_function_00424414.md) (function, `0x00424414`)
- `0x00ABBACA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00ABBB08` → [IopGetRegistryValue](../99/IopGetRegistryValue_function_009990EC.md) (function, `0x009990EC`)
- `0x00ABBB6A` → [PipMakeGloballyUniqueId](../A6/PipMakeGloballyUniqueId_function_00A6F428.md) (function, `0x00A6F428`)
- `0x00ABBBC8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABBBF4` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (function, `0x0048B984`)
- `0x00ABBC35` → [PnpGetGenericStorePropertyKeys](../99/PnpGetGenericStorePropertyKeys_function_00992378.md) (function, `0x00992378`)
- `0x00ABBC56` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABBC7C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABBC96` → [RtlCreateUnicodeString](../9B/RtlCreateUnicodeString_function_009BD860.md) (function, `0x009BD860`)
- `0x00ABBCE0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABBD50` → [PnpGetGenericStoreProperty](../8E/PnpGetGenericStoreProperty_function_008EFBA0.md) (function, `0x008EFBA0`)
- `0x00ABBD7A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABBD95` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00ABBDC2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABBDD6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABBDE9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00ABBE95` → [PiSwStartCreate](../73/PiSwStartCreate_function_0073B2CC.md) (function, `0x0073B2CC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00ABB43C` → RVA `0x00E0A740` (`.data`; read)
- `0x00ABB54F` → RVA `0x00AFF3D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABB580` → RVA `0x00AFF2F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABB5A7` → RVA `0x00B00280` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABB5C6` → RVA `0x00AFF330` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABB5DF` → RVA `0x00AFF1D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABB5F8` → RVA `0x00AFF3F0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABB736` → RVA `0x00F8C438` (`.data`; read)
- `0x00ABB74C` → RVA `0x00F8AC08` (`.data`; read)
- `0x00ABB75D` → RVA `0x0001C650` (`.rdata`; read)
- `0x00ABB79F` → RVA `0x00011750` (`.rdata`; read)
- `0x00ABB808` → RVA `0x000122B8` (`.rdata`; read)
- `0x00ABB83F` → RVA `0x000122A0` (`.rdata`; read)
- `0x00ABB8CC` → RVA `0x00E66398` (`.data`; read)
- `0x00ABBA8A` → RVA `0x00EF012C` (`.data`; read)
- `0x00ABBA97` → RVA `0x00027320` (`.rdata`; read)
- `0x00ABBB01` → RVA `0x00AFCD60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00ABBBE6` → RVA `0x00B002A0` (` ?? ::NNGAKEGL::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **31**
  - `0x00ABB52A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00ABB768` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABB79A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABB7AA` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABB813` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABB84A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
  - `0x00ABB89F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABB92F` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00ABB944` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00ABB9DD` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00ABB9EC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABB9FA` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBA0F` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBA24` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBA39` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBA4E` → [ExFreePool](../../poolcode/B8/ExFreePool_function_00B82850.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBA64` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBA73` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBA81` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00ABBAAF` → [McTemplateK0zzd_EtwWriteTransfer](../../text/42/McTemplateK0zzd_EtwWriteTransfer_function_00424414.md) (`PAGE` → `.text`)
  - `0x00ABBACA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00ABBBC8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBBF4` → [RtlUnicodeStringPrintf](../../text/48/RtlUnicodeStringPrintf_function_0048B984.md) (`PAGE` → `.text`)
  - `0x00ABBC56` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBC7C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBCE0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBD7A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBD95` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBDC2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBDD6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00ABBDE9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABB420  40 55                           push rbp
00ABB422  53                              push rbx
00ABB423  56                              push rsi
00ABB424  57                              push rdi
00ABB425  41 54                           push r12
00ABB427  41 55                           push r13
00ABB429  41 56                           push r14
00ABB42B  41 57                           push r15
00ABB42D  48 8D AC 24 B8 FD FF FF         lea rbp, [rsp - 0x248]
00ABB435  48 81 EC 48 03 00 00            sub rsp, 0x348
00ABB43C  48 8B 05 FD F2 34 00            mov rax, qword ptr [rip + 0x34f2fd]
00ABB443  48 33 C4                        xor rax, rsp
00ABB446  48 89 85 30 02 00 00            mov qword ptr [rbp + 0x230], rax
00ABB44D  0F 57 C0                        xorps xmm0, xmm0
00ABB450  48 89 4D 70                     mov qword ptr [rbp + 0x70], rcx
00ABB454  0F 57 C9                        xorps xmm1, xmm1
00ABB457  4C 89 4D 80                     mov qword ptr [rbp - 0x80], r9
00ABB45B  48 8B C1                        mov rax, rcx
00ABB45E  4C 89 45 08                     mov qword ptr [rbp + 8], r8
00ABB462  33 C9                           xor ecx, ecx
00ABB464  C7 45 B4 01 00 00 00            mov dword ptr [rbp - 0x4c], 1
00ABB46B  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
00ABB46F  4D 8B E9                        mov r13, r9
00ABB472  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
00ABB475  4D 8B D8                        mov r11, r8
00ABB478  89 4D B8                        mov dword ptr [rbp - 0x48], ecx
00ABB47B  4C 8B D2                        mov r10, rdx
00ABB47E  89 4D 94                        mov dword ptr [rbp - 0x6c], ecx
00ABB481  8B F1                           mov esi, ecx
00ABB483  89 4D 90                        mov dword ptr [rbp - 0x70], ecx
00ABB486  44 8B F9                        mov r15d, ecx
00ABB489  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
00ABB48C  44 8B F1                        mov r14d, ecx
00ABB48F  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
00ABB493  8B D9                           mov ebx, ecx
00ABB495  48 89 4D 10                     mov qword ptr [rbp + 0x10], rcx
00ABB499  44 8B E1                        mov r12d, ecx
00ABB49C  89 4D BC                        mov dword ptr [rbp - 0x44], ecx
00ABB49F  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00ABB4A4  89 4D C0                        mov dword ptr [rbp - 0x40], ecx
00ABB4A7  48 89 4D A0                     mov qword ptr [rbp - 0x60], rcx
00ABB4AB  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
00ABB4AF  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
00ABB4B3  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00ABB4B7  0F 11 4D E0                     movups xmmword ptr [rbp - 0x20], xmm1
00ABB4BB  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00ABB4BF  0F 11 8D 88 00 00 00            movups xmmword ptr [rbp + 0x88], xmm1
00ABB4C6  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
00ABB4CA  0F 11 4D 38                     movups xmmword ptr [rbp + 0x38], xmm1
00ABB4CE  0F 11 45 18                     movups xmmword ptr [rbp + 0x18], xmm0
00ABB4D2  0F 11 4D 48                     movups xmmword ptr [rbp + 0x48], xmm1
00ABB4D6  0F 11 45 58                     movups xmmword ptr [rbp + 0x58], xmm0
00ABB4DA  48 85 C0                        test rax, rax
00ABB4DD  74 10                           je 0x140abb4ef
00ABB4DF  48 8B 80 E0 00 00 00            mov rax, qword ptr [rax + 0xe0]
00ABB4E6  48 85 C0                        test rax, rax
00ABB4E9  74 04                           je 0x140abb4ef
00ABB4EB  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00ABB4EF  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00ABB4F4  48 8D 45 A8                     lea rax, [rbp - 0x58]
00ABB4F8  49 8B CA                        mov rcx, r10
00ABB4FB  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ABB500  41 B9 19 00 02 00               mov r9d, 0x20019
00ABB506  45 33 C0                        xor r8d, r8d
00ABB509  49 8B D3                        mov rdx, r11
00ABB50C  E8 FF 42 E3 FF                  call 0x1408ef810
00ABB511  8B F8                           mov edi, eax
00ABB513  85 C0                           test eax, eax
00ABB515  0F 88 B6 04 00 00               js 0x140abb9d1
00ABB51B  33 D2                           xor edx, edx
00ABB51D  48 8D 8D A0 00 00 00            lea rcx, [rbp + 0xa0]
00ABB524  41 B8 88 01 00 00               mov r8d, 0x188
00ABB52A  E8 11 B7 C0 FF                  call 0x1406c6c40
00ABB52F  BA 30 01 00 00                  mov edx, 0x130
00ABB534  C7 85 68 01 00 00 00 00 00 04   mov dword ptr [rbp + 0x168], 0x4000000
00ABB53E  B9 00 00 00 07                  mov ecx, 0x7000000
00ABB543  89 95 A8 00 00 00               mov dword ptr [rbp + 0xa8], edx
00ABB549  89 8D C0 00 00 00               mov dword ptr [rbp + 0xc0], ecx
00ABB54F  48 8D 05 7A 3E 04 00            lea rax, [rip + 0x43e7a]
00ABB556  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
00ABB55D  4C 8D 85 A0 00 00 00            lea r8, [rbp + 0xa0]
00ABB564  89 95 E0 00 00 00               mov dword ptr [rbp + 0xe0], edx
00ABB56A  48 8D 45 D0                     lea rax, [rbp - 0x30]
00ABB56E  48 89 85 B8 00 00 00            mov qword ptr [rbp + 0xb8], rax
00ABB575  BA 20 01 00 00                  mov edx, 0x120
00ABB57A  89 8D F8 00 00 00               mov dword ptr [rbp + 0xf8], ecx
00ABB580  48 8D 05 69 3D 04 00            lea rax, [rip + 0x43d69]
00ABB587  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
00ABB58E  B9 00 00 00 01                  mov ecx, 0x1000000
00ABB593  48 8D 45 E0                     lea rax, [rbp - 0x20]
00ABB597  89 95 18 01 00 00               mov dword ptr [rbp + 0x118], edx
00ABB59D  48 89 85 F0 00 00 00            mov qword ptr [rbp + 0xf0], rax
00ABB5A4  45 33 C9                        xor r9d, r9d
00ABB5A7  48 8D 05 D2 4C 04 00            lea rax, [rip + 0x44cd2]
00ABB5AE  89 8D 30 01 00 00               mov dword ptr [rbp + 0x130], ecx
00ABB5B4  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
00ABB5BB  48 8D 45 F0                     lea rax, [rbp - 0x10]
00ABB5BF  48 89 85 28 01 00 00            mov qword ptr [rbp + 0x128], rax
00ABB5C6  48 8D 05 63 3D 04 00            lea rax, [rip + 0x43d63]
00ABB5CD  48 89 85 58 01 00 00            mov qword ptr [rbp + 0x158], rax
00ABB5D4  48 8D 45 98                     lea rax, [rbp - 0x68]
00ABB5D8  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
00ABB5DF  48 8D 05 EA 3B 04 00            lea rax, [rip + 0x43bea]
00ABB5E6  48 89 85 90 01 00 00            mov qword ptr [rbp + 0x190], rax
00ABB5ED  48 8D 45 28                     lea rax, [rbp + 0x28]
00ABB5F1  48 89 85 98 01 00 00            mov qword ptr [rbp + 0x198], rax
00ABB5F8  48 8D 05 F1 3D 04 00            lea rax, [rip + 0x43df1]
00ABB5FF  48 89 85 C8 01 00 00            mov qword ptr [rbp + 0x1c8], rax
00ABB606  48 8D 45 38                     lea rax, [rbp + 0x38]
00ABB60A  89 95 50 01 00 00               mov dword ptr [rbp + 0x150], edx
00ABB610  89 95 88 01 00 00               mov dword ptr [rbp + 0x188], edx
00ABB616  89 8D A0 01 00 00               mov dword ptr [rbp + 0x1a0], ecx
00ABB61C  89 95 C0 01 00 00               mov dword ptr [rbp + 0x1c0], edx
00ABB622  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
00ABB626  89 8D D8 01 00 00               mov dword ptr [rbp + 0x1d8], ecx
00ABB62C  B9 00 00 00 C0                  mov ecx, 0xc0000000
00ABB631  48 89 85 D0 01 00 00            mov qword ptr [rbp + 0x1d0], rax
00ABB638  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00ABB63D  E8 0E DA E0 FF                  call 0x1408c9050
00ABB642  33 D2                           xor edx, edx
00ABB644  8B F8                           mov edi, eax
00ABB646  85 C0                           test eax, eax
00ABB648  0F 88 83 03 00 00               js 0x140abb9d1
00ABB64E  8D 42 02                        lea eax, [rdx + 2]
00ABB651  48 39 55 D8                     cmp qword ptr [rbp - 0x28], rdx
00ABB655  74 14                           je 0x140abb66b
00ABB657  66 39 45 D0                     cmp word ptr [rbp - 0x30], ax
00ABB65B  77 0E                           ja 0x140abb66b
00ABB65D  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00ABB661  E8 9A 51 F0 FF                  call 0x1409c0800
00ABB666  33 D2                           xor edx, edx
00ABB668  8D 42 02                        lea eax, [rdx + 2]
00ABB66B  48 39 55 E8                     cmp qword ptr [rbp - 0x18], rdx
00ABB66F  74 11                           je 0x140abb682
00ABB671  66 39 45 E0                     cmp word ptr [rbp - 0x20], ax
00ABB675  77 0B                           ja 0x140abb682
00ABB677  48 8D 4D E0                     lea rcx, [rbp - 0x20]
00ABB67B  E8 80 51 F0 FF                  call 0x1409c0800
00ABB680  33 D2                           xor edx, edx
00ABB682  48 39 55 F8                     cmp qword ptr [rbp - 8], rdx
00ABB686  74 32                           je 0x140abb6ba
00ABB688  B8 02 00 00 00                  mov eax, 2
00ABB68D  66 39 45 F0                     cmp word ptr [rbp - 0x10], ax
00ABB691  73 0B                           jae 0x140abb69e
00ABB693  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00ABB697  E8 64 51 F0 FF                  call 0x1409c0800
00ABB69C  33 D2                           xor edx, edx
00ABB69E  48 39 55 F8                     cmp qword ptr [rbp - 8], rdx
00ABB6A2  74 16                           je 0x140abb6ba
00ABB6A4  48 8D 95 88 00 00 00            lea rdx, [rbp + 0x88]
00ABB6AB  48 8D 4D F0                     lea rcx, [rbp - 0x10]
00ABB6AF  E8 3C 68 E3 FF                  call 0x1408f1ef0
00ABB6B4  33 D2                           xor edx, edx
00ABB6B6  85 C0                           test eax, eax
00ABB6B8  79 0A                           jns 0x140abb6c4
00ABB6BA  0F 57 C0                        xorps xmm0, xmm0
00ABB6BD  0F 11 85 88 00 00 00            movups xmmword ptr [rbp + 0x88], xmm0
00ABB6C4  B8 02 00 00 00                  mov eax, 2
00ABB6C9  48 39 55 30                     cmp qword ptr [rbp + 0x30], rdx
00ABB6CD  74 14                           je 0x140abb6e3
00ABB6CF  66 39 45 28                     cmp word ptr [rbp + 0x28], ax
00ABB6D3  73 0E                           jae 0x140abb6e3
00ABB6D5  48 8D 4D 28                     lea rcx, [rbp + 0x28]
00ABB6D9  E8 22 51 F0 FF                  call 0x1409c0800
00ABB6DE  33 D2                           xor edx, edx
00ABB6E0  8D 42 02                        lea eax, [rdx + 2]
00ABB6E3  48 39 55 40                     cmp qword ptr [rbp + 0x40], rdx
00ABB6E7  74 11                           je 0x140abb6fa
00ABB6E9  66 39 45 38                     cmp word ptr [rbp + 0x38], ax
00ABB6ED  73 0B                           jae 0x140abb6fa
00ABB6EF  48 8D 4D 38                     lea rcx, [rbp + 0x38]
00ABB6F3  E8 08 51 F0 FF                  call 0x1409c0800
00ABB6F8  33 D2                           xor edx, edx
00ABB6FA  48 39 55 D8                     cmp qword ptr [rbp - 0x28], rdx
00ABB6FE  75 10                           jne 0x140abb710
00ABB700  48 39 55 E8                     cmp qword ptr [rbp - 0x18], rdx
00ABB704  75 0A                           jne 0x140abb710
00ABB706  BF BB 00 00 C0                  mov edi, 0xc00000bb
00ABB70B  E9 C1 02 00 00                  jmp 0x140abb9d1
00ABB710  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
00ABB714  4D 8B 75 00                     mov r14, qword ptr [r13]
00ABB718  48 89 45 78                     mov qword ptr [rbp + 0x78], rax
00ABB71C  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00ABB720  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00ABB727  B8 02 00 00 00                  mov eax, 2
00ABB72C  89 45 68                        mov dword ptr [rbp + 0x68], eax
00ABB72F  C7 45 6C 03 00 00 00            mov dword ptr [rbp + 0x6c], 3
00ABB736  4C 3B 35 FB 0C 4D 00            cmp r14, qword ptr [rip + 0x4d0cfb]
00ABB73D  49 8B DF                        mov rbx, r15
00ABB740  8B C7                           mov eax, edi
00ABB742  0F 84 A6 03 00 00               je 0x140abbaee
00ABB748  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
00ABB74C  48 8B 05 B5 F4 4C 00            mov rax, qword ptr [rip + 0x4cf4b5]
00ABB753  48 39 41 08                     cmp qword ptr [rcx + 8], rax
00ABB757  0F 85 59 02 00 00               jne 0x140abb9b6
00ABB75D  48 8D 15 EC 0E 56 FF            lea rdx, [rip - 0xa9f114]
00ABB764  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00ABB768  E8 13 F0 96 FF                  call 0x14042a780
00ABB76D  49 8D 56 28                     lea rdx, [r14 + 0x28]
00ABB771  41 B0 01                        mov r8b, 1
00ABB774  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00ABB778  E8 F3 97 E3 FF                  call 0x1408f4f70
00ABB77D  33 D2                           xor edx, edx
00ABB77F  84 C0                           test al, al
00ABB781  0F 84 2F 02 00 00               je 0x140abb9b6
00ABB787  49 8B 46 30                     mov rax, qword ptr [r14 + 0x30]
00ABB78B  0F B7 4D 48                     movzx ecx, word ptr [rbp + 0x48]
00ABB78F  48 D1 E9                        shr rcx, 1
00ABB792  48 8D 14 48                     lea rdx, [rax + rcx*2]
00ABB796  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00ABB79A  E8 E1 EF 96 FF                  call 0x14042a780
00ABB79F  48 8D 15 AA 5F 55 FF            lea rdx, [rip - 0xaaa056]
00ABB7A6  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00ABB7AA  E8 D1 EF 96 FF                  call 0x14042a780
00ABB7AF  41 B0 01                        mov r8b, 1
00ABB7B2  48 8D 55 18                     lea rdx, [rbp + 0x18]
00ABB7B6  48 8D 4D 48                     lea rcx, [rbp + 0x48]
00ABB7BA  E8 B1 97 E3 FF                  call 0x1408f4f70
00ABB7BF  33 D2                           xor edx, edx
00ABB7C1  84 C0                           test al, al
00ABB7C3  0F 84 ED 01 00 00               je 0x140abb9b6
00ABB7C9  0F B7 4D 48                     movzx ecx, word ptr [rbp + 0x48]
00ABB7CD  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
00ABB7D1  48 D1 E9                        shr rcx, 1
00ABB7D4  66 83 3C 48 5C                  cmp word ptr [rax + rcx*2], 0x5c
00ABB7D9  0F 85 D7 01 00 00               jne 0x140abb9b6
00ABB7DF  85 F6                           test esi, esi
00ABB7E1  0F 85 8F 00 00 00               jne 0x140abb876
00ABB7E7  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00ABB7EB  4C 8D 45 94                     lea r8, [rbp - 0x6c]
00ABB7EF  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00ABB7F3  E8 28 F9 F6 FF                  call 0x140a2b120
00ABB7F8  8B F8                           mov edi, eax
00ABB7FA  85 C0                           test eax, eax
00ABB7FC  0F 88 C2 01 00 00               js 0x140abb9c4
00ABB802  F6 45 98 08                     test byte ptr [rbp - 0x68], 8
00ABB806  75 34                           jne 0x140abb83c
00ABB808  48 8D 15 A9 6A 55 FF            lea rdx, [rip - 0xaa9557]
00ABB80F  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00ABB813  E8 68 EF 96 FF                  call 0x14042a780
00ABB818  4C 8D 4D 90                     lea r9, [rbp - 0x70]
00ABB81C  45 33 C0                        xor r8d, r8d
00ABB81F  B2 01                           mov dl, 1
00ABB821  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00ABB825  E8 56 EF EB FF                  call 0x14097a780
00ABB82A  8B F8                           mov edi, eax
00ABB82C  85 C0                           test eax, eax
00ABB82E  0F 88 90 01 00 00               js 0x140abb9c4
00ABB834  8B 75 94                        mov esi, dword ptr [rbp - 0x6c]
00ABB837  03 75 90                        add esi, dword ptr [rbp - 0x70]
00ABB83A  EB 03                           jmp 0x140abb83f
00ABB83C  8B 75 94                        mov esi, dword ptr [rbp - 0x6c]
00ABB83F  48 8D 15 5A 6A 55 FF            lea rdx, [rip - 0xaa95a6]
00ABB846  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00ABB84A  E8 31 EF 96 FF                  call 0x14042a780
00ABB84F  4C 8D 4D 90                     lea r9, [rbp - 0x70]
00ABB853  45 33 C0                        xor r8d, r8d
00ABB856  B2 01                           mov dl, 1
00ABB858  48 8D 4D 18                     lea rcx, [rbp + 0x18]
00ABB85C  E8 1F EF EB FF                  call 0x14097a780
00ABB861  33 D2                           xor edx, edx
00ABB863  8B F8                           mov edi, eax
00ABB865  85 C0                           test eax, eax
00ABB867  0F 88 57 01 00 00               js 0x140abb9c4
00ABB86D  03 75 90                        add esi, dword ptr [rbp - 0x70]
00ABB870  89 75 B8                        mov dword ptr [rbp - 0x48], esi
00ABB873  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00ABB876  41 39 B6 AC 02 00 00            cmp dword ptr [r14 + 0x2ac], esi
00ABB87D  0F 85 33 01 00 00               jne 0x140abb9b6
00ABB883  4D 85 FF                        test r15, r15
00ABB886  75 2A                           jne 0x140abb8b2
00ABB888  BA 00 08 00 00                  mov edx, 0x800
00ABB88D  C7 45 B0 00 08 00 00            mov dword ptr [rbp - 0x50], 0x800
00ABB894  B9 00 01 00 00                  mov ecx, 0x100
00ABB899  41 B8 50 70 20 20               mov r8d, 0x20207050
00ABB89F  E8 4C 68 0C 00                  call 0x140b820f0
00ABB8A4  33 D2                           xor edx, edx
00ABB8A6  4C 8B F8                        mov r15, rax
00ABB8A9  48 85 C0                        test rax, rax
00ABB8AC  0F 84 0D 01 00 00               je 0x140abb9bf
00ABB8B2  44 8B 65 B0                     mov r12d, dword ptr [rbp - 0x50]
00ABB8B6  48 8D 5D 68                     lea rbx, [rbp + 0x68]
00ABB8BA  48 89 5D 00                     mov qword ptr [rbp], rbx
00ABB8BE  4C 8D 6D 78                     lea r13, [rbp + 0x78]
00ABB8C2  8B F2                           mov esi, edx
00ABB8C4  44 8B 0B                        mov r9d, dword ptr [rbx]
00ABB8C7  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00ABB8CC  48 8B 0D C5 AA 3A 00            mov rcx, qword ptr [rip + 0x3aaac5]
00ABB8D3  45 33 C0                        xor r8d, r8d
00ABB8D6  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00ABB8DA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ABB8DF  48 8D 45 B4                     lea rax, [rbp - 0x4c]
00ABB8E3  44 89 64 24 70                  mov dword ptr [rsp + 0x70], r12d
00ABB8E8  49 8B 56 30                     mov rdx, qword ptr [r14 + 0x30]
00ABB8EC  4C 89 7C 24 28                  mov qword ptr [rsp + 0x28], r15
00ABB8F1  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ABB8F6  E8 75 1F E3 FF                  call 0x1408ed870
00ABB8FB  33 D2                           xor edx, edx
00ABB8FD  8B F8                           mov edi, eax
00ABB8FF  85 C0                           test eax, eax
00ABB901  78 0F                           js 0x140abb912
00ABB903  83 7D B4 07                     cmp dword ptr [rbp - 0x4c], 7
00ABB907  75 09                           jne 0x140abb912
00ABB909  8D 42 02                        lea eax, [rdx + 2]
00ABB90C  39 44 24 70                     cmp dword ptr [rsp + 0x70], eax
00ABB910  73 06                           jae 0x140abb918
00ABB912  66 41 89 17                     mov word ptr [r15], dx
00ABB916  8B FA                           mov edi, edx
00ABB918  83 FE 01                        cmp esi, 1
00ABB91B  75 50                           jne 0x140abb96d
00ABB91D  49 8B DF                        mov rbx, r15
00ABB920  66 39 13                        cmp word ptr [rbx], dx
00ABB923  74 44                           je 0x140abb969
00ABB925  48 8D 15 8C 69 55 FF            lea rdx, [rip - 0xaa9674]
00ABB92C  48 8B CB                        mov rcx, rbx
00ABB92F  E8 4C 47 A4 FF                  call 0x140500080
00ABB934  33 D2                           xor edx, edx
00ABB936  85 C0                           test eax, eax
00ABB938  74 2C                           je 0x140abb966
00ABB93A  48 8D 15 5F 69 55 FF            lea rdx, [rip - 0xaa96a1]
00ABB941  48 8B CB                        mov rcx, rbx
00ABB944  E8 37 47 A4 FF                  call 0x140500080
00ABB949  33 D2                           xor edx, edx
00ABB94B  85 C0                           test eax, eax
00ABB94D  74 17                           je 0x140abb966
00ABB94F  48 83 C8 FF                     or rax, 0xffffffffffffffff
00ABB953  48 FF C0                        inc rax
00ABB956  66 39 14 43                     cmp word ptr [rbx + rax*2], dx
00ABB95A  75 F7                           jne 0x140abb953
00ABB95C  48 8D 1C 43                     lea rbx, [rbx + rax*2]
00ABB960  48 83 C3 02                     add rbx, 2
00ABB964  EB BA                           jmp 0x140abb920
00ABB966  66 89 13                        mov word ptr [rbx], dx
00ABB969  48 8B 5D 00                     mov rbx, qword ptr [rbp]
00ABB96D  49 8B 4D 00                     mov rcx, qword ptr [r13]
00ABB971  48 85 C9                        test rcx, rcx
00ABB974  74 13                           je 0x140abb989
00ABB976  41 B0 01                        mov r8b, 1
00ABB979  49 8B D7                        mov rdx, r15
00ABB97C  E8 FB 18 C8 FF                  call 0x14073d27c
00ABB981  33 D2                           xor edx, edx
00ABB983  84 C0                           test al, al
00ABB985  75 08                           jne 0x140abb98f
00ABB987  EB 1D                           jmp 0x140abb9a6
00ABB989  66 41 39 17                     cmp word ptr [r15], dx
00ABB98D  75 17                           jne 0x140abb9a6
00ABB98F  48 83 C3 04                     add rbx, 4
00ABB993  FF C6                           inc esi
00ABB995  49 83 C5 08                     add r13, 8
00ABB999  48 89 5D 00                     mov qword ptr [rbp], rbx
00ABB99D  83 FE 02                        cmp esi, 2
00ABB9A0  0F 82 1E FF FF FF               jb 0x140abb8c4
00ABB9A6  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
00ABB9AA  83 FE 02                        cmp esi, 2
00ABB9AD  0F 83 31 01 00 00               jae 0x140abbae4
00ABB9B3  8B 75 B8                        mov esi, dword ptr [rbp - 0x48]
00ABB9B6  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
00ABB9BA  E9 77 FD FF FF                  jmp 0x140abb736
00ABB9BF  BF 9A 00 00 C0                  mov edi, 0xc000009a
00ABB9C4  4C 8B 75 88                     mov r14, qword ptr [rbp - 0x78]
00ABB9C8  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
00ABB9CC  48 8B 5C 24 78                  mov rbx, qword ptr [rsp + 0x78]
00ABB9D1  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00ABB9D5  45 33 E4                        xor r12d, r12d
00ABB9D8  48 85 C9                        test rcx, rcx
00ABB9DB  74 05                           je 0x140abb9e2
00ABB9DD  E8 6E 6E 0C 00                  call 0x140b82850
00ABB9E2  48 85 DB                        test rbx, rbx
00ABB9E5  74 0A                           je 0x140abb9f1
00ABB9E7  33 D2                           xor edx, edx
00ABB9E9  48 8B CB                        mov rcx, rbx
00ABB9EC  E8 7F 6E 0C 00                  call 0x140b82870
00ABB9F1  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
00ABB9F5  48 85 C9                        test rcx, rcx
00ABB9F8  74 0C                           je 0x140abba06
00ABB9FA  E8 51 6E 0C 00                  call 0x140b82850
00ABB9FF  0F 57 C0                        xorps xmm0, xmm0
00ABBA02  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00ABBA06  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
00ABBA0A  48 85 C9                        test rcx, rcx
00ABBA0D  74 0C                           je 0x140abba1b
00ABBA0F  E8 3C 6E 0C 00                  call 0x140b82850
00ABBA14  0F 57 C0                        xorps xmm0, xmm0
00ABBA17  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00ABBA1B  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
00ABBA1F  48 85 C9                        test rcx, rcx
00ABBA22  74 0C                           je 0x140abba30
00ABBA24  E8 27 6E 0C 00                  call 0x140b82850
00ABBA29  0F 57 C0                        xorps xmm0, xmm0
00ABBA2C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00ABBA30  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00ABBA34  48 85 C9                        test rcx, rcx
00ABBA37  74 0C                           je 0x140abba45
00ABBA39  E8 12 6E 0C 00                  call 0x140b82850
00ABBA3E  0F 57 C0                        xorps xmm0, xmm0
00ABBA41  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
00ABBA45  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00ABBA49  48 85 C9                        test rcx, rcx
00ABBA4C  74 0C                           je 0x140abba5a
00ABBA4E  E8 FD 6D 0C 00                  call 0x140b82850
00ABBA53  0F 57 C0                        xorps xmm0, xmm0
00ABBA56  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
00ABBA5A  4D 85 F6                        test r14, r14
00ABBA5D  74 0A                           je 0x140abba69
00ABBA5F  33 D2                           xor edx, edx
00ABBA61  49 8B CE                        mov rcx, r14
00ABBA64  E8 07 6E 0C 00                  call 0x140b82870
00ABBA69  4D 85 FF                        test r15, r15
00ABBA6C  74 0A                           je 0x140abba78
00ABBA6E  33 D2                           xor edx, edx
00ABBA70  49 8B CF                        mov rcx, r15
00ABBA73  E8 F8 6D 0C 00                  call 0x140b82870
00ABBA78  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00ABBA7C  48 85 C9                        test rcx, rcx
00ABBA7F  74 05                           je 0x140abba86
00ABBA81  E8 2A 18 BF FF                  call 0x1406ad2b0
00ABBA86  85 FF                           test edi, edi
00ABBA88  79 2A                           jns 0x140abbab4
00ABBA8A  F6 05 9B 46 43 00 04            test byte ptr [rip + 0x43469b], 4
00ABBA91  74 21                           je 0x140abbab4
00ABBA93  4D 8B 4D 00                     mov r9, qword ptr [r13]
00ABBA97  48 8D 15 82 B8 56 FF            lea rdx, [rip - 0xa9477e]
00ABBA9E  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
00ABBAA2  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00ABBAA6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ABBAAB  4D 8B 49 30                     mov r9, qword ptr [r9 + 0x30]
00ABBAAF  E8 60 89 96 FF                  call 0x140424414
00ABBAB4  45 39 65 08                     cmp dword ptr [r13 + 8], r12d
00ABBAB8  7C 04                           jl 0x140abbabe
00ABBABA  41 89 7D 08                     mov dword ptr [r13 + 8], edi
00ABBABE  33 C0                           xor eax, eax
00ABBAC0  48 8B 8D 30 02 00 00            mov rcx, qword ptr [rbp + 0x230]
00ABBAC7  48 33 CC                        xor rcx, rsp
00ABBACA  E8 71 0B BF FF                  call 0x1406ac640
00ABBACF  48 81 C4 48 03 00 00            add rsp, 0x348
00ABBAD6  41 5F                           pop r15
00ABBAD8  41 5E                           pop r14
00ABBADA  41 5D                           pop r13
00ABBADC  41 5C                           pop r12
00ABBADE  5F                              pop rdi
00ABBADF  5E                              pop rsi
00ABBAE0  5B                              pop rbx
00ABBAE1  5D                              pop rbp
00ABBAE2  C3                              ret
00ABBAE3  CC                              int3
00ABBAE4  BF 04 07 00 C0                  mov edi, 0xc0000704
00ABBAE9  E9 D6 FE FF FF                  jmp 0x140abb9c4
00ABBAEE  85 C0                           test eax, eax
00ABBAF0  0F 88 CE FE FF FF               js 0x140abb9c4
00ABBAF6  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
00ABBAFA  4C 8D 4D 88                     lea r9, [rbp - 0x78]
00ABBAFE  45 33 C0                        xor r8d, r8d
00ABBB01  48 8D 15 58 12 04 00            lea rdx, [rip + 0x41258]
00ABBB08  E8 DF D5 ED FF                  call 0x1409990ec
00ABBB0D  4C 8B 75 88                     mov r14, qword ptr [rbp - 0x78]
00ABBB11  8B F8                           mov edi, eax
00ABBB13  85 C0                           test eax, eax
00ABBB15  79 0D                           jns 0x140abbb24
00ABBB17  3D 34 00 00 C0                  cmp eax, 0xc0000034
00ABBB1C  0F 85 A6 FE FF FF               jne 0x140abb9c8
00ABBB22  EB 26                           jmp 0x140abbb4a
00ABBB24  41 83 7E 04 03                  cmp dword ptr [r14 + 4], 3
00ABBB29  0F 85 7E 03 00 00               jne 0x140abbead
00ABBB2F  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
00ABBB33  89 45 BC                        mov dword ptr [rbp - 0x44], eax
00ABBB36  83 F8 28                        cmp eax, 0x28
00ABBB39  0F 82 6E 03 00 00               jb 0x140abbead
00ABBB3F  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00ABBB43  49 03 C6                        add rax, r14
00ABBB46  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
00ABBB4A  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
00ABBB4E  49 8B 4D 00                     mov rcx, qword ptr [r13]
00ABBB52  48 3B 0D DF 08 4D 00            cmp rcx, qword ptr [rip + 0x4d08df]
00ABBB59  0F 84 2F 01 00 00               je 0x140abbc8e
00ABBB5F  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00ABBB63  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00ABBB68  33 D2                           xor edx, edx
00ABBB6A  E8 B9 38 FB FF                  call 0x140a6f428
00ABBB6F  8B F8                           mov edi, eax
00ABBB71  85 C0                           test eax, eax
00ABBB73  0F 88 53 FE FF FF               js 0x140abb9cc
00ABBB79  48 8B 75 08                     mov rsi, qword ptr [rbp + 8]
00ABBB7D  49 83 CD FF                     or r13, 0xffffffffffffffff
00ABBB81  49 8B CD                        mov rcx, r13
00ABBB84  45 33 FF                        xor r15d, r15d
00ABBB87  48 FF C1                        inc rcx
00ABBB8A  66 44 39 3C 4E                  cmp word ptr [rsi + rcx*2], r15w
00ABBB8F  75 F6                           jne 0x140abbb87
00ABBB91  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00ABBB96  49 FF C5                        inc r13
00ABBB99  66 46 39 3C 6F                  cmp word ptr [rdi + r13*2], r15w
00ABBB9E  75 F6                           jne 0x140abbb96
00ABBBA0  8D 41 02                        lea eax, [rcx + 2]
00ABBBA3  41 B8 53 74 72 67               mov r8d, 0x67727453
00ABBBA9  66 41 03 C5                     add ax, r13w
00ABBBAD  66 03 C0                        add ax, ax
00ABBBB0  66 89 45 5A                     mov word ptr [rbp + 0x5a], ax
00ABBBB4  4A 8D 04 29                     lea rax, [rcx + r13]
00ABBBB8  48 8D 04 45 04 00 00 00         lea rax, [rax*2 + 4]
00ABBBC0  B9 00 01 00 00                  mov ecx, 0x100
00ABBBC5  0F B7 D0                        movzx edx, ax
00ABBBC8  E8 23 65 0C 00                  call 0x140b820f0
00ABBBCD  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
00ABBBD1  48 85 C0                        test rax, rax
00ABBBD4  75 0D                           jne 0x140abbbe3
00ABBBD6  BF 9A 00 00 C0                  mov edi, 0xc000009a
00ABBBDB  4C 8B FB                        mov r15, rbx
00ABBBDE  E9 E5 FD FF FF                  jmp 0x140abb9c8
00ABBBE3  4C 8B CF                        mov r9, rdi
00ABBBE6  48 8D 15 B3 46 04 00            lea rdx, [rip + 0x446b3]
00ABBBED  4C 8B C6                        mov r8, rsi
00ABBBF0  48 8D 4D 58                     lea rcx, [rbp + 0x58]
00ABBBF4  E8 8B FD 9C FF                  call 0x14048b984
00ABBBF9  8B F8                           mov edi, eax
00ABBBFB  4C 8B FB                        mov r15, rbx
00ABBBFE  85 C0                           test eax, eax
00ABBC00  0F 88 C2 FD FF FF               js 0x140abb9c8
00ABBC06  44 8B 6D C0                     mov r13d, dword ptr [rbp - 0x40]
00ABBC0A  4C 8B FB                        mov r15, rbx
00ABBC0D  48 8B 5D 70                     mov rbx, qword ptr [rbp + 0x70]
00ABBC11  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
00ABBC15  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00ABBC1A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00ABBC1F  45 33 C9                        xor r9d, r9d
00ABBC22  44 89 6C 24 28                  mov dword ptr [rsp + 0x28], r13d
00ABBC27  45 33 C0                        xor r8d, r8d
00ABBC2A  48 8B CB                        mov rcx, rbx
00ABBC2D  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00ABBC32  4D 8B F4                        mov r14, r12
00ABBC35  E8 3E 67 ED FF                  call 0x140992378
00ABBC3A  8B F8                           mov edi, eax
00ABBC3C  3D 23 00 00 C0                  cmp eax, 0xc0000023
00ABBC41  75 74                           jne 0x140abbcb7
00ABBC43  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00ABBC47  41 3B C5                        cmp eax, r13d
00ABBC4A  76 61                           jbe 0x140abbcad
00ABBC4C  4D 85 E4                        test r12, r12
00ABBC4F  74 0E                           je 0x140abbc5f
00ABBC51  33 D2                           xor edx, edx
00ABBC53  49 8B CC                        mov rcx, r12
00ABBC56  E8 15 6C 0C 00                  call 0x140b82870
00ABBC5B  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00ABBC5F  44 8B E8                        mov r13d, eax
00ABBC62  B9 00 01 00 00                  mov ecx, 0x100
00ABBC67  41 B8 50 70 20 20               mov r8d, 0x20207050
00ABBC6D  4A 8D 14 AD 00 00 00 00         lea rdx, [r13*4]
00ABBC75  49 03 D5                        add rdx, r13
00ABBC78  48 C1 E2 02                     shl rdx, 2
00ABBC7C  E8 6F 64 0C 00                  call 0x140b820f0
00ABBC81  4C 8B E0                        mov r12, rax
00ABBC84  48 85 C0                        test rax, rax
00ABBC87  75 88                           jne 0x140abbc11
00ABBC89  E9 31 FD FF FF                  jmp 0x140abb9bf
00ABBC8E  48 8B 55 08                     mov rdx, qword ptr [rbp + 8]
00ABBC92  48 8D 4D 58                     lea rcx, [rbp + 0x58]
00ABBC96  E8 C5 1B F0 FF                  call 0x1409bd860
00ABBC9B  84 C0                           test al, al
00ABBC9D  0F 85 63 FF FF FF               jne 0x140abbc06
00ABBCA3  BF 9A 00 00 C0                  mov edi, 0xc000009a
00ABBCA8  E9 1F FD FF FF                  jmp 0x140abb9cc
00ABBCAD  BF E5 00 00 C0                  mov edi, 0xc00000e5
00ABBCB2  E9 24 01 00 00                  jmp 0x140abbddb
00ABBCB7  8B 74 24 70                     mov esi, dword ptr [rsp + 0x70]
00ABBCBB  85 C0                           test eax, eax
00ABBCBD  0F 88 18 01 00 00               js 0x140abbddb
00ABBCC3  33 FF                           xor edi, edi
00ABBCC5  85 F6                           test esi, esi
00ABBCC7  0F 84 53 01 00 00               je 0x140abbe20
00ABBCCD  48 8D 14 76                     lea rdx, [rsi + rsi*2]
00ABBCD1  B9 00 01 00 00                  mov ecx, 0x100
00ABBCD6  48 C1 E2 04                     shl rdx, 4
00ABBCDA  41 B8 50 70 20 20               mov r8d, 0x20207050
00ABBCE0  E8 0B 64 0C 00                  call 0x140b820f0
00ABBCE5  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00ABBCE9  48 85 C0                        test rax, rax
00ABBCEC  75 0A                           jne 0x140abbcf8
00ABBCEE  BF 9A 00 00 C0                  mov edi, 0xc000009a
00ABBCF3  E9 E3 00 00 00                  jmp 0x140abbddb
00ABBCF8  49 8B D6                        mov rdx, r14
00ABBCFB  48 8D 58 20                     lea rbx, [rax + 0x20]
00ABBCFF  48 89 55 A0                     mov qword ptr [rbp - 0x60], rdx
00ABBD03  44 8B E7                        mov r12d, edi
00ABBD06  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00ABBD0A  0F 11 43 E0                     movups xmmword ptr [rbx - 0x20], xmm0
00ABBD0E  41 8B 46 10                     mov eax, dword ptr [r14 + 0x10]
00ABBD12  89 43 F0                        mov dword ptr [rbx - 0x10], eax
00ABBD15  41 8B C4                        mov eax, r12d
00ABBD18  89 7B F4                        mov dword ptr [rbx - 0xc], edi
00ABBD1B  48 8D 0C 80                     lea rcx, [rax + rax*4]
00ABBD1F  4C 8D 2C 8A                     lea r13, [rdx + rcx*4]
00ABBD23  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
00ABBD27  48 8D 44 24 70                  lea rax, [rsp + 0x70]
00ABBD2C  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
00ABBD30  4D 8B CD                        mov r9, r13
00ABBD33  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00ABBD38  45 33 C0                        xor r8d, r8d
00ABBD3B  8B 43 04                        mov eax, dword ptr [rbx + 4]
00ABBD3E  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00ABBD42  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00ABBD46  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00ABBD4B  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00ABBD50  E8 4B 3E E3 FF                  call 0x1408efba0
00ABBD55  8B F8                           mov edi, eax
00ABBD57  3D 23 00 00 C0                  cmp eax, 0xc0000023
00ABBD5C  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00ABBD60  0F 85 8D 00 00 00               jne 0x140abbdf3
00ABBD66  3B 43 04                        cmp eax, dword ptr [rbx + 4]
00ABBD69  0F 86 A6 00 00 00               jbe 0x140abbe15
00ABBD6F  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00ABBD73  48 85 C9                        test rcx, rcx
00ABBD76  74 0B                           je 0x140abbd83
00ABBD78  33 D2                           xor edx, edx
00ABBD7A  E8 F1 6A 0C 00                  call 0x140b82870
00ABBD7F  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
00ABBD83  89 43 04                        mov dword ptr [rbx + 4], eax
00ABBD86  B9 00 01 00 00                  mov ecx, 0x100
00ABBD8B  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
00ABBD8F  41 B8 50 70 20 20               mov r8d, 0x20207050
00ABBD95  E8 56 63 0C 00                  call 0x140b820f0
00ABBD9A  48 89 43 08                     mov qword ptr [rbx + 8], rax
00ABBD9E  48 85 C0                        test rax, rax
00ABBDA1  75 80                           jne 0x140abbd23
00ABBDA3  BF 9A 00 00 C0                  mov edi, 0xc000009a
00ABBDA8  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
00ABBDAC  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
00ABBDB0  85 F6                           test esi, esi
00ABBDB2  74 1D                           je 0x140abbdd1
00ABBDB4  49 8D 5E 28                     lea rbx, [r14 + 0x28]
00ABBDB8  48 8B 0B                        mov rcx, qword ptr [rbx]
00ABBDBB  48 85 C9                        test rcx, rcx
00ABBDBE  74 07                           je 0x140abbdc7
00ABBDC0  33 D2                           xor edx, edx
00ABBDC2  E8 A9 6A 0C 00                  call 0x140b82870
00ABBDC7  48 83 C3 30                     add rbx, 0x30
00ABBDCB  48 83 EE 01                     sub rsi, 1
00ABBDCF  75 E7                           jne 0x140abbdb8
00ABBDD1  33 D2                           xor edx, edx
00ABBDD3  49 8B CE                        mov rcx, r14
00ABBDD6  E8 95 6A 0C 00                  call 0x140b82870
00ABBDDB  4D 85 E4                        test r12, r12
00ABBDDE  0F 84 E0 FB FF FF               je 0x140abb9c4
00ABBDE4  33 D2                           xor edx, edx
00ABBDE6  49 8B CC                        mov rcx, r12
00ABBDE9  E8 82 6A 0C 00                  call 0x140b82870
00ABBDEE  E9 D1 FB FF FF                  jmp 0x140abb9c4
00ABBDF3  89 43 04                        mov dword ptr [rbx + 4], eax
00ABBDF6  85 FF                           test edi, edi
00ABBDF8  78 AE                           js 0x140abbda8
00ABBDFA  41 FF C4                        inc r12d
00ABBDFD  48 83 C3 30                     add rbx, 0x30
00ABBE01  49 83 C6 14                     add r14, 0x14
00ABBE05  44 3B E6                        cmp r12d, esi
00ABBE08  73 12                           jae 0x140abbe1c
00ABBE0A  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
00ABBE0E  33 FF                           xor edi, edi
00ABBE10  E9 F1 FE FF FF                  jmp 0x140abbd06
00ABBE15  BF E5 00 00 C0                  mov edi, 0xc00000e5
00ABBE1A  EB 8C                           jmp 0x140abbda8
00ABBE1C  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
00ABBE20  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
00ABBE24  48 8B 45 F8                     mov rax, qword ptr [rbp - 8]
00ABBE28  48 8B D9                        mov rbx, rcx
00ABBE2B  48 8B 55 80                     mov rdx, qword ptr [rbp - 0x80]
00ABBE2F  48 F7 D8                        neg rax
00ABBE32  4C 8B 4D D8                     mov r9, qword ptr [rbp - 0x28]
00ABBE36  48 8D 85 88 00 00 00            lea rax, [rbp + 0x88]
00ABBE3D  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
00ABBE41  4D 1B C0                        sbb r8, r8
00ABBE44  4C 23 C0                        and r8, rax
00ABBE47  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
00ABBE4C  8B 45 BC                        mov eax, dword ptr [rbp - 0x44]
00ABBE4F  48 8D 0D FA 58 55 FF            lea rcx, [rip - 0xaaa706]
00ABBE56  48 8B 12                        mov rdx, qword ptr [rdx]
00ABBE59  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00ABBE5D  48 8B 45 10                     mov rax, qword ptr [rbp + 0x10]
00ABBE61  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00ABBE66  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
00ABBE6A  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
00ABBE6E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00ABBE73  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00ABBE77  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00ABBE7C  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
00ABBE7F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00ABBE83  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
00ABBE87  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
00ABBE8C  4C 8B 45 60                     mov r8, qword ptr [rbp + 0x60]
00ABBE90  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00ABBE95  E8 32 F4 C7 FF                  call 0x14073b2cc
00ABBE9A  8B F8                           mov edi, eax
00ABBE9C  4C 8B F3                        mov r14, rbx
00ABBE9F  48 85 DB                        test rbx, rbx
00ABBEA2  0F 85 08 FF FF FF               jne 0x140abbdb0
00ABBEA8  E9 2E FF FF FF                  jmp 0x140abbddb
00ABBEAD  BF 01 00 00 C0                  mov edi, 0xc0000001
00ABBEB2  E9 11 FB FF FF                  jmp 0x140abb9c8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiCreateDriverSwDeviceCallback(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned int v_stack_m138;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A8;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned int v_stack_m21C;
    unsigned int v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int16 v_stack_m22E;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned int v_stack_m2C8;
    unsigned int v_stack_m2CC;
    unsigned int v_stack_m2D0;
    unsigned int v_stack_m2D4;
    unsigned int v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned int v_stack_m2F0;
    unsigned int v_stack_m2F4;
    unsigned int v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned int v_stack_m318;
    unsigned int v_stack_m350;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;

    v_rsp = (v_rsp) - (840);
    result = (*(unsigned __int64 *)(v_rip + 3470077)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m218 = a1;
    v_stack_m308 = a4;
    v_stack_m280 = a3;
    a1 = 0;
    v_stack_m2D4 = 1;
    v_stack_m2E0 = 0;
    v_stack_m2F0 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2F4 = 0;
    v_stack_m2F8 = 0;
    v_stack_m2D8 = 0;
    v_stack_m300 = 0;
    v_stack_m278 = 0;
    v_stack_m2CC = 0;
    v_stack_m310 = 0;
    v_stack_m2C8 = 0;
    v_stack_m2E8 = 0;
    v_stack_m2C0 = 0;
    v_stack_m318 = 0;
    v_stack_m2B8 = v_xmm0;
    v_stack_m2A8 = v_xmm1;
    v_stack_m298 = v_xmm0;
    v_stack_m200 = v_xmm1;
    v_stack_m260 = v_xmm0;
    v_stack_m250 = v_xmm1;
    v_stack_m270 = v_xmm0;
    v_stack_m240 = v_xmm1;
    v_stack_m230 = v_xmm0;
    if (0 == 0) goto loc_00ABB4EF;
    if (*(unsigned __int64 *)(a1 + 224) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 224) + 8);
    }
    v_stack_m360 = a1;
    v_stack_m368 = v_stack_m2E0;
    a3 = 0;
    result = _RegRtlOpenKeyTransacted(a2, 0, a3, (unsigned int)(0x20019ULL));
    if (sign_flag) goto loc_00ABB9D1;
    a2 = 0;
    result = memset(v_stack_m1E8, a2, 392, (unsigned int)(0x20019ULL));
    v_stack_m120 = 0x4000000ULL;
    v_stack_m1E0 = 304;
    v_stack_m1C8 = (unsigned int)((unsigned int)(0x7000000ULL));
    v_stack_m1D8 = v_rip + 278138;
    v_stack_m1A8 = 304;
    v_stack_m1D0 = v_stack_m2B8;
    v_stack_m190 = (unsigned int)((unsigned int)(0x7000000ULL));
    v_stack_m1A0 = v_rip + 277865;
    v_stack_m170 = 288;
    v_stack_m198 = v_stack_m2A8;
    a4 = 0;
    v_stack_m158 = (unsigned int)((unsigned int)(0x1000000ULL));
    v_stack_m168 = v_rip + 281810;
    v_stack_m160 = v_stack_m298;
    v_stack_m130 = v_rip + 277859;
    v_stack_m128 = v_stack_m2F0;
    v_stack_mF8 = v_rip + 277482;
    v_stack_mF0 = v_stack_m260;
    v_stack_mC0 = v_rip + 278001;
    v_stack_m138 = 288;
    v_stack_m100 = 288;
    v_stack_mE8 = (unsigned int)((unsigned int)(0x1000000ULL));
    v_stack_mC8 = 288;
    v_stack_mB0 = (unsigned int)((unsigned int)(0x1000000ULL));
    v_stack_mB8 = v_stack_m250;
    v_stack_m360 = 1;
    result = RtlpQueryRegistryValues((unsigned int)(0xC0000000ULL), v_stack_m2E0, v_stack_m1E8, a4);
    a2 = 0;
    if (sign_flag) goto loc_00ABB9D1;
    if (v_stack_m2B0 == 0) goto loc_00ABB66B;
    result = a2 + 2;
    if (v_stack_m2B8 <= ((unsigned __int16)(a2 + 2))) {
        a1 = v_stack_m2B8;
        result = RtlFreeAnsiString(a1, a2, v_stack_m1E8, a4);
        a2 = 0;
        result = a2 + 2;
    }
    if (v_stack_m2A0 == 0) goto loc_00ABB682;
    if (v_stack_m2A8 <= ((unsigned __int16)(result))) {
        a1 = v_stack_m2A8;
        result = RtlFreeAnsiString(a1, a2, v_stack_m1E8, a4);
        a2 = 0;
    }
    if (v_stack_m290 == 0) goto loc_00ABB6BA;
    result = 2;
    if (v_stack_m298 < 2) {
        a1 = v_stack_m298;
        result = RtlFreeAnsiString(a1, a2, v_stack_m1E8, a4);
        a2 = 0;
    }
    if (v_stack_m290 == 0) goto loc_00ABB6BA;
    result = RtlGUIDFromString(v_stack_m298, v_stack_m200, v_stack_m1E8, a4);
    a2 = 0;
    if (sign_flag) {
        v_stack_m200 = v_xmm0;
    }
    if (v_stack_m258 == 0) goto loc_00ABB6E3;
    result = 2;
    if (v_stack_m260 < 2) {
        a1 = v_stack_m260;
        result = RtlFreeAnsiString(a1, a2, v_stack_m1E8, a4);
        a2 = 0;
        result = a2 + 2;
    }
    if (v_stack_m248 == 0) goto loc_00ABB6FA;
    if (v_stack_m250 < ((unsigned __int16)(result))) {
        a1 = v_stack_m250;
        result = RtlFreeAnsiString(a1, a2, v_stack_m1E8, a4);
        a2 = 0;
    }
    if (v_stack_m2B0 != 0) goto loc_00ABB710;
    if (v_stack_m2A0 != 0) goto loc_00ABB710;
    goto loc_00ABB9D1;
loc_00ABB710:
    v_stack_m210 = v_stack_m2B0;
    v_stack_m208 = v_stack_m2A0;
    v_stack_m220 = 2;
    v_stack_m21C = 3;
loc_00ABB736:
    if ((*(unsigned __int64 *)(a4)) == (*(unsigned __int64 *)(v_rip + 5049595))) goto loc_00ABBAEE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 32) + 8)) != (*(unsigned __int64 *)(v_rip + 5043381))) goto loc_00ABB9B6;
    result = RtlInitUnicodeString(v_stack_m240, v_rip - 11137300, v_stack_m1E8, a4);
    result = RtlPrefixUnicodeString(v_stack_m240, *(unsigned __int64 *)(a4) + 40, 1, a4);
    a2 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00ABB9B6;
    a1 = (v_stack_m240) >> (1);
    result = RtlInitUnicodeString(v_stack_m270, *(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 48) + a1 * 2, 1, a4);
    result = RtlInitUnicodeString(v_stack_m240, v_rip - 11182166, 1, a4);
    result = RtlPrefixUnicodeString(v_stack_m240, v_stack_m270, 1, a4);
    a2 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_00ABB9B6;
    a1 = (v_stack_m240) >> (1);
    if ((*(unsigned __int16 *)(v_stack_m268 + a1 * 2)) != 92) goto loc_00ABB9B6;
    if (0 != 0) goto loc_00ABB876;
    result = PnpGenerateDeviceIdsHash(v_stack_m2B0, v_stack_m2A0, v_stack_m2F4, a4);
    if (sign_flag) goto loc_00ABB9C4;
    if (((v_stack_m2F0) & (8)) != 0) goto loc_00ABB83C;
    result = RtlInitUnicodeString(v_stack_m270, v_rip - 11179351, v_stack_m2F4, a4);
    a3 = 0;
    result = RtlHashUnicodeString(v_stack_m270, 1, a3, v_stack_m2F8);
    if (sign_flag) goto loc_00ABB9C4;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m2F4)) + (v_stack_m2F8));
    goto loc_00ABB83F;
loc_00ABB83C:
loc_00ABB83F:
    result = RtlInitUnicodeString(v_stack_m270, v_rip - 11179430, a3, v_stack_m2F8);
    a3 = 0;
    result = RtlHashUnicodeString(v_stack_m270, 1, a3, v_stack_m2F8);
    a2 = 0;
    if (sign_flag) goto loc_00ABB9C4;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m2F4)) + (v_stack_m2F8));
    v_stack_m2D0 = (unsigned int)(v_rsi);
    v_stack_m2F4 = (unsigned int)(v_rsi);
loc_00ABB876:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a4) + 684)) != ((unsigned int)(v_rsi))) goto loc_00ABB9B6;
    if (0 != 0) goto loc_00ABB8B2;
    v_stack_m2D8 = 0x800ULL;
    result = ExAllocatePool2(256, (unsigned int)(0x800ULL), (unsigned int)(0x20207050ULL), v_stack_m2F8);
    a2 = 0;
    if (result == 0) goto loc_00ABB9BF;
loc_00ABB8B2:
    v_stack_m288 = v_stack_m220;
loc_00ABB8C4:
    a3 = 0;
    v_stack_m350 = 0;
    v_stack_m358 = v_stack_m318;
    v_stack_m318 = (unsigned int)((unsigned int)(v_stack_m2D8));
    v_stack_m360 = result;
    v_stack_m368 = v_stack_m2D4;
    result = CmGetDeviceRegProp(*(unsigned __int64 *)(v_rip + 3844805), *(unsigned __int64 *)(*(unsigned __int64 *)(a4) + 48), a3, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    a2 = 0;
    if (sign_flag) goto loc_00ABB912;
    if (v_stack_m2D4 != 7) goto loc_00ABB912;
    v_rdi = (unsigned int)((unsigned int)(result));
    if (v_stack_m318 < ((unsigned int)(a2 + 2))) {
        *(unsigned __int16 *)(result) = 0;
        v_rdi = 0;
    }
    if (0 != 1) goto loc_00ABB96D;
loc_00ABB920:
    if ((*(unsigned __int16 *)(result)) == 0) goto loc_00ABB969;
    result = wcsicmp(result, v_rip - 11179636, a3, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_00ABB966;
    result = wcsicmp(result, v_rip - 11179681, a3, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_00ABB966;
    result = (result) | (-1);
loc_00ABB953:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(result + result * 2)) != 0) goto loc_00ABB953;
    v_rbx = (result + result * 2) + (2);
    goto loc_00ABB920;
loc_00ABB966:
    *(unsigned __int16 *)(v_rbx) = 0;
loc_00ABB969:
loc_00ABB96D:
    if (*(unsigned __int64 *)(v_stack_m210) == 0) goto loc_00ABB989;
    result = PnpCompareMultiSz(*(unsigned __int64 *)(v_stack_m210), result, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    a2 = 0;
    if ((unsigned __int8)(result) != 0) goto loc_00ABB98F;
    goto loc_00ABB9A6;
loc_00ABB989:
    if ((*(unsigned __int16 *)(result)) != 0) goto loc_00ABB9A6;
loc_00ABB98F:
    v_rbx = (v_stack_m288) + (4);
    v_rsi = (unsigned int)((0) + 1);
    v_r13 = (v_stack_m210) + (8);
    v_stack_m288 = v_rbx;
    if (((unsigned int)(v_rsi)) < 2) goto loc_00ABB8C4;
loc_00ABB9A6:
    if (((unsigned int)(v_rsi)) >= 2) goto loc_00ABBAE4;
loc_00ABB9B6:
    goto loc_00ABB736;
loc_00ABB9BF:
loc_00ABB9C4:
loc_00ABB9C8:
loc_00ABB9CC:
loc_00ABB9D1:
    v_r12 = 0;
    if (v_stack_m228 != 0) {
        result = ExFreePool(v_stack_m228, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    }
    if (v_stack_m310 != 0) {
        a2 = 0;
        a1 = v_stack_m310;
        result = ExFreePoolWithTag(a1, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    }
    if (v_stack_m2B0 != 0) {
        result = ExFreePool(v_stack_m2B0, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
        v_stack_m2B8 = v_xmm0;
    }
    if (v_stack_m2A0 != 0) {
        result = ExFreePool(v_stack_m2A0, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
        v_stack_m2A8 = v_xmm0;
    }
    if (v_stack_m290 != 0) {
        result = ExFreePool(v_stack_m290, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
        v_stack_m298 = v_xmm0;
    }
    if (v_stack_m258 != 0) {
        result = ExFreePool(v_stack_m258, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
        v_stack_m260 = v_xmm0;
    }
    if (v_stack_m248 != 0) {
        result = ExFreePool(v_stack_m248, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
        v_stack_m250 = v_xmm0;
    }
    if (v_stack_m300 != 0) {
        a2 = 0;
        a1 = v_stack_m300;
        result = ExFreePoolWithTag(a1, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    }
    if (result != 0) {
        a2 = 0;
        a1 = result;
        result = ExFreePoolWithTag(a1, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    }
    if (v_stack_m2E0 != 0) {
        result = ZwClose(v_stack_m2E0, a2, 1, (unsigned int)(*(unsigned int *)(v_stack_m220)));
    }
    if (!sign_flag) goto loc_00ABBAB4;
    if (((*(unsigned __int8 *)(v_rip + 4408987)) & (4)) != 0) {
        a4 = *(unsigned __int64 *)(v_stack_m308);
        a2 = v_rip - 11093886;
        result = v_stack_m280;
        v_stack_m360 = (unsigned int)((unsigned int)(0xC000009AULL));
        v_stack_m368 = result;
        a4 = *(unsigned __int64 *)(a4 + 48);
        result = McTemplateK0zzd_EtwWriteTransfer(v_stack_m2E0, a2, 1, a4);
    }
    if ((*(unsigned int *)(v_stack_m308 + 8)) >= 0) {
        *(unsigned int *)(v_stack_m308 + 8) = (unsigned int)((unsigned int)(0xC000009AULL));
    }
    result = 0;
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, a4);
    v_rsp = (v_rsp) + (840);
    return result;
loc_00ABBAE4:
    goto loc_00ABB9C4;
loc_00ABBAEE:
    if (sign_flag) goto loc_00ABB9C4;
    a3 = 0;
    result = IopGetRegistryValue(v_stack_m2E0, v_rip + 266840, a3, v_stack_m300);
    if (!sign_flag) goto loc_00ABBB24;
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00ABB9C8;
    goto loc_00ABBB4A;
loc_00ABBB24:
    if ((*(unsigned int *)(v_stack_m300 + 4)) != 3) goto loc_00ABBEAD;
    v_stack_m2CC = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m300 + 12)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m300 + 12)))) < 40) goto loc_00ABBEAD;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m300 + 8))) + (v_stack_m300);
    v_stack_m278 = result;
loc_00ABBB4A:
    if ((*(unsigned __int64 *)(v_stack_m308)) == (*(unsigned __int64 *)(v_rip + 5048543))) goto loc_00ABBC8E;
    a2 = 0;
    result = PipMakeGloballyUniqueId(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m308) + 32), a2, v_stack_p78, v_stack_m300);
    if (sign_flag) goto loc_00ABB9CC;
    v_r13 = (v_stack_m308) | (-1);
    v_r15 = 0;
loc_00ABBB87:
    a1 = (v_r13) + 1;
    if ((*(unsigned __int16 *)(v_stack_m280 + a1 * 2)) != 0) goto loc_00ABBB87;
loc_00ABBB96:
    v_r13 = (v_r13) + 1;
    if ((*(unsigned __int16 *)(v_stack_p78 + v_r13 * 2)) != 0) goto loc_00ABBB96;
    result = (unsigned __int16)((a1 + 2) + ((unsigned __int16)(v_r13)));
    result = (unsigned __int16)((result) + ((unsigned __int16)(result)));
    v_stack_m22E = (unsigned __int16)(result);
    result = ExAllocatePool2(256, (unsigned __int16)(a1 + v_r13 * 1 * 2 + 4), (unsigned int)(0x67727453ULL), v_stack_m300);
    v_stack_m228 = result;
    if (result != 0) goto loc_00ABBBE3;
    goto loc_00ABB9C8;
loc_00ABBBE3:
    result = RtlUnicodeStringPrintf(v_stack_m230, v_rip + 280243, v_stack_m280, (unsigned int)(0xC000009AULL));
    if (sign_flag) goto loc_00ABB9C8;
loc_00ABBC06:
loc_00ABBC11:
    v_stack_p30 = v_stack_p70;
    a4 = 0;
    v_stack_p28 = (unsigned int)((unsigned int)(v_stack_m2C8));
    a3 = 0;
    v_stack_p20 = 0;
    result = PnpGetGenericStorePropertyKeys(v_stack_m218, v_stack_m2E0, a3, a4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00ABBCB7;
    if (((unsigned int)((unsigned int)(v_stack_p70))) <= ((unsigned int)((unsigned int)(v_stack_m2C8)))) goto loc_00ABBCAD;
    result = (unsigned int)(v_stack_p70);
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
        result = v_stack_p70;
    }
    a2 = ((unsigned int)((unsigned int)(result)) * 4) + ((unsigned int)((unsigned int)(result)));
    a2 = (a2) << (2);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20207050ULL), a4);
    if (result != 0) goto loc_00ABBC11;
    goto loc_00ABB9BF;
loc_00ABBC8E:
    result = RtlCreateUnicodeString(v_stack_m230, v_stack_m280, (unsigned int)(0x20207050ULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00ABBC06;
    goto loc_00ABB9CC;
loc_00ABBCAD:
    goto loc_00ABBDDB;
loc_00ABBCB7:
    if (sign_flag) goto loc_00ABBDDB;
    v_rdi = 0;
    if ((unsigned int)((unsigned int)(v_stack_p70)) == 0) goto loc_00ABBE20;
    a2 = ((unsigned int)(v_stack_p70) + (unsigned int)(v_stack_p70) * 2) << (4);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20207050ULL), a4);
    v_stack_m2C0 = result;
    if (result != 0) goto loc_00ABBCF8;
    goto loc_00ABBDDB;
loc_00ABBCF8:
    v_stack_m2E8 = 0;
loc_00ABBD06:
    *(unsigned __int64 *)(result + 32 - 32) = v_xmm0;
    *(unsigned int *)(result + 32 - 16) = (unsigned int)((unsigned int)(*(unsigned int *)(0 + 16)));
    *(unsigned int *)(result + 32 - 12) = (unsigned int)((unsigned int)(0xC000009AULL));
loc_00ABBD23:
    v_stack_p38 = v_stack_p70;
    a3 = 0;
    v_stack_p30 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 32 + 4)));
    v_stack_p28 = *(unsigned __int64 *)(result + 32 + 8);
    v_stack_p20 = result + 32;
    result = PnpGetGenericStoreProperty(v_stack_m218, v_stack_m2E0, a3, 0 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) * 4 * 4);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_00ABBDF3;
    if (((unsigned int)((unsigned int)(v_stack_p70))) <= (*(unsigned int *)(result + 32 + 4))) goto loc_00ABBE15;
    result = (unsigned int)(v_stack_p70);
    if (*(unsigned __int64 *)(result + 32 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(result + 32 + 8), a2, a3, 0 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) * 4 * 4);
        result = v_stack_p70;
    }
    *(unsigned int *)(result + 32 + 4) = (unsigned int)(result);
    result = ExAllocatePool2(256, (unsigned int)(v_stack_p70), (unsigned int)(0x20207050ULL), 0 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) * 4 * 4);
    *(unsigned __int64 *)(result + 32 + 8) = result;
    if (result != 0) goto loc_00ABBD23;
loc_00ABBDA8:
loc_00ABBDB0:
    if ((unsigned int)((unsigned int)(v_stack_p70)) == 0) goto loc_00ABBDD1;
loc_00ABBDB8:
    if (*(unsigned __int64 *)(v_stack_m2C0 + 40) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m2C0 + 40), a2, (unsigned int)(0x20207050ULL), 0 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) * 4 * 4);
    }
    v_rbx = (v_stack_m2C0 + 40) + (48);
    v_rsi = ((unsigned int)(v_stack_p70)) - (1);
    if (condition_is_not_equal) goto loc_00ABBDB8;
loc_00ABBDD1:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2C0, a2, (unsigned int)(0x20207050ULL), 0 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) * 4 * 4);
loc_00ABBDDB:
    if (v_stack_m2E8 == 0) goto loc_00ABB9C4;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2E8, a2, (unsigned int)(0x20207050ULL), 0 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL))))) * 4 * 4);
    goto loc_00ABB9C4;
loc_00ABBDF3:
    *(unsigned int *)(v_rbx + 4) = (unsigned int)(result);
    if (sign_flag) goto loc_00ABBDA8;
    v_r12 = (unsigned int)((v_stack_m2E8) + 1);
    v_rbx = (v_rbx) + (48);
    v_r14 = (v_stack_m2C0) + (20);
    if (((unsigned int)(v_r12)) >= ((unsigned int)(v_rsi))) goto loc_00ABBE1C;
    v_rdi = 0;
    goto loc_00ABBD06;
loc_00ABBE15:
    goto loc_00ABBDA8;
loc_00ABBE1C:
loc_00ABBE20:
    result = -(v_stack_m290);
    v_stack_p60 = (unsigned int)(v_rsi);
    a3 = ((unsigned int)(0x20207050ULL)) & (v_stack_m200);
    v_stack_p58 = v_stack_m2C0;
    v_stack_p50 = (unsigned int)((unsigned int)(v_stack_m2CC));
    v_stack_p48 = v_stack_m278;
    v_stack_p40 = v_stack_m248;
    v_stack_p38 = v_stack_m258;
    v_stack_p30 = (unsigned int)((unsigned int)(v_stack_m2F0));
    v_stack_p28 = a3;
    v_stack_p20 = v_stack_m2A0;
    result = PiSwStartCreate(v_rip - 11183878, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m308) + 48), v_stack_m228, v_stack_m2B0);
    if (v_stack_m2C0 != 0) goto loc_00ABBDB0;
    goto loc_00ABBDDB;
loc_00ABBEAD:
    goto loc_00ABB9C8;
}
```

## 5. (Beta) C Style

```c
int64_t PiCreateDriverSwDeviceCallback(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint32_t v_stack_m138;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A8;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint32_t v_stack_m21C;
    uint32_t v_stack_m220;
    uint64_t v_stack_m228;
    uint16_t v_stack_m22E;
    uint64_t v_stack_m230;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint32_t v_stack_m2C8;
    uint32_t v_stack_m2CC;
    uint32_t v_stack_m2D0;
    uint32_t v_stack_m2D4;
    uint32_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint32_t v_stack_m2F0;
    uint32_t v_stack_m2F4;
    uint32_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint32_t v_stack_m318;
    uint32_t v_stack_m350;
    uint64_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m58;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint32_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p20;
    uint32_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;

    local_rsp = (local_rsp) - (840);
    result = (*(uint64_t *)(v_rip + 0x34F2FD)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m218 = Arg1;
    v_stack_m308 = Arg4;
    v_stack_m280 = Arg3;
    Arg1 = 0;
    v_stack_m2D4 = 1;
    v_stack_m2E0 = 0;
    v_stack_m2F0 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2F4 = 0;
    v_stack_m2F8 = 0;
    v_stack_m2D8 = 0;
    v_stack_m300 = 0;
    v_stack_m278 = 0;
    v_stack_m2CC = 0;
    v_stack_m310 = 0;
    v_stack_m2C8 = 0;
    v_stack_m2E8 = 0;
    v_stack_m2C0 = 0;
    v_stack_m318 = 0;
    v_stack_m2B8 = v_xmm0;
    v_stack_m2A8 = v_xmm1;
    v_stack_m298 = v_xmm0;
    v_stack_m200 = v_xmm1;
    v_stack_m260 = v_xmm0;
    v_stack_m250 = v_xmm1;
    v_stack_m270 = v_xmm0;
    v_stack_m240 = v_xmm1;
    v_stack_m230 = v_xmm0;
    if (0 == 0) goto loc_00ABB4EF;
    if (*(uint64_t *)(Arg1 + 0xE0) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0xE0) + 0x8);
    }
    v_stack_m360 = Arg1;
    v_stack_m368 = v_stack_m2E0;
    Arg3 = 0;
    result = _RegRtlOpenKeyTransacted(Arg2, 0, Arg3, (uint32_t)(0x20019ULL));
    if (sign_flag) goto loc_00ABB9D1;
    Arg2 = 0;
    result = memset(v_stack_m1E8, Arg2, 392, (uint32_t)(0x20019ULL));
    v_stack_m120 = 0x4000000ULL;
    v_stack_m1E0 = 304;
    v_stack_m1C8 = (uint32_t)((uint32_t)(0x7000000ULL));
    v_stack_m1D8 = v_rip + 278138;
    v_stack_m1A8 = 304;
    v_stack_m1D0 = v_stack_m2B8;
    v_stack_m190 = (uint32_t)((uint32_t)(0x7000000ULL));
    v_stack_m1A0 = v_rip + 277865;
    v_stack_m170 = 288;
    v_stack_m198 = v_stack_m2A8;
    Arg4 = 0;
    v_stack_m158 = (uint32_t)((uint32_t)(0x1000000ULL));
    v_stack_m168 = v_rip + 281810;
    v_stack_m160 = v_stack_m298;
    v_stack_m130 = v_rip + 277859;
    v_stack_m128 = v_stack_m2F0;
    v_stack_mF8 = v_rip + 277482;
    v_stack_mF0 = v_stack_m260;
    v_stack_mC0 = v_rip + 278001;
    v_stack_m138 = 288;
    v_stack_m100 = 288;
    v_stack_mE8 = (uint32_t)((uint32_t)(0x1000000ULL));
    v_stack_mC8 = 288;
    v_stack_mB0 = (uint32_t)((uint32_t)(0x1000000ULL));
    v_stack_mB8 = v_stack_m250;
    v_stack_m360 = 1;
    result = RtlpQueryRegistryValues((uint32_t)(0xC0000000ULL), v_stack_m2E0, v_stack_m1E8, Arg4);
    Arg2 = 0;
    if (sign_flag) goto loc_00ABB9D1;
    if (v_stack_m2B0 == 0) goto loc_00ABB66B;
    result = Arg2 + 2;
    if (v_stack_m2B8 <= ((uint16_t)(Arg2 + 2))) {
        Arg1 = v_stack_m2B8;
        result = RtlFreeAnsiString(Arg1, Arg2, v_stack_m1E8, Arg4);
        Arg2 = 0;
        result = Arg2 + 2;
    }
    if (v_stack_m2A0 == 0) goto loc_00ABB682;
    if (v_stack_m2A8 <= ((uint16_t)(result))) {
        Arg1 = v_stack_m2A8;
        result = RtlFreeAnsiString(Arg1, Arg2, v_stack_m1E8, Arg4);
        Arg2 = 0;
    }
    if (v_stack_m290 == 0) goto loc_00ABB6BA;
    result = 2;
    if (v_stack_m298 < 2) {
        Arg1 = v_stack_m298;
        result = RtlFreeAnsiString(Arg1, Arg2, v_stack_m1E8, Arg4);
        Arg2 = 0;
    }
    if (v_stack_m290 == 0) goto loc_00ABB6BA;
    result = RtlGUIDFromString(v_stack_m298, v_stack_m200, v_stack_m1E8, Arg4);
    Arg2 = 0;
    if (sign_flag) {
        v_stack_m200 = v_xmm0;
    }
    if (v_stack_m258 == 0) goto loc_00ABB6E3;
    result = 2;
    if (v_stack_m260 < 2) {
        Arg1 = v_stack_m260;
        result = RtlFreeAnsiString(Arg1, Arg2, v_stack_m1E8, Arg4);
        Arg2 = 0;
        result = Arg2 + 2;
    }
    if (v_stack_m248 == 0) goto loc_00ABB6FA;
    if (v_stack_m250 < ((uint16_t)(result))) {
        Arg1 = v_stack_m250;
        result = RtlFreeAnsiString(Arg1, Arg2, v_stack_m1E8, Arg4);
        Arg2 = 0;
    }
    if (v_stack_m2B0 != 0) goto loc_00ABB710;
    if (v_stack_m2A0 != 0) goto loc_00ABB710;
    goto loc_00ABB9D1;
loc_00ABB710:
    v_stack_m210 = v_stack_m2B0;
    v_stack_m208 = v_stack_m2A0;
    v_stack_m220 = 2;
    v_stack_m21C = 3;
loc_00ABB736:
    if ((*(uint64_t *)(arg4)) == (*(uint64_t *)(v_rip + 0x4D0CFB))) goto loc_00ABBAEE;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg4) + 0x20) + 0x8)) != (*(uint64_t *)(v_rip + 0x4CF4B5))) goto loc_00ABB9B6;
    result = RtlInitUnicodeString(v_stack_m240, v_rip - 11137300, v_stack_m1E8, Arg4);
    result = RtlPrefixUnicodeString(v_stack_m240, *(uint64_t *)(arg4) + 40, 1, Arg4);
    Arg2 = 0;
    if ((uint8_t)(result) == 0) goto loc_00ABB9B6;
    Arg1 = (v_stack_m240) >> (1);
    result = RtlInitUnicodeString(v_stack_m270, *(uint64_t *)(*(uint64_t *)(arg4) + 0x30) + Arg1 * 2, 1, Arg4);
    result = RtlInitUnicodeString(v_stack_m240, v_rip - 11182166, 1, Arg4);
    result = RtlPrefixUnicodeString(v_stack_m240, v_stack_m270, 1, Arg4);
    Arg2 = 0;
    if ((uint8_t)(result) == 0) goto loc_00ABB9B6;
    Arg1 = (v_stack_m240) >> (1);
    if ((*(uint16_t *)(v_stack_m268 + Arg1 * 2)) != 92) goto loc_00ABB9B6;
    if (0 != 0) goto loc_00ABB876;
    result = PnpGenerateDeviceIdsHash(v_stack_m2B0, v_stack_m2A0, v_stack_m2F4, Arg4);
    if (sign_flag) goto loc_00ABB9C4;
    if (((v_stack_m2F0) & (8)) != 0) goto loc_00ABB83C;
    result = RtlInitUnicodeString(v_stack_m270, v_rip - 11179351, v_stack_m2F4, Arg4);
    Arg3 = 0;
    result = RtlHashUnicodeString(v_stack_m270, 1, Arg3, v_stack_m2F8);
    if (sign_flag) goto loc_00ABB9C4;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m2F4)) + (v_stack_m2F8));
    goto loc_00ABB83F;
loc_00ABB83C:
loc_00ABB83F:
    result = RtlInitUnicodeString(v_stack_m270, v_rip - 11179430, Arg3, v_stack_m2F8);
    Arg3 = 0;
    result = RtlHashUnicodeString(v_stack_m270, 1, Arg3, v_stack_m2F8);
    Arg2 = 0;
    if (sign_flag) goto loc_00ABB9C4;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m2F4)) + (v_stack_m2F8));
    v_stack_m2D0 = (uint32_t)(local_rsi);
    v_stack_m2F4 = (uint32_t)(local_rsi);
loc_00ABB876:
    if ((*(uint32_t *)(*(uint64_t *)(arg4) + 0x2AC)) != ((uint32_t)(local_rsi))) goto loc_00ABB9B6;
    if (0 != 0) goto loc_00ABB8B2;
    v_stack_m2D8 = 0x800ULL;
    result = ExAllocatePool2(256, (uint32_t)(0x800ULL), (uint32_t)(0x20207050ULL), v_stack_m2F8);
    Arg2 = 0;
    if (result == 0) goto loc_00ABB9BF;
loc_00ABB8B2:
    v_stack_m288 = v_stack_m220;
loc_00ABB8C4:
    Arg3 = 0;
    v_stack_m350 = 0;
    v_stack_m358 = v_stack_m318;
    v_stack_m318 = (uint32_t)((uint32_t)(v_stack_m2D8));
    v_stack_m360 = result;
    v_stack_m368 = v_stack_m2D4;
    result = CmGetDeviceRegProp(*(uint64_t *)(v_rip + 0x3AAAC5), *(uint64_t *)(*(uint64_t *)(arg4) + 0x30), Arg3, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    Arg2 = 0;
    if (sign_flag) goto loc_00ABB912;
    if (v_stack_m2D4 != 7) goto loc_00ABB912;
    local_rdi = (uint32_t)((uint32_t)(result));
    if (v_stack_m318 < ((uint32_t)(Arg2 + 2))) {
        *(uint16_t *)(result) = 0;
        local_rdi = 0;
    }
    if (0 != 1) goto loc_00ABB96D;
loc_00ABB920:
    if ((*(uint16_t *)(result)) == 0) goto loc_00ABB969;
    result = wcsicmp(result, v_rip - 11179636, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_00ABB966;
    result = wcsicmp(result, v_rip - 11179681, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_00ABB966;
    result = (result) | (-1);
loc_00ABB953:
    result = (result) + 1;
    if ((*(uint16_t *)(result + result * 2)) != 0) goto loc_00ABB953;
    local_rbx = (result + result * 2) + (2);
    goto loc_00ABB920;
loc_00ABB966:
    *(uint16_t *)(local_rbx) = 0;
loc_00ABB969:
loc_00ABB96D:
    if (*(uint64_t *)(v_stack_m210) == 0) goto loc_00ABB989;
    result = PnpCompareMultiSz(*(uint64_t *)(v_stack_m210), result, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    Arg2 = 0;
    if ((uint8_t)(result) != 0) goto loc_00ABB98F;
    goto loc_00ABB9A6;
loc_00ABB989:
    if ((*(uint16_t *)(result)) != 0) goto loc_00ABB9A6;
loc_00ABB98F:
    local_rbx = (v_stack_m288) + (4);
    local_rsi = (uint32_t)((0) + 1);
    local_r13 = (v_stack_m210) + (8);
    v_stack_m288 = local_rbx;
    if (((uint32_t)(local_rsi)) < 2) goto loc_00ABB8C4;
loc_00ABB9A6:
    if (((uint32_t)(local_rsi)) >= 2) goto loc_00ABBAE4;
loc_00ABB9B6:
    goto loc_00ABB736;
loc_00ABB9BF:
loc_00ABB9C4:
loc_00ABB9C8:
loc_00ABB9CC:
loc_00ABB9D1:
    local_r12 = 0;
    if (v_stack_m228 != 0) {
        result = ExFreePool(v_stack_m228, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    }
    if (v_stack_m310 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m310;
        result = ExFreePoolWithTag(Arg1, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    }
    if (v_stack_m2B0 != 0) {
        result = ExFreePool(v_stack_m2B0, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
        v_stack_m2B8 = v_xmm0;
    }
    if (v_stack_m2A0 != 0) {
        result = ExFreePool(v_stack_m2A0, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
        v_stack_m2A8 = v_xmm0;
    }
    if (v_stack_m290 != 0) {
        result = ExFreePool(v_stack_m290, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
        v_stack_m298 = v_xmm0;
    }
    if (v_stack_m258 != 0) {
        result = ExFreePool(v_stack_m258, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
        v_stack_m260 = v_xmm0;
    }
    if (v_stack_m248 != 0) {
        result = ExFreePool(v_stack_m248, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
        v_stack_m250 = v_xmm0;
    }
    if (v_stack_m300 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m300;
        result = ExFreePoolWithTag(Arg1, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    }
    if (result != 0) {
        Arg2 = 0;
        Arg1 = result;
        result = ExFreePoolWithTag(Arg1, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    }
    if (v_stack_m2E0 != 0) {
        result = ZwClose(v_stack_m2E0, Arg2, 1, (uint32_t)(*(uint32_t *)(v_stack_m220)));
    }
    if (!sign_flag) goto loc_00ABBAB4;
    if (((*(uint8_t *)(v_rip + 0x43469B)) & (4)) != 0) {
        Arg4 = *(uint64_t *)(v_stack_m308);
        Arg2 = v_rip - 11093886;
        result = v_stack_m280;
        v_stack_m360 = (uint32_t)((uint32_t)(0xC000009AULL));
        v_stack_m368 = result;
        Arg4 = *(uint64_t *)(arg4 + 0x30);
        result = McTemplateK0zzd_EtwWriteTransfer(v_stack_m2E0, Arg2, 1, Arg4);
    }
    if ((*(uint32_t *)(v_stack_m308 + 0x8)) >= 0) {
        *(uint32_t *)(v_stack_m308 + 0x8) = (uint32_t)((uint32_t)(0xC000009AULL));
    }
    result = 0;
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, Arg4);
    local_rsp = (local_rsp) + (840);
    return result;
loc_00ABBAE4:
    goto loc_00ABB9C4;
loc_00ABBAEE:
    if (sign_flag) goto loc_00ABB9C4;
    Arg3 = 0;
    result = IopGetRegistryValue(v_stack_m2E0, v_rip + 266840, Arg3, v_stack_m300);
    if (!sign_flag) goto loc_00ABBB24;
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00ABB9C8;
    goto loc_00ABBB4A;
loc_00ABBB24:
    if ((*(uint32_t *)(v_stack_m300 + 0x4)) != 3) goto loc_00ABBEAD;
    v_stack_m2CC = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m300 + 0xC)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m300 + 0xC)))) < 40) goto loc_00ABBEAD;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m300 + 0x8))) + (v_stack_m300);
    v_stack_m278 = result;
loc_00ABBB4A:
    if ((*(uint64_t *)(v_stack_m308)) == (*(uint64_t *)(v_rip + 0x4D08DF))) goto loc_00ABBC8E;
    Arg2 = 0;
    result = PipMakeGloballyUniqueId(*(uint64_t *)(*(uint64_t *)(v_stack_m308) + 0x20), Arg2, v_stack_p78, v_stack_m300);
    if (sign_flag) goto loc_00ABB9CC;
    local_r13 = (v_stack_m308) | (-1);
    local_r15 = 0;
loc_00ABBB87:
    Arg1 = (local_r13) + 1;
    if ((*(uint16_t *)(v_stack_m280 + Arg1 * 2)) != 0) goto loc_00ABBB87;
loc_00ABBB96:
    local_r13 = (local_r13) + 1;
    if ((*(uint16_t *)(v_stack_p78 + local_r13 * 2)) != 0) goto loc_00ABBB96;
    result = (uint16_t)((Arg1 + 2) + ((uint16_t)(local_r13)));
    result = (uint16_t)((result) + ((uint16_t)(result)));
    v_stack_m22E = (uint16_t)(result);
    result = ExAllocatePool2(256, (uint16_t)(Arg1 + local_r13 * 1 * 2 + 4), (uint32_t)(0x67727453ULL), v_stack_m300);
    v_stack_m228 = result;
    if (result != 0) goto loc_00ABBBE3;
    goto loc_00ABB9C8;
loc_00ABBBE3:
    result = RtlUnicodeStringPrintf(v_stack_m230, v_rip + 280243, v_stack_m280, (uint32_t)(0xC000009AULL));
    if (sign_flag) goto loc_00ABB9C8;
loc_00ABBC06:
loc_00ABBC11:
    v_stack_p30 = v_stack_p70;
    Arg4 = 0;
    v_stack_p28 = (uint32_t)((uint32_t)(v_stack_m2C8));
    Arg3 = 0;
    v_stack_p20 = 0;
    result = PnpGetGenericStorePropertyKeys(v_stack_m218, v_stack_m2E0, Arg3, Arg4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00ABBCB7;
    if (((uint32_t)((uint32_t)(v_stack_p70))) <= ((uint32_t)((uint32_t)(v_stack_m2C8)))) goto loc_00ABBCAD;
    result = (uint32_t)(v_stack_p70);
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_p70;
    }
    Arg2 = ((uint32_t)((uint32_t)(result)) * 4) + ((uint32_t)((uint32_t)(result)));
    Arg2 = (Arg2) << (2);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20207050ULL), Arg4);
    if (result != 0) goto loc_00ABBC11;
    goto loc_00ABB9BF;
loc_00ABBC8E:
    result = RtlCreateUnicodeString(v_stack_m230, v_stack_m280, (uint32_t)(0x20207050ULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00ABBC06;
    goto loc_00ABB9CC;
loc_00ABBCAD:
    goto loc_00ABBDDB;
loc_00ABBCB7:
    if (sign_flag) goto loc_00ABBDDB;
    local_rdi = 0;
    if ((uint32_t)((uint32_t)(v_stack_p70)) == 0) goto loc_00ABBE20;
    Arg2 = ((uint32_t)(v_stack_p70) + (uint32_t)(v_stack_p70) * 2) << (4);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20207050ULL), Arg4);
    v_stack_m2C0 = result;
    if (result != 0) goto loc_00ABBCF8;
    goto loc_00ABBDDB;
loc_00ABBCF8:
    v_stack_m2E8 = 0;
loc_00ABBD06:
    *(uint64_t *)(result + 0x20 - 0x20) = v_xmm0;
    *(uint32_t *)(result + 0x20 - 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x10)));
    *(uint32_t *)(result + 0x20 - 0xC) = (uint32_t)((uint32_t)(0xC000009AULL));
loc_00ABBD23:
    v_stack_p38 = v_stack_p70;
    Arg3 = 0;
    v_stack_p30 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x20 + 0x4)));
    v_stack_p28 = *(uint64_t *)(result + 0x20 + 0x8);
    v_stack_p20 = result + 32;
    result = PnpGetGenericStoreProperty(v_stack_m218, v_stack_m2E0, Arg3, 0 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) * 4 * 4);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_00ABBDF3;
    if (((uint32_t)((uint32_t)(v_stack_p70))) <= (*(uint32_t *)(result + 0x20 + 0x4))) goto loc_00ABBE15;
    result = (uint32_t)(v_stack_p70);
    if (*(uint64_t *)(result + 0x20 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(result + 0x20 + 0x8), Arg2, Arg3, 0 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) * 4 * 4);
        result = v_stack_p70;
    }
    *(uint32_t *)(result + 0x20 + 0x4) = (uint32_t)(result);
    result = ExAllocatePool2(256, (uint32_t)(v_stack_p70), (uint32_t)(0x20207050ULL), 0 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) * 4 * 4);
    *(uint64_t *)(result + 0x20 + 0x8) = result;
    if (result != 0) goto loc_00ABBD23;
loc_00ABBDA8:
loc_00ABBDB0:
    if ((uint32_t)((uint32_t)(v_stack_p70)) == 0) goto loc_00ABBDD1;
loc_00ABBDB8:
    if (*(uint64_t *)(v_stack_m2C0 + 0x28) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m2C0 + 0x28), Arg2, (uint32_t)(0x20207050ULL), 0 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) * 4 * 4);
    }
    local_rbx = (v_stack_m2C0 + 40) + (48);
    local_rsi = ((uint32_t)(v_stack_p70)) - (1);
    if (condition_is_not_equal) goto loc_00ABBDB8;
loc_00ABBDD1:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2C0, Arg2, (uint32_t)(0x20207050ULL), 0 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) * 4 * 4);
loc_00ABBDDB:
    if (v_stack_m2E8 == 0) goto loc_00ABB9C4;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2E8, Arg2, (uint32_t)(0x20207050ULL), 0 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL))))) * 4 * 4);
    goto loc_00ABB9C4;
loc_00ABBDF3:
    *(uint32_t *)(local_rbx + 0x4) = (uint32_t)(result);
    if (sign_flag) goto loc_00ABBDA8;
    local_r12 = (uint32_t)((v_stack_m2E8) + 1);
    local_rbx = (local_rbx) + (48);
    local_r14 = (v_stack_m2C0) + (20);
    if (((uint32_t)(local_r12)) >= ((uint32_t)(local_rsi))) goto loc_00ABBE1C;
    local_rdi = 0;
    goto loc_00ABBD06;
loc_00ABBE15:
    goto loc_00ABBDA8;
loc_00ABBE1C:
loc_00ABBE20:
    result = -(v_stack_m290);
    v_stack_p60 = (uint32_t)(local_rsi);
    Arg3 = ((uint32_t)(0x20207050ULL)) & (v_stack_m200);
    v_stack_p58 = v_stack_m2C0;
    v_stack_p50 = (uint32_t)((uint32_t)(v_stack_m2CC));
    v_stack_p48 = v_stack_m278;
    v_stack_p40 = v_stack_m248;
    v_stack_p38 = v_stack_m258;
    v_stack_p30 = (uint32_t)((uint32_t)(v_stack_m2F0));
    v_stack_p28 = Arg3;
    v_stack_p20 = v_stack_m2A0;
    result = PiSwStartCreate(v_rip - 11183878, *(uint64_t *)(*(uint64_t *)(v_stack_m308) + 0x30), v_stack_m228, v_stack_m2B0);
    if (v_stack_m2C0 != 0) goto loc_00ABBDB0;
    goto loc_00ABBDDB;
loc_00ABBEAD:
    goto loc_00ABB9C8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABB420&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
