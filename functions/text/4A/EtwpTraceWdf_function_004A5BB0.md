# EtwpTraceWdf

- RVA: `0x004A5BB0`–`0x004A5C04` (길이 `84` bytes)
- VA: `0x00000001404A5BB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060904`
- 디코드: `19`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004A5BEC` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x004A5BF9` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x004A5BB4` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A5BB0  48 83 EC 58                     sub rsp, 0x58
004A5BB4  48 8B 05 85 4B 96 00            mov rax, qword ptr [rip + 0x964b85]
004A5BBB  48 33 C4                        xor rax, rsp
004A5BBE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
004A5BC3  0F B6 84 24 80 00 00 00         movzx eax, byte ptr [rsp + 0x80]
004A5BCB  83 64 24 3C 00                  and dword ptr [rsp + 0x3c], 0
004A5BD0  0D 00 18 50 00                  or eax, 0x501800
004A5BD5  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
004A5BDA  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
004A5BDF  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
004A5BE3  BA 01 00 00 00                  mov edx, 1
004A5BE8  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
004A5BEC  E8 5F F7 D8 FF                  call 0x140235350
004A5BF1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
004A5BF6  48 33 CC                        xor rcx, rsp
004A5BF9  E8 42 6A 20 00                  call 0x1406ac640
004A5BFE  48 83 C4 58                     add rsp, 0x58
004A5C02  C3                              ret
004A5C03  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpTraceWdf(__int64 a1, int a2, __int64 a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 9849733)) ^ (v_rsp);
    v_stack_m18 = result;
    result = (unsigned int)((a5) | (0x501800ULL));
    v_stack_m28 = a1;
    v_stack_m20 = a2;
    v_stack_m38 = (unsigned int)(result);
    result = EtwTraceKernelEvent(v_stack_m28, 1, a3, a4);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpTraceWdf(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x964B85)) ^ (local_rsp);
    v_stack_m18 = result;
    result = (uint32_t)((Arg5) | (0x501800ULL));
    v_stack_m28 = Arg1;
    v_stack_m20 = Arg2;
    v_stack_m38 = (uint32_t)(result);
    result = EtwTraceKernelEvent(v_stack_m28, 1, Arg3, Arg4);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A5BB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A5BB0[BB_004A5BB0]
  bb_004A5C03[BB_004A5C03]
```
