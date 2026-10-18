# ObQueryDeviceMapInformation

- RVA: `0x0096C5C0`–`0x0096CBC0` (길이 `1,536` bytes)
- VA: `0x000000014096C5C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00095C88`
- 디코드: `378`개 명령, `1,536/1,536` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **13**; 고유 호출 대상: **11**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0096C632` → [ObpReferenceCurrentDeviceMap](ObpReferenceCurrentDeviceMap_function_0096CBD0.md) (function, `0x0096CBD0`)
- `0x0096C646` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x0096C64E` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x0096C670` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0096C695` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0096CAB9` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0096CAC2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0096CAC7` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)
- `0x0096CADA` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0096CAE3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0096CB08` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0096CB8E` → [ObDereferenceDeviceMap](ObDereferenceDeviceMap_function_0096D0E8.md) (function, `0x0096D0E8`)
- `0x0096CB9C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)

### Direct callers
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB551`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **11**
  - `0x0096C646` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x0096C64E` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x0096C670` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0096C695` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0096CAB9` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0096CAC2` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0096CAC7` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (`PAGE` → `.text`)
  - `0x0096CADA` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0096CAE3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0096CB08` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x0096CB9C` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0096C5C0  4C 8B DC                        mov r11, rsp
0096C5C3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0096C5C7  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0096C5CB  49 89 53 10                     mov qword ptr [r11 + 0x10], rdx
0096C5CF  57                              push rdi
0096C5D0  41 54                           push r12
0096C5D2  41 55                           push r13
0096C5D4  41 56                           push r14
0096C5D6  41 57                           push r15
0096C5D8  48 83 EC 50                     sub rsp, 0x50
0096C5DC  45 8B F0                        mov r14d, r8d
0096C5DF  48 8B F9                        mov rdi, rcx
0096C5E2  49 C7 43 20 00 00 00 00         mov qword ptr [r11 + 0x20], 0
0096C5EA  0F 57 C0                        xorps xmm0, xmm0
0096C5ED  33 C0                           xor eax, eax
0096C5EF  0F 11 44 24 28                  movups xmmword ptr [rsp + 0x28], xmm0
0096C5F4  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
0096C5F9  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
0096C5FD  45 32 ED                        xor r13b, r13b
0096C600  41 F7 C0 FE FF FF FF            test r8d, 0xfffffffe
0096C607  0F 85 88 05 00 00               jne 0x14096cb95
0096C60D  48 85 C9                        test rcx, rcx
0096C610  74 16                           je 0x14096c628
0096C612  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0096C61B  48 39 88 B8 00 00 00            cmp qword ptr [rax + 0xb8], rcx
0096C622  0F 85 6D 05 00 00               jne 0x14096cb95
0096C628  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
0096C630  33 C9                           xor ecx, ecx
0096C632  E8 99 05 00 00                  call 0x14096cbd0
0096C637  48 8B D8                        mov rbx, rax
0096C63A  48 85 FF                        test rdi, rdi
0096C63D  0F 84 59 05 00 00               je 0x14096cb9c
0096C643  48 8B CF                        mov rcx, rdi
0096C646  E8 95 F8 AD FF                  call 0x14044bee0
0096C64B  48 8B C8                        mov rcx, rax
0096C64E  E8 4D 8A 8B FF                  call 0x1402250a0
0096C653  4C 8B F8                        mov r15, rax
0096C656  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0096C65F  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0096C666  90                              nop
0096C667  45 33 C0                        xor r8d, r8d
0096C66A  33 D2                           xor edx, edx
0096C66C  49 8D 4F 78                     lea rcx, [r15 + 0x78]
0096C670  E8 BB 3B 8A FF                  call 0x140210230
0096C675  48 8B F0                        mov rsi, rax
0096C678  33 C0                           xor eax, eax
0096C67A  41 BB 11 00 00 00               mov r11d, 0x11
0096C680  F0 4D 0F B1 5F 78               lock cmpxchg qword ptr [r15 + 0x78], r11
0096C686  74 18                           je 0x14096c6a0
0096C688  4D 8D 4F 78                     lea r9, [r15 + 0x78]
0096C68C  4C 8B C6                        mov r8, rsi
0096C68F  33 D2                           xor edx, edx
0096C691  49 8D 4F 78                     lea rcx, [r15 + 0x78]
0096C695  E8 B2 3D 8A FF                  call 0x14021044c
0096C69A  41 BB 11 00 00 00               mov r11d, 0x11
0096C6A0  48 85 F6                        test rsi, rsi
0096C6A3  74 04                           je 0x14096c6a9
0096C6A5  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0096C6A9  48 85 DB                        test rbx, rbx
0096C6AC  0F 84 F4 04 00 00               je 0x14096cba6
0096C6B2  41 B5 01                        mov r13b, 1
0096C6B5  33 FF                           xor edi, edi
0096C6B7  48 85 DB                        test rbx, rbx
0096C6BA  0F 84 EA 03 00 00               je 0x14096caaa
0096C6C0  44 8B CF                        mov r9d, edi
0096C6C3  41 F6 C6 01                     test r14b, 1
0096C6C7  75 04                           jne 0x14096c6cd
0096C6C9  4C 8B 4B 18                     mov r9, qword ptr [rbx + 0x18]
0096C6CD  44 8B 83 00 01 00 00            mov r8d, dword ptr [rbx + 0x100]
0096C6D4  44 89 44 24 28                  mov dword ptr [rsp + 0x28], r8d
0096C6D9  B8 01 00 00 00                  mov eax, 1
0096C6DE  BA 02 00 00 00                  mov edx, 2
0096C6E3  0F 1F 40 00                     nop dword ptr [rax]
0096C6E7  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
0096C6F0  8D 4A FE                        lea ecx, [rdx - 2]
0096C6F3  44 8B D1                        mov r10d, ecx
0096C6F6  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C6FE  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C703  44 85 C0                        test eax, r8d
0096C706  75 20                           jne 0x14096c728
0096C708  4D 85 C9                        test r9, r9
0096C70B  74 1B                           je 0x14096c728
0096C70D  43 0F B6 8C 11 04 01 00 00      movzx ecx, byte ptr [r9 + r10 + 0x104]
0096C716  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C71B  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C722  23 C8                           and ecx, eax
0096C724  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C728  03 C0                           add eax, eax
0096C72A  8D 4A FF                        lea ecx, [rdx - 1]
0096C72D  44 8B D1                        mov r10d, ecx
0096C730  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C738  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C73D  44 85 C0                        test eax, r8d
0096C740  75 20                           jne 0x14096c762
0096C742  4D 85 C9                        test r9, r9
0096C745  74 1B                           je 0x14096c762
0096C747  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C750  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C755  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C75C  23 C8                           and ecx, eax
0096C75E  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C762  03 C0                           add eax, eax
0096C764  44 8B D2                        mov r10d, edx
0096C767  41 0F B6 8C 1A 04 01 00 00      movzx ecx, byte ptr [r10 + rbx + 0x104]
0096C770  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C775  44 85 C0                        test eax, r8d
0096C778  75 20                           jne 0x14096c79a
0096C77A  4D 85 C9                        test r9, r9
0096C77D  74 1B                           je 0x14096c79a
0096C77F  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C788  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C78D  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C794  23 C8                           and ecx, eax
0096C796  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C79A  03 C0                           add eax, eax
0096C79C  8D 4A 01                        lea ecx, [rdx + 1]
0096C79F  44 8B D1                        mov r10d, ecx
0096C7A2  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C7AA  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C7AF  44 85 C0                        test eax, r8d
0096C7B2  75 20                           jne 0x14096c7d4
0096C7B4  4D 85 C9                        test r9, r9
0096C7B7  74 1B                           je 0x14096c7d4
0096C7B9  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C7C2  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C7C7  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C7CE  23 C8                           and ecx, eax
0096C7D0  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C7D4  03 C0                           add eax, eax
0096C7D6  8D 4A 02                        lea ecx, [rdx + 2]
0096C7D9  44 8B D1                        mov r10d, ecx
0096C7DC  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C7E4  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C7E9  44 85 C0                        test eax, r8d
0096C7EC  75 20                           jne 0x14096c80e
0096C7EE  4D 85 C9                        test r9, r9
0096C7F1  74 1B                           je 0x14096c80e
0096C7F3  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C7FC  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C801  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C808  23 C8                           and ecx, eax
0096C80A  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C80E  03 C0                           add eax, eax
0096C810  8D 4A 03                        lea ecx, [rdx + 3]
0096C813  44 8B D1                        mov r10d, ecx
0096C816  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C81E  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C823  44 85 C0                        test eax, r8d
0096C826  75 20                           jne 0x14096c848
0096C828  4D 85 C9                        test r9, r9
0096C82B  74 1B                           je 0x14096c848
0096C82D  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C836  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C83B  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C842  23 C8                           and ecx, eax
0096C844  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C848  03 C0                           add eax, eax
0096C84A  8D 4A 04                        lea ecx, [rdx + 4]
0096C84D  44 8B D1                        mov r10d, ecx
0096C850  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C858  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C85D  44 85 C0                        test eax, r8d
0096C860  75 20                           jne 0x14096c882
0096C862  4D 85 C9                        test r9, r9
0096C865  74 1B                           je 0x14096c882
0096C867  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C870  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C875  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C87C  23 C8                           and ecx, eax
0096C87E  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C882  03 C0                           add eax, eax
0096C884  8D 4A 05                        lea ecx, [rdx + 5]
0096C887  44 8B D1                        mov r10d, ecx
0096C88A  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C892  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C897  44 85 C0                        test eax, r8d
0096C89A  75 20                           jne 0x14096c8bc
0096C89C  4D 85 C9                        test r9, r9
0096C89F  74 1B                           je 0x14096c8bc
0096C8A1  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C8AA  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C8AF  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C8B6  23 C8                           and ecx, eax
0096C8B8  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C8BC  03 C0                           add eax, eax
0096C8BE  8D 4A 06                        lea ecx, [rdx + 6]
0096C8C1  44 8B D1                        mov r10d, ecx
0096C8C4  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C8CC  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C8D1  44 85 C0                        test eax, r8d
0096C8D4  75 20                           jne 0x14096c8f6
0096C8D6  4D 85 C9                        test r9, r9
0096C8D9  74 1B                           je 0x14096c8f6
0096C8DB  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C8E4  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C8E9  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C8F0  23 C8                           and ecx, eax
0096C8F2  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C8F6  03 C0                           add eax, eax
0096C8F8  8D 4A 07                        lea ecx, [rdx + 7]
0096C8FB  44 8B D1                        mov r10d, ecx
0096C8FE  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C906  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C90B  44 85 C0                        test eax, r8d
0096C90E  75 20                           jne 0x14096c930
0096C910  4D 85 C9                        test r9, r9
0096C913  74 1B                           je 0x14096c930
0096C915  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C91E  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C923  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C92A  23 C8                           and ecx, eax
0096C92C  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C930  03 C0                           add eax, eax
0096C932  8D 4A 08                        lea ecx, [rdx + 8]
0096C935  44 8B D1                        mov r10d, ecx
0096C938  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C940  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C945  44 85 C0                        test eax, r8d
0096C948  75 20                           jne 0x14096c96a
0096C94A  4D 85 C9                        test r9, r9
0096C94D  74 1B                           je 0x14096c96a
0096C94F  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C958  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C95D  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C964  23 C8                           and ecx, eax
0096C966  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C96A  03 C0                           add eax, eax
0096C96C  8D 4A 09                        lea ecx, [rdx + 9]
0096C96F  44 8B D1                        mov r10d, ecx
0096C972  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C97A  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C97F  44 85 C0                        test eax, r8d
0096C982  75 20                           jne 0x14096c9a4
0096C984  4D 85 C9                        test r9, r9
0096C987  74 1B                           je 0x14096c9a4
0096C989  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C992  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C997  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C99E  23 C8                           and ecx, eax
0096C9A0  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C9A4  03 C0                           add eax, eax
0096C9A6  8D 4A 0A                        lea ecx, [rdx + 0xa]
0096C9A9  44 8B D1                        mov r10d, ecx
0096C9AC  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C9B4  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C9B9  44 85 C0                        test eax, r8d
0096C9BC  75 20                           jne 0x14096c9de
0096C9BE  4D 85 C9                        test r9, r9
0096C9C1  74 1B                           je 0x14096c9de
0096C9C3  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096C9CC  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C9D1  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096C9D8  23 C8                           and ecx, eax
0096C9DA  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096C9DE  03 C0                           add eax, eax
0096C9E0  8D 4A 0B                        lea ecx, [rdx + 0xb]
0096C9E3  44 8B D1                        mov r10d, ecx
0096C9E6  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096C9EE  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096C9F3  44 85 C0                        test eax, r8d
0096C9F6  75 20                           jne 0x14096ca18
0096C9F8  4D 85 C9                        test r9, r9
0096C9FB  74 1B                           je 0x14096ca18
0096C9FD  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096CA06  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096CA0B  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096CA12  23 C8                           and ecx, eax
0096CA14  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096CA18  03 C0                           add eax, eax
0096CA1A  8D 4A 0C                        lea ecx, [rdx + 0xc]
0096CA1D  44 8B D1                        mov r10d, ecx
0096CA20  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096CA28  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096CA2D  44 85 C0                        test eax, r8d
0096CA30  75 20                           jne 0x14096ca52
0096CA32  4D 85 C9                        test r9, r9
0096CA35  74 1B                           je 0x14096ca52
0096CA37  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096CA40  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096CA45  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096CA4C  23 C8                           and ecx, eax
0096CA4E  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096CA52  03 C0                           add eax, eax
0096CA54  8D 4A 0D                        lea ecx, [rdx + 0xd]
0096CA57  44 8B D1                        mov r10d, ecx
0096CA5A  0F B6 8C 19 04 01 00 00         movzx ecx, byte ptr [rcx + rbx + 0x104]
0096CA62  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096CA67  44 85 C0                        test eax, r8d
0096CA6A  75 20                           jne 0x14096ca8c
0096CA6C  4D 85 C9                        test r9, r9
0096CA6F  74 1B                           je 0x14096ca8c
0096CA71  43 0F B6 8C 0A 04 01 00 00      movzx ecx, byte ptr [r10 + r9 + 0x104]
0096CA7A  42 88 4C 14 2C                  mov byte ptr [rsp + r10 + 0x2c], cl
0096CA7F  41 8B 89 00 01 00 00            mov ecx, dword ptr [r9 + 0x100]
0096CA86  23 C8                           and ecx, eax
0096CA88  09 4C 24 28                     or dword ptr [rsp + 0x28], ecx
0096CA8C  03 C0                           add eax, eax
0096CA8E  83 C2 10                        add edx, 0x10
0096CA91  8D 4A FE                        lea ecx, [rdx - 2]
0096CA94  83 F9 20                        cmp ecx, 0x20
0096CA97  0F 82 53 FC FF FF               jb 0x14096c6f0
0096CA9D  49 8B C3                        mov rax, r11
0096CAA0  F0 49 0F B1 7F 78               lock cmpxchg qword ptr [r15 + 0x78], rdi
0096CAA6  75 2E                           jne 0x14096cad6
0096CAA8  EB 35                           jmp 0x14096cadf
0096CAAA  49 8B C3                        mov rax, r11
0096CAAD  F0 49 0F B1 7F 78               lock cmpxchg qword ptr [r15 + 0x78], rdi
0096CAB3  74 09                           je 0x14096cabe
0096CAB5  49 8D 4F 78                     lea rcx, [r15 + 0x78]
0096CAB9  E8 82 69 8F FF                  call 0x140263440
0096CABE  49 8D 4F 78                     lea rcx, [r15 + 0x78]
0096CAC2  E8 39 4B 97 FF                  call 0x1402e1600
0096CAC7  E8 74 61 97 FF                  call 0x1402e2c40
0096CACC  BF 11 00 00 C0                  mov edi, 0xc0000011
0096CAD1  E9 93 00 00 00                  jmp 0x14096cb69
0096CAD6  49 8D 4F 78                     lea rcx, [r15 + 0x78]
0096CADA  E8 61 69 8F FF                  call 0x140263440
0096CADF  49 8D 4F 78                     lea rcx, [r15 + 0x78]
0096CAE3  E8 18 4B 97 FF                  call 0x1402e1600
0096CAE8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0096CAF1  90                              nop
0096CAF2  66 83 80 E6 01 00 00 01         add word ptr [rax + 0x1e6], 1
0096CAFA  75 11                           jne 0x14096cb0d
0096CAFC  90                              nop
0096CAFD  48 05 98 00 00 00               add rax, 0x98
0096CB03  48 39 00                        cmp qword ptr [rax], rax
0096CB06  74 05                           je 0x14096cb0d
0096CB08  E8 73 61 97 FF                  call 0x1402e2c80
0096CB0D  41 80 FD 01                     cmp r13b, 1
0096CB11  75 32                           jne 0x14096cb45
0096CB13  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
0096CB1B  48 85 C0                        test rax, rax
0096CB1E  74 66                           je 0x14096cb86
0096CB20  0F 0D 08                        prefetchw byte ptr [rax]
0096CB23  48 8B 00                        mov rax, qword ptr [rax]
0096CB26  48 8B C8                        mov rcx, rax
0096CB29  48 33 CB                        xor rcx, rbx
0096CB2C  48 83 F9 0F                     cmp rcx, 0xf
0096CB30  73 54                           jae 0x14096cb86
0096CB32  48 8D 48 01                     lea rcx, [rax + 1]
0096CB36  48 8B 94 24 98 00 00 00         mov rdx, qword ptr [rsp + 0x98]
0096CB3E  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
0096CB43  75 E1                           jne 0x14096cb26
0096CB45  0F 10 44 24 28                  movups xmm0, xmmword ptr [rsp + 0x28]
0096CB4A  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0096CB52  0F 11 01                        movups xmmword ptr [rcx], xmm0
0096CB55  0F 10 4C 24 38                  movups xmm1, xmmword ptr [rsp + 0x38]
0096CB5A  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
0096CB5E  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
0096CB62  89 41 20                        mov dword ptr [rcx + 0x20], eax
0096CB65  EB 02                           jmp 0x14096cb69
0096CB67  8B F8                           mov edi, eax
0096CB69  8B C7                           mov eax, edi
0096CB6B  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0096CB70  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0096CB74  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
0096CB78  49 8B E3                        mov rsp, r11
0096CB7B  41 5F                           pop r15
0096CB7D  41 5E                           pop r14
0096CB7F  41 5D                           pop r13
0096CB81  41 5C                           pop r12
0096CB83  5F                              pop rdi
0096CB84  C3                              ret
0096CB85  CC                              int3
0096CB86  BA 01 00 00 00                  mov edx, 1
0096CB8B  48 8B CB                        mov rcx, rbx
0096CB8E  E8 55 05 00 00                  call 0x14096d0e8
0096CB93  EB B0                           jmp 0x14096cb45
0096CB95  B8 0D 00 00 C0                  mov eax, 0xc000000d
0096CB9A  EB CF                           jmp 0x14096cb6b
0096CB9C  E8 4F 16 99 FF                  call 0x1402fe1f0
0096CBA1  E9 AD FA FF FF                  jmp 0x14096c653
0096CBA6  48 8D 87 18 03 00 00            lea rax, [rdi + 0x318]
0096CBAD  48 85 FF                        test rdi, rdi
0096CBB0  49 0F 44 C7                     cmove rax, r15
0096CBB4  48 8B 18                        mov rbx, qword ptr [rax]
0096CBB7  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
0096CBBB  E9 F5 FA FF FF                  jmp 0x14096c6b5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObQueryDeviceMapInformation(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(v_rsp + 32) = 0;
    result = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    v_r13 = 0;
    if (((a3) & (0xFFFFFFFEULL)) != 0) goto loc_0096CB95;
    if (a1 == 0) goto loc_0096C628;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != a1) goto loc_0096CB95;
