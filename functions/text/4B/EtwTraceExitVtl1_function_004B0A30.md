# EtwTraceExitVtl1

- RVA: `0x004B0A30`–`0x004B0A9A` (길이 `106` bytes)
- VA: `0x00000001404B0A30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B3A94`
- 디코드: `22`개 명령, `106/106` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B0A82` → [EtwTraceKernelEvent](../23/EtwTraceKernelEvent_function_00235350.md) (function, `0x00235350`)
- `0x004B0A8F` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_002361D4](../23/Unknown_function_002361D4.md) at `0x00236245`

### Static image references
- `0x004B0A34` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B0A30  48 83 EC 58                     sub rsp, 0x58
004B0A34  48 8B 05 05 9D 95 00            mov rax, qword ptr [rip + 0x959d05]
004B0A3B  48 33 C4                        xor rax, rsp
004B0A3E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
004B0A43  83 64 24 44 00                  and dword ptr [rsp + 0x44], 0
004B0A48  48 8D 44 24 30                  lea rax, [rsp + 0x30]
004B0A4D  66 89 54 24 32                  mov word ptr [rsp + 0x32], dx
004B0A52  41 B9 4A 05 00 00               mov r9d, 0x54a
004B0A58  66 89 4C 24 30                  mov word ptr [rsp + 0x30], cx
004B0A5D  BA 01 00 00 00                  mov edx, 1
004B0A62  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
004B0A67  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
004B0A6C  41 B8 08 00 00 A0               mov r8d, 0xa0000008
004B0A72  C7 44 24 40 04 00 00 00         mov dword ptr [rsp + 0x40], 4
004B0A7A  C7 44 24 20 02 19 50 00         mov dword ptr [rsp + 0x20], 0x501902
004B0A82  E8 C9 48 D8 FF                  call 0x140235350
004B0A87  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
004B0A8C  48 33 CC                        xor rcx, rsp
004B0A8F  E8 AC BB 1F 00                  call 0x1406ac640
004B0A94  48 83 C4 58                     add rsp, 0x58
004B0A98  C3                              ret
004B0A99  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTraceExitVtl1(unsigned __int16 a1, unsigned __int16 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m14;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int16 v_stack_m26;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    result = (*(unsigned __int64 *)(v_rip + 9805061)) ^ (v_rsp);
    v_stack_m10 = result;
    v_stack_m26 = a2;
    v_stack_m28 = a1;
    v_stack_m20 = v_stack_m28;
    v_stack_m18 = 4;
    v_stack_m38 = 0x501902ULL;
    result = EtwTraceKernelEvent(v_stack_m20, 1, (unsigned int)(0xA0000008ULL), (unsigned int)(0x54AULL));
    a1 = (v_stack_m10) ^ (v_rsp);
    result = _security_check_cookie(a1, 1, (unsigned int)(0xA0000008ULL), (unsigned int)(0x54AULL));
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTraceExitVtl1(uint16_t Arg1, uint16_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m14;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint16_t v_stack_m26;
    uint64_t v_stack_m28;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    result = (*(uint64_t *)(v_rip + 0x959D05)) ^ (local_rsp);
    v_stack_m10 = result;
    v_stack_m26 = Arg2;
    v_stack_m28 = Arg1;
    v_stack_m20 = v_stack_m28;
    v_stack_m18 = 4;
    v_stack_m38 = 0x501902ULL;
    result = EtwTraceKernelEvent(v_stack_m20, 1, (uint32_t)(0xA0000008ULL), (uint32_t)(0x54AULL));
    Arg1 = (v_stack_m10) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 1, (uint32_t)(0xA0000008ULL), (uint32_t)(0x54AULL));
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B0A30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B0A30[BB_004B0A30]
  bb_004B0A99[BB_004B0A99]
```
