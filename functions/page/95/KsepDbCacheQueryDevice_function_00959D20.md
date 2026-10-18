# KsepDbCacheQueryDevice

- RVA: `0x00959D20`–`0x00959DE0` (길이 `192` bytes)
- VA: `0x0000000140959D20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000928B8`
- 디코드: `49`개 명령, `192/192` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00959D5D` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00959D6A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00959D76` → [CmpLockSiloKeyLockTrackerExclusive](../8F/CmpLockSiloKeyLockTrackerExclusive_function_008F9EF8.md) (function, `0x008F9EF8`)
- `0x00959D87` → [KsepCacheLookup](KsepCacheLookup_function_00959DE8.md) (function, `0x00959DE8`)
- `0x00959D9B` → [KsepCacheUnlock](KsepCacheUnlock_function_00959ECC.md) (function, `0x00959ECC`)
- `0x00959DD7` → [KsepDbCacheQueryDeviceData](../74/KsepDbCacheQueryDeviceData_function_00748CFC.md) (function, `0x00748CFC`)

### Direct callers
- [KseQueryDeviceData](KseQueryDeviceData_function_0095AFB0.md) at `0x0095B088`

### Static image references
- `0x00959D6F` → RVA `0x00E66CC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00959D5D` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00959D6A` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00959D20  4C 8B DC                        mov r11, rsp
00959D23  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00959D27  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00959D2B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00959D2F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00959D33  41 56                           push r14
00959D35  48 81 EC 80 00 00 00            sub rsp, 0x80
00959D3C  33 C0                           xor eax, eax
00959D3E  49 8B E8                        mov rbp, r8
00959D41  4C 8B F2                        mov r14, rdx
00959D44  89 44 24 34                     mov dword ptr [rsp + 0x34], eax
00959D48  48 8B D9                        mov rbx, rcx
00959D4B  33 D2                           xor edx, edx
00959D4D  49 8D 4B A8                     lea rcx, [r11 - 0x58]
00959D51  49 8B F1                        mov rsi, r9
00959D54  44 8D 40 44                     lea r8d, [rax + 0x44]
00959D58  BF 25 02 00 C0                  mov edi, 0xc0000225
00959D5D  E8 DE CE D6 FF                  call 0x1406c6c40
00959D62  48 8B D3                        mov rdx, rbx
00959D65  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
00959D6A  E8 11 0A AD FF                  call 0x14042a780
00959D6F  48 8B 0D 52 CF 50 00            mov rcx, qword ptr [rip + 0x50cf52]
00959D76  E8 7D 01 FA FF                  call 0x1408f9ef8
00959D7B  48 8B 0D 46 CF 50 00            mov rcx, qword ptr [rip + 0x50cf46]
00959D82  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00959D87  E8 5C 00 00 00                  call 0x140959de8
00959D8C  48 8B C8                        mov rcx, rax
00959D8F  48 85 C0                        test rax, rax
00959D92  75 2D                           jne 0x140959dc1
00959D94  48 8B 0D 2D CF 50 00            mov rcx, qword ptr [rip + 0x50cf2d]
00959D9B  E8 2C 01 00 00                  call 0x140959ecc
00959DA0  4C 8D 9C 24 80 00 00 00         lea r11, [rsp + 0x80]
00959DA8  8B C7                           mov eax, edi
00959DAA  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
00959DAE  49 8B 6B 18                     mov rbp, qword ptr [r11 + 0x18]
00959DB2  49 8B 73 20                     mov rsi, qword ptr [r11 + 0x20]
00959DB6  49 8B 7B 28                     mov rdi, qword ptr [r11 + 0x28]
00959DBA  49 8B E3                        mov rsp, r11
00959DBD  41 5E                           pop r14
00959DBF  C3                              ret
00959DC0  CC                              int3
00959DC1  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00959DC9  4C 8B CE                        mov r9, rsi
00959DCC  4C 8B C5                        mov r8, rbp
00959DCF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00959DD4  49 8B D6                        mov rdx, r14
00959DD7  E8 20 EF DE FF                  call 0x140748cfc
00959DDC  8B F8                           mov edi, eax
00959DDE  EB B4                           jmp 0x140959d94
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KsepDbCacheQueryDevice(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (128);
    result = 0;
    v_stack_m54 = 0;
    a2 = 0;
    result = memset(v_rsp - 88, a2, result + 68, a4);
    result = RtlInitUnicodeString(v_stack_m30, a1, result + 68, a4);
    result = CmpLockSiloKeyLockTrackerExclusive(*(unsigned __int64 *)(v_rip + 5295954), a1, result + 68, a4);
    result = KsepCacheLookup(*(unsigned __int64 *)(v_rip + 5295942), v_stack_m58, result + 68, a4);
    if (result != 0) goto loc_00959DC1;
loc_00959D94:
    result = KsepCacheUnlock(*(unsigned __int64 *)(v_rip + 5295917), v_stack_m58, result + 68, a4);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000225ULL)));
loc_00959DC1:
    v_stack_m60 = a5;
    result = KsepDbCacheQueryDeviceData(*(unsigned __int64 *)(v_rip + 5295917), 0, *(unsigned __int64 *)(v_stack_m8 + 24), *(unsigned __int64 *)(v_stack_m8 + 32));
    goto loc_00959D94;
}
```

## 5. (Beta) C Style

```c
int64_t KsepDbCacheQueryDevice(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m30;
    uint32_t v_stack_m54;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (128);
    result = 0;
    v_stack_m54 = 0;
    Arg2 = 0;
    result = memset(local_rsp - 88, Arg2, result + 68, Arg4);
    result = RtlInitUnicodeString(v_stack_m30, Arg1, result + 68, Arg4);
    result = CmpLockSiloKeyLockTrackerExclusive(*(uint64_t *)(v_rip + 0x50CF52), Arg1, result + 68, Arg4);
    result = KsepCacheLookup(*(uint64_t *)(v_rip + 0x50CF46), v_stack_m58, result + 68, Arg4);
    if (result != 0) goto loc_00959DC1;
loc_00959D94:
    result = KsepCacheUnlock(*(uint64_t *)(v_rip + 0x50CF2D), v_stack_m58, result + 68, Arg4);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000225ULL)));
loc_00959DC1:
    v_stack_m60 = Arg5;
    result = KsepDbCacheQueryDeviceData(*(uint64_t *)(v_rip + 0x50CF2D), 0, *(uint64_t *)(v_stack_m8 + 0x18), *(uint64_t *)(v_stack_m8 + 0x20));
    goto loc_00959D94;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00959D20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00959D20[BB_00959D20]
  bb_00959D94[BB_00959D94]
  bb_00959DC0[BB_00959DC0]
  bb_00959DC1[BB_00959DC1]
  bb_00959D20 -->|branch| bb_00959DC1
  bb_00959D20 -->|fallthrough| bb_00959D94
  bb_00959DC0 -->|flow| bb_00959DC1
  bb_00959DC1 -->|branch| bb_00959D94
```