loc_0096C628:
    a1 = 0;
    result = ObpReferenceCurrentDeviceMap(a1, v_stack_p20, a3, a4);
    if (0 == 0) goto loc_0096CB9C;
    result = PsGetProcessServerSilo(0, v_stack_p20, a3, a4);
    result = PsGetServerSiloGlobals(result, v_stack_p20, a3, a4);
loc_0096C653:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 120, a2, a3, a4);
    result = 0;
    v_r11 = 17;
    if (!(condition_is_equal)) {
        a4 = result + 120;
        a3 = 0;
        a2 = 0;
        a1 = result + 120;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        v_r11 = 17;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (result == 0) goto loc_0096CBA6;
loc_0096C6B5:
    v_rdi = 0;
    if (result == 0) goto loc_0096CAAA;
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) == 0) {
        a4 = *(unsigned __int64 *)(result + 24);
    }
    v_stack_m50 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 256)));
loc_0096C6F0:
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 - 2)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 - 2 + result * 1 + 260));
    if (((1) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C728;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)(a4 + (unsigned int)((unsigned int)(2 - 2)) * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 - 2)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & (1));
    }
    result = (unsigned int)((1) + (1));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 - 1)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 - 1 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C762;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 - 1)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 - 1)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + 2 * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C79A;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)(2 + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + 2 * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 1)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 1 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C7D4;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 1)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 1)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 2)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 2 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C80E;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 2)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 2)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 3)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 3 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C848;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 3)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 3)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 4)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 4 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C882;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 4)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 4)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 5)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 5 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C8BC;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 5)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 5)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 6)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 6 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C8F6;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 6)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 6)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 7)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 7 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C930;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 7)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 7)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 8)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 8 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C96A;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 8)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 8)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 9)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 9 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C9A4;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 9)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 9)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 10)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 10 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096C9DE;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 10)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 10)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 11)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 11 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096CA18;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 11)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 11)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 12)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 12 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096CA52;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 12)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 12)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 13)) * 1 + 44) = (unsigned __int8)(*(unsigned __int8 *)(2 + 13 + result * 1 + 260));
    if ((((unsigned int)(result)) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + 256))))) != 0) goto loc_0096CA8C;
    if (a4 != 0) {
        a1 = *(unsigned __int8 *)((unsigned int)((unsigned int)(2 + 13)) + a4 * 1 + 260);
        *(unsigned __int8 *)(v_rsp + (unsigned int)((unsigned int)(2 + 13)) * 1 + 44) = (unsigned __int8)(a1);
        a1 = *(unsigned int *)(a4 + 256);
        a1 = (unsigned int)((a1) & ((unsigned int)(result)));
    }
    result = (unsigned int)((result) + ((unsigned int)(result)));
    a2 = (unsigned int)((2) + (16));
    if (((unsigned int)(a2 - 2)) < 32) goto loc_0096C6F0;
    if (((unsigned int)(a2 - 2)) != 32) goto loc_0096CAD6;
    goto loc_0096CADF;
