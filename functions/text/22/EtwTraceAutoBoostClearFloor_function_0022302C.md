# EtwTraceAutoBoostClearFloor

- RVA: `0x0022302C`–`0x002230C7` (길이 `155` bytes)
- VA: `0x000000014022302C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F638`
- 디코드: `34`개 명령, `155/155` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00223058` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledNoReportingNoInline](../4F/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledNoReportingNoInline_function_004F6A14.md) (function, `0x004F6A14`)
- `0x002230AE` → [EtwTraceSiloKernelEvent](EtwTraceSiloKernelEvent_function_002242A0.md) (function, `0x002242A0`)
- `0x002230BB` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_00210BCA](../21/Unknown_function_00210BCA.md) at `0x00210DEE`

### Static image references
- `0x00223032` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0022302C  40 53                           push rbx
0022302E  48 83 EC 60                     sub rsp, 0x60
00223032  48 8B 05 07 77 BE 00            mov rax, qword ptr [rip + 0xbe7707]
00223039  48 33 C4                        xor rax, rsp
0022303C  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00223041  8B 81 10 05 00 00               mov eax, dword ptr [rcx + 0x510]
00223047  48 8B D9                        mov rbx, rcx
0022304A  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0022304E  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00223053  44 89 44 24 3C                  mov dword ptr [rsp + 0x3c], r8d
00223058  E8 B7 39 2D 00                  call 0x1404f6a14
0022305D  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
00223062  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
00223067  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0022306C  F7 D8                           neg eax
0022306E  48 8B 8B 20 02 00 00            mov rcx, qword ptr [rbx + 0x220]
00223075  41 B9 00 10 00 A0               mov r9d, 0xa0001000
0022307B  1B D2                           sbb edx, edx
0022307D  C7 44 24 48 10 00 00 00         mov dword ptr [rsp + 0x48], 0x10
00223085  81 E2 00 04 00 00               and edx, 0x400
0022308B  41 B8 01 00 00 00               mov r8d, 1
00223091  81 C2 02 1A 60 00               add edx, 0x601a02
00223097  48 8B 89 F0 05 00 00            mov rcx, qword ptr [rcx + 0x5f0]
0022309E  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
002230A2  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
002230A7  66 C7 44 24 20 43 05            mov word ptr [rsp + 0x20], 0x543
002230AE  E8 ED 11 00 00                  call 0x1402242a0
002230B3  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
002230B8  48 33 CC                        xor rcx, rsp
002230BB  E8 80 95 48 00                  call 0x1406ac640
002230C0  48 83 C4 60                     add rsp, 0x60
002230C4  5B                              pop rbx
002230C5  C3                              ret
002230C6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceAutoBoostClearFloor(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m2C;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned __int16 v_stack_m48;

    v_rsp = (v_rsp) - (96);
    result = (*(unsigned __int64 *)(v_rip + 12482311)) ^ (v_rsp);
    v_stack_m18 = result;
    v_stack_m30 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 1296)));
    v_stack_m38 = a2;
    v_stack_m2C = a3;
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledNoReportingNoInline(a1, a2, a3, a4);
    v_stack_m28 = v_stack_m38;
    result = (unsigned int)(-(result));
    v_stack_m20 = 16;
    a2 = (unsigned int)((a2) & (0x400ULL));
    a2 = (unsigned int)((a2) + (0x601A02ULL));
    v_stack_m40 = (unsigned int)(a2);
    v_stack_m48 = 0x543ULL;
    result = EtwTraceSiloKernelEvent(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 544) + 1520), v_stack_m28, 1, (unsigned int)(0xA0001000ULL));
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m28, 1, (unsigned int)(0xA0001000ULL));
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceAutoBoostClearFloor(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m2C;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint16_t v_stack_m48;

    local_rsp = (local_rsp) - (96);
    result = (*(uint64_t *)(v_rip + 0xBE7707)) ^ (local_rsp);
    v_stack_m18 = result;
    v_stack_m30 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x510)));
    v_stack_m38 = Arg2;
    v_stack_m2C = Arg3;
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledNoReportingNoInline(Arg1, Arg2, Arg3, a4);
    v_stack_m28 = v_stack_m38;
    result = (uint32_t)(-(result));
    v_stack_m20 = 16;
    Arg2 = (uint32_t)((Arg2) & (0x400ULL));
    Arg2 = (uint32_t)((Arg2) + (0x601A02ULL));
    v_stack_m40 = (uint32_t)(Arg2);
    v_stack_m48 = 0x543ULL;
    result = EtwTraceSiloKernelEvent(*(uint64_t *)(*(uint64_t *)(arg1 + 0x220) + 0x5F0), v_stack_m28, 1, (uint32_t)(0xA0001000ULL));
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m28, 1, (uint32_t)(0xA0001000ULL));
    local_rsp = (local_rsp) + (96);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x220` | `64` | `R` |
| `Arg1` | `+ 0x510` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022302C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0022302C[BB_0022302C]
  bb_002230C6[BB_002230C6]
```
