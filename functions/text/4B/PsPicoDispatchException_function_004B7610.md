# PsPicoDispatchException

- RVA: `0x004B7610`–`0x004B7633` (길이 `35` bytes)
- VA: `0x00000001404B7610`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `9`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B7628` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiDeliverPicoExceptionForProbedPage](../67/MiDeliverPicoExceptionForProbedPage_function_00673DE4.md) at `0x00673E4B`
- [sub_006E9870](../6E/Unknown_function_006E9870.md) at `0x006E98C4`

### Static image references
- `0x004B7619` → RVA `0x00F06540` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7610  48 83 EC 38                     sub rsp, 0x38
004B7614  44 8A 4C 24 60                  mov r9b, byte ptr [rsp + 0x60]
004B7619  48 8B 05 20 EF A4 00            mov rax, qword ptr [rip + 0xa4ef20]
004B7620  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
004B7625  45 33 C9                        xor r9d, r9d
004B7628  E8 A3 34 20 00                  call 0x1406baad0
004B762D  48 83 C4 38                     add rsp, 0x38
004B7631  C3                              ret
004B7632  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsPicoDispatchException(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = a5;
    a4 = 0;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsPicoDispatchException(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = Arg5;
    Arg4 = 0;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7610[BB_004B7610]
  bb_004B7632[BB_004B7632]
```