loc_0096CAAA:
    result = v_r11;
    if (((unsigned int)(a2 - 2)) != 32) {
        a1 = result + 120;
        result = ExfReleasePushLockShared(a1, a2, (unsigned int)(*(unsigned int *)(result + 256)), a4);
    }
    result = KeAbPostRelease(result + 120, a2, (unsigned int)(*(unsigned int *)(result + 256)), a4);
    result = KeLeaveGuardedRegion(result + 120, a2, (unsigned int)(*(unsigned int *)(result + 256)), a4);
    goto loc_0096CB69;
loc_0096CAD6:
    result = ExfReleasePushLockShared(result + 120, a2, (unsigned int)(*(unsigned int *)(result + 256)), a4);
loc_0096CADF:
    result = KeAbPostRelease(result + 120, a2, (unsigned int)(*(unsigned int *)(result + 256)), a4);
    if (((unsigned int)(a2 - 2)) != 32) goto loc_0096CB0D;
    result = (*(unsigned __int64 *)(gs_base + (0 + 392))) + (152);
    if ((*(unsigned __int64 *)(result)) != result) {
        result = KiCheckForKernelApcDelivery(result + 120, a2, (unsigned int)(*(unsigned int *)(result + 256)), a4);
    }
    if (1 != 1) goto loc_0096CB45;
    if (v_stack_p20 == 0) goto loc_0096CB86;
