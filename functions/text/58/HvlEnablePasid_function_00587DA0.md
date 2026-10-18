# HvlEnablePasid

- RVA: `0x00587DA0`–`0x00587E3D` (길이 `157` bytes)
- VA: `0x0000000140587DA0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A02F8`
- 디코드: `38`개 명령, `157/157` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00587DEE` → [HvcallFastExtended](../31/HvcallFastExtended_function_003130E0.md) (function, `0x003130E0`)
- `0x00587E04` → [HvlpHvStatusIsInsufficientMemory](../30/HvlpHvStatusIsInsufficientMemory_function_00307BB0.md) (function, `0x00307BB0`)
- `0x00587E11` → [HvlpHandleInsufficientMemory](HvlpHandleInsufficientMemory_function_00584514.md) (function, `0x00584514`)
- `0x00587E25` → [HvlpHvToNtStatus](../30/HvlpHvToNtStatus_function_00307BD8.md) (function, `0x00307BD8`)
- `0x00587E32` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00587DA4` → RVA `0x00E0A740` (`.data`; read)
- `0x00587DF6` → RVA `0x00FC6A90` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00587DA0  48 83 EC 78                     sub rsp, 0x78
00587DA4  48 8B 05 95 29 88 00            mov rax, qword ptr [rip + 0x882995]
00587DAB  48 33 C4                        xor rax, rsp
00587DAE  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00587DB3  83 64 24 54 00                  and dword ptr [rsp + 0x54], 0
00587DB8  48 83 4C 24 40 FF               or qword ptr [rsp + 0x40], 0xffffffffffffffff
00587DBE  48 C7 44 24 30 A4 00 00 00      mov qword ptr [rsp + 0x30], 0xa4
00587DC7  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00587DCC  89 54 24 50                     mov dword ptr [rsp + 0x50], edx
00587DD0  C7 44 24 30 A4 00 01 00         mov dword ptr [rsp + 0x30], 0x100a4
00587DD8  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00587DDD  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00587DE2  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
00587DE7  45 33 C9                        xor r9d, r9d
00587DEA  45 8D 41 18                     lea r8d, [r9 + 0x18]
00587DEE  E8 ED B2 D8 FF                  call 0x1403130e0
00587DF3  4C 8B C0                        mov r8, rax
00587DF6  8B 05 94 EC A3 00               mov eax, dword ptr [rip + 0xa3ec94]
00587DFC  A8 02                           test al, 2
00587DFE  74 21                           je 0x140587e21
00587E00  41 0F B7 C8                     movzx ecx, r8w
00587E04  E8 A7 FD D7 FF                  call 0x140307bb0
00587E09  84 C0                           test al, al
00587E0B  74 14                           je 0x140587e21
00587E0D  41 0F B7 C8                     movzx ecx, r8w
00587E11  E8 FE C6 FF FF                  call 0x140584514
00587E16  85 C0                           test eax, eax
00587E18  79 BE                           jns 0x140587dd8
00587E1A  B8 9A 00 00 C0                  mov eax, 0xc000009a
00587E1F  EB 09                           jmp 0x140587e2a
00587E21  41 0F B7 C8                     movzx ecx, r8w
00587E25  E8 AE FD D7 FF                  call 0x140307bd8
00587E2A  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
00587E2F  48 33 CC                        xor rcx, rsp
00587E32  E8 09 48 12 00                  call 0x1406ac640
00587E37  48 83 C4 78                     add rsp, 0x78
00587E3B  C3                              ret
00587E3C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlEnablePasid(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m58;

    v_rsp = (v_rsp) - (120);
    result = (*(unsigned __int64 *)(v_rip + 8923541)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m48 = 164;
    v_stack_m30 = a1;
    v_stack_m28 = a2;
    v_stack_m48 = 0x100A4ULL;
loc_00587DD8:
    a4 = 0;
    result = HvcallFastExtended(v_stack_m48, v_stack_m38, a4 + 24, a4);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10742932)))) & (2)) == 0) goto loc_00587E21;
    result = HvlpHvStatusIsInsufficientMemory((unsigned __int16)(result), v_stack_m38, result, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00587E21;
    result = HvlpHandleInsufficientMemory((unsigned __int16)(result), v_stack_m38, result, a4);
    if (!sign_flag) goto loc_00587DD8;
    goto loc_00587E2A;
loc_00587E21:
    result = HvlpHvToNtStatus((unsigned __int16)(result), v_stack_m38, result, a4);
loc_00587E2A:
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m38, result, a4);
    v_rsp = (v_rsp) + (120);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlEnablePasid(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint32_t v_stack_m58;

    local_rsp = (local_rsp) - (120);
    result = (*(uint64_t *)(v_rip + 0x882995)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m48 = 164;
    v_stack_m30 = Arg1;
    v_stack_m28 = Arg2;
    v_stack_m48 = 0x100A4ULL;
loc_00587DD8:
    Arg4 = 0;
    result = HvcallFastExtended(v_stack_m48, v_stack_m38, Arg4 + 24, Arg4);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA3EC94)))) & (2)) == 0) goto loc_00587E21;
    result = HvlpHvStatusIsInsufficientMemory((uint16_t)(result), v_stack_m38, result, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00587E21;
    result = HvlpHandleInsufficientMemory((uint16_t)(result), v_stack_m38, result, Arg4);
    if (!sign_flag) goto loc_00587DD8;
    goto loc_00587E2A;
loc_00587E21:
    result = HvlpHvToNtStatus((uint16_t)(result), v_stack_m38, result, Arg4);
loc_00587E2A:
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m38, result, Arg4);
    local_rsp = (local_rsp) + (120);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00587DA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00587DA0[BB_00587DA0]
  bb_00587DD8[BB_00587DD8]
  bb_00587E00[BB_00587E00]
  bb_00587E0D[BB_00587E0D]
  bb_00587E1A[BB_00587E1A]
  bb_00587E21[BB_00587E21]
  bb_00587E2A[BB_00587E2A]
  bb_00587E3C[BB_00587E3C]
  bb_00587DA0 -->|flow| bb_00587DD8
  bb_00587DD8 -->|branch| bb_00587E21
  bb_00587DD8 -->|fallthrough| bb_00587E00
  bb_00587E00 -->|branch| bb_00587E21
  bb_00587E00 -->|fallthrough| bb_00587E0D
  bb_00587E0D -->|branch| bb_00587DD8
  bb_00587E0D -->|fallthrough| bb_00587E1A
  bb_00587E1A -->|branch| bb_00587E2A
  bb_00587E21 -->|flow| bb_00587E2A
```