loc_0096CB26:
    a1 = (*(unsigned __int64 *)(v_stack_p20)) ^ (result);
    if (a1 >= 15) goto loc_0096CB86;
    if (a1 != 15) goto loc_0096CB26;
loc_0096CB45:
    *(unsigned __int64 *)(v_stack_p10) = v_xmm0;
    *(unsigned __int64 *)(v_stack_p10 + 16) = v_xmm1;
    *(unsigned int *)(v_stack_p10 + 32) = (unsigned int)((unsigned int)(v_stack_m30));
    goto loc_0096CB69;
loc_0096CB69:
loc_0096CB6B:
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000011ULL)));
loc_0096CB86:
    result = ObDereferenceDeviceMap(*(unsigned __int64 *)(v_stack_m28 + 48), 1, (unsigned int)(*(unsigned int *)(result + 256)), a4);
    goto loc_0096CB45;
loc_0096CB95:
    goto loc_0096CB6B;
loc_0096CB9C:
    result = PsGetCurrentServerSiloGlobals(*(unsigned __int64 *)(v_stack_m28 + 48), 1, (unsigned int)(*(unsigned int *)(result + 256)), a4);
    goto loc_0096C653;
loc_0096CBA6:
    result = (unsigned int)(0xC0000011ULL) + 792;
    if ((unsigned int)(0xC0000011ULL) == 0) { result = result; }
    v_rbx = (*(unsigned __int64 *)(result)) & (-16);
    goto loc_0096C6B5;
}
```

## 5. (Beta) C Style

```c
int64_t ObQueryDeviceMapInformation(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_r11;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    local_rsp = (local_rsp) - (80);
    *(uint64_t *)(local_rsp + 0x20) = 0;
    result = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x30) = 0;
    local_r13 = 0;
    if (((Arg3) & (0xFFFFFFFEULL)) != 0) goto loc_0096CB95;
    if (Arg1 == 0) goto loc_0096C628;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != Arg1) goto loc_0096CB95;
loc_0096C628:
    Arg1 = 0;
    result = ObpReferenceCurrentDeviceMap(Arg1, v_stack_p20, Arg3, a4);
    if (0 == 0) goto loc_0096CB9C;
    result = PsGetProcessServerSilo(0, v_stack_p20, Arg3, a4);
    result = PsGetServerSiloGlobals(result, v_stack_p20, Arg3, a4);
loc_0096C653:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 120, Arg2, Arg3, a4);
    result = 0;
    local_r11 = 17;
    if (!(condition_is_equal)) {
        a4 = result + 120;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 120;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
        local_r11 = 17;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (result == 0) goto loc_0096CBA6;
loc_0096C6B5:
    local_rdi = 0;
    if (result == 0) goto loc_0096CAAA;
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) == 0) {
        a4 = *(uint64_t *)(result + 0x18);
    }
    v_stack_m50 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100)));
loc_0096C6F0:
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 - 0x2)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 - 0x2 + result * 1 + 0x104));
    if (((1) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C728;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)(a4 + (uint32_t)((uint32_t)(2 - 0x2)) * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 - 0x2)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & (1));
    }
    result = (uint32_t)((1) + (1));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 - 0x1)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 - 0x1 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C762;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 - 0x1)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 - 0x1)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + 0x2 * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C79A;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)(2 + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + 0x2 * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x1)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x1 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C7D4;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x1)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x1)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x2)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x2 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C80E;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x2)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x2)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x3)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x3 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C848;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x3)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x3)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x4)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x4 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C882;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x4)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x4)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x5)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x5 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C8BC;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x5)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x5)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x6)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x6 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C8F6;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x6)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x6)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x7)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x7 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C930;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x7)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x7)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x8)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x8 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C96A;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x8)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x8)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x9)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0x9 + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C9A4;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0x9)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0x9)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xA)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0xA + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096C9DE;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0xA)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xA)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xB)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0xB + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096CA18;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0xB)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xB)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xC)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0xC + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096CA52;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0xC)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xC)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xD)) * 1 + 0x2C) = (uint8_t)(*(uint8_t *)(2 + 0xD + result * 1 + 0x104));
    if ((((uint32_t)(result)) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x100))))) != 0) goto loc_0096CA8C;
    if (a4 != 0) {
        Arg1 = *(uint8_t *)((uint32_t)((uint32_t)(2 + 0xD)) + a4 * 1 + 0x104);
        *(uint8_t *)(local_rsp + (uint32_t)((uint32_t)(2 + 0xD)) * 1 + 0x2C) = (uint8_t)(Arg1);
        Arg1 = *(uint32_t *)(a4 + 0x100);
        Arg1 = (uint32_t)((Arg1) & ((uint32_t)(result)));
    }
    result = (uint32_t)((result) + ((uint32_t)(result)));
    Arg2 = (uint32_t)((2) + (16));
    if (((uint32_t)(Arg2 - 2)) < 32) goto loc_0096C6F0;
    if (((uint32_t)(Arg2 - 2)) != 32) goto loc_0096CAD6;
    goto loc_0096CADF;
loc_0096CAAA:
    result = local_r11;
    if (((uint32_t)(Arg2 - 2)) != 32) {
        Arg1 = result + 120;
        result = ExfReleasePushLockShared(Arg1, Arg2, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
    }
    result = KeAbPostRelease(result + 120, Arg2, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
    result = KeLeaveGuardedRegion(result + 120, Arg2, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
    goto loc_0096CB69;
loc_0096CAD6:
    result = ExfReleasePushLockShared(result + 120, Arg2, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
loc_0096CADF:
    result = KeAbPostRelease(result + 120, Arg2, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
    if (((uint32_t)(Arg2 - 2)) != 32) goto loc_0096CB0D;
    result = (*(uint64_t *)(gs_base + (0 + 0x188))) + (152);
    if ((*(uint64_t *)(result)) != result) {
        result = KiCheckForKernelApcDelivery(result + 120, Arg2, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
    }
    if (1 != 1) goto loc_0096CB45;
    if (v_stack_p20 == 0) goto loc_0096CB86;
loc_0096CB26:
    Arg1 = (*(uint64_t *)(v_stack_p20)) ^ (result);
    if (Arg1 >= 15) goto loc_0096CB86;
    if (Arg1 != 15) goto loc_0096CB26;
loc_0096CB45:
    *(uint64_t *)(v_stack_p10) = v_xmm0;
    *(uint64_t *)(v_stack_p10 + 0x10) = v_xmm1;
    *(uint32_t *)(v_stack_p10 + 0x20) = (uint32_t)((uint32_t)(v_stack_m30));
    goto loc_0096CB69;
loc_0096CB69:
loc_0096CB6B:
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000011ULL)));
loc_0096CB86:
    result = ObDereferenceDeviceMap(*(uint64_t *)(v_stack_m28 + 0x30), 1, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
    goto loc_0096CB45;
loc_0096CB95:
    goto loc_0096CB6B;
loc_0096CB9C:
    result = PsGetCurrentServerSiloGlobals(*(uint64_t *)(v_stack_m28 + 0x30), 1, (uint32_t)(*(uint32_t *)(result + 0x100)), a4);
    goto loc_0096C653;
loc_0096CBA6:
    result = (uint32_t)(0xC0000011ULL) + 792;
    if ((uint32_t)(0xC0000011ULL) == 0) { result = result; }
    local_rbx = (*(uint64_t *)(result)) & (-16);
    goto loc_0096C6B5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0096C5C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
